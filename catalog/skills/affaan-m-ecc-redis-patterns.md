# redis-patterns

> Redis data structure patterns, caching strategies, distributed locks, rate limiting, pub/sub, and connection management for production applications. Use when adding caching, a distributed lock, rate limiting, or pub/sub with Redis, or when key design needs review.

| | |
|---|---|
| **ID** | `affaan-m/ECC:redis-patterns` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 405 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adding caching, a distributed lock, rate limiting, or pub/sub with Redis, or when key design needs review.

## What it says up front

> Quick reference for Redis best practices across common backend use cases.

## How it is structured

The skill's own section headings, in order:

- How It Works
- When to Activate
- Data Structure Cheat Sheet
- Core Patterns
  - Cache-Aside (Lazy Loading)
  - Write-Through Cache
  - Cache Invalidation
  - Session Storage
- Rate Limiting
  - Fixed Window (Simple)
  - Sliding Window (Lua — Atomic)
- Distributed Locks
  - Distributed Lock (Single Node — SET NX PX)
- Pub/Sub & Streams
  - Pub/Sub (Fire-and-Forget)
  - Redis Streams (Durable Queue)
- Key Design
  - Naming Conventions
  - TTL Strategy
- Connection Management
  - Connection Pooling
  - Cluster Mode
  - Sentinel (High Availability)
- Eviction Policies
- Anti-Patterns
  - Cache Miss Stampede Prevention
- Examples
- Quick Reference
- Related

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:api-design](affaan-m-ecc-api-design.md) - REST API design patterns including resource naming, status codes, pagination, filtering, error responses, vers
- [affaan-m/ECC:django-patterns](affaan-m-ecc-django-patterns.md) - Django architecture patterns, REST API design with DRF, ORM best practices, caching, signals, middleware, and 
- [affaan-m/ECC:springboot-patterns](affaan-m-ecc-springboot-patterns.md) - Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, 
- [affaan-m/ECC:mysql-patterns](affaan-m-ecc-mysql-patterns.md) - MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for producti

## Invoke / install

- Invoke: `/affaan-m/ECC:redis-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/redis-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f9e3fbaf3356d9fde6610f58f18b742d0ddb8fc444ebf266203b5764b81e72ff --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
