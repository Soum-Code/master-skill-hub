# humanizer

> Personal writing filter that strips AI-sounding tells (Wikipedia's "Signs of AI writing" patterns) and Claude's own verbal tics out of any text Claude produces. Use this on every response — chat replies, drafts, emails, documents, code comments, anything written in prose — for this user, not just when they explicitly say "humanize this." Trigger it silently on every turn where Claude is generating written content; don't wait to be asked.

| | |
|---|---|
| **ID** | `anthropic-skills:humanizer` |
| **Pack** | Documents, Writing & Content |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `anthropic-skills` |
| **License** | not declared |
| **Size** | 75 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## How it is structured

The skill's own section headings, in order:

- 1. Banned vocabulary
- 2. Sentence-level patterns
- 3. Formatting habits
- 4. Claude-specific tics (not from Wikipedia, but just as recognizable)
- 5. How to actually write instead
- Scope

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:docx](anthropic-skills-docx.md) - Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx) or Word tem

## Invoke / install

- Invoke: `/anthropic-skills:humanizer`  (Skill tool: `anthropic-skills:humanizer`)
- Install: `built into the Claude desktop app / claude.ai`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
