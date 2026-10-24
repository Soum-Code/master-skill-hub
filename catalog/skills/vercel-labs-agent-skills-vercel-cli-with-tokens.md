# vercel-cli-with-tokens

> Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. "deploy to vercel", "set up vercel", "add environment variables to vercel".

| | |
|---|---|
| **ID** | `vercel-labs/agent-skills:vercel-cli-with-tokens` |
| **Pack** | MLOps / DevOps / Cloud (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| **License** | not declared |
| **Size** | 354 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when working with Vercel CLI using access tokens rather than interactive login — e.g.

## How it is structured

The skill's own section headings, in order:

- Step 1: Locate the Vercel Token
  - A) `VERCEL_TOKEN` is already set in the environment
  - B) Token is in a `.env` file under `VERCEL_TOKEN`
  - C) Token is in a `.env` file under a different name
  - D) No token found — ask the user
- Step 2: Locate the Project and Team
- CLI Setup
- Deploying a Project
  - Quick Deploy (have project ID — no linking needed)
  - Full Deploy Flow (no project ID — need to link)
  - Deploying from a Remote Repository (code not cloned locally)
  - About `.vercel/` Directory
- Managing Environment Variables
- Inspecting Deployments
- Managing Domains
- Stripe Projects Plan Changes
  - What Pro gives you
- Working Agreement
- Troubleshooting
  - Token not found
  - Authentication error
  - Wrong team
  - Build failure
  - CLI not installed

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:netlify-deploy](openai-skills-netlify-deploy.md) - Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, 
- [vercel-labs/agent-browser:protected-vercel-deployments](vercel-labs-agent-browser-protected-vercel-deployments.md) - Access and test Vercel deployments protected by Vercel Authentication, SSO, or Deployment Protection with agen

## Invoke / install

- Invoke: `/vercel-labs/agent-skills:vercel-cli-with-tokens`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-skills --path skills/vercel-cli-with-tokens --commit 063bee94c3f4df8453406c830b0a7df0f2860278 --expect-tree 84be539bc95ce959d656a298ac3c3e96794607992026f109b809c29677377b79 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
