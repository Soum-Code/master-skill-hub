# hexagonal-architecture

> Design, implement, and refactor Ports & Adapters systems with clear domain boundaries, dependency inversion, and testable use-case orchestration across TypeScript, Java, Kotlin, and Go services. Use when introducing or refactoring toward Ports and Adapters, or when domain logic has become entangled with I/O.

| | |
|---|---|
| **ID** | `affaan-m/ECC:hexagonal-architecture` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 278 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when introducing or refactoring toward Ports and Adapters, or when domain logic has become entangled with I/O.

## What it says up front

> Hexagonal architecture (Ports and Adapters) keeps business logic independent from frameworks, transport, and persistence details. The core app depends on abstract ports, and adapters implement those ports at the edges.

## How it is structured

The skill's own section headings, in order:

- When to Use
- Core Concepts
- How It Works
  - Step 1: Model a use case boundary
  - Step 2: Define outbound ports first
  - Step 3: Implement the use case with pure orchestration
  - Step 4: Build adapters at the edge
  - Step 5: Wire everything in a composition root
  - Step 6: Test per boundary
- Architecture Diagram
- Suggested Module Layout
- TypeScript Example
  - Port definitions
  - Use case
  - Outbound adapter
  - Composition root
- Multi-Language Mapping
- Anti-Patterns to Avoid
- Migration Playbook
  - Refactoring Existing Systems
- Testing Guidance (Same Hexagonal Boundaries)
- Best Practices Checklist

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:system-design](engineering-system-design.md) - Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "s
- [affaan-m/ECC:error-handling](affaan-m-ecc-error-handling.md) - Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, r
- [affaan-m/ECC:springboot-patterns](affaan-m-ecc-springboot-patterns.md) - Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, 

## Invoke / install

- Invoke: `/affaan-m/ECC:hexagonal-architecture`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/hexagonal-architecture --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 8ca74919a4b02aa02e57a289be83c961e6beffc5fd978575403174da401a51a2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
