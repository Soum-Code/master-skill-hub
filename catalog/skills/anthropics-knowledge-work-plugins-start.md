# start

> Set up your bio-research environment and explore available tools. Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:start` |
| **Pack** | Research & Learning |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 80 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when first getting oriented with the plugin, checking which literature, drug-discovery, or visualization MCP servers are connected, or surveying available analysis skills before starting a new project.

## What it says up front

> You are helping a biological researcher get oriented with the bio-research plugin. Walk through the following steps in order.

## How it is structured

The skill's own section headings, in order:

- Step 1: Welcome
- Step 2: Check Available MCP Servers
- Step 3: Survey Available Skills
- Step 4: Optional Setup — Binary MCP Servers
- Step 5: Ask How to Help

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use
- [anthropic-skills:setup-claude](anthropic-skills-setup-claude.md) - Guided setup — install role-matched plugins, connect your tools, try a skill.
- [anthropic-skills:setup-cowork](anthropic-skills-setup-cowork.md) - Guided setup — install role-matched plugins, connect your tools, try a skill.
- [huggingface/skills:hf-mcp](huggingface-skills-hf-mcp.md) - Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch do

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:start`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path bio-research/skills/start --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 5d6d3c8a75ffcf653df39c8b17bc802a6cd2321939b08b19fbfe55d5356c1582 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
