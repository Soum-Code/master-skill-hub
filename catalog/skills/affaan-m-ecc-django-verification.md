# django-verification

> Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest with coverage targets, pip-audit and bandit security scans, settings and logging review, and diff review — producing a phased pass/fail report before release or PR. Use when preparing a Django pull request, validating migrations or coverage, or running pre-deploy readiness checks.

| | |
|---|---|
| **ID** | `affaan-m/ECC:django-verification` |
| **Pack** | Spec-driven Dev Workflow (also: Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 471 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when preparing a Django pull request, validating migrations or coverage, or running pre-deploy readiness checks.

## What it says up front

> Run before PRs, after major changes, and pre-deploy to ensure Django application quality and security.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Phase 1: Environment Check
- Phase 2: Code Quality & Formatting
- Phase 3: Migrations
- Phase 4: Tests + Coverage
- Phase 5: Security Scan
- Phase 6: Django Management Commands
- Phase 7: Performance Checks
- Phase 8: Static Assets
- Phase 9: Configuration Review
- Phase 10: Logging Configuration
- Phase 11: API Documentation (if DRF)
- Phase 12: Diff Review
- Output Template
- Pre-Deployment Checklist
- Continuous Integration
  - GitHub Actions Example
- Quick Reference

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:springboot-verification](affaan-m-ecc-springboot-verification.md) - Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle static analy
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s
- [affaan-m/ECC:laravel-verification](affaan-m-ecc-laravel-verification.md) - Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security sc
- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 

## Invoke / install

- Invoke: `/affaan-m/ECC:django-verification`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/django-verification --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 35cefd72de21ada77d029799a89d4320c4b908edfcd927ccca0e6b0662937b92 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
