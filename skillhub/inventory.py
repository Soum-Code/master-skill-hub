"""Scan skills installed on THIS machine (Claude Code plugins, ~/.claude/skills, and the
Claude desktop app's bundled plugins) and turn them into registry records.

Local paths are never written to the registry (they contain the username)."""
from __future__ import annotations

import glob
import json
import os
from pathlib import Path

from .common import REGISTRY, REPO_SLUG, clean, read_yaml, vet
from .records import make_record

HOME = Path(os.path.expanduser("~"))
CLAUDE = HOME / ".claude"
KNOWLEDGE_WORK_REPO = "anthropics/knowledge-work-plugins"


def _jload(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return None


def _filelist(d: Path) -> list[list]:
    out = []
    for dp, dns, fns in os.walk(d):
        dns[:] = [x for x in dns if x not in (".git", "node_modules", "__pycache__")]
        for fn in fns:
            fp = Path(dp) / fn
            try:
                out.append([str(fp.relative_to(d)).replace("\\", "/"), fp.stat().st_size])
            except OSError:
                pass
    return out


def _license_hint(plugin_dir: Path | None, skill_dir: Path) -> str | None:
    if plugin_dir:
        pj = _jload(plugin_dir / ".claude-plugin" / "plugin.json") or {}
        if pj.get("license"):
            return str(pj["license"])
    for base in (skill_dir, plugin_dir):
        if not base:
            continue
        for fn in ("LICENSE", "LICENSE.md", "LICENSE.txt"):
            p = base / fn
            if p.is_file():
                head = p.read_text(encoding="utf-8", errors="replace")[:600].lower()
                if "mit license" in head:
                    return "MIT"
                if "apache license" in head:
                    return "Apache-2.0"
                if "bsd" in head:
                    return "BSD"
                if "proprietary" in head or "all rights reserved" in head:
                    return "Proprietary"
    return None


def _skill_dirs(plugin_root: Path, entry: dict | None) -> list[Path]:
    if entry and isinstance(entry.get("skills"), list):
        return [plugin_root / s for s in entry["skills"] if (plugin_root / s / "SKILL.md").is_file()]
    sd = plugin_root / "skills"
    if sd.is_dir():
        return sorted(p for p in sd.iterdir() if (p / "SKILL.md").is_file())
    return []


def _command_files(plugin_root: Path) -> list[Path]:
    cd = plugin_root / "commands"
    return sorted(cd.glob("*.md")) if cd.is_dir() else []


def scan(packs: dict) -> list[dict]:
    recs: dict[str, dict] = {}

    def add(rec: dict) -> None:
        recs.setdefault(rec["id"], rec)

    # 1) user-level skills
    ud = CLAUDE / "skills"
    if ud.is_dir():
        for d in sorted(ud.iterdir()):
            md = d / "SKILL.md"
            if md.is_file():
                add(make_record(
                    sid=d.name, dirname=d.name, text=md.read_text(encoding="utf-8", errors="replace"),
                    files=_filelist(d), packs=packs, license_hint=_license_hint(None, d),
                    source={"type": "user", "install": f"copy the skill folder into ~/.claude/skills/{d.name}"}))

    # 2) Claude Code plugins
    inst = (_jload(CLAUDE / "plugins" / "installed_plugins.json") or {}).get("plugins", {})
    known = _jload(CLAUDE / "plugins" / "known_marketplaces.json") or {}
    for key, installs in inst.items():
        pname, _, mkt = key.partition("@")
        for it in installs if isinstance(installs, list) else []:
            root = Path(it.get("installPath", ""))
            if not root.is_dir():
                continue
            pj = _jload(root / ".claude-plugin" / "plugin.json") or {}
            pname = pj.get("name") or pname
            repo = ((known.get(mkt) or {}).get("source") or {}).get("repo")
            mj = _jload(CLAUDE / "plugins" / "marketplaces" / mkt / ".claude-plugin" / "marketplace.json") or {}
            entry = next((p for p in mj.get("plugins", []) if p.get("name") == pname), None)
            src = {"type": "plugin", "marketplace": mkt, "plugin": pname, "repo": repo,
                   "version": it.get("version"), "commit": it.get("gitCommitSha"),
                   "install": (f"claude plugin marketplace add {repo} && claude plugin install {pname}@{mkt}" if repo else "")}
            for d in _skill_dirs(root, entry):
                add(make_record(sid=f"{pname}:{d.name}", dirname=d.name, plugin=pname,
                                text=(d / "SKILL.md").read_text(encoding="utf-8", errors="replace"),
                                files=_filelist(d), packs=packs, license_hint=_license_hint(root, d), source=src))
            for c in _command_files(root):
                text = c.read_text(encoding="utf-8", errors="replace")
                meta, _ = vet.parse_frontmatter(text)
                if meta.get("description"):
                    add(make_record(sid=f"{pname}:{c.stem}", dirname=c.stem, plugin=pname, kind="command", text=text,
                                    files=[[c.name, c.stat().st_size]], packs=packs,
                                    license_hint=_license_hint(root, root), source=src))

    # 3) Claude desktop / Cowork bundled plugins
    appdata = os.environ.get("APPDATA") or str(HOME / "Library" / "Application Support")
    base = Path(appdata) / "Claude"
    for g in sorted(glob.glob(str(base / "rpm" / "*" / "*" / "plugin_*"))):
        root = Path(g)
        pj = _jload(root / ".claude-plugin" / "plugin.json") or {}
        pname = pj.get("name")
        if not pname:
            continue
        src = {"type": "bundled", "plugin": pname, "repo": KNOWLEDGE_WORK_REPO, "version": pj.get("version"),
               "install": f"bundled with Claude desktop (Cowork plugin '{pname}'); source: github.com/{KNOWLEDGE_WORK_REPO}"}
        for d in _skill_dirs(root, None):
            add(make_record(sid=f"{pname}:{d.name}", dirname=d.name, plugin=pname,
                            text=(d / "SKILL.md").read_text(encoding="utf-8", errors="replace"),
                            files=_filelist(d), packs=packs, license_hint=_license_hint(root, d), source=src))
        for c in _command_files(root):
            text = c.read_text(encoding="utf-8", errors="replace")
            meta, _ = vet.parse_frontmatter(text)
            if meta.get("description"):
                add(make_record(sid=f"{pname}:{c.stem}", dirname=c.stem, plugin=pname, kind="command", text=text,
                                files=[[c.name, c.stat().st_size]], packs=packs,
                                license_hint=_license_hint(root, root), source=src))
    for g in sorted(glob.glob(str(base / "local-agent-mode-sessions" / "skills-plugin" / "*" / "*"))):
        sd = Path(g) / "skills"
        if not sd.is_dir():
            continue
        src = {"type": "builtin", "plugin": "anthropic-skills",
               "install": "built into the Claude desktop app / claude.ai"}
        for d in sorted(p for p in sd.iterdir() if (p / "SKILL.md").is_file()):
            add(make_record(sid=f"anthropic-skills:{d.name}", dirname=d.name, plugin="anthropic-skills",
                            text=(d / "SKILL.md").read_text(encoding="utf-8", errors="replace"),
                            files=_filelist(d), packs=packs, license_hint=_license_hint(None, d), source=src))

    # 4) harness built-ins that have no files on disk (curated list)
    for b in (read_yaml(REGISTRY / "builtin-skills.yml", {}) or {}).get("skills", []):
        text = f"---\nname: {b['name']}\ndescription: {b['description']}\n---\n"
        add(make_record(sid=b["name"], dirname=b["name"], text=text, files=[], packs=packs, license_hint=None,
                        source={"type": "builtin", "install": "built into Claude Code"}))
    return sorted(recs.values(), key=lambda r: r["id"])
