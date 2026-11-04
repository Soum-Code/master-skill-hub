# orch-fix-defect

> Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit — by delegating each phase to the matching ECC agent. Use when existing behavior is broken or wrong.

| | |
|---|---|
| **ID** | `affaan-m/ECC:orch-fix-defect` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 44 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when existing behavior is broken or wrong.

## What it says up front

> Actor · action · target: **orch · fix · defect**. Thin wrapper over the shared engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

## How it is structured

The skill's own section headings, in order:

- When to Use
- Operation settings
- How It Works
- Example

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:orch-add-feature](affaan-m-ecc-orch-add-feature.md) - Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated co
- [affaan-m/ECC:orch-change-feature](affaan-m-ecc-orch-change-feature.md) - Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, 
- [affaan-m/ECC:orch-refine-code](affaan-m-ecc-orch-refine-code.md) - Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, k
- [bm:code-review-fix](bm-code-review-fix.md) - Auto-fix issues found by code review in REVIEW.md. Spawns fixer agent, commits each fix atomically, produces R

## Invoke / install

- Invoke: `/affaan-m/ECC:orch-fix-defect`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/orch-fix-defect --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c0201cf2f3301509e06a621ed47e47a13e4b485dc1ad372a8d9f936492591f54 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
