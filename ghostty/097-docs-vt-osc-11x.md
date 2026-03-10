---
title: Reset Dynamic Colors (OSC 110–119) - OSC
url: https://ghostty.org/docs/vt/osc/11x
source: crawler
fetched_at: 2026-03-10T06:35:46.106665-03:00
rendered_js: true
word_count: 90
summary: This document explains the use of the OSC sequence 11x to reset specific dynamic colors based on the numerical index provided.
tags:
    - osc-sequence
    - dynamic-colors
    - color-reset
    - terminal-control
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