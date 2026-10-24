# undo

> Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks.

| | |
|---|---|
| **ID** | `bm:undo` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 35 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Safe git revert — roll back GSD phase or plan commits using the phase manifest, with dependency checks and a confirmation gate before execution.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Glob`, `Grep`, `AskUserQuestion`

## Related skills

- [bm:stats](bm-stats.md) - Display project statistics — phases, plans, requirements, git metrics, and timeline
- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:analyze-dependencies](bm-analyze-dependencies.md) - Analyze phase dependencies and suggest Depends on entries for ROADMAP.md

## Invoke / install

- Invoke: `/bm:undo`  (Skill tool: `bm:undo`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
