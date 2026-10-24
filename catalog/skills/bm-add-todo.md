# add-todo

> Capture idea or task as todo from current conversation context

| | |
|---|---|
| **ID** | `bm:add-todo` |
| **Pack** | Productivity & Automation (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 48 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Capture an idea, task, or issue that surfaces during a GSD session as a structured todo for later work.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `AskUserQuestion`

## Related skills

- [bm:note](bm-note.md) - Zero-friction idea capture. Append, list, or promote notes to todos.
- [bm:add-phase](bm-add-phase.md) - Add phase to end of current milestone in roadmap
- [bm:add-backlog](bm-add-backlog.md) - Add an idea to the backlog parking lot (999.x numbering)
- [bm:plant-seed](bm-plant-seed.md) - Capture a forward-looking idea with trigger conditions — surfaces automatically at the right milestone

## Invoke / install

- Invoke: `/bm:add-todo`  (Skill tool: `bm:add-todo`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
