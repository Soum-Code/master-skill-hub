# ck

> Persistent per-project memory for Claude Code (Context Keeper) driven by deterministic Node.js /ck commands: init, save, resume, info, list, forget, and v1-to-v2 migrate, plus a SessionStart hook that injects a compact project brief. Use when context must survive across sessions, saving session state with next steps and decisions, resuming where a previous session left off, or picking up a project without re-explaining it.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ck` |
| **Pack** | Productivity & Automation |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 166 lines in SKILL.md, 10 file(s) |

## When to use it

- Use when context must survive across sessions, saving session state with next steps and decisions, resuming where a previous session left off, or picking up a project without re-explaining it.

## What it says up front

> You are the **Context Keeper** assistant. When the user invokes any `/ck:*` command, run the corresponding Node.js script and present its stdout to the user verbatim. Scripts live in the `commands/` directory next to this SKILL.md (for example `~/.claude/skills/ck/commands/` for a manual install, or

## How it is structured

The skill's own section headings, in order:

- Data Layout
- Commands
  - `/ck:init` — Register a Project
  - `/ck:save` — Save Session State
  - `/ck:resume [name\|number]` — Full Briefing
  - `/ck:info [name\|number]` — Quick Snapshot
  - `/ck:list` — Portfolio View
  - `/ck:forget [name\|number]` — Remove a Project
  - `/ck:migrate` — Convert v1 Data to v2
- SessionStart Hook
- Rules

## What it bundles

- scripts: `commands/forget.mjs`, `commands/info.mjs`, `commands/init.mjs`, `commands/list.mjs`, `commands/migrate.mjs`, `commands/resume.mjs`, `commands/save.mjs`, `commands/shared.mjs` ...

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [affaan-m/ECC:unified-memory](affaan-m-ecc-unified-memory.md) - Share durable, inspectable context and handoffs between Claude, Codex, Hermes, Cursor, OpenCode, and other age
- [affaan-m/ECC:agentic-os](affaan-m-ecc-agentic-os.md) - Build persistent multi-agent operating systems on Claude Code. Covers kernel architecture, specialist agents, 

## Invoke / install

- Invoke: `/affaan-m/ECC:ck`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ck --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 877e908ade7e42aa3589c286cde232d5775359e24ee03418a82898aec8903ba7 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
