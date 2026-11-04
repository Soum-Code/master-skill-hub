# inherit-legacy-style

> Prevent AI style drift on legacy projects by scanning the codebase for implicit conventions, resolving conflicts with the operator one at a time, and writing an enforceable .ai-style-rules.md (Golden Files, naming rules, DONTs) plus an optional CLAUDE.md hook. Use when onboarding an AI agent onto a hand-written legacy codebase or extracting a project's unwritten coding rules.

| | |
|---|---|
| **ID** | `affaan-m/ECC:inherit-legacy-style` |
| **Pack** | Software Development (also: AI / ML Engineering, Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 158 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when onboarding an AI agent onto a hand-written legacy codebase or extracting a project's unwritten coding rules.

## What it says up front

> Prevents AI code style drift in legacy projects by scanning the codebase for implicit conventions across 4 meta-architecture dimensions, resolving conflicts with the user one at a time, and crystallizing the consensus into an enforceable `.ai-style-rules.md`. Fully language- and framework-agnostic.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- When to Use
- Prerequisites
- Workflow
  - Step 0 — Auto-Detect Mode
  - Branch A — First-time Full-Scan
  - Branch B — Incremental Sniff
  - Per-Turn Enforcement
- How It Works
- Output Specification
- Anti-Patterns
- Best Practices
- Related Skills
- Examples

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Glob`, `Grep`, `Bash`, `Edit`, `Write`, `AskUserQuestion`

## Related skills

- [affaan-m/ECC:codebase-onboarding](affaan-m-ecc-codebase-onboarding.md) - Analyze an unfamiliar codebase and generate a structured onboarding guide with architecture map, key entry poi
- [affaan-m/ECC:java-coding-standards](affaan-m-ecc-java-coding-standards.md) - Java coding standards for Spring Boot and Quarkus services: naming, immutability, Optional usage, streams, exc
- [init](init.md) - Initialize a project with a CLAUDE.md that documents the codebase for future sessions.

## Invoke / install

- Invoke: `/affaan-m/ECC:inherit-legacy-style`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/inherit-legacy-style --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree faa339a938772194a3b439cc838a14a900aa2f75f4f63cb30ba541f5af00b61e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
