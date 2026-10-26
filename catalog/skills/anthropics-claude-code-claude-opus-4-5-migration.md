# claude-opus-4-5-migration

> Migrate prompts and code from Claude Sonnet 4.0, Sonnet 4.5, or Opus 4.1 to Opus 4.5. Use when the user wants to update their codebase, prompts, or API calls to use Opus 4.5. Handles model string updates and prompt adjustments for known Opus 4.5 behavioral differences. Does NOT migrate Haiku 4.5.

| | |
|---|---|
| **ID** | `anthropics/claude-code:claude-opus-4-5-migration` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **License** | not declared |
| **Size** | 106 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when the user wants to update their codebase, prompts, or API calls to use Opus 4.5.

## How it is structured

The skill's own section headings, in order:

- Migration Workflow
- Model String Updates
  - Unsupported Beta Headers
  - Target Model Strings (Opus 4.5)
  - Source Model Strings to Replace
- Prompt Adjustments
  - 1. Tool Overtriggering
  - 2. Over-Engineering Prevention
  - 3. Code Exploration
  - 4. Frontend Design
  - 5. Thinking Sensitivity
- Reference

## What it bundles

- reference docs: `references/effort.md`, `references/prompt-snippets.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create
- [claude-api](claude-api.md) - Reference for the Claude API and Anthropic SDKs - model ids, pricing, streaming, tool use, MCP, agents, prompt
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [loop](loop.md) - Run a prompt or slash command on a recurring interval, or let the model self-pace. Use when the user wants to 

## Invoke / install

- Invoke: `/anthropics/claude-code:claude-opus-4-5-migration`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-code --path plugins/claude-opus-4-5-migration/skills/claude-opus-4-5-migration --commit 2eff7a8d21c80be48904f62ebdea36d945d7b504 --expect-tree be905763352e50bbfcb6991c174b328ce47609e95a70098e2f9e08951e41109d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
