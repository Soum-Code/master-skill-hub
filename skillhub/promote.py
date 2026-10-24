"""`python -m skillhub promote <id>` - the human gate. Re-downloads the candidate at its pinned commit,
re-vets it, checks the tree hash, and only then marks it verified. Nothing unvetted can pass here."""
from __future__ import annotations

from pathlib import Path

from . import registry as R
from .common import installer, now_iso, read_json, today, write_json
from .records import make_record


def run(ns) -> int:
    cands = (read_json(R.CANDIDATES_JSON, {}) or {}).get("items", [])
    wanted = [c for c in cands if c["id"] == ns.id or c["repo"].lower() == ns.id.lower()]
    if not wanted:
        print(f"no candidate matches '{ns.id}'. Known: {[c['id'] for c in cands[:10]]}")
        return 1
    packs = R.load_packs()
    skills = {s["id"]: s for s in R.load_skills()}
    override = {x.strip() for x in ns.override_fail.split(",") if x.strip()}
    promoted, refused = [], []
    for c in wanted:
        dirs = installer.fetch_skill_dirs(c["repo"], c["commit"])
        entry = dirs.get(c["path"])
        if entry is None:
            refused.append((c["id"], "skill folder not found at the pinned commit"))
            continue
        name = Path(c["path"]).name if c["path"] != "." else c["repo"].split("/")[1]
        rep = installer.vet_skill(entry, name)
        if rep["tree_sha256"] != c["tree_sha256"]:
            refused.append((c["id"], "tree hash differs from what was vetted - upstream rewrote that commit?"))
            continue
        hard = {f["rule"] for f in rep["findings"] if f["severity"] in ("high", "critical")}
        if rep["verdict"] == "fail" and not hard <= override:
            refused.append((c["id"], f"vet FAIL ({sorted(hard - override)}). Owner may pass --override-fail <rules> after reading the skill."))
            continue
        if rep["verdict"] == "review" and not ns.accept_review:
            refused.append((c["id"], "vet REVIEW: read the findings, then pass --accept-review"))
            continue
        md = entry["files"]["SKILL.md"].decode("utf-8", "replace")
        rec = make_record(
            sid=c["id"], dirname=name, text=md, files=[[rel, len(b)] for rel, b in entry["files"].items()], packs=packs,
            license_hint=c.get("license"), status="verified",
            source={"type": "external", "repo": c["repo"], "path": c["path"], "commit": c["commit"], "tree_sha256": c["tree_sha256"],
                    "stars": c.get("stars", 0), "approved": today(),
                    "install": f"python skills/skill-vetter/scripts/install.py {c['repo']} --path {c['path']} --commit {c['commit']} --expect-tree {c['tree_sha256']} --apply"})
        rec["vet"] = {"verdict": rep["verdict"], "score": rep["score"], "date": today(), "findings": rep["counts"],
                      "override": sorted(override & hard)}
        rec["first_seen"] = rec["last_seen"] = today()
        skills[c["id"]] = rec
        promoted.append(c["id"])
    R.save_skills(list(skills.values()))
    left = [c for c in cands if c["id"] not in promoted]
    write_json(R.CANDIDATES_JSON, {"updated": now_iso(), "items": left})
    for pid in promoted:
        print("promoted:", pid)
    for pid, why in refused:
        print("refused:", pid, "-", why)
    return 0 if promoted else 2
