# production-audit

> Local-evidence production readiness audit for shipped apps, pre-launch reviews, post-merge checks, and "what breaks in prod?" questions without sending repo data to an external audit service. Use when auditing production readiness before launch, after a merge, or when asked what breaks in prod.

| | |
|---|---|
| **ID** | `affaan-m/ECC:production-audit` |
| **Pack** | Finance & Accounting (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 208 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when auditing production readiness before launch, after a merge, or when asked what breaks in prod.

## What it says up front

> Use this skill when the user asks whether an application is ready to ship, what could break in production, or what must be fixed before a launch. This is a maintainer-safe rewrite of the stale community production-audit idea: it keeps the useful production-readiness lens and removes unpinned externa

## How it is structured

The skill's own section headings, in order:

- When to Use
- When Not to Use
- How It Works
- Evidence Checklist
- Risk Lenses
  - Security And Auth
  - Data Integrity
  - Payments And Webhooks
  - Operations
  - User Experience
- Scoring
- Output Format
- Example
- Anti-Patterns
- See Also

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [bm:ship](bm-ship.md) - Create PR, run review, and prepare for merge after verification passes
- [affaan-m/ECC:change-impact](affaan-m-ecc-change-impact.md) - Perform evidence-backed impact analysis before changing code, data, interfaces, or governance documents, then 
- [affaan-m/ECC:deployment-patterns](affaan-m-ecc-deployment-patterns.md) - Deployment workflows, CI/CD pipeline patterns, Docker containerization, health checks, rollback strategies, an
- [vercel-labs/agent-skills:writing-guidelines](vercel-labs-agent-skills-writing-guidelines.md) - Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style"

## Invoke / install

- Invoke: `/affaan-m/ECC:production-audit`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/production-audit --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 20eb99cf801c8d92d0d9df060705b1c6ea3f370f0c1594dbe31528a4f6904e9a --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
