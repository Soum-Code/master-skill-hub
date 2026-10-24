# from-gsd2

> Import a GSD-2 (.gsd/) project back to GSD v1 (.planning/) format

| | |
|---|---|
| **ID** | `bm:from-gsd2` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 48 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Reverse-migrate a GSD-2 project (`.gsd/` directory) back to GSD v1 (`.planning/`) format.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`

## Related skills

- [bm:import](bm-import.md) - Ingest external plans with conflict detection against project decisions before writing anything.
- [bm:graphify](bm-graphify.md) - Build, query, and inspect the project knowledge graph in .planning/graphs/
- [bm:stats](bm-stats.md) - Display project statistics — phases, plans, requirements, git metrics, and timeline
- [bm:undo](bm-undo.md) - Safe git revert. Roll back phase or plan commits using the phase manifest with dependency checks.

## Invoke / install

- Invoke: `/bm:from-gsd2`  (Skill tool: `bm:from-gsd2`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
