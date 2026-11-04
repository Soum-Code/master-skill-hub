# parallel-execution-optimizer

> Speed up a task by turning it into a dependency graph of parallel lanes with a lane matrix, batched reads and checks, write surfaces isolated by file, worktree, branch, or service, and a final verification table. Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls, isolated worktrees, many independent verification lanes, or bounded homogeneous work that reuses shared preparation while record operations remain sequential, without losing correctness.

| | |
|---|---|
| **ID** | `affaan-m/ECC:parallel-execution-optimizer` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 174 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user wants a task done much faster through parallel work, concurrent agents, batched tool calls, isolated worktrees, many independent verification lanes, or bounded homogeneous work that reuses shared preparation while record operations remain seq.

## What it says up front

> Use this skill when speed comes from doing independent work at the same time: repo inspection, file reads, API checks, browser checks, build/test lanes, deploy readbacks, or multi-worktree implementation passes. Also use it when homogeneous work repeats unchanged preparation between records, even if

## How it is structured

The skill's own section headings, in order:

- Core Pattern
- Lane Matrix
- Execution Rules
- Bounded Homogeneous Work
  - Planner/Executor Example
  - Resume After a Connector Change
  - Evaluation Criteria
- Output Shape
- Failure Modes

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ralphinho-rfc-pipeline](affaan-m-ecc-ralphinho-rfc-pipeline.md) - Split an RFC into a multi-agent execution DAG — decompose into work units with dependencies and acceptance tes

## Invoke / install

- Invoke: `/affaan-m/ECC:parallel-execution-optimizer`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/parallel-execution-optimizer --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 4eba193079d6ce14e8dc4f3171ae1bf35b3c89f37e0694fd30a9ef2485db023e --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
