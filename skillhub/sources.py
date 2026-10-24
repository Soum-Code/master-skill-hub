"""Discovery sources. Each returns (hits, status). A hit is a GitHub repo mentioned somewhere:
    {"repo": "owner/name", "source": "hackernews", "url": "<where it was mentioned>", "note": "...", "weight": 1.0}
Every source is best-effort: failure is reported in the weekly report, never raised.
All text pulled from the internet is treated as data; we only regex GitHub slugs out of it."""
from __future__ import annotations

import base64
import datetime as dt
import html
import json
import os
import re
import time
import urllib.parse
import xml.etree.ElementTree as ET

from .net import GitHub, HttpError, get_json, get_text, github_repos_in, http

Hit = dict
REPO_META: dict[str, dict] = {}  # lower(slug) -> GitHub API repo object, filled by search results


def _remember(it: dict) -> None:
    REPO_META[it["full_name"].lower()] = it


def _hit(repo: str, source: str, url: str, note: str = "", weight: float = 1.0) -> Hit:
    return {"repo": repo, "source": source, "url": url, "note": note[:140], "weight": weight}


def _days_ago(n: int) -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=n)


def _strip_html(s: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", " ", s or ""))


# ---------------------------------------------------------------- GitHub-native
def github_topics(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    c = cfg.get("github_search", {})
    since, since90 = _days_ago(14).strftime("%Y-%m-%d"), _days_ago(90).strftime("%Y-%m-%d")
    hits: list[Hit] = []
    queries: list[tuple[str, str]] = []
    for t in c.get("topics", []):
        r, e = c.get("rising", {}), c.get("established", {})
        queries.append((f"topic:{t} created:>={since90} stars:>={r.get('min_stars', 15)}", f"topic:{t} rising"))
        queries.append((f"topic:{t} pushed:>={since} stars:>={e.get('min_stars', 300)}", f"topic:{t} established"))
    for pid, p in packs.items():
        for q in (p.get("queries") or [])[:2]:
            queries.append((f'"{q}" in:name,description,readme pushed:>={since90} stars:>=10', f"pack:{pid}"))
    n_err = 0
    for q, note in queries:
        if len(hits) >= c.get("max_total", 120) * 4:
            break
        try:
            for it in gh.search_repos(q, per_page=c.get("rising", {}).get("per_topic", 15)):
                _remember(it)
                hits.append(_hit(it["full_name"], "github-search", it["html_url"], note, 1.0))
        except HttpError as e:
            n_err += 1
            if e.status in (403, 422) and n_err >= 3:
                return hits, f"partial: {len(hits)} hits, stopped after repeated {e.status}"
    return hits, f"ok: {len(queries)} searches, {len(hits)} hits" + (f", {n_err} errors" if n_err else "")


def watchlist(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    hits = [_hit(r, "watchlist", f"https://github.com/{r}", "watchlist", 2.0) for r in cfg.get("watchlist", [])]
    return hits, f"ok: {len(hits)} repos"


def awesome_lists(cfg: dict, packs: dict, gh: GitHub, seen: dict) -> tuple[list[Hit], str]:
    hits: list[Hit] = []
    base = seen.setdefault("awesome_links", {})
    notes = []
    for repo in cfg.get("awesome_lists", []):
        try:
            text = get_text(f"https://raw.githubusercontent.com/{repo}/HEAD/README.md", headers={"Accept": "text/plain"})
        except HttpError as e:
            notes.append(f"{repo}: HTTP {e.status}")
            continue
        links = [l for l in github_repos_in(text) if l.lower() != repo.lower()]
        known = set(base.get(repo, []))
        new = [l for l in links if l not in known]
        if not known:  # first sight: take the prominent ones only
            new = new[:60]
        base[repo] = sorted(known | set(links))[-3000:]
        hits += [_hit(l, "awesome-list", f"https://github.com/{repo}", repo, 1.2) for l in new]
        notes.append(f"{repo}: {len(new)} new")
    return hits, "ok: " + "; ".join(notes) if notes else "ok: none"


# ---------------------------------------------------------------- community sources
def hackernews(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    c = cfg["sources"]["hackernews"]
    ts = int(_days_ago(c.get("days", 10)).timestamp())
    hits: list[Hit] = []
    for q in c.get("queries", []):
        url = "https://hn.algolia.com/api/v1/search_by_date?" + urllib.parse.urlencode(
            {"query": q, "tags": "story", "numericFilters": f"created_at_i>{ts}", "hitsPerPage": 40})
        for h in get_json(url).get("hits", []):
            blob = " ".join([h.get("url") or "", h.get("story_text") or "", h.get("title") or ""])
            for repo in github_repos_in(blob):
                hits.append(_hit(repo, "hackernews", f"https://news.ycombinator.com/item?id={h.get('objectID')}",
                                 f"{h.get('points', 0)} pts: {h.get('title', '')}", 1.0 + min((h.get("points") or 0) / 200, 2)))
    return hits, f"ok: {len(hits)} hits"


def devto(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    c = cfg["sources"]["devto"]
    hits: list[Hit] = []
    for tag in c.get("tags", []):
        arts = get_json(f"https://dev.to/api/articles?tag={tag}&top={c.get('top_days', 7)}&per_page=15")
        for a in arts[:8]:
            try:
                body = get_json(f"https://dev.to/api/articles/{a['id']}").get("body_markdown", "")
            except HttpError:
                continue
            for repo in github_repos_in(body):
                hits.append(_hit(repo, "dev.to", a.get("url", ""), a.get("title", ""), 1.0 + min(a.get("positive_reactions_count", 0) / 100, 2)))
    return hits, f"ok: {len(hits)} hits"


def lobsters(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    hits: list[Hit] = []
    kw = re.compile(r"claude|skill|agent|mcp|llm|copilot|cursor", re.I)
    for tag in cfg["sources"]["lobsters"].get("tags", []):
        for it in get_json(f"https://lobste.rs/t/{tag}.json"):
            if kw.search(it.get("title", "")):
                for repo in github_repos_in((it.get("url") or "") + " " + (it.get("description") or "")):
                    hits.append(_hit(repo, "lobsters", it.get("comments_url", ""), it.get("title", ""), 1.0))
    return hits, f"ok: {len(hits)} hits"


def mastodon(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    c = cfg["sources"]["mastodon"]
    hits: list[Hit] = []
    for tag in c.get("hashtags", []):
        data = get_json(f"{c['instance'].rstrip('/')}/api/v1/timelines/tag/{urllib.parse.quote(tag)}?limit=40")
        for st in data:
            blob = _strip_html(st.get("content", "")) + " " + ((st.get("card") or {}).get("url") or "")
            for repo in github_repos_in(blob):
                hits.append(_hit(repo, "mastodon", st.get("url", ""), f"#{tag}", 0.8))
    return hits, f"ok: {len(hits)} hits"


def npm(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    hits: list[Hit] = []
    for kw in cfg["sources"]["npm"].get("keywords", []):
        data = get_json("https://registry.npmjs.org/-/v1/search?" + urllib.parse.urlencode({"text": f"keywords:{kw}", "size": 40}))
        for o in data.get("objects", []):
            pkg = o.get("package", {})
            links = pkg.get("links", {})
            for repo in github_repos_in((links.get("repository") or "") + " " + (links.get("homepage") or "")):
                hits.append(_hit(repo, "npm", links.get("npm", ""), pkg.get("name", ""), 0.9))
    return hits, f"ok: {len(hits)} hits"


def reddit(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    c = cfg["sources"]["reddit"]
    cid, sec = os.environ.get("REDDIT_CLIENT_ID"), os.environ.get("REDDIT_CLIENT_SECRET")
    hits: list[Hit] = []
    ua = "master-skill-hub/1.0 (discovery; read-only)"
    if cid and sec:
        tok = json.loads(http("https://www.reddit.com/api/v1/access_token", data=b"grant_type=client_credentials", method="POST",
                              headers={"Authorization": "Basic " + base64.b64encode(f"{cid}:{sec}".encode()).decode(),
                                       "User-Agent": ua, "Content-Type": "application/x-www-form-urlencoded"})[0])["access_token"]
        for sub in c.get("subreddits", []):
            data = get_json(f"https://oauth.reddit.com/r/{sub}/top?t=week&limit=50", headers={"Authorization": f"bearer {tok}", "User-Agent": ua})
            for ch in data["data"]["children"]:
                d = ch["data"]
                for repo in github_repos_in(f"{d.get('url', '')} {d.get('selftext', '')}"):
                    hits.append(_hit(repo, "reddit", "https://reddit.com" + d.get("permalink", ""), d.get("title", ""), 1.0 + min(d.get("score", 0) / 300, 2)))
        return hits, f"ok (oauth): {len(hits)} hits"
    blocked = 0
    for sub in c.get("subreddits", []):  # anonymous RSS: usually blocked from cloud IPs, so just try
        try:
            xml = get_text(f"https://www.reddit.com/r/{sub}/top/.rss?t=week", headers={"User-Agent": ua, "Accept": "application/atom+xml"}, retries=0)
            root = ET.fromstring(xml)
            for e in root.iter("{http://www.w3.org/2005/Atom}entry"):
                content = "".join(x.text or "" for x in e.iter("{http://www.w3.org/2005/Atom}content"))
                title = "".join(x.text or "" for x in e.iter("{http://www.w3.org/2005/Atom}title"))
                for repo in github_repos_in(_strip_html(content)):
                    hits.append(_hit(repo, "reddit", f"https://reddit.com/r/{sub}", title, 0.9))
        except Exception:
            blocked += 1
        time.sleep(1)
    if blocked == len(c.get("subreddits", [])):
        return hits, "blocked: Reddit refuses anonymous cloud requests (add REDDIT_CLIENT_ID/REDDIT_CLIENT_SECRET to enable)"
    return hits, f"partial (anonymous rss): {len(hits)} hits, {blocked} blocked"


def bluesky(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    handle, pw = os.environ.get("BSKY_HANDLE"), os.environ.get("BSKY_APP_PASSWORD")
    if not (handle and pw):
        return [], "skipped: no BSKY_HANDLE / BSKY_APP_PASSWORD secret"
    sess = json.loads(http("https://bsky.social/xrpc/com.atproto.server.createSession", method="POST",
                           data=json.dumps({"identifier": handle, "password": pw}).encode(),
                           headers={"Content-Type": "application/json"})[0])
    h = {"Authorization": "Bearer " + sess["accessJwt"]}
    hits: list[Hit] = []
    for q in cfg["sources"]["bluesky"].get("queries", []):
        data = get_json("https://bsky.social/xrpc/app.bsky.feed.searchPosts?" + urllib.parse.urlencode({"q": q, "limit": 50, "sort": "latest"}), headers=h)
        for p in data.get("posts", []):
            rec = p.get("record", {})
            blob = rec.get("text", "") + " " + json.dumps(rec.get("facets", [])) + " " + json.dumps(p.get("embed", {}))
            for repo in github_repos_in(blob):
                hits.append(_hit(repo, "bluesky", f"https://bsky.app/profile/{p['author']['handle']}", q, 0.9 + min(p.get("likeCount", 0) / 100, 1)))
    return hits, f"ok: {len(hits)} hits"


def youtube(cfg: dict, packs: dict, gh: GitHub) -> tuple[list[Hit], str]:
    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        return [], "skipped: no YOUTUBE_API_KEY secret"
    hits: list[Hit] = []
    after = _days_ago(14).strftime("%Y-%m-%dT%H:%M:%SZ")
    for q in cfg["sources"]["youtube"].get("queries", []):
        s = get_json("https://www.googleapis.com/youtube/v3/search?" + urllib.parse.urlencode(
            {"part": "snippet", "q": q, "type": "video", "order": "date", "publishedAfter": after, "maxResults": 20, "key": key}))
        ids = ",".join(i["id"]["videoId"] for i in s.get("items", []) if i.get("id", {}).get("videoId"))
        if not ids:
            continue
        v = get_json("https://www.googleapis.com/youtube/v3/videos?" + urllib.parse.urlencode({"part": "snippet", "id": ids, "key": key}))
        for it in v.get("items", []):
            sn = it["snippet"]
            for repo in github_repos_in(sn.get("description", "")):
                hits.append(_hit(repo, "youtube", f"https://youtu.be/{it['id']}", sn.get("title", ""), 0.9))
    return hits, f"ok: {len(hits)} hits"


def github_issues(cfg: dict, packs: dict, gh: GitHub, slug: str) -> tuple[list[Hit], str, list[dict]]:
    """User submissions (submit-skill) and wishes (skill-request) on the hub repo itself."""
    hits: list[Hit] = []
    requests: list[dict] = []
    try:
        for label in ("submit-skill", "skill-request"):
            for iss in gh.issues(slug, label, per_page=20):
                if iss.get("pull_request"):
                    continue
                body = f"{iss.get('title', '')}\n{iss.get('body') or ''}"
                if label == "submit-skill":
                    for repo in github_repos_in(body)[:5]:
                        hits.append(_hit(repo, "user-submission", iss["html_url"], iss.get("title", ""), 3.0))
                else:
                    q = re.sub(r"\s+", " ", iss.get("title", ""))[:120]
                    requests.append({"issue": iss["html_url"], "query": q})
                    try:
                        for it in gh.search_repos(f'{q} claude skill in:name,description,readme stars:>=5', per_page=5):
                            _remember(it)
                            hits.append(_hit(it["full_name"], "skill-request", iss["html_url"], q, 2.0))
                    except HttpError:
                        pass
    except HttpError as e:
        return hits, f"failed: HTTP {e.status}", requests
    return hits, f"ok: {len(hits)} hits, {len(requests)} requests", requests
