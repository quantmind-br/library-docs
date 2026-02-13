---
title: ConEmu Extensions (OSC 9;n) - OSC
url: https://ghostty.org/docs/vt/osc/conemu
source: crawler
fetched_at: 2026-02-11T01:43:41.531723-03:00
rendered_js: true
word_count: 339
summary: This document describes Ghostty's implementation of ConEmu-specific OSC 9 escape sequences used to manage and display terminal progress states.
tags:
    - terminal-emulator
    - osc-sequences
    - conemu
    - progress-bar
    - terminal-protocol
    - escape-codes
category: reference
---

Various extensions pioneered by ConEmu.

[ConEmu](https://conemu.github.io/), an older terminal emulator for Windows, pioneered several [custom protocols](https://conemu.github.io/en/AnsiEscapeCodes.html#ConEmu_specific_OSC) using OSC 9. Unfortunately, this conflicts with iTerm2's [Show Desktop Notification](https://ghostty.org/docs/vt/osc/9) protocol, which also uses OSC 9. Ghostty attempts to differentiate between the two by trying to find the *sub-ID* that each ConEmu sequence has, which determines its actual function. When one is not found, a Show Desktop Notification sequence is assumed instead.

Because the following protocols are often underspecified at best and highly questionable security-wise at worst, Ghostty only *implements* the extensions that are listed below. There are many more that Ghostty does parse, but either due to security reasons or the fact that Ghostty does not try to be a ConEmu clone, they are either ignored or converted into [OSC 9](https://ghostty.org/docs/vt/osc/9) sequences.

1. 0x1B
   
   ESC
2. 0x5D
   
   ]
3. 0x39
   
   9
4. 0x3B
   
   ;
5. 0x34
   
   4
6. 0x3B
   
   ;
7. \_\_\__
   
   s
8. 0x1B
   
   ESC
9. 0x5C
   
   \\

<!--THE END-->

01. 0x1B
    
    ESC
02. 0x5D
    
    ]
03. 0x39
    
    9
04. 0x3B
    
    ;
05. 0x34
    
    4
06. 0x3B
    
    ;
07. \_\_\__
    
    s
08. 0x3B
    
    ;
09. \_\_\__
    
    v
10. 0x1B
    
    ESC
11. 0x5C
    
    \\

Change the current progress state based on the value of `s` and `v`.

The current progress can be in various states: inactive (default), in progress, error, or indeterminate, which is represented visually in Ghostty as a progress bar on top of each split. Its value is represented as an integer between 0 and 100 inclusive, corresponding to the percentage level of the progress bar.

The new state and value chiefly depends on the value of `s`:

`s`New stateNew value`0`Inactive0`1`In progress`v``2`Error`v` when specified, otherwise unchanged`3`IndeterminateUnchanged`4`Paused`v` when specified, otherwise unchanged

> Note that the terminal cannot determine when a progress state becomes *stale* with this protocol, e.g. when a program is terminated without cleaning up its progress state. This is why Ghostty has a **hardcoded timeout** of around 15 seconds, after which the current progress state is reset.
> 
> If you're writing a program that uses this protocol, you need to make sure to update the progress state regularly as a keep-alive signal. There is sadly no standardization around this, but we recommend at least updating once per second.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/vt/osc/conemu.mdx)