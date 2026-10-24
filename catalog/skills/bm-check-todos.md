# check-todos

> List pending todos and select one to work on

| | |
|---|---|
| **ID** | `bm:check-todos` |
| **Pack** | Spec-driven Dev Workflow (also: Productivity & Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 46 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> List all pending todos, allow selection, load full context for the selected todo, and route to appropriate action.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `AskUserQuestion`

## Related skills

- [bm:note](bm-note.md) - Zero-friction idea capture. Append, list, or promote notes to todos.
- [productivity:start](productivity-start.md) - Initialize the productivity system and open the dashboard. Use when setting up the plugin for the first time, 
- [schedule](schedule.md) - Create, update, list or run scheduled cloud agents (routines) on a cron schedule. Use for recurring cloud agen
- [bm:list-workspaces](bm-list-workspaces.md) - List active GSD workspaces and their status

## Invoke / install

- Invoke: `/bm:check-todos`  (Skill tool: `bm:check-todos`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
