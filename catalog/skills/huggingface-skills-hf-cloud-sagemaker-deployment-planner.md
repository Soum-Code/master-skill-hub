# hf-cloud-sagemaker-deployment-planner

> Plan and coordinate the deployment of a model to Amazon SageMaker AI. Use this skill whenever the user wants to deploy, host, serve, or expose a model on SageMaker or AWS — including phrases like "deploy a model", "host this LLM on AWS", "serve this embedding model", "deploy a reranker", "deploy a text-to-image / diffusion model", "host this for async inference", "create an endpoint", "serve my fine-tuned model", or any request that involves making a model available for inference on AWS. Use this even when the user is vague (e.g. "I just want to get this running on AWS, you figure it out"). Works for text-generation LLMs, embedding models, rerankers, classifiers, text-to-image / diffusion models — picks the right serving stack and chooses between real-time and async inference. This is the entry-point skill for SageMaker deployment work — it asks clarifying questions, picks a deployment pathway, and coordinates the other deployment skills.

| | |
|---|---|
| **ID** | `huggingface/skills:hf-cloud-sagemaker-deployment-planner` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 91 lines in SKILL.md, 1 file(s) |

## When to use it

- Use this skill whenever the user wants to deploy, host, serve, or expose a model on SageMaker or AWS — including phrases like "deploy a model", "host this LLM on AWS", "serve this embedding model", "deploy a reranker", "deploy a text-to-image / diffusion model.

## What it says up front

> You are helping a user deploy a model to Amazon SageMaker. Most users invoking this skill want the model deployed with reasonable defaults, in as few questions as possible. Ask only what you need, recommend a pathway honestly, and hand off to the specialized skills.

## How it is structured

The skill's own section headings, in order:

- Workflow phases
- Discovery: ask only what you need
- Pathway selection
- Instance selection: check quota before recommending
- Style

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:hf-cloud-serving-image-selection](huggingface-skills-hf-cloud-serving-image-selection.md) - Pick the right serving container for a SageMaker model deployment and find its current image URI. Use this ski
- [huggingface/skills:hf-cloud-python-env-setup](huggingface-skills-hf-cloud-python-env-setup.md) - Set up an isolated Python environment for SageMaker / AWS work, with the right Python version and current boto
- [huggingface/skills:hf-cloud-sagemaker-iam-preflight](huggingface-skills-hf-cloud-sagemaker-iam-preflight.md) - Ensure a usable SageMaker execution role exists before deploying or training. Use this skill whenever about to
- [anthropics/claude-plugins-official:build-mcp-server](anthropics-claude-plugins-official-build-mcp-server.md) - This skill should be used when the user asks to "build an MCP server", "create an MCP", "make an MCP integrati

## Invoke / install

- Invoke: `/huggingface/skills:hf-cloud-sagemaker-deployment-planner`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/hf-cloud-sagemaker-deployment-planner --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 8a0a269f31487fe45447621d73c11f3a3900e57c49e4aa348d90737723596dd2 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
