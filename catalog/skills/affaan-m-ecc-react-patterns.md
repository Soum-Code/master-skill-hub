# react-patterns

> React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundaries, form actions, data fetching, state management decision trees, and accessibility-first composition. Use when writing or reviewing React components.

| | |
|---|---|
| **ID** | `affaan-m/ECC:react-patterns` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 343 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or reviewing React components.

## What it says up front

> Idiomatic React 18/19 patterns for building robust, accessible, performant component trees.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Principles
  - 1. Render is a Pure Function of Props and State
  - 2. Side Effects Outside Render
  - 3. Composition Over Inheritance
- Hooks Discipline
- State Location Decision Tree
- Server / Client Components (RSC)
- Suspense + Error Boundaries
- Forms
  - React 19 form actions (preferred for new code)
  - Controlled inputs
  - Complex forms
- Data Fetching Decision Matrix
- Composition Recipes
  - Slot via `children`
  - Named slots
  - Compound components (shared state via Context)
  - Render prop / function-as-child
- Performance
  - When `React.memo` Actually Helps
  - Avoiding Render Cascades
  - Lists
- Accessibility-First Composition
- Routing
- Out of Scope (Pointer Sections)
- Related
- Examples
  - Custom hook for debounced search
  - Optimistic UI with React 19 `useOptimistic`

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:react-native-patterns](affaan-m-ecc-react-native-patterns.md) - React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanS
- [affaan-m/ECC:react-testing](affaan-m-ecc-react-testing.md) - React component testing with React Testing Library, Vitest/Jest, MSW for network mocking, accessibility assert
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac
- [vercel-labs/agent-skills:vercel-react-best-practices](vercel-labs-agent-skills-vercel-react-best-practices.md) - React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when 

## Invoke / install

- Invoke: `/affaan-m/ECC:react-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/react-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b6fd778badb86720827ed66128cc7af799572571e51f45b1152f9d39e7ff5489 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
