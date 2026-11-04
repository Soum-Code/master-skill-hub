# terminal-opener

> Open an executable and its argument array in a visible terminal window through a reusable, shell-free launch plan with dry-run, JSON, capability detection, detached fallback, and standalone recovery modes. Use when Codex needs to open an interactive CLI, SSH session, local development process, sandbox, or other argv-based command in a new host terminal; diagnose whether a supported terminal is available; or provide an actionable plan when the requested terminal is unsupported.

| | |
|---|---|
| **ID** | `affaan-m/ECC:terminal-opener` |
| **Pack** | Spec-driven Dev Workflow (also: Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 56 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when Codex needs to open an interactive CLI, SSH session, local development process, sandbox, or other argv-based command in a new host terminal; diagnose whether a supported terminal is available; or provide an actionable plan when the requested terminal.

## What it says up front

> Use `scripts/open-terminal.js` to preserve an executable and every argument as separate process entries. Never interpolate a shell command string. Keep every spawn on `shell: false`. Default to a non-launching plan. Use `--launch` only after the user explicitly requests a real window and the argv ha

## How it is structured

The skill's own section headings, in order:

- Launch a command
- Recover from terminal configuration
- Inspect before launch

## What it bundles

- scripts: `scripts/open-terminal.js`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/affaan-m/ECC:terminal-opener`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/terminal-opener --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 06bf02fb27a613a7bb4c3cd8d1e3b63cd2d51563518756837bf16114e84405a9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
