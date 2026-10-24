# instrument-data-to-allotrope

> Convert laboratory instrument output files (PDF, CSV, Excel, TXT) to Allotrope Simple Model (ASM) JSON format or flattened 2D CSV. Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis. Supports auto-detection of instrument types. Outputs include full ASM JSON, flattened CSV for easy import, and exportable Python code for data engineers. Common triggers include converting instrument files, standardizing lab data, preparing data for upload to LIMS/ELN systems, or generating parser code for production pipelines.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:instrument-data-to-allotrope` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 281 lines in SKILL.md, 11 file(s) |

## When to use it

- Use this skill when scientists need to standardize instrument data for LIMS systems, data lakes, or downstream analysis.

## What it says up front

> Convert instrument files into standardized Allotrope Simple Model (ASM) format for LIMS upload, data lakes, or handoff to data engineering teams.

## How it is structured

The skill's own section headings, in order:

- Workflow Overview
- Quick Start
- Output Format Selection
- Calculated Data Handling
- Validation
- Supported Instruments
- Detection & Parsing Strategy
  - Tier 1: Native allotropy parsing (PREFERRED)
  - Tier 2: Flexible fallback parsing
  - Tier 3: PDF extraction
- Pre-Parsing Checklist
- Common Mistakes to Avoid
- Code Export for Data Engineers
- File Structure
- Usage Examples
  - Example 1: Vi-CELL BLU file
  - Example 2: Request for code handoff
  - Example 3: LIMS-ready flattened output
- Implementation Notes
  - Installing allotropy
  - Handling parse failures
  - ASM Schema Validation

## What it bundles

- scripts: `scripts/convert_to_asm.py`, `scripts/export_parser.py`, `scripts/flatten_asm.py`, `scripts/validate_asm.py`
- reference docs: `references/asm_schema_overview.md`, `references/field_classification_guide.md`, `references/flattening_guide.md`, `references/supported_instruments.md`
- 2 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [anthropic-skills:xlsx](anthropic-skills-xlsx.md) - Use this skill any time a spreadsheet file is the primary input or output. This means any task where the user 

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:instrument-data-to-allotrope`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path bio-research/skills/instrument-data-to-allotrope --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree 0a337ec574f907fc001b06633f4110506bd55eb407b039e8190d7d55c45fe410 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
