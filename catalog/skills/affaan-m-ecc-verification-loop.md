# verification-loop

> Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, security grep, and diff review — then produce a PASS/FAIL verification report. Use when verifying work after completing a feature or refactor, before creating a PR, or when quality gates must pass.

| | |
|---|---|
| **ID** | `affaan-m/ECC:verification-loop` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 151 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when verifying work after completing a feature or refactor, before creating a PR, or when quality gates must pass.

## What it says up front

> A comprehensive verification system for Claude Code sessions.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Verification Phases
  - Phase 1: Build Verification
  - Phase 2: Type Check
  - Phase 3: Lint Check
  - Phase 4: Test Suite
  - Phase 5: Security Scan
  - Phase 6: Diff Review
- Target Acceptance
- Output Format
- Continuous Mode
- Integration with Hooks

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:django-verification](affaan-m-ecc-django-verification.md) - Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest w
- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 
- [affaan-m/ECC:laravel-verification](affaan-m-ecc-laravel-verification.md) - Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security sc
- [affaan-m/ECC:codehealth-mcp](affaan-m-ecc-codehealth-mcp.md) - Real-time structural Code Health via CodeScene MCP — review before edits, verify score deltas after changes, g

## Invoke / install

- Invoke: `/affaan-m/ECC:verification-loop`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/verification-loop --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree a8cf012ce6f29c109c77cb7340cd00d84a6b8ea5517591056861a8b6efbbf0d7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
