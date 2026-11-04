# swift-actor-persistence

> Thread-safe data persistence in Swift using actors — in-memory cache with file-backed storage, eliminating data races by design. Use when persisting data in Swift and a data race or thread-safety problem needs designing out.

| | |
|---|---|
| **ID** | `affaan-m/ECC:swift-actor-persistence` |
| **Pack** | Data & Analytics (also: Spec-driven Dev Workflow, Productivity & Automation) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 145 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when persisting data in Swift and a data race or thread-safety problem needs designing out.

## What it says up front

> Patterns for building thread-safe data persistence layers using Swift actors. Combines in-memory caching with file-backed storage, leveraging the actor model to eliminate data races at compile time.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Pattern
  - Actor-Based Repository
  - Usage
  - Combining with @Observable ViewModel
- Key Design Decisions
- Best Practices
- Anti-Patterns to Avoid
- When to Use

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:system-design](engineering-system-design.md) - Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "s

## Invoke / install

- Invoke: `/affaan-m/ECC:swift-actor-persistence`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/swift-actor-persistence --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 27896ed5f31e21e50c37d2d86d185dafd95d84a0a49b9907105c8da7609e6e81 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
