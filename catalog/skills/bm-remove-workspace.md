# remove-workspace

> Remove a GSD workspace and clean up worktrees

| | |
|---|---|
| **ID** | `bm:remove-workspace` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 27 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Remove a workspace directory after confirmation. For worktree strategy, runs `git worktree remove` for each member repo first. Refuses if any repo has uncommitted changes.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash`, `Read`, `AskUserQuestion`

## Related skills

- [bm:list-workspaces](bm-list-workspaces.md) - List active GSD workspaces and their status
- [bm:join-discord](bm-join-discord.md) - Join the GSD Discord community
- [bm:help](bm-help.md) - Show available GSD commands and usage guide
- [bm:remove-phase](bm-remove-phase.md) - Remove a future phase from roadmap and renumber subsequent phases

## Invoke / install

- Invoke: `/bm:remove-workspace`  (Skill tool: `bm:remove-workspace`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
