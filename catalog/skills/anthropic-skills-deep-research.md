# deep-research

> Use this skill when the user's prompt requires (1) researching a topic across multiple sources, comparing options or alternatives, analyzing trends or history, understanding markets or industries, or reviewing literature or studies and (2) synthesizing that research into a comprehensive, narrative report. If you're planning to search the web or internal knowledge bases, consider using this skill. This skill coordinates research subagents, so use it only when you have a tool for spawning subagents (the Agent or Task tool); otherwise, research the question directly.

| | |
|---|---|
| **ID** | `anthropic-skills:deep-research` |
| **Pack** | Research & Learning |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | not declared |
| **Size** | 147 lines in SKILL.md, 3 file(s) |

## When to use it

- Use this skill when the user's prompt requires (1) researching a topic across multiple sources, comparing options or alternatives, analyzing trends or history, understanding markets or industries, or reviewing literature or studies and (2) synthesizing that re.

## How it is structured

The skill's own section headings, in order:

- Your Role
- Process
  - 1. [If necessary] Ask the user follow up questions
  - 2. Choose a title for this research and create its directories
  - 3. Decompose the user's query to determine subagent count
  - 4. Spawn foreground research subagents (in parallel)
  - 5. [If absolutely necessary] Conduct one additional round of research
  - 6. Spawn foreground report writer subagent
  - 7. Deliver report to user

## What it bundles

- reference docs: `references/report-writer.md`, `references/researcher.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/anthropic-skills:deep-research`  (Skill tool: `anthropic-skills:deep-research`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
