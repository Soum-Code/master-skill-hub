# electron

> Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via Chrome DevTools Protocol. Use when the user needs to interact with an Electron app, automate a desktop app, connect to a running app, control a native app, or test an Electron application. Triggers include "automate Slack app", "control VS Code", "interact with Discord app", "test this Electron app", "connect to desktop app", or any task requiring automation of a native Electron application.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:electron` |
| **Pack** | Browser & Web Automation (also: Communication & Collaboration) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 237 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user needs to interact with an Electron app, automate a desktop app, connect to a running app, control a native app, or test an Electron application.

## What it says up front

> Automate any Electron desktop app using agent-browser. Electron apps are built on Chromium and expose a Chrome DevTools Protocol (CDP) port that agent-browser can connect to, enabling the same snapshot-interact workflow used for web pages.

## How it is structured

The skill's own section headings, in order:

- Core Workflow
- Launching Electron Apps with CDP
  - macOS
  - Linux
  - Windows
- Connecting
- Tab Management
- Webview Support
- Common Patterns
  - Inspect and Navigate an App
  - Take Screenshots of Desktop Apps
  - Extract Data from a Desktop App
  - Fill Forms in Desktop Apps
  - Run Multiple Apps Simultaneously
- Color Scheme
- Troubleshooting
  - "Connection refused" or "Cannot connect"
  - App launches but connect fails
  - Elements not appearing in snapshot
  - Cannot type in input fields
- Supported Apps

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `agent-browser:*)`

## Related skills

- [vercel-labs/agent-browser:agent-browser](vercel-labs-agent-browser-agent-browser.md) - Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating 
- [vercel-labs/agent-browser:vercel-sandbox](vercel-labs-agent-browser-vercel-sandbox.md) - Run agent-browser + Chrome inside Vercel Sandbox microVMs for browser automation from any Vercel-deployed app.
- [vercel-labs/agent-browser:slack](vercel-labs-agent-browser-slack.md) - Interact with Slack workspaces using browser automation. Use when the user needs to check unread channels, nav
- [vercel-labs/agent-browser:agentcore](vercel-labs-agent-browser-agentcore.md) - Run agent-browser on AWS Bedrock AgentCore cloud browsers. Use when the user wants to use AgentCore, run brows

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:electron`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/electron --commit 372ac5ce20fab885dbf45ee0c9d510ec8c3b6fdb --expect-tree 29cde98bbd2eab466c23e6c7c9b357904658487e5ba70f464c9a8fd0943126ed --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
