# linear

> Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets in Linear.

| | |
|---|---|
| **ID** | `openai/skills:linear` |
| **Pack** | Communication & Collaboration (also: Claude / Skills / Plugin Tooling, Spec-driven Dev Workflow, MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 88 lines in SKILL.md, 5 file(s) |

## When to use it

- Use when the user wants to read, create or updates tickets in Linear.

## How it is structured

The skill's own section headings, in order:

- Overview
- Prerequisites
- Required Workflow
  - Step 0: Set up Linear MCP (if not already configured)
  - Step 1
  - Step 2
  - Step 3
  - Step 4
- Available Tools
- Practical Workflows
- Tips for Maximum Productivity
- Troubleshooting

## What it bundles

- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma-create-design-system-rules](openai-skills-figma-create-design-system-rules.md) - Generates custom design system rules for the user's codebase. Use when user says "create design system rules",
- [anthropic-skills:schedule](anthropic-skills-schedule.md) - Create or update a scheduled task that runs automatically. Use when the user says things like "every day", "ea
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [openai/skills:cli-creator](openai-skills-cli-creator.md) - Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an

## Invoke / install

- Invoke: `/openai/skills:linear`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/linear --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 0642dd8c6ce9dd89dcb607a373ad6761cc8d3271ea1f42a9f2d263c218a4f0c8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
