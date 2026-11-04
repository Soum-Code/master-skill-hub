# design-system

> Generate a design system from an existing codebase or audit one for visual consistency: extract tokens (colors, typography, spacing, shadows) into design-tokens.json and CSS custom properties with DESIGN.md rationale and an interactive HTML preview, score the UI across 10 dimensions, and flag AI-slop patterns. Use when starting a design system, auditing visual consistency before a redesign, or reviewing a PR that touches styling.

| | |
|---|---|
| **ID** | `affaan-m/ECC:design-system` |
| **Pack** | Software Development (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 84 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when starting a design system, auditing visual consistency before a redesign, or reviewing a PR that touches styling.

## What it says up front

> Analyzes your codebase and generates a cohesive design system:

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Mode 1: Generate Design System
  - Mode 2: Visual Audit
  - Mode 3: AI Slop Detection
- Examples

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:design-system](anthropics-knowledge-work-plugins-design-system.md) - Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded value
- [taste-skill:redesign-skill](taste-skill-redesign-skill.md) - Upgrades existing websites and apps to premium quality. Audits current design, identifies generic AI patterns,
- [bm:eval-review](bm-eval-review.md) - Retroactively audit an executed AI phase's evaluation coverage — scores each eval dimension as COVERED/PARTIAL
- [taste-skill:stitch-skill](taste-skill-stitch-skill.md) - Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium,

## Invoke / install

- Invoke: `/affaan-m/ECC:design-system`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/design-system --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1eed334e951a0878ff776a036724fc51e900b230c491d08f2355231664e20ec0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
