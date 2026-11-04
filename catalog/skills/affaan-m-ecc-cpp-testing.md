# cpp-testing

> Use only when writing/updating/fixing C++ tests, configuring GoogleTest/CTest, diagnosing failing or flaky tests, or adding coverage/sanitizers.

| | |
|---|---|
| **ID** | `affaan-m/ECC:cpp-testing` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 326 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Agent-focused testing workflow for modern C++ (C++17/20) using GoogleTest/GoogleMock with CMake/CTest.

## How it is structured

The skill's own section headings, in order:

- When to Use
  - When NOT to Use
- Core Concepts
- TDD Workflow
- Code Examples
  - Basic Unit Test (gtest)
  - Fixture (gtest)
  - Mock (gmock)
  - CMake/CTest Quickstart
- Running Tests
- Debugging Failures
- Coverage
- Sanitizers
- Flaky Tests Guardrails
- Best Practices
  - DO
  - DON'T
  - Common Pitfalls
- Optional Appendix: Fuzzing / Property Testing
- Alternatives to GoogleTest

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:python-testing](affaan-m-ecc-python-testing.md) - Python testing strategies using pytest, TDD methodology, fixtures, mocking, parametrization, and coverage requ
- [affaan-m/ECC:e2e-testing](affaan-m-ecc-e2e-testing.md) - Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and
- [affaan-m/ECC:rust-testing](affaan-m-ecc-rust-testing.md) - Rust testing patterns including unit tests, integration tests, async testing, property-based testing, mocking,
- [affaan-m/ECC:perl-testing](affaan-m-ecc-perl-testing.md) - Perl testing patterns using Test2::V0, Test::More, prove runner, mocking, coverage with Devel::Cover, and TDD 

## Invoke / install

- Invoke: `/affaan-m/ECC:cpp-testing`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/cpp-testing --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f61b3f6d99c71c36f9c94977171427ff8bfba7e92bdc6f4ac31772c483fb67f3 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
