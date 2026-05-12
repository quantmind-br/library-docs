---
title: Miscellaneous protocol extensions
url: https://github.com/kovidgoyal/kitty/blob/master/docs/misc-protocol.rst
source: git
fetched_at: 2026-05-04T15:58:15.431586246-03:00
rendered_js: false
word_count: 277
summary: Custom protocol extensions in the kitty terminal emulator: state management, attribute control, event reporting, and escape code families.
tags:
    - terminal-emulator
    - escape-codes
    - protocol-extension
    - kitty-terminal
    - sgr-sequences
    - mouse-reporting
category: reference
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# Miscellaneous protocol extensions

Small protocol extensions kitty implements, primarily for its own kittens.

## Save/restore all terminal modes

XTerm's `XTSAVE`/`XTRESTORE` escape codes require an explicit mode list. kitty extends this: when no modes are specified, all *side-effect-free* modes are saved/restored.

| Mode type | Side effects? | Example |
|-----------|--------------|---------|
| Side-effect-free | No | Bracketed paste, mouse tracking |
| With side effects | Yes (cursor, screen) | `DECOM`, `DECCOLM` |

This lets TUI apps save/restore emulator state without maintaining mode lists.

### Escape codes

- Save all modes: `` <ESC>[s ``
- Restore all modes: `` <ESC>[u ``

## Independent bold/faint reset

Standard SGR: bold (1), faint (2), reset both (22). kitty adds independent resets:

- `` <ESC>[221m `` — reset bold only
- `` <ESC>[222m `` — reset faint only

## Mouse leave window reporting

Extends xterm's SGR Pixel mouse protocol to report when the mouse exits the window.

| Bit | Meaning |
|-----|---------|
| 8 | Mouse left window event |
| 5 | Motion-related event |
| 1-7 (except 5) | Button and modifier info |

> [!warning]
> When bit 8 is set, pixel position values are undefined and must be ignored.

## Move screen contents to scrollback

`` <ESC>[22J `` moves all screen contents (text and images) to scrollback, leaving the screen cleared.

## kitty private escape codes (DCS family)

All kitty-specific escape codes are DCS (Device Control String) sequences:

```
<ESC>P @ kitty-<payload><ESC>\
```

| Prefix | Purpose |
|--------|---------|
| `kitty-` | Core private codes |
| `kitty-rc-` | Remote control commands |
| `kitty-info-` | Terminal information queries |

Used for remote control, clipboard, window management, and other inter-process communication.
