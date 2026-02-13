---
title: Reset Palette Colors (OSC 104) - OSC
url: https://ghostty.org/docs/vt/osc/104
source: crawler
fetched_at: 2026-02-11T01:43:40.350977-03:00
rendered_js: true
word_count: 108
summary: This document explains the OSC 104 terminal escape sequence used to reset specific color indices or the entire color palette to their default values.
tags:
    - terminal-emulation
    - osc-sequences
    - color-palette
    - ansi-escape-codes
    - terminal-configuration
category: reference
---

Reset colors in the palette.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x31 0x30 0x34
   
   104
4. 0x3B
   
   ;
5. \_\_\__
   
   n
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Reset the color in the palette at index `n`. `n` can be specified **zero or more** times, separated with semicolons (`;`) When `n` is not specified, the entire palette is reset.

When `n` is between 0 and 255, the normal 256-color palette is used. When `n` is above 255, however, they instead map to [special colors](https://ghostty.org/docs/vt/concepts/colors#special-colors), with 256 mapping to the first special color (bold), 257 the second (underline), etc. This makes it behave equivalently to [OSC 105](https://ghostty.org/docs/vt/osc/105) with the index subtracted by 256.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/104.mdx)