# claude-security

> Claude Security: scan the codebase (the whole repository or a scoped part of it), scan changes (this branch's or a pull request's diff, or one commit), or suggest patches (findings turned into targeted patch files, each verified by a panel of agents, that you apply when you choose). Use when the user asks to scan, audit or check code with Claude Security, to scan their changes with Claude Security, or to fix or patch Claude Security findings.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:claude-security` |
| **Pack** | Security & Privacy (also: AI / ML Engineering) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 70 lines in SKILL.md, 7 file(s) |

## When to use it

- Use when the user asks to scan, audit or check code with Claude Security, to scan their changes with Claude Security, or to fix or patch Claude Security findings.

## What it says up front

> This is the front desk. Its whole purpose is to work out which job the user wants and drive it, following that job's recipe.

## How it is structured

The skill's own section headings, in order:

- The front-desk menu
- Environment and Paths (substituted at invocation, use verbatim)
- What to say about safety, if asked
- Existing Findings

## What it bundles

- 6 other file(s)

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Glob`, `Grep`, `AskUserQuestion`, `Workflow`, `Workflow(claude-security:scan)`, `Agent(claude-security:scan-inventory, claude-security:scan-r`, `Bash(date *)`, `Bash(ls *)`, `Bash(wc *)`, `Bash(mkdir -p *)`, `Bash(git *)`, `Bash(GIT_CONFIG_GLOBAL=/dev/null GIT_TERMINAL_PROMPT=0 git *`, `Bash(find . -maxdepth 1 -type d -name "CLAUDE-SECURITY-2*")`, `Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/render_report.py`, `Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/save_result.py" `, `Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/write_scan_meta.`, `Bash(bash "${CLAUDE_PLUGIN_ROOT}/scripts/keep-waiting.sh" *)`, `Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/patch_artifacts.`, `Bash(sleep *)`, `Bash(GIT_TERMINAL_PROMPT=0 git *)`

## Related skills

- [anthropics/claude-plugins-official:claude-md-improver](anthropics-claude-plugins-official-claude-md-improver.md) - Audit and improve CLAUDE.md files in repositories. Use when user asks to check, audit, update, improve, or fix
- [affaan-m/ECC:security-scan](affaan-m-ecc-security-scan.md) - Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and 
- [openai/skills:yeet](openai-skills-yeet.md) - Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow usin
- [affaan-m/ECC:context-budget](affaan-m-ecc-context-budget.md) - Routes live context checks to the native Codex or Claude Code meter without scanning files, and performs a bou

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:claude-security`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/claude-security/skills/claude-security --commit 0412be76f50ab4f4f8abff3753efa9269fbbca5b --expect-tree 5912501c4916daebe0c74aaa66365851e5e71533bd9c4b5bc041733567593278 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
