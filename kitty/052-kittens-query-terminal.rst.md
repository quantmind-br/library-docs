---
title: Query terminal
url: https://github.com/kovidgoyal/kitty/blob/master/docs/kittens/query_terminal.rst
source: git
fetched_at: 2026-05-08T15:58:03.584580761-03:00
rendered_js: false
word_count: 182
summary: Query runtime options and configuration values from the kitty terminal emulator using XTGETTCAP escape sequences.
tags:
    - terminal-emulator
    - query-tool
    - escape-sequences
    - xtgetcap
    - kitty-terminal
    - command-line-utilities
category: reference
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# Query terminal

Query kitty from any terminal program about version, runtime options, and feature states. Works over SSH.

> [!info]
> Uses the XTGETTCAP escape sequence (xterm-compatible). Slow since it requires a roundtrip to the terminal and back.

## Usage

```bash
kitty +kitten query_terminal <key> [<key> ...]
```

## Available query keys

| Key | Description |
|-----|-------------|
| `version` | kitty version string |
| `foreground_processes` | Processes in the active window |
| `background_processes` | Processes in background tabs |
| `active_processes` | All running processes |
| `tab_title` | Current tab title |
| `window_title` | Current window title |
| `cwd` | Current working directory |
| `list_outputs` | Available screen outputs |
| `screen_size` | Screen dimensions in pixels |
| `cell_size` | Character cell dimensions |
| `colors` | Current color palette |
| `cursor` | Cursor style and blink state |
| `graphic_options` | Supported graphics features |
| `text_undercurl` | Whether underline styles are supported |

## Raw escape codes

Send queries directly from any program. Prefix kitty-specific keys with `kitty-query-`. See the [xterm ctlseqs documentation](https://invisible-island.net/xterm/ctlseqs/ctlseqs.html) for the full XTGETTCAP syntax.
