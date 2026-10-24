# list-phase-assumptions

> Surface Claude's assumptions about a phase approach before planning

| | |
|---|---|
| **ID** | `bm:list-phase-assumptions` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 47 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Analyze a phase and present Claude's assumptions about technical approach, implementation order, scope boundaries, risk areas, and dependencies.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Grep`, `Glob`

## Related skills

- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:autonomous](bm-autonomous.md) - Run all remaining phases autonomously — discuss→plan→execute per phase
- [bm:research-phase](bm-research-phase.md) - Research how to implement a phase (standalone - usually use /bm:plan-phase instead)

## Invoke / install

- Invoke: `/bm:list-phase-assumptions`  (Skill tool: `bm:list-phase-assumptions`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
