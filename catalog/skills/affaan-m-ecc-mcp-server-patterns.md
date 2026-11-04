# mcp-server-patterns

> Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HTTP. Use Context7 or official MCP docs for latest API. Use when building or debugging an MCP server — tools, resources, prompts, validation, or transport choice.

| | |
|---|---|
| **ID** | `affaan-m/ECC:mcp-server-patterns` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 71 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building or debugging an MCP server — tools, resources, prompts, validation, or transport choice.

## What it says up front

> The Model Context Protocol (MCP) lets AI assistants call tools, read resources, and use prompts from your server. Use this skill when building or maintaining MCP servers. The SDK API evolves; check Context7 (query-docs for "MCP") or the official MCP documentation for current method names and signatu

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Core concepts
  - Connecting with stdio
  - Remote (Streamable HTTP)
- Examples
  - Install and server setup
- Best Practices
- Official SDKs and Docs

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [example-skills:mcp-builder](example-skills-mcp-builder.md) - Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with externa
- [openai/skills:openai-docs](openai-skills-openai-docs.md) - Use when the user asks how to build with OpenAI products or APIs, asks about Codex itself or choosing Codex su
- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati
- [microsoft/skills:copilot-sdk](microsoft-skills-copilot-sdk.md) - Build applications powered by GitHub Copilot using the Copilot SDK. Use when creating programmatic integration

## Invoke / install

- Invoke: `/affaan-m/ECC:mcp-server-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/mcp-server-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f8da8b4117bd40b4a6cb2aa956d5d2369979a905c73391422dc7b0e63f7781bb --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
