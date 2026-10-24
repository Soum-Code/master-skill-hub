# frontend-design-review

> Review and create distinctive, production-grade frontend interfaces with high design quality and design system compliance. Evaluates using three pillars: frictionless insight-to-action, quality craft, and trustworthy building. USE FOR: PR reviews, design reviews, accessibility audits, design system compliance checks, creative frontend design, UI code review, component reviews, responsive design checks, theme testing, and creating memorable UI. DO NOT USE FOR: Backend API reviews, database schema reviews, infrastructure or DevOps work, pure business logic without UI, or non-frontend code.

| | |
|---|---|
| **ID** | `microsoft/skills:frontend-design-review` |
| **Pack** | Software Development (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 139 lines in SKILL.md, 5 file(s) |

## When to use it

- USE FOR: PR reviews, design reviews, accessibility audits, design system compliance checks, creative frontend design, UI code review, component reviews, responsive design checks, theme testing, and creating memorable UI.
- DO NOT USE FOR: Backend API reviews, database schema reviews, infrastructure or DevOps work, pure business logic without UI, or non-frontend code.

## What it says up front

> Review UI implementations against design quality standards and your design system **OR** create distinctive, production-grade frontend interfaces from scratch.

## How it is structured

The skill's own section headings, in order:

- Two Modes
  - Mode 1: Design Review
  - Mode 2: Creative Frontend Design
- Creative Frontend Design
  - Aesthetics Guidelines
- Design Review
  - Design System Workflow
  - Review Process
  - Core Principles
- Quality Pillars
  - 1. Frictionless Insight to Action
  - 2. Quality is Craft
  - 3. Trustworthy Building
- Review Output Format
- Review Type Modifiers
- Quick Checklist
- Pattern Examples
- Acknowledgments

## What it bundles

- reference docs: `references/pattern-examples.md`, `references/quick-checklist.md`, `references/review-output-format.md`, `references/review-type-modifiers.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility
- [bm:ui-review](bm-ui-review.md) - Retroactive 6-pillar visual audit of implemented frontend code
- [anthropics/knowledge-work-plugins:design-system](anthropics-knowledge-work-plugins-design-system.md) - Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded value
- [engineering:architecture](engineering-architecture.md) - Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka 

## Invoke / install

- Invoke: `/microsoft/skills:frontend-design-review`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/frontend-design-review --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 04f1a4dec6c7f487aecc9d41d2111aa0c36a7753dba1eeee948e8c3a59cf9e5f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
