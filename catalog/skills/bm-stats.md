# stats

> Display project statistics — phases, plans, requirements, git metrics, and timeline

| | |
|---|---|
| **ID** | `bm:stats` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 20 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Display comprehensive project statistics including phase progress, plan execution metrics, requirements completion, git history stats, and project timeline.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`

## Related skills

- [bm:undo](bm-undo.md) - Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks.
- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:autonomous](bm-autonomous.md) - Run all remaining phases autonomously — discuss→plan→execute per phase

## Invoke / install

- Invoke: `/bm:stats`  (Skill tool: `bm:stats`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
