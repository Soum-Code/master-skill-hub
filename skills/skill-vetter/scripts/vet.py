#!/usr/bin/env python3
"""vet.py - static security vetting for Agent Skills (Python stdlib only).

Usage:
    python vet.py <skill-dir> [--json] [--fail-on medium|high]

Exit code: 0 = pass, 1 = review (medium findings), 2 = fail (high/critical).

What it does NOT do: it cannot prove a skill is safe. Static checks catch the
common, lazy attack patterns (hidden unicode, curl|sh, credential paths, exfil
endpoints, prompt-injection phrasing, binaries, install hooks). A determined
attacker can phrase an injection that no regex catches, so a "pass" means
"no known red flags", and every install must still be pinned to a commit SHA
and file hashes (see skillhub/install.py).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

try:  # optional, only used for nicer frontmatter parsing
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None

SEV_ORDER = ["info", "low", "medium", "high", "critical"]
PENALTY = {"info": 0, "low": 2, "medium": 10, "high": 35, "critical": 60}

MAX_FILES = 400
MAX_TOTAL_BYTES = 12 * 1024 * 1024
MAX_FILE_BYTES = 2 * 1024 * 1024

DOC_EXT = {".md", ".markdown", ".txt", ".rst"}
CODE_EXT = {
    ".py", ".sh", ".bash", ".zsh", ".fish", ".ps1", ".psm1", ".bat", ".cmd",
    ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx", ".rb", ".pl", ".php", ".go",
    ".rs", ".java", ".kt", ".swift", ".lua", ".r", ".vbs",
}
DATA_EXT = {
    ".yml", ".yaml", ".json", ".toml", ".ini", ".cfg", ".csv", ".tsv", ".xml",
    ".html", ".htm", ".css", ".svg", ".lock", ".env", ".example", ".tmpl",
    ".j2", ".sql", ".graphql", ".proto", ".gitignore",
}
BAD_BINARY_EXT = {
    ".exe", ".dll", ".so", ".dylib", ".bin", ".msi", ".jar", ".apk", ".scr",
    ".com", ".pyc", ".pyd", ".node", ".class", ".o", ".a", ".lib", ".sys",
    ".drv", ".wsf", ".lnk", ".dmg", ".pkg", ".deb", ".rpm", ".wasm",
}
ARCHIVE_EXT = {".zip", ".tar", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar", ".whl"}
BENIGN_BINARY_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".bmp", ".pdf", ".ttf",
    ".otf", ".woff", ".woff2", ".mp3", ".mp4", ".wav", ".webm", ".docx",
    ".xlsx", ".pptx", ".potx", ".dotx",
}
SKIP_DIRS = {".git", "__pycache__"}
MAGIC_BAD = (b"MZ", b"\x7fELF", b"\xcf\xfa\xed\xfe", b"\xce\xfa\xed\xfe", b"\xca\xfe\xba\xbe", b"\xfe\xed\xfa")

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RESERVED_NAME_WORDS = ("anthropic", "claude")

# ---------------------------------------------------------------- rules
# (id, severity, regex, scope, message)
#   scope "text": every line of every text file, full severity
#   scope "code": code files at full severity; fenced / inline code inside
#                 docs at one severity level lower
_I = re.I
RULES: list[tuple[str, str, "re.Pattern[str]", str, str, "re.Pattern[str] | None"]] = []

# Lines that talk ABOUT attacks (docs, detectors) rather than issuing them.
DEFENSIVE_RE = re.compile(
    r"\b(detect(?:s|ing|ion)?|treat(?:ed)? (?:it |them |this )?as (?:data|untrusted)|untrusted|do not follow|"
    r"don'?t follow|never follow|must not follow|prompt[- ]injection|injection attacks?|attack(?:s|er|ers)?|"
    r"malicious|suspicious|red flags?|phishing|refuse|not instructions|embedded instructions)\b", re.I)


def _rule(rid: str, sev: str, pattern: str, scope: str, msg: str, flags: int = _I,
          unless: str | None = None) -> None:
    RULES.append((rid, sev, re.compile(pattern, flags), scope, msg,
                  re.compile(unless, re.I) if unless else None))


# ---- prompt injection / manipulation of the model
_rule("inj-override", "high",
      r"\b(ignore|disregard|forget|override)\b\s+(?:(?:all|any|the|your|every|of)\s+)*(previous|prior|above|earlier|preceding|system|safety|security|original)\s+(instructions?|rules?|prompts?|guidelines?|polic(?:y|ies)|restrictions?|guardrails?|messages?)\b",
      "text", "Tells the model to ignore or override prior/system instructions")
_rule("inj-roleplay", "high",
      r"\byou are now\b[^.\n]{0,40}\b(dan|jailbreak|unrestricted|developer mode|root|admin|evil|uncensored|without (any )?(rules|restrictions|limits))",
      "text", "Jailbreak-style persona switch")
_rule("inj-conceal", "high",
      r"\b(do not|don'?t|never)\s+(?:ever\s+)?(?:tell|inform|notify|mention|reveal|disclose|alert)\s+(?:the\s+|this\s+)?(?:user|human|operator)\s+(?:about|of)\s+(?:this|these|that|it|what|how|any)\b|\b(do not|don'?t|never)\s+(?:ever\s+)?(?:tell|mention|reveal|disclose|show)\s+(?:this|that|it|these|any of this)\s+to\s+(?:the\s+)?(?:user|human|operator)\b|\b(hide|conceal)\b[^.\n]{0,30}\bfrom the (user|human)\b",
      "text", "Instructs the model to conceal actions from the user")
_rule("inj-silent", "medium",
      r"\bwithout (telling|informing|notifying|alerting) the (user|human)\b",
      "text", "Acts without telling the user",
      unless=r"\b(never|not|don'?t|avoid|shouldn'?t|mustn'?t)\b[^.\n]{0,80}without (telling|informing|notifying|alerting)")
_rule("inj-secret-exfil", "high",
      r"\b(send|post|upload|exfiltrate|transmit|forward|leak|email|curl)\b[^.\n]{0,60}\b(api[ _-]?keys?|secrets?|access tokens?|passwords?|credentials?|private keys?|ssh keys?|\.env\b|cookies?|system prompt)\b[^.\n]{0,80}(https?://|webhook|discord|telegram|pastebin|@[a-z0-9.-]+\.[a-z]{2,})",
      "text", "Instructs sending secrets/credentials to an external destination")
_rule("inj-reveal-prompt", "medium",
      r"\b(reveal|print|output|repeat|show|display|leak)\b[^.\n]{0,30}\b(your|the)\s+(system prompt|hidden instructions|initial instructions)",
      "text", "Asks the model to reveal its system prompt")
_rule("inj-fake-tags", "medium",
      r"<\|?(im_start|im_end|system|endoftext)\|?>|\[/?SYSTEM\]|<system-reminder>",
      "text", "Fake system/role delimiters that can confuse the model")
_rule("rank-manipulation", "medium",
      r"\b(always|must)\s+(use|invoke|trigger|load)\s+this\s+skill\b|\btakes?\s+(precedence|priority)\s+over\b[^.\n]{0,30}\bskills?\b|\bhighest[- ]priority skill\b|\bthis skill (replaces|supersedes|overrides)\b[^.\n]{0,30}\b(other|all)\b|\bignore (all )?other skills\b",
      "text", "Tries to bias skill selection (ranking manipulation)")
_rule("perm-bypass", "medium",
      r"--dangerously-skip-permissions|\bbypassPermissions\b|dangerouslyDisableSandbox|skipDangerousModePermissionPrompt|--no-verify\b",
      "text", "Mentions disabling permission or safety checks")
_rule("no-confirm", "low",
      r"\bwithout (asking|confirmation|confirming|approval|permission)\b",
      "text", "Acts without user confirmation (autonomy flag)")

# ---- code & shell behaviour
_rule("exec-remote", "high",
      r"\b(curl|wget|iwr|irm|Invoke-WebRequest|Invoke-RestMethod)\b[^\n|;]*\|\s*(sudo\s+)?(ba|z|da|k)?sh\b|\b(iwr|irm|Invoke-WebRequest|Invoke-RestMethod)\b[^\n]*\|\s*iex\b|\biex\s*\(.{0,80}(DownloadString|Invoke-WebRequest|Invoke-RestMethod)|\bbash\s+<\(\s*curl",
      "code", "Downloads and executes remote code")
_rule("exec-obfuscated", "high",
      r"base64\s+(-d|--decode)[^\n]*\|\s*(ba)?sh\b|(?<![\w.])(eval|exec)\s*\(.{0,60}(b64decode|fromCharCode|atob\(|bytes\.fromhex|codecs\.decode|Buffer\.from\([^)]*base64)|\b(window|global|globalThis)\.eval\s*\(.{0,60}(atob|fromCharCode|base64)|\bpowershell(\.exe)?\b[^\n]*\s-(enc|encodedcommand)\b|\\x[0-9a-f]{2}(\\x[0-9a-f]{2}){12,}",
      "code", "Obfuscated/encoded code execution")
_rule("exec-dynamic", "medium",
      r"(?<![\w.])(eval|exec)\s*\(|\bnew Function\s*\(|\bos\.system\s*\(|subprocess\.[a-z_]+\([^)\n]*shell\s*=\s*True|\bchild_process\b[^\n]*\bexec(Sync)?\s*\(|\bcompile\s*\(.{0,40}['\"]exec['\"]",
      "code", "Dynamic code execution or shell=True")
_rule("cred-paths", "high",
      r"\.ssh[/\\](id_|authorized_keys|known_hosts)|\.aws[/\\]credentials|\.config[/\\]gcloud|\.git-credentials|\.docker[/\\]config\.json|\.kube[/\\]config|Application Support[/\\](Google[/\\]Chrome|Firefox)|AppData[/\\](Local|Roaming)[/\\][^\n'\"]{0,40}(Chrome|Edge|Brave|Firefox)|\.claude[/\\]\.credentials",
      "code", "Touches credential / browser-profile / key material paths")
_rule("cred-names", "medium",
      r"\.npmrc\b|\.pypirc\b|Login Data|Local State\b|wallet\.dat|\.credentials\.json|\bid_rsa\b|\bid_ed25519\b|\bkeychain\b",
      "code", "Mentions credential files or key names")
_rule("env-dump", "medium",
      r"json\.dumps\(\s*(dict\()?os\.environ|JSON\.stringify\(\s*process\.env|\bprintenv\b|(^|[|;&]\s*)env\s*\||Get-ChildItem\s+env:",
      "code", "Dumps the entire environment (may contain secrets)")
_rule("exfil-sink", "high",
      r"webhook\.site|pastebin\.com|transfer\.sh|ngrok(-free)?\.(io|app|dev)|discord(app)?\.com/api/webhooks|api\.telegram\.org/bot|requestbin|pipedream\.net|interact\.sh|oast\.(fun|live|me|online|pro|site)|burpcollaborator|file\.io\b|0x0\.st|anonfiles|hastebin|ghostbin|paste\.ee|temp\.sh|bashupload|\.onion\b|serveo\.net|localhost\.run|trycloudflare\.com",
      "text", "Known data-exfiltration / tunnelling endpoint")
_rule("raw-ip-url", "high",
      r"https?://(?!(?:127\.0\.0\.1|0\.0\.0\.0|10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)\b)\d{1,3}(?:\.\d{1,3}){3}",
      "text", "Fetches from a raw public IP address")
_rule("url-shortener", "medium",
      r"https?://(bit\.ly|tinyurl\.com|t\.co|goo\.gl|is\.gd|cutt\.ly|rb\.gy|ow\.ly|shorturl\.at)/",
      "text", "URL shortener hides the real destination")
_rule("destructive", "high",
      r"\brm\s+-[a-z]*r[a-z]*f?[a-z]*\s+(--no-preserve-root\s+)?(/|~|\$HOME|\"\$HOME\"|\*)(\s|$|\")|\bdel\s+/[sfq]\b[^\n]*\b[a-z]:\\|Remove-Item\b[^\n]*-Recurse[^\n]*(C:\\|\$env:USERPROFILE|~)|\bformat\s+[a-z]:|\bmkfs\.|\bdd\s+if=[^\n]*of=/dev/|:\(\)\s*\{\s*:\|:&\s*\};:",
      "code", "Destructive filesystem command")
_rule("persistence", "high",
      r"\bcrontab\b|\bschtasks\b[^\n]*/create|CurrentVersion\\Run|\breg\s+add\b|\blaunchctl\s+load\b|\bsystemctl\s+(--user\s+)?enable\b|>>\s*~?/?\.?(bashrc|zshrc|profile|bash_profile)\b|\\Start Menu\\Programs\\Startup|Register-ScheduledTask",
      "code", "Installs persistence (cron, scheduled task, startup, shell rc)")
_rule("cfg-tamper", "medium",
      r"(?:~|\$HOME|%USERPROFILE%|\$env:USERPROFILE)[/\\]\.claude[/\\](settings|\.claude\.json|CLAUDE\.md|hooks|plugins)",
      "code", "Reads/writes the user's Claude configuration")
_rule("priv-esc", "medium",
      r"\bsudo\s|chmod\s+(\+s|-R\s+777|777)\b|\bchown\s+root\b|Start-Process\b[^\n]*-Verb\s+RunAs|\brunas\b",
      "code", "Privilege escalation")
_rule("download-exec", "medium",
      r"\b(curl|wget|Invoke-WebRequest|iwr)\b[^\n]*(-o|-OutFile|>)\s*\S+\.(exe|msi|dll|ps1|sh|bat|cmd)\b|\bchmod\s+\+x\b[^\n]*(&&|;)[^\n]*\./",
      "code", "Downloads an executable and runs it")
_rule("unpinned-install", "low",
      r"\bnpx\s+-y\b|\bnpm\s+(i|install)\s+-g\b|\bpip3?\s+install\s+(?!-r\b)(?![^\n]*==)[a-z]",
      "code", "Installs unpinned third-party packages")
_rule("secret-material", "high",
      r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
      "text", "Embedded private key", re.I)
_rule("leaked-token", "medium",
      r"\bAKIA[0-9A-Z]{16}\b|\bghp_[A-Za-z0-9]{36}\b|\bgithub_pat_[A-Za-z0-9_]{50,}|\bsk-[A-Za-z0-9]{32,}|\bxox[baprs]-[A-Za-z0-9-]{10,}",
      "text", "Looks like a leaked credential", 0)

DOWNGRADE = {"critical": "high", "high": "medium", "medium": "low", "low": "info", "info": "info"}

_ZW_RE = re.compile("[\u200b\u200c\u2060\ufeff]")
_BIDI_RE = re.compile("[\u202a-\u202e\u2066-\u2069]")
_TAG_RE = re.compile("[\U000e0000-\U000e007f]")
_FLAG_SEQ_RE = re.compile("\U0001F3F4[\U000e0020-\U000e007e]+\U000e007f")  # legit subdivision flags


# ---------------------------------------------------------------- frontmatter
_FM_RE = re.compile(r"\A\ufeff?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", re.S)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (meta, body). Lenient: falls back to a line parser if YAML fails."""
    m = _FM_RE.match(text)
    if not m:
        return {}, text
    raw, body = m.group(1), text[m.end():]
    if yaml is not None:
        try:
            data = yaml.safe_load(raw)
            if isinstance(data, dict):
                return {str(k): v for k, v in data.items()}, body
        except Exception:
            pass
    data: dict = {}
    key = None
    for line in raw.splitlines():
        km = re.match(r"^([A-Za-z0-9_.-]+):\s*(.*)$", line)
        if km and not line.startswith((" ", "\t")):
            key = km.group(1)
            val = km.group(2).strip()
            if val in (">", "|", ">-", "|-", ">+", "|+"):
                val = ""
            data[key] = val.strip("\"'")
        elif key is not None and line.strip():
            data[key] = (str(data[key]) + " " + line.strip()).strip()
    return data, body


# ---------------------------------------------------------------- helpers
def _sev_max(a: str, b: str) -> str:
    return a if SEV_ORDER.index(a) >= SEV_ORDER.index(b) else b


def _excerpt(line: str, m: "re.Match[str] | None" = None, width: int = 110) -> str:
    s = line.strip()
    if m is not None:
        start = max(0, m.start() - 30)
        s = line[start:start + width].strip()
    s = _TAG_RE.sub("?", s)
    s = _BIDI_RE.sub("?", s)
    return s[:width]


def _kind(rel: str) -> str:
    ext = os.path.splitext(rel.lower())[1]
    base = os.path.basename(rel).lower()
    if ext in DOC_EXT or base in ("skill.md", "license", "readme", "notice"):
        return "doc"
    if ext in CODE_EXT:
        return "code"
    if ext in DATA_EXT or base in (".gitignore", ".env", ".env.example", "makefile", "dockerfile"):
        return "data"
    if ext in BAD_BINARY_EXT:
        return "badbin"
    if ext in ARCHIVE_EXT:
        return "archive"
    if ext in BENIGN_BINARY_EXT:
        return "binary"
    return "unknown"


def _looks_binary(data: bytes) -> bool:
    if b"\x00" in data[:4096]:
        return True
    try:
        data[:4096].decode("utf-8")
        return False
    except UnicodeDecodeError:
        return True


class _Collector:
    def __init__(self) -> None:
        self.findings: list[dict] = []
        self._seen: set[tuple] = set()

    def add(self, rule: str, sev: str, file: str, line: int, msg: str, excerpt: str = "") -> None:
        key = (rule, file, line)
        if key in self._seen:
            return
        self._seen.add(key)
        self.findings.append({
            "rule": rule, "severity": sev, "file": file, "line": line,
            "message": msg, "excerpt": excerpt,
        })


def _scan_text(col: _Collector, rel: str, text: str, kind: str) -> None:
    # invisible unicode
    for lineno, line in enumerate(text.splitlines(), 1):
        if _TAG_RE.search(_FLAG_SEQ_RE.sub("", line)):
            col.add("hidden-unicode-tag", "critical", rel, lineno,
                    "Unicode tag characters (invisible text, a known prompt-smuggling trick)", _excerpt(line))
        if _BIDI_RE.search(line):
            col.add("bidi-control", "high", rel, lineno,
                    "Bidirectional control characters can disguise text", _excerpt(line))
    zw = _ZW_RE.findall(text[1:] if text.startswith("\ufeff") else text)
    if zw:
        col.add("zero-width-chars", "high" if len(zw) >= 10 else "medium", rel, 0,
                f"{len(zw)} zero-width characters in text", "")

    in_fence = False
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        if kind == "doc" and (stripped.startswith("```") or stripped.startswith("~~~")):
            in_fence = not in_fence
        code_context = kind == "code" or (kind == "doc" and (in_fence or "`" in line)) or kind == "data"
        for rid, sev, rx, scope, msg, unless in RULES:
            if scope == "code":
                if not code_context:
                    continue
                eff = sev if kind in ("code", "data") else DOWNGRADE[sev]
            else:
                eff = sev
            m = rx.search(line)
            if m:
                if unless is not None and unless.search(line):
                    continue
                if rid.startswith("inj-") and DEFENSIVE_RE.search(line):
                    eff = DOWNGRADE[eff]
                col.add(rid, eff, rel, lineno, msg, _excerpt(line, m))


def _scan_frontmatter(col: _Collector, meta: dict, dirname: str | None, has_fm: bool) -> None:
    f = "SKILL.md"
    if not has_fm or not meta:
        col.add("fm-missing", "medium", f, 1, "SKILL.md has no YAML frontmatter")
        return
    name = str(meta.get("name", "")).strip()
    desc = str(meta.get("description", "")).strip()
    if not name:
        col.add("fm-name", "medium", f, 1, "frontmatter 'name' missing")
    else:
        if not NAME_RE.match(name) or len(name) > 64:
            col.add("fm-name-format", "low", f, 1, f"name '{name[:40]}' is not lowercase-hyphen <=64 chars")
        if any(w in name for w in RESERVED_NAME_WORDS):
            col.add("fm-name-reserved", "low", f, 1, "name contains a reserved word (claude.ai upload rejects it)")
        if dirname and dirname != name:
            col.add("fm-name-dir", "info", f, 1, f"name '{name}' differs from directory '{dirname}'")
    if not desc:
        col.add("fm-desc", "medium", f, 1, "frontmatter 'description' missing")
    else:
        if len(desc) > 1024:
            col.add("fm-desc-long", "low", f, 1, f"description is {len(desc)} chars (limit 1024)")
        if re.search(r"<[a-zA-Z/][^>]*>", desc):
            col.add("fm-desc-xml", "low", f, 1, "description contains XML/HTML tags")
        terms = [t for t in re.split(r"[,;/|]", desc) if t.strip()]
        words = re.findall(r"[a-z]{3,}", desc.lower())
        if len(terms) > 45 or (len(words) > 60 and len(set(words)) / max(len(words), 1) < 0.35):
            col.add("fm-desc-stuffing", "medium", f, 1, "description looks keyword-stuffed (ranking manipulation)")
    allowed = meta.get("allowed-tools") or meta.get("allowed_tools")
    if allowed:
        tools = " ".join(allowed) if isinstance(allowed, list) else str(allowed)
        if re.search(r"(^|[\s,\[])\*($|[\s,\]])", tools):
            col.add("perm-all-tools", "medium", f, 1, "allowed-tools pre-approves every tool")
        elif re.search(r"(^|[\s,\[])(Bash|Bash\(\*\)|Bash\(\*:\*\))($|[\s,\]])", tools):
            col.add("perm-broad-bash", "low", f, 1, "allowed-tools pre-approves unrestricted Bash")


def vet_blobs(files: dict[str, bytes], symlinks: list[str] | None = None,
              dirname: str | None = None) -> dict:
    """Vet a skill given as {relative_path: bytes}."""
    col = _Collector()
    symlinks = symlinks or []
    total = sum(len(b) for b in files.values())
    if len(files) > MAX_FILES:
        col.add("too-many-files", "medium", "", 0, f"{len(files)} files (limit {MAX_FILES})")
    if total > MAX_TOTAL_BYTES:
        col.add("too-large", "medium", "", 0, f"{total} bytes total (limit {MAX_TOTAL_BYTES})")
    for s in symlinks:
        col.add("symlink", "high", s, 0, "Symlink inside skill (can point outside the skill directory)")

    skill_md = files.get("SKILL.md")
    if skill_md is None:
        col.add("no-skill-md", "high", "", 0, "No SKILL.md at the skill root")
        meta, body = {}, ""
    else:
        text = skill_md.decode("utf-8", errors="replace")
        meta, body = parse_frontmatter(text)
        _scan_frontmatter(col, meta, dirname, bool(_FM_RE.match(text)))
        if text.count("\n") > 500:
            col.add("skill-md-long", "info", "SKILL.md", 0, f"SKILL.md has {text.count(chr(10))} lines (recommended <500)")

    hashes: dict[str, str] = {}
    for rel in sorted(files):
        data = files[rel]
        hashes[rel] = hashlib.sha256(data).hexdigest()
        parts = Path(rel).parts
        if ".." in parts or rel.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:", rel):
            col.add("path-traversal", "high", rel, 0, "Path escapes the skill directory")
            continue
        if any(p == "node_modules" for p in parts):
            col.add("vendored-deps", "medium", rel, 0, "Vendored node_modules cannot be reviewed")
            continue
        kind = _kind(rel)
        base = os.path.basename(rel).lower()
        if base in (".npmrc", ".pypirc", ".netrc", ".env") and kind != "doc":
            col.add("secret-file", "medium", rel, 0, f"Ships a {base} file")
        if len(data) > MAX_FILE_BYTES:
            col.add("big-file", "medium", rel, 0, f"File is {len(data)} bytes (limit {MAX_FILE_BYTES})")
        exec_magic = any(data.startswith(m) for m in MAGIC_BAD) and (
            kind not in ("doc", "code", "data") or _looks_binary(data))
        if kind == "badbin" or exec_magic:
            col.add("binary-executable", "high", rel, 0, "Executable/binary payload")
            continue
        if kind == "archive":
            col.add("nested-archive", "medium", rel, 0, "Nested archive cannot be reviewed")
            continue
        if kind in ("binary",):
            continue
        if kind == "unknown" and _looks_binary(data):
            col.add("opaque-binary", "medium", rel, 0, "Unrecognised binary file")
            continue
        text = data.decode("utf-8", errors="replace")
        _scan_text(col, rel, text, kind if kind != "unknown" else "data")
        if base == "package.json":
            try:
                scripts = (json.loads(text).get("scripts") or {})
                for hook in ("preinstall", "install", "postinstall", "prepare"):
                    if hook in scripts:
                        col.add("npm-install-hook", "high", rel, 0,
                                f"package.json runs '{hook}' script on install", str(scripts[hook])[:100])
            except Exception:
                pass
        if base == "setup.py" and re.search(r"cmdclass|os\.system|subprocess", text):
            col.add("setup-py-hook", "high", rel, 0, "setup.py executes code at install time")

    # score
    per_rule: dict[str, int] = {}
    penalty = 0
    worst = "info"
    for f in col.findings:
        worst = _sev_max(worst, f["severity"])
        n = per_rule.get(f["rule"], 0)
        if n < 3:
            penalty += PENALTY[f["severity"]]
        per_rule[f["rule"]] = n + 1
    score = max(0, 100 - penalty)
    if SEV_ORDER.index(worst) >= SEV_ORDER.index("high"):
        verdict = "fail"
    elif worst == "medium":
        verdict = "review"
    else:
        verdict = "pass"
    tree = hashlib.sha256("\n".join(f"{k}:{v}" for k, v in sorted(hashes.items())).encode()).hexdigest()
    col.findings.sort(key=lambda f: (-SEV_ORDER.index(f["severity"]), f["file"], f["line"]))
    return {
        "name": str(meta.get("name", "") or dirname or ""),
        "verdict": verdict,
        "score": score,
        "worst": worst,
        "files": len(files),
        "bytes": total,
        "tree_sha256": tree,
        "file_hashes": hashes,
        "counts": {s: sum(1 for f in col.findings if f["severity"] == s) for s in SEV_ORDER},
        "findings": col.findings,
    }


def collect_dir(path: Path) -> tuple[dict[str, bytes], list[str]]:
    files: dict[str, bytes] = {}
    links: list[str] = []
    root = path.resolve()
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for d in list(dirnames):
            full = Path(dirpath) / d
            if full.is_symlink():
                links.append(str(full.relative_to(root)).replace("\\", "/"))
                dirnames.remove(d)
        for fn in filenames:
            full = Path(dirpath) / fn
            rel = str(full.relative_to(root)).replace("\\", "/")
            if full.is_symlink():
                links.append(rel)
                continue
            try:
                if full.stat().st_size > MAX_FILE_BYTES * 4:
                    files[rel] = b"\x00" * (MAX_FILE_BYTES + 1)  # placeholder -> big-file finding
                    continue
                files[rel] = full.read_bytes()
            except OSError:
                continue
    return files, links


def vet_dir(path: str | Path) -> dict:
    p = Path(path)
    files, links = collect_dir(p)
    return vet_blobs(files, links, dirname=p.resolve().name)


# ---------------------------------------------------------------- CLI
def _print_report(rep: dict, verbose: bool = True) -> None:
    icon = {"pass": "PASS", "review": "REVIEW", "fail": "FAIL"}[rep["verdict"]]
    print(f"[{icon}] {rep['name'] or '(unnamed)'}  score={rep['score']}  files={rep['files']}  bytes={rep['bytes']}")
    print(f"       tree_sha256={rep['tree_sha256']}")
    c = rep["counts"]
    print("       findings: " + ", ".join(f"{k}={v}" for k, v in c.items() if v) if any(c.values()) else "       findings: none")
    if verbose:
        for f in rep["findings"]:
            if f["severity"] == "info":
                continue
            loc = f"{f['file']}:{f['line']}" if f["line"] else f["file"]
            print(f"  - [{f['severity'].upper():8}] {f['rule']}: {f['message']} ({loc})")
            if f["excerpt"]:
                print(f"      > {f['excerpt']}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Static security vetting for an Agent Skill directory")
    ap.add_argument("path", help="skill directory (contains SKILL.md)")
    ap.add_argument("--json", action="store_true", help="print JSON report")
    ap.add_argument("--fail-on", choices=["medium", "high"], default="high",
                    help="exit non-zero threshold (default high; 'medium' also fails review)")
    ns = ap.parse_args(argv)
    rep = vet_dir(ns.path)
    if ns.json:
        slim = {k: v for k, v in rep.items() if k != "file_hashes"}
        print(json.dumps(slim, indent=2, ensure_ascii=False))
    else:
        _print_report(rep)
    if rep["verdict"] == "fail":
        return 2
    if rep["verdict"] == "review":
        return 1 if ns.fail_on == "medium" else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
