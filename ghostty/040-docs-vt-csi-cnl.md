---
title: Cursor Next Line (CNL) - CSI
url: https://ghostty.org/docs/vt/csi/cnl
source: crawler
fetched_at: 2026-02-11T01:43:29.288147-03:00
rendered_js: true
word_count: 74
summary: This document explains the Cursor Next Line (CNL) escape sequence, which moves the cursor down a specified number of lines to the beginning of the row.
tags:
    - terminal-emulation
    - escape-sequences
    - csi
    - cursor-movement
    - control-sequences
category: reference
---

Move the cursor down \`n\` cells and to the beginning of the line.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   n
4. 0x45
   
   E

The parameter `n` must be an integer greater than or equal to 1. If `n` is less than or equal to 0, adjust `n` to be 1. If `n` is omitted, `n` defaults to 1.

The logic of this sequence is identical to [Cursor Down (CUD)](https://ghostty.org/docs/vt/csi/cud) followed by [Carriage Return (CR)](https://ghostty.org/docs/vt/control/cr).

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/cnl.mdx)