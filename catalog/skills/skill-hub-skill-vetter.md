# skill-vetter

> Security-vet an Agent Skill, plugin folder or a GitHub repo of skills before installing or sharing it. Use whenever the user is about to install, copy, or enable a third-party skill; asks "is this skill safe", "check this SKILL.md", "audit this plugin"; or when a new skill, MCP helper or script bundle arrives from the internet. Runs a static scan (hidden Unicode, prompt-injection phrasing, curl-pipe-shell, credential paths, exfiltration endpoints, binaries, install hooks, ranking manipulation), pins the exact commit and file hashes, and reports PASS / REVIEW / FAIL with line numbers. Not a guarantee of safety.

| | |
|---|---|
| **ID** | `skill-hub:skill-vetter` |
| **Pack** | Claude / Skills / Plugin Tooling (also: Security & Privacy) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | plugin `skill-hub` - [Soum-Code/master-skill-hub](https://github.com/Soum-Code/master-skill-hub) |
| **License** | MIT |
| **Size** | 43 lines in SKILL.md, 3 file(s) |

## When to use it

- Use whenever the user is about to install, copy, or enable a third-party skill; asks "is this skill safe", "check this SKILL.md", "audit this plugin"; or when a new skill, MCP helper or script bundle arrives from the internet.

## What it says up front

> Third-party skills are instructions plus scripts that run with the user's permissions. Treat them like a dependency from a stranger.

## How it is structured

The skill's own section headings, in order:

- Procedure
- Reading the verdict
- What the scanner checks
- Limits

## What it bundles

- scripts: `scripts/install.py`, `scripts/vet.py`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/skill-hub:skill-vetter`
- Install: `claude plugin marketplace add Soum-Code/master-skill-hub && claude plugin install skill-hub@master-skill-hub`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
