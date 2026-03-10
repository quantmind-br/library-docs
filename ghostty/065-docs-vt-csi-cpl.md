---
title: Cursor Preceding Line (CPL) - CSI
url: https://ghostty.org/docs/vt/csi/cpl
source: crawler
fetched_at: 2026-03-10T06:35:31.136404-03:00
rendered_js: true
word_count: 78
summary: This document details the control sequence for moving the terminal cursor up 'n' lines to the start of the respective lines, known as Cursor Previous Line (CPL). It specifies the required byte sequence and parameter handling for the 'n' parameter.
tags:
    - cursor-movement
    - terminal-control
    - cpl
    - ansi-escape-sequence
    - control-sequence
category: reference
---

## Cursor Previous Line (CPL)

Move the cursor up \`n\` cells and to the beginning of the line.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x46
   
   F

The parameter `n` must be an integer greater than or equal to 1. If `n` is less than or equal to 0, adjust `n` to be 1. If `n` is omitted, `n` defaults to 1.

The logic of this sequence is identical to [Cursor Up (CUU)](https://ghostty.org/docs/vt/csi/cuu) followed by [Carriage Return (CR)](https://ghostty.org/docs/vt/control/cr).

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/cpl.mdx)