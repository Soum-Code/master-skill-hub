# autonomous

> Run all remaining phases autonomously — discuss→plan→execute per phase

| | |
|---|---|
| **ID** | `bm:autonomous` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Execute all remaining milestone phases autonomously. For each phase: discuss → plan → execute. Pauses only for user decisions (grey area acceptance, blockers, validation requests).

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `Glob`, `Grep`, `AskUserQuestion`, `Task`, `Agent`

## Related skills

- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:plan-milestone-gaps](bm-plan-milestone-gaps.md) - Create phases to close all gaps identified by milestone audit
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:audit-uat](bm-audit-uat.md) - Cross-phase audit of all outstanding UAT and verification items

## Invoke / install

- Invoke: `/bm:autonomous`  (Skill tool: `bm:autonomous`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
