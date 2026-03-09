---
title: Change Window Title (OSC 2) - OSC
url: https://ghostty.org/docs/vt/osc/2
source: crawler
fetched_at: 2026-03-03T08:23:42.42638-03:00
rendered_js: true
word_count: 67
summary: This document details the specific sequence of escape codes required to change the terminal window title, noting differences in string encoding interpretation between xterm and Ghostty.
tags:
    - terminal-control
    - window-title
    - osc-sequence
    - escape-codes
    - utf-8-encoding
    - xterm
    - ghostty
category: guide
---

Change the name of the window title.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x32
   
   2
4. 0x3B
   
   ;
5. \_\_\__
   
   t
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

Change the window title to `t`.

While xterm defaults to interpreting `t` as a ISO-8859-1-encoded string, which can be changed via Set Title Mode (XTSMTITLE) to either accept a hexadecimal-escaped or bare UTF-8 string, Ghostty always unconditionally expects `t` to be directly UTF-8-encoded.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/2.mdx)