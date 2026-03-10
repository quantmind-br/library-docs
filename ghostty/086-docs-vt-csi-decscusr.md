---
title: Set Cursor Style (DECSCUSR) - CSI
url: https://ghostty.org/docs/vt/csi/decscusr
source: crawler
fetched_at: 2026-03-10T06:35:26.943383-03:00
rendered_js: true
word_count: 75
summary: This document details the ANSI escape sequence used to set the cursor style in a terminal, specifying the meaning of the optional parameter 'n'. It provides a mapping between integer values of 'n' and the resulting cursor appearance.
tags:
    - ansi-escape-sequences
    - cursor-style
    - terminal-control
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