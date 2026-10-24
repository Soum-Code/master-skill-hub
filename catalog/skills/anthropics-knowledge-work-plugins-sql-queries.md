# sql-queries

> Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.). Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:sql-queries` |
| **Pack** | Data & Analytics (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 429 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing queries, optimizing slow SQL, translating between dialects, or building complex analytical queries with CTEs, window functions, or aggregations.

## What it says up front

> Write correct, performant, readable SQL across all major data warehouse dialects.

## How it is structured

The skill's own section headings, in order:

- Dialect-Specific Reference
  - PostgreSQL (including Aurora, RDS, Supabase, Neon)
  - Snowflake
  - BigQuery (Google Cloud)
  - Redshift (Amazon)
  - Databricks SQL
- Common SQL Patterns
  - Window Functions
  - CTEs for Readability
  - Cohort Retention
  - Funnel Analysis
  - Deduplication
- Error Handling and Debugging

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:write-query](anthropics-knowledge-work-plugins-write-query.md) - Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need in

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:sql-queries`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path data/skills/sql-queries --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree c30fd7ee92029ad0151eb60b0bab429afaa288d09110fdde8579195ecfb4f960 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
