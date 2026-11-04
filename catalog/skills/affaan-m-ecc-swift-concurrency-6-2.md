# swift-concurrency-6-2

> Swift 6.2 Approachable Concurrency — single-threaded by default, @concurrent for explicit background offloading, isolated conformances for main actor types. Use when adopting Swift 6.2 concurrency — offloading with @concurrent or resolving main-actor isolation.

| | |
|---|---|
| **ID** | `affaan-m/ECC:swift-concurrency-6-2` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 217 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when adopting Swift 6.2 concurrency — offloading with @concurrent or resolving main-actor isolation.

## What it says up front

> Patterns for adopting Swift 6.2's concurrency model where code runs single-threaded by default and concurrency is introduced explicitly. Eliminates common data-race errors without sacrificing performance.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Problem: Implicit Background Offloading
- Core Pattern — Isolated Conformances
- Core Pattern — Global and Static Variables
  - MainActor Default Inference Mode
- Core Pattern — @concurrent for Background Work
- Key Design Decisions
- Migration Steps
- Best Practices
- Anti-Patterns to Avoid
- When to Use

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:swift-concurrency-6-2`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/swift-concurrency-6-2 --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 019c3f01edd7e363b591329fd1f61b1d112f254b747f32263561673e951d6bcf --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
