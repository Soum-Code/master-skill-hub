# springboot-verification

> Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle static analysis, unit and Testcontainers integration tests with JaCoCo coverage, OWASP dependency and secret scans, and diff review — producing a pass/fail readiness report. Use when preparing a Spring Boot pull request, validating coverage thresholds, or running pre-deploy verification.

| | |
|---|---|
| **ID** | `affaan-m/ECC:springboot-verification` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 233 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when preparing a Spring Boot pull request, validating coverage thresholds, or running pre-deploy verification.

## What it says up front

> Run before PRs, after major changes, and pre-deploy.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Phase 1: Build
- Phase 2: Static Analysis
- Phase 3: Tests + Coverage
  - Unit Tests
  - Integration Tests with Testcontainers
  - API Tests with MockMvc
- Phase 4: Security Scan
  - Common Security Findings
- Phase 5: Lint/Format (optional gate)
- Phase 6: Diff Review
- Output Template
- Continuous Mode

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:django-verification](affaan-m-ecc-django-verification.md) - Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest w
- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 
- [affaan-m/ECC:laravel-verification](affaan-m-ecc-laravel-verification.md) - Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security sc
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s

## Invoke / install

- Invoke: `/affaan-m/ECC:springboot-verification`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/springboot-verification --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 954c3709d719a97d8d4962cf5f24ce54985d585e7a9c09c2cb27bc3f8a74213c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
