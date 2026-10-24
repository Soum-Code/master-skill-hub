"""CLI:  python -m skillhub <command>

  inventory   scan this machine's installed skills into registry/skills.json
  build       rebuild slim registry, router bundle, catalog, site and zips
  validate    consistency checks used by CI
  vet PATH    vet a skill directory (same engine as the skill-vetter skill)
  discover    weekly discovery run (also vets what it finds)
  promote ID  re-vet a candidate at its pinned commit and mark it verified
  install ID  install a verified skill at its pinned commit after re-vetting
  report      print the latest weekly report
"""
from __future__ import annotations

import argparse
import sys

from . import registry as R
from .common import now_iso, vet


def cmd_inventory(ns) -> int:
    from . import inventory
    packs = R.load_packs()
    found = inventory.scan(packs)
    existing = {s["id"]: s for s in R.load_skills()}
    first_party_ids = set()
    for rec in found:
        old = existing.get(rec["id"])
        rec["status"] = "installed"
        rec["first_seen"] = (old or {}).get("first_seen") or now_iso()[:10]
        rec["last_seen"] = now_iso()[:10]
        existing[rec["id"]] = rec
        first_party_ids.add(rec["id"])
    # records that were 'installed' earlier but are gone locally are kept (the registry is cumulative)
    allrecs = list(existing.values())
    R.classify_all(allrecs, packs)
    R.save_skills(allrecs)
    by_src: dict[str, int] = {}
    for r in found:
        by_src[r["source"].get("type", "?")] = by_src.get(r["source"].get("type", "?"), 0) + 1
    print(f"inventory: {len(found)} skills found, registry now has {len(existing)}  by source: {by_src}")
    return 0


def cmd_build(ns) -> int:
    from . import build
    return build.run(ns)


def cmd_validate(ns) -> int:
    from . import validate
    return validate.run(ns)


def cmd_vet(ns) -> int:
    return vet.main([ns.path] + (["--json"] if ns.json else []))


def cmd_discover(ns) -> int:
    from . import discover
    return discover.run(ns)


def cmd_promote(ns) -> int:
    from . import promote
    return promote.run(ns)


def cmd_install(ns) -> int:
    from . import install
    return install.run(ns)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except Exception:
            pass
    ap = argparse.ArgumentParser(prog="skillhub", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("inventory").set_defaults(fn=cmd_inventory)
    b = sub.add_parser("build")
    b.add_argument("--no-zip", action="store_true")
    b.set_defaults(fn=cmd_build)
    v = sub.add_parser("validate")
    v.set_defaults(fn=cmd_validate)
    vt = sub.add_parser("vet")
    vt.add_argument("path")
    vt.add_argument("--json", action="store_true")
    vt.set_defaults(fn=cmd_vet)
    d = sub.add_parser("discover")
    d.add_argument("--max-repos", type=int, default=40, help="max repos to vet this run")
    d.add_argument("--max-skills-per-repo", type=int, default=40)
    d.add_argument("--sources", default="", help="comma list to restrict sources")
    d.add_argument("--dry-run", action="store_true", help="do not write registry files")
    d.add_argument("--report", default="", help="write the markdown report to this path")
    d.set_defaults(fn=cmd_discover)
    p = sub.add_parser("promote")
    p.add_argument("id", help="owner/repo or owner/repo:path/to/skill")
    p.add_argument("--accept-review", action="store_true", help="allow a 'review' verdict (medium findings)")
    p.add_argument("--override-fail", default="", help="comma list of rule ids to accept despite a 'fail' (owner only; recorded)")
    p.set_defaults(fn=cmd_promote)
    i = sub.add_parser("install")
    i.add_argument("id")
    i.add_argument("--apply", action="store_true", help="actually copy files (default: dry run)")
    i.add_argument("--dest", default="", help="override destination (default ~/.claude/skills)")
    i.set_defaults(fn=cmd_install)
    ns = ap.parse_args(argv)
    return ns.fn(ns)


if __name__ == "__main__":
    sys.exit(main())
