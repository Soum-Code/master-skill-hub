# modern-web-guidance

> Apply Chrome's Modern Web Guidance to frontend code, then verify the built page in a real browser with agent-browser. Use when asked to build or modernize UI with web platform best practices, follow Modern Web Guidance or Baseline guidance, or check that a change fixed layout shift, respects reduced motion or the color scheme, or gives a dialog correct focus and inert behavior. Triggers include "use modern web guidance", "modern web best practices", "fix layout shift", "respect reduced motion", "add dark mode", "build an accessible dialog", and "verify this against the guide".

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:modern-web-guidance` |
| **Pack** | Browser & Web Automation (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 166 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when asked to build or modernize UI with web platform best practices, follow Modern Web Guidance or Baseline guidance, or check that a change fixed layout shift, respects reduced motion or the color scheme, or gives a dialog correct focus and inert behavio.

## What it says up front

> Use Modern Web Guidance to decide what to write and agent-browser to check the built page in Chrome. Finish only after every rule you applied has a browser check with recorded evidence.

## How it is structured

The skill's own section headings, in order:

- Get the guidance
- Workflow
- Layout shift
- Reduced motion
- Color scheme
- Dialog focus and inertness
- Report
- Cleanup

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `modern-web-guidance@latest:*)`

## Related skills

- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility
- [anthropics/claude-code:Agent Development](anthropics-claude-code-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [anthropics/claude-plugins-official:agent-development](anthropics-claude-plugins-official-agent-development.md) - This skill should be used when the user asks to "create an agent", "add an agent", "write a subagent", "agent 
- [example-skills:webapp-testing](example-skills-webapp-testing.md) - Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend 

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:modern-web-guidance`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/modern-web-guidance --commit 4720bc3dd73f2c8f7c84f415adfa560330b924c4 --expect-tree d0d165350f283304c6a13173619ee19d8a109eb069acbbe5b9993e64dba16918 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
