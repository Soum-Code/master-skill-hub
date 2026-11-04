# motion-patterns

> Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exit animations, scroll, and layout — built on motion-foundations tokens and springs. Use when animating a specific UI element in React or Next.js — button, modal, toast, stagger, page transition, or scroll.

| | |
|---|---|
| **ID** | `affaan-m/ECC:motion-patterns` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 436 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when animating a specific UI element in React or Next.js — button, modal, toast, stagger, page transition, or scroll.

## What it says up front

> Copy-paste patterns for the most common UI animation needs. Every pattern here is built on `motion-foundations` tokens and springs. Do not define new duration or easing values here — import them.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Outputs
- Principles
- Rules
- Decision Guidance
  - Choosing the right pattern
  - When to use `mode="wait"` vs `mode="sync"`
- Core Concepts
  - AnimatePresence contract
  - layout vs layoutId
- Code Examples
  - Button feedback
  - Stagger list
  - Modal
  - Toast stack
  - Page transition (Next.js App Router)
  - Scroll reveal
  - Scroll progress bar
  - Expanding card
  - Shared-element crossfade
  - Accordion
- End-to-End Example
- Constraints / Non-Goals
- Anti-Patterns
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:motion-foundations](affaan-m-ecc-motion-foundations.md) - Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety
- [affaan-m/ECC:motion-advanced](affaan-m-ecc-motion-advanced.md) - Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custo
- [vercel-labs/agent-skills:vercel-react-view-transitions](vercel-labs-agent-skills-vercel-react-view-transitions.md) - Guide for implementing smooth, native-feeling animations using React's View Transition API (`` component, `add
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac

## Invoke / install

- Invoke: `/affaan-m/ECC:motion-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/motion-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 31ec389f976401728fbbdae9bc904ea4e47bf28b9bec68d1d7fd86b1fe8abff1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
