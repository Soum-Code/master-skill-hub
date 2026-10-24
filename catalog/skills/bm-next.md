# next

> Automatically advance to the next logical step in the GSD workflow

| | |
|---|---|
| **ID** | `bm:next` |
| **Pack** | Spec-driven Dev Workflow (also: Claude / Skills / Plugin Tooling, MLOps / DevOps / Cloud, Operations & Business) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 30 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Detect the current project state and automatically invoke the next logical GSD workflow step. No arguments needed — reads STATE.md, ROADMAP.md, and phase directories to determine what comes next.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Grep`, `Glob`, `SlashCommand`

## Related skills

- [bm:do](bm-do.md) - Route freeform text to the right GSD command automatically
- [bm:settings](bm-settings.md) - Configure GSD workflow toggles and model profile
- [bm:forensics](bm-forensics.md) - Post-mortem investigation for failed GSD workflows — analyzes git history, artifacts, and state to diagnose wh
- [bm:list-workspaces](bm-list-workspaces.md) - List active GSD workspaces and their status

## Invoke / install

- Invoke: `/bm:next`  (Skill tool: `bm:next`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
