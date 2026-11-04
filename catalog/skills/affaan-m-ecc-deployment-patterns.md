# deployment-patterns

> Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, and production readiness checklists for web applications. Use when setting up CI/CD, containerizing an app, or checking production readiness before a release.

| | |
|---|---|
| **ID** | `affaan-m/ECC:deployment-patterns` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 429 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when setting up CI/CD, containerizing an app, or checking production readiness before a release.

## What it says up front

> Production deployment workflows and CI/CD best practices.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Deployment Strategies
  - Rolling Deployment (Default)
  - Blue-Green Deployment
  - Canary Deployment
- Docker
  - Multi-Stage Dockerfile (Node.js)
  - Multi-Stage Dockerfile (Go)
  - Multi-Stage Dockerfile (Python/Django)
  - Docker Best Practices
- CI/CD Pipeline
  - GitHub Actions (Standard Pipeline)
  - Pipeline Stages
- Health Checks
  - Health Check Endpoint
  - Kubernetes Probes
- Environment Configuration
  - Twelve-Factor App Pattern
  - Configuration Validation
- Rollback Strategy
  - Instant Rollback
  - Rollback Checklist
- Production Readiness Checklist
  - Application
  - Infrastructure
  - Monitoring
  - Security
  - Operations

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [engineering:deploy-checklist](engineering-deploy-checklist.md) - Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migr
- [affaan-m/ECC:production-audit](affaan-m-ecc-production-audit.md) - Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what b
- [affaan-m/ECC:e2e-testing](affaan-m-ecc-e2e-testing.md) - Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and
- [affaan-m/ECC:laravel-verification](affaan-m-ecc-laravel-verification.md) - Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security sc

## Invoke / install

- Invoke: `/affaan-m/ECC:deployment-patterns`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/deployment-patterns --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree fa4622db60fdb98a22e7514e432a4b623fbc0b7d45db4ae39ab35ffa8e73d2cc --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
