# rust-patterns

> Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe, performant applications. Use when writing or reviewing Rust code and ownership, error handling, traits, or concurrency is in question.

| | |
|---|---|
| **ID** | `affaan-m/ECC:rust-patterns` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 501 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or reviewing Rust code and ownership, error handling, traits, or concurrency is in question.

## What it says up front

> Idiomatic Rust patterns and best practices for building safe, performant, and maintainable applications.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Core Principles
  - 1. Ownership and Borrowing
  - Use `Cow` for Flexible Ownership
- Error Handling
  - Use `Result` and `?` — Never `unwrap()` in Production
  - Library Errors with `thiserror`, Application Errors with `anyhow`
  - `Option` Combinators Over Nested Matching
- Enums and Pattern Matching
  - Model States as Enums
  - Exhaustive Matching — No Catch-All for Business Logic
- Traits and Generics
  - Accept Generics, Return Concrete Types
  - Trait Objects for Dynamic Dispatch
  - Newtype Pattern for Type Safety
- Structs and Data Modeling
  - Builder Pattern for Complex Construction
- Iterators and Closures
  - Prefer Iterator Chains Over Manual Loops
  - Use `collect()` with Type Annotation
- Concurrency
  - `Arc>` for Shared Mutable State
  - Channels for Message Passing
  - Async with Tokio
- Unsafe Code
  - When Unsafe Is Acceptable
  - When Unsafe Is NOT Acceptable
- Module System and Crate Structure
  - Organize by Domain, Not by Type

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:golang-patterns](affaan-m-ecc-golang-patterns.md) - Idiomatic Go patterns, best practices, and conventions for building robust, efficient, and maintainable Go app
- [affaan-m/ECC:kotlin-patterns](affaan-m-ecc-kotlin-patterns.md) - Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Ko
- [affaan-m/ECC:python-patterns](affaan-m-ecc-python-patterns.md) - Pythonic idioms, PEP 8 standards, type hints, and best practices for building robust, efficient, and maintaina
- [affaan-m/ECC:perl-patterns](affaan-m-ecc-perl-patterns.md) - Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.

## Invoke / install

- Invoke: `/affaan-m/ECC:rust-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/rust-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 080419acbabb4d364128c5283f449c1392d5933826fab7fe605a8a7633077830 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
