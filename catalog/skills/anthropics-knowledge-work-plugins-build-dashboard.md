# build-dashboard

> Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:build-dashboard` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 925 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.

## What it says up front

> Build a self-contained interactive HTML dashboard with charts, filters, tables, and professional styling. Opens directly in a browser -- no server or dependencies required.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Understand the Dashboard Requirements
  - 2. Gather the Data
  - 3. Design the Dashboard Layout
  - 4. Build the HTML Dashboard
  - 5. Implement Chart Types
  - 6. Add Interactivity
  - 7. Save and Open
- Base Template
- KPI Card Pattern
- Chart.js Integration
  - Chart Container Pattern
  - Line Chart
  - Bar Chart
  - Doughnut Chart
  - Updating Charts on Filter Change
- Filter and Interactivity Implementation
  - Dropdown Filter
  - Date Range Filter
  - Combined Filter Logic
  - Sortable Table
- CSS Styling for Dashboards
  - Color System
  - Layout
  - KPI Cards
  - Chart Containers
  - Filters
  - Data Table
  - Responsive Design

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:create-viz](anthropics-knowledge-work-plugins-create-viz.md) - Create publication-quality visualizations with Python. Use when turning query results or a DataFrame into a ch
- [anthropics/claude-plugins-official:playground](anthropics-claude-plugins-official-playground.md) - Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:build-dashboard`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path data/skills/build-dashboard --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree fd4aaecbe9d07d89f1f91530a11e23c3a00afe921eff2b5a3a1702d0e0135487 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
