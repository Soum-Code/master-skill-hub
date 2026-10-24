# chrome-browser

> Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named mcp__claude-in-chrome__* (also called Chrome, the browser extension, or the external browser) and which acts in the person's real Chrome with their own sign-ins; before those tools are turned on there may be a single enable__mcp__claude-in-chrome tool instead. It covers loading the tools in one ToolSearch call, checking the person's open tabs and working in a new tab, site permissions, GIF recordings, console logs, dialogs to avoid, and when to stop and ask. It is not for the built-in browser (mcp__Claude_Browser__* or mcp__remote-devices__Claude_Browser__* tools), which has its own skill, and it does not decide which browser to use.

| | |
|---|---|
| **ID** | `anthropic-skills:chrome-browser` |
| **Pack** | Browser & Web Automation |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | Proprietary. LICENSE.txt has complete terms |
| **Size** | 65 lines in SKILL.md, 2 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Claude in Chrome is a browser extension. Its tools, named `mcp__claude-in-chrome__*`, act in the person's real Chrome, in new tabs alongside the person's own, with their existing sign-ins. Claude in Chrome is available only while the person's Chrome is running with the extension connected; if its to

## How it is structured

The skill's own section headings, in order:

- Loading the tools
- Starting a session: tab context first, then a new tab
- Site permissions
- Recording a GIF
- Reading console output
- Alerts and dialogs
- Staying on task, and when to stop

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:built-in-browser](anthropic-skills-built-in-browser.md) - Read this skill before the first step that uses the built-in browser, the browser pane inside the Claude deskt
- [anthropic-skills:computer-use](anthropic-skills-computer-use.md) - Read this skill before the first step of any request to do something in an app on the person's own computer (N
- [anthropic-skills:docs](anthropic-skills-docs.md) - docs (editable docs people share and comment on; the default for any document, named as a doc or not: a docume
- [anthropic-skills:google-workspace](anthropic-skills-google-workspace.md) - Read this before the first Google Drive, Docs, Sheets or Slides connector call whenever the task creates or ch

## Invoke / install

- Invoke: `/anthropic-skills:chrome-browser`  (Skill tool: `anthropic-skills:chrome-browser`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
