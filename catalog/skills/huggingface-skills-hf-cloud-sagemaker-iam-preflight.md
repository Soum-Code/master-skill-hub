# hf-cloud-sagemaker-iam-preflight

> Ensure a usable SageMaker execution role exists before deploying or training. Use this skill whenever about to create a SageMaker endpoint, model, training job, or any resource that requires an execution role. Use it especially when the user has not provided a role ARN explicitly, when scripts are about to call `iam:CreateRole`, or when an AccessDenied error mentions an IAM action. Never blindly call `iam:CreateRole` — always check for existing roles first. This skill prevents the most common SageMaker deployment failure: trying to create IAM resources from an SSO principal that has no IAM write permissions.

| | |
|---|---|
| **ID** | `huggingface/skills:hf-cloud-sagemaker-iam-preflight` |
| **Pack** | MLOps / DevOps / Cloud |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 103 lines in SKILL.md, 5 file(s) |

## When to use it

- Use this skill whenever about to create a SageMaker endpoint, model, training job, or any resource that requires an execution role.
- Use it especially when the user has not provided a role ARN explicitly, when scripts are about to call `iam:CreateRole`, or when an AccessDenied error mentions an IAM action.

## What it says up front

> Every SageMaker resource needs an **execution role** — the IAM role SageMaker assumes to read model artifacts from S3, pull serving containers from ECR, and write logs. Most deployments fail here because the script tried to create a new role without checking if a usable one already existed, then ble

## How it is structured

The skill's own section headings, in order:

- Running the helpers (cross-platform)
- Order of operations
  - Step 1 — Did the user provide a role?
  - Step 2 — Discover existing roles
  - Step 3 — Create, only if discovery found nothing
- What "validated" means
- Minimum permissions
- Native AWS CLI equivalent (fallback)

## What it bundles

- scripts: `scripts/check_role.py`, `scripts/create_role.py`
- reference docs: `references/minimum-permissions.json`, `references/trust-policy.json`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [huggingface/skills:hf-cloud-python-env-setup](huggingface-skills-hf-cloud-python-env-setup.md) - Set up an isolated Python environment for SageMaker / AWS work, with the right Python version and current boto
- [huggingface/skills:hf-cloud-serving-image-selection](huggingface-skills-hf-cloud-serving-image-selection.md) - Pick the right serving container for a SageMaker model deployment and find its current image URI. Use this ski
- [huggingface/skills:hf-cloud-sagemaker-deployment-planner](huggingface-skills-hf-cloud-sagemaker-deployment-planner.md) - Plan and coordinate the deployment of a model to Amazon SageMaker AI. Use this skill whenever the user wants t

## Invoke / install

- Invoke: `/huggingface/skills:hf-cloud-sagemaker-iam-preflight`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/hf-cloud-sagemaker-iam-preflight --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree ead6432fdfb309127912035047c51cbc9dd662000111738716de485c294ea932 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
