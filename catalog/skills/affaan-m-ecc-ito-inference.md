# ito-inference

> Inspect the availability of model serving on a completed Itô compute booking and, when the canonical backend becomes available, hand off an explicitly confirmed serving manifest. Use after ito-compute has booked GPU nodes and the user asks for an OpenAI-compatible endpoint, ito-serve, hosted Kimi, or self-hosted open-weights inference. ECC implements no serving stack of its own.

| | |
|---|---|
| **ID** | `affaan-m/ECC:ito-inference` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 120 lines in SKILL.md, 1 file(s) |

## When to use it

- The description above is the trigger. It does not spell out extra conditions.

## What it says up front

> `ito-inference` is the sole canonical ECC skill for inference serving on Itô compute. Requests naming `ito-serve` route here; do not create or install a second `ito-serve` skill. ECC never SSHes to nodes, downloads weights, launches an engine, or exposes an endpoint; it never books, reserves, or spe

## How it is structured

The skill's own section headings, in order:

- Current production boundary
- Required entitlement
- Future CLI and API contract
- Confirmation and execution gates
- Lifecycle and recovery
- Proposed backend stages

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [affaan-m/ECC:ito-training](affaan-m-ecc-ito-training.md) - Inspect the availability of ML training on a completed Itô compute booking and, when the canonical backend bec
- [affaan-m/ECC:ito-compute](affaan-m-ecc-ito-compute.md) - Query live GPU inventory, submit an authenticated Itô fixed-rate RFQ, inspect RFQ or procurement status, revok
- [huggingface/skills:hf-cloud-sagemaker-deployment-planner](huggingface-skills-hf-cloud-sagemaker-deployment-planner.md) - Plan and coordinate the deployment of a model to Amazon SageMaker AI. Use this skill whenever the user wants t

## Invoke / install

- Invoke: `/affaan-m/ECC:ito-inference`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/ito-inference --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 00c1e81becef433ea746ca326981263f59df8a34b9eea8422c960742b34308ea --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
