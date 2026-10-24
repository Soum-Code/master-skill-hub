# hf-cloud-python-env-setup

> Set up an isolated Python environment for SageMaker / AWS work, with the right Python version and current boto3. Use this skill whenever Python code will be executed for a SageMaker deployment, training job, or any AWS automation — including when about to run `pip install`, when about to invoke `boto3`, when creating or activating a virtualenv, or when the user asks to "set up the environment". Never use system Python and never `pip install` into it. Always isolate. This skill prevents the most common failure modes: wrong Python version, dependency conflicts, and stale SDKs.

| | |
|---|---|
| **ID** | `huggingface/skills:hf-cloud-python-env-setup` |
| **Pack** | Claude / Skills / Plugin Tooling (also: MLOps / DevOps / Cloud, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 91 lines in SKILL.md, 4 file(s) |

## When to use it

- Use this skill whenever Python code will be executed for a SageMaker deployment, training job, or any AWS automation — including when about to run `pip install`, when about to invoke `boto3`, when creating or activating a virtualenv, or when the user asks to ".

## What it says up front

> Most SageMaker deployment failures that look like AWS problems are actually Python environment problems: wrong Python version, broken dependency resolution, stale SDK that doesn't know about a current API. This skill makes env setup boring and correct.

## How it is structured

The skill's own section headings, in order:

- Core rules
- boto3 vs the SageMaker SDK
- How to set up
- Verifying
- Deployment-specific extras
- Common pitfalls

## What it bundles

- scripts: `scripts/check_versions.py`, `scripts/setup_env.py`
- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [huggingface/skills:hf-cloud-serving-image-selection](huggingface-skills-hf-cloud-serving-image-selection.md) - Pick the right serving container for a SageMaker model deployment and find its current image URI. Use this ski
- [huggingface/skills:hf-cloud-sagemaker-iam-preflight](huggingface-skills-hf-cloud-sagemaker-iam-preflight.md) - Ensure a usable SageMaker execution role exists before deploying or training. Use this skill whenever about to
- [huggingface/skills:hf-cloud-sagemaker-deployment-planner](huggingface-skills-hf-cloud-sagemaker-deployment-planner.md) - Plan and coordinate the deployment of a model to Amazon SageMaker AI. Use this skill whenever the user wants t
- [microsoft/skills:microsoft-docs](microsoft-skills-microsoft-docs.md) - Understand Microsoft technologies by querying official documentation. Use whenever the user asks how something

## Invoke / install

- Invoke: `/huggingface/skills:hf-cloud-python-env-setup`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/hf-cloud-python-env-setup --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 877999d0bb95f6e32e6389cf97c5453d248059b4a22e8a5e9784f2daff9c7255 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
