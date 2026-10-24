# execute-phase

> Execute all plans in a phase with wave-based parallelization

| | |
|---|---|
| **ID** | `bm:execute-phase` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 68 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Execute all plans in a phase using wave-based parallel execution.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Bash`, `Task`, `TodoWrite`, `AskUserQuestion`

## Related skills

- [bm:autonomous](bm-autonomous.md) - Run all remaining phases autonomously — discuss→plan→execute per phase
- [bm:plan-milestone-gaps](bm-plan-milestone-gaps.md) - Create phases to close all gaps identified by milestone audit
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:audit-uat](bm-audit-uat.md) - Cross-phase audit of all outstanding UAT and verification items

## Invoke / install

- Invoke: `/bm:execute-phase`  (Skill tool: `bm:execute-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
