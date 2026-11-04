# content-hash-cache-pattern

> Cache expensive file processing results using SHA-256 content hashes — path-independent, auto-invalidating, with service layer separation. Use when repeated file processing is slow and results should be cached and invalidated by content rather than path.

| | |
|---|---|
| **ID** | `affaan-m/ECC:content-hash-cache-pattern` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 163 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when repeated file processing is slow and results should be cached and invalidated by content rather than path.

## What it says up front

> Cache expensive file processing results (PDF parsing, text extraction, image analysis) using SHA-256 content hashes as cache keys. Unlike path-based caching, this approach survives file moves/renames and auto-invalidates when content changes.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Pattern
  - 1. Content-Hash Based Cache Key
  - 2. Frozen Dataclass for Cache Entry
  - 3. File-Based Cache Storage
  - 4. Service Layer Wrapper (SRP)
- Key Design Decisions
- Best Practices
- Anti-Patterns to Avoid
- When to Use
- When NOT to Use

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:springboot-patterns](affaan-m-ecc-springboot-patterns.md) - Spring Boot architecture patterns, REST API design, layered services, data access, caching, async processing, 
- [affaan-m/ECC:laravel-patterns](affaan-m-ecc-laravel-patterns.md) - Laravel architecture patterns, routing/controllers, Eloquent ORM, service layers, queues, events, caching, and

## Invoke / install

- Invoke: `/affaan-m/ECC:content-hash-cache-pattern`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/content-hash-cache-pattern --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree ab52fea3f69086dd4e340938f5e45d40555bf071b0b48ec6d896ab8e946cdc39 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
