# benchmark-optimization-loop

> Convert 'make it faster' requests into a bounded measured optimization loop — baseline first, generate one-hypothesis variants, benchmark each against a correctness gate, and promote the fastest safe variant with reproducible commands. Use when asked to speed something up, try many variants, run recursive optimization, benchmark latency/throughput/cost, or pick the best implementation by repeated measured tests.

| | |
|---|---|
| **ID** | `affaan-m/ECC:benchmark-optimization-loop` |
| **Pack** | Operations & Business (also: AI / ML Engineering, Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 72 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when asked to speed something up, try many variants, run recursive optimization, benchmark latency/throughput/cost, or pick the best implementation by repeated measured tests.

## What it says up front

> Use this skill to convert "make it 20x faster" or "try 50 recursive optimizations" into a bounded measured loop that can actually improve a system.

## How it is structured

The skill's own section headings, in order:

- Required Baseline
- Loop
- Variant Table
- Recursive Search
- Promotion Gate

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:benchmark-optimization-loop`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/benchmark-optimization-loop --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 641e0e247f49a0de28d73cf4b56a2faab11f89aa900b3b7dc95503c72be2b882 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
