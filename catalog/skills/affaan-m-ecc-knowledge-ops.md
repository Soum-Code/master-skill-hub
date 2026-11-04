# knowledge-ops

> Knowledge base management, ingestion, sync, and retrieval across multiple storage layers (local files, MCP memory, vector stores, Git repos). Use when the user wants to save, organize, sync, deduplicate, or search across their knowledge systems.

| | |
|---|---|
| **ID** | `affaan-m/ECC:knowledge-ops` |
| **Pack** | AI / ML Engineering (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 156 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants to save, organize, sync, deduplicate, or search across their knowledge systems.

## What it says up front

> Manage a multi-layered knowledge system for ingesting, organizing, syncing, and retrieving knowledge across multiple stores.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Knowledge Architecture
  - Layer 1: Active execution truth
  - Layer 2: Claude Code Memory (Quick Access)
  - Layer 3: MCP Memory Server (Structured Knowledge Graph)
  - Layer 4: Knowledge base repo / durable document store
  - Layer 5: External Data Store (Supabase, PostgreSQL, etc.)
  - Layer 6: Local context/archive folder
- Ingestion Workflow
  - 1. Classify
  - 2. Deduplicate
  - 3. Store
  - 4. Index
- Sync Operations
  - Conversation Sync
  - Workspace State Sync
  - GitHub / Linear Sync
  - Cross-Source Knowledge Sync
- Memory Patterns
- Best Practices
- Quality Gate

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [modelcontextprotocol/specification:search-mcp-github](modelcontextprotocol-specification-search-mcp-github.md) - Search MCP PRs, issues, and discussions across the modelcontextprotocol GitHub org
- [productivity:memory-management](productivity-memory-management.md) - Two-tier memory system that makes Claude a true workplace collaborator. Decodes shorthand, acronyms, nicknames
- [productivity:task-management](productivity-task-management.md) - Simple task management using a shared TASKS.md file. Reference this when the user asks about their tasks, want
- [affaan-m/ECC:project-flow-ops](affaan-m-ecc-project-flow-ops.md) - Operate execution flow across GitHub and Linear by triaging issues and pull requests, linking active work, and

## Invoke / install

- Invoke: `/affaan-m/ECC:knowledge-ops`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/knowledge-ops --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree a5ae284acab8693aa15e57943cb5e254e82be567d4e6719ccff039953cfaa5aa --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
