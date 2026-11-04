# orch-pipeline

> Shared orchestration engine behind the orch-* skill family — the gated Research-Plan-TDD-Review-Commit pipeline, size classifier, agent and command map, and two human gates (plan approval, commit confirmation) that orch-* operation skills delegate to. Use indirectly via orch-add-feature, orch-fix-defect, orch-change-feature, orch-refine-code, or orch-build-mvp; read directly only when adding an orch operation or tuning shared phases.

| | |
|---|---|
| **ID** | `affaan-m/ECC:orch-pipeline` |
| **Pack** | MLOps / DevOps / Cloud (also: Spec-driven Dev Workflow, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 122 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> The `orch-*` skills are thin wrappers. They do not re-implement any work — they classify the request, choose which phases of *this* pipeline run, and delegate each phase to an existing ECC agent or command. This file is that pipeline.

## How it is structured

The skill's own section headings, in order:

- When to Use
- The operation family
- Step 0 — Classify size (right-sizing)
- The phases
- The two gates
- Agent / command map
- Security-review trigger
- Handoff artifacts
- Verification

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:orch-add-feature](affaan-m-ecc-orch-add-feature.md) - Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated co
- [affaan-m/ECC:orch-fix-defect](affaan-m-ecc-orch-fix-defect.md) - Orchestrate fixing a bug — reproduce it as a failing regression test, fix to green, review, and gated commit —
- [affaan-m/ECC:orch-refine-code](affaan-m-ecc-orch-refine-code.md) - Orchestrate a behavior-preserving refactor — confirm tests are green, restructure without changing behavior, k
- [affaan-m/ECC:orch-change-feature](affaan-m-ecc-orch-change-feature.md) - Orchestrate altering an existing, working feature to new desired behavior — update its tests to the new spec, 

## Invoke / install

- Invoke: `/affaan-m/ECC:orch-pipeline`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/orch-pipeline --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 0760638364c4443d1e2887286003fe2d066379559e71199b48339e20c913534e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
