# huggingface-datasets

> Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-datasets` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 108 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters, download parquet URLs, and read size or statistics.

## What it says up front

> Use this skill to execute read-only Dataset Viewer API calls for dataset exploration and extraction.

## How it is structured

The skill's own section headings, in order:

- Core workflow
- Defaults
- Dataset Viewer
- Creating and Uploading Datasets
- Agent Traces

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-papers](huggingface-skills-huggingface-papers.md) - Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as 
- [huggingface/skills:huggingface-tool-builder](huggingface-skills-huggingface-tool-builder.md) - Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging F
- [huggingface/skills:hf-mcp](huggingface-skills-hf-mcp.md) - Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch do

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-datasets`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-datasets --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 46ab85d02e37eb68cdf6eee40b8fcb365f28e73f368184ca07a667fddea42dec --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
