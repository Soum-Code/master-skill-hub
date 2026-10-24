# analyze-dependencies

> Analyze phase dependencies and suggest Depends on entries for ROADMAP.md

| | |
|---|---|
| **ID** | `bm:analyze-dependencies` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 35 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Analyze the phase dependency graph for the current milestone. For each phase pair, determine if there is a dependency relationship based on: - File overlap (phases that modify the same files must be ordered) - Semantic dependencies (a phase that uses an API built by another phase) - Data flow (a pha

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`, `AskUserQuestion`

## Related skills

- [bm:add-phase](bm-add-phase.md) - Add phase to end of current milestone in roadmap
- [bm:remove-phase](bm-remove-phase.md) - Remove a future phase from roadmap and renumber subsequent phases
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:ui-phase](bm-ui-phase.md) - Generate UI design contract (UI-SPEC.md) for frontend phases

## Invoke / install

- Invoke: `/bm:analyze-dependencies`  (Skill tool: `bm:analyze-dependencies`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
