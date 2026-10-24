# Skill Development

> This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.

| | |
|---|---|
| **ID** | `anthropics/claude-code:Skill Development` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **License** | not declared |
| **Size** | 638 lines in SKILL.md, 2 file(s) |

## When to use it

- This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best prac.

## How it is structured

The skill's own section headings, in order:

- About Skills
  - What Skills Provide
  - Anatomy of a Skill
  - Progressive Disclosure Design Principle
- Skill Creation Process
  - Step 1: Understanding the Skill with Concrete Examples
  - Step 2: Planning the Reusable Skill Contents
  - Step 3: Create Skill Structure
  - Step 4: Edit the Skill
  - Step 5: Validate and Test
  - Step 6: Iterate
- Plugin-Specific Considerations
  - Skill Location in Plugins
  - Auto-Discovery
  - No Packaging Needed
  - Testing in Plugins
- Examples from Plugin-Dev
- Progressive Disclosure in Practice
  - What Goes in SKILL.md
  - What Goes in references/
  - What Goes in examples/
  - What Goes in scripts/
- Writing Style Requirements
  - Imperative/Infinitive Form
  - Third-Person in Description
  - Objective, Instructional Language
- Validation Checklist
- Common Mistakes to Avoid
  - Mistake 1: Weak Trigger Description
  - Mistake 2: Too Much in SKILL.md

## What it bundles

- reference docs: `references/skill-creator-original.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:skill-development](anthropics-claude-plugins-official-skill-development.md) - This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-code:Command Development](anthropics-claude-code-command-development.md) - This skill should be used when the user asks to "create a slash command", "add a command", "write a custom com

## Invoke / install

- Invoke: `/anthropics/claude-code:Skill Development`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-code --path plugins/plugin-dev/skills/skill-development --commit 318b7e6ac4e726e88a4ad326214866a93c373b1b --expect-tree 1391c4f292cad2114cd28de751ed755e46fec9aa2e0bab4329c78d6f1696c7b9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
