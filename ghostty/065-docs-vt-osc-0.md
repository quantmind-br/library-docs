---
title: Change Window Icon and Title (OSC 0) - OSC
url: https://ghostty.org/docs/vt/osc/0
source: crawler
fetched_at: 2026-02-11T01:43:36.86047-03:00
rendered_js: true
word_count: 54
summary: Describes the OSC 0 terminal escape sequence used to set both the window icon and title, specifically how it is handled as a title change in Ghostty.
tags:
    - terminal-escapes
    - osc-sequences
    - window-title
    - ghostty
    - control-codes
category: reference
---

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x30
   
   0
4. 0x3B
   
   ;
5. \_\_\__
   
   t
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Equivalent to [Change Window Icon (OSC 1)](https://ghostty.org/docs/vt/osc/1) followed by [Change Window Title (OSC 2)](https://ghostty.org/docs/vt/osc/2) with the same argument `t`.

Since Ghostty does not support changing the window icon, this is treated as an alias of [Change Window Title (OSC 2)](https://ghostty.org/docs/vt/osc/2).