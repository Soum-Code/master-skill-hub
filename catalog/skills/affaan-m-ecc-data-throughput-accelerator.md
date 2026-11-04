# data-throughput-accelerator

> Diagnose and accelerate large data movement — ingestion, backfill, export, ETL, warehouse loading, manifest catch-up, and table synchronization — by isolating the true bottleneck, benchmarking variants, and codifying the fastest path with a hard accounting block proving rows and timestamps cohere. Use when a pipeline or backfill is too slow and must get faster without losing data correctness.

| | |
|---|---|
| **ID** | `affaan-m/ECC:data-throughput-accelerator` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 75 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a pipeline or backfill is too slow and must get faster without losing data correctness.

## What it says up front

> Use this skill when the bottleneck is moving, transforming, or saving lots of data. The goal is not just speed. The goal is faster correct data landing in the right place with proof.

## How it is structured

The skill's own section headings, in order:

- First Distinction
- Fast Path Heuristics
- Workflow
- Accounting Output
- Guardrails

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:data-throughput-accelerator`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/data-throughput-accelerator --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree c4e0f6c44ee7dfd642720e61dc59b1bb7d43712d6da2351dac884aab6ce268ed --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
