# prisma-patterns

> Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and critical traps like updateMany returning count not records, $transaction timeouts, migrate dev resetting the DB, @updatedAt skipped on bulk writes, and serverless connection exhaustion. Use when writing a Prisma schema or query, or debugging transactions, migrations, or serverless connection limits.

| | |
|---|---|
| **ID** | `affaan-m/ECC:prisma-patterns` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 402 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing a Prisma schema or query, or debugging transactions, migrations, or serverless connection limits.

## What it says up front

> Production patterns and non-obvious traps for Prisma ORM in TypeScript backends.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Concepts
  - ID Strategy
  - Schema Defaults
  - `include` vs `select`
  - Transaction Form Selection
  - PrismaClient Singleton
  - N+1 Problem
- Code Examples
  - Cursor Pagination (preferred for feeds and large datasets)
  - Soft Delete
  - Error Handling
  - Connection Pool — Serverless
- Anti-Patterns
  - `updateMany` returns a count, not records
  - `$transaction` interactive form times out after 5 seconds
  - `migrate dev` can reset the database
  - Manually editing a migration file breaks future deploys
  - Breaking schema changes require multi-step migration
  - `@updatedAt` does not fire on `updateMany`
  - Soft delete + `findUniqueOrThrow` leaks deleted records
  - `deleteMany` without `where` deletes every row
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:mysql-patterns](affaan-m-ecc-mysql-patterns.md) - MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for producti
- [affaan-m/ECC:kotlin-exposed-patterns](affaan-m-ecc-kotlin-exposed-patterns.md) - JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, 
- [affaan-m/ECC:jpa-patterns](affaan-m-ecc-jpa-patterns.md) - JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing,
- [affaan-m/ECC:postgres-patterns](affaan-m-ecc-postgres-patterns.md) - PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase 

## Invoke / install

- Invoke: `/affaan-m/ECC:prisma-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/prisma-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 8207820fe692ae2cea1aff1ef9903f87384be00b99c05501274e2bc23bb2f8e9 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
