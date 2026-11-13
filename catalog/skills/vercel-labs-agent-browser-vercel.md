# vercel

> Access and test Vercel deployments with agent-browser, behind Deployment Protection or at a different feature flag variant. Use when a preview or production URL redirects to a Vercel login page, returns a protection 401 or 403, needs short-lived Trusted Sources OIDC authentication instead of a static bypass secret or public exception, or must be viewed with a Vercel feature flag set to another variant.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:vercel` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 161 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a preview or production URL redirects to a Vercel login page, returns a protection 401 or 403, needs short-lived Trusted Sources OIDC authentication instead of a static bypass secret or public exception, or must be viewed with a Vercel feature flag se.

## What it says up front

> Reach a Vercel deployment as the user asked to see it without changing what anyone else sees. Pass protection and flag overrides on this browser's requests; changing project settings or a flag's served variant needs explicit approval.

## How it is structured

The skill's own section headings, in order:

- Deployment Protection
  - Same-project preview
  - Other environments and callers
  - Human intervention boundaries
  - Use the correct header
  - Diagnose failures
  - Static-secret fallback
- Feature flags
- Avoid dead ends

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `agent-browser:*)`, `Bash(vc:*)`, `Bash(vercel:*)`

## Related skills

- [vercel-labs/agent-browser:protected-vercel-deployments](vercel-labs-agent-browser-protected-vercel-deployments.md) - Access and test Vercel deployments protected by Vercel Authentication, SSO, or Deployment Protection with agen
- [affaan-m/ECC:opensource-pipeline](affaan-m-ecc-opensource-pipeline.md) - Open-source pipeline: fork, sanitize, and package private projects for safe public release. Chains 3 agents (f

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:vercel`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/vercel --commit 4720bc3dd73f2c8f7c84f415adfa560330b924c4 --expect-tree a9fe07c23848ea1726bd4d49f309526006bdc32df0fc551bae160f1abcf12113 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
