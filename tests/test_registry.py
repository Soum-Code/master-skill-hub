import json
import zipfile
from pathlib import Path

from skillhub import registry as R, validate
from skillhub.common import ROOT, vet


def test_registry_validates():
    assert validate.run(None) == 0


def test_slim_has_only_servable_and_sanitised_text():
    slim = json.loads(R.SLIM_JSON.read_text(encoding="utf-8"))
    assert slim["skills"], "empty registry"
    for s in slim["skills"]:
        assert s["status"] in R.SERVABLE
        assert len(s["desc"]) <= 400
        assert "<" not in s["desc"]


def test_bundled_registry_matches_slim():
    a = json.loads(R.SLIM_JSON.read_text(encoding="utf-8"))
    b = json.loads((ROOT / "skills" / "master-skill" / "references" / "registry.json").read_text(encoding="utf-8"))
    assert a == b


def test_no_local_paths_leak_into_registry():
    text = R.SKILLS_JSON.read_text(encoding="utf-8") + R.SLIM_JSON.read_text(encoding="utf-8")
    for needle in ("C:\\\\Users", "C:/Users", "/Users/", "/home/", "AppData", "somna"):
        assert needle not in text, needle


def test_zips_are_claude_ai_shaped():
    from skillhub import build
    out = ROOT / "dist"
    build.make_zip(ROOT / "skills" / "master-skill", out / "master-skill.zip")
    with zipfile.ZipFile(out / "master-skill.zip") as z:
        names = z.namelist()
    assert "master-skill/SKILL.md" in names
    assert "master-skill/scripts/route.py" in names
    assert "master-skill/references/registry.json" in names
    assert not any("__pycache__" in n for n in names)


def test_every_pack_has_discovery_queries_and_chains_reference_real_skills():
    packs = R.load_packs()
    assert all(p.get("queries") for p in packs.values())
    ids = {s["id"] for s in R.load_skills()}
    for c in R.load_chains():
        assert all(st["skill"] in ids for st in c["steps"]), c["id"]


def test_inventory_records_never_marked_verified_unless_hub_or_vetted():
    for s in R.load_skills():
        if s["status"] == "verified":
            assert s["source"].get("type") in ("hub", "external"), s["id"]
