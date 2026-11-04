# clickhouse-io

> ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloads. Use when writing ClickHouse schemas or queries, or when an analytical query is too slow.

| | |
|---|---|
| **ID** | `affaan-m/ECC:clickhouse-io` |
| **Pack** | Data & Analytics (also: Operations & Business, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 446 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing ClickHouse schemas or queries, or when an analytical query is too slow.

## What it says up front

> ClickHouse-specific patterns for high-performance analytics and data engineering.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Overview
- Table Design Patterns
  - MergeTree Engine (Most Common)
  - ReplacingMergeTree (Deduplication)
  - AggregatingMergeTree (Pre-aggregation)
- Query Optimization Patterns
  - Efficient Filtering
  - Aggregations
  - Window Functions
- Data Insertion Patterns
  - Bulk Insert (Recommended)
  - Streaming Insert
- Materialized Views
  - Real-time Aggregations
- Performance Monitoring
  - Query Performance
  - Table Statistics
- Common Analytics Queries
  - Time Series Analysis
  - Funnel Analysis
  - Cohort Analysis
- Data Pipeline Patterns
  - ETL Pattern
  - Change Data Capture (CDC)
- Best Practices
  - 1. Partitioning Strategy
  - 2. Ordering Key
  - 3. Data Types
  - 4. Avoid

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:postgres-patterns](affaan-m-ecc-postgres-patterns.md) - PostgreSQL database patterns for query optimization, schema design, indexing, and security. Based on Supabase 
- [vercel-labs/agent-skills:vercel-react-best-practices](vercel-labs-agent-skills-vercel-react-best-practices.md) - React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when 
- [affaan-m/ECC:backend-patterns](affaan-m-ecc-backend-patterns.md) - Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, 
- [affaan-m/ECC:frontend-patterns](affaan-m-ecc-frontend-patterns.md) - Frontend development patterns for React, Next.js, state management, performance optimization, and UI best prac

## Invoke / install

- Invoke: `/affaan-m/ECC:clickhouse-io`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/clickhouse-io --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3e7d737226488ed4206420353fb29de46120a955de28c6dbf3d740e05d75273a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
