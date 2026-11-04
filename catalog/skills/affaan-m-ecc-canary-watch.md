# canary-watch

> Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, static assets, console errors, and performance regressions after deploys, merges, or dependency upgrades. Smoke / canary / post-deploy verification.

| | |
|---|---|
| **ID** | `affaan-m/ECC:canary-watch` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 109 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill to monitor and verify a deployed URL after releases — checks HTTP endpoints, SSE streams, static assets, console errors, and performance regressions after deploys, merges, or dependency upgrades.

## What it says up front

> Monitors a deployed URL for regressions. Runs in a loop until stopped or until the watch window expires.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - What It Watches
  - Watch Modes
  - Alert Thresholds
  - Notifications
- Output
- Integration

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:laravel-verification](affaan-m-ecc-laravel-verification.md) - Verification loop for Laravel projects: env checks, linting, static analysis, tests with coverage, security sc
- [affaan-m/ECC:quarkus-verification](affaan-m-ecc-quarkus-verification.md) - Verification loop for Quarkus projects: build, static analysis (Checkstyle, PMD, SpotBugs), tests with JaCoCo 
- [affaan-m/ECC:browser-qa](affaan-m-ecc-browser-qa.md) - Run automated post-deploy UI verification with a browser automation MCP (claude-in-chrome, Playwright, or Pupp
- [engineering:code-review](engineering-code-review.md) - Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this be

## Invoke / install

- Invoke: `/affaan-m/ECC:canary-watch`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/canary-watch --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 6e82a38db99c7e99e1a81541d9e48766c4cd1a324491186e1a5e346654b09266 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
