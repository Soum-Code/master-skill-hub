# context-budget

> Routes live context checks to the native Codex or Claude Code meter without scanning files, and performs a bounded static component audit only when explicitly requested. Use for context-budget requests about remaining capacity or installed context overhead.

| | |
|---|---|
| **ID** | `affaan-m/ECC:context-budget` |
| **Pack** | Finance & Accounting |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 134 lines in SKILL.md, 1 file(s) |

## When to use it

- Use for context-budget requests about remaining capacity or installed context overhead.

## What it says up front

> Use the provider's native meter for live session usage. Keep the separate, estimated installation audit behind an explicit opt-in.

## How it is structured

The skill's own section headings, in order:

- Default: Live Context
- Explicit Static Audit
- Audit Output
- Optional Selected-Record Diagnostic

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:claude-security](anthropics-claude-plugins-official-claude-security.md) - Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's 
- [affaan-m/ECC:security-scan](affaan-m-ecc-security-scan.md) - Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and 
- [affaan-m/ECC:repo-scan](affaan-m-ecc-repo-scan.md) - Bootstrap pointer that installs the external repo-scan skill from a pinned, reviewable commit. Use when repo-s
- [affaan-m/ECC:skill-stocktake](affaan-m-ecc-skill-stocktake.md) - Use when auditing Claude skills and commands for quality. Supports Quick Scan (changed skills only) and Full S

## Invoke / install

- Invoke: `/affaan-m/ECC:context-budget`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/context-budget --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2639d7c59f9b15c340754cf22011a69d493b4f28adfe83ea709460fcfa37a70d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
