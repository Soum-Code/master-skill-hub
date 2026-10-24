# chrome-extensions

> Build and publish Chrome Extensions using Manifest V3 best practices. Use this skill whenever the user asks to create, modify, debug, or understand Chrome browser extensions, add-ons, or anything involving the Chrome Extensions API. Trigger on mentions of: 'Chrome extension', 'browser extension', 'manifest.json', 'content script', 'service worker' (in browser context), 'popup' (in browser extension context), 'side panel', 'chrome.* API', 'declarativeNetRequest', 'omnibox', 'context menu' (in extension context), 'userScripts', 'user script', 'script manager', or any request to build functionality that integrates with the Chrome browser UI. Also trigger for publishing to the Chrome Web Store: 'publish extension', preparing an extension for publishing, responding to a review rejection, writing permission justifications, or drafting a privacy policy.

| | |
|---|---|
| **ID** | `modern-web-guidance:chrome-extensions` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `modern-web-guidance` v0.0.184 - [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 531 lines in SKILL.md, 24 file(s) |

## When to use it

- Use this skill whenever the user asks to create, modify, debug, or understand Chrome browser extensions, add-ons, or anything involving the Chrome Extensions API.
- Trigger on mentions of: 'Chrome extension', 'browser extension', 'manifest.json', 'content script', 'service worker' (in browser context), 'popup' (in browser extension context), 'side panel', 'chrome.* API', 'declarativeNetRequest', 'om.

## What it says up front

> Build production-quality Chrome extensions using Manifest V3 and publish them to the Chrome Web Store.

## How it is structured

The skill's own section headings, in order:

- Part 1 — Building Extensions
  - Mandatory Rules
  - Always Manifest V3
- Part 2 — Publishing to the Chrome Web Store
  - Core Workflow
  - How to fill it out
  - CHROMEWEBSTORE.md Sections
  - Pre-Publish Checklist
  - Store Listing Copy Guidelines
- Reference Files
- Output Checklist

## What it bundles

- reference docs: `references/extensions/api-calling.md`, `references/extensions/auth-identity.md`, `references/extensions/content-scripts.md`, `references/extensions/context-menus.md`, `references/extensions/csp-sandbox.md`, `references/extensions/declarative-net-request.md`, `references/extensions/devtools.md`, `references/extensions/icons.md` ...
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:microsoft-docs](microsoft-skills-microsoft-docs.md) - Understand Microsoft technologies by querying official documentation. Use whenever the user asks how something
- [anthropics/claude-code:MCP Integration](anthropics-claude-code-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [anthropics/claude-plugins-official:mcp-integration](anthropics-claude-plugins-official-mcp-integration.md) - This skill should be used when the user asks to "add MCP server", "integrate MCP", "configure MCP in plugin", 
- [vercel-labs/agent-skills:vercel-react-view-transitions](vercel-labs-agent-skills-vercel-react-view-transitions.md) - Guide for implementing smooth, native-feeling animations using React's View Transition API (`` component, `add

## Invoke / install

- Invoke: `/modern-web-guidance:chrome-extensions`  (Skill tool: `modern-web-guidance:chrome-extensions`)
- Install: `claude plugin marketplace add anthropics/claude-plugins-official && claude plugin install modern-web-guidance@claude-plugins-official`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
