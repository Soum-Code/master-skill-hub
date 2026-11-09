# master-agreement-generator

> Generate review drafts of counterparty master agreements from one template plus a JSON spec, with role-selected clauses and a Schedule A workflow limited to the executed agreement's notice authority. Use when you need reproducible drafting and separately reviewed execution preparation.

| | |
|---|---|
| **ID** | `affaan-m/ECC:master-agreement-generator` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 231 lines in SKILL.md, 4 file(s) |

## When to use it

- Use when you need reproducible drafting and separately reviewed execution preparation.

## What it says up front

> One master template, one small spec per counterparty, one draft build step. The generator always labels output **DRAFT**, including documents generated from a completed template. A successful conversion proves artifact generation, not legal completeness, authority to contract, or readiness to send o

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Template
  - Spec
  - Role table
  - Build
  - Signature page geometry
  - Schedule A append workflow
- Examples
  - Notice text
  - Adding the entry to the spec
  - Counterparty fills its own details at signing

## What it bundles

- scripts: `scripts/build-agreement.js`
- reference docs: `references/master-template.example.md`, `references/spec.example.json`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [google-gemini/gemini-cli:spec_generator](google-gemini-gemini-cli-spec-generator.md) - Generates a structured Workable Spec JSON to guide a Developer Worker.
- [legal:review-contract](legal-review-contract.md) - Review a contract against your organization's negotiation playbook — flag deviations, generate redlines, provi

## Invoke / install

- Invoke: `/affaan-m/ECC:master-agreement-generator`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/master-agreement-generator --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree acd00f49d373412baccde98bb9133fd80d1e72cbadea5e8efb99a4c20598da72 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
