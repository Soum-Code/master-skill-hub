# example-skill

> This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns. Provides a reference template for creating Claude Code plugin skills.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:example-skill` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 85 lines in SKILL.md, 1 file(s) |

## When to use it

- This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill template", or discusses skill development patterns.

## What it says up front

> This skill demonstrates the structure and format for Claude Code plugin skills.

## How it is structured

The skill's own section headings, in order:

- Overview
- When This Skill Applies
- Skill Structure
  - Required Files
  - Optional Supporting Files
- Frontmatter Options
- Writing Effective Descriptions
- Skill Content Guidelines
- Best Practices

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-code:Command Development](anthropics-claude-code-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com
- [anthropics/claude-plugins-official:command-development](anthropics-claude-plugins-official-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:example-skill`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/example-plugin/skills/example-skill --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 03a037c03124aa6750121ff056ecb9b50f821b5008a9905fef1a61e9614517d3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
