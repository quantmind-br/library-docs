---
title: Query or Change Special Colors (OSC 5) - OSC
url: https://ghostty.org/docs/vt/osc/5
source: crawler
fetched_at: 2026-02-11T01:43:38.283196-03:00
rendered_js: true
word_count: 83
summary: This document explains the OSC 5 escape sequence used to query or modify specific special terminal colors based on their index.
tags:
    - osc-5
    - escape-sequences
    - terminal-colors
    - vt-specification
    - color-configuration
category: reference
---

Query or change a special color based on its index.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x35
   
   5
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

Query or change the [special color](https://ghostty.org/docs/vt/concepts/colors#special-colors) corresponding to `n` depending on the value of `c`.

`n` and `c` behave nearly identically to [OSC 4](https://ghostty.org/docs/vt/osc/4), and may also be repeated multiple times in one sequence. The difference is that `n` now ranges between 0 and 4 inclusive, corresponding to the five special colors.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/5.mdx)