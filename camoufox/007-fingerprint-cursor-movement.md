---
title: Cursor Movement | Camoufox
url: https://camoufox.com/fingerprint/cursor-movement/
source: crawler
fetched_at: 2026-02-14T14:05:49.883481-03:00
rendered_js: true
word_count: 108
summary: This document explains how to configure and use human-like cursor movement and visual highlighters in the Camoufox browser.
tags:
    - camoufox
    - cursor-movement
    - human-simulation
    - browser-stealth
    - configuration
category: configuration
---

## [#](#human-like-cursor-movement)Human-like Cursor movement

Camoufox has built-in support for human-like cursor movement. The natural motion algorithm was originally from [riflosnake's HumanCursor](https://github.com/riflosnake/HumanCursor), but has been rewritten in C++ and modified for more distance-aware trajectories.

* * *

## [#](#properties)Properties

PropertyTypeDescription`humanize`boolEnable/disable human-like cursor movement. Defaults to False.`humanize:maxTime`doubleMaximum time in seconds for the cursor movement. Defaults to `1.5`.`humanize:minTime`doubleMinimum time in seconds for the cursor movement.`showcursor`boolToggles the cursor highlighter. Defaults to True.

##### Note

The cursor highlighter is **not** ran in the page context. It will not be visible to the page. You don't have to worry about it leaking.

* * *

## [#](#demo)Demo

Here is a demo of the cursor highlighter. The testing page for this can be found [here](https://camoufox.com/tests/buttonclick).