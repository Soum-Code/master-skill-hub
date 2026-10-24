"""Registry files: full records (skills.json), router bundle (skills.slim.json), candidates, quarantine."""
from __future__ import annotations

from .common import REGISTRY, REPO_SLUG, clean, now_iso, read_json, read_yaml, route, write_json

SKILLS_JSON = REGISTRY / "skills.json"
SLIM_JSON = REGISTRY / "skills.slim.json"
CANDIDATES_JSON = REGISTRY / "candidates.json"
QUARANTINE_JSON = REGISTRY / "quarantine.json"
SEEN_JSON = REGISTRY / "seen.json"
LAST_RUN_JSON = REGISTRY / "last-run.json"

SERVABLE = ("installed", "verified")  # statuses the router may recommend


def load_packs() -> dict:
    return (read_yaml(REGISTRY / "packs.yml", {}) or {}).get("packs", {})


def load_profiles() -> dict:
    return (read_yaml(REGISTRY / "profiles.yml", {}) or {}).get("profiles", {})


def load_chains() -> list[dict]:
    return (read_yaml(REGISTRY / "chains.yml", {}) or {}).get("chains", [])


def load_sources() -> dict:
    return read_yaml(REGISTRY / "sources.yml", {}) or {}


def load_skills() -> list[dict]:
    return (read_json(SKILLS_JSON, {}) or {}).get("skills", [])


def updated_stamp() -> str:
    return (read_json(SKILLS_JSON, {}) or {}).get("updated", "1970-01-01T00:00:00Z")


def save_skills(skills: list[dict]) -> None:
    """Write skills.json. The `updated` stamp moves only when content changes, so builds are reproducible."""
    skills = sorted(skills, key=lambda r: r["id"])
    old = read_json(SKILLS_JSON, {}) or {}
    stamp = old.get("updated") if old.get("skills") == skills else now_iso()
    write_json(SKILLS_JSON, {"schema": 1, "repo": REPO_SLUG, "updated": stamp or now_iso(), "skills": skills})


def load_overrides() -> dict:
    return (read_yaml(REGISTRY / "overrides.yml", {}) or {}).get("overrides", {})


def classify_all(skills: list[dict], packs: dict) -> None:
    """Re-run keyword classification, then apply manual overrides."""
    ov = load_overrides()
    for s in skills:
        pack, extra = route.classify(s["name"], s.get("desc", ""), packs, s.get("tags"))
        o = ov.get(s["id"])
        if o:
            pack = o.get("pack", pack)
            extra = o.get("packs", [p for p in extra if p != pack])
        s["pack"], s["packs"] = pack, extra


def build_slim(skills: list[dict], packs: dict, profiles: dict, chains: list[dict]) -> dict:
    out = []
    for s in skills:
        if s.get("status") not in SERVABLE:
            continue
        src = s.get("source") or {}
        out.append({
            "id": s["id"], "name": s["name"], "kind": s.get("kind", "skill"),
            "desc": clean(s.get("desc", ""), 400), "when": clean(s.get("when", ""), 260),
            "pack": s.get("pack", "general"), "packs": s.get("packs", []), "tags": s.get("tags", []),
            "status": s["status"],
            "source": {k: src[k] for k in ("type", "plugin", "repo", "install") if src.get(k)},
        })
    return {
        "schema": 1,
        "generated": updated_stamp(),
        "meta": {"repo": REPO_SLUG, "count": len(out)},
        "packs": {k: {"title": v["title"], "summary": v.get("summary", ""), "keywords": v.get("keywords", [])}
                  for k, v in packs.items()},
        "profiles": profiles,
        "chains": chains,
        "skills": out,
    }
