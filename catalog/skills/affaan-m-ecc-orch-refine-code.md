# orch-refine-code

> Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, keep tests green, review, and gated commit. Use when the structure should improve but behavior must not change.

| | |
|---|---|
| **ID** | `affaan-m/ECC:orch-refine-code` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 45 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the structure should improve but behavior must not change.

## What it says up front

> Actor · action · target: **orch · refine · code**. Thin wrapper over the shared engine in [`orch-pipeline`](../orch-pipeline/SKILL.md).

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

- [affaan-m/ECC:orch-change-feature](affaan-m-ecc-orch-change-feature.md) - Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, 
- [affaan-m/ECC:orch-fix-defect](affaan-m-ecc-orch-fix-defect.md) - Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit —
- [affaan-m/ECC:orch-add-feature](affaan-m-ecc-orch-add-feature.md) - Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated co
- [simplify](simplify.md) - Review changed code for reuse, simplification, efficiency and altitude cleanups, then apply the fixes. Quality

## Invoke / install

- Invoke: `/affaan-m/ECC:orch-refine-code`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/orch-refine-code --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 5202bb6860d6a1cf09ed8b58000b5c195383bf630dab052f4efc2509169993b8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
