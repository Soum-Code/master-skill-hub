# kotlin-ktor-patterns

> Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSockets, and testApplication testing. Use when building a Ktor server — routing, plugins, auth, DI, serialization, or tests.

| | |
|---|---|
| **ID** | `affaan-m/ECC:kotlin-ktor-patterns` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 691 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when building a Ktor server — routing, plugins, auth, DI, serialization, or tests.

## What it says up front

> Comprehensive Ktor patterns for building robust, maintainable HTTP servers with Kotlin coroutines.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Application Structure
  - Standard Ktor Project Layout
  - Application Entry Point
- Routing DSL
  - Basic Routes
  - Route Organization with Authenticated Routes
- Content Negotiation & Serialization
  - kotlinx.serialization Setup
  - Serializable Models
  - Custom Serializers
- Authentication
  - JWT Authentication
  - Auth Routes
- Status Pages (Error Handling)
- CORS Configuration
- Koin Dependency Injection
  - Module Definition
  - Using Koin in Routes
  - Koin for Testing
- Request Validation
- WebSockets
- testApplication Testing
  - Basic Route Testing
  - Testing Authenticated Routes
- Configuration
  - application.yaml
  - Reading Config
- Quick Reference: Ktor Patterns

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:kotlin-exposed-patterns](affaan-m-ecc-kotlin-exposed-patterns.md) - JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, 
- [affaan-m/ECC:fastapi-patterns](affaan-m-ecc-fastapi-patterns.md) - FastAPI best practices covering project structure, Pydantic v2 schemas, dependency injection, async handlers, 
- [affaan-m/ECC:vite-patterns](affaan-m-ecc-vite-patterns.md) - Vite build tool patterns including config, plugins, HMR, env variables, proxy setup, SSR, library mode, depend
- [affaan-m/ECC:kotlin-patterns](affaan-m-ecc-kotlin-patterns.md) - Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Ko

## Invoke / install

- Invoke: `/affaan-m/ECC:kotlin-ktor-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/kotlin-ktor-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 94d812c5662c5ab146489b824aae69fe1ab067eb56b51f53189d951417dd4a78 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
