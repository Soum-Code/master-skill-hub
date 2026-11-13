# simplify-codebase

> Simplification audit or authorized codebase simplification whose stated objective is to remove accidental complexity. Use for evidence-backed deletion or consolidation of dead code, duplicate state, redundant APIs or layers, ownerless abstractions, obsolete compatibility or design records, and over-engineering in any language; also use for 代码简化 or 熵回收. Do not use for general code review, onboarding, style-only refactoring, or performance tuning.

| | |
|---|---|
| **ID** | `tt-a1i/archify:simplify-codebase` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [tt-a1i/archify](https://github.com/tt-a1i/archify) |
| **License** | Apache-2.0 |
| **Size** | 84 lines in SKILL.md, 8 file(s) |

## When to use it

- Use for evidence-backed deletion or consolidation of dead code, duplicate state, redundant APIs or layers, ownerless abstractions, obsolete compatibility or design records, and over-engineering in any language; also use for 代码简化 or 熵回收.
- Do not use for general code review, onboarding, style-only refactoring, or performance tuning.

## What it says up front

> Reduce the number of concepts and obligations a codebase must keep coherent. Line-count reduction is supporting evidence, not the objective. A successful run may conclude that the inspected surface is already justified.

## How it is structured

The skill's own section headings, in order:

- Select mode and scope
- Establish the contract
- Cover the relevant surface
- Build a proof record
- Decide and act
- Deliver the result

## What it bundles

- reference docs: `references/boundaries-and-lifecycle.md`, `references/decision-records.md`, `references/execution-and-recovery.md`, `references/integrating-findings.md`, `references/investigation.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [simplify](simplify.md) - Review changed code for reuse, simplification, efficiency and altitude cleanups, then apply the fixes. Quality
- [openai/skills:security-best-practices](openai-skills-security-best-practices.md) - Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only 
- [openai/skills:security-threat-model](openai-skills-security-threat-model.md) - Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse pat

## Invoke / install

- Invoke: `/tt-a1i/archify:simplify-codebase`
- Install: `python skills/skill-vetter/scripts/install.py tt-a1i/archify --path .agents/skills/simplify-codebase --commit 11b0d6031853bdae89eed57e7979aabbf0034097 --expect-tree 6d885603c692ffc70533adb505fc2426158f8a9dd8c3f70980fc47b48de73e3b --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
