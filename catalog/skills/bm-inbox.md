# inbox

> Triage and review all open GitHub issues and PRs against project templates and contribution guidelines

| | |
|---|---|
| **ID** | `bm:inbox` |
| **Pack** | Communication & Collaboration (also: Productivity & Automation, MLOps / DevOps / Cloud, Software Development) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `bm` v4.5.5 - [jnuyens/gsd-plugin](https://github.com/jnuyens/gsd-plugin) |
| **License** | MIT |
| **Size** | 39 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> One-command triage of the project's GitHub inbox. Fetches all open issues and PRs, reviews each against the corresponding template requirements (feature, enhancement, bug, chore, fix PR, enhancement PR, feature PR), reports completeness and compliance, and optionally applies labels or closes non-com

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Pre-approved tools: `Read`, `Bash`, `Write`, `Grep`, `Glob`, `AskUserQuestion`

## Related skills

- [openai/skills:gh-address-comments](openai-skills-gh-address-comments.md) - Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth f
- [vercel-labs/agent-skills:writing-guidelines](vercel-labs-agent-skills-writing-guidelines.md) - Review docs/prose for Writing Guidelines compliance. Use when asked to "review my docs", "check writing style"
- [vercel-labs/agent-skills:web-design-guidelines](vercel-labs-agent-skills-web-design-guidelines.md) - Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility
- [anthropics/claude-plugins-official:claude-md-improver](anthropics-claude-plugins-official-claude-md-improver.md) - Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix

## Invoke / install

- Invoke: `/bm:inbox`  (Skill tool: `bm:inbox`)
- Install: `claude plugin marketplace add jnuyens/gsd-plugin && claude plugin install bm@gsd-plugin`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
