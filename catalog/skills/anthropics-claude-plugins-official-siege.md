# siege

> Work on one hard mathematics problem in rounds: each round a judge writes a few self-contained questions, independent workers answer them, and the judge keeps a ledger of what is proved, refuted and open, until the judge concludes or the rounds run out, and then a proof.md says plainly what is and is not proved. A run takes hours and dozens of worker runs. Usage: /math-proof:siege [NAME=value settings] .

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:siege` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 733 lines in SKILL.md, 2 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> The skill works on one problem in at most MAX_ROUNDS rounds. Each round a judge writes a few self-contained questions, at most WAVE of them before round ESC_ROUND. The steps below call them queries. Each question goes to a fresh worker that sees only that question and the problem statement. The judg

## How it is structured

The skill's own section headings, in order:

- The approach
- Setup
- The round loop — for r = 1, 2, …, MAX_ROUNDS
- The proof tail (after the loop ends, by CONCLUDE, TAIL, or finishing round MAX_ROUNDS)
- Rules that hold throughout
- PLAN BRIEF (round {r} of at most {MAX_ROUNDS}; {CAP}, {HORIZON}, {CONCLUDE_RULE}, {ESC_SUM
- DRAFT BRIEF
- REFINE BRIEF (step name {S} = refine_2, refine_3, … in order)
- SELECT BRIEF
- FINALIZE BRIEF

## What it bundles

- scripts: `scripts/ledger.py`

## Permissions and risk notes

- Pre-approved tools: `Read`, `Write`, `Edit`, `Glob`, `Grep`, `Agent`, `Bash(python3`, `${CLAUDE_SKILL_DIR}/scripts/ledger.py`, `*)`, `Bash(python3`, `${CLAUDE_PLUGIN_ROOT}/skills/siege/scripts/ledger.py`, `*)`, `Bash(python`, `${CLAUDE_SKILL_DIR}/scripts/ledger.py`, `*)`, `Bash(python`, `${CLAUDE_PLUGIN_ROOT}/skills/siege/scripts/ledger.py`, `*)`, `Bash(mkdir`, `*)`, `Bash(cp`, `*)`, `Bash(mv`, `*)`, `Bash(cat`, `*)`, `Bash(test`, `*)`, `Bash(ls`, `*)`
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropics/claude-plugins-official:solo](anthropics-claude-plugins-official-solo.md) - Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, record ea

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:siege`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/math-proof/skills/siege --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 0a577d438e4c0f8655281704c5d85d4e5873d1f1f094022e096c19bfbf6bcd6c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
