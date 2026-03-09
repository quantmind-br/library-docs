---
title: Reset Dynamic Colors (OSC 110–119) - OSC
url: https://ghostty.org/docs/vt/osc/11x
source: crawler
fetched_at: 2026-03-03T08:23:45.092196-03:00
rendered_js: true
word_count: 90
summary: This document explains the ANSI escape sequence used to reset dynamic terminal colors based on specific numeric indices (110-119). It details the mapping between these indices and the particular color being reset.
tags:
    - ansi-escape-sequence
    - dynamic-colors
    - osc
    - terminal-control
    - color-reset
category: reference
---

Reset dynamic colors based on their indices.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. \_\_\__
   
   n
4. 0x1B
   
   ESC
5. 0x5C
   
   \\

When `n` is between `110` and `119` inclusive, reset the [dynamic color](https://ghostty.org/docs/vt/concepts/colors#dynamic-colors) corresponding to `n`.

The correspondence between `n` and the dynamic colors are as follows:

`n`Color`110`Foreground color`111`Background color`112`Cursor color`113`Pointer foreground color`114`Pointer background color`115`Tektronix foreground color`116`Tektronix background color`117`Highlight background color`118`Tektronix cursor color`119`Highlight foreground color

> Currently, Ghostty only supports `n` between `110` and `112` inclusive. All other dynamic colors are ignored.

> xterm allows a trailing semicolon (`;`) to come after `n`.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/11x.mdx)