---
title: Vertical Position Absolute (VPA) - CSI
url: https://ghostty.org/docs/vt/csi/vpa
source: crawler
fetched_at: 2026-03-10T06:35:35.869673-03:00
rendered_js: true
word_count: 91
summary: This document describes the VT escape sequence VPA (Vertical Position Absolute) used to move the cursor to a specific row in a terminal interface.
tags:
    - vt
    - escape-sequence
    - cursor-control
    - vpa
    - cup
category: reference
---

Move the cursor to a specific row.

1. 0x1B
   
   ESC
2. 0x5B
   
   [
3. \_\_\__
   
   y
4. 0x64
   
   d

This sequence performs [cursor position (CUP)](https://ghostty.org/docs/vt/csi/cup) with `y` set to the parameterized value and `x` set to the current cursor position. There is no additional or different behavior for using `VPA`.

Because this invokes `CUP`, the cursor column (`y`) can change if it is outside the bounds of the `CUP` operation. For example, if [origin mode](#TODO) is set and the current cursor position is outside of the scroll region, the column will be adjusted.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/csi/vpa.mdx)