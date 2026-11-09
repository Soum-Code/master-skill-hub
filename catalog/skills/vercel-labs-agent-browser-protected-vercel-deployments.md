# protected-vercel-deployments

> Access and test Vercel deployments protected by Vercel Authentication, SSO, or Deployment Protection with agent-browser. Use when a preview or production URL redirects to a Vercel login page, returns a protection 401 or 403, or needs short-lived Trusted Sources OIDC authentication instead of a static bypass secret or public exception.

| | |
|---|---|
| **ID** | `vercel-labs/agent-browser:protected-vercel-deployments` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser) |
| **License** | Apache-2.0 |
| **Size** | 111 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a preview or production URL redirects to a Vercel login page, returns a protection 401 or 403, or needs short-lived Trusted Sources OIDC authentication instead of a static bypass secret or public exception.

## What it says up front

> Use the caller's existing Vercel identity and a short-lived OIDC token. Do not disable Deployment Protection, make the deployment public, or ask for a static bypass secret first.

## How it is structured

The skill's own section headings, in order:

- Same-project preview
- Other environments and callers
- Human intervention boundaries
- Use the correct header
- Diagnose failures
- Static-secret fallback
- Avoid dead ends

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Bash(agent-browser:*)`, `Bash(npx`, `agent-browser:*)`, `Bash(vc:*)`, `Bash(vercel:*)`

## Related skills

- [vercel-labs/agent-skills:vercel-cli-with-tokens](vercel-labs-agent-skills-vercel-cli-with-tokens.md) - Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using 

## Invoke / install

- Invoke: `/vercel-labs/agent-browser:protected-vercel-deployments`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-browser --path skill-data/protected-vercel-deployments --commit 4b0e9f01fa8d214d39bbfe5391257640634fb9a0 --expect-tree 92495dd7f10b3c40a4a40f8b9c8329af61a47fd8144edf481912a9f2b041ab34 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
