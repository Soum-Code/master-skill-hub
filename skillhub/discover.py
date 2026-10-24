"""Weekly discovery: find skills in the wild, vet every one at an exact commit, then triage.

    hits (many sources) -> repos -> prefilter -> download zip at commit SHA -> vet -> LLM second opinion
    -> policy: FAIL => quarantine | trusted owner + PASS => verified | everything else => candidate
    -> rank (impact + novelty + power + quality + relevance) -> registry files + markdown report
"""
from __future__ import annotations

import datetime as dt
import math
import os
import traceback
from pathlib import Path

from . import llm, registry as R, sources as S
from .common import REPO_SLUG, clean, installer, license_class, now_iso, read_json, route, today, vet, write_json, write_text
from .net import GitHub, HttpError
from .records import make_record

MAX_CANDIDATES_KEPT = 400


def _age_days(iso: str | None) -> float:
    if not iso:
        return 0.0
    try:
        t = dt.datetime.fromisoformat(iso.replace("Z", "+00:00"))
        return (dt.datetime.now(dt.timezone.utc) - t).total_seconds() / 86400
    except ValueError:
        return 0.0


def _meta_of(it: dict) -> dict:
    lic = (it.get("license") or {}).get("spdx_id")
    return {"slug": it["full_name"], "stars": it.get("stargazers_count", 0), "pushed_at": it.get("pushed_at"),
            "created_at": it.get("created_at"), "license": None if lic in (None, "NOASSERTION") else lic,
            "archived": bool(it.get("archived")), "fork": bool(it.get("fork")), "size": it.get("size", 0),
            "default_branch": it.get("default_branch") or "HEAD", "desc": clean(it.get("description") or "", 200),
            "url": it.get("html_url", f"https://github.com/{it['full_name']}")}


def decide(verdict: str, slug: str, meta: dict, trusted: set[str], min_age: float, llm_out: dict | None) -> tuple[str, str]:
    """Return (status, reason). Trust only ever UPGRADES a clean vet; it never overrides a fail."""
    if verdict == "fail":
        return "quarantined", "failed static vetting"
    owner = slug.split("/")[0].lower()
    flagged = bool(llm_out and llm_out.get("risk") == "high")
    if owner in trusted and not meta.get("fork") and verdict == "pass" and not flagged and _age_days(meta.get("created_at")) >= min_age:
        return "verified", f"trusted owner '{owner}' + clean vet"
    why = []
    if owner not in trusted:
        why.append("owner not on trusted list")
    if verdict == "review":
        why.append("vet verdict REVIEW")
    if flagged:
        why.append("LLM reviewer flagged high risk")
    if meta.get("fork"):
        why.append("fork")
    if _age_days(meta.get("created_at")) < min_age:
        why.append(f"repo younger than {int(min_age)} days")
    return "candidate", "; ".join(why) or "needs approval"


def _dtok(text: str) -> set[str]:
    return set(route.tokenize(text))


def novelty(desc: str, existing: list[set[str]]) -> float:
    a = _dtok(desc)
    if not a:
        return 0.0
    best = 0.0
    for b in existing:
        if b:
            best = max(best, len(a & b) / len(a | b))
    return round(1.0 - best, 3)


def rank_score(*, stars: int, velocity: int, mentions: int, nov: float, rec: dict, vet_score: int, rel: float) -> float:
    impact = 10 * math.log10(1 + max(stars, 0)) + min(velocity, 500) ** 0.5 + 3 * min(mentions, 6)
    power = (3 if rec.get("scripts") else 0) + (3 if rec.get("references") else 0) + min(rec.get("file_count", 1), 24) / 4
    return round(impact + 20 * nov + power + vet_score / 10 + 12 * rel, 2)


PLACEHOLDER_DIRS = {"template", "template-skill", "skill-template", "example", "examples", "sample", "samples",
                    "test", "tests", "fixture", "fixtures", "demo", "boilerplate"}


def is_placeholder(path: str, entry: dict) -> bool:
    """Templates and fixtures are not skills anyone should install."""
    segs = [x.lower() for x in path.split("/")]
    if any(x in PLACEHOLDER_DIRS for x in segs):
        return True
    meta, _ = vet.parse_frontmatter(entry["files"].get("SKILL.md", b"").decode("utf-8", "replace"))
    desc = str(meta.get("description", "")).strip().lower()
    return desc.startswith(("replace with", "todo", "describe ", "your skill", "<description", "[description"))


def process_repo(slug: str, meta: dict, ctx: dict) -> dict:
    """Download one repo at its HEAD commit and vet every skill folder in it."""
    gh: GitHub = ctx["gh"]
    sha = gh.head_sha(slug, None if meta.get("default_branch") in (None, "HEAD") else meta["default_branch"])
    out = {"slug": slug, "commit": sha, "skills": [], "note": ""}
    dirs = installer.fetch_skill_dirs(slug, sha)
    if not dirs:
        out["note"] = "no SKILL.md found"
        return out
    seen_hash: dict[str, dict] = {}
    for path in sorted(dirs, key=lambda p: (p.count("/"), p))[: ctx["max_skills"] * 3]:
        entry = dirs[path]
        name = Path(path).name if path != "." else slug.split("/")[1]
        if is_placeholder(path, entry):
            continue
        rep = installer.vet_skill(entry, name)
        h = rep["tree_sha256"]
        if h in seen_hash:  # same skill copied for several agents (.cursor/, .claude/, ...)
            seen_hash[h]["copies"] += 1
            continue
        md = entry["files"].get("SKILL.md", b"").decode("utf-8", "replace")
        files = [[rel, len(b)] for rel, b in entry["files"].items()]
        rec = make_record(
            sid=f"{slug}:{rep['name'] or name}", dirname=name, text=md, files=files, packs=ctx["packs"],
            license_hint=meta.get("license"), status="candidate",
            source={"type": "external", "repo": slug, "path": path, "commit": sha, "tree_sha256": h, "stars": meta.get("stars", 0),
                    "install": f"python skills/skill-vetter/scripts/install.py {slug} --path {path} --commit {sha} --expect-tree {h} --apply"})
        item = {"rec": rec, "rep": rep, "path": path, "copies": 1, "files": entry["files"]}
        seen_hash[h] = item
        out["skills"].append(item)
        if len(out["skills"]) >= ctx["max_skills"]:
            break
    return out


def run(ns) -> int:
    cfg = R.load_sources()
    packs, profiles = R.load_packs(), R.load_profiles()
    seen = read_json(R.SEEN_JSON, {}) or {}
    seen.setdefault("repos", {})
    seen.setdefault("processed", {})
    skills = R.load_skills()
    by_id = {s["id"]: s for s in skills}
    cands = {c["id"]: c for c in (read_json(R.CANDIDATES_JSON, {}) or {}).get("items", [])}
    quar = {q["id"]: q for q in (read_json(R.QUARANTINE_JSON, {}) or {}).get("items", [])}
    trusted = {k.lower() for k in (cfg.get("trusted_owners") or {})}
    min_age = float(cfg.get("min_repo_age_days", 14))
    gh = GitHub()
    only = {x.strip() for x in ns.sources.split(",") if x.strip()}

    # ---------- 1. gather hits
    table: list[tuple[str, str]] = []
    hits: list[dict] = []
    requests: list[dict] = []

    def run_source(name: str, fn):
        if only and name not in only:
            return
        enabled = (cfg.get("sources", {}).get(name) or {}).get("enabled", True) if name not in ("github", "watchlist", "awesome") else True
        if not enabled:
            table.append((name, "disabled in sources.yml"))
            return
        try:
            res = fn()
            if name == "issues":
                h, status, reqs = res
                requests.extend(reqs)
            else:
                h, status = res
            hits.extend(h)
            table.append((name, status))
        except Exception as e:  # a broken source must never sink the run
            table.append((name, f"failed: {type(e).__name__}: {str(e)[:120]}"))
            if os.environ.get("SKILL_HUB_DEBUG"):
                traceback.print_exc()

    run_source("watchlist", lambda: S.watchlist(cfg, packs, gh))
    run_source("github", lambda: S.github_topics(cfg, packs, gh))
    run_source("awesome", lambda: S.awesome_lists(cfg, packs, gh, seen))
    run_source("hackernews", lambda: S.hackernews(cfg, packs, gh))
    run_source("devto", lambda: S.devto(cfg, packs, gh))
    run_source("lobsters", lambda: S.lobsters(cfg, packs, gh))
    run_source("mastodon", lambda: S.mastodon(cfg, packs, gh))
    run_source("npm", lambda: S.npm(cfg, packs, gh))
    run_source("reddit", lambda: S.reddit(cfg, packs, gh))
    run_source("bluesky", lambda: S.bluesky(cfg, packs, gh))
    run_source("youtube", lambda: S.youtube(cfg, packs, gh))
    run_source("issues", lambda: S.github_issues(cfg, packs, gh, os.environ.get("GITHUB_REPOSITORY", REPO_SLUG)))
    # re-check upstream of everything already verified (rug-pull detection)
    for s in skills:
        src = s.get("source") or {}
        if s.get("status") == "verified" and src.get("type") == "external":
            hits.append(S._hit(src["repo"], "pinned-recheck", f"https://github.com/{src['repo']}", "re-vet pinned skill", 1.0))

    # ---------- 2. merge by repo, attach metadata, prefilter
    repos: dict[str, dict] = {}
    for h in hits:
        k = h["repo"].lower()
        r = repos.setdefault(k, {"slug": h["repo"], "hits": [], "weight": 0.0})
        r["hits"].append(h)
        r["weight"] += h["weight"]
    watch = {w.lower() for w in cfg.get("watchlist", [])}
    forced = watch | {h["repo"].lower() for h in hits if h["source"] in ("user-submission", "skill-request", "pinned-recheck")}
    n_meta_calls = 0
    for k, r in sorted(repos.items(), key=lambda kv: -kv[1]["weight"]):
        meta_raw = S.REPO_META.get(k)
        if meta_raw is None and n_meta_calls < 150:
            try:
                meta_raw = gh.repo(r["slug"])
                n_meta_calls += 1
            except HttpError:
                continue
        if meta_raw is None:
            continue
        r["meta"] = _meta_of(meta_raw)
    keep = []
    for k, r in repos.items():
        m = r.get("meta")
        if not m:
            continue
        forced_repo = k in forced
        if not forced_repo:
            if m["fork"] or m["archived"] or _age_days(m["pushed_at"]) > 365 or m["stars"] < 5:
                continue
        pre = 10 * math.log10(1 + m["stars"]) + 3 * min(r["weight"], 8) + (50 if forced_repo else 0)
        keep.append((pre, r))
    keep.sort(key=lambda x: -x[0])
    chosen = [r for _, r in keep[: ns.max_repos]]

    # ---------- 3. vet
    existing_desc = [_dtok(s.get("desc", "")) for s in skills if s.get("status") in R.SERVABLE]
    ctx = {"gh": gh, "packs": packs, "max_skills": ns.max_skills_per_repo}
    prof_w = (profiles.get(cfg.get("rank_profile", "ai-engineer")) or {}).get("packs", {})
    new_verified, new_cands, new_quar, updates, notes = [], [], [], [], []
    for r in chosen:
        slug, meta = r["slug"], r["meta"]
        try:
            res = process_repo(slug, meta, ctx)
        except Exception as e:
            notes.append(f"{slug}: {type(e).__name__}: {str(e)[:100]}")
            continue
        sha = res["commit"]
        prev = seen["repos"].get(slug, {})
        hist = prev.get("stars", [])
        vel = meta["stars"] - (hist[0][1] if hist and _age_days(hist[0][0] + "T00:00:00Z") >= 5 else meta["stars"])
        seen["repos"][slug] = {"first_seen": prev.get("first_seen", today()), "last_checked": today(), "last_commit": sha,
                               "stars": (hist + [[today(), meta["stars"]]])[-12:], "skills": len(res["skills"])}
        if res["note"]:
            notes.append(f"{slug}: {res['note']}")
        key = f"{slug}@{sha}"
        if key in seen["processed"] and not getattr(ns, "force", False):
            continue
        seen["processed"][key] = today()
        for item in res["skills"]:
            rec, rep = item["rec"], item["rep"]
            sid = rec["id"]
            llm_out = llm.review(item["files"]) if rep["verdict"] != "fail" and meta["stars"] >= 0 else None
            status, why = decide(rep["verdict"], slug, meta, trusted, min_age, llm_out)
            rec["status"] = status
            pw = max([prof_w.get(p, 0.0) for p in [rec["pack"]] + rec["packs"]] or [0.0])
            others = [d for d in existing_desc]
            nov = novelty(rec["desc"], others)
            mentions = len({h["source"] for h in r["hits"]})
            rk = rank_score(stars=meta["stars"], velocity=vel, mentions=mentions, nov=nov, rec=rec, vet_score=rep["score"], rel=pw)
            if status == "quarantined":
                quar[sid] = {"id": sid, "repo": slug, "commit": sha, "first_seen": quar.get(sid, {}).get("first_seen", today()),
                             "top_findings": [{k: f[k] for k in ("rule", "severity", "file", "line")} for f in rep["findings"] if f["severity"] in ("high", "critical")][:5]}
                cands.pop(sid, None)
                new_quar.append(sid)
                continue
            dup = [s for s in skills if s.get("status") in R.SERVABLE and s["name"] == rec["name"] and s["id"] != sid
                   and len(_dtok(s.get("desc", "")) & _dtok(rec["desc"])) / max(len(_dtok(s.get("desc", "")) | _dtok(rec["desc"])), 1) >= 0.85]
            if dup and sid not in by_id:
                notes.append(f"{sid}: same skill as '{dup[0]['id']}' already in registry, not added")
                continue
            rec.update({"first_seen": by_id.get(sid, {}).get("first_seen") or today(), "last_seen": today(),
                        "vet": {"verdict": rep["verdict"], "score": rep["score"], "date": today(), "findings": rep["counts"]},
                        "llm": llm_out, "novelty": nov, "rank": rk, "copies": item["copies"]})
            old = by_id.get(sid)
            if status == "verified":
                if old and old.get("status") == "verified" and (old.get("source") or {}).get("commit") == sha:
                    continue
                if old and old.get("status") == "verified":
                    updates.append(f"{sid}: {old['source']['commit'][:8]} -> {sha[:8]} (clean, trusted; re-pinned)")
                by_id[sid] = rec
                cands.pop(sid, None)
                new_verified.append(sid)
            else:
                if old and old.get("status") == "verified":
                    old["update_available"] = {"commit": sha, "verdict": rep["verdict"], "reason": why}
                    updates.append(f"{sid}: upstream moved to {sha[:8]} but is now {rep['verdict'].upper()} ({why}); pinned version kept")
                    continue
                cands[sid] = {"id": sid, "repo": slug, "path": rec["source"]["path"], "name": rec["name"], "desc": rec["desc"][:300],
                              "pack": rec["pack"], "stars": meta["stars"], "url": f"{meta['url']}/tree/{sha}/{rec['source']['path']}".replace("/./", "/").rstrip("/."),
                              "commit": sha, "tree_sha256": rec["source"]["tree_sha256"], "verdict": rep["verdict"], "vet_score": rep["score"],
                              "rank": rk, "why": why, "novelty": nov, "velocity": vel, "license": meta.get("license"),
                              "sources": sorted({h["source"] for h in r["hits"]}), "llm": llm_out,
                              "first_seen": cands.get(sid, {}).get("first_seen", today())}
                new_cands.append(sid)

    # ---------- 4. write
    ranked_cands = sorted(cands.values(), key=lambda c: -c.get("rank", 0))[:MAX_CANDIDATES_KEPT]
    summary = {"new_verified": new_verified, "new_candidates": new_cands, "new_quarantined": new_quar, "updates": updates,
               "repos_vetted": len(chosen), "hits": len(hits), "github_api_calls": gh.calls}
    report = render_report(summary, table, ranked_cands, quar, cands, by_id, requests, notes, seen)
    if ns.report:
        write_text(Path(ns.report), report)
    if ns.dry_run:
        print(report)
        print("\n(dry run: registry files not written)")
        return 0
    R.save_skills(list(by_id.values()))
    write_json(R.CANDIDATES_JSON, {"updated": now_iso(), "items": ranked_cands})
    write_json(R.QUARANTINE_JSON, {"updated": now_iso(), "items": sorted(quar.values(), key=lambda q: q["id"])[:400]})
    seen["processed"] = dict(sorted(seen["processed"].items(), key=lambda kv: kv[1])[-4000:])
    write_json(R.SEEN_JSON, seen, compact=True)
    write_json(R.LAST_RUN_JSON, {"at": now_iso(), "summary": summary, "sources": dict(table)})
    print(report)
    return 0


def render_report(summary, table, ranked, quar, cands, by_id, requests, notes, seen) -> str:
    L = [f"# Weekly skill discovery - {today()}", "",
         f"Vetted **{summary['repos_vetted']}** repositories from **{summary['hits']}** mentions. "
         f"**{len(summary['new_verified'])}** auto-verified (trusted owner + clean vet), "
         f"**{len(summary['new_candidates'])}** new candidates, **{len(summary['new_quarantined'])}** quarantined.", ""]
    if summary["new_verified"]:
        L += ["## Auto-verified this week", "", "Trusted owner and a clean static vet at the pinned commit. Still worth a glance.", ""]
        for sid in summary["new_verified"][:40]:
            r = by_id.get(sid, {})
            L.append(f"- `{sid}` ({r.get('pack', '')}) - {clean(r.get('desc', ''), 140)}")
        L.append("")
    top = [c for c in ranked if c["id"] in set(summary["new_candidates"])][:15] or ranked[:10]
    L += ["## Needs your approval", "",
          "Ranked by impact (stars, velocity, cross-source mentions) + novelty vs what you already have + power (scripts, references) + vet score + fit to your profile.", "",
          "| Rank | Skill | Pack | Stars | Vet | Why not auto | Approve |", "|---|---|---|---|---|---|---|"]
    for c in top:
        L.append(f"| {c['rank']} | [{c['id']}]({c['url']}) | {c['pack']} | {c['stars']} | {c['verdict']} {c['vet_score']} | {c['why']} | `promote {c['id']}` |")
        if c.get("llm") and c["llm"].get("summary"):
            L.append(f"| | _AI summary:_ {c['llm']['summary']} (reviewer risk: {c['llm']['risk']}) | | | | | |")
    L.append("")
    if summary["updates"]:
        L += ["## Upstream changes to skills you already pin", ""] + [f"- {u}" for u in summary["updates"]] + [""]
    if summary["new_quarantined"]:
        L += ["## Quarantined (failed vetting - do not install)", ""]
        for sid in summary["new_quarantined"][:25]:
            q = quar[sid]
            L.append(f"- `{sid}`: " + ", ".join(f"{f['rule']} ({f['file']}:{f['line']})" for f in q["top_findings"][:3]))
        L.append("")
    trending = sorted([(slug, v["stars"][-1][1] - v["stars"][0][1], v["stars"][-1][1]) for slug, v in seen["repos"].items() if len(v.get("stars", [])) > 1],
                      key=lambda x: -x[1])[:8]
    if trending and trending[0][1] > 0:
        L += ["## Trending (stars gained since first sighting)", ""] + [f"- {s}: +{d} ({n} total)" for s, d, n in trending if d > 0] + [""]
    if requests:
        L += ["## Open skill requests searched for", ""] + [f"- {r['query']} ({r['issue']})" for r in requests] + [""]
    L += ["## Source health", "", "| Source | Status |", "|---|---|"] + [f"| {n} | {s} |" for n, s in table] + [""]
    if notes:
        L += ["## Notes", ""] + [f"- {n}" for n in notes[:40]] + [""]
    L += ["---", "_Approve with `python -m skillhub promote <id>` or the **promote** workflow. "
          "\"Verified\" means static checks passed at a pinned commit; read the skill before trusting it with anything sensitive._"]
    return "\n".join(L)
