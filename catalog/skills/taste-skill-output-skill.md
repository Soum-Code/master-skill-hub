# full-output-enforcement

> Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output.

| | |
|---|---|
| **ID** | `taste-skill:output-skill` |
| **Pack** | Software Development |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `taste-skill` v1.0.0 - [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) |
| **License** | MIT |
| **Size** | 50 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Treat every task as production-critical. A partial output is a broken output. Do not optimize for brevity — optimize for completeness. If the user asks for a full file, deliver the full file. If the user asks for 5 components, deliver 5 components. No exceptions.

## How it is structured

The skill's own section headings, in order:

- Baseline
- Banned Output Patterns
- Execution Process
- Handling Long Outputs
- Quick Check

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/taste-skill:output-skill`  (Skill tool: `taste-skill:output-skill`)
- Install: `claude plugin marketplace add leonxlnx/taste-skill && claude plugin install taste-skill@taste-skill`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
