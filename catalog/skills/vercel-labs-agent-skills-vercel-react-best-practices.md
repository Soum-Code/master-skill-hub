# vercel-react-best-practices

> React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

| | |
|---|---|
| **ID** | `vercel-labs/agent-skills:vercel-react-best-practices` |
| **Pack** | Web, Frontend & UI Design (also: MLOps / DevOps / Cloud, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| **License** | MIT |
| **Size** | 150 lines in SKILL.md, 76 file(s) |

## When to use it

- Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

## What it says up front

> Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Contains 70 rules across 8 categories, prioritized by impact to guide automated refactoring and code generation.

## How it is structured

The skill's own section headings, in order:

- When to Apply
- Rule Categories by Priority
- Quick Reference
  - 1. Eliminating Waterfalls (CRITICAL)
  - 2. Bundle Size Optimization (CRITICAL)
  - 3. Server-Side Performance (HIGH)
  - 4. Client-Side Data Fetching (MEDIUM-HIGH)
  - 5. Re-render Optimization (MEDIUM)
  - 6. Rendering Performance (MEDIUM)
  - 7. JavaScript Performance (LOW-MEDIUM)
  - 8. Advanced Patterns (LOW)
- How to Use
- Full Compiled Document

## What it bundles

- 75 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-skills:vercel-react-native-skills](vercel-labs-agent-skills-vercel-react-native-skills.md) - React Native and Expo best practices for building performant mobile apps. Use when building React Native compo
- [vercel-labs/agent-skills:vercel-composition-patterns](vercel-labs-agent-skills-vercel-composition-patterns.md) - React composition patterns that scale. Use when refactoring components with boolean prop proliferation, buildi
- [openai/skills:security-best-practices](openai-skills-security-best-practices.md) - Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only 
- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility

## Invoke / install

- Invoke: `/vercel-labs/agent-skills:vercel-react-best-practices`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-skills --path skills/react-best-practices --commit 063bee94c3f4df8453406c830b0a7df0f2860278 --expect-tree 502eb06700e2c3cb1bd7f710860528f72281320bd5171a2087b05a090b573dc1 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
