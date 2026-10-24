# example-command

> An example user-invoked skill that demonstrates frontmatter options and the skills//SKILL.md layout

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:example-command` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 40 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> This demonstrates the `skills//SKILL.md` layout for user-invoked slash commands. It is functionally identical to the legacy `commands/example-command.md` format — both are loaded the same way; only the file layout differs.

## How it is structured

The skill's own section headings, in order:

- Arguments
- Instructions
- Frontmatter Options Reference
- Example Usage

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Glob`, `Grep`, `Bash`

## Related skills

- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-code:Plugin Settings](anthropics-claude-code-plugin-settings.md) - This skill should be used when the user asks about "plugin settings", "store plugin configuration", "user-conf

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:example-command`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/example-plugin/skills/example-command --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree f711bd1f447db67a063461382a245659a7fe754e64f01ae9e3eae15e45c8bcb2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
