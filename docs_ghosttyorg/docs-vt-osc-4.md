---
title: Query or Change Palette Colors (OSC 4) - OSC
url: https://ghostty.org/docs/vt/osc/4
source: crawler
fetched_at: 2026-03-03T08:23:43.436974-03:00
rendered_js: true
word_count: 215
summary: This document explains how to query or modify colors within the terminal's palette using specific control sequences based on an index and a color value or query character.
tags:
    - terminal-control
    - color-palette
    - osc-4
    - color-query
    - color-modification
category: reference
---

Query or change colors in the palette based on their indices.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x34
   
   4
4. 0x3B
   
   ;
5. \_\_\__
   
   n
6. 0x3B
   
   ;
7. \_\_\__
   
   c
8. 0x1B
   
   ESC
9. 0x5C
   
   \\

Query or change the color in the palette at index `n` depending on the value of `c`.

If `c` is given as the single character `?`, then the terminal will respond with the [color specification](https://ghostty.org/docs/vt/concepts/colors#color-specifications) of the color at index `n`. If `c` is a valid color, then the palette color is changed to it.

Pairs of `n` and `c` can be provided **multiple times**, separated with a semicolon (`;`). The terminal may reply with multiple sequences when multiple queries are made in one request.

> The terminal need not return the color exactly as it was specified.
> 
> When a color at a given index is changed, the terminal is allowed to convert the color into its internal representation, then reply in a different format when the same color is queried.

When `n` is between 0 and 255, the normal 256-color palette is used. When `n` is above 255, however, they instead map to [special colors](https://ghostty.org/docs/vt/concepts/colors#special-colors), with 256 mapping to the first special color (bold), 257 the second (underline), etc. This makes it behave equivalently to [OSC 5](https://ghostty.org/docs/vt/osc/5) with the index subtracted by 256.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/4.mdx)