# hermes-imports

> Convert local Hermes operator workflows into sanitized ECC skills and release-pack artifacts. Use when preparing a Hermes workflow for public ECC reuse without leaking private workspace state, credentials, or local-only paths.

| | |
|---|---|
| **ID** | `affaan-m/ECC:hermes-imports` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 90 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when preparing a Hermes workflow for public ECC reuse without leaking private workspace state, credentials, or local-only paths.

## What it says up front

> Use this skill when turning a repeated Hermes workflow into something safe to ship in ECC.

## How it is structured

The skill's own section headings, in order:

- When To Use
- Import Rules
- Sanitization Checklist
- Conversion Pattern
- Example: Launch Handoff
- Example: Quiet-Hours Operator Job
- Output Contract

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:research-ops](affaan-m-ecc-research-ops.md) - Evidence-first current-state research workflow for ECC. Use when the user wants fresh facts, comparisons, enri
- [affaan-m/ECC:workspace-surface-audit](affaan-m-ecc-workspace-surface-audit.md) - Audit the active repo, MCP servers, plugins, connectors, env surfaces, and harness setup, then recommend the h
- [affaan-m/ECC:skill-host-compat](affaan-m-ecc-skill-host-compat.md) - Lint ECC skills for Codex/Cursor-safe frontmatter and Claude-only substitutions before a skill PR.

## Invoke / install

- Invoke: `/affaan-m/ECC:hermes-imports`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/hermes-imports --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5ba34ca516e5ea62176402c4bf738ba4f6855aae97b3fa4158b1f1f440574185 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
