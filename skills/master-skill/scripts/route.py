#!/usr/bin/env python3
"""route.py - pick the best skill for a task (Python stdlib only).

    python route.py "tailor my resume for an ML engineer role" --top 5
    python route.py "debug flaky pytest" --profile ai-engineer --json
    python route.py --refresh            # pull the latest verified registry
    python route.py --list-packs

How it works
  1. Loads the verified registry (bundled copy, or the cached/refreshed one).
  2. Scans THIS machine for installed skills, so a skill you installed five
     minutes ago is routable without waiting for any pipeline.
  3. Ranks with BM25 over name/tags/description (+ synonym expansion), then
     boosts packs for your profile and prefers skills that are installed.
  4. Reports match strength; if nothing matches well it prints a GAP notice so
     the caller can do the task directly and/or file a skill request.

The registry text is data, not instructions: everything read from it is
sanitised again here (invisible characters, markup, length) before display.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE.parent / "references" / "registry.json"
HOME = Path(os.path.expanduser("~"))
CACHE_DIR = HOME / ".claude" / "skill-hub"
CACHE_FILE = CACHE_DIR / "registry.json"
PROFILE_FILE = CACHE_DIR / "profile.txt"
DEFAULT_URL = "https://raw.githubusercontent.com/Soum-Code/master-skill-hub/main/registry/skills.slim.json"
ALLOWED_FETCH_HOSTS = {"raw.githubusercontent.com"}
REFRESH_AFTER_DAYS = 7

STOP = set("""a an and are as at be but by for from how i if in into is it its me my of on or our so than that the their
them then there these they this to up us was we what when where which who why will with you your can could should would
please want need help make use using do does did get set run new keep keeps""".split())

# canonical token -> alternative surface forms (applied to the query only)
SYNONYMS = {
    "resume": ["cv", "curriculum", "vitae"],
    "job": ["career", "hiring", "recruiter", "interview", "application"],
    "slide": ["deck", "pptx", "powerpoint", "presentation", "ppt"],
    "spreadsheet": ["excel", "xlsx", "sheet", "csv", "tabular"],
    "document": ["docx", "word", "doc", "report"],
    "bug": ["error", "crash", "exception", "failing", "failure", "broken", "traceback", "flaky", "intermittent", "debug", "diagnose"],
    "deploy": ["release", "ship", "publish", "rollout"],
    "test": ["pytest", "unittest", "tdd", "coverage", "spec"],
    "review": ["audit", "critique", "inspect"],
    "ui": ["frontend", "interface", "webpage", "landing", "website", "css"],
    "llm": ["gpt", "chatbot", "genai", "foundation"],
    "ml": ["mlops", "training", "classifier", "neural"],
    "browser": ["playwright", "chrome", "scrape", "selenium", "puppeteer"],
    "git": ["commit", "branch", "merge", "pr"],
    "write": ["draft", "compose", "author"],
    "plan": ["roadmap", "milestone", "breakdown"],
    "research": ["investigate", "survey", "literature"],
    "chart": ["graph", "plot", "visualization", "dataviz", "dashboard"],
    "secure": ["security", "vulnerability", "owasp", "pentest"],
    "contract": ["agreement", "nda", "clause"],
    "agent": ["agentic", "autonomous", "subagent"],
    "pipeline": ["workflow", "cicd", "automation"],
    "summarize": ["summary", "tldr", "digest", "brief"],
    "kubernetes": ["k8s", "kubectl", "helm", "cluster"],
    "docker": ["container", "dockerfile"],
    "sql": ["query", "postgres", "mysql", "database"],
    "email": ["gmail", "mail", "inbox"],
    "meeting": ["standup", "minutes", "sync"],
    "learn": ["study", "tutor", "teach"],
    "optimize": ["performance", "latency", "slow", "speed"],
}
_GROUPS: dict[str, set[str]] = {}
_SYN_LOOKUP: dict[str, str] = {}

_INVISIBLE = re.compile("[\u200b-\u200f\u202a-\u202e\u2060-\u2064\u2066-\u206f\ufeff\U000e0000-\U000e007f\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
_TAGS = re.compile(r"<[^>]{0,200}>")


def clean(s: object, limit: int = 400) -> str:
    s = _INVISIBLE.sub("", str(s or ""))
    s = _TAGS.sub("", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s[:limit]


def stem(w: str) -> str:
    if len(w) > 7 and w.endswith("ly"):
        w = w[:-2]
    if len(w) > 5 and w.endswith("ing"):
        w = w[:-3]
        if len(w) > 3 and w[-1] == w[-2] and w[-1] in "bdgmnprt":
            w = w[:-1]
    elif len(w) > 5 and w.endswith("ed"):
        w = w[:-2]
        if len(w) > 3 and w[-1] == w[-2] and w[-1] in "bdgmnprt":
            w = w[:-1]
    elif len(w) > 4 and w.endswith("ies"):
        w = w[:-3] + "y"
    elif len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        w = w[:-1]
    return w


def tokenize(text: str) -> list[str]:
    out = []
    for w in re.findall(r"[a-z0-9][a-z0-9+#.-]*", clean(text, 4000).lower()):
        for part in re.split(r"[-.]", w):
            if len(part) > 1 and part not in STOP:
                out.append(stem(part))
    return out


def _build_synonyms() -> None:
    for canon, alts in SYNONYMS.items():
        key = stem(canon)
        members = {key} | {stem(a) for a in alts}
        _GROUPS[key] = members
        for m in members:
            _SYN_LOOKUP.setdefault(m, key)


_build_synonyms()


# ------------------------------------------------------------------ registry
def _valid_registry(d: object) -> bool:
    return isinstance(d, dict) and isinstance(d.get("skills"), list) and isinstance(d.get("packs"), dict)


def load_json(path: Path) -> dict | None:
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        return d if _valid_registry(d) else None
    except Exception:
        return None


def pick_registry(explicit: str | None) -> tuple[dict, str]:
    cands: list[Path] = []
    if explicit:
        cands.append(Path(explicit))
    if os.environ.get("SKILL_HUB_REGISTRY"):
        cands.append(Path(os.environ["SKILL_HUB_REGISTRY"]))
    best: tuple[dict, str] | None = None
    for p in cands:
        d = load_json(p)
        if d:
            return d, str(p)
    bundled = load_json(BUNDLED)
    cached = load_json(CACHE_FILE) if CACHE_FILE.exists() else None
    if cached and bundled:
        best = (cached, "cache") if cached.get("generated", "") >= bundled.get("generated", "") else (bundled, "bundled")
    elif cached:
        best = (cached, "cache")
    elif bundled:
        best = (bundled, "bundled")
    if best is None:
        return {"skills": [], "packs": {}, "profiles": {}, "chains": [], "meta": {}}, "none"
    return best


def refresh(url: str | None = None, force: bool = False) -> str:
    url = url or os.environ.get("SKILL_HUB_REGISTRY_URL") or DEFAULT_URL
    host = re.match(r"^https://([^/]+)/", url)
    if not host or host.group(1) not in ALLOWED_FETCH_HOSTS:
        return f"refused: {url} is not an allowed https host {sorted(ALLOWED_FETCH_HOSTS)}"
    if CACHE_FILE.exists() and not force:
        age_days = (time.time() - CACHE_FILE.stat().st_mtime) / 86400
        if age_days < REFRESH_AFTER_DAYS:
            return f"cache is {age_days:.1f} days old; use --refresh to force"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "skill-hub-router/1"})
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read(8 * 1024 * 1024)
        d = json.loads(raw.decode("utf-8"))
        if not _valid_registry(d):
            return "refused: downloaded file is not a valid registry"
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        CACHE_FILE.write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
        return f"refreshed: {len(d['skills'])} skills, generated {d.get('generated', '?')}"
    except Exception as e:  # network off, repo private, etc. - never fatal
        return f"refresh failed ({type(e).__name__}); using existing registry"


# ------------------------------------------------------------------ local scan
def _read_head(p: Path, n: int = 6000) -> str:
    try:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            return f.read(n)
    except OSError:
        return ""


def _frontmatter(text: str) -> dict:
    m = re.match(r"\A\ufeff?---[ \t]*\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return {}
    data: dict[str, str] = {}
    key = None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", line)
        if km and not line.startswith((" ", "\t")):
            key = km.group(1)
            v = km.group(2).strip()
            data[key] = "" if v in (">", "|", ">-", "|-") else v.strip("\"'")
        elif key and line.strip():
            data[key] = (data[key] + " " + line.strip()).strip()
    return data


def _plugin_name(skills_dir: Path) -> str | None:
    for up in (skills_dir.parent, skills_dir.parent.parent):
        pj = up / ".claude-plugin" / "plugin.json"
        if pj.exists():
            try:
                return json.loads(pj.read_text(encoding="utf-8")).get("name")
            except Exception:
                return None
    return None


def local_roots() -> list[tuple[Path, str | None]]:
    """(skills_dir, plugin_name or None). None => user/project-level skill."""
    roots: list[tuple[Path, str | None]] = [(HOME / ".claude" / "skills", None), (Path.cwd() / ".claude" / "skills", None)]
    ip = HOME / ".claude" / "plugins" / "installed_plugins.json"
    if ip.exists():
        try:
            data = json.loads(ip.read_text(encoding="utf-8")).get("plugins", {})
            for key, installs in data.items():
                for inst in installs if isinstance(installs, list) else []:
                    sd = Path(inst.get("installPath", "")) / "skills"
                    if sd.is_dir():
                        roots.append((sd, _plugin_name(sd) or key.split("@")[0]))
        except Exception:
            pass
    appdata = os.environ.get("APPDATA") or str(HOME / "Library" / "Application Support")
    base = Path(appdata) / "Claude"
    for pat in ("rpm/*/*/plugin_*/skills", "local-agent-mode-sessions/skills-plugin/*/*/skills"):
        for g in glob.glob(str(base / pat)):
            sd = Path(g)
            name = _plugin_name(sd) or ("anthropic-skills" if "skills-plugin" in g else None)
            roots.append((sd, name))
    return roots


def local_skills() -> list[dict]:
    out: dict[str, dict] = {}
    for sd, plugin in local_roots():
        if not sd.is_dir():
            continue
        try:
            entries = sorted(sd.iterdir())
        except OSError:
            continue
        for d in entries:
            md = d / "SKILL.md"
            if not md.is_file():
                continue
            fm = _frontmatter(_read_head(md))
            name = clean(fm.get("name") or d.name, 80)
            sid = f"{plugin}:{d.name}" if plugin else name
            if sid in out:
                continue
            out[sid] = {"id": sid, "name": name, "desc": clean(fm.get("description", ""), 400),
                        "plugin": plugin, "source": {"type": "local"}, "status": "installed", "kind": "skill"}
    return list(out.values())


# ------------------------------------------------------------------ classify
def classify(name: str, desc: str, packs: dict, tags: list[str] | None = None) -> tuple[str, list[str]]:
    ntok, dtok, ttok = set(tokenize(name)), set(tokenize(desc)), set(tokenize(" ".join(tags or [])))
    scores: dict[str, float] = {}
    for pid, p in packs.items():
        kws = {stem(k) for k in p.get("keywords", [])}
        s = 3.0 * len(kws & ntok) + 2.0 * len(kws & ttok) + 1.0 * len(kws & dtok)
        if s:
            scores[pid] = s
    if not scores:
        return "general", []
    ranked = sorted(scores, key=lambda k: (-scores[k], k))
    top = scores[ranked[0]]
    extra = [p for p in ranked[1:4] if scores[p] >= max(2.0, top * 0.6)]
    return ranked[0], extra


# ------------------------------------------------------------------ ranking
class Index:
    def __init__(self, skills: list[dict], packs: dict):
        self.skills = skills
        self.docs: list[dict[str, float]] = []
        self.dtok: list[set[str]] = []  # tokens that count for coverage (no pack-title tokens)
        df: dict[str, int] = {}
        lens = []
        for s in skills:
            tf: dict[str, float] = {}
            fields = [(s.get("id", "").replace(":", " ").replace("-", " "), 3.0), (s.get("name", ""), 3.0),
                      (" ".join(s.get("tags", []) or []), 2.0), (s.get("desc", ""), 1.0), (s.get("when", ""), 1.0)]
            cov_tokens: set[str] = set()
            for text, w in fields:
                for t in tokenize(text):
                    tf[t] = tf.get(t, 0.0) + w
                    if w >= 1.0:
                        cov_tokens.add(t)
            self.docs.append(tf)
            self.dtok.append(cov_tokens)
            lens.append(sum(tf.values()))
            for t in tf:
                df[t] = df.get(t, 0) + 1
        self.n = max(len(skills), 1)
        self.avg = (sum(lens) / len(lens)) if lens else 1.0
        self.lens = lens
        self.df = df

    def idf(self, t: str) -> float:
        d = self.df.get(t, 0)
        return math.log(1 + (self.n - d + 0.5) / (d + 0.5))

    def score(self, q: list[tuple[str, float]], i: int, k1: float = 1.5, b: float = 0.75) -> float:
        tf = self.docs[i]
        norm = 1 - b + b * (self.lens[i] / self.avg)
        total = 0.0
        for t, w in q:
            f = tf.get(t)
            if f:
                total += w * self.idf(t) * (f * (k1 + 1)) / (f + k1 * norm)
        return total


def expand_query(text: str) -> tuple[list[tuple[str, float]], list[set[str]]]:
    """Weighted query terms + groups (a group is satisfied if any member matches)."""
    base = tokenize(text)
    terms: dict[str, float] = {}
    groups: list[set[str]] = []
    for t in base:
        terms[t] = max(terms.get(t, 0.0), 1.0)
        grp = {t}
        key = _SYN_LOOKUP.get(t)
        if key:
            members = _GROUPS[key]
            for m in members:
                if m != t:
                    terms[m] = max(terms.get(m, 0.0), 0.55)
            grp |= members
        groups.append(grp)
    return list(terms.items()), groups


def infer_query_packs(q: list[tuple[str, float]], packs: dict) -> dict[str, float]:
    """Which packs does the task itself look like? Returns pack -> share of the best pack (0..1)."""
    scores: dict[str, float] = {}
    for pid, p in packs.items():
        kws = {stem(k) for k in p.get("keywords", [])}
        sc = sum(w for t, w in q if t in kws)
        if sc >= 1.0:
            scores[pid] = sc
    if not scores:
        return {}
    top = max(scores.values())
    return {k: v / top for k, v in scores.items() if v >= 0.5 * top}


def merge_local(reg_skills: list[dict], local: list[dict], packs: dict) -> list[dict]:
    by_id = {s["id"]: dict(s) for s in reg_skills if s.get("id")}
    by_name: dict[str, str] = {}
    for sid, s in by_id.items():
        by_name.setdefault(s.get("name", ""), sid)
    for ls in local:
        sid = ls["id"]
        if sid in by_id:
            by_id[sid]["installed"] = True
            continue
        alt = by_name.get(ls["name"])
        if alt and not ls.get("plugin"):
            by_id[alt]["installed"] = True
            continue
        pack, extra = classify(ls["name"], ls["desc"], packs)
        rec = dict(ls)
        rec.update({"pack": pack, "packs": extra, "tags": [], "installed": True, "local_only": True})
        by_id[sid] = rec
    return list(by_id.values())


def match_chains(chains: list[dict], qtokens: set[str], limit: int = 2) -> list[dict]:
    scored = []
    for c in chains or []:
        best = 0.0
        for phrase in c.get("keywords", []):
            toks = set(tokenize(phrase))
            if toks:
                best = max(best, len(toks & qtokens) / len(toks))
        if best >= 0.66:
            scored.append((best, c))
    scored.sort(key=lambda x: (-x[0], x[1].get("id", "")))
    return [c for _, c in scored[:limit]]


def route(query: str, reg: dict, *, profile: str = "general", pack: str | None = None, top: int = 5,
          use_local: bool = True, installed_only: bool = False) -> dict:
    packs = reg.get("packs", {})
    skills = merge_local(reg.get("skills", []), local_skills() if use_local else [], packs)
    if pack:
        skills = [s for s in skills if s.get("pack") == pack or pack in (s.get("packs") or [])]
    if installed_only:
        skills = [s for s in skills if s.get("installed")]
    idx = Index(skills, packs)
    q, groups = expand_query(query)
    weights = (reg.get("profiles", {}).get(profile, {}) or {}).get("packs", {})
    qpacks = infer_query_packs(q, packs)
    ranked = []
    for i, s in enumerate(skills):
        sc = idx.score(q, i)
        if sc <= 0:
            continue
        pw = max([weights.get(p, 0.0) for p in [s.get("pack", "")] + list(s.get("packs") or [])] or [0.0])
        sc *= 1 + 0.4 * pw
        qb = max([qpacks.get(p, 0.0) for p in [s.get("pack", "")] + list(s.get("packs") or [])] or [0.0])
        sc *= 1 + 0.5 * qb
        if s.get("installed"):
            sc *= 1.10
        cov = sum(1 for g in groups if g & idx.dtok[i]) / max(len(groups), 1)
        conf = 0.75 * cov + 0.25 * qb if cov >= 0.2 else 0.25 * cov
        ranked.append((sc, cov, conf, s))
    ranked.sort(key=lambda x: (-x[0], x[3].get("id", "")))
    results = []
    for sc, cov, conf, s in ranked[:top]:
        strength = "strong" if conf >= 0.65 else "moderate" if conf >= 0.35 else "weak"
        results.append({
            "id": s.get("id"), "name": s.get("name"), "pack": s.get("pack"), "score": round(sc, 2),
            "coverage": round(cov, 2), "match": strength, "installed": bool(s.get("installed")),
            "status": s.get("status"), "desc": clean(s.get("desc", ""), 220),
            "install": (s.get("source") or {}).get("install", ""),
        })
    gap = not results or results[0]["match"] == "weak"
    if gap:
        results = results[:2]
    else:
        results = [r for r in results if r["match"] != "weak"]
    return {"query": query, "profile": profile, "results": results, "gap": gap, "query_packs": sorted(qpacks, key=lambda k: -qpacks[k])[:3],
            "chains": match_chains(reg.get("chains", []), {t for t, _ in q}), "skills_considered": len(skills)}


def default_profile() -> str:
    if os.environ.get("SKILL_HUB_PROFILE"):
        return os.environ["SKILL_HUB_PROFILE"]
    try:
        return PROFILE_FILE.read_text(encoding="utf-8").strip() or "general"
    except OSError:
        return "general"


def render(out: dict, reg: dict, source: str) -> str:
    lines = [f"Task: {clean(out['query'], 200)}",
             f"Profile: {out['profile']}  |  registry: {source}, generated {reg.get('generated', '?')}  |  skills considered: {out['skills_considered']}"]
    if out.get("query_packs"):
        lines.append("Looks like: " + ", ".join(out["query_packs"]))
    if not out["results"]:
        lines.append("No matching skills.")
    elif out["gap"]:
        lines.append("Closest matches (all weak):")
    for n, r in enumerate(out["results"], 1):
        tag = "installed here" if r["installed"] else ("not installed here; verified in hub" if r["status"] == "verified" else "not installed here")
        lines.append(f"{n}. {r['id']}  [{tag}]  pack={r['pack']}  match={r['match']}  score={r['score']}")
        lines.append(f"   {r['desc']}")
        if r["installed"]:
            lines.append(f"   invoke: Skill(\"{r['id']}\")")
        elif r["install"]:
            lines.append(f"   install: {r['install']}   (vet first: python ../../skill-vetter/scripts/vet.py <dir>)")
    for c in out["chains"]:
        lines.append(f"Chain - {c['title']}: " + " -> ".join(s["skill"] for s in c.get("steps", [])))
    if out["gap"]:
        repo = (reg.get("meta") or {}).get("repo", "Soum-Code/master-skill-hub")
        lines.append("GAP: no strong match. Do the task directly, and offer the user a skill request:")
        lines.append(f"   gh issue create --repo {repo} --label skill-request --title \"{clean(out['query'], 70)}\"")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="Pick the best skill for a task")
    ap.add_argument("query", nargs="*", help="task description")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--profile", default=None)
    ap.add_argument("--pack", default=None)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--registry", default=None)
    ap.add_argument("--no-local", action="store_true", help="ignore skills installed on this machine")
    ap.add_argument("--installed-only", action="store_true")
    ap.add_argument("--refresh", action="store_true", help="download the latest registry")
    ap.add_argument("--list-packs", action="store_true")
    ap.add_argument("--list-profiles", action="store_true")
    ns = ap.parse_args(argv)

    if ns.refresh:
        print(refresh(force=True))
        if not ns.query:
            return 0
    elif not os.environ.get("SKILL_HUB_NO_AUTO_REFRESH") and not ns.registry:
        msg = refresh()
        if msg.startswith("refreshed"):
            print(msg, file=sys.stderr)

    reg, source = pick_registry(ns.registry)
    if ns.list_packs:
        counts: dict[str, int] = {}
        for s in reg.get("skills", []):
            counts[s.get("pack", "general")] = counts.get(s.get("pack", "general"), 0) + 1
        for pid, p in reg.get("packs", {}).items():
            print(f"{pid:24} {counts.get(pid, 0):4}  {p.get('title', '')}")
        return 0
    if ns.list_profiles:
        for pid, p in reg.get("profiles", {}).items():
            print(f"{pid:20} {p.get('title', '')}")
        return 0
    if not ns.query:
        ap.print_usage()
        return 2
    profile = ns.profile or default_profile()
    out = route(" ".join(ns.query), reg, profile=profile, pack=ns.pack, top=ns.top,
                use_local=not ns.no_local, installed_only=ns.installed_only)
    if ns.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(render(out, reg, source))
    return 0


if __name__ == "__main__":
    sys.exit(main())
