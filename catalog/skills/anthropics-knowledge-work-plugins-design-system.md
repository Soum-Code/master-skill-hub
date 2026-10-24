# design-system

> Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, and accessibility notes, or designing a new pattern that fits the existing system.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:design-system` |
| **Pack** | Software Development (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 191 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when checking for naming inconsistencies or hardcoded values across components, writing documentation for a component's variants, states, and accessibility notes, or designing a new pattern that fits the existing system.

## What it says up front

> Manage your design system — audit for consistency, document components, or design new patterns.

## How it is structured

The skill's own section headings, in order:

- Usage
- Components of a Design System
  - Design Tokens
  - Components
  - Patterns
- Principles
- Output — Audit
- Output — Document
- Output — Extend
- If Connectors Available
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility
- [engineering:architecture](engineering-architecture.md) - Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka 
- [microsoft/skills:frontend-design-review](microsoft-skills-frontend-design-review.md) - Review and create distinctive, production-grade frontend interfaces with high design quality and design system
- [legal:vendor-check](legal-vendor-check.md) - Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and docu

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:design-system`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path design/skills/design-system --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree c8ca8dcb903113e96d457dc22e6b1146d555ff49065dd7ff003ab04235c2ac1c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
