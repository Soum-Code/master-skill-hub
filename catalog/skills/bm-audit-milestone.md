# audit-milestone

> Audit milestone completion against original intent before archiving

| | |
|---|---|
| **ID** | `bm:audit-milestone` |
| **Pack** | Spec-driven Dev Workflow (also: Finance & Accounting, Security & Privacy) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 37 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Verify milestone achieved its definition of done. Check requirements coverage, cross-phase integration, and end-to-end flows.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Glob`, `Grep`, `Bash`, `Task`, `Write`

## Related skills

- [bm:plan-milestone-gaps](bm-plan-milestone-gaps.md) - Create phases to close all gaps identified by milestone audit
- [bm:import](bm-import.md) - Ingest external plans with conflict detection against project decisions before writing anything.

## Invoke / install

- Invoke: `/bm:audit-milestone`  (Skill tool: `bm:audit-milestone`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
