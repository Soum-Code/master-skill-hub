# Writing Hookify Rules

> This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.

| | |
|---|---|
| **ID** | `anthropics/claude-code:Writing Hookify Rules` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **License** | not declared |
| **Size** | 375 lines in SKILL.md, 1 file(s) |

## When to use it

- This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule", or needs guidance on hookify rule syntax and patterns.

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

- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/anthropics/claude-code:Writing Hookify Rules`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-code --path plugins/hookify/skills/writing-rules --commit 318b7e6ac4e726e88a4ad326214866a93c373b1b --expect-tree 6f9cfd729fa47600e6c572a1df0342b9b8990942eade010a136dbbafe5432a5b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
