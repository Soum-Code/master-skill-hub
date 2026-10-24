"""Generate the human-readable catalog (deep dive per skill, per pack, index) and the
compact pack files bundled inside the master skill. Output is deterministic."""
from __future__ import annotations

import shutil
from pathlib import Path

from .common import CATALOG, REPO_SLUG, SKILLS, clean, route, slugify, write_text
from . import registry as R

STATUS_LABEL = {
    "installed": "installed (owner's machine)",
    "verified": "verified (vetted at pinned commit)",
    "candidate": "candidate (vetted, awaiting approval)",
    "quarantined": "quarantined (failed vetting)",
}


def slug(sid: str) -> str:
    return slugify(sid.replace(":", "--"))


def cell(s: object, n: int = 160) -> str:
    return clean(s, n).replace("|", "\\|").replace("\n", " ")


def _related(skills: list[dict], k: int = 4) -> dict[str, list[dict]]:
    toks = {s["id"]: set(route.tokenize(" ".join([s["name"], s.get("desc", ""), " ".join(s.get("tags", []))]))) for s in skills}
    out: dict[str, list[dict]] = {}
    for s in skills:
        a = toks[s["id"]]
        scored = []
        for t in skills:
            if t["id"] == s["id"]:
                continue
            b = toks[t["id"]]
            if not a or not b:
                continue
            j = len(a & b) / len(a | b)
            if t.get("pack") == s.get("pack"):
                j *= 1.15
            if j >= 0.10:
                scored.append((j, t))
        scored.sort(key=lambda x: (-x[0], x[1]["id"]))
        out[s["id"]] = [t for _, t in scored[:k]]
    return out


def invoke_line(s: dict) -> str:
    src = s.get("source") or {}
    if s.get("kind") == "command":
        return f"`/{s['id']}`"
    if src.get("type") in ("plugin", "bundled", "builtin") and ":" in s["id"]:
        return f"`/{s['id']}`  (Skill tool: `{s['id']}`)"
    return f"`/{s['id']}`"


def skill_page(s: dict, related: list[dict], packs: dict) -> str:
    src = s.get("source") or {}
    pack_title = packs.get(s.get("pack", ""), {}).get("title", s.get("pack", ""))
    extra = ", ".join(packs.get(p, {}).get("title", p) for p in s.get("packs", []))
    origin = []
    if src.get("plugin"):
        origin.append(f"plugin `{src['plugin']}`" + (f" v{src['version']}" if src.get("version") else ""))
    if src.get("repo"):
        origin.append(f"[{src['repo']}](https://github.com/{src['repo']})")
    if not origin:
        origin.append(src.get("type", "unknown"))
    L = [f"# {cell(s['name'], 80)}", "",
         f"> {cell(s.get('desc', ''), 1024)}", "",
         "| | |", "|---|---|",
         f"| **ID** | `{s['id']}` |",
         f"| **Pack** | {pack_title}" + (f" (also: {extra})" if extra else "") + " |",
         f"| **Kind** | {s.get('kind', 'skill')} |",
         f"| **Status** | {STATUS_LABEL.get(s.get('status'), s.get('status'))} |",
         f"| **Origin** | {' - '.join(origin)} |",
         f"| **License** | {cell(s.get('license') or 'not declared', 60)} |",
         f"| **Size** | {s.get('lines', 0)} lines in SKILL.md, {s.get('file_count', 0)} file(s) |", ""]
    L += ["## When to use it", ""]
    if s.get("when"):
        for t in [x for x in s["when"].split(". ") if x.strip()]:
            L.append(f"- {cell(t.strip().rstrip('.'), 260)}.")
    else:
        L.append("- The description above is the trigger. It does not spell out extra conditions.")
    L.append("")
    if s.get("summary"):
        L += ["## What it says up front", "", f"> {cell(s['summary'], 300)}", ""]
    if s.get("headings"):
        L += ["## How it is structured", "", "The skill's own section headings, in order:", ""]
        for lvl, text in s["headings"][:30]:
            L.append(("  " * (int(lvl) - 2)) + f"- {cell(text, 90)}")
        L.append("")
    bundles = []
    if s.get("scripts"):
        bundles.append("scripts: " + ", ".join(f"`{x}`" for x in s["scripts"][:8]) + (" ..." if len(s["scripts"]) > 8 else ""))
    if s.get("references"):
        bundles.append("reference docs: " + ", ".join(f"`{x}`" for x in s["references"][:8]) + (" ..." if len(s["references"]) > 8 else ""))
    other = max(0, s.get("file_count", 0) - 1 - len(s.get("scripts", [])) - len(s.get("references", [])))
    if other:
        bundles.append(f"{other} other file(s)")
    L += ["## What it bundles", ""]
    L += [f"- {b}" for b in bundles] if bundles else ["- Just the SKILL.md (instructions only, no scripts)."]
    L.append("")
    L += ["## Permissions and risk notes", ""]
    if s.get("allowed_tools"):
        L.append("- Pre-approved tools: " + ", ".join(f"`{t}`" for t in s["allowed_tools"]))
    else:
        L.append("- Declares no pre-approved tools; Claude asks as usual.")
    if s.get("scripts"):
        L.append("- Ships executable scripts. Review them before trusting the skill outside its trusted source.")
    L.append("")
    if related:
        L += ["## Related skills", ""]
        for r in related:
            L.append(f"- [{r['id']}]({slug(r['id'])}.md) - {cell(r.get('desc', ''), 110)}")
        L.append("")
    L += ["## Invoke / install", "", f"- Invoke: {invoke_line(s)}"]
    if src.get("install"):
        L.append(f"- Install: `{src['install']}`")
    L += ["", "---", f"_Generated from the skill's own metadata by [master-skill-hub](https://github.com/{REPO_SLUG}). Nothing here is hand-written opinion._", ""]
    return "\n".join(L)


def build_catalog(skills: list[dict], packs: dict, chains: list[dict], candidates: dict, quarantine: dict) -> None:
    shown = [s for s in skills if s.get("status") in R.SERVABLE]
    rel = _related(shown)
    out = CATALOG
    if out.exists():
        shutil.rmtree(out)
    (out / "skills").mkdir(parents=True)
    (out / "packs").mkdir(parents=True)

    for s in shown:
        write_text(out / "skills" / f"{slug(s['id'])}.md", skill_page(s, rel.get(s["id"], []), packs))

    by_pack: dict[str, list[dict]] = {}
    for s in shown:
        by_pack.setdefault(s.get("pack", "general"), []).append(s)

    for pid, items in by_pack.items():
        p = packs.get(pid, {"title": pid, "summary": ""})
        L = [f"# {p['title']}", "", p.get("summary", ""), "", f"{len(items)} skill(s). Back to the [catalog](../README.md).", "",
             "| Skill | What it does | Status |", "|---|---|---|"]
        for s in sorted(items, key=lambda x: x["id"]):
            L.append(f"| [`{s['id']}`](../skills/{slug(s['id'])}.md) | {cell(s.get('desc', ''), 170)} | {s['status']} |")
        write_text(out / "packs" / f"{pid}.md", "\n".join(L) + "\n")

    L = ["# Skill catalog", "",
         f"{len(shown)} skills across {len(by_pack)} packs. Every page is generated from the skill's own SKILL.md, "
         "so the descriptions are the authors' words, not a summary I made up.", "",
         "## Packs (industries and roles)", "", "| Pack | Skills | What it covers |", "|---|---|---|"]
    for pid in sorted(by_pack, key=lambda k: (-len(by_pack[k]), k)):
        p = packs.get(pid, {"title": pid, "summary": ""})
        L.append(f"| [{p['title']}](packs/{pid}.md) | {len(by_pack[pid])} | {cell(p.get('summary', ''), 140)} |")
    L += ["", "## Multi-skill chains", ""]
    for c in chains:
        L.append(f"- **{c['title']}**: " + " -> ".join(f"`{st['skill']}`" for st in c["steps"]))
    L += ["", "## Pending review", "",
          f"- [{len(candidates.get('items', []))} candidates](candidates.md) vetted and waiting for a human OK",
          f"- [{len(quarantine.get('items', []))} quarantined](quarantine.md) repos that failed vetting", "",
          "## Everything, A to Z", "", "| Skill | Pack | Description |", "|---|---|---|"]
    for s in sorted(shown, key=lambda x: x["id"]):
        L.append(f"| [`{s['id']}`](skills/{slug(s['id'])}.md) | {s.get('pack', '')} | {cell(s.get('desc', ''), 150)} |")
    write_text(out / "README.md", "\n".join(L) + "\n")

    # candidates / quarantine pages
    L = ["# Candidates awaiting approval", "",
         "Vetted at the pinned commit, but the owner is not on the trusted list (or the verdict was REVIEW). "
         "Approve one with the `promote` workflow or `python -m skillhub promote <id>`.", "",
         "| Repo / skill | Pack | Stars | Verdict | Score | Pinned commit |", "|---|---|---|---|---|---|"]
    for c in sorted(candidates.get("items", []), key=lambda x: -x.get("rank", 0)):
        L.append(f"| [{c['id']}]({c.get('url', '')}) | {c.get('pack', '')} | {c.get('stars', '')} | {c.get('verdict', '')} | {c.get('rank', '')} | `{str(c.get('commit', ''))[:10]}` |")
    write_text(out / "candidates.md", "\n".join(L) + "\n")
    L = ["# Quarantine", "",
         "These failed vetting. Findings show rule ids and short excerpts only. Do not install them.", "",
         "| Repo / skill | Why | Pinned commit |", "|---|---|---|"]
    for q in quarantine.get("items", []):
        why = "; ".join(f"{f['rule']} ({f['file']}:{f['line']})" for f in q.get("top_findings", [])[:3])
        L.append(f"| {cell(q['id'], 80)} | {cell(why, 200)} | `{str(q.get('commit', ''))[:10]}` |")
    write_text(out / "quarantine.md", "\n".join(L) + "\n")


def build_bundle(skills: list[dict], packs: dict, chains: list[dict], slim: dict) -> None:
    """Files that ship INSIDE the master skill so it works offline and in claude.ai."""
    ref = SKILLS / "master-skill" / "references"
    if ref.exists():
        shutil.rmtree(ref)
    (ref / "packs").mkdir(parents=True)
    from .common import write_json
    write_json(ref / "registry.json", slim, compact=True)
    shown = [s for s in skills if s.get("status") in R.SERVABLE]
    by_pack: dict[str, list[dict]] = {}
    for s in shown:
        by_pack.setdefault(s.get("pack", "general"), []).append(s)
    L = ["# Pack index", "", "Pick the pack that matches the task, then open `packs/<pack>.md`.", "",
         "| Pack | Skills | Covers |", "|---|---|---|"]
    for pid in sorted(by_pack, key=lambda k: (-len(by_pack[k]), k)):
        p = packs.get(pid, {"title": pid, "summary": ""})
        L.append(f"| `{pid}` {p['title']} | {len(by_pack[pid])} | {cell(p.get('summary', ''), 120)} |")
    write_text(ref / "index.md", "\n".join(L) + "\n")
    for pid, items in by_pack.items():
        L = [f"# {packs.get(pid, {}).get('title', pid)}", ""]
        for s in sorted(items, key=lambda x: x["id"]):
            L.append(f"- `{s['id']}` - {cell(s.get('desc', ''), 190)}")
        write_text(ref / "packs" / f"{pid}.md", "\n".join(L) + "\n")
    L = ["# Chains", "", "Multi-skill workflows. Invoke each skill when its step begins.", ""]
    for c in chains:
        L += [f"## {c['title']}", ""]
        for i, st in enumerate(c["steps"], 1):
            L.append(f"{i}. `{st['skill']}` - {st['purpose']}")
        L.append("")
    write_text(ref / "chains.md", "\n".join(L))
