---
title: Set Cursor Style (DECSCUSR) - CSI
url: https://ghostty.org/docs/vt/csi/decscusr
source: crawler
fetched_at: 2026-03-03T08:23:31.918362-03:00
rendered_js: true
word_count: 75
summary: This document details the Control Sequence Introducer (CSI) sequence DECSETCURSOR to define the visual style of the text cursor within a terminal environment based on an integer parameter 'n'. It provides a mapping table showing which cursor style corresponds to each valid value of 'n' from 0 to 6.
tags:
    - terminal-control
    - csi-sequence
    - cursor-style
    - vt100
    - decsetcursor
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