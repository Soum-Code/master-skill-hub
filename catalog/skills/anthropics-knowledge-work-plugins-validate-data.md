# validate-data

> QA an analysis before sharing -- methodology, accuracy, and bias checks. Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

| | |
|---|---|
| **ID** | `anthropics/knowledge-work-plugins:validate-data` |
| **Pack** | Data & Analytics |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) |
| **License** | Apache-2.0 |
| **Size** | 384 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when reviewing an analysis before a stakeholder presentation, spot-checking calculations and aggregation logic, verifying a SQL query's results look right, or assessing whether conclusions are actually supported by the data.

## What it says up front

> Review an analysis for accuracy, methodology, and potential biases before sharing with stakeholders. Generates a confidence assessment and improvement suggestions.

## How it is structured

The skill's own section headings, in order:

- Usage
- Workflow
  - 1. Review Methodology and Assumptions
  - 2. Run the Pre-Delivery QA Checklist
  - 3. Check for Common Analytical Pitfalls
  - 4. Verify Calculations and Aggregations
  - 5. Assess Visualizations
  - 6. Evaluate Narrative and Conclusions
  - 7. Suggest Improvements
  - 8. Generate Confidence Assessment
- Output Format
- Pre-Delivery QA Checklist
  - Data Quality Checks
  - Calculation Checks
  - Reasonableness Checks
  - Presentation Checks
- Common Data Analysis Pitfalls
  - Join Explosion
  - Survivorship Bias
  - Incomplete Period Comparison
  - Denominator Shifting
  - Average of Averages
  - Timezone Mismatches
  - Selection Bias in Segmentation
  - Other Statistical Traps
- Result Sanity Checking
  - Magnitude Checks
  - Cross-Validation Techniques
  - Red Flags That Warrant Investigation
- Documentation Standards for Reproducibility

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/anthropics/knowledge-work-plugins:validate-data`
- Install: `python skills/skill-vetter/scripts/install.py anthropics/knowledge-work-plugins --path data/skills/validate-data --commit 33d3dea41a341b341d4f5da2e8801ae0c89be2b8 --expect-tree f51b13d3a8309f6fe143116fbdbc7785a9413df717acf64c5bea912fa6329486 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
