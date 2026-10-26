# Agent Development

> This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, system prompts, triggering conditions, or agent development best practices for Claude Code plugins.

| | |
|---|---|
| **ID** | `anthropics/claude-code:Agent Development` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **License** | not declared |
| **Size** | 416 lines in SKILL.md, 7 file(s) |

## When to use it

- This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent frontmatter", "when to use description", "agent examples", "agent tools", "agent colors", "autonomous agent", or needs guidance on agent structure, sy.

## How it is structured

The skill's own section headings, in order:

- Overview
- Agent File Structure
  - Complete Format
- Frontmatter Fields
  - name (required)
  - description (required)
  - model (required)
  - color (required)
  - tools (optional)
- System Prompt Design
  - Structure
  - Best Practices
- Creating Agents
  - Method 1: AI-Assisted Generation
  - Method 2: Manual Creation
- Validation Rules
  - Identifier Validation
  - Description Validation
  - System Prompt Validation
- Agent Organization
  - Plugin Agents Directory
  - Namespacing
- Testing Agents
  - Test Triggering
  - Test System Prompt
- Quick Reference
  - Minimal Agent
  - Frontmatter Fields Summary
  - Best Practices
- Additional Resources

## What it bundles

- scripts: `scripts/validate-agent.sh`
- reference docs: `references/agent-creation-system-prompt.md`, `references/system-prompt-design.md`, `references/triggering-examples.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-code:Skill Development](anthropics-claude-code-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-code:Command Development](anthropics-claude-code-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com

## Invoke / install

- Invoke: `/anthropics/claude-code:Agent Development`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-code --path plugins/plugin-dev/skills/agent-development --commit 2eff7a8d21c80be48904f62ebdea36d945d7b504 --expect-tree d7ff27a1505be385a44899b9dbf2c08e771e9e2049bd7a2831ecd271e3a7624b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
