---
title: Set Cursor Style (DECSCUSR) - CSI
url: https://ghostty.org/docs/vt/csi/decscusr
source: crawler
fetched_at: 2026-02-11T01:43:24.111307-03:00
rendered_js: true
word_count: 75
summary: This document explains the DECSCUSR control sequence used to configure the terminal cursor style, defining how various integer values change the cursor's shape and blinking behavior.
tags:
    - terminal-graphics
    - cursor-style
    - vt-sequence
    - csi-sequence
    - decscusr
category: reference
---

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x20
5. 0x71
   
   q

If `n` is omitted, `n` defaults to `0`. `n` must be an integer between 0 and 6 (inclusive). The mapping of `n` to cursor style is below:

nstyle0terminal default1blinking block2steady block3blinking underline4steady underline5blinking vertical bar6steady vertical bar

For `n = 0`, the terminal default is up to the terminal and is inconsistent across terminal implementations. The default may also be impacted by terminal configuration.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/decscusr.mdx)