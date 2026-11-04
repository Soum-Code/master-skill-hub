# react-performance

> React and Next.js performance optimization patterns adapted from Vercel Engineering's React Best Practices (https://github.com/vercel-labs/agent-skills). Organizes 70+ rules across 8 priority categories — waterfalls, bundle size, server-side, client fetching, re-render, rendering, JS micro-perf, advanced. Use when writing, reviewing, or refactoring React/Next.js code for performance.

| | |
|---|---|
| **ID** | `affaan-m/ECC:react-performance` |
| **Pack** | Software Development (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 576 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing, reviewing, or refactoring React/Next.js code for performance.

## What it says up front

> Performance optimization patterns for React 18/19 and Next.js, adapted from [Vercel Labs `react-best-practices`](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) (MIT, v1.0.0). This skill organizes rules by priority and provides decision-tree guidance for active cod

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Priority Index
- 1. Eliminating Waterfalls (CRITICAL)
  - Cheap conditions before await
  - Defer awaits until used
  - Promise.all for independent work
  - Partial dependencies — start early, await late
  - Suspense for streaming
  - Server Components: parallel through composition
- 2. Bundle Size Optimization (CRITICAL)
  - Direct imports, not barrels
  - Statically analyzable paths
  - Dynamic imports for heavy components
  - Defer third-party scripts
  - Conditional module loading
  - Preload on hover/focus
- 3. Server-Side Performance (HIGH)
  - Authenticate Server Actions like API routes
  - `React.cache()` for per-request deduplication
  - LRU cache for cross-request data
  - Avoid duplicate serialization in RSC props
  - Hoist static I/O to module scope
  - No mutable module-level state in RSC/SSR
  - Minimize data passed to Client Components
  - Parallelize nested fetches with Promise.all per item
  - Use `after()` for non-blocking work
- 4. Client-Side Data Fetching (MEDIUM-HIGH)
  - SWR / TanStack Query for deduplication
  - Deduplicate global event listeners
  - Passive listeners for scroll

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-skills:vercel-react-best-practices](vercel-labs-agent-skills-vercel-react-best-practices.md) - React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when 
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac
- [affaan-m/ECC:backend-patterns](affaan-m-ecc-backend-patterns.md) - Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, 
- [affaan-m/ECC:swiftui-patterns](affaan-m-ecc-swiftui-patterns.md) - SwiftUI architecture patterns, state management with @Observable, view composition, navigation, performance op

## Invoke / install

- Invoke: `/affaan-m/ECC:react-performance`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/react-performance --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 09db0ac893bdf8f3de9b080a9ab0e6ae6356483867fa7b089f9abc900e3dcab3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
