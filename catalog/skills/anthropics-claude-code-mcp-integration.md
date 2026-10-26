# MCP Integration

> This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types (SSE, stdio, HTTP, WebSocket). Provides comprehensive guidance for integrating Model Context Protocol servers into Claude Code plugins for external tool and service integration.

| | |
|---|---|
| **ID** | `anthropics/claude-code:MCP Integration` |
| **Pack** | Claude / Skills / Plugin Tooling (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-code](https://github.com/anthropics/claude-code) |
| **License** | not declared |
| **Size** | 555 lines in SKILL.md, 7 file(s) |

## When to use it

- This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", "use .mcp.json", "set up Model Context Protocol", "connect external service", mentions "${CLAUDE_PLUGIN_ROOT} with MCP", or discusses MCP server types.

## How it is structured

The skill's own section headings, in order:

- Overview
- MCP Server Configuration Methods
  - Method 1: Dedicated .mcp.json (Recommended)
  - Method 2: Inline in plugin.json
- MCP Server Types
  - stdio (Local Process)
  - SSE (Server-Sent Events)
  - HTTP (REST API)
  - WebSocket (Real-time)
- Environment Variable Expansion
- MCP Tool Naming
  - Using MCP Tools in Commands
- Lifecycle Management
- Authentication Patterns
  - OAuth (SSE/HTTP)
  - Token-Based (Headers)
  - Environment Variables (stdio)
- Integration Patterns
  - Pattern 1: Simple Tool Wrapper
  - Pattern 2: Autonomous Agent
  - Pattern 3: Multi-Server Plugin
- Security Best Practices
  - Use HTTPS/WSS
  - Token Management
  - Permission Scoping
- Error Handling
  - Connection Failures
  - Tool Call Errors
  - Configuration Errors
- Performance Considerations

## What it bundles

- reference docs: `references/authentication.md`, `references/server-types.md`, `references/tool-usage.md`
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:mcp-integration](anthropics-claude-plugins-official-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati
- [anthropics/claude-plugins-official:example-skill](anthropics-claude-plugins-official-example-skill.md) - This skill should be used when the user asks to "demonstrate skills", "show skill format", "create a skill tem
- [claude-code-setup:claude-automation-recommender](claude-code-setup-claude-automation-recommender.md) - Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use

## Invoke / install

- Invoke: `/anthropics/claude-code:MCP Integration`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-code --path plugins/plugin-dev/skills/mcp-integration --commit 2eff7a8d21c80be48904f62ebdea36d945d7b504 --expect-tree 2b76c1654b5f97827d3b63ea79e97d5df5683d575a6b48f30856bc992b81237c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
