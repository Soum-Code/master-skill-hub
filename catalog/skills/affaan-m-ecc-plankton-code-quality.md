# plankton-code-quality

> Write-time code quality enforcement using Plankton — auto-formatting, linting, and Claude-powered fixes on every file edit via hooks. Use when setting up write-time formatting, linting, or auto-fix hooks on file edits.

| | |
|---|---|
| **ID** | `affaan-m/ECC:plankton-code-quality` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 329 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when setting up write-time formatting, linting, or auto-fix hooks on file edits.

## What it says up front

> Integration reference for Plankton (credit: @alxfazio), a write-time code quality enforcement system for Claude Code. Plankton runs formatters and linters on every file edit via PostToolUse hooks, then spawns Claude subprocesses to fix violations the agent didn't catch.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Three-Phase Architecture
  - What the Main Agent Sees
  - Config Protection (Defense Against Rule-Gaming)
  - Package Manager Enforcement
- Setup
  - Quick Start
  - Per-Project Integration
  - Language-Specific Dependencies
- Pairing with ECC
  - Complementary, Not Overlapping
  - Recommended Combination
  - Avoiding Hook Conflicts
- Configuration Reference
- Environment Overrides
- References
- ECC v1.8 Additions
  - Copyable Hook Profile
  - Language Gate Table
  - Config Tamper Guard
  - CI Integration Pattern
  - Health Metrics
- Gabe's addition: oxlint complexity + ratchet ceiling (JS/TS)
  - Turn on oxlint's `complexity` rule when using it
  - Model-routing row
  - The ratchet-ceiling technique

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:codehealth-mcp](affaan-m-ecc-codehealth-mcp.md) - Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, g
- [update-config](update-config.md) - Configure the Claude Code harness via settings.json - hooks, permissions, environment variables and other auto
- [bm:code-review](bm-code-review.md) - Review source files changed during a phase for bugs, security issues, and code quality problems
- [affaan-m/ECC:codebase-onboarding](affaan-m-ecc-codebase-onboarding.md) - Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry poi

## Invoke / install

- Invoke: `/affaan-m/ECC:plankton-code-quality`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/plankton-code-quality --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e1199ea4c1b2583be005b8efd81901ad9037a1d4f71671faf8577b249647c422 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
