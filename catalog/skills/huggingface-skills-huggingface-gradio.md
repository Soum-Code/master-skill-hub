# huggingface-gradio

> Build Gradio web UIs and demos in Python. Use when creating or editing Gradio apps, components, event listeners, layouts, or chatbots.

| | |
|---|---|
| **ID** | `huggingface/skills:huggingface-gradio` |
| **Pack** | AI / ML Engineering (also: Browser & Web Automation, Documents, Writing & Content, Software Development) |
| **Kind** | skill |
| **Status** | verified (vetted at pinned commit) |
| **Origin** | [huggingface/skills](https://github.com/huggingface/skills) |
| **License** | Apache-2.0 |
| **Size** | 299 lines in SKILL.md, 2 file(s) |

## When to use it

- Use when creating or editing Gradio apps, components, event listeners, layouts, or chatbots.

## What it says up front

> Gradio is a Python library for building interactive web UIs and ML demos. This skill covers the core API, patterns, and examples.

## How it is structured

The skill's own section headings, in order:

- Guides
- Core Patterns
- Key Component Signatures
  - `Textbox(value: str \| I18nData \| Callable \| None = None, type: Literal['text', 'password',
  - `Number(value: float \| Callable \| None = None, label: str \| I18nData \| None = None, placeh
  - `Slider(minimum: float = 0, maximum: float = 100, value: float \| Callable \| None = None, s
  - `Checkbox(value: bool \| Callable = False, label: str \| I18nData \| None = None, info: str \|
  - `Dropdown(choices: Sequence[str \| int \| float \| tuple[str, str \| int \| float]] \| None = No
  - `Radio(choices: Sequence[str \| int \| float \| tuple[str, str \| int \| float]] \| None = None,
  - `Image(value: str \| PIL.Image.Image \| np.ndarray \| Callable \| None = None, format: str = "
  - `Audio(value: str \| Path \| tuple[int, np.ndarray] \| Callable \| None = None, sources: list[
  - `Video(value: str \| Path \| Callable \| None = None, format: str \| None = None, sources: lis
  - `File(value: str \| list[str] \| Callable \| None = None, file_count: Literal['single', 'mult
  - `Chatbot(value: list[MessageDict \| Message] \| Callable \| None = None, label: str \| I18nDat
  - `Button(value: str \| I18nData \| Callable = "Run", every: Timer \| float \| None = None, inpu
  - `Markdown(value: str \| I18nData \| Callable \| None = None, label: str \| I18nData \| None = N
  - `HTML(value: Any \| Callable \| None = None, label: str \| I18nData \| None = None, html_templ
- Custom HTML Components
- Event Listeners
- Prediction CLI
  - `gradio info` — Discover endpoints and parameters
  - `gradio predict` — Send predictions
- Additional Reference

## What it bundles

- 1 other file(s)

## Permissions and risk notes

- Declares no pre-approved tools; Claude asks as usual.

## Related skills

- [huggingface/skills:huggingface-spaces](huggingface-skills-huggingface-spaces.md) - Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and d

## Invoke / install

- Invoke: `/huggingface/skills:huggingface-gradio`
- Install: `python skills/skill-vetter/scripts/install.py huggingface/skills --path skills/huggingface-gradio --commit fabc634a893f62ad5c2039830397efa35fa62715 --expect-tree 214bf2cd5104ee4202b9084cbd780da062dd1a501fbd25c4905f1ebbb466d4dc --apply`

---
_Generated from the skill's own metadata by [master-skill-hub](https://github.com/Soum-Code/master-skill-hub). Nothing here is hand-written opinion._
