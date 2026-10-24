# security-best-practices

> Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks.

| | |
|---|---|
| **ID** | `openai/skills:security-best-practices` |
| **Pack** | Software Development (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [openai/skills](https://github.com/openai/skills) |
| **License** | not declared |
| **Size** | 87 lines in SKILL.md, 13 file(s) |

## When to use it

- Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help.
- Trigger only for supported languages (python, javascript/typescript, go).
- Do not trigger for general code review, debugging, or non-security tasks.

## How it is structured

The skill's own section headings, in order:

- Overview
- Workflow
- Workflow Decision Tree
  - Avoid Using Incrementing IDs for Public IDs of Resources
  - A note on TLS

## What it bundles

- reference docs: `references/golang-general-backend-security.md`, `references/javascript-express-web-server-security.md`, `references/javascript-general-web-frontend-security.md`, `references/javascript-jquery-web-frontend-security.md`, `references/javascript-typescript-nextjs-web-server-security.md`, `references/javascript-typescript-react-web-frontend-security.md`, `references/javascript-typescript-vue-web-frontend-security.md`, `references/python-django-web-server-security.md` ...
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:security-threat-model](openai-skills-security-threat-model.md) - Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse pat
- [openai/skills:security-ownership-map](openai-skills-security-ownership-map.md) - Analyze git repositories to build a security ownership topology (people-to-file), compute bus factor and sensi
- [vercel-labs/agent-skills:vercel-react-best-practices](vercel-labs-agent-skills-vercel-react-best-practices.md) - React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when 
- [huggingface/skills:huggingface-zerogpu](huggingface-skills-huggingface-zerogpu.md) - AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU. Use when writing or reviewing cod

## Invoke / install

- Invoke: `/openai/skills:security-best-practices`
- Install: `python skills/skill-vetter/scripts/install.py openai/skills --path skills/.curated/security-best-practices --commit 49f948faa9258a0c61caceaf225e179651397431 --expect-tree 58b9255ed3b29426cdb165ae470893c6652b616a7c23425e02053d5df7626159 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
