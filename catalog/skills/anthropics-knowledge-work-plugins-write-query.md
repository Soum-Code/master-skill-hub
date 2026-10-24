# write-query

> Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitioned table, or getting dialect-specific syntax for Snowflake, BigQuery, Postgres, etc.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:write-query` |
| **Pack** | Documents, Writing & Content (also: Data & Analytics) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 123 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when translating a natural-language data need into SQL, building a multi-CTE query with joins and aggregations, optimizing a query against a large partitioned table, or getting dialect-specific syntax for Snowflake, BigQuery, Postgres, etc.

## What it says up front

> Write a SQL query from a natural language description, optimized for your specific SQL dialect and following best practices.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Understand the Request
  - 2. Determine SQL Dialect
  - 3. Discover Schema (If Warehouse Connected)
  - 4. Write the Query
  - 5. Present the Query
  - 6. Offer to Execute
- Examples
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:sql-queries](anthropics-knowledge-work-plugins-sql-queries.md) - Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, Postg
- [microsoft/skills:azure-kusto-graph](microsoft-skills-azure-kusto-graph.md) - Build and query Kusto graphs from natural language. Covers transient graphs (make-graph), persistent graph mod

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:write-query`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path data/skills/write-query --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 0ddd724589426802f63e224357d7360c2ff231bef7de6ce76baaff22800fa100 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
