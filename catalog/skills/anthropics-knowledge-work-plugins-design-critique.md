# design-critique

> Get structured design feedback on usability, hierarchy, and consistency. Trigger with "review this design", "critique this mockup", "what do you think of this screen?", or when sharing a Figma link or screenshot for feedback at any stage from exploration to final polish.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:design-critique` |
| **Pack** | Web, Frontend & UI Design (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 119 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Get structured design feedback across multiple dimensions.

## How it is structured

The skill's own section headings, in order:

- Usage
- What I Need From You
- Critique Framework
  - 1. First Impression (2 seconds)
  - 2. Usability
  - 3. Visual Hierarchy
  - 4. Consistency
  - 5. Accessibility
- How to Give Feedback
- Output
- If Connectors Available
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:figma](openai-skills-figma.md) - Use the Figma MCP server to fetch design context, screenshots, variables, and assets from Figma, and to transl
- [anthropics/knowledge-work-plugins:accessibility-review](anthropics-knowledge-work-plugins-accessibility-review.md) - Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "
- [anthropics/knowledge-work-plugins:user-research](anthropics-knowledge-work-plugins-user-research.md) - Plan, conduct, and synthesize user research. Trigger with "user research plan", "interview guide", "usability 

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:design-critique`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path design/skills/design-critique --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 6a3d37dd498998eede1e30e29da3e37b8d9f320b0f2517518e1c3257d81541c5 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
