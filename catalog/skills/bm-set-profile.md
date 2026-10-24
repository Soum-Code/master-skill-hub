# set-profile

> Switch model profile for GSD agents (quality/balanced/budget/inherit)

| | |
|---|---|
| **ID** | `bm:set-profile` |
| **Pack** | Spec-driven Dev Workflow (also: Careers, Jobs & Hiring, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 13 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Show the following output to the user verbatim, with no extra commentary:

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash`

## Related skills

- [bm:settings](bm-settings.md) - Configure GSD workflow toggles and model profile
- [bm:quick](bm-quick.md) - Execute a quick task with GSD guarantees (atomic commits, state tracking) but skip optional agents

## Invoke / install

- Invoke: `/bm:set-profile`  (Skill tool: `bm:set-profile`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
