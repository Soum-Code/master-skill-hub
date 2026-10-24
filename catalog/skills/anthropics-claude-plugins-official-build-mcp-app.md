# build-mcp-app

> This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inline in the conversation, or mentions "apps SDK" in the context of MCP. Use AFTER the build-mcp-server skill has settled the deployment model, or when the user already knows they want UI widgets.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:build-mcp-app` |
| **Pack** | AI / ML Engineering (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 393 lines in SKILL.md, 7 file(s) |

## When to use it

- This skill should be used when the user wants to build an "MCP app", add "interactive UI" or "widgets" to an MCP server, "render components in chat", build "MCP UI resources", make a tool that shows a "form", "picker", "dashboard" or "confirmation dialog" inli.

## What it says up front

> An MCP app is a standard MCP server that **also serves UI resources** — interactive components rendered inline in the chat surface. Build once, runs in Claude *and* ChatGPT and any other host that implements the apps surface.

## How it is structured

The skill's own section headings, in order:

- Claude host specifics
- When a widget beats plain text
- Widgets vs Elicitation — route correctly
- Architecture: two deployment shapes
  - Remote MCP app (most common)
  - MCPB-packaged MCP app (local + UI)
- How widgets attach to tools
- Widget runtime — the `App` class
- Scaffold: minimal picker widget
- Design notes that save you a rewrite
- Testing
- Reference files

## What it bundles

- reference docs: `references/abuse-protection.md`, `references/apps-sdk-messages.md`, `references/directory-checklist.md`, `references/iframe-sandbox.md`, `references/payload-budgeting.md`, `references/widget-templates.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati
- [anthropics/claude-code:MCP Integration](anthropics-claude-code-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:mcp-integration](anthropics-claude-plugins-official-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:build-mcpb](anthropics-claude-plugins-official-build-mcpb.md) - This skill should be used when the user wants to "package an MCP server", "bundle an MCP", "make an MCPB", "sh

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:build-mcp-app`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/mcp-server-dev/skills/build-mcp-app --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree afa516b5b52e2ad64fcf58a2e673efc48881c47b368a8fce379f07252c2cd466 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
