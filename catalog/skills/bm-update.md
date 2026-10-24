# update

> Update GSD to latest version with changelog display

| | |
|---|---|
| **ID** | `bm:update` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Communication & Collaboration) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 38 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Check for GSD updates, install if available, and display what changed.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash`, `AskUserQuestion`

## Related skills

- [bm:version](bm-version.md) - Print the installed GSD plugin version and check online for updates
- [bm:reapply-patches](bm-reapply-patches.md) - Reapply local modifications after a GSD update
- [bm:join-discord](bm-join-discord.md) - Join the GSD Discord community
- [bm:list-workspaces](bm-list-workspaces.md) - List active GSD workspaces and their status

## Invoke / install

- Invoke: `/bm:update`  (Skill tool: `bm:update`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
