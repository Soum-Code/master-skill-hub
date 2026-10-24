# close-management

> Manage the month-end close process with task sequencing, dependencies, and status tracking. Use when planning the close calendar, tracking close progress, identifying blockers, or sequencing close activities by day.

| | |
|---|---|
| **ID** | `finance:close-management` |
| **Pack** | Operations & Business (also: Finance & Accounting) |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `finance` v1.3.0 - [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 222 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when planning the close calendar, tracking close progress, identifying blockers, or sequencing close activities by day.

## What it says up front

> Month-end close checklist, task sequencing and dependencies, status tracking, and common close activities organized by day.

## How it is structured

The skill's own section headings, in order:

- Month-End Close Checklist
  - Pre-Close (Last 2-3 Business Days of the Month)
  - Close Day 1 (T+1: First Business Day After Month-End)
  - Close Day 2 (T+2)
  - Close Day 3 (T+3)
  - Close Day 4 (T+4)
  - Close Day 5 (T+5)
- Task Sequencing and Dependencies
  - Dependency Map
  - Critical Path
- Status Tracking and Reporting
  - Close Status Dashboard
  - Status Definitions
  - Daily Close Status Meeting (Recommended)
  - Close Metrics to Track Over Time
- Common Close Activities by Day
  - Typical 5-Day Close Calendar
  - Accelerated Close (3-Day Target)
- Close Process Improvement
  - Common Bottlenecks and Solutions
  - Close Retrospective Questions

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [openai/skills:notion-spec-to-implementation](openai-skills-notion-spec-to-implementation.md) - Turn Notion specs into implementation plans, tasks, and progress tracking; use when implementing PRDs/feature 
- [bm:workstreams](bm-workstreams.md) - Manage parallel workstreams — list, create, switch, status, progress, complete, and resume

## Invoke / install

- Invoke: `/finance:close-management`  (Skill tool: `finance:close-management`)
- Install: `bundled with Claude desktop (Cowork plugin 'finance'); source: github.com/anthropics/knowledge-work-plugins`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
