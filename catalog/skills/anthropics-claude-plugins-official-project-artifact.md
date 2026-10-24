# project-artifact

> Generate and publish a project status artifact — an opinionated, tabbed status page for a project too big for one update (overview & success criteria, the workstream sequence, next steps, plus background, plan, risks & open questions, and decisions/FAQ when they earn a tab) — published with the built-in Artifact tool to a default-private claude.ai page the user can share with teammates. Use when a piece of work spans several workstreams and you want a shareable overview kept current. Each artifact is backed by a small per-project config in the plugin data dir, so refreshing it re-gathers live state, redeploys the same URL, and reports only the delta. For software projects whose workstreams are PRs, also read swe.md (the X.Y PR-numbering convention; pulling PR state with gh/git; a per-PR detail block). Needs the built-in Artifact tool (claude.ai login). Not for single-PR changes or public docs.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:project-artifact` |
| **Pack** | Spec-driven Dev Workflow (also: Web, Frontend & UI Design) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 262 lines in SKILL.md, 3 file(s) |

## When to use it

- Use when a piece of work spans several workstreams and you want a shareable overview kept current.

## What it says up front

> This skill produces one specific *kind* of artifact: a tabbed status page that represents a project too big for one update — a software migration, a research effort, a launch, an org initiative; anything with a set of parallel/dependent workstreams tracked over time. It generates the HTML (one file,

## How it is structured

The skill's own section headings, in order:

- Workflow
- The artifact config (one per project)
- Refreshing an artifact (deltas, not re-narratives)
- Freshness and trust
- Reading an existing artifact page
- Tab catalog (domain-neutral)
- Conventions (all domains)
- Specializations
- Files

## What it bundles

- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [anthropic-skills:chrome-browser](anthropic-skills-chrome-browser.md) - Read this skill before the first step that uses Claude in Chrome, the browser extension whose tools are named 

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:project-artifact`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/project-artifact/skills/project-artifact --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 2568201919b501813bc8875d2e848f9aa3a7b20c78b89c1de29ae2ab43e4446f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
