# esign-field-placement

> Deterministic method for placing signature, date, and text fields in a web e-signature composer through a browser automation session, using a fixed signature page, numeric Location panel coordinates instead of drag, and a save-as-draft default. Use when automating envelope preparation for generated agreements and you need repeatable field positions, correct per-recipient ownership, and a hard gate before anything is sent or signed.

| | |
|---|---|
| **ID** | `affaan-m/ECC:esign-field-placement` |
| **Pack** | Legal & Compliance |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 200 lines in SKILL.md, 2 file(s) |

## When to use it

- Use when automating envelope preparation for generated agreements and you need repeatable field positions, correct per-recipient ownership, and a hard gate before anything is sent or signed.

## What it says up front

> Numeric Location panel inputs support repeatable placement when the document geometry and coordinate transform are verified. This skill describes field ownership, calibration and operator gates as a written workflow contract, not an executable browser controller or proof of browser enforcement.

## How it is structured

The skill's own section headings, in order:

- When to Use
- How It Works
  - Preconditions
  - Trusted browser target
  - Recipients
  - Calibration
  - Placing fields
  - Evidence
  - Hard gate
- Examples
  - Dry run for a new counterparty
  - Draft for operator review
  - Session expired
- Invariants to test

## What it bundles

- reference docs: `references/placement-checklist.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:esign-field-placement`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/esign-field-placement --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 70e193d68c2830593f48fd5ada721826d56da4922f86ae4a3fc9ce1552acf2c0 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
