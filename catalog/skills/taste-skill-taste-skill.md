# design-taste-frontend

> Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check.

| | |
|---|---|
| **ID** | `taste-skill:taste-skill` |
| **Pack** | Web, Frontend & UI Design |
| **Kind** | skill |
| **Status** | installed (owner's machine) |
| **Origin** | plugin `taste-skill` v1.0.0 - [leonxlnx/taste-skill](https://github.com/leonxlnx/taste-skill) |
| **License** | MIT |
| **Size** | 1207 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> Before touching code or tweaking dials, **infer what the user actually wants**. Most LLM design output is bad because the model jumps to a default aesthetic instead of reading the room.

## How it is structured

The skill's own section headings, in order:

- 0. BRIEF INFERENCE (Read the Room Before Anything Else)
  - 0.A Read these signals first
  - 0.B Output a one-line "Design Read" before generating
  - 0.C If the brief is ambiguous, ask one question, do not guess
  - 0.D Anti-Default Discipline
- 1. THE THREE DIALS (Core Configuration)
  - 1.A Dial Inference (design read → dial values)
  - 1.B Use-Case Presets
  - 1.C How the Dials Drive Output
- 2. BRIEF → DESIGN SYSTEM MAP
  - 2.A When to reach for a real design system (use official packages)
  - 2.B When the brief is an aesthetic, not a system
- 3. DEFAULT ARCHITECTURE & CONVENTIONS
  - 3.A Stack
  - 3.B State
  - 3.C Icons
  - 3.D Emoji Policy
  - 3.E Responsiveness & Layout Mechanics
  - 3.F Dependency Verification (mandatory)
- 4. DESIGN ENGINEERING DIRECTIVES (Bias Correction)
  - 4.1 Typography
  - 4.2 Color Calibration
  - 4.3 Layout Diversification
  - 4.4 Materiality, Shadows, Cards
  - 4.5 Interactive UI States
  - 4.6 Data & Form Patterns
  - 4.7 Layout Discipline (Hard Rules. Failing any of these is shipping broken work)
  - 4.8 Image & Visual Asset Strategy
  - 4.9 Content Density
  - 4.10 Quotes & Testimonials

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [taste-skill:stitch-skill](taste-skill-stitch-skill.md) - Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium,
- [example-skills:frontend-design](example-skills-frontend-design.md) - Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps w
- [frontend-design:frontend-design](frontend-design-frontend-design.md) - Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. Helps w
- [taste-skill:imagegen-frontend-web](taste-skill-imagegen-frontend-web.md) - Elite frontend image-direction skill for generating premium, conversion-aware website design references. CRITI

## Invoke / install

- Invoke: `/taste-skill:taste-skill`  (Skill tool: `taste-skill:taste-skill`)
- Install: `claude plugin marketplace add leonxlnx/taste-skill && claude plugin install taste-skill@taste-skill`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
