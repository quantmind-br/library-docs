---
title: Sessions
url: https://github.com/kovidgoyal/kitty/blob/master/docs/sessions.rst
source: git
fetched_at: 2026-05-04T15:58:28.392658299-03:00
rendered_js: false
word_count: 543
summary: Configure and manage kitty sessions — window layouts, startup programs, keybindings to switch between projects, and the save_as_session action.
tags:
    - kitty
    - terminal-emulator
    - session-management
    - window-layout
    - productivity
    - terminal-automation
category: guide
optimized: true
optimized_at: 2026-05-04T20:30:00Z
---
# Sessions

A session is a text file defining kitty windows, tabs, layouts, and programs. Use `goto_session` to switch between sessions with keystrokes.

## Quick example

Create `~/path/to/myproject/launch.kitty-session`:

```session
layout tall
cd ~/path/to/myproject
launch --title "Edit My Project" /usr/bin/nvim
launch --title "Build My Project"
launch --title "Log for my project" /usr/bin/tail -f /path/to/project/log/file
```

Launch it:

```bash
kitty --session ~/path/to/myproject/launch.kitty-session
```

Or set via `startup_session` in `kitty.conf`.

## Switch sessions with a keypress

```conf
map f7>c goto_session ~/path/to/cool/cool.kitty-session
map f7>h goto_session ~/path/to/hot/hot.kitty-session
map f7>/ goto_session
map f7>/ goto_session --active-only
map f7>/ goto_session --sort-by=alphabetical
map f7>p goto_session ~/.local/share/kitty/sessions
map f7>- goto_session -1  # go to previous session
```

When a directory path is supplied, kitty scans for `.kitty-session`, `.kitty_session`, or `.session` files. Use `close_session` to close all windows in a session with one key.

## Display session name in tab bar

```conf
tab_title_template {session_name} {title}
```

Or set the tab title directly in the session file:

```
new_tab My Project Name
```

## Complex sessions

Set up manually, then save with a key:

```bash
kitty -o 'map f1 save_as_session --use-foreground-process --relocatable'
```

Create your layout, press F1, enter a path — the session file is saved and opened in your editor.

> [!tip]
> Save to a specific directory regardless of CWD:
> ```conf
> map f7>s save_as_session --use-foreground-process --base-dir ~/.local/share/kitty/sessions
> ```
> Omit `--relocatable` when using `--base-dir`.

### Session file reference

```session
# Layout and directory
layout tall
cd ~

# Launch windows
launch zsh
launch --env FOO=BAR vim
launch --title "Chat with x" irssi --profile x
launch --hold message-of-the-day

# Tabs
new_tab my tab
enabled_layouts tall,stack
layout stack
launch zsh

# OS Windows
new_os_window
os_window_size 80c 24c
os_window_title my fancy os window
os_window_class mywindow
os_window_name myname
os_window_state normal
launch sh
resize_window wider 2
focus
focus_os_window
launch emacs

# Another tab
new_tab logs
launch tail -f /var/log/syslog
focus_tab 0

# Complex layout (splits)
new_tab complex tab
layout splits
launch --var window=first
launch --location=vsplit
launch --location=hsplit --bias=40
focus_matching_window var:window=first
launch --location=hsplit
```

> [!NOTE]
> `launch` in session files cannot create OS windows or tabs — use the dedicated keywords.

> [!NOTE]
> `${NAME}` and `$NAME` env vars are expanded in session files, except in `launch` arguments.

## New windows join existing session

```conf
map kitty_mod+enter new_window_with_cwd
map kitty_mod+t new_tab_with_cwd
map kitty_mod+n new_os_window_with_cwd
```

Update the session file:

```conf
map f5 save_as_session --relocatable --use-foreground-process --match=session:. .
```

Or use `launch --add-to-session` for finer control.

## Sessions with remote connections

When using the ssh kitten, `save_as_session` preserves the ssh invocation, remote working directory, and running programs. Setup:

```bash
kitty -o 'map f1 save_as_session --use-foreground-process --relocatable' \
  --session <(echo "layout vertical\nlaunch\nlaunch")
```

In both windows, run `kitten ssh localhost`. After setup, press F1 to save. Running the session file re-creates both windows with correct state.

## Multiple sessions in one OS window

Restrict the tab bar to only show tabs from the active session:

```conf
tab_bar_filter session:~ or session:^$
```

Tabs without a session show the most recent active session's tabs instead.

## Keyword reference

| Keyword | Description |
|---------|-------------|
| `cd [path]` | Change working directory for all windows in the current tab |
| `focus` | Give keyboard focus to the window from the previous `launch` |
| `focus_matching_window` | Focus window matching a search expression |
| `focus_os_window` | Give focus to the current OS Window |
| `focus_tab [spec]` | Focus tab by index (0-based) or match expression |
| `enabled_layouts` | Set allowed layouts (comma-separated) |
| `launch` | Create a new window (see [[053-launch.rst\|The launch command]]) |
| `layout name` | Set the layout for the current tab |
| `new_os_window` | Create a new OS Window |
| `new_tab [title]` | Create a new tab |
| `os_window_title` | Set the OS Window title |
| `os_window_class` | Set the WM_CLASS / Wayland Application Id |
| `os_window_name` | Set the WM_CLASS Window name |
| `os_window_size` | Set OS Window size (e.g., `80c 24c`) |
| `os_window_state` | Set state: `normal`, `fullscreen`, `maximized`, `minimized` |
| `resize_window` | Resize current window (e.g., `wider 2`) |
| `set_layout_state` | Internal use only |
| `title` | Set title for the next window (deprecated, use `launch --title`) |

## The save_as_session action

Mapped to a keypress in `kitty.conf`. Saves the current OS Windows, tabs, windows, programs, working directories, etc. to a session file. Options:

- `--use-foreground-process`: save foreground process instead of shell
- `--relocatable`: resolve paths relative to the session file location
- `--base-dir`: save to a specific directory
- `--match`: only save windows matching a session expression

#kitty #terminal-emulator #session-management #window-layout #productivity
