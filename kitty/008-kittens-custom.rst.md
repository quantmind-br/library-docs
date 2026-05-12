---
title: Custom kittens
title: Custom kittens
word_count: 411
summary: This document explains how to create and configure custom kittens to extend the functionality of the kitty terminal emulator using Python.
category: tutorial
optimized: true
optimized_at: 2026-05-04T20:45:08Z
---
# Custom kittens

Kittens are terminal programs written in Python that extend kitty. When launched, kitty opens an overlay window over the current window and optionally passes the contents of the current window/scrollback to the kitten over STDIN. After execution, the kitten has access to the running kitty instance to perform arbitrary actions (closing windows, pasting text, etc.).

## Simple example

Create `~/.config/kitty/mykitten.py`:

```python
from kitty.boss import Boss

def main(args: list[str]) -> str:
    answer = input('Enter some text: ')
    return answer

def handle_result(args: list[str], answer: str, target_window_id: int, boss: Boss) -> None:
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        w.paste_text(answer)
```

Add to [[037-conf|kitty.conf]]:

```
map ctrl+k kitten mykitten.py
```

Press Ctrl+K to run. See the [kittens sub-directory](https://github.com/kovidgoyal/kitty/tree/master/kittens) in the kitty source for built-in examples. Also see [[010-kittens-developing-builtin-kittens|Developing builtin kittens]] (Go language) and [[008-kittens-custom|third-party kittens]].

## kitty API for kittens

Kittens have full access to internal kitty APIs (unstable/undocumented). Prefer the kitty [[028-remote-control|Remote control API]]:

```python
def handle_result(args, answer, target_window_id, boss):
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        boss.call_remote_control(w, ('send-text', f'--match=id:{w.id}', 'hello world'))
```

Run `kitten @ --help` to see all available remote control commands.

## Passing arguments

```
map ctrl+k kitten mykitten.py arg1 arg2
```

Arguments are available as `args` in `main()` and `handle_result()`. The special argument `@selection` is replaced by the currently selected text. The current working directory is set to the working directory of the program running in the active kitty window.

## Passing screen/scrollback contents to the kitten

```python
from kittens.tui.handler import result_handler

@result_handler(type_of_input='text')
def handle_result(args, stdin_data, target_window_id, boss):
    pass
```

`stdin_data` receives plain text of the active window. Available input types include: `screen`, `ansi`, `output` (last command output), `last_visited_output`, `first_output`. Shell integration is required for command-output-based types.

## Scripting kitty without terminal UI

Use `@result_handler(no_ui=True)` to run `handle_result()` without `main()`:

```python
from kittens.tui.handler import result_handler

@result_handler(no_ui=True)
def handle_result(args, answer, target_window_id, boss):
    tab = boss.active_tab
    if tab is not None:
        if tab.current_layout.name == 'stack':
            tab.last_used_layout()
        else:
            tab.goto_layout('stack')
```

## Sending mouse events

```python
from kitty.fast_data_types import send_mouse_event
send_mouse_event(screen, x, y, button, action, mods)
```

- `screen`: window's `screen` attribute
- `x`, `y`: 0-indexed coordinates
- `button`: X11 numbering (left:1, middle:2, right:3, scroll-up:4, scroll-down:5, scroll-left:6, scroll-right:7, back:8, forward:9)
- `action`: `PRESS`, `RELEASE`, `DRAG`, or `MOVE`
- `mods`: bitmask of `GLFW_MOD_SHIFT`, `GLFW_MOD_CONTROL`, `GLFW_MOD_ALT`
- Returns `True` if event was sent, `False` if not (program not receiving that event type)

Example — left click at x:2, y:3:

```python
from kitty.fast_data_types import send_mouse_event, PRESS
send_mouse_event(boss.active_window.screen, 2, 3, 1, PRESS, 0)
```

## Using remote control inside main()

Enable remote control for a kitten with `@kitten_ui(allow_remote_control=True)`:

```python
from kittens.tui.handler import kitten_ui

@kitten_ui(allow_remote_control=True)
def main(args):
    cp = main.remote_control(['ls'], capture_output=True)
    if cp.returncode != 0:
        sys.stderr.buffer.write(cp.stderr)
        raise SystemExit(cp.returncode)
    output = json.loads(cp.stdout)
    pprint(output)
    title = input('Enter the name of tab: ')
    main.remote_control(['launch', '--type=tab', '--tab-title', title], check=True)
```

Use `main.remote_control()` for subprocess commands (child processes cannot use remote control by default). Restrict to specific commands with `remote_control_password='ls set-colors'`. The password is available as `main.password` and is used automatically.

## Debugging kittens

- `main()` output — visible in the kitten window (print statements).
- `handle_result()` output — goes to kitty's STDOUT. Run kitty from another kitty instance to see it there.

```python
from kittens.tui.loop import debug
debug('whatever')  # like print(), but goes to kitty's STDOUT
```

## Third-party kittens

- [vim-kitty-navigator](https://github.com/knubie/vim-kitty-navigator) — navigate between vim and kitty splits with consistent hotkeys.
- [smart-scroll](https://github.com/yurikhan/kitty-smart-scroll) — kitty scroll bindings in full screen applications.
- [kitty-tab-switcher](https://github.com/OsiPog/kitty-tab-switcher) — fuzzy finder for kitty tabs with previews.
- [gattino](https://github.com/salvozappa/gattino) — integrate kitty with an LLM to convert plain language prompts into shell commands.
- [weechat-hints](https://github.com/GermainZ/kitty-weechat-hints) — URL hints for WeeChat without raw-mode.
