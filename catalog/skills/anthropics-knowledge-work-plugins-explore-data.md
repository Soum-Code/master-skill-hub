# explore-data

> Profile and explore a dataset to understand its shape, quality, and patterns. Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:explore-data` |
| **Pack** | Data & Analytics (also: Research & Learning) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 326 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when encountering a new table or file, checking null rates and column distributions, spotting data quality issues like duplicates or suspicious values, or deciding which dimensions and metrics to analyze.

## What it says up front

> Generate a comprehensive data profile for a table or uploaded file. Understand its shape, quality, and patterns before diving into analysis.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Access the Data
  - 2. Understand Structure
  - 3. Generate Data Profile
  - 4. Identify Data Quality Issues
  - 5. Discover Relationships and Patterns
  - 6. Suggest Interesting Dimensions and Metrics
  - 7. Recommend Follow-Up Analyses
- Output Format
- Quality Assessment Framework
  - Completeness Score
  - Consistency Checks
  - Accuracy Indicators
  - Timeliness Assessment
- Pattern Discovery Techniques
  - Distribution Analysis
  - Temporal Patterns
  - Segmentation Discovery
  - Correlation Exploration
- Schema Understanding and Documentation
  - Schema Documentation Template
  - Schema Exploration Queries
  - Lineage and Dependencies
- Tips

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:explore-data`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path data/skills/explore-data --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 9649b241a0b2341307ea4268631f874005299390a00d864e88dfce298ad6d48d --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
