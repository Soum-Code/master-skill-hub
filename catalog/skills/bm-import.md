# import

> Ingest external plans with conflict detection against project decisions before writing anything.

| | |
|---|---|
| **ID** | `bm:import` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 38 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Import external plan files into the GSD planning system with conflict detection against PROJECT.md decisions.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Bash`, `Glob`, `Grep`, `AskUserQuestion`, `Task`

## Related skills

- [bm:from-gsd2](bm-from-gsd2.md) - Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format
- [bm:audit-milestone](bm-audit-milestone.md) - Audit milestone completion against original intent before archiving
- [bm:graphify](bm-graphify.md) - Build, query, and inspect the project knowledge graph in .planning/graphs/
- [bm:list-phase-assumptions](bm-list-phase-assumptions.md) - Surface Claude's assumptions about a phase approach before planning

## Invoke / install

- Invoke: `/bm:import`  (Skill tool: `bm:import`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
