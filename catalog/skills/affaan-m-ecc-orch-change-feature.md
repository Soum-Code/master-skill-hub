# orch-change-feature

> Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, change the implementation to match, review, and gated commit. Use when behavior is not broken but should be different.

| | |
|---|---|
| **ID** | `affaan-m/ECC:orch-change-feature` |
| **Pack** | Operations & Business |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 44 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when behavior is not broken but should be different.

## What it says up front

> Actor · action · target: **orch · change · feature**. Thin wrapper over the shared engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

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

- [affaan-m/ECC:orch-fix-defect](affaan-m-ecc-orch-fix-defect.md) - Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit —
- [affaan-m/ECC:orch-add-feature](affaan-m-ecc-orch-add-feature.md) - Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated co
- [affaan-m/ECC:orch-refine-code](affaan-m-ecc-orch-refine-code.md) - Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, k
- [affaan-m/ECC:orch-build-mvp](affaan-m-ecc-orch-build-mvp.md) - Orchestrate bootstrapping a working MVP from a design or spec document — ingest the SDD/PRD, plan thin vertica

## Invoke / install

- Invoke: `/affaan-m/ECC:orch-change-feature`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/orch-change-feature --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 27f2effb04851529cc591ac26b16f7c8ca1a3993da7c52c40edace4e4ea90078 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
