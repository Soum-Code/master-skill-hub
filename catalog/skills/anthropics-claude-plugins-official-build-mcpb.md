# build-mcpb

> This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs an MCP server that interacts with the local filesystem, desktop apps, or OS and must be installable without the user having Node/Python set up.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:build-mcpb` |
| **Pack** | Claude / Skills / Plugin Tooling (also: AI / ML Engineering, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 200 lines in SKILL.md, 3 file(s) |

## When to use it

- This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "ship a local MCP server", "distribute a local MCP", discusses ".mcpb files", mentions bundling a Node or Python runtime with their MCP server, or needs.

## What it says up front

> MCPB is a local MCP server **packaged with its runtime**. The user installs one file; it runs without needing Node, Python, or any toolchain on their machine. It's the sanctioned way to distribute local MCP servers.

## How it is structured

The skill's own section headings, in order:

- What an MCPB bundle contains
- Manifest
- Server code: same as local stdio
- Build pipeline
  - Node
  - Python
- MCPB has no sandbox — security is on you
- MCPB + UI widgets
- Testing
- Reference files

## What it bundles

- reference docs: `references/local-security.md`, `references/manifest-schema.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati
- [anthropics/claude-plugins-official:build-mcp-app](anthropics-claude-plugins-official-build-mcp-app.md) - This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an M
- [anthropics/claude-code:MCP Integration](anthropics-claude-code-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:mcp-integration](anthropics-claude-plugins-official-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:build-mcpb`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/mcp-server-dev/skills/build-mcpb --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 2e1eda1310f5785464a2acad33cdb575b9be5c23484c35e77b4a98c5c183d034 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
