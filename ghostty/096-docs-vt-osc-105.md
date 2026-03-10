---
title: Reset Special Colors (OSC 105) - OSC
url: https://ghostty.org/docs/vt/osc/105
source: crawler
fetched_at: 2026-03-10T06:35:45.286609-03:00
rendered_js: true
word_count: 48
summary: This document details the structure and function of OSC sequence 105, which is used to reset special terminal colors, optionally specifying which color indexes to affect.
tags:
    - osc-105
    - terminal-control
    - color-reset
    - escape-sequences
    - ansi
category: reference
---

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x31 0x30 0x35
   
   105
4. 0x3B
   
   ;
5. \_\_\__
   
   n
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Reset the [special color](https://ghostty.org/docs/vt/concepts/colors#special-colors) at index `n`. `n` can be specified **zero or more** times, separated with semicolons (`;`) When `n` is not specified, all special colors are reset.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/105.mdx)