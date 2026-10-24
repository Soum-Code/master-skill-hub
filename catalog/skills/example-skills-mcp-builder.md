# mcp-builder

> Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

| | |
|---|---|
| **ID** | `example-skills:mcp-builder` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `example-skills` v3b3fad96af16 - [anthropics/skills](https://github.com/anthropics/skills) |
| **License** | Complete terms in LICENSE.txt |
| **Size** | 237 lines in SKILL.md, 10 file(s) |

## When to use it

- Use when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK).

## What it says up front

> Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality of an MCP server is measured by how well it enables LLMs to accomplish real-world tasks.

## How it is structured

The skill's own section headings, in order:

- Overview
- 🚀 High-Level Workflow
  - Phase 1: Deep Research and Planning
  - Phase 2: Implementation
  - Phase 3: Review and Test
  - Phase 4: Create Evaluations
- 📚 Documentation Library
  - Core MCP Documentation (Load First)
  - SDK Documentation (Load During Phase 1/2)
  - Language-Specific Implementation Guides (Load During Phase 2)
  - Evaluation Guide (Load During Phase 4)

## What it bundles

- scripts: `scripts/connections.py`, `scripts/evaluation.py`
- reference docs: `reference/evaluation.md`, `reference/mcp_best_practices.md`, `reference/node_mcp_server.md`, `reference/python_mcp_server.md`
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [microsoft/skills:copilot-sdk](microsoft-skills-copilot-sdk.md) - Build applications powered by GitHub Copilot using the Copilot SDK. Use when creating programmatic integration
- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati
- [anthropics/claude-code:MCP Integration](anthropics-claude-code-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:mcp-integration](anthropics-claude-plugins-official-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 

## Invoke / install

- Invoke: `/example-skills:mcp-builder`  (Skill tool: `example-skills:mcp-builder`)
- Install: `claude plugin marketplace add anthropics/skills && claude plugin install example-skills@anthropic-agent-skills`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
