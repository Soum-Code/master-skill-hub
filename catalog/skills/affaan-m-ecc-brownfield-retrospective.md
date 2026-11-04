# brownfield-retrospective

> Run the ECC engineering process retroactively against an existing project slice. Audit current state, reconstruct past decisions, produce a four-axis gap register (thinking, coding practice, missing features, technology selection), then execute fixes forward through the plan-TDD-review pipeline. Use when adopting ECC mid-project, taking over an inherited codebase, or asking what was missed and what would have been built differently from day one.

| | |
|---|---|
| **ID** | `affaan-m/ECC:brownfield-retrospective` |
| **Pack** | Spec-driven Dev Workflow (also: Software Development, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 178 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adopting ECC mid-project, taking over an inherited codebase, or asking what was missed and what would have been built differently from day one.

## What it says up front

> Run ECC's engineering process retroactively against a project that was built without it. Pick any slice of an existing codebase, audit what exists, reconstruct how it got there, extract a four-axis gap register, then execute the fixes forward through the standard ECC pipeline.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- When Not to Use
- The Working Set
- How It Works
  - Phase 0 — Pick the Entry Point
  - Phase 1 — Present-State Audit
  - Phase 2 — Backward Reconstruction
  - Phase 3 — Gap Analysis (Four Axes)
  - Phase 4 — Redesign / Rethink
  - Phase 5 — Forward Execution
  - Phase 6 — Closure and Re-Audit
- Resuming Mid-Stream
- Anti-Patterns
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:orch-add-feature](affaan-m-ecc-orch-add-feature.md) - Orchestrate building a brand-new feature end to end — research, plan, TDD implementation, review, and gated co

## Invoke / install

- Invoke: `/affaan-m/ECC:brownfield-retrospective`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/brownfield-retrospective --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 1ef18aa168115831db94a4f1497ecc1f6c3f4dbfb6b4eb75c428f2a559971b5c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
