# slack

> Interact with Slack workspaces using browser automation. Use when the user needs to check unread channels, navigate Slack, send messages, extract data, find information, search conversations, or automate any Slack task. Triggers include "check my Slack", "what channels have unreads", "send a message to", "search Slack for", "extract from Slack", "find who said", or any task requiring programmatic Slack interaction.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:slack` |
| **Pack** | Communication & Collaboration (also: Browser & Web Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 289 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when the user needs to check unread channels, navigate Slack, send messages, extract data, find information, search conversations, or automate any Slack task.

## What it says up front

> Interact with Slack workspaces to check messages, extract data, and automate common tasks.

## How it is structured

The skill's own section headings, in order:

- Quick Start
- Core Workflow
- Common Tasks
  - Checking Unread Messages
  - Navigating to a Channel
  - Finding Messages/Threads
  - Extracting Channel Information
  - Checking Channel Details
  - Taking Notes/Capturing State
- Sidebar Structure
- Tabs in Slack
- Extracting Data from Slack
  - Get Text Content
  - Parse Accessibility Tree
  - Count Unreads
- Best Practices
- Limitations
- Debugging
  - Check console for errors
  - Get current page state
- Example: Full Unread Check
- References

## What it bundles

- reference docs: `references/slack-tasks.md`
- 1 other file(s)

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `agent-browser:*)`

## Related skills

- [vercel-labs/agent-browser:agent-browser](vercel-labs-agent-browser-agent-browser.md) - Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating 
- [vercel-labs/agent-browser:electron](vercel-labs-agent-browser-electron.md) - Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via
- [vercel-labs/agent-browser:agentcore](vercel-labs-agent-browser-agentcore.md) - Run agent-browser on AWS Bedrock AgentCore cloud browsers. Use when the user wants to use AgentCore, run brows
- [agent-browser](agent-browser.md) - Fast browser automation CLI for AI agents (vercel-labs/agent-browser). Use when the user asks to interact with

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:slack`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/slack --commit 372ac5ce20fab885dbf45ee0c9d510ec8c3b6fdb --expect-tree c0326012821de932a827a916121d9045c83e2b97df5fff911e70ecb21ec9b3e0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
