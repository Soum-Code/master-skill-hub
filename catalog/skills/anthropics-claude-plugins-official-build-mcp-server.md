# build-mcp-server

> This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol. It is the entry point for MCP server development — it interrogates the user about their use case, determines the right deployment model (remote HTTP, MCPB, local stdio), picks a tool-design pattern, and hands off to specialized skills.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:build-mcp-server` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 222 lines in SKILL.md, 9 file(s) |

## When to use it

- This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integration", "wrap an API for Claude", "expose tools to Claude", "make an MCP app", or discusses building something with the Model Context Protocol.

## What it says up front

> You are guiding a developer through designing and building an MCP server that works seamlessly with Claude. MCP servers come in many forms — picking the wrong shape early causes painful rewrites later. Your first job is **discovery, not code**.

## How it is structured

The skill's own section headings, in order:

- Phase 1 — Interrogate the use case
  - 1. What does it connect to?
  - 2. Who will use it?
  - 3. How many distinct actions does it expose?
  - 4. Does a tool need mid-call user input or rich display?
  - 5. What auth does the upstream service use?
- Phase 2 — Recommend a deployment model
  - ⭐ Remote streamable-HTTP MCP server (default recommendation)
  - Elicitation (structured input, no UI build)
  - MCP app (remote HTTP + interactive UI)
  - MCPB (bundled local server)
  - Local stdio (npx / uvx) — *not recommended for distribution*
- Phase 3 — Pick a tool-design pattern
  - Pattern A: One tool per action (small surface)
  - Pattern B: Search + execute (large surface)
- Phase 4 — Pick a framework
- Phase 5 — Scaffold and hand off
- Beyond tools — the other primitives
- Phase 6 — Test in Claude and publish
- Quick reference: decision matrix
- Reference files

## What it bundles

- reference docs: `references/auth.md`, `references/deploy-cloudflare-workers.md`, `references/elicitation.md`, `references/remote-http-scaffold.md`, `references/resources-and-prompts.md`, `references/server-capabilities.md`, `references/tool-design.md`, `references/versions.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-code:MCP Integration](anthropics-claude-code-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:mcp-integration](anthropics-claude-plugins-official-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:build-mcp-app](anthropics-claude-plugins-official-build-mcp-app.md) - This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an M
- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:build-mcp-server`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/mcp-server-dev/skills/build-mcp-server --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree c80a065bb298d455e47bfed903b70bc8c5f6986ac59ff8013b31f2fed0800ea9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
