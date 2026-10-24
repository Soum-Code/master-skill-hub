# do

> Route freeform text to the right GSD command automatically

| | |
|---|---|
| **ID** | `bm:do` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 31 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Analyze freeform natural language input and dispatch to the most appropriate GSD command.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `AskUserQuestion`

## Related skills

- [bm:help](bm-help.md) - Show available GSD commands and usage guide
- [bm:next](bm-next.md) - Automatically advance to the next logical step in the GSD workflow
- [bm:plant-seed](bm-plant-seed.md) - Capture a forward-looking idea with trigger conditions — surfaces automatically at the right milestone
- [bm:list-workspaces](bm-list-workspaces.md) - List active GSD workspaces and their status

## Invoke / install

- Invoke: `/bm:do`  (Skill tool: `bm:do`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
