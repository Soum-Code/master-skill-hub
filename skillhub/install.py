"""`python -m skillhub install <id>` - install a VERIFIED registry skill using the pinned commit and recorded tree hash."""
from __future__ import annotations

from pathlib import Path

from . import registry as R
from .common import installer


def run(ns) -> int:
    rec = next((s for s in R.load_skills() if s["id"] == ns.id and s.get("status") == "verified"), None)
    if rec is None:
        print(f"'{ns.id}' is not a verified skill in the registry (candidates must be promoted first).")
        return 1
    src = rec.get("source") or {}
    if src.get("type") != "external":
        print(f"'{ns.id}' is {src.get('type')}: {src.get('install') or 'install it with its own plugin/marketplace'}")
        return 0
    res = installer.install(src["repo"], src["path"], src["commit"], src["tree_sha256"],
                            Path(ns.dest) if ns.dest else None, ns.apply, accept_review=(rec.get("vet") or {}).get("verdict") == "review")
    print({k: v for k, v in res.items() if k != "findings"})
    return 0
