# azure-kusto-irql-graph

> Apply IRQL graph functions to KQL or IRQL query results for Kusto Explorer visualization. Generates Lift_To_Graph mappings and composes Graph_Render_View, Graph_Fold_By_Property, Extract_Node_*, Enrich_Node_*, and Enrich_Graph_* calls. Accepts a supplied query or limited basic natural-language source request; it is not a general natural-language-to-KQL/IRQL skill. WHEN: Lift_To_Graph, Graph_Render_View, Graph_Fold_By_Property, IRQL graph enrichment, graph mapping for existing query results, icon-decorated graph, fold graph nodes. Use azure-kusto-graph for native make-graph analysis, graph-match, shortest paths, components, or persistent graphs.

| | |
|---|---|
| **ID** | `microsoft/skills:azure-kusto-irql-graph` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 301 lines in SKILL.md, 4 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Apply the IRQL graph function family to tabular results. Given a KQL or IRQL query and the user's graph description, generate a `Lift_To_Graph` mapping and compose only the stored graph functions needed to visualize, fold, extract, or enrich the graph in Kusto Explorer. The source query does not nee

## How it is structured

The skill's own section headings, in order:

- Scope and Routing
- Input Contract
- Activation Triggers
- Environment
  - Function Preflight
- IRQL Graph Function Family
  - `Lift_To_Graph(T, mappingJson)`
  - `Graph_Render_View(T)`
  - `Graph_Fold_By_Property(T, NodeType, PropertyName)`
  - Graph Extraction and Enrichment Functions
- Mapping JSON Schema
  - `node_types[]`
  - `edges[]`
  - Icon Repository
- Mapping Generation Rules
  - Column Reference (IRQL unified schema)
- Function Selection
- Pipeline Pattern
- Examples
  - Authentication graph: IP -> AuthEvent -> User -> Host
  - Email graph: Sender -> Message -> Recipient
  - Suspicious domain investigation (end-to-end)
  - Process execution graph: User -> Process -> ParentProcess
- Query Results -> Mapping Translation
- Opening Queries in Kusto Explorer (Windows Only)

## What it bundles

- reference docs: `references/DEPLOY_IRQL_FUNCTIONS.md`, `references/EXAMPLES.md`, `references/KUSTO_EXPLORER_LAUNCH.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-kusto-graph](microsoft-skills-azure-kusto-graph.md) - Build and query Kusto graphs from natural language. Covers transient graphs (make-graph), persistent graph mod
- [microsoft/skills:azure-kusto-irql](microsoft-skills-azure-kusto-irql.md) - Compose IRQL (Incident Response Query Language) queries for Kusto cybersecurity investigations. Translates nat
- [microsoft/skills:kql](microsoft-skills-kql.md) - KQL language expertise for writing correct, efficient Kusto Query Language queries. Covers syntax gotchas, joi

## Invoke / install

- Invoke: `/microsoft/skills:azure-kusto-irql-graph`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-kusto-graph-skills/skills/azure-kusto-irql-graph --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree 13231492aa34644a15c7e5e4c96235b476c99078179df26da23992c59b9222bf --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
