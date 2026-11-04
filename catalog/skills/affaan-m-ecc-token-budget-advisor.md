# token-budget-advisor

> Offer a choice of response depth (25%/50%/75%/100%) with token estimates before answering, then answer at that level. Use when the user asks to control response length or token budget, such as 'token budget', 'short version', 'brief answer', 'respuesta corta vs larga', 'cuántos tokens', 'ahorrar tokens', 'responde al 50%', 'dame la versión corta', 'quiero controlar cuánto usas'. Skip if depth is already set this session or 'token' means an auth/payment token.

| | |
|---|---|
| **ID** | `affaan-m/ECC:token-budget-advisor` |
| **Pack** | Finance & Accounting |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 123 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when the user asks to control response length or token budget, such as 'token budget', 'short version', 'brief answer', 'respuesta corta vs larga', 'cuántos tokens', 'ahorrar tokens', 'responde al 50%', 'dame la versión corta', 'quiero controlar cuánto usa.

## What it says up front

> Intercept the response flow to offer the user a choice about response depth **before** Claude answers.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Step 1 — Estimate input tokens
  - Step 2 — Estimate response size by complexity
  - Step 3 — Present depth options
  - Step 4 — Respond at the chosen level
- Shortcuts — skip the question
- Precision note
- Examples
  - Triggers
  - Does Not Trigger
- Source

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:token-budget-advisor`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/token-budget-advisor --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree b21047ad35b8471436e1d360da8e3d69b77d6218d75edfa34725797b64be687f --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
