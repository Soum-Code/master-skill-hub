# api-design

> REST API design patterns including resource naming, status codes, pagination, filtering, error responses, versioning, and rate limiting for production APIs. Use when designing or reviewing REST endpoints, resource names, status codes, pagination, or versioning.

| | |
|---|---|
| **ID** | `affaan-m/ECC:api-design` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 525 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when designing or reviewing REST endpoints, resource names, status codes, pagination, or versioning.

## What it says up front

> Conventions and best practices for designing consistent, developer-friendly REST APIs.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Resource Design
  - URL Structure
  - Naming Rules
- HTTP Methods and Status Codes
  - Method Semantics
  - Status Code Reference
  - Common Mistakes
- Response Format
  - Success Response
  - Collection Response (with Pagination)
  - Error Response
  - Response Envelope Variants
- Pagination
  - Offset-Based (Simple)
  - Cursor-Based (Scalable)
  - When to Use Which
- Filtering, Sorting, and Search
  - Filtering
  - Sorting
  - Full-Text Search
  - Sparse Fieldsets
- Authentication and Authorization
  - Token-Based Auth
  - Authorization Patterns
- Rate Limiting
  - Headers
  - Rate Limit Tiers
- Versioning
  - URL Path Versioning (Recommended)

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:django-patterns](affaan-m-ecc-django-patterns.md) - Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and 
- [affaan-m/ECC:redis-patterns](affaan-m-ecc-redis-patterns.md) - Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection m
- [affaan-m/ECC:laravel-patterns](affaan-m-ecc-laravel-patterns.md) - Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and
- [affaan-m/ECC:springboot-patterns](affaan-m-ecc-springboot-patterns.md) - Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, 

## Invoke / install

- Invoke: `/affaan-m/ECC:api-design`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/api-design --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 0aef4813900d15d454c4d9a7097f508c0c5f82b5547b5d3b6600f1f25a2d0ff3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
