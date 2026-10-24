# netlify-deploy

> Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

| | |
|---|---|
| **ID** | `openai/skills:netlify-deploy` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 248 lines in SKILL.md, 8 file(s) |

## When to use it

- Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys.

## How it is structured

The skill's own section headings, in order:

- Overview
- Prerequisites
- Authentication Pattern
- Workflow
  - 1. Verify Netlify CLI Authentication
  - 2. Detect Site Link Status
  - 3. Link to Existing Site or Create New
  - 4. Verify Dependencies
  - 5. Deploy to Netlify
  - 6. Report Results
- Handling netlify.toml
- Example Full Workflow
- Error Handling
- Troubleshooting
  - Escalated Network Access
- Environment Variables
- Tips
- Reference
- Bundled References (Load As Needed)

## What it bundles

- reference docs: `references/cli-commands.md`, `references/deployment-patterns.md`, `references/netlify-toml.md`
- 4 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:vercel-deploy](openai-skills-vercel-deploy.md) - Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app"
- [microsoft/playwright-cli:dev](microsoft-playwright-cli-dev.md) - Development workflows for the playwright-cli repository. Use when the user asks about rolling dependencies, re
- [huggingface/skills:huggingface-papers](huggingface-skills-huggingface-papers.md) - Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as 
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin

## Invoke / install

- Invoke: `/openai/skills:netlify-deploy`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/netlify-deploy --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree e6bc4b59b51fcdca7b33cbc132a703f441e43a9ccf06fe28675d903a86306910 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
