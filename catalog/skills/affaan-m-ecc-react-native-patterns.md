# react-native-patterns

> React Native and Expo app patterns — Expo Router navigation, state separation (server/client/route/form), TanStack Query data fetching with Zod, performant lists, NativeWind/StyleSheet styling, native APIs, and secure storage. Use when building or editing React Native / Expo screens, components, navigation, or data layers.

| | |
|---|---|
| **ID** | `affaan-m/ECC:react-native-patterns` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 327 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building or editing React Native / Expo screens, components, navigation, or data layers.

## What it says up front

> Practical patterns for building production React Native apps with Expo. Covers navigation, state, data fetching, lists, styling, and native APIs. Pairs with the `rules/react-native/` ruleset: rules say *what* to enforce, this skill shows *how*.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
  - Project structure (Expo Router)
  - Navigation: validate route params
  - State: keep concerns separate
  - Data fetching: a cache library + Zod
  - Lists: virtualize, never map a big array in a ScrollView
  - Styling: pick one system
  - Native APIs: wrap in hooks, clean up effects
  - Secure storage for tokens
- Code Examples
  - A full screen: route → query → list → states
  - A form: React Hook Form + Zod resolver
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-skills:vercel-react-native-skills](vercel-labs-agent-skills-vercel-react-native-skills.md) - React Native and Expo best practices for building performant mobile apps. Use when building React Native compo
- [affaan-m/ECC:react-patterns](affaan-m-ecc-react-patterns.md) - React 18/19 patterns including hooks discipline, server/client component boundaries, Suspense + error boundari
- [affaan-m/ECC:vue-patterns](affaan-m-ecc-vue-patterns.md) - Vue.js 3 Composition API patterns, component architecture, reactivity best practices, Pinia state management, 
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac

## Invoke / install

- Invoke: `/affaan-m/ECC:react-native-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/react-native-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 739235562badfb05d9e66ecca63f2e20748548d431b090a6c80189a9ed19196d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
