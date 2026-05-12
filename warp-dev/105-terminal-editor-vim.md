---
title: Input editor Vim keybindings | Warp
url: https://docs.warp.dev/terminal/editor/vim
source: sitemap
fetched_at: 2026-04-29T15:02:23.714069567-03:00
rendered_js: false
word_count: 404
summary: This document explains how to enable, customize, and utilize the built-in Vim keybinding support within the Warp terminal's input editor.
tags:
    - warp-terminal
    - vim-mode
    - keybindings
    - text-editing
    - command-line-tools
category: guide
optimized: true
optimized_at: 2026-04-29T19:02:00Z
---
Warp implements Vim keybindings (Vim mode) natively in the input editor, replacing shell editor capabilities.

## Enable Vim keybindings

- **Settings** → **Features** → **Text Editing** → toggle "Edit commands with Vim keybindings"
- `CMD-SHIFT-V` if Warp detects shell vi mode

> [!info]
> Editor starts in insert mode. Press `CTRL-C` or `ENTER` to clear pending command state.

## Customize keybindings

Only the "Exit Vim Insert Mode" shortcut is customizable:
- **Settings** → **Keyboard shortcuts** → **Exit Vim Insert Mode**
- [Command Palette](https://docs.warp.dev/terminal/command-palette): search "Exit Vim Insert Mode"

## Supported keybindings

### Movement

| Key | Action |
|-----|--------|
| `h`/`l` | single-char movement with line wrap |
| `0` | first non-whitespace character of line |
| `^` | beginning of current line |
| `$` | end of line |
| `%` | prev/next unmatched bracket |
| `+`/`-` | first non-whitespace of next/previous line |
| `gg` | beginning of buffer |
| `G` | end of buffer |

### Editing

| Key | Action |
|-----|--------|
| `r` | replace character under cursor |
| `c` | change range/object (delete, go to insert mode) |
| `s` | substitute (change, delete at cursor only) |
| `y` | yank to clipboard |
| `~` | toggle upper/lowercase |
| `u`/`U` | lowercase/uppercase |
| `J` | join current and following lines |

### Text objects

| Key | Object |
|-----|--------|
| `i"`/`a"` | inner/around quoted string |
| `i'`/`a'` | inner/around single-quoted string |
| `iw`/`aw` | inner/around word |
| `i(`/`a(` | inner/around parenthesized string |

### Character search

| Key | Action |
|-----|--------|
| `f`/`F` | find next/prev matching character on line |
| `;`/`,` | repeat last character search same/opposite direction |

### General search

> [!note]
> Unlike Vim, general search opens Warp's native command search rather than searching within the buffer.

### Mode switching

| Key | Action |
|-----|--------|
| `i` | insert before cursor |
| `I` | insert before first non-whitespace |
| `a` | append after cursor |
| `A` | append at end of line |
| `o` | new line below, insert |
| `O` | new line above, insert |

### Registers

| Register | Contents |
|----------|----------|
| `"` | unnamed register (last delete or yank) |

## Feedback

Report bugs and request features via [GitHub Issues](https://github.com/warpdotdev/Warp/issues) (tag for Vim Keybindings).

#vim-mode #keybindings #text-editing #command-line-tools
