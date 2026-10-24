# research-phase

> Research how to implement a phase (standalone - usually use /bm:plan-phase instead)

| | |
|---|---|
| **ID** | `bm:research-phase` |
| **Pack** | Spec-driven Dev Workflow (also: Product Management, Research & Learning) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 196 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Research how to implement a phase. Spawns gsd-phase-researcher agent with phase context.

## How it is structured

The skill's own section headings, in order:

- 0. Initialize Context
- 1. Validate Phase
- 2. Check Existing Research
- 3. Gather Phase Context
- 4. Spawn gsd-phase-researcher Agent
- 5. Handle Agent Return
- 6. Spawn Continuation Agent

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Task`

## Related skills

- [bm:execute-phase](bm-execute-phase.md) - Execute all plans in a phase with wave-based parallelization
- [bm:plan-phase](bm-plan-phase.md) - Create detailed phase plan (PLAN.md) with verification loop
- [bm:autonomous](bm-autonomous.md) - Run all remaining phases autonomously — discuss→plan→execute per phase
- [bm:list-phase-assumptions](bm-list-phase-assumptions.md) - Surface Claude's assumptions about a phase approach before planning

## Invoke / install

- Invoke: `/bm:research-phase`  (Skill tool: `bm:research-phase`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
