# rust-testing

> Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking, and coverage. Follows TDD methodology. Use when writing Rust tests — unit, integration, async, property-based, or coverage.

| | |
|---|---|
| **ID** | `affaan-m/ECC:rust-testing` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 502 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when writing Rust tests — unit, integration, async, property-based, or coverage.

## What it says up front

> Comprehensive Rust testing patterns for writing reliable, maintainable tests following TDD methodology.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- TDD Workflow for Rust
  - The RED-GREEN-REFACTOR Cycle
  - Step-by-Step TDD in Rust
- Unit Tests
  - Module-Level Test Organization
  - Assertion Macros
- Error and Panic Testing
  - Testing `Result` Returns
  - Testing Panics
- Integration Tests
  - File Structure
  - Writing Integration Tests
- Async Tests
  - With Tokio
- Test Organization Patterns
  - Parameterized Tests with `rstest`
  - Test Helpers
- Property-Based Testing with `proptest`
  - Basic Property Tests
  - Custom Strategies
- Mocking with `mockall`
  - Trait-Based Mocking
- Doc Tests
  - Executable Documentation
- Benchmarking with Criterion
- Test Coverage
  - Running Coverage
  - Coverage Targets

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:kotlin-testing](affaan-m-ecc-kotlin-testing.md) - Kotlin testing patterns with Kotest, MockK, coroutine testing, property-based testing, and Kover coverage. Fol
- [affaan-m/ECC:golang-testing](affaan-m-ecc-golang-testing.md) - Go testing patterns including table-driven tests, subtests, benchmarks, fuzzing, and test coverage. Follows TD
- [affaan-m/ECC:perl-testing](affaan-m-ecc-perl-testing.md) - Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD 
- [affaan-m/ECC:python-testing](affaan-m-ecc-python-testing.md) - Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requ

## Invoke / install

- Invoke: `/affaan-m/ECC:rust-testing`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/rust-testing --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 49f228473e4853f95210d91662e51f2dac6d084edd0b3b340dde3f039b795c91 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
