---
title: Extending the CLI | Hermes Agent
url: https://hermes-agent.nousresearch.com/docs/developer-guide/extending-the-cli
source: crawler
fetched_at: 2026-04-24T17:00:37.113641035-03:00
rendered_js: false
word_count: 371
summary: This document explains how to extend HermesCLI, a command-line interface, by utilizing protected hook points instead of overriding the main run() method. It details various extension seams like adding custom TUI widgets, defining keybindings, and processing commands.
tags:
    - hermescli
    - extension-hooks
    - tui-customization
    - wrapper-cli
    - keybinding-registration
    - command-processing
category: guide
---

Hermes exposes protected extension hooks on `HermesCLI` so wrapper CLIs can add widgets, keybindings, and layout customizations without overriding the 1000+ line `run()` method. This keeps your extension decoupled from internal changes.

## Extension points[​](#extension-points "Direct link to Extension points")

There are five extension seams available:

HookPurposeOverride when...`_get_extra_tui_widgets()`Inject widgets into the layoutYou need a persistent UI element (panel, status line, mini-player)`_register_extra_tui_keybindings(kb, *, input_area)`Add keyboard shortcutsYou need hotkeys (toggle panels, transport controls, modal shortcuts)`_build_tui_layout_children(**widgets)`Full control over widget orderingYou need to reorder or wrap existing widgets (rare)`process_command()`Add custom slash commandsYou need `/mycommand` handling (pre-existing hook)`_build_tui_style_dict()`Custom prompt\_toolkit stylesYou need custom colors or styling (pre-existing hook)

The first three are new protected hooks. The last two already existed.

## Quick start: a wrapper CLI[​](#quick-start-a-wrapper-cli "Direct link to Quick start: a wrapper CLI")

```python
#!/usr/bin/env python3
"""my_cli.py — Example wrapper CLI that extends Hermes."""

from cli import HermesCLI
from prompt_toolkit.layout import FormattedTextControl, Window
from prompt_toolkit.filters import Condition


classMyCLI(HermesCLI):

def__init__(self,**kwargs):
super().__init__(**kwargs)
        self._panel_visible =False

def_get_extra_tui_widgets(self):
"""Add a toggleable info panel above the status bar."""
        cli_ref = self
return[
            Window(
                FormattedTextControl(lambda:"📊 My custom panel content"),
                height=1,
filter=Condition(lambda: cli_ref._panel_visible),
),
]

def_register_extra_tui_keybindings(self, kb,*, input_area):
"""F2 toggles the custom panel."""
        cli_ref = self

@kb.add("f2")
def_toggle_panel(event):
            cli_ref._panel_visible =not cli_ref._panel_visible

defprocess_command(self, cmd:str)->bool:
"""Add a /panel slash command."""
if cmd.strip().lower()=="/panel":
            self._panel_visible =not self._panel_visible
            state ="visible"if self._panel_visible else"hidden"
print(f"Panel is now {state}")
returnTrue
returnsuper().process_command(cmd)


if __name__ =="__main__":
    cli = MyCLI()
    cli.run()
```

Run it:

```bash
cd ~/.hermes/hermes-agent
source .venv/bin/activate
python my_cli.py
```

## Hook reference[​](#hook-reference "Direct link to Hook reference")

Returns a list of prompt\_toolkit widgets to insert into the TUI layout. Widgets appear **between the spacer and the status bar** — above the input area but below the main output.

```python
def_get_extra_tui_widgets(self)->list:
return[]# default: no extra widgets
```

Each widget should be a prompt\_toolkit container (e.g., `Window`, `ConditionalContainer`, `HSplit`). Use `ConditionalContainer` or `filter=Condition(...)` to make widgets toggleable.

```python
from prompt_toolkit.layout import ConditionalContainer, Window, FormattedTextControl
from prompt_toolkit.filters import Condition

def_get_extra_tui_widgets(self):
return[
        ConditionalContainer(
            Window(FormattedTextControl("Status: connected"), height=1),
filter=Condition(lambda: self._show_status),
),
]
```

Called after Hermes registers its own keybindings and before the layout is built. Add your keybindings to `kb`.

```python
def_register_extra_tui_keybindings(self, kb,*, input_area):
pass# default: no extra keybindings
```

Parameters:

- **`kb`** — The `KeyBindings` instance for the prompt\_toolkit application
- **`input_area`** — The main `TextArea` widget, if you need to read or manipulate user input

```python
def_register_extra_tui_keybindings(self, kb,*, input_area):
    cli_ref = self

@kb.add("f3")
def_clear_input(event):
        input_area.text =""

@kb.add("f4")
def_insert_template(event):
        input_area.text ="/search "
```

**Avoid conflicts** with built-in keybindings: `Enter` (submit), `Escape Enter` (newline), `Ctrl-C` (interrupt), `Ctrl-D` (exit), `Tab` (auto-suggest accept). Function keys F2+ and Ctrl-combinations are generally safe.

### `_build_tui_layout_children(**widgets)`[​](#_build_tui_layout_childrenwidgets "Direct link to _build_tui_layout_childrenwidgets")

Override this only when you need full control over widget ordering. Most extensions should use `_get_extra_tui_widgets()` instead.

```python
def_build_tui_layout_children(self,*, sudo_widget, secret_widget,
    approval_widget, clarify_widget, spinner_widget, spacer,
    status_bar, input_rule_top, image_bar, input_area,
    input_rule_bot, voice_status_bar, completions_menu)->list:
```

The default implementation returns:

```python
[
    Window(height=0),# anchor
    sudo_widget,# sudo password prompt (conditional)
    secret_widget,# secret input prompt (conditional)
    approval_widget,# dangerous command approval (conditional)
    clarify_widget,# clarify question UI (conditional)
    spinner_widget,# thinking spinner (conditional)
    spacer,# fills remaining vertical space
*self._get_extra_tui_widgets(),# YOUR WIDGETS GO HERE
    status_bar,# model/token/context status line
    input_rule_top,# ─── border above input
    image_bar,# attached images indicator
    input_area,# user text input
    input_rule_bot,# ─── border below input
    voice_status_bar,# voice mode status (conditional)
    completions_menu,# autocomplete dropdown
]
```

## Layout diagram[​](#layout-diagram "Direct link to Layout diagram")

The default layout from top to bottom:

1. **Output area** — scrolling conversation history
2. **Spacer**
3. **Extra widgets** — from `_get_extra_tui_widgets()`
4. **Status bar** — model, context %, elapsed time
5. **Image bar** — attached image count
6. **Input area** — user prompt
7. **Voice status** — recording indicator
8. **Completions menu** — autocomplete suggestions

## Tips[​](#tips "Direct link to Tips")

- **Invalidate the display** after state changes: call `self._invalidate()` to trigger a prompt\_toolkit redraw.
- **Access agent state**: `self.agent`, `self.model`, `self.conversation_history` are all available.
- **Custom styles**: Override `_build_tui_style_dict()` and add entries for your custom style classes.
- **Slash commands**: Override `process_command()`, handle your commands, and call `super().process_command(cmd)` for everything else.
- **Don't override `run()`** unless absolutely necessary — the extension hooks exist specifically to avoid that coupling.