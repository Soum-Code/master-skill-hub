# vercel-react-view-transitions

> Guide for implementing smooth, native-feeling animations using React's View Transition API (`` component, `addTransitionType`, and CSS view transition pseudo-elements). Use this skill whenever the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, implement directional (forward/back) navigation animations, or integrate view transitions in Next.js. Also use when the user mentions view transitions, `startViewTransition`, `ViewTransition`, transition types, or asks about animating between UI states in React without third-party animation libraries.

| | |
|---|---|
| **ID** | `vercel-labs/agent-skills:vercel-react-view-transitions` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| **License** | MIT |
| **Size** | 333 lines in SKILL.md, 9 file(s) |

## When to use it

- Use this skill whenever the user wants to add page transitions, animate route changes, create shared element animations, animate enter/exit of components, animate list reorder, implement directional (forward/back) navigation animations, or integrate view trans.

## What it says up front

> Animate between UI states using the browser's native `document.startViewTransition`. Declare *what* with ``, trigger *when* with `startTransition` / `useDeferredValue` / `Suspense`, control *how* with CSS classes. Unsupported browsers skip animations gracefully.

## How it is structured

The skill's own section headings, in order:

- When to Animate
  - Choosing Animation Style
- Availability
- Implementation Workflow
- Core Concepts
  - The `` Component
  - Animation Triggers
  - Critical Placement Rule
- Styling with View Transition Classes
  - Props
  - CSS Pseudo-Elements
- Transition Types
  - `router.back()` and Browser Back Button
  - Types and Suspense
  - Shared Element Readiness
- Shared Element Transitions
- Common Patterns
  - Enter/Exit
  - List Reorder
  - Layout Displacement Morph
  - Composing Shared Elements with List Identity
  - Force Re-Enter with `key`
  - Suspense Fallback to Content
- How Multiple VTs Interact
  - Use `default="none"` Deliberately
  - Two Patterns Coexist
  - Nested VT Limitation
- Next.js Integration
- Accessibility
- Reference Files

## What it bundles

- reference docs: `references/css-recipes.md`, `references/implementation.md`, `references/nextjs.md`, `references/patterns.md`, `references/troubleshooting.md`
- 3 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:motion-patterns](affaan-m-ecc-motion-patterns.md) - Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exi
- [vercel-labs/agent-skills:vercel-react-native-skills](vercel-labs-agent-skills-vercel-react-native-skills.md) - React Native and Expo best practices for building performant mobile apps. Use when building React Native compo
- [affaan-m/ECC:react-native-patterns](affaan-m-ecc-react-native-patterns.md) - React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanS
- [openai/skills:figma-generate-library](openai-skills-figma-generate-library.md) - Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create

## Invoke / install

- Invoke: `/vercel-labs/agent-skills:vercel-react-view-transitions`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-skills --path skills/react-view-transitions --commit 1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62 --expect-tree 0706daa0bac7d5e9cb2a8b1622f5ebe3e7f3fa34cd749ff67c7c25ce00acb36c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
