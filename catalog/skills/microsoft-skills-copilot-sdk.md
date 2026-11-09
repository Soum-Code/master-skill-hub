# copilot-sdk

> Build applications powered by GitHub Copilot using the Copilot SDK. Use when creating programmatic integrations with Copilot across Node.js/TypeScript, Python, Go, or .NET. Covers session management, custom tools, streaming, hooks, MCP servers, BYOK providers, session persistence, custom agents, skills, and deployment patterns. Requires GitHub Copilot CLI installed and a GitHub Copilot subscription (unless using BYOK).

| | |
|---|---|
| **ID** | `microsoft/skills:copilot-sdk` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Productivity & Automation, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 905 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when creating programmatic integrations with Copilot across Node.js/TypeScript, Python, Go, or .NET.

## What it says up front

> Build applications that programmatically interact with GitHub Copilot. The SDK wraps the Copilot CLI via JSON-RPC, providing session management, custom tools, hooks, MCP server integration, and streaming across Node.js, Python, Go, and .NET.

## How it is structured

The skill's own section headings, in order:

- Prerequisites
- Installation
- Architecture
- Core Pattern: Client → Session → Message
  - Node.js / TypeScript
  - Python
  - Go
  - .NET
- Streaming Responses
  - Node.js
  - Python
  - Event Subscription
- Custom Tools
  - Node.js
  - Python
  - Go
  - .NET
  - Tool Requirements
- Hooks
  - Pre-Tool Use Hook
  - Post-Tool Use Hook
  - User Prompt Submitted Hook
  - Session Lifecycle Hooks
  - Error Handling Hook
  - Python Hook Example
  - Go Hook Example
- MCP Server Integration
  - Local Stdio Server
  - Remote HTTP Server
  - MCP Config Fields

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:search-first](affaan-m-ecc-search-first.md) - Research-before-coding workflow: search npm/PyPI, MCP servers, skills, and GitHub for existing tools before wr
- [example-skills:mcp-builder](example-skills-mcp-builder.md) - Guide for creating high-quality MCP (Model Context Protocol) servers that enable LLMs to interact with externa
- [affaan-m/ECC:mcp-server-patterns](affaan-m-ecc-mcp-server-patterns.md) - Build MCP servers with Node/TypeScript SDK — tools, resources, prompts, Zod validation, stdio vs Streamable HT
- [google-gemini/gemini-skills:gemini-live-api-dev](google-gemini-gemini-skills-gemini-live-api-dev.md) - Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migr

## Invoke / install

- Invoke: `/microsoft/skills:copilot-sdk`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/copilot-sdk --commit 0696600436a9669184ce47e8d8b2ceac62e4bfac --expect-tree bc7427d5af874029378a9574bd4d8885d798614e03f9ef9c2b9cc8835ec15af7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
