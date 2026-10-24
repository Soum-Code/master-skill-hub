# settings

> Configure GSD workflow toggles and model profile

| | |
|---|---|
| **ID** | `bm:settings` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 37 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Interactive configuration of GSD workflow agents and model profile via multi-question prompt.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Bash`, `AskUserQuestion`

## Related skills

- [bm:set-profile](bm-set-profile.md) - Switch model profile for GSD agents (quality/balanced/budget/inherit)
- [bm:next](bm-next.md) - Automatically advance to the next logical step in the GSD workflow
- [cowork-plugin-management:cowork-plugin-customizer](cowork-plugin-management-cowork-plugin-customizer.md) - Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, 
- [update-config](update-config.md) - Configure the Claude Code harness via settings.json - hooks, permissions, environment variables and other auto

## Invoke / install

- Invoke: `/bm:settings`  (Skill tool: `bm:settings`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
