# built-in-browser

> Read this skill before the first step that uses the built-in browser, the browser pane inside the Claude desktop app (also called the in-app browser, the browser pane, Claude's browser, or "your own browser"), whose tools are named mcp__Claude_Browser__* when the session runs in the desktop app and mcp__remote-devices__Claude_Browser__* when a cloud session is linked to the person's computer; before those tools are turned on there may be a single enable__mcp__remote-devices__Claude_Browser tool instead. It covers the pane's persistent sign-ins, tabs and preview_start, reading pages as text, site approvals, what the pane cannot open, and what to do when it cannot be reached. It is not for Claude in Chrome (mcp__claude-in-chrome__* tools), which has its own skill, and it does not decide which browser to use.

| | |
|---|---|
| **ID** | `anthropic-skills:built-in-browser` |
| **Pack** | Browser & Web Automation (also: Claude / Skills / Plugin Tooling) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 49 lines in SKILL.md, 2 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> The built-in browser is a real browser pane inside the Claude desktop app, separate from the person's Chrome. Its tools are named `mcp__Claude_Browser__*` when the session itself runs inside the desktop app, and `mcp__remote-devices__Claude_Browser__*` when the session runs in the cloud (started fro

## How it is structured

The skill's own section headings, in order:

- What the person can see
- Sign-ins persist, and they are the person's
- Tabs
- Loading via ToolSearch
- Reading pages
- Site approvals, blocked sites, and request_access
- What the built-in browser cannot open
- When the built-in browser cannot be reached

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:chrome-browser](anthropic-skills-chrome-browser.md) - Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named 
- [anthropic-skills:computer-use](anthropic-skills-computer-use.md) - Read this skill before the first step of any request to do something in an app on the person's own computer (N
- [vercel-labs/agent-browser:agent-browser](vercel-labs-agent-browser-agent-browser.md) - Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating 
- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume

## Invoke / install

- Invoke: `/anthropic-skills:built-in-browser`  (Skill tool: `anthropic-skills:built-in-browser`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
