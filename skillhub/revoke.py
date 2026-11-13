"""`python -m skillhub revoke <id> --reason "..."` - kill switch.
The skill leaves the router at once (status 'revoked' is not servable) and, because the reason ships in the
registry, every router that refreshes it warns users who still have that skill installed."""
from __future__ import annotations

from . import registry as R
from .common import clean, today


def run(ns) -> int:
    skills = R.load_skills()
    hit = [s for s in skills if s["id"] == ns.id or s.get("source", {}).get("repo", "").lower() == ns.id.lower()]
    if not hit:
        print(f"no skill or repo matches '{ns.id}'")
        return 1
    for s in hit:
        s["status"], s["revoked_reason"], s["revoked_on"] = "revoked", clean(ns.reason, 200), today()
    R.save_skills(skills)
    print(f"revoked {len(hit)} skill(s): {', '.join(s['id'] for s in hit[:8])}")
    return 0
