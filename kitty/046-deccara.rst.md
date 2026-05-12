---
title: Setting text styles/colors in arbitrary regions of the screen
url: https://github.com/kovidgoyal/kitty/blob/master/docs/deccara.rst
source: git
fetched_at: 2026-05-04T15:57:38.371098772-03:00
rendered_js: false
word_count: 129
summary: Extension to the DECCARA escape sequence that allows applying all SGR text attributes to arbitrary rectangular regions of the screen in the kitty terminal emulator.
tags:
    - terminal-emulation
    - escape-codes
    - sgr-attributes
    - kitty-terminal
    - deccara
    - screen-rendering
category: reference
optimized: true
optimized_at: 2026-05-04T18:00:00Z
---
# Setting text styles/colors in arbitrary regions of the screen

The standard `DECCARA <https://vt100.net/docs/vt510-rm/DECCARA.html>`__ escape sequence sets only a few text attributes in rectangular screen regions. kitty extends DECCARA to support *all* SGR attributes, including background color.

This solves problems with the traditional *background color erase (bce)* capability. See [issue discussion](https://github.com/kovidgoyal/kitty/issues/160#issuecomment-346470545) and the [ncurses FAQ on bce mismatches](https://invisible-island.net/ncurses/ncurses.faq.html#bce_mismatches).

## Syntax

To set attributes (e.g., blue background) in a rectangular region from cell `(row=3, col=4)` to `(row=10, col=11)`:

```bash
<ESC>[2*x<ESC>[4;3;11;10;44$r<ESC>[*x
```

| Parameter | Value | Meaning |
|-----------|-------|---------|
| `4` | 44 | Blue background (SGR) |
| `3` | 3 | Top row |
| `11` | 10 | Bottom row |
| `10` | 4 | Left column |
| `11` | 11 | Right column |

General form: `<ESC>[2*x<ESC>[<sgr>;<top>;<bottom>;<left>;<right>]$r<ESC>[*x`
