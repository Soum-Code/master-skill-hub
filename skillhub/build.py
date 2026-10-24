"""`python -m skillhub build` - regenerate everything derived from registry/*.json|yml."""
from __future__ import annotations

import re
import zipfile
from pathlib import Path

from . import catalog, registry as R, site
from .common import DIST, REPO_SLUG, ROOT, SKILLS, read_json, write_json, write_text
from .records import make_record

HUB_PLUGIN = "skill-hub"
HUB_INSTALL = f"claude plugin marketplace add {REPO_SLUG} && claude plugin install {HUB_PLUGIN}@master-skill-hub"


def hub_records(packs: dict) -> list[dict]:
    recs = []
    for d in sorted(SKILLS.iterdir()):
        md = d / "SKILL.md"
        if not md.is_file():
            continue
        files = [[str(p.relative_to(d)).replace("\\", "/"), p.stat().st_size]
                 for p in d.rglob("*") if p.is_file() and "__pycache__" not in p.parts]
        rec = make_record(
            sid=f"{HUB_PLUGIN}:{d.name}", dirname=d.name, plugin=HUB_PLUGIN,
            text=md.read_text(encoding="utf-8"), files=files, packs=packs, license_hint="MIT",
            source={"type": "hub", "plugin": HUB_PLUGIN, "repo": REPO_SLUG, "install": HUB_INSTALL},
            status="verified")
        recs.append(rec)
    return recs


def make_zip(src_dir: Path, out: Path) -> None:
    """Zip a skill folder so that <name>/SKILL.md sits at the archive root (claude.ai format)."""
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src_dir.rglob("*")):
            if p.is_dir() or "__pycache__" in p.parts or p.suffix == ".pyc":
                continue
            arc = f"{src_dir.name}/{p.relative_to(src_dir).as_posix()}"
            info = zipfile.ZipInfo(arc, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())


def update_readme_stats(skills: list[dict], packs: dict) -> None:
    rd = ROOT / "README.md"
    if not rd.exists():
        return
    text = rd.read_text(encoding="utf-8")
    shown = [s for s in skills if s.get("status") in R.SERVABLE]
    by: dict[str, int] = {}
    for s in shown:
        by[s.get("pack", "general")] = by.get(s.get("pack", "general"), 0) + 1
    cand = (read_json(R.CANDIDATES_JSON, {}) or {}).get("items", [])
    quar = (read_json(R.QUARANTINE_JSON, {}) or {}).get("items", [])
    rows = ["| Pack | Skills |", "|---|---|"]
    for pid in sorted(by, key=lambda k: (-by[k], k)):
        rows.append(f"| [{packs.get(pid, {}).get('title', pid)}](catalog/packs/{pid}.md) | {by[pid]} |")
    block = (f"**{len(shown)} skills** in {len(by)} packs - {len(cand)} candidates awaiting approval - "
             f"{len(quar)} quarantined. Registry updated {R.updated_stamp()[:10]}.\n\n" + "\n".join(rows))
    new = re.sub(r"(<!-- STATS:START -->).*?(<!-- STATS:END -->)", lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", text, flags=re.S)
    if new != text:
        write_text(rd, new)


def run(ns) -> int:
    packs, profiles, chains = R.load_packs(), R.load_profiles(), R.load_chains()
    skills = [s for s in R.load_skills() if s.get("source", {}).get("type") != "hub"]
    skills += hub_records(packs)
    R.classify_all(skills, packs)
    R.save_skills(skills)

    slim = R.build_slim(skills, packs, profiles, chains)
    write_json(R.SLIM_JSON, slim, compact=True)
    cands = read_json(R.CANDIDATES_JSON, {"items": []}) or {"items": []}
    quar = read_json(R.QUARANTINE_JSON, {"items": []}) or {"items": []}

    catalog.build_catalog(skills, packs, chains, cands, quar)
    catalog.build_bundle(skills, packs, chains, slim)
    site.build_site(slim, cands.get("items", []))
    update_readme_stats(skills, packs)

    if not getattr(ns, "no_zip", False):
        for d in sorted(SKILLS.iterdir()):
            if (d / "SKILL.md").is_file():
                make_zip(d, DIST / f"{d.name}.zip")
    print(f"build: {len(slim['skills'])} servable skills, {len(packs)} packs, {len(chains)} chains, "
          f"{len(cands.get('items', []))} candidates, {len(quar.get('items', []))} quarantined")
    return 0
