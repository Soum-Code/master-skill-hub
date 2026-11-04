# orch-build-mvp

> Orchestrate bootstrapping a working MVP from a design or spec document — ingest the SDD/PRD, plan thin vertical slices, scaffold the first end-to-end slice, then drive a generator-evaluator build loop with review and gated feat commits. Use when a design or spec document must become a running MVP through planned vertical slices.

| | |
|---|---|
| **ID** | `affaan-m/ECC:orch-build-mvp` |
| **Pack** | Product Management (also: Software Development, Documents, Writing & Content, Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 50 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a design or spec document must become a running MVP through planned vertical slices.

## What it says up front

> Actor · action · target: **orch · build · mvp**. Thin wrapper over the shared engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

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
- [affaan-m/ECC:orch-pipeline](affaan-m-ecc-orch-pipeline.md) - Shared orchestration engine behind the orch-* skill family — the gated Research-Plan-TDD-Review-Commit pipelin

## Invoke / install

- Invoke: `/affaan-m/ECC:orch-build-mvp`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/orch-build-mvp --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3822bf79e09dfe7171b46aa737b37ed831e31303b4312a29446823156d7cdee8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
