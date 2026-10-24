#!/usr/bin/env python3
"""install.py - fetch a skill from GitHub at an EXACT commit, vet it, and (only with --apply) install it.

    python install.py owner/repo --path skills/my-skill --commit <40-hex sha> [--expect-tree <sha256>] [--apply]
    python install.py owner/repo --list                      # list skill folders at the latest commit

Safety properties
  * Pinned: files come from the zip of one commit SHA, never from a moving branch.
  * Hash-checked: if --expect-tree is given (the registry records it), any difference aborts.
  * Vetted: vet.py runs on the downloaded bytes before anything touches disk.
  * Contained: zip entries are never extracted with extractall; paths are normalised, symlinks and
    traversal are rejected, sizes are capped, and the destination must stay inside the skills dir.
  * Dry-run by default.
Python stdlib only.
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import json
import os
import posixpath
import re
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("vet_mod", HERE / "vet.py")
vet = importlib.util.module_from_spec(_spec)  # type: ignore[arg-type]
_spec.loader.exec_module(vet)  # type: ignore[union-attr]

UA = {"User-Agent": "skill-hub-installer/1"}
MAX_ZIP_BYTES = 200 * 1024 * 1024
MAX_UNZIPPED = 400 * 1024 * 1024
MAX_FILE = 20 * 1024 * 1024
MAX_ENTRIES = 60000
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SKIP_SEGMENTS = {"node_modules", ".git"}


def _get(url: str, headers: dict | None = None, limit: int = 8 * 1024 * 1024, timeout: int = 60) -> bytes:
    h = dict(UA)
    h.update(headers or {})
    with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=timeout) as r:
        data = r.read(limit + 1)
    if len(data) > limit:
        raise ValueError(f"response from {url} exceeds {limit} bytes")
    return data


def commit_sha(repo: str, ref: str | None = None, token: str | None = None) -> str:
    """Resolve a ref (default branch when None) to a full commit SHA via the GitHub API."""
    if not REPO_RE.match(repo):
        raise ValueError("bad repo name")
    h = {"Accept": "application/vnd.github.sha"}
    token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    target = ref or "HEAD"
    sha = _get(f"https://api.github.com/repos/{repo}/commits/{target}", h, limit=1024).decode().strip()
    if not SHA_RE.match(sha):
        raise ValueError(f"unexpected sha response: {sha[:60]!r}")
    return sha


def download_zip(repo: str, sha: str) -> bytes:
    if not REPO_RE.match(repo) or not SHA_RE.match(sha):
        raise ValueError("repo must be owner/name and sha a 40-hex commit")
    return _get(f"https://codeload.github.com/{repo}/zip/{sha}", limit=MAX_ZIP_BYTES, timeout=180)


def _entries(zip_bytes: bytes):
    """Yield (relative_path, bytes_or_None, is_symlink). Paths are relative to the repo root."""
    z = zipfile.ZipFile(io.BytesIO(zip_bytes))
    infos = z.infolist()
    if len(infos) > MAX_ENTRIES:
        raise ValueError("zip has too many entries")
    total = 0
    for info in infos:
        if info.is_dir():
            continue
        name = info.filename.replace("\\", "/")
        parts = name.split("/", 1)
        if len(parts) < 2:
            continue
        rel = posixpath.normpath(parts[1])
        if rel.startswith(("/", "../")) or rel == ".." or "/../" in rel:
            yield rel, None, True  # traversal -> treated as hostile
            continue
        mode = (info.external_attr >> 16) & 0o170000
        if mode == 0o120000:
            yield rel, None, True
            continue
        if info.file_size > MAX_FILE:
            yield rel, b"\x00" * (vet.MAX_FILE_BYTES + 1), False
            continue
        total += info.file_size
        if total > MAX_UNZIPPED:
            raise ValueError("zip expands beyond the size cap")
        yield rel, z.read(info), False


def skill_dirs(zip_bytes: bytes) -> dict[str, dict]:
    """Map skill-folder path -> {'files': {rel: bytes}, 'symlinks': [rel]} for every folder with a SKILL.md."""
    files: dict[str, bytes] = {}
    links: list[str] = []
    for rel, data, is_link in _entries(zip_bytes):
        if any(seg in SKIP_SEGMENTS for seg in rel.split("/")):
            continue
        if is_link:
            links.append(rel)
        elif data is not None:
            files[rel] = data
    roots = sorted({posixpath.dirname(p) for p in files if posixpath.basename(p) == "SKILL.md"})
    out: dict[str, dict] = {}
    for root in roots:
        prefix = root + "/" if root else ""
        out[root or "."] = {
            "files": {p[len(prefix):]: b for p, b in files.items() if p.startswith(prefix)},
            "symlinks": [p[len(prefix):] for p in links if p.startswith(prefix)],
        }
    return out


def repo_size_kb(repo: str, token: str | None = None) -> int:
    h = {"Accept": "application/vnd.github+json"}
    token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return int(json.loads(_get(f"https://api.github.com/repos/{repo}", h, limit=1 << 20)).get("size", 0))


def tree_skill_dirs(repo: str, sha: str, max_dirs: int = 60, token: str | None = None) -> dict[str, dict]:
    """Same result as skill_dirs(), but via the git tree + raw file downloads. Used for huge repositories
    where zipping the whole thing would be wasteful; only the skill folders are fetched."""
    import concurrent.futures
    import urllib.parse
    h = {"Accept": "application/vnd.github+json"}
    token = token or os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    tree = json.loads(_get(f"https://api.github.com/repos/{repo}/git/trees/{sha}?recursive=1", h, limit=64 << 20))
    if tree.get("truncated"):
        raise ValueError("git tree too large to list")
    blobs = {e["path"]: e for e in tree.get("tree", []) if e.get("type") == "blob"
             and not any(seg in SKIP_SEGMENTS for seg in e["path"].split("/"))}
    roots = sorted({posixpath.dirname(p) for p in blobs if posixpath.basename(p) == "SKILL.md"})[:max_dirs]
    todo: list[tuple[str, str]] = []  # (root, path)
    links: dict[str, list[str]] = {}
    for root in roots:
        prefix = root + "/" if root else ""
        paths = [p for p in blobs if p.startswith(prefix)]
        if len(paths) > vet.MAX_FILES + 50:
            paths = paths[: vet.MAX_FILES + 50]
        for p in paths:
            if blobs[p].get("mode") == "120000":
                links.setdefault(root, []).append(p[len(prefix):])
            else:
                todo.append((root, p))

    def fetch(item):
        root, path = item
        if blobs[path].get("size", 0) > MAX_FILE:
            return root, path, b"\x00" * (vet.MAX_FILE_BYTES + 1)
        url = f"https://raw.githubusercontent.com/{repo}/{sha}/" + urllib.parse.quote(path)
        return root, path, _get(url, limit=MAX_FILE + 1)

    out: dict[str, dict] = {(r or "."): {"files": {}, "symlinks": links.get(r, [])} for r in roots}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for root, path, data in ex.map(fetch, todo):
            prefix = root + "/" if root else ""
            out[root or "."]["files"][path[len(prefix):]] = data
    return out


def fetch_skill_dirs(repo: str, sha: str) -> dict[str, dict]:
    """Zip for normal repos, tree+raw for very large ones. Both yield identical file sets."""
    try:
        big = repo_size_kb(repo) > 120_000
    except Exception:
        big = False
    return tree_skill_dirs(repo, sha) if big else skill_dirs(download_zip(repo, sha))


def vet_skill(entry: dict, dirname: str) -> dict:
    return vet.vet_blobs(entry["files"], entry["symlinks"], dirname=dirname)


def default_dest() -> Path:
    return Path(os.path.expanduser("~")) / ".claude" / "skills"


def install(repo: str, path: str, sha: str, expect_tree: str | None = None, dest: Path | None = None,
            apply: bool = False, accept_review: bool = False) -> dict:
    dest = (dest or default_dest()).resolve()
    dirs = fetch_skill_dirs(repo, sha)
    entry = dirs.get(path or ".")
    if entry is None:
        raise SystemExit(f"no skill folder '{path}' at {sha[:10]} (found: {sorted(dirs)[:8]})")
    name = posixpath.basename(path.rstrip("/")) if path not in ("", ".") else repo.split("/")[1]
    rep = vet_skill(entry, name)
    result = {"repo": repo, "path": path, "commit": sha, "name": rep["name"] or name, "verdict": rep["verdict"],
              "tree_sha256": rep["tree_sha256"], "findings": rep["findings"], "installed_to": None}
    if expect_tree and expect_tree != rep["tree_sha256"]:
        raise SystemExit(f"ABORT: tree hash mismatch (registry {expect_tree[:12]} vs downloaded {rep['tree_sha256'][:12]}). "
                         "The upstream content differs from what was vetted.")
    if rep["verdict"] == "fail":
        raise SystemExit("ABORT: vetting FAILED; refusing to install. Run vet.py for details.")
    if rep["verdict"] == "review" and not accept_review:
        result["note"] = "verdict REVIEW: read the findings, then re-run with --accept-review to proceed"
        return result
    if not apply:
        result["note"] = "dry run: nothing written (use --apply)"
        return result
    final = rep["name"] or name
    if not vet.NAME_RE.match(final):
        raise SystemExit(f"ABORT: skill name {final!r} is not a safe folder name")
    target = (dest / final).resolve()
    if dest not in target.parents:
        raise SystemExit("ABORT: destination escapes the skills directory")
    if target.exists():
        raise SystemExit(f"ABORT: {target} already exists; remove or rename it first")
    tmp = dest / f".{final}.installing"
    if tmp.exists():
        shutil.rmtree(tmp)
    for rel, data in entry["files"].items():
        out = (tmp / rel).resolve()
        if tmp.resolve() not in out.parents:
            shutil.rmtree(tmp, ignore_errors=True)
            raise SystemExit("ABORT: file path escapes the skill folder")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(data)
    tmp.rename(target)
    (target / ".skill-hub.json").write_text(json.dumps(
        {"repo": repo, "path": path, "commit": sha, "tree_sha256": rep["tree_sha256"], "verdict": rep["verdict"]}, indent=2), encoding="utf-8")
    result["installed_to"] = str(target)
    return result


def main(argv: list[str] | None = None) -> int:
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="Pinned, vetted skill installer")
    ap.add_argument("repo", help="owner/name")
    ap.add_argument("--path", default="", help="skill folder inside the repo ('.' for repo root)")
    ap.add_argument("--commit", default="", help="40-hex commit SHA (default: resolve latest and print it)")
    ap.add_argument("--expect-tree", default="", help="tree_sha256 recorded when the skill was vetted")
    ap.add_argument("--dest", default="", help="skills directory (default ~/.claude/skills)")
    ap.add_argument("--apply", action="store_true", help="write files (default is a dry run)")
    ap.add_argument("--accept-review", action="store_true", help="allow a REVIEW verdict")
    ap.add_argument("--list", action="store_true", help="list skill folders at the commit")
    ns = ap.parse_args(argv)
    sha = ns.commit or commit_sha(ns.repo)
    if not ns.commit:
        print(f"resolved latest commit: {sha}  (pass --commit {sha} to pin it)")
    if ns.list:
        for p, e in sorted(fetch_skill_dirs(ns.repo, sha).items()):
            rep = vet_skill(e, posixpath.basename(p))
            print(f"{rep['verdict']:6} score={rep['score']:3}  {p}")
        return 0
    if not ns.path:
        ap.error("--path is required (use --list to see choices)")
    res = install(ns.repo, ns.path, sha, ns.expect_tree or None, Path(ns.dest) if ns.dest else None, ns.apply, ns.accept_review)
    print(json.dumps({k: v for k, v in res.items() if k != "findings"}, indent=2))
    for f in res["findings"]:
        if f["severity"] in ("medium", "high", "critical"):
            print(f"  - [{f['severity']}] {f['rule']}: {f['message']} ({f['file']}:{f['line']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
