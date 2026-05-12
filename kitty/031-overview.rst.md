---
title: Overview
url: https://github.com/kovidgoyal/kitty/blob/master/docs/overview.rst
source: git
fetched_at: 2026-05-04T15:58:18.394785602-03:00
rendered_js: false
word_count: 599
summary: Overview of the kitty terminal emulator — design philosophy, configuration, layouts, kittens, remote control, sessions, and key features.
tags:
    - terminal-emulator
    - window-management
    - keyboard-shortcuts
    - scripting
    - configuration
    - remote-control
category: concept
optimized: true
optimized_at: 2026-05-04T20:30:00Z
---
# Overview

## Design philosophy

kitty is designed for power keyboard users. All controls work from the keyboard (mouse also supported). Configuration is a single human-editable file for easy reproducibility.

Technology stack: C (performance), Python (extensibility/UI), Go (CLI kittens). Uses only OpenGL for rendering — no large UI toolkit dependencies.

Supports all modern terminal features: Unicode, true color, bold/italic fonts, text formatting, colored underlines, and more. Easily extensible.

## Configuration

Open the sample config in your editor:

```bash
edit_config_file
```

See [[037-conf.rst|kitty.conf]] for full details. Browse mappable actions with `command_palette`.

## Layouts

A layout arranges kitty windows inside an OS window. Currently available:

| Layout | Description |
|--------|-------------|
| **Fat** | Top: full-width window(s); bottom: side-by-side windows |
| **Grid** | All windows in a grid |
| **Horizontal** | All windows side-by-side |
| **Splits** | Arbitrary patterns via horizontal/vertical splits |
| **Stack** | Single maximized window at a time |
| **Tall** | Left: full-height window(s); right: stacked windows |
| **Vertical** | All windows stacked vertically |

Switch layouts with `next_layout`. Configure shortcuts for specific layouts in `conf-kitty-shortcuts.layout`. First layout in `enabled_layouts` is the default.

See [[039-layouts.rst|Arrange windows]] for details.

## Extending kitty

Create terminal programs called *kittens* to add features or leverage kitty's capabilities:

- [[018-kittens-remote-file.rst|Edit remote files]]
- [[022-kittens-unicode-input.rst|Input Unicode characters]]
- [[014-kittens-icat.rst|View images]]
- [[011-kittens-diff.rst|Diff files with image support]]

See [[030-kittens-intro.rst|Extend with kittens]] and [[008-kittens-custom.rst|Custom kittens]]. Use the watchers framework for Python scripts responding to events (resize, close, title changes, etc.).

## Remote control

Control kitty from the shell, even over SSH. Change colors, fonts, open windows/tabs, set titles, change layouts, pipe text between windows, and more.

See [[028-remote-control.rst|Control kitty from scripts]] for the tutorial.

## Sessions

Define tabs, windows, layouts, working directories, and startup programs in a session file. Switch between sessions with a keypress.

See [[029-sessions.rst|Sessions]] for details.

## Creating tabs/windows

Run arbitrary programs in new tabs, windows, or overlays at a keypress. See [[053-launch.rst|The launch command]].

## Mouse features

- Click URLs to open in browser
- Double-click to select a word; drag to extend
- Triple-click to select a line; drag to extend more
- Triple-click with Ctrl+Alt to select from click point to end of line
- Right-click to extend previous selection
- Ctrl+Alt+drag for column selection
- Selecting text copies to primary clipboard
- Middle-click to paste from primary clipboard
- Ctrl+Shift+right-click opens command output in pager (requires `shell_integration`)
- Hold Shift to select text even when a program has grabbed the mouse

Customize all mouse actions in `conf-kitty-mouse.mousemap`. Configure hyperlink clicks, file opening, downloads, browser opening in `open_actions`.

Drag and drop tabs to reorder or move to another OS window. Drag window borders to resize. Double-click empty tab bar region to create a new tab; double-click a tab to rename it.

## Font control

Specify individual font families for regular, bold, italic, and bold+italic. Specify fonts for specific Unicode character ranges. Supports OpenType features and variable fonts.

See [[038-kittens-choose-fonts.rst|Changing kitty fonts]] and `conf-kitty-fonts`.

## Scrollback buffer

Scroll to view history (keyboard or mouse). An interactive scrollbar shows position. Open scrollback in your pager:

```bash
map f1 launch --stdin-source=@screen_scrollback --stdin-add-formatting less +G -R
```

Press `show_scrollback` for the same. See `kitty-scrollback.nvim` or `kitty-grab` for editor integrations. Increase `scrollback_pager_history_size` for large scrollback.

## Shell integration

kitty integrates with zsh, fish, and bash for: jumping to previous prompts in scrollback, viewing last command output in less, mouse cursor movement while editing prompts.

See [[041-shell-integration.rst|Shell integration]].

## Multiple copy/paste buffers

```conf
map f1 copy_to_buffer a
map f2 paste_from_buffer a
```

Define any number of named buffers.

## Marks

Mark text on screen based on regular expressions to highlight words or phrases. See [[026-marks.rst|Mark text on screen]].

#terminal-emulator #window-management #scripting #configuration #remote-control
