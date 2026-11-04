# accessibility

> Design, implement, and audit accessible UI to WCAG 2.2 Level AA across Web, iOS, and Android — semantic ARIA roles and labels, accessibility traits and hints, focus management, contrast, target size, and screen-reader support. Use when building or auditing UI for accessibility compliance, keyboard navigation, or screen-reader support.

| | |
|---|---|
| **ID** | `affaan-m/ECC:accessibility` |
| **Pack** | Web, Frontend & UI Design (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 147 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building or auditing UI for accessibility compliance, keyboard navigation, or screen-reader support.

## What it says up front

> This skill ensures that digital interfaces are Perceivable, Operable, Understandable, and Robust (POUR) for all users, including those using screen readers, switch controls, or keyboard navigation. It focuses on the technical implementation of WCAG 2.2 success criteria.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Core Concepts
- How It Works
  - Step 1: Identify the Component Role
  - Step 2: Define Perceivable Attributes
  - Step 3: Implement Operable Controls
  - Step 4: Ensure Understandable Logic
  - Step 5: Verify Robust Compatibility
- Accessibility Architecture Diagram
- Cross-Platform Mapping
- Examples
  - Web: Accessible Search
  - iOS: Accessible Action Button
  - Android: Accessible Toggle
- Anti-Patterns to Avoid
- Best Practices Checklist
- References
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:accessibility-review](anthropics-knowledge-work-plugins-accessibility-review.md) - Run a WCAG 2.1 AA accessibility audit on a design or page. Trigger with "audit accessibility", "check a11y", "
- [affaan-m/ECC:frontend-a11y](affaan-m-ecc-frontend-a11y.md) - Accessibility patterns for React and Next.js — semantic HTML, ARIA attributes, form labeling, keyboard navigat
- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility
- [affaan-m/ECC:swiftui-patterns](affaan-m-ecc-swiftui-patterns.md) - SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance op

## Invoke / install

- Invoke: `/affaan-m/ECC:accessibility`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/accessibility --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 74f4023c702382bed7c5b285c5121b17abf22cde63f75210c636dbaf9a1d77e6 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
