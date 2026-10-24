# dogfood

> Systematically explore and test a web application to find bugs, UX issues, and other problems. Use when asked to "dogfood", "QA", "exploratory test", "find issues", "bug hunt", "test this app/site/platform", or review the quality of a web application. Produces a structured report with full reproduction evidence -- step-by-step screenshots, repro videos, and detailed repro steps for every issue -- so findings can be handed directly to the responsible teams.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:dogfood` |
| **Pack** | Software Development (also: Browser & Web Automation, Careers, Jobs & Hiring) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 225 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when asked to "dogfood", "QA", "exploratory test", "find issues", "bug hunt", "test this app/site/platform", or review the quality of a web application.

## What it says up front

> Systematically explore a web application, find issues, and produce a report with full reproduction evidence for every finding.

## How it is structured

The skill's own section headings, in order:

- Setup
- Workflow
  - 1. Initialize
  - 2. Authenticate
  - 3. Orient
  - 4. Explore
  - 5. Document Issues (Repro-First)
  - 6. Wrap Up
- Guidance
- References
- Templates

## What it bundles

- reference docs: `references/issue-taxonomy.md`
- 1 other file(s)

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `agent-browser:*)`

## Related skills

- [bm:code-review](bm-code-review.md) - Review source files changed during a phase for bugs, security issues, and code quality problems
- [vercel-labs/agent-browser:agent-browser](vercel-labs-agent-browser-agent-browser.md) - Browser automation CLI for AI agents. Use when the user needs to interact with websites, including navigating 
- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:dogfood`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/dogfood --commit 372ac5ce20fab885dbf45ee0c9d510ec8c3b6fdb --expect-tree 24b3db742edc8a27d02baa61b2b4493209844bad176514f2fbe4f2e8b00bd3a9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
