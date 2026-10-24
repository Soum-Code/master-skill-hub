# math-olympiad

> Solve competition math problems (IMO, Putnam, USAMO, AIME) with adversarial verification that catches the errors self-verification misses. Activates when asked to 'solve this IMO problem', 'prove this olympiad inequality', 'verify this competition proof', 'find a counterexample', 'is this proof correct', or for any problem with 'IMO', 'Putnam', 'USAMO', 'olympiad', or 'competition math' in it. Uses pure reasoning (no tools) — then a fresh-context adversarial verifier attacks the proof using specific failure patterns, not generic 'check logic'. Outputs calibrated confidence — will say 'no confident solution' rather than bluff. If LaTeX is available, produces a clean PDF after verification passes.

| | |
|---|---|
| **ID** | `anthropics/claude-plugins-official:math-olympiad` |
| **Pack** | Spec-driven Dev Workflow |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) |
| **License** | Apache-2.0 |
| **Size** | 412 lines in SKILL.md, 11 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> biased toward agreement. Fresh context, cleaned proof only. 2. **"Does this prove RH?"** — if your theorem's specialization to ζ is a famous open problem, you have a gap. Most reliable red flag. 3. **Short proof → extract the general lemma** — try 2×2 counterexamples. If general form is false, find

## How it is structured

The skill's own section headings, in order:

- The five things that change outcomes
- When to use which approach
  - For a full problem set
- The Workflow
  - 1. Interpretation check (30 seconds, catches 50/63 of one class of errors)
  - 2. Generate candidates with internal refinement (parallel, thinking only)
  - 3. Clean the solution (context isolation — the #1 lever)
  - 4. Adversarial verify (fresh context, pattern-armed)
  - 5. Rank and vote-verify (asymmetric + early exit)
  - 5b. When one case won't close — step back before grinding
  - 6. Revise (if needed)
  - 6c. Deep mode (when tight-budget abstains)
  - 7. Calibrated abstention
  - 8. Presentation pass (after correctness is established)
- Model tier defaults
- For numeric-answer problems (AIME-style)
- Key references
- What makes this different from generic verify-and-refine

## What it bundles

- scripts: `scripts/check_latex.sh`, `scripts/compile_pdf.sh`
- reference docs: `references/adversarial_prompts.md`, `references/attempt_agent.md`, `references/known_constructions.md`, `references/model_tier_defaults.md`, `references/presentation_prompts.md`, `references/solver_heuristics.md`, `references/verifier_patterns.md`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Invoke / install

- Invoke: `/anthropics/claude-plugins-official:math-olympiad`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/claude-plugins-official --path plugins/math-olympiad/skills/math-olympiad --commit 58267944f92187b7d6a1c822165c96c81c864806 --expect-tree 4b9abdf266f71afdc777bc87e1374cc1cb6abf75344fc4806b42f73ab4f5bf67 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
