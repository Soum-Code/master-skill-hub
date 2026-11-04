# ai-regression-testing

> Regression testing strategies for AI-assisted development. Sandbox-mode API testing without database dependencies, automated bug-check workflows, and patterns to catch AI blind spots where the same model writes and reviews code. Use when adding regression coverage to AI-assisted code, or when the same model both wrote and reviewed a change.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ai-regression-testing` |
| **Pack** | Software Development (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 387 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adding regression coverage to AI-assisted code, or when the same model both wrote and reviewed a change.

## What it says up front

> Testing patterns specifically designed for AI-assisted development, where the same model writes code and reviews it — creating systematic blind spots that only automated tests can catch.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- The Core Problem
- Sandbox-Mode API Testing
  - Setup (Vitest + Next.js App Router)
  - Test Helper for Next.js API Routes
  - Writing Regression Tests
  - Testing Sandbox/Production Parity
- Integrating Tests into Bug-Check Workflow
  - Custom Command Definition
  - The Workflow
- Common AI Regression Patterns
  - Pattern 1: Sandbox/Production Path Mismatch
  - Pattern 2: SELECT Clause Omission
  - Pattern 3: Error State Leakage
  - Pattern 4: Optimistic Update Without Proper Rollback
- Strategy: Test Where Bugs Were Found
- Quick Reference
- DO / DON'T

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:orch-refine-code](affaan-m-ecc-orch-refine-code.md) - Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, k
- [engineering:testing-strategy](engineering-testing-strategy.md) - Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests fo
- [microsoft/skills:frontend-design-review](microsoft-skills-frontend-design-review.md) - Review and create distinctive, production-grade frontend interfaces with high design quality and design system
- [affaan-m/ECC:kotlin-testing](affaan-m-ecc-kotlin-testing.md) - Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Fol

## Invoke / install

- Invoke: `/affaan-m/ECC:ai-regression-testing`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ai-regression-testing --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 64ebb62a9a64069b3bf0dd28739d4f639a7efc73ea3d2d6b1cf019592a1ffceb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
