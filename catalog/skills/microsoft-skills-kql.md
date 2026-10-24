# kql

> KQL language expertise for writing correct, efficient Kusto Query Language queries. Covers syntax gotchas, join patterns, dynamic types, datetime pitfalls, regex patterns, serialization, memory management, result-size discipline, and advanced functions (geo, vector, graph). USE THIS SKILL whenever writing, debugging, or reviewing KQL queries — even simple ones — because the gotchas section prevents the most common errors that waste tool calls and cause expensive retry cascades. Trigger on: KQL, Kusto, ADX, Azure Data Explorer, Fabric Real-Time Intelligence, EventHouse, Log Analytics, log analysis, data exploration, time series, anomaly detection, summarize, where clause, join, extend, project, let statement, parse operator, extract function, any mention of pipe-forward query syntax.

| | |
|---|---|
| **ID** | `microsoft/skills:kql` |
| **Pack** | Documents, Writing & Content (also: Data & Analytics) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 443 lines in SKILL.md, 5 file(s) |

## When to use it

- USE THIS SKILL whenever writing, debugging, or reviewing KQL queries — even simple ones — because the gotchas section prevents the most common errors that waste tool calls and cause expensive retry cascades.
- Trigger on: KQL, Kusto, ADX, Azure Data Explorer, Fabric Real-Time Intelligence, EventHouse, Log Analytics, log analysis, data exploration, time series, anomaly detection, summarize, where cla.

## What it says up front

> Kusto Query Language (KQL) is a pipe-forward query language for exploring data. It is the native query language for Azure Data Explorer (ADX), Microsoft Fabric Real-Time Intelligence (EventHouse), Azure Monitor Log Analytics, Microsoft Sentinel, and other Microsoft data services.

## How it is structured

The skill's own section headings, in order:

- 1. KQL Basics
  - Pipe-forward syntax
  - Query vs management commands
- 2. Dynamic Type Discipline
- 3. Join Patterns & Pitfalls
  - Equality only
  - Left/right attribute matching
  - Cardinality check before large joins
- 4. Regex in KQL
  - The `extract_all` gotcha
  - Regex toolkit — don't fall back to Python
- 5. Serialization Requirements
- 6. Memory-Safe Query Patterns
  - The progression of safety
  - Rules for large tables (>1M rows)
  - When you see `E_LOW_MEMORY_CONDITION`
  - When you see `E_RUNAWAY_QUERY`
- 7. Result Size Discipline
- 8. String Comparison Strictness
- 9. Advanced Functions
  - Vector similarity
  - Geo operations
  - Graph queries
  - Time series
- 10. Self-Correction Lookup Table
- 11. Datetime Pitfalls
  - Literal format
  - Filtering by year, month, or hour
  - Time bucketing in summarize
  - Useful datetime functions

## What it bundles

- reference docs: `references/advanced-patterns.md`, `references/discovery-queries.md`, `references/error-recovery.md`, `references/query-templates.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-kusto-irql-graph](microsoft-skills-azure-kusto-irql-graph.md) - Apply IRQL graph functions to KQL or IRQL query results for Kusto Explorer visualization. Generates Lift_To_Gr

## Invoke / install

- Invoke: `/microsoft/skills:kql`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/skills/kql --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 1b93389afd040464a7f92dd9b3bf215e3ed29ec935d54089a89f79a1c16387e3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
