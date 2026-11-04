# typescript-patterns

> TypeScript patterns for strict, type-safe, maintainable code in modern TypeScript and JavaScript applications. Covers strict compiler configuration, type design, narrowing, discriminated unions, generics, async and error handling, module boundaries, dependency hygiene, and type-level testing. Use when writing or reviewing TypeScript or JavaScript code.

| | |
|---|---|
| **ID** | `affaan-m/ECC:typescript-patterns` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 593 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing or reviewing TypeScript or JavaScript code.

## What it says up front

> TypeScript patterns and best practices for building robust, type-safe, and maintainable applications. The compiler is most useful when it can prove your program's shape, so the guiding principle here is: push the type system to do real work instead of fighting it. This skill is the "how." For the "w

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Core Principles
  - 1. Strict Mode Is the Baseline
  - 2. `any` Is a Bug, Not a Tool
  - 3. Public APIs Get Explicit Types, Locals Get Inference
- Type Design
  - Interfaces vs. Type Aliases
  - Discriminated Unions Are the Default State Machine
  - Brands and Nominal Safety Where Structure Is Not Enough
  - Generics Model Caller-Dependent Types
  - Options Objects over Positional Parameters
- Narrowing and Runtime Safety
  - Validate at the Boundary, Trust Inside
  - Type Predicates and Assertion Functions
  - Readonly by Default
- Error Handling
  - Fail at the Boundary, Handle at the Edge
  - Result Types for Expected Failures
  - Preserve Error Context
- Async Patterns
  - Prefer `Promise.allSettled` for Independent Fan-Out
  - Avoid Unbounded Concurrency
  - Timeouts and Cancellation
- Null and Undefined Discipline
- Module Boundaries and Exports
  - Small, Named Modules
  - Avoid Barrel Bloat and Circular Imports
  - Split by Dependency Direction
- Dependencies and Build
  - Diagnose, Then Add Dependencies

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:rust-patterns](affaan-m-ecc-rust-patterns.md) - Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe,
- [affaan-m/ECC:error-handling](affaan-m-ecc-error-handling.md) - Patterns for robust error handling across TypeScript, Python, and Go. Covers typed errors, error boundaries, r
- [affaan-m/ECC:perl-patterns](affaan-m-ecc-perl-patterns.md) - Modern Perl 5.36+ idioms, best practices, and conventions for building robust, maintainable Perl applications.
- [affaan-m/ECC:dart-flutter-patterns](affaan-m-ecc-dart-flutter-patterns.md) - Production-ready Dart and Flutter patterns covering null safety, immutable state with Freezed, async compositi

## Invoke / install

- Invoke: `/affaan-m/ECC:typescript-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/typescript-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f6df53d599194d180a664b5fdc82956c4a3f338913c335abb93fddca8655703a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
