# generating-python-installer

> Commercial-grade Python installer expert for Windows: Nuitka extreme compilation, dist slimming, DLL footprint analysis, and Inno Setup packaging to ship the smallest, fastest installers. Use when a Python app must ship as a minimal, fast-starting Windows installer; not for basic script-to-exe conversion. 中文触发：Nuitka 极限优化、Python 商业打包、极限编译 Python、dist 瘦身、DLL 分析、最小安装包、最快启动、商业级打包风格

| | |
|---|---|
| **ID** | `affaan-m/ECC:generating-python-installer` |
| **Pack** | Software Development (also: Spec-driven Dev Workflow) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [affaan-m/ECC](https://github.com/affaan-m/ECC) |
| **License** | MIT |
| **Size** | 821 lines in SKILL.md, 1 file(s) |

## When to use it

- Use when a Python app must ship as a minimal, fast-starting Windows installer; not for basic script-to-exe conversion.

## What it says up front

> You are a **Python commercial deployment expert**. Your goal is the **smallest, fastest-starting, cleanest** Windows installer. The core approach is **"Nuitka folder mode (dist) + Inno Setup packaging"** — no single-file builds, no stray console window.

## How it is structured

The skill's own section headings, in order:

- When to Activate
- How It Works
- Examples
- 核心理念
- 实战参考案例（生产级 PySide2 桌面应用，323 MB，含 OpenCV / Playwright）
  - 项目概况
  - 关键优化策略
  - 体积分布
  - 预期效果对比
- 核心工作流 (Workflow) - WARNING: 严格执行
- Nuitka 极限优化编译（基于 参考项目经验）
  - 一、32 位 vs 64 位选择策略
  - 二、模块排除清单（参考项目验证过的）
  - 三、GUI 框架专用优化
  - 四、一键编译脚本模板
  - 五、dist 瘦身脚本（参考项目级别清理）
  - 六、DLL 依赖分析工具
- 完整优化工作流
  - 步骤 1：修改编译脚本配置
  - 步骤 2：一键编译+瘦身
  - 步骤 3：分析 DLL 依赖
  - 步骤 4：根据分析结果优化
- VC++ 运行库处理方案
  - 方案一：静态链接（推荐）
  - 方案二：捆绑运行库安装（商业发布推荐）
- Inno Setup 脚本模板（商业终极版）
- 占位符说明
- 常见问题 (FAQ)
  - Q1: 安装后双击程序无反应？
  - Q2: 安装包体积过大？

## What it bundles

- Just the SKILL.md (instructions only, no scripts).

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Invoke / install

- Invoke: `/affaan-m/ECC:generating-python-installer`
- Install: `python skills/skill-vetter/scripts/install.py affaan-m/ECC --path skills/generating-python-installer --commit b38be6a7f6350964d59328b52f0624e1d1d552d1 --expect-tree 47c20b1194cd325a81295a59d7ec5b52448582f4f2afaf8d78f5f60bd97abd8c --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
