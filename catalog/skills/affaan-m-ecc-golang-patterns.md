# golang-patterns

> Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go applications. Use when writing or reviewing Go code and idiomatic structure or conventions are in question.

| | |
|---|---|
| **ID** | `affaan-m/ECC:golang-patterns` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 682 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or reviewing Go code and idiomatic structure or conventions are in question.

## What it says up front

> Idiomatic Go patterns and best practices for building robust, efficient, and maintainable applications.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Principles
  - 1. Simplicity and Clarity
  - 2. Make the Zero Value Useful
  - 3. Accept Interfaces, Return Structs
- Error Handling Patterns
  - Error Wrapping with Context
  - Custom Error Types
  - Error Checking with errors.Is and errors.As
  - Never Ignore Errors
- Concurrency Patterns
  - Worker Pool
  - Context for Cancellation and Timeouts
  - Graceful Shutdown
  - errgroup for Coordinated Goroutines
  - Avoiding Goroutine Leaks
- Interface Design
  - Small, Focused Interfaces
  - Define Interfaces Where They're Used
  - Optional Behavior with Type Assertions
- Package Organization
  - Standard Project Layout
  - Package Naming
  - Avoid Package-Level State
- Struct Design
  - Functional Options Pattern
  - Embedding for Composition
- Memory and Performance
  - Preallocate Slices When Size is Known
  - Use sync.Pool for Frequent Allocations

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:kotlin-patterns](affaan-m-ecc-kotlin-patterns.md) - Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Ko
- [affaan-m/ECC:python-patterns](affaan-m-ecc-python-patterns.md) - Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintaina
- [affaan-m/ECC:perl-patterns](affaan-m-ecc-perl-patterns.md) - Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
- [affaan-m/ECC:dotnet-patterns](affaan-m-ecc-dotnet-patterns.md) - Idiomatic C# and .NET patterns, conventions, dependency injection, async/await, and best practices for buildin

## Invoke / install

- Invoke: `/affaan-m/ECC:golang-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/golang-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 3d533e573dada0153dc1d7086cee7570daabda274ba54dbe2d2248f4ebb742d6 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
