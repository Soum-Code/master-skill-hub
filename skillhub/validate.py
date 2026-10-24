"""`python -m skillhub validate` - consistency gate for CI. Exit 1 on any error."""
from __future__ import annotations

import re

from . import registry as R
from .common import ROOT, SKILLS, read_json, vet

ALLOWED_FM = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
RESERVED = ("anthropic", "claude")
# The scanner's own source necessarily contains the attack patterns it searches for.
SELF_EXEMPT = {("skill-vetter", "scripts/vet.py")}


def run(ns) -> int:
    errors: list[str] = []
    warns: list[str] = []

    packs, profiles, chains = R.load_packs(), R.load_profiles(), R.load_chains()
    skills = R.load_skills()
    ids = [s["id"] for s in skills]
    if len(ids) != len(set(ids)):
        dup = sorted({i for i in ids if ids.count(i) > 1})
        errors.append(f"duplicate skill ids: {dup[:5]}")

    for pid, p in packs.items():
        for k in ("title", "summary", "keywords", "queries"):
            if not p.get(k):
                errors.append(f"pack {pid}: missing {k}")
    for prof, pdef in profiles.items():
        for pk in (pdef.get("packs") or {}):
            if pk not in packs:
                errors.append(f"profile {prof}: unknown pack {pk}")
    for s in skills:
        if s.get("pack") not in packs and s.get("pack") != "general":
            errors.append(f"skill {s['id']}: unknown pack {s.get('pack')}")
    for o_id, o in R.load_overrides().items():
        if o_id not in ids:
            warns.append(f"override for unknown skill {o_id}")
        for pk in [o.get("pack")] + list(o.get("packs", [])):
            if pk and pk not in packs:
                errors.append(f"override {o_id}: unknown pack {pk}")

    idset = set(ids)
    for c in chains:
        for st in c.get("steps", []):
            if st["skill"] not in idset:
                errors.append(f"chain {c['id']}: step skill '{st['skill']}' is not in the registry")
        if c.get("pack") not in packs:
            errors.append(f"chain {c['id']}: unknown pack {c.get('pack')}")

    slim = read_json(R.SLIM_JSON, {}) or {}
    servable = [s for s in skills if s.get("status") in R.SERVABLE]
    if len(slim.get("skills", [])) != len(servable):
        errors.append(f"skills.slim.json has {len(slim.get('skills', []))} skills but registry has {len(servable)} servable - run `python -m skillhub build`")
    bundled = read_json(SKILLS / "master-skill" / "references" / "registry.json", {}) or {}
    if bundled.get("generated") != slim.get("generated"):
        errors.append("master-skill/references/registry.json is stale - run `python -m skillhub build`")

    # hub-authored skills must satisfy the strictest consumer (claude.ai upload) and pass vetting
    for d in sorted(SKILLS.iterdir()):
        md = d / "SKILL.md"
        if not md.is_file():
            continue
        text = md.read_text(encoding="utf-8")
        meta, _ = vet.parse_frontmatter(text)
        extra = set(meta) - ALLOWED_FM
        if extra:
            errors.append(f"{d.name}: frontmatter keys not accepted by claude.ai: {sorted(extra)}")
        if meta.get("name") != d.name:
            errors.append(f"{d.name}: name '{meta.get('name')}' must equal the folder name")
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", str(meta.get("name", ""))) or any(w in str(meta.get("name", "")) for w in RESERVED):
            errors.append(f"{d.name}: invalid or reserved name")
        if len(str(meta.get("description", ""))) > 1024:
            errors.append(f"{d.name}: description over 1024 chars")
        if text.count("\n") > 500:
            errors.append(f"{d.name}: SKILL.md over 500 lines")
        rep = vet.vet_dir(d)
        bad = [f for f in rep["findings"] if f["severity"] in ("medium", "high", "critical")
               and (d.name, f["file"]) not in SELF_EXEMPT]
        if bad:
            errors.append(f"{d.name}: own vet findings -> {[(f['rule'], f['file'], f['line']) for f in bad][:4]}")

    for w in warns:
        print("warn:", w)
    for e in errors:
        print("ERROR:", e)
    print(f"validate: {len(skills)} skills, {len(packs)} packs, {len(chains)} chains -> {'FAILED' if errors else 'ok'}")
    return 1 if errors else 0
