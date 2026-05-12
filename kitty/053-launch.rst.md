---
title: The launch command
title: The launch command
word_count: 284
summary: kitty's launch action for running programs in new windows/tabs with powerful options for stdin, cwd, and watchers.
category: reference
optimized: true
optimized_at: 2026-05-04T20:46:03Z
---
# The launch command

kitty's launch action runs arbitrary programs in new windows/tabs, mapped in [[037-conf|kitty.conf]]. Supports sending screen/scrollback content to the launched program.

## Basic usage

```
map f1 launch                    # Open new window with shell
map f1 launch vim path/to/file   # Run vim
map f1 launch --cwd=current      # Same working directory as current window
map f1 launch --type=tab        # Open in new tab
map f1 launch sh -c "ls && exec zsh"  # Multiple commands
map f1 launch --stdin-source=@screen_scrollback less  # Pass screen+scrollback
```

> [!tip]
> Use [[042-actions|action_alias]] to avoid duplicating launch actions:
> ```
> action_alias launch_tab launch --cwd=current --type=tab
> map f1 launch_tab vim
> map f2 launch_tab emacs
> ```

## The piping environment

When using `launch --stdin-source`, the program receives `KITTY_PIPE_DATA`:

```
KITTY_PIPE_DATA={scrolled_by}:{cursor_x},{cursor_y}:{lines},{columns}
```

| Variable | Meaning |
|----------|---------|
| `scrolled_by` | Lines kitty is currently scrolled |
| `cursor_(x\|y)` | Cursor position (1,1 = top-left) |
| `lines,columns` | Screen dimensions |

## Special placeholder arguments

| Placeholder | Replaced with |
|-------------|---------------|
| `@selection` | Currently selected text |
| `@active-kitty-window-id` | ID of active kitty window |
| `@line-count` | Lines in STDIN (when passing data) |
| `@input-line-number` | Lines pager should scroll (see scrollback_pager) |
| `@scrolled-by` | Current scroll offset |
| `@cursor-x` | Cursor x position (1 = leftmost) |
| `@cursor-y` | Cursor y position (1 = topmost) |
| `@first-line-on-screen` | First visible line |
| `@last-line-on-screen` | Last visible line |

```
map f1 launch my-program @active-kitty-window-id
```

## Watching launched windows

`launch --watcher` specifies Python functions called on window events. Also configurable globally via [[028-remote-control|watcher]].

```python
# ~/.config/kitty/mywatcher.py
from typing import Any
from kitty.boss import Boss
from kitty.window import Window

def on_load(boss: Boss, data: dict[str, Any]) -> None:
    """Called once when watcher module is first loaded."""
    ...

def on_resize(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called on resize; data contains old_geometry, new_geometry.
    First resize has zeroed old_geometry (xnum/ynum = 0)."""
    ...

def on_focus_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called on focus; data contains focused."""
    ...

def on_close(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called when window closes (program exits)."""
    ...

def on_set_user_var(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called when user variable set/deleted; data contains key, value."""
    ...

def on_title_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called on title change; data contains title, from_child.
    from_child=True when set via escape code from terminal program."""
    ...

def on_cmd_startstop(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called when shell starts/stops command; data contains
    is_start, cmdline, time."""
    ...

def on_color_scheme_preference_change(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called on light/dark preference change; data contains
    is_dark, via_escape_code."""
    ...

def on_tab_bar_dirty(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called on tab bar changes (new tabs, title changes, moves).
    Global watchers only. data contains tab_manager."""
    ...

def on_quit(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    """Called before quit dialog (data['confirmed']=False),
    then after confirmation (data['confirmed']=True).
    Set data['aborted']=True to abort quit. Global watchers only."""
    ...
```

Every callback receives `Boss` (global) and `Window` objects. Use [[028-remote-control|kitty RC API]] for most tasks:

```python
def on_resize(boss: Boss, window: Window, data: dict[str, Any]) -> None:
    boss.call_remote_control(window, ('send-text', f'--match=id:{window.id}', 'hello world'))
```

Run `kitten @ --help` for all available remote control commands.

## Finding executables

Commands specified by name (not absolute path) are searched in:
1. System PATH environment variable
2. System-specific default paths
3. Shell's PATH (if not found above)

> [!note]
> Shell startup scripts often modify PATH — the value may differ from system PATH.

See [[037-conf|exe_search_path]] for details.

#terminal-emulator #command-line-automation #window-management #python-scripting
