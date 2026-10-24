# azure-kusto-graph

> Build and query Kusto graphs from natural language. Covers transient graphs (make-graph), persistent graph models/snapshots, pattern matching (graph-match), shortest paths, connected components, and graph-to-table export. Generates the edges-first thinking: define edges, define node lookups, union, make-graph. WHEN: make-graph, graph-match, graph-shortest-paths, graph-to-table, graph-mark-components, persistent graph, graph model, graph snapshot, build a graph from data, find paths between nodes, pattern matching in graph, connected components, transient graph, Kusto graph, KQL graph.

| | |
|---|---|
| **ID** | `microsoft/skills:azure-kusto-graph` |
| **Pack** | MLOps / DevOps / Cloud (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 471 lines in SKILL.md, 4 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Build transient and persistent graphs from tabular data using KQL graph operators. This skill translates natural language into the edges-first graph construction pattern and graph query operators.

## How it is structured

The skill's own section headings, in order:

- Activation Triggers
- The Edges-First Approach
- Graph Operators Reference
  - `make-graph` -- Build a graph from tables
  - `graph-match` -- Find patterns
  - `graph-shortest-paths` -- Find shortest paths
  - `graph-to-table` -- Export graph to tables
  - `graph-mark-components` -- Find connected components
  - `graph()` function -- Query persistent graphs
- Transient Graphs
  - Template: Basic two-entity graph
  - Template: Multi-relationship graph
- Persistent Graphs
  - Step 1: Create a graph model
  - Step 2: Create a snapshot
  - Step 3: Query the snapshot
  - Management commands
- Transient vs Persistent: When to Use Which
- Security & Threat Hunting Examples
  - Authentication graph: who logged into what from where
  - Lateral movement detection: users sharing compromised hosts
  - Shortest attack path
  - Connected components: find isolated clusters
  - Visualize in Kusto Explorer
- Using with IRQL
  - Example: IRQL selectors -> make-graph -> shortest path
  - Example: IRQL selectors -> make-graph -> connected components
  - Example: IRQL + make-graph integration
- Practical Usage Scenarios
- MCP Tools Used

## What it bundles

- reference docs: `references/EXAMPLES.md`, `references/KUSTO_EXPLORER_LAUNCH.md`, `references/SCENARIOS.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-kusto-irql-graph](microsoft-skills-azure-kusto-irql-graph.md) - Apply IRQL graph functions to KQL or IRQL query results for Kusto Explorer visualization. Generates Lift_To_Gr
- [microsoft/skills:azure-kusto-irql](microsoft-skills-azure-kusto-irql.md) - Compose IRQL (Incident Response Query Language) queries for Kusto cybersecurity investigations. Translates nat
- [anthropics/knowledge-work-plugins:write-query](anthropics-knowledge-work-plugins-write-query.md) - Write optimized SQL for your dialect with best practices. Use when translating a natural-language data need in

## Invoke / install

- Invoke: `/microsoft/skills:azure-kusto-graph`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-kusto-graph-skills/skills/azure-kusto-graph --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree c383adaecc4e28172a671e0eca89b96657a5fa49a78e98e4243a4536382bd597 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
