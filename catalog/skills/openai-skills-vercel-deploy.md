# vercel-deploy

> Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

| | |
|---|---|
| **ID** | `openai/skills:vercel-deploy` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 78 lines in SKILL.md, 6 file(s) |

## When to use it

- Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

## How it is structured

The skill's own section headings, in order:

- Prerequisites
- Quick Start
- Fallback (No Auth)
- Production Deploys
- Output
- Troubleshooting
  - Escalated Network Access

## What it bundles

- scripts: `scripts/deploy.sh`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [openai/skills:netlify-deploy](openai-skills-netlify-deploy.md) - Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, 
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [anthropics/claude-plugins-official:playground](anthropics-claude-plugins-official-playground.md) - Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something

## Invoke / install

- Invoke: `/openai/skills:vercel-deploy`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/vercel-deploy --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 610407ed21fd55ea65422c0c9468dd10843d0210a0bc45b1e937285d5787d1b2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
