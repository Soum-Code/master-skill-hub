# Command Development

> This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use AskUserQuestion in command", or needs guidance on slash command structure, YAML frontmatter fields, dynamic arguments, bash execution in commands, user interaction patterns, or command development best practices for Claude Code.

| | |
|---|---|
| **ID** | `anthropics/claude-code:Command Development` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **License** | not declared |
| **Size** | 835 lines in SKILL.md, 11 file(s) |

## When to use it

- This skill should be used when the user asks to "create a slash command", "add a command", "write a custom command", "define command arguments", "use command frontmatter", "organize commands", "create command with file references", "interactive command", "use.

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

- [anthropics/claude-plugins-official:command-development](anthropics-claude-plugins-official-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 

## Invoke / install

- Invoke: `/anthropics/claude-code:Command Development`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-code --path plugins/plugin-dev/skills/command-development --commit 318b7e6ac4e726e88a4ad326214866a93c373b1b --expect-tree 6f128f24f0a8064edb073e53b8132af704e178987e86527202e5dbff1f14b06f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
