# dashboard-builder

> Build monitoring dashboards that answer real operator questions for Grafana, SigNoz, and similar platforms. Use when turning metrics into a working dashboard instead of a vanity board.

| | |
|---|---|
| **ID** | `affaan-m/ECC:dashboard-builder` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 110 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when turning metrics into a working dashboard instead of a vanity board.

## What it says up front

> Use this when the task is to build a dashboard people can operate from.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Guardrails
- Workflow
  - 1. Define the operating questions
  - 2. Study the target platform schema
  - 3. Build the minimum useful board
  - 4. Cut vanity panels
- Example Panel Sets
  - Elasticsearch
  - Kafka
  - API gateway / ingress
- Quality Checklist
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropics/knowledge-work-plugins:build-dashboard](anthropics-knowledge-work-plugins-build-dashboard.md) - Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview 

## Invoke / install

- Invoke: `/affaan-m/ECC:dashboard-builder`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/dashboard-builder --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 145ea2bb1f2e06907552d618cc9a67adb968ea6dec00dcdcacbb335f6c56f88a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
