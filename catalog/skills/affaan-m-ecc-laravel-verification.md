# laravel-verification

> Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security scans, and deployment readiness. Use when verifying a Laravel project before merge or deploy — lint, static analysis, tests, coverage, security.

| | |
|---|---|
| **ID** | `affaan-m/ECC:laravel-verification` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 181 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when verifying a Laravel project before merge or deploy — lint, static analysis, tests, coverage, security.

## What it says up front

> Run before PRs, after major changes, and pre-deploy.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
- Phase 1: Environment Checks
- Phase 1.5: Composer and Autoload
- Phase 2: Linting and Static Analysis
- Phase 3: Tests and Coverage
- Phase 4: Security and Dependency Checks
- Phase 5: Database and Migrations
- Phase 6: Build and Deployment Readiness
- Phase 7: Queue and Scheduler Checks
- Examples

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s
- [affaan-m/ECC:django-verification](affaan-m-ecc-django-verification.md) - Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest w
- [affaan-m/ECC:springboot-verification](affaan-m-ecc-springboot-verification.md) - Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle static analy

## Invoke / install

- Invoke: `/affaan-m/ECC:laravel-verification`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/laravel-verification --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 00c48e2a1c0432aa6b0c76089a34ec15c12e519b033a3d45bd7c0046ac9735b2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
