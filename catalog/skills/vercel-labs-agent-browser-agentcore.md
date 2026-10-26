# agentcore

> Run agent-browser on AWS Bedrock AgentCore cloud browsers. Use when the user wants to use AgentCore, run browser automation on AWS, use a cloud browser with AWS credentials, or needs a managed browser session backed by AWS infrastructure. Triggers include "use agentcore", "run on AWS", "cloud browser with AWS", "bedrock browser", "agentcore session", or any task requiring AWS-hosted browser automation.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:agentcore` |
| **Pack** | MLOps / DevOps / Cloud (also: Browser & Web Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 116 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to use AgentCore, run browser automation on AWS, use a cloud browser with AWS credentials, or needs a managed browser session backed by AWS infrastructure.

## What it says up front

> Run agent-browser on cloud browser sessions hosted by AWS Bedrock AgentCore. All standard agent-browser commands work identically; the only difference is where the browser runs.

## How it is structured

The skill's own section headings, in order:

- Setup
- Core Workflow
- Environment Variables
- Persistent Profiles
- Live View
- Region Selection
- Credential Patterns
- Using with AGENT_BROWSER_PROVIDER
- Common Issues

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `agent-browser:*)`

## Related skills

- [vercel-labs/agent-browser:vercel-sandbox](vercel-labs-agent-browser-vercel-sandbox.md) - Run agent-browser + Chrome inside Vercel Sandbox microVMs for browser automation from any Vercel-deployed app.
- [vercel-labs/agent-browser:electron](vercel-labs-agent-browser-electron.md) - Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via
- [vercel-labs/agent-browser:slack](vercel-labs-agent-browser-slack.md) - Interact with Slack workspaces using browser automation. Use when the user needs to check unread channels, nav
- [vercel-labs/agent-browser:agent-browser](vercel-labs-agent-browser-agent-browser.md) - Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating 

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:agentcore`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/agentcore --commit 04ba5264dade678062c3cdcce0f4f293e748249f --expect-tree a0a45d30f61ac972b940ca35246d8c6fcc8355c6b05ee21d708373967fbb8afc --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
