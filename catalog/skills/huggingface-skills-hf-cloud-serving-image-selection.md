# hf-cloud-serving-image-selection

> Pick the right serving container for a SageMaker model deployment and find its current image URI. Use this skill whenever about to deploy a model to a SageMaker endpoint and an image URI needs to be chosen — including when the user says "deploy this LLM", "host this HuggingFace model", "serve this fine-tuned model", "deploy this embedding model", "host a reranker", "serve a sentence-transformers model", or when about to hardcode any container URI in deployment code. HuggingFace-curated Deep Learning Containers are ALWAYS preferred: HuggingFace vLLM (LLMs and generative rerankers), HuggingFace vLLM-Omni (multimodal), TEI (embeddings/cross-encoder rerankers), HF Inference Toolkit (other transformers). Generic images (AWS vLLM, DJL-LMI, SGLang) are used only when no HuggingFace image is compatible — never merely because they carry a newer version. Never hardcode a container URI from memory and never default to TGI. Prevents stale-image failures and wrong-region URIs.

| | |
|---|---|
| **ID** | `huggingface/skills:hf-cloud-serving-image-selection` |
| **Pack** | AI / ML Engineering (also: MLOps / DevOps / Cloud) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 221 lines in SKILL.md, 3 file(s) |

## When to use it

- Use this skill whenever about to deploy a model to a SageMaker endpoint and an image URI needs to be chosen — including when the user says "deploy this LLM", "host this HuggingFace model", "serve this fine-tuned model", "deploy this embedding model", "host a r.

## What it says up front

> The serving container is the single thing most likely to break a SageMaker deployment that "looked correct on paper". Wrong container, stale tag, or the wrong AMI — all produce the same opaque `Failed to pass health check` error.

## How it is structured

The skill's own section headings, in order:

- Rule zero: HuggingFace images always win
- Where image URIs come from
- Quick decision
- Rerankers: TEI or vLLM?
- Workflow
  - TEI: pick the right variant
- vLLM AMI requirement
- Configuring the vLLM DLCs (HuggingFace vLLM and AWS vLLM)
  - Required for every HuggingFace LLM deployment
  - Tuning (optional)
- Configuring TEI
- CUDA / instance compatibility
- VPC / NAT gateway problem
- When the catalog page won't render, is stale, or is wrong
- Known-broken images (last checked July 2026)
- Hub download time at first boot

## What it bundles

- scripts: `scripts/mirror_image.py`
- reference docs: `references/model-to-image.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [huggingface/skills:hf-cloud-sagemaker-deployment-planner](huggingface-skills-hf-cloud-sagemaker-deployment-planner.md) - Plan and coordinate the deployment of a model to Amazon SageMaker AI. Use this skill whenever the user wants t
- [huggingface/skills:hf-cloud-python-env-setup](huggingface-skills-hf-cloud-python-env-setup.md) - Set up an isolated Python environment for SageMaker / AWS work, with the right Python version and current boto
- [huggingface/skills:hf-cloud-sagemaker-iam-preflight](huggingface-skills-hf-cloud-sagemaker-iam-preflight.md) - Ensure a usable SageMaker execution role exists before deploying or training. Use this skill whenever about to

## Invoke / install

- Invoke: `/huggingface/skills:hf-cloud-serving-image-selection`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/hf-cloud-serving-image-selection --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree a840778db25c420e3a24c2486e1620ffe817745df0c7e86daef26a1e3fe34027 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
