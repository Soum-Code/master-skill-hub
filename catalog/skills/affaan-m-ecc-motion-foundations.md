# motion-foundations

> Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety for React / Next.js using motion/react. Foundation layer — all other motion skills depend on this. Use when setting up motion tokens, spring presets, reduced-motion handling, or SSR-safe animation in React or Next.js.

| | |
|---|---|
| **ID** | `affaan-m/ECC:motion-foundations` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 301 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when setting up motion tokens, spring presets, reduced-motion handling, or SSR-safe animation in React or Next.js.

## What it says up front

> The base layer of the motion system. Defines every value, constraint, and rule that downstream skills (`motion-patterns`, `motion-advanced`) inherit. Load this skill before any animation work begins.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Outputs
- Principles
- Rules
- Decision Guidance
  - Choosing a duration
  - Choosing a spring
  - When to disable animation entirely
- Core Concepts
  - Token system
  - Runtime flags
  - Accessibility
  - SSR / hydration safety
- Code Examples
  - End-to-end: tokens + springs + accessibility + SSR guard
- Constraints / Non-Goals
- Anti-Patterns
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:motion-patterns](affaan-m-ecc-motion-patterns.md) - Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exi
- [affaan-m/ECC:motion-advanced](affaan-m-ecc-motion-advanced.md) - Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custo
- [affaan-m/ECC:nuxt4-patterns](affaan-m-ecc-nuxt4-patterns.md) - Nuxt 4 app patterns for hydration safety, performance, route rules, lazy loading, and SSR-safe data fetching w
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac

## Invoke / install

- Invoke: `/affaan-m/ECC:motion-foundations`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/motion-foundations --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c929ee32a0158966db75a9944f19e94ede7ad3a3d6416882fc329cc5d358b429 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
