# vercel-sandbox

> Run agent-browser + Chrome inside Vercel Sandbox microVMs for browser automation from any Vercel-deployed app. Use when the user needs browser automation in a Vercel app (Next.js, SvelteKit, Nuxt, Remix, Astro, etc.), wants to run headless Chrome without binary size limits, needs persistent browser sessions across commands, or wants ephemeral isolated browser environments. Triggers include "Vercel Sandbox browser", "microVM Chrome", "agent-browser in sandbox", "browser automation on Vercel", or any task requiring Chrome in a Vercel Sandbox.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:vercel-sandbox` |
| **Pack** | Browser & Web Automation (also: MLOps / DevOps / Cloud, Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 220 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user needs browser automation in a Vercel app (Next.js, SvelteKit, Nuxt, Remix, Astro, etc.), wants to run headless Chrome without binary size limits, needs persistent browser sessions across commands, or wants ephemeral isolated browser environme.

## What it says up front

> Run agent-browser + headless Chrome inside ephemeral Vercel Sandbox microVMs. A Linux VM spins up on demand, executes browser commands, and shuts down. Works with any Vercel-deployed framework (Next.js, SvelteKit, Nuxt, Remix, Astro, etc.).

## How it is structured

The skill's own section headings, in order:

- Dependencies
- Core Pattern
- Screenshot
- Accessibility Snapshot
- Multi-Step Workflows
- Sandbox Snapshots (Fast Startup)
  - Creating a sandbox snapshot
- Authentication
- Scheduled Workflows (Cron)
- Environment Variables
- Framework Examples
- Example

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-browser:electron](vercel-labs-agent-browser-electron.md) - Automate Electron desktop apps (VS Code, Slack, Discord, Figma, Notion, Spotify, etc.) using agent-browser via
- [vercel-labs/agent-browser:agentcore](vercel-labs-agent-browser-agentcore.md) - Run agent-browser on AWS Bedrock AgentCore cloud browsers. Use when the user wants to use AgentCore, run brows
- [agent-browser](agent-browser.md) - Fast browser automation CLI for AI agents (vercel-labs/agent-browser). Use when the user asks to interact with
- [vercel-labs/agent-browser:agent-browser](vercel-labs-agent-browser-agent-browser.md) - Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating 

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:vercel-sandbox`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/vercel-sandbox --commit 04ba5264dade678062c3cdcce0f4f293e748249f --expect-tree 4428ac8f0e2afc17ffb8fe9898fb438c9000ae4340b4e06dd5edaa0c333876f5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
