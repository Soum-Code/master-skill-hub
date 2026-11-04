# quarkus-verification

> Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo coverage, OWASP dependency and container security scans, GraalVM native compilation, health checks, and config validation. Use when verifying a Quarkus service before a PR, after major refactoring or dependency upgrades, or pre-deploy.

| | |
|---|---|
| **ID** | `affaan-m/ECC:quarkus-verification` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 482 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when verifying a Quarkus service before a PR, after major refactoring or dependency upgrades, or pre-deploy.

## What it says up front

> Run before PRs, after major changes, and pre-deploy.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Phase 1: Build
- Phase 2: Static Analysis
  - Checkstyle, PMD, SpotBugs (Maven)
  - SonarQube (if configured)
  - Common Issues to Address
- Phase 3: Tests + Coverage
  - Test Categories
  - Coverage Report
- Phase 4: Security Scanning
  - Dependency Vulnerabilities (Maven)
  - Quarkus Security Audit
  - OWASP ZAP (API Security Testing)
  - Common Security Checks
- Phase 5: Native Compilation
  - Native Image Troubleshooting
- Phase 6: Performance Testing
  - Load Testing with K6
  - Metrics to Monitor
- Phase 7: Health Checks
- Phase 8: Container Image Build
  - Container Security Scan
- Phase 9: Configuration Validation
  - Environment-Specific Checks
- Phase 10: Documentation Review
- Verification Checklist
  - Code Quality
  - Testing
  - Security
  - Deployment

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:laravel-verification](affaan-m-ecc-laravel-verification.md) - Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security sc
- [affaan-m/ECC:springboot-verification](affaan-m-ecc-springboot-verification.md) - Run the full Spring Boot verification loop — Maven or Gradle build, SpotBugs, PMD, and Checkstyle static analy
- [affaan-m/ECC:verification-loop](affaan-m-ecc-verification-loop.md) - Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s
- [affaan-m/ECC:django-verification](affaan-m-ecc-django-verification.md) - Run the full Django verification loop — environment check, mypy/ruff/black linting, migration safety, pytest w

## Invoke / install

- Invoke: `/affaan-m/ECC:quarkus-verification`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/quarkus-verification --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree f14d9cedafff7e93cbbd71ca42e3985f46c60fb82ad457311e7a01aac35a66ea --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
