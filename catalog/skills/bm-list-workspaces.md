# list-workspaces

> List active GSD workspaces and their status

| | |
|---|---|
| **ID** | `bm:list-workspaces` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 20 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Scan `~/gsd-workspaces/` for workspace directories containing `WORKSPACE.md` manifests. Display a summary table with name, path, repo count, strategy, and GSD project status.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash`, `Read`

## Related skills

- [bm:remove-workspace](bm-remove-workspace.md) - Remove a GSD workspace and clean up worktrees
- [bm:workstreams](bm-workstreams.md) - Manage parallel workstreams — list, create, switch, status, progress, complete, and resume
- [bm:join-discord](bm-join-discord.md) - Join the GSD Discord community
- [bm:help](bm-help.md) - Show available GSD commands and usage guide

## Invoke / install

- Invoke: `/bm:list-workspaces`  (Skill tool: `bm:list-workspaces`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
