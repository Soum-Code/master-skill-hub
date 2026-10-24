# writing-hookify-rules

> This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:writing-hookify-rules` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 375 lines in SKILL.md, 1 file(s) |

## When to use it

- This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.

## What it says up front

> Hookify rules are markdown files with YAML frontmatter that define patterns to watch for and messages to show when those patterns match. Rules are stored in `.claude/hookify.{rule-name}.local.md` files.

## How it is structured

The skill's own section headings, in order:

- Overview
- Rule File Format
  - Basic Structure
  - Frontmatter Fields
  - Advanced Format (Multiple Conditions)
- Message Body
- Event Type Guide
  - bash Events
  - file Events
  - stop Events
  - prompt Events
- Pattern Writing Tips
  - Regex Basics
  - Testing Patterns
  - Common Pitfalls
- File Organization
- Workflow
  - Creating a Rule
  - Refining a Rule
  - Disabling a Rule
- Examples
- Quick Reference

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:writing-hookify-rules`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/hookify/skills/writing-rules --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree cf70e695dcde31d280d63572ac2d7d3221ce1dfb0ca2112abe56b58d2f097ae2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
