# claude-automation-recommender

> Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

| | |
|---|---|
| **ID** | `claude-code-setup:claude-automation-recommender` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Browser & Web Automation) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `claude-code-setup` v1.0.0 - [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 290 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when user asks for automation recommendations, wants to optimize their Claude Code setup, mentions improving Claude Code workflows, asks how to first set up Claude Code for a project, or wants to know what Claude Code features they should use.

## What it says up front

> Analyze codebase patterns to recommend tailored Claude Code automations across all extensibility options.

## How it is structured

The skill's own section headings, in order:

- Output Guidelines
- Automation Types Overview
- Workflow
  - Phase 1: Codebase Analysis
  - Phase 2: Generate Recommendations
  - Phase 3: Output Recommendations Report
- Decision Framework
  - When to Recommend MCP Servers
  - When to Recommend Skills
  - When to Recommend Hooks
  - When to Recommend Subagents
  - When to Recommend Plugins
- Configuration Tips
  - MCP Server Setup
  - Headless Mode (for CI/Automation)
  - Permissions for Hooks

## What it bundles

- reference docs: `references/hooks-patterns.md`, `references/mcp-servers.md`, `references/plugins-reference.md`, `references/skills-reference.md`, `references/subagent-templates.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [cowork-plugin-management:cowork-plugin-customizer](cowork-plugin-management-cowork-plugin-customizer.md) - Customize a Claude Code plugin for a specific organization's tools and workflows. Use when: customize plugin, 
- [anthropic-skills:setup-claude](anthropic-skills-setup-claude.md) - Guided setup — install role-matched plugins, connect your tools, try a skill.
- [bm:remember-access](bm-remember-access.md) - Capture or review how this project connects to external systems (GitHub, AWS, npm, SSH, etc.) so future sessio
- [playwright-cli](playwright-cli.md) - Official Microsoft browser automation CLI (@playwright/cli). Use when the user asks to automate browser intera

## Invoke / install

- Invoke: `/claude-code-setup:claude-automation-recommender`  (Skill tool: `claude-code-setup:claude-automation-recommender`)
- Install: `claude plugin marketplace add anthropics/claude-plugins-official && claude plugin install claude-code-setup@claude-plugins-official`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
