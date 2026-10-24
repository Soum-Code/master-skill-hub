# create-cowork-plugin

> Guide users through creating a new plugin from scratch in a cowork session. Use when users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin. This skill requires Cowork mode with access to the outputs directory for delivering the final .plugin file.

| | |
|---|---|
| **ID** | `cowork-plugin-management:create-cowork-plugin` |
| **Pack** | Claude / Skills / Plugin Tooling |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `cowork-plugin-management` v0.2.2 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 268 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when users want to create a plugin, build a plugin, make a new plugin, develop a plugin, scaffold a plugin, start a plugin from scratch, or design a plugin.

## What it says up front

> Build a new plugin from scratch through guided conversation. Walk the user through discovery, planning, design, implementation, and packaging — delivering a ready-to-install `.plugin` file at the end.

## How it is structured

The skill's own section headings, in order:

- Overview
- Plugin Architecture
  - Directory Structure
  - plugin.json Manifest
  - Component Schemas
  - Customizable plugins with `~~` placeholders
  - ${CLAUDE_PLUGIN_ROOT} Variable
- Guided Workflow
  - Phase 1: Discovery
  - Phase 2: Component Planning
  - Phase 3: Design & Clarifying Questions
  - Phase 4: Implementation
  - Phase 5: Review & Package
- Best Practices
- Additional Resources

## What it bundles

- reference docs: `references/component-schemas.md`, `references/example-plugins.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create
- [anthropic-skills:skill-creator](anthropic-skills-skill-creator.md) - Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to c
- [example-skills:skill-creator](example-skills-skill-creator.md) - Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to c

## Invoke / install

- Invoke: `/cowork-plugin-management:create-cowork-plugin`  (Skill tool: `cowork-plugin-management:create-cowork-plugin`)
- Install: `bundled with Claude desktop (Cowork plugin 'cowork-plugin-management'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
