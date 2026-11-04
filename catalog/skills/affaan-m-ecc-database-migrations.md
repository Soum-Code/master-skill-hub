# database-migrations

> Safe, reversible database migration patterns: forward-only production changes, expand-contract zero-downtime renames, concurrent indexes, batched backfills, and per-tool workflows for PostgreSQL, Prisma, Drizzle, Kysely, Django, and golang-migrate. Use when writing a schema or data migration, adding a column or index to a large table, planning a rollback, or preparing a zero-downtime deploy.

| | |
|---|---|
| **ID** | `affaan-m/ECC:database-migrations` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 431 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing a schema or data migration, adding a column or index to a large table, planning a rollback, or preparing a zero-downtime deploy.

## What it says up front

> Safe, reversible database schema changes for production systems.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Principles
- Migration Safety Checklist
- PostgreSQL Patterns
  - Adding a Column Safely
  - Adding an Index Without Downtime
  - Renaming a Column (Zero-Downtime)
  - Removing a Column Safely
  - Large Data Migrations
- Prisma (TypeScript/Node.js)
  - Workflow
  - Schema Example
  - Custom SQL Migration
- Drizzle (TypeScript/Node.js)
  - Workflow
  - Schema Example
- Kysely (TypeScript/Node.js)
  - Workflow (kysely-ctl)
  - Migration File
  - Programmatic Migrator
- Django (Python)
  - Workflow
  - Data Migration
  - SeparateDatabaseAndState
- golang-migrate (Go)
  - Workflow
  - Migration Files
- Zero-Downtime Migration Strategy
  - Timeline Example
- Anti-Patterns

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:postgres-patterns](affaan-m-ecc-postgres-patterns.md) - PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase 
- [affaan-m/ECC:mysql-patterns](affaan-m-ecc-mysql-patterns.md) - MySQL and MariaDB schema, query, indexing, transaction, replication, and connection-pool patterns for producti
- [affaan-m/ECC:change-impact](affaan-m-ecc-change-impact.md) - Perform evidence-backed impact analysis before changing code, data, interfaces, or governance documents, then 
- [engineering:deploy-checklist](engineering-deploy-checklist.md) - Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migr

## Invoke / install

- Invoke: `/affaan-m/ECC:database-migrations`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/database-migrations --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree ec7220772a409af64dbb4938342494e215d64c63457a6d7b520c3104dd262a30 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
