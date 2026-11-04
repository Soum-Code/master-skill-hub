"""`python -m skillhub sync-local` - find skills on THIS machine that the hub does not know yet.

Nothing is published without a yes: the default only lists. Add chosen ones with --add id1,id2
(or --add all), optionally --push to commit and push. Adding publishes the skill's name and
description in a public repo, so private/work skills should be left out."""
from __future__ import annotations

import subprocess

from . import build, inventory, registry as R
from .common import ROOT, now_iso, today


def run(ns) -> int:
    packs = R.load_packs()
    reg = R.load_skills()
    known = {s["id"] for s in reg}
    known_names = {s["name"] for s in reg}  # a local copy of an indexed skill (e.g. an ECC install) is not new
    found = inventory.scan(packs)
    new = [r for r in found if r["id"] not in known and not (r["source"].get("type") == "user" and r["name"] in known_names)]
    if not new:
        print("hub is up to date: no new skills on this machine.")
        return 0
    print(f"{len(new)} skill(s) on this machine are not in the hub yet:")
    for r in new:
        print(f"  {r['id']:40} {r['source'].get('type'):8} {r['desc'][:80]}")
    if not ns.add:
        print("\nNothing was added. Re-run with --add <id,id|all> after the owner says yes.")
        return 0
    chosen = new if ns.add == "all" else [r for r in new if r["id"] in {x.strip() for x in ns.add.split(",")}]
    if not chosen:
        print("none of the requested ids matched.")
        return 1
    skills = {s["id"]: s for s in R.load_skills()}
    for r in chosen:
        r["status"], r["first_seen"], r["last_seen"] = "installed", today(), today()
        skills[r["id"]] = r
    allrecs = list(skills.values())
    R.classify_all(allrecs, packs)
    R.save_skills(allrecs)
    build.run(type("N", (), {"no_zip": True})())
    print(f"added {len(chosen)}: {', '.join(r['id'] for r in chosen)}")
    if ns.push:
        git = lambda *a: subprocess.run(["git", "-C", str(ROOT), *a], check=True)
        git("add", "-A")
        git("commit", "-m", f"chore(local): add {len(chosen)} skill(s) from owner machine\n\nCo-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>")
        git("pull", "--rebase", "--autostash")
        git("push")
        print("pushed.")
    return 0
