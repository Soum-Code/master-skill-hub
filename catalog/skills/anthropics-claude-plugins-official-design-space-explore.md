# design-space-explore

> Generates a batch of CAD variants directly in Autodesk Fusion by applying changed parameters to an engineer's existing model, never designing from scratch and never overwriting the base. Checks first whether the parameters the engineer wants to vary actually drive the model's geometry, and stops rather than generating garbage if they don't. Confirms the variant count with the engineer before generating anything. Captures mass, volume, bounding box and every other model-computed property per variant, and hands the batch off in the shape trade-study-report consumes — it does not run analysis itself. Use when someone says "explore the design space," "generate variants," "try different wall thicknesses," "run a parameter sweep," or "vary this and see what happens."

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:design-space-explore` |
| **Pack** | Research & Learning (also: Software Development, Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 235 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when someone says "explore the design space," "generate variants," "try different wall thicknesses," "run a parameter sweep," or "vary this and see what happens.".

## What it says up front

> An engineering team designing a part rarely has one answer. They have a **design space** — a range of possible designs bounded by what they're allowed to vary (wall thickness, rib count, hole pattern, material) and what the part must satisfy (envelope, mass, load, cost, manufacturability). Modeling

## How it is structured

The skill's own section headings, in order:

- Inputs
- Workflow
  - Step 1 — Connect to the CAD environment
  - Step 2 — Read the parameter set, and check what actually drives it
  - Step 3 — Confirm the variant plan
  - Step 4 — Generate, and verify each one
  - Step 5 — Capture per-variant properties
  - Step 6 — Produce the handoff manifest
  - Step 7 — Never touch the base model
- Approval gates
- Output
- Edge cases and failure modes
- Degradation
- Chain position
- Reference files

## What it bundles

- reference docs: `reference/adapt-prior-model.md`, `reference/cad-adapter.md`, `reference/parametric-check.md`, `reference/variant-generation.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:trade-study-report](anthropics-claude-plugins-official-trade-study-report.md) - Turns a filled-in trade study matrix and its analysis results into a scored comparison and a decision memo, wi

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:design-space-explore`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-for-manufacturing/skills/design-space-explore --commit f75f5b25ae94f4332be4ff5f18435741d2589bdb --expect-tree e17e977049fa34c2032dce3e98b5c6e5b43c9acfd24815b69c3ceacc26ef52f2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
