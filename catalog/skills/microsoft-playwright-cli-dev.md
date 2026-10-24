# dev

> Development workflows for the playwright-cli repository. Use when the user asks about rolling dependencies, releasing, or other repo maintenance tasks.

| | |
|---|---|
| **ID** | `microsoft/playwright-cli:dev` |
| **Pack** | Browser & Web Automation (also: Claude / Skills / Plugin Tooling, MLOps / DevOps / Cloud, Operations & Business) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/playwright-cli](https://github.com/microsoft/playwright-cli) |
| **License** | Apache-2.0 |
| **Size** | 10 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when the user asks about rolling dependencies, releasing, or other repo maintenance tasks.

## What it bundles

- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:netlify-deploy](openai-skills-netlify-deploy.md) - Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, 
- [productivity:task-management](productivity-task-management.md) - Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, want
- [engineering:tech-debt](engineering-tech-debt.md) - Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what s
- [playwright-cli](playwright-cli.md) - Official Microsoft browser automation CLI (@playwright/cli). Use when the user asks to automate browser intera

## Invoke / install

- Invoke: `/microsoft/playwright-cli:dev`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/playwright-cli --path .claude/skills/dev --commit b1a5903c5b633b8c9f843ad7b629c2a78437040c --expect-tree 85de6010a0e1eb5827f856c9caabf92252d3a8f5308bcc72f457435b9cdf20cf --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
