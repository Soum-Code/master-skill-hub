# accessibility-review

> Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "is this accessible?", or when reviewing a design for color contrast, keyboard navigation, touch target size, or screen reader behavior before handoff.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:accessibility-review` |
| **Pack** | Web, Frontend & UI Design (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 129 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Audit a design or page for WCAG 2.1 AA accessibility compliance.

## How it is structured

The skill's own section headings, in order:

- Usage
- WCAG 2.1 AA Quick Reference
  - Perceivable
  - Operable
  - Understandable
  - Robust
- Common Issues
- Testing Approach
- Output
- If Connectors Available
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility
- [vercel-labs/agent-skills:writing-guidelines](vercel-labs-agent-skills-writing-guidelines.md) - Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style"
- [anthropics/knowledge-work-plugins:design-critique](anthropics-knowledge-work-plugins-design-critique.md) - Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "c
- [anthropics/knowledge-work-plugins:design-system](anthropics-knowledge-work-plugins-design-system.md) - Audit, document, or extend your design system. Use when checking for naming inconsistencies or hardcoded value

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:accessibility-review`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path design/skills/accessibility-review --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree ca1845c4991a886854f150a772007be2dd1756ef561d2aa5f6706e9b42cc9e0d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
