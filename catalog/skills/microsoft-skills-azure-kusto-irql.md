# azure-kusto-irql

> Compose IRQL (Incident Response Query Language) queries for Kusto cybersecurity investigations. Translates natural language hunting questions into composable IRQL pipelines using Get_*, Extract_*, and Enrich_* functions. WHEN: IRQL query, security hunt, threat hunting KQL, incident response query, compose hunting pipeline, failed logins, phishing investigation, lateral movement, process execution, file creation events.

| | |
|---|---|
| **ID** | `microsoft/skills:azure-kusto-irql` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [microsoft/skills](https://github.com/microsoft/skills) |
| **License** | MIT |
| **Size** | 241 lines in SKILL.md, 3 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Compose IRQL function pipelines from selector, extractor, and enricher building blocks. IRQL wraps raw KQL security tables behind intent-revealing, composable functions so analysts (and LLMs) can express hunts without memorizing schemas, cluster locations, or join keys.

## How it is structured

The skill's own section headings, in order:

- Activation Triggers
- IRQL Function Preflight
- What IRQL Is
- Deploying IRQL
- Function Catalog
  - 1. Selectors -- `Get_*`
  - 2. Extractors -- `Extract_*`
  - 3. Enrichers -- `Enrich_*`
  - 4. External Enrichment
- Composition Rules
- Query Generation Guidelines
- Examples
  - Brute-force detection
  - Phishing triage by recipient seniority
  - Post-exploitation pivot from an indicator
  - Suspicious outbound traffic enriched with identity
  - External IP authentication anomaly
- MCP Tools Used
- Opening Queries in Kusto Explorer (Windows Only)

## What it bundles

- reference docs: `references/EXAMPLES.md`, `references/KUSTO_EXPLORER_LAUNCH.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [microsoft/skills:azure-kusto-irql-graph](microsoft-skills-azure-kusto-irql-graph.md) - Apply IRQL graph functions to KQL or IRQL query results for Kusto Explorer visualization. Generates Lift_To_Gr
- [microsoft/skills:azure-kusto-graph](microsoft-skills-azure-kusto-graph.md) - Build and query Kusto graphs from natural language. Covers transient graphs (make-graph), persistent graph mod

## Invoke / install

- Invoke: `/microsoft/skills:azure-kusto-irql`
- Install: `python skills/skill-vetter/scripts/install.py microsoft/skills --path .github/plugins/azure-kusto-graph-skills/skills/azure-kusto-irql --commit 2130750147dee0311215099ddf36647ba1e0f006 --expect-tree d612576c7a4b37cf230958ba94ed6e2e9ec41844ae444d0c88c214c34324cee8 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
