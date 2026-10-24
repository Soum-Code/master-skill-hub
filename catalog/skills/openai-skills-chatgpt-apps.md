# chatgpt-apps

> Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code.

| | |
|---|---|
| **ID** | `openai/skills:chatgpt-apps` |
| **Pack** | Software Development (also: AI / ML Engineering, Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 321 lines in SKILL.md, 11 file(s) |

## When to use it

- Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold.

## How it is structured

The skill's own section headings, in order:

- Overview
- Mandatory Docs-First Workflow
- Prompt Guidance
- Classify The App Before Choosing Code
- Default Starting-Point Order
- Build Workflow
  - 0. Classify The App Archetype
  - 1. Plan Tools Before Code
  - 2. Choose an App Architecture
  - 2a. Start From An Upstream Example When One Fits
  - 2b. Use the Starter Script When a Low-Dependency Fallback Helps
  - 3. Scaffold the MCP Server
  - 4. Scaffold the Widget UI
  - 5. Add Resource Metadata and Security
  - 5a. Enforce A Minimum Working Repo Contract
  - 6. Validate the Local Loop
  - 7. Connect and Test in ChatGPT (Developer Mode)
  - 8. Plan Production Hosting and Deployment
  - 9. Prepare Submission and Publish (Public Apps Only)
- Interactive State Guidance
- Output Expectations
- References

## What it bundles

- scripts: `scripts/scaffold_node_ext_apps.mjs`
- reference docs: `references/app-archetypes.md`, `references/apps-sdk-docs-workflow.md`, `references/interactive-state-sync-patterns.md`, `references/repo-contract-and-validation.md`, `references/search-fetch-standard.md`, `references/upstream-example-workflow.md`, `references/window-openai-patterns.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-plugins-official:build-mcp-app](anthropics-claude-plugins-official-build-mcp-app.md) - This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an M
- [openai/skills:openai-docs](openai-skills-openai-docs.md) - Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex su
- [openai/skills:cli-creator](openai-skills-cli-creator.md) - Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an
- [anthropics/knowledge-work-plugins:start](anthropics-knowledge-work-plugins-start.md) - Set up your bio-research environment and explore available tools. Use when first getting oriented with the plu

## Invoke / install

- Invoke: `/openai/skills:chatgpt-apps`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/chatgpt-apps --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree c945d113c5b823b365ad847031f95a2cac1446a4b19ecd6384a3b87a2e79c568 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
