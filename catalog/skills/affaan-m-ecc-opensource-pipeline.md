# opensource-pipeline

> Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (forker, sanitizer, packager). Triggers: '/opensource', 'open source this', 'make this public', 'prepare for open source'. Use when a private project must be forked, stripped of secrets, and packaged for public release.

| | |
|---|---|
| **ID** | `affaan-m/ECC:opensource-pipeline` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 329 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a private project must be forked, stripped of secrets, and packaged for public release.

## What it says up front

> Safely open-source any project through a 3-stage pipeline: **Fork** (strip secrets) → **Sanitize** (verify clean) → **Package** (CLAUDE.md + setup.sh + README).

## How it is structured

The skill's own section headings, in order:

- When to Activate
- Commands
- Protocol
  - /opensource fork PROJECT
  - /opensource verify PROJECT
  - /opensource package PROJECT
  - /opensource list
  - /opensource status PROJECT
- Staging Layout
- Anti-Patterns
- Best Practices
- Related Skills

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [vercel-labs/agent-browser:vercel](vercel-labs-agent-browser-vercel.md) - Access and test Vercel deployments with agent-browser, behind Deployment Protection or at a different feature 

## Invoke / install

- Invoke: `/affaan-m/ECC:opensource-pipeline`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/opensource-pipeline --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b56bdbc16c79a62011d29479b083908fceae2f71a0268bad8701b77b862b618c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
