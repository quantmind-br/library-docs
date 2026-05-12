---
title: Code editor Vim keybindings | Warp
url: https://docs.warp.dev/code/code-editor/code-editor-vim-keybindings
source: sitemap
fetched_at: 2026-04-29T15:03:25.448174305-03:00
rendered_js: false
word_count: 361
summary: This document provides instructions on enabling Vim mode in the Warp code editor and outlines the supported keybindings, movement commands, and editing features.
tags:
    - vim-keybindings
    - code-editor
    - text-editing
    - keyboard-shortcuts
    - developer-tools
    - warp-terminal
category: guide
optimized: true
optimized_at: 2026-04-29T15:03:25.448174305-03:00
---
The Vi family (Vim, Neovim) are modal text editors with keyboard-driven editing. Warp's [[181-code-code-editor|native code editor]] includes Vim mode support.

## Enable Vim Keybindings

**Settings** > **Features** > **Text Editing** > toggle "Edit code and commands with Vim keybindings".

Unlike the input editor, the code editor starts in Normal mode.

## Customize Keybindings

Warp supports default Vim keybindings. The "Exit Vim Insert Mode" shortcut can be rebind via **Settings** > **Keyboard shortcuts** or the [Command Palette](https://docs.warp.dev/terminal/command-palette).

## Supported Keybindings

### Movement

| Key | Action |
|-----|--------|
| `j/k/h/l` | single-char movement with line wrap |
| `^` | first non-whitespace character of line |
| `%` | prev/next unmatched bracket |
| `0` | beginning of current line |
| `+` / `-` | first non-whitespace of next/previous line |

### Editing

| Key | Action |
|-----|--------|
| `r` | replace character under cursor |
| `c` | change range/object (delete, enter insert mode) |
| `s` | substitute (delete, enter insert mode) |
| `y` | yank (copy) to clipboard |
| `~` | toggle upper/lowercase |
| `u` / `U` | lowercase/uppercase |
| `J` | join current and following lines |
| `gc` | toggle comments on line/visual selection |

### Text Objects

| Key | Object |
|-----|--------|
| `i"` | inner quotes |
| `a"` | around quotes |
| `iw` | inner word |
| `i(` / `a(` | inner/around parentheses |

### Search

| Key | Action |
|-----|--------|
| `f/F` | find next/prev character on line |
| `;` / `,` | repeat last search same/opposite direction |

General search (`/` or `?`) opens Warp's native command search instead of buffer search.

### Mode Switching

| Key | Action |
|-----|--------|
| `i` | insert before cursor |
| `I` | insert before first non-whitespace |
| `a` | append after cursor |
| `A` | append at end of line |
| `o` | new line below, insert |
| `O` | new line above, insert |

### Registers

- `"` — unnamed register (last delete/yank)

> [!tip]
> Report Vim keybinding bugs/features via [GitHub Issues](https://github.com/warpdotdev/Warp/issues) (label for Vim Keybindings).
