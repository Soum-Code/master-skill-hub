# kotlin-coroutines-flows

> Kotlin Coroutines and Flow patterns for Android and KMP — structured concurrency, Flow operators, StateFlow, error handling, and testing. Use when writing coroutines or Flow code on Android or KMP, or debugging cancellation and concurrency.

| | |
|---|---|
| **ID** | `affaan-m/ECC:kotlin-coroutines-flows` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 286 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing coroutines or Flow code on Android or KMP, or debugging cancellation and concurrency.

## What it says up front

> Patterns for structured concurrency, Flow-based reactive streams, and coroutine testing in Android and Kotlin Multiplatform projects.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Structured Concurrency
  - Scope Hierarchy
  - Parallel Decomposition
  - SupervisorScope
- Flow Patterns
  - Cold Flow — One-Shot to Stream Conversion
  - StateFlow for UI State
  - Combining Multiple Flows
  - Flow Operators
  - SharedFlow for One-Time Events
- Dispatchers
- Cancellation
  - Cooperative Cancellation
  - Cleanup with try/finally
- Testing
  - Testing StateFlow with Turbine
  - Testing with TestDispatcher
  - Faking Flows
- Anti-Patterns to Avoid
- References

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:android-clean-architecture](affaan-m-ecc-android-clean-architecture.md) - Clean Architecture patterns for Android and Kotlin Multiplatform projects — module structure, dependency rules
- [affaan-m/ECC:rust-patterns](affaan-m-ecc-rust-patterns.md) - Idiomatic Rust patterns, ownership, error handling, traits, concurrency, and best practices for building safe,
- [affaan-m/ECC:kotlin-testing](affaan-m-ecc-kotlin-testing.md) - Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Fol
- [affaan-m/ECC:kotlin-patterns](affaan-m-ecc-kotlin-patterns.md) - Idiomatic Kotlin patterns, best practices, and conventions for building robust, efficient, and maintainable Ko

## Invoke / install

- Invoke: `/affaan-m/ECC:kotlin-coroutines-flows`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/kotlin-coroutines-flows --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b57d303812888258e803679411c59a88049b76504d6e06c02610f4b79083b490 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
