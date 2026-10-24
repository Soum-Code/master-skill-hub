"""HTTP helpers: JSON GET/POST with retries, GitHub API client, GitHub-URL extraction."""
from __future__ import annotations

import json
import os
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "master-skill-hub-discovery/1.0 (+https://github.com/Soum-Code/master-skill-hub)"

# github.com/<owner>/<repo> but not site sections
_GH_RE = re.compile(r"https?://(?:www\.)?github\.com/([A-Za-z0-9][A-Za-z0-9-]{0,38})/([A-Za-z0-9_.-]{1,100})", re.I)
_NOT_OWNERS = {"sponsors", "orgs", "topics", "features", "about", "login", "join", "settings", "marketplace", "pricing",
               "enterprise", "collections", "trending", "readme", "security", "apps", "notifications", "explore",
               "issues", "pulls", "search", "site", "customer-stories", "resources", "solutions", "contact"}


def github_repos_in(text: str) -> list[str]:
    """Distinct owner/repo slugs mentioned in free text (order preserved)."""
    out: list[str] = []
    for m in _GH_RE.finditer(text or ""):
        owner, repo = m.group(1), m.group(2)
        repo = re.sub(r"\.git$", "", repo).rstrip(".")
        if owner.lower() in _NOT_OWNERS or not repo or repo.lower() in ("issues", "pulls", "wiki", "actions", "releases"):
            continue
        slug = f"{owner}/{repo}"
        if slug.lower() not in {s.lower() for s in out}:
            out.append(slug)
    return out


class HttpError(Exception):
    def __init__(self, status: int, url: str, body: str = ""):
        super().__init__(f"HTTP {status} for {url}")
        self.status, self.url, self.body = status, url, body


def http(url: str, *, headers: dict | None = None, data: bytes | None = None, method: str | None = None,
         timeout: int = 30, retries: int = 2, limit: int = 8 * 1024 * 1024) -> tuple[bytes, dict]:
    h = {"User-Agent": UA, "Accept": "application/json"}
    h.update(headers or {})
    last: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, data=data, headers=h, method=method)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read(limit), dict(r.headers)
        except urllib.error.HTTPError as e:
            body = e.read(2000).decode("utf-8", "replace") if e.fp else ""
            if e.code in (429, 502, 503, 504) or (e.code == 403 and "rate limit" in body.lower()):
                wait = int(e.headers.get("Retry-After", "0") or 0)
                reset = e.headers.get("X-RateLimit-Reset")
                if not wait and reset and e.headers.get("X-RateLimit-Remaining") == "0":
                    wait = max(0, min(int(reset) - int(time.time()), 90))
                last = HttpError(e.code, url, body)
                if attempt < retries:
                    time.sleep(min(wait or (3 * (attempt + 1)), 90))
                    continue
            raise HttpError(e.code, url, body)
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            last = e
            if attempt < retries:
                time.sleep(2 * (attempt + 1))
                continue
    raise last if last else RuntimeError("request failed")


def get_json(url: str, **kw):
    body, _ = http(url, **kw)
    return json.loads(body.decode("utf-8", "replace"))


def get_text(url: str, **kw) -> str:
    kw.setdefault("headers", {})["Accept"] = kw.get("headers", {}).get("Accept", "text/plain,*/*")
    body, _ = http(url, **kw)
    return body.decode("utf-8", "replace")


def local_gh_token() -> str | None:
    """Local developer convenience only: the token the `gh` CLI already holds. Never used in Actions."""
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=10)
        tok = out.stdout.strip()
        return tok or None
    except Exception:
        return None


class GitHub:
    def __init__(self, token: str | None = None):
        self.token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or local_gh_token()
        self.calls = 0
        self._last_search = 0.0

    def _h(self) -> dict:
        h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if self.token:
            h["Authorization"] = f"Bearer {self.token}"
        return h

    def api(self, path: str, params: dict | None = None):
        url = "https://api.github.com" + path
        if params:
            url += "?" + urllib.parse.urlencode(params)
        self.calls += 1
        return get_json(url, headers=self._h())

    def search_repos(self, q: str, per_page: int = 20, sort: str = "stars"):
        # search API: 30 req/min authenticated; stay well under it
        wait = 2.4 - (time.time() - self._last_search)
        if wait > 0:
            time.sleep(wait)
        self._last_search = time.time()
        res = self.api("/search/repositories", {"q": q, "sort": sort, "order": "desc", "per_page": per_page})
        return res.get("items", [])

    def repo(self, slug: str) -> dict:
        return self.api(f"/repos/{slug}")

    def head_sha(self, slug: str, branch: str | None = None) -> str:
        self.calls += 1
        h = self._h()
        h["Accept"] = "application/vnd.github.sha"
        body, _ = http(f"https://api.github.com/repos/{slug}/commits/{branch or 'HEAD'}", headers=h, limit=1024)
        return body.decode().strip()

    def issues(self, slug: str, labels: str, state: str = "open", per_page: int = 30):
        return self.api(f"/repos/{slug}/issues", {"labels": labels, "state": state, "per_page": per_page})
