"""Turn a SKILL.md (+ file list) into a registry record. Deterministic: no LLM involved,
so every statement in the catalog is something that is literally in the skill."""
from __future__ import annotations

import re
from collections import Counter

from .common import clean, license_class, route, vet

GENERIC = set("""skill skills use used using user users when claude code agent task tasks file files
any all also not only more most other new via per make create creating build building help helps
work works working need needs like etc include includes including based provide provides support
supports within across without after before while should must may can will""".split())

TRIGGER_RE = re.compile(r"(use (this )?(skill |it )?(when|for|to|if|whenever|any ?time)|trigger(s|ed)? (on|when|for)|when the user|invoke when|activate when|use proactively)", re.I)


def _headings(body: str) -> list[list]:
    out, fence = [], False
    for line in body.splitlines():
        s = line.lstrip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{2,3})\s+(.+?)\s*#*\s*$", line)
        if m:
            out.append([len(m.group(1)), clean(m.group(2), 90)])
        if len(out) >= 40:
            break
    return out


def _summary(body: str) -> str:
    fence = False
    para: list[str] = []
    seen_h1 = False
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            continue
        if fence:
            continue
        if s.startswith("#"):
            if para:
                break
            seen_h1 = True
            continue
        if not s:
            if para:
                break
            continue
        if s.startswith(("|", "-", "*", ">", "1.", "<", "!", "[")) and not para:
            continue
        para.append(s)
    text = clean(" ".join(para), 300)
    return text if seen_h1 or text else ""


def _tags(name: str, desc: str, limit: int = 8) -> list[str]:
    words = [w for w in re.findall(r"[a-z][a-z0-9+#]{2,}", desc.lower()) if w not in GENERIC and w not in route.STOP]
    cnt = Counter(words)
    tags: list[str] = []
    for w in re.split(r"[-_:]", name.lower()):
        if len(w) > 2 and w not in GENERIC and w not in tags:
            tags.append(w)
    for w, _ in cnt.most_common(30):
        if w not in tags:
            tags.append(w)
        if len(tags) >= limit:
            break
    return tags[:limit]


def _triggers(desc: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+", desc)
    out = [clean(p, 260) for p in parts if TRIGGER_RE.search(p)]
    return out[:3]


def _tools(meta: dict) -> list[str]:
    raw = meta.get("allowed-tools") or meta.get("allowed_tools")
    if not raw:
        return []
    if isinstance(raw, list):
        return [clean(x, 60) for x in raw][:30]
    return [clean(x, 60) for x in re.split(r"[\s,]+", str(raw)) if x][:30]


def make_record(*, sid: str, dirname: str, text: str, files: list[list], packs: dict,
                kind: str = "skill", plugin: str | None = None, license_hint: str | None = None,
                source: dict | None = None, status: str = "installed") -> dict:
    text = text.replace("\r\n", "\n")  # CRLF vs LF checkouts must not change the registry
    meta, body = vet.parse_frontmatter(text)
    name = clean(meta.get("name") or dirname, 80)
    desc = clean(meta.get("description", ""), 1024)
    lic = clean(meta.get("license") or license_hint or "", 80) or None
    tags = _tags(name, desc)
    pack, extra = route.classify(name, desc, packs, tags)
    lc = license_class(lic)
    rec = {
        "id": sid,
        "name": name,
        "kind": kind,
        "plugin": plugin,
        "desc": desc,
        "when": " ".join(_triggers(desc))[:400],
        "pack": pack,
        "packs": extra,
        "tags": tags,
        "license": lic,
        "license_class": lc,
        "allowed_tools": _tools(meta),
        "headings": _headings(body),
        "lines": text.count("\n") + 1,
        "bytes": len(text.encode("utf-8")),
        "files": sorted(f[0] for f in files)[:60],
        "file_count": len(files),
        "scripts": sorted(f[0] for f in files if f[0].lower().endswith((".py", ".sh", ".js", ".mjs", ".ts", ".ps1")))[:20],
        "references": sorted(f[0] for f in files if f[0].lower().startswith(("references/", "reference/", "docs/")))[:20],
        "source": source or {},
        "status": status,
    }
    if lc == "permissive":
        rec["summary"] = _summary(body)
    return rec
