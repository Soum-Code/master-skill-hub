# hookify-rules

> Create and configure hookify rules — markdown files with YAML frontmatter that match bash, file, prompt, or stop events by regex or conditions and show warn/block messages to the agent. Use when creating a hookify rule, writing hook rule syntax, configuring hookify, or adding pattern guardrails such as blocking dangerous commands, .env edits, or debug code.

| | |
|---|---|
| **ID** | `affaan-m/ECC:hookify-rules` |
| **Pack** | Documents, Writing & Content (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 150 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when creating a hookify rule, writing hook rule syntax, configuring hookify, or adding pattern guardrails such as blocking dangerous commands, .env edits, or debug code.

## What it says up front

> ECC evaluates project-local Hookify rules with its built-in Node runtime. No separate Hookify plugin or Python installation is required when ECC hooks are enabled.

## How it is structured

The skill's own section headings, in order:

- Overview
- Rule File Format
  - Basic Structure
  - Frontmatter Fields
  - Advanced Format (Multiple Conditions)
- Event Type Guide
  - bash Events
  - file Events
  - stop Events
  - prompt Events
- Pattern Writing Tips
  - Regex Basics
  - Common Pitfalls
  - Testing
- Runtime Behavior
- File Organization
- Commands
- Quick Reference

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-code:Writing Hookify Rules](anthropics-claude-code-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-plugins-official:writing-hookify-rules](anthropics-claude-plugins-official-writing-hookify-rules.md) - This skill should be used when the user asks to "create a hookify rule", "write a hook rule", "configure hooki
- [anthropics/claude-code:Command Development](anthropics-claude-code-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com
- [anthropics/claude-plugins-official:command-development](anthropics-claude-plugins-official-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com

## Invoke / install

- Invoke: `/affaan-m/ECC:hookify-rules`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/hookify-rules --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f05986a189557bfa15ea46ca43e82e3ed9483f7f5455077aa79a223b19b08973 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
