# api-connector-builder

> Build a new API connector or provider by matching the target repo's existing integration pattern exactly. Use when adding one more integration without inventing a second architecture.

| | |
|---|---|
| **ID** | `affaan-m/ECC:api-connector-builder` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 122 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adding one more integration without inventing a second architecture.

## What it says up front

> Use this when the job is to add a repo-native integration surface, not just a generic HTTP client.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Guardrails
- Workflow
  - 1. Learn the house style
  - 2. Narrow the target integration
  - 3. Build in repo-native layers
  - 4. Validate against the source pattern
- Reference Shapes
  - Provider-style
  - Connector-style
  - TypeScript plugin-style
- Quality Checklist
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:nestjs-patterns](affaan-m-ecc-nestjs-patterns.md) - NestJS architecture patterns for modules, controllers, providers, DTO validation, guards, interceptors, config
- [affaan-m/ECC:laravel-patterns](affaan-m-ecc-laravel-patterns.md) - Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and
- [affaan-m/ECC:django-patterns](affaan-m-ecc-django-patterns.md) - Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and 
- [affaan-m/ECC:backend-patterns](affaan-m-ecc-backend-patterns.md) - Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, 

## Invoke / install

- Invoke: `/affaan-m/ECC:api-connector-builder`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/api-connector-builder --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 00c4cc54f8a3f142522355966d4059c55692041f937663cdfbaabeafc8f50648 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
