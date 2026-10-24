# huggingface-vision-trainer

> Trains and fine-tunes vision models for object detection (D-FINE, RT-DETR v2, DETR, YOLOS), image classification (timm models — MobileNetV3, MobileViT, ResNet, ViT/DINOv3 — plus any Transformers classifier), and SAM/SAM2 segmentation using Hugging Face Transformers on Hugging Face Jobs cloud GPUs. Covers COCO-format dataset preparation, Albumentations augmentation, mAP/mAR evaluation, accuracy metrics, SAM segmentation with bbox/point prompts, DiceCE loss, hardware selection, cost estimation, Trackio monitoring, and Hub persistence. Use when users mention training object detection, image classification, SAM, SAM2, segmentation, image matting, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, bounding box models, or fine-tuning vision models on Hugging Face Jobs.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-vision-trainer` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 594 lines in SKILL.md, 12 file(s) |

## When to use it

- Use when users mention training object detection, image classification, SAM, SAM2, segmentation, image matting, DETR, D-FINE, RT-DETR, ViT, timm, MobileNet, ResNet, bounding box models, or fine-tuning vision models on Hugging Face Jobs.

## What it says up front

> Train object detection, image classification, and SAM/SAM2 segmentation models on managed cloud GPUs. No local GPU setup required—results are automatically saved to the Hugging Face Hub.

## How it is structured

The skill's own section headings, in order:

- When to Use This Skill
- Related Skills
- Local Script Execution
- Prerequisites Checklist
  - Account & Authentication
  - Dataset Requirements — Object Detection
  - Dataset Requirements — Image Classification
  - Dataset Requirements — SAM/SAM2 Segmentation
  - Critical Settings
- Dataset Validation
  - Running the Inspector
  - Reading Results
- Automatic Bbox Preprocessing
- Training workflow
- Critical directives
  - 1. Job submission: `hf_jobs` MCP tool vs Python API
  - 2. Authentication via job secrets + explicit hub_token injection
  - 3. JobInfo attribute
  - 4. Required training flags and HfArgumentParser boolean syntax
  - 5. Timeout management
  - 6. Trackio monitoring
- Model & hardware selection
  - Recommended object detection models
  - Recommended image classification models
  - Recommended SAM/SAM2 segmentation models
  - Hardware recommendation
- Quick start — Object Detection
  - Key OD `script_args`
- Quick start — Image Classification
  - Key IC `script_args`

## What it bundles

- scripts: `scripts/dataset_inspector.py`, `scripts/estimate_cost.py`, `scripts/image_classification_training.py`, `scripts/object_detection_training.py`, `scripts/sam_segmentation_training.py`
- reference docs: `references/finetune_sam2_trainer.md`, `references/hub_saving.md`, `references/image_classification_training_notebook.md`, `references/object_detection_training_notebook.md`, `references/reliability_principles.md`, `references/timm_trainer.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [huggingface/skills:huggingface-community-evals](huggingface-skills-huggingface-community-evals.md) - Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend 
- [huggingface/skills:transformers-js](huggingface-skills-transformers-js.md) - Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript. Support

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-vision-trainer`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-vision-trainer --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 48f968b81e8a7b26023268a4943cc25ff83d03e0f8f9f25f9e28da3571864e95 --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
