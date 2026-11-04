# latency-critical-systems

> Optimize and verify latency-sensitive systems — realtime dashboards, market data feeds, streaming agents, execution gateways, queues, and caches — by tracking p50/p95/p99 latency, freshness age, and queue depth, mapping hot paths, and running live readbacks. Use when p95 latency, throughput, or data freshness matters.

| | |
|---|---|
| **ID** | `affaan-m/ECC:latency-critical-systems` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 76 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when p95 latency, throughput, or data freshness matters.

## What it says up front

> Use this skill when the user cares about realtime behavior, hot paths, streaming freshness, or execution speed. This includes HFT-like infrastructure, but the skill is engineering-focused. It does not authorize live trading or financial advice.

## How it is structured

The skill's own section headings, in order:

- Split The Metrics
- Map The Hot Path
- Optimization Order
- Verification
- Guardrails

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:latency-critical-systems`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/latency-critical-systems --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 6489a63bf9638541973aa45b016c4b0caa0a80dcc3746671586c1d008f738d0f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
