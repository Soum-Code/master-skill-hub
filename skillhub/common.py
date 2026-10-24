"""Shared paths, JSON/YAML IO and small helpers. The vetter and router are standalone
stdlib scripts that also ship inside skills, so they are loaded by path, not copied."""
from __future__ import annotations

import datetime as dt
import importlib.util
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry"
CATALOG = ROOT / "catalog"
DIST = ROOT / "dist"
SKILLS = ROOT / "skills"
REPO_SLUG = "Soum-Code/master-skill-hub"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    sys.modules[name] = mod
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


vet = _load("hub_vet", SKILLS / "skill-vetter" / "scripts" / "vet.py")
route = _load("hub_route", SKILLS / "master-skill" / "scripts" / "route.py")
installer = _load("hub_install", SKILLS / "skill-vetter" / "scripts" / "install.py")


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def today() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def write_json(path: Path, data, *, compact: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if compact:
        text = json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    else:
        text = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
    path.write_text(text + "\n", encoding="utf-8", newline="\n")


def read_yaml(path: Path, default=None):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return default


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def slugify(s: str) -> str:
    return re.sub(r"-{2,}", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-") or "x"


def clean(s: object, limit: int = 400) -> str:
    return route.clean(s, limit)


PERMISSIVE = ("mit", "apache", "bsd", "isc", "cc0", "unlicense", "0bsd", "mpl", "zlib", "cc-by-4")


def license_class(lic: str | None) -> str:
    """'permissive' | 'proprietary' | 'unknown'"""
    if not lic:
        return "unknown"
    low = lic.lower()
    if any(p in low for p in PERMISSIVE):
        return "permissive"
    if any(w in low for w in ("proprietary", "all rights reserved", "commercial")):
        return "proprietary"
    return "unknown"
