---
title: Query or Change Dynamic Colors (OSC 10–19) - OSC
url: https://ghostty.org/docs/vt/osc/1x
source: crawler
fetched_at: 2026-02-11T01:43:39.896645-03:00
rendered_js: true
word_count: 259
summary: This document explains how to use terminal escape sequences to query or modify dynamic colors such as foreground, background, and cursor colors using index-based OSC sequences.
tags:
    - terminal-sequences
    - osc-sequences
    - dynamic-colors
    - ansi-escape-codes
    - color-configuration
    - ghostty
category: reference
---

Query or change dynamic colors based on their indices.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. \_\_\__
   
   n
4. 0x3B
   
   ;
5. \_\_\__
   
   c
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

When `n` is between `10` and `19` inclusive, either query or change the [dynamic color](https://ghostty.org/docs/vt/concepts/colors#dynamic-colors) corresponding to `n` depending on the value of `c`. `c` may be provided **multiple times**, each separated with a semicolon (`;`).

If `c` is given as a single character `?`, then the terminal will respond with the [color specification](https://ghostty.org/docs/vt/concepts/colors#color-specifications) of the dynamic color at index `n`. If `c` is a valid color specification, then the dynamic color is changed according to it.

If there are more `c`s left in the sequence, then `n` is incremented by one, and the process repeats.

The correspondence between `n` and the dynamic colors are as follows:

`n`Color`10`Foreground color`11`Background color`12`Cursor color`13`Pointer foreground color`14`Pointer background color`15`Tektronix foreground color`16`Tektronix background color`17`Highlight background color`18`Tektronix cursor color`19`Highlight foreground color

> Currently, Ghostty only supports `n` between `10` and `12` inclusive. All other dynamic colors are ignored.

As an example, this sequence changes the background color and the cursor color to `red` and `blue` respectively:

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x31 0x31
   
   11
4. 0x3B
   
   ;
5. 0x72 0x65 0x64
   
   red
6. 0x3B
   
   ;
7. 0x62 0x6C 0x75 0x65
   
   blue
8. 0x1B
   
   ESC
9. 0x5C
   
   \\

This is equivalent to combining an OSC 11 and an OSC 12 together:

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x31 0x31
   
   11
4. 0x3B
   
   ;
5. 0x72 0x65 0x64
   
   red
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

<!--THE END-->

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x31 0x32
   
   12
4. 0x3B
   
   ;
5. 0x62 0x6C 0x75 0x65
   
   blue
6. 0x1B
   
   ESC
7. 0x5C
   
   \\

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/1x.mdx)