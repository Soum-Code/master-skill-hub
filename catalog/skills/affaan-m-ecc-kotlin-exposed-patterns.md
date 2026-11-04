# kotlin-exposed-patterns

> JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, Flyway migrations, and repository pattern. Use when working with the Exposed ORM — DSL or DAO queries, transactions, pooling, or migrations.

| | |
|---|---|
| **ID** | `affaan-m/ECC:kotlin-exposed-patterns` |
| **Pack** | general |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 721 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when working with the Exposed ORM — DSL or DAO queries, transactions, pooling, or migrations.

## What it says up front

> Comprehensive patterns for database access with JetBrains Exposed ORM, including DSL queries, DAO, transactions, and production-ready configuration.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Examples
  - DSL Query
  - DAO Entity Usage
  - HikariCP Configuration
- Database Setup
  - HikariCP Connection Pooling
  - Flyway Migrations
  - Migration Files
- Table Definitions
  - DSL Style Tables
  - Composite Tables
- DSL Queries
  - Basic CRUD
  - Advanced Queries
  - Pagination
  - Batch Operations
- DAO Pattern
  - Entity Definitions
  - DAO Operations
- Transactions
  - Suspend Transaction Support
  - Transaction Isolation
- Repository Pattern
  - Interface Definition
  - Exposed Implementation
- JSON Columns
  - JSONB with kotlinx.serialization
- Testing with Exposed

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:mysql-patterns](affaan-m-ecc-mysql-patterns.md) - MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for producti
- [affaan-m/ECC:prisma-patterns](affaan-m-ecc-prisma-patterns.md) - Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and
- [affaan-m/ECC:kotlin-ktor-patterns](affaan-m-ecc-kotlin-ktor-patterns.md) - Ktor server patterns including routing DSL, plugins, authentication, Koin DI, kotlinx.serialization, WebSocket
- [affaan-m/ECC:jpa-patterns](affaan-m-ecc-jpa-patterns.md) - JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing,

## Invoke / install

- Invoke: `/affaan-m/ECC:kotlin-exposed-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/kotlin-exposed-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 2ad91cb7df1262922451c02090c091c7d04f1d97e7af2c63e2cd94719075e0b7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
