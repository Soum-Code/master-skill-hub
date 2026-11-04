# browser-qa

> Run automated post-deploy UI verification with a browser automation MCP (claude-in-chrome, Playwright, or Puppeteer): console-error and Core Web Vitals smoke checks, form and auth-flow interaction tests, screenshot visual regression across three breakpoints, and axe-core accessibility audits ending in a SHIP / DO-NOT-SHIP verdict. Use when testing a deployed feature on staging or preview, before shipping frontend changes, reviewing a frontend PR, or checking responsive layout and accessibility.

| | |
|---|---|
| **ID** | `affaan-m/ECC:browser-qa` |
| **Pack** | Browser & Web Automation (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 106 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when testing a deployed feature on staging or preview, before shipping frontend changes, reviewing a frontend PR, or checking responsive layout and accessibility.

## What it says up front

> Uses the browser automation MCP (claude-in-chrome, Playwright, or Puppeteer) to interact with live pages like a real user.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Safety first — blast radius (run read-only by default)
  - Phase 1: Smoke Test
  - Phase 2: Interaction Test
  - Phase 3: Visual Regression
  - Phase 4: Accessibility
- Output Format
- Integration

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [example-skills:webapp-testing](example-skills-webapp-testing.md) - Toolkit for interacting with and testing local web applications using Playwright. Supports verifying frontend 
- [microsoft/skills:frontend-design-review](microsoft-skills-frontend-design-review.md) - Review and create distinctive, production-grade frontend interfaces with high design quality and design system
- [openai/skills:playwright](openai-skills-playwright.md) - Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, s
- [affaan-m/ECC:canary-watch](affaan-m-ecc-canary-watch.md) - Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, stati

## Invoke / install

- Invoke: `/affaan-m/ECC:browser-qa`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/browser-qa --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e6e858168e2eab3c28af9db2cea9dcf202b53cbdba1c824fb1958168c1b01428 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
