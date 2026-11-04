# mysql-patterns

> MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for production backends. Use when designing MySQL or MariaDB schemas and indexes, or when a query, transaction, or replica lags.

| | |
|---|---|
| **ID** | `affaan-m/ECC:mysql-patterns` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 414 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when designing MySQL or MariaDB schemas and indexes, or when a query, transaction, or replica lags.

## What it says up front

> Use this skill when working on MySQL or MariaDB schema design, migrations, slow-query investigation, queue-style transactions, connection pools, or production database configuration. Prefer exact version checks before applying a feature-specific pattern because MySQL and MariaDB have diverged in sev

## How it is structured

The skill's own section headings, in order:

- Activation
- Version Check
- Schema Defaults
- Indexing
- Query Patterns
  - Upsert
  - Keyset Pagination
  - JSON Fields
  - Full-Text Search
- Transactions
- Connection Pools
- Diagnostics
- Replication
- Security
- Configuration
- Anti-Patterns
- Output Expectations
- Related

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:postgres-patterns](affaan-m-ecc-postgres-patterns.md) - PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase 
- [affaan-m/ECC:jpa-patterns](affaan-m-ecc-jpa-patterns.md) - JPA/Hibernate patterns for entity design, relationships, query optimization, transactions, auditing, indexing,
- [affaan-m/ECC:prisma-patterns](affaan-m-ecc-prisma-patterns.md) - Prisma ORM patterns for TypeScript backends — schema design, query optimization, transactions, pagination, and
- [affaan-m/ECC:kotlin-exposed-patterns](affaan-m-ecc-kotlin-exposed-patterns.md) - JetBrains Exposed ORM patterns including DSL queries, DAO pattern, transactions, HikariCP connection pooling, 

## Invoke / install

- Invoke: `/affaan-m/ECC:mysql-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/mysql-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b4d4915e9a4bba34074f66557f32dc5bbf58cfe6ba276be2cd6f221286726e11 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
