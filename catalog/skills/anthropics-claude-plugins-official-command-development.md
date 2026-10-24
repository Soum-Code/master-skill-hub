# command-development

> This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:command-development` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 885 lines in SKILL.md, 11 file(s) |

## When to use it

- This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use.

## What it says up front

> Slash commands are frequently-used prompts defined as Markdown files that Claude executes during interactive sessions. Understanding command structure, frontmatter options, and dynamic features enables creating powerful, reusable workflows.

## How it is structured

The skill's own section headings, in order:

- Overview
- Command Basics
  - What is a Slash Command?
  - Critical: Commands are Instructions FOR Claude
  - Command Locations
- File Format
  - Basic Structure
  - With YAML Frontmatter
- YAML Frontmatter Fields
  - description
  - allowed-tools
  - model
  - argument-hint
  - disable-model-invocation
- Dynamic Arguments
  - Using $ARGUMENTS
  - Using Positional Arguments
  - Combining Arguments
- File References
  - Using @ Syntax
  - Multiple File References
  - Static File References
- Bash Execution in Commands
- Command Organization
  - Flat Structure
  - Namespaced Structure
- Best Practices
  - Command Design
  - Argument Handling
  - File References

## What it bundles

- reference docs: `references/advanced-workflows.md`, `references/documentation-patterns.md`, `references/frontmatter-reference.md`, `references/interactive-commands.md`, `references/marketplace-considerations.md`, `references/plugin-features-reference.md`, `references/testing-strategies.md`
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-code:Command Development](anthropics-claude-code-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:command-development`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/plugin-dev/skills/command-development --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 994379141c61106d9bd96765d225416d0350d939c92a3a3d197bc29200fb42b5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
