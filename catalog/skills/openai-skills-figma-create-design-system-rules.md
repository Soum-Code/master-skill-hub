# figma-create-design-system-rules

> Generates custom design system rules for the user's codebase. Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows. Requires Figma MCP server connection.

| | |
|---|---|
| **ID** | `openai/skills:figma-create-design-system-rules` |
| **Pack** | Software Development (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 538 lines in SKILL.md, 8 file(s) |

## When to use it

- Use when user says "create design system rules", "generate rules for my project", "set up design rules", "customize design system guidelines", or wants to establish project-specific conventions for Figma-to-code workflows.

## How it is structured

The skill's own section headings, in order:

- Overview
  - Supported Rule Files
- What Are Design System Rules?
- Prerequisites
- When to Use This Skill
- Required Workflow
  - Step 1: Run the Create Design System Rules Tool
  - Step 2: Analyze the Codebase
  - Step 3: Generate Project-Specific Rules
  - Step 4: Save Rules to the Appropriate Rule File
  - Step 5: Validate and Iterate
- Rule Categories and Examples
  - Essential Rules (Always Include)
  - Recommended Rules (Highly Valuable)
  - Optional Rules (Project-Specific)
- Examples
  - Example 1: React + Tailwind Project
  - Example 2: Vue + Custom CSS Project
  - Example 3: Design System Team
- Best Practices
  - Start Simple, Iterate
  - Be Specific
  - Make Rules Actionable
  - Use IMPORTANT for Critical Rules
  - Document the Why
- Common Issues and Solutions
  - Issue: The agent isn't following the rules
  - Issue: Rules conflict with each other
  - Issue: Too many rules increase latency
  - Issue: Rules become outdated as project evolves

## What it bundles

- scripts: `scripts/check_agents_md.sh`
- reference docs: `references/rule-template.md`
- 5 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:figma-code-connect-components](openai-skills-figma-code-connect-components.md) - Connects Figma design components to code components using Code Connect mapping tools. Use when user says "code
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create
- [openai/skills:linear](openai-skills-linear.md) - Manage issues, projects & team workflows in Linear. Use when the user wants to read, create or updates tickets

## Invoke / install

- Invoke: `/openai/skills:figma-create-design-system-rules`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/figma-create-design-system-rules --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 172256e3c0a8e0858d8e880c13bc3e94d82c019aef418110d03bb880a46d5c8c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
