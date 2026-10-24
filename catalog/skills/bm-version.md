# version

> Print the installed GSD plugin version and check online for updates

| | |
|---|---|
| **ID** | `bm:version` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 17 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Run this and relay its output verbatim; add nothing.

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash`

## Related skills

- [bm:update](bm-update.md) - Update GSD to latest version with changelog display
- [bm:reapply-patches](bm-reapply-patches.md) - Reapply local modifications after a GSD update
- [anthropic-skills:setup-claude](anthropic-skills-setup-claude.md) - Guided setup — install role-matched plugins, connect your tools, try a skill.
- [anthropic-skills:setup-cowork](anthropic-skills-setup-cowork.md) - Guided setup — install role-matched plugins, connect your tools, try a skill.

## Invoke / install

- Invoke: `/bm:version`  (Skill tool: `bm:version`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
