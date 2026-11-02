# deploy-to-vercel

> Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

| | |
|---|---|
| **ID** | `vercel-labs/agent-skills:deploy-to-vercel` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) |
| **License** | not declared |
| **Size** | 231 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user requests deployment actions like "deploy my app", "deploy and give me the link", "push this live", or "create a preview deployment".

## How it is structured

The skill's own section headings, in order:

- Step 1: Gather Project State
  - Team selection
- Step 2: Choose a Deploy Method
  - Linked (`.vercel/` exists) + has git remote → Git Push
  - Linked (`.vercel/` exists) + no git remote → `vercel deploy`
  - Not linked + CLI is authenticated → Link first, then deploy
  - Not linked + CLI not authenticated → Install, auth, link, deploy
  - No-Auth Fallback — `vercel deploy --temporary`
- Agent-Specific Notes
  - Claude Code / terminal-based agents
  - Sandboxed environments (claude.ai, Codex)
- Output
- Troubleshooting
  - Network Egress Error (claude.ai)
  - Escalated Network Access (Codex / sandboxed environments)
  - CLI Auth Failure

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:vercel-deploy](openai-skills-vercel-deploy.md) - Deploy applications and websites to Vercel. Use when the user requests deployment actions like "deploy my app"
- [openai/skills:netlify-deploy](openai-skills-netlify-deploy.md) - Deploy web projects to Netlify using the Netlify CLI (`npx netlify`). Use when the user asks to deploy, host, 
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [anthropics/claude-plugins-official:playground](anthropics-claude-plugins-official-playground.md) - Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something

## Invoke / install

- Invoke: `/vercel-labs/agent-skills:deploy-to-vercel`
- Install: `python skills/skill-vetter/scripts/install.py vercel-labs/agent-skills --path skills/deploy-to-vercel --commit 1a2c79d4e6c4a2283dc2c614b6538cbe1ed5ca62 --expect-tree 09741b0ee68e9deb9d32f3c89a4f3a41d1b56ec518fe78b2ac71349357a7ae96 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
