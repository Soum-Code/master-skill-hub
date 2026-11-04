# openclaw-persona-forge

> 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创建、设计或定制 OpenClaw 龙虾灵魂时使用。 不适用于：微调已有 SOUL.md、非 OpenClaw 平台的角色设计、纯工具型无性格 Agent。 触发词：龙虾灵魂、虾魂、OpenClaw 灵魂、养虾灵魂、龙虾角色、龙虾定位、 龙虾剧本杀角色、龙虾游戏角色、龙虾 NPC、龙虾性格、龙虾背景故事、 lobster soul、lobster character、抽卡、随机龙虾、龙虾 SOUL、gacha。 Use when creating, designing, or customizing an OpenClaw lobster persona — identity, SOUL.md, name, or avatar prompt.

| | |
|---|---|
| **ID** | `affaan-m/ECC:openclaw-persona-forge` |
| **Pack** | AI / ML Engineering |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 290 lines in SKILL.md, 9 file(s) |

## When to use it

- 为 OpenClaw AI Agent 锻造完整的龙虾灵魂方案。根据用户偏好或随机抽卡， 输出身份定位、灵魂描述(SOUL.md)、角色化底线规则、名字和头像生图提示词。 如当前环境提供已审核的生图 skill，可自动生成统一风格头像图片。 当用户需要创建、设计或定制 OpenClaw 龙虾灵魂时使用。 不适用于：微调已有 SOUL.md、非 OpenClaw 平台的角色设计、纯工具型无性格 Agent。 触发词：龙虾灵魂、虾魂、OpenClaw 灵魂、养虾灵魂、龙虾角色、龙虾定位、 龙虾剧本杀角色、龙虾游戏角色、.

## What it says up front

> 2. Replace all `${SKILL_DIR}` in this document with the actual path

## How it is structured

The skill's own section headings, in order:

- When to Use
  - Avoid when
- 前置条件
- Skill 目录约定
- 内置工具
  - 抽卡引擎（gacha.py）
- 可选依赖
  - 头像自动生图：可选生图 skill
- 核心理念
- How It Works
  - 触发判断
- Step 1：选方向（引导模式）
- Step 1-B：抽卡模式
- Step 2：锻造身份张力
- Step 3：推导底线规则
- Step 4：锻造名字
- Step 5：生成头像
  - 流程
- Step 6：输出完整方案 & 生成文件
- 对话语气指南
  - 原则
  - 各步骤的语气参考（不要照抄，每次变化）
- Examples
- 错误处理
- 注意事项
  - 好灵魂的检验标准
  - 避坑
  - 何时重新调整灵魂
- 兼容性

## What it bundles

- scripts: `gacha.py`, `gacha.sh`
- reference docs: `references/avatar-style.md`, `references/boundary-rules.md`, `references/error-handling.md`, `references/identity-tension.md`, `references/naming-system.md`, `references/output-template.md`

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.
- Ships executable scripts. Review them before trusting the skill outside its trusted source.

## Related skills

- [microsoft/skills:skill-creator](microsoft-skills-skill-creator.md) - Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry service

## Invoke / install

- Invoke: `/affaan-m/ECC:openclaw-persona-forge`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/openclaw-persona-forge --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree e4f3a59365021d103c50ece46d3957c6d1d7f2e091477d03c0a23d9ce06770ef --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
