# orch-add-feature

> Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated commit — by delegating each phase to the matching ECC agent. Use when adding a capability that does not exist yet.

| | |
|---|---|
| **ID** | `affaan-m/ECC:orch-add-feature` |
| **Pack** | Spec-driven Dev Workflow (also: Product Management, Research & Learning, Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 46 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adding a capability that does not exist yet.

## What it says up front

> Actor · action · target: **orch · add · feature**. Thin wrapper over the shared engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

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
- [affaan-m/ECC:orch-change-feature](affaan-m-ecc-orch-change-feature.md) - Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, 
- [affaan-m/ECC:orch-pipeline](affaan-m-ecc-orch-pipeline.md) - Shared orchestration engine behind the orch-* skill family — the gated Research-Plan-TDD-Review-Commit pipelin
- [affaan-m/ECC:orch-build-mvp](affaan-m-ecc-orch-build-mvp.md) - Orchestrate bootstrapping a working MVP from a design or spec document — ingest the SDD/PRD, plan thin vertica

## Invoke / install

- Invoke: `/affaan-m/ECC:orch-add-feature`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/orch-add-feature --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c7d91e3df800d7748b7c8c2838c7bf1e0f16e8dc2ca4e6c61013ad5d6df19c4a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
