---
title: Monitor work area offset
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/monitor-work-area-offset.md
source: git
fetched_at: 2026-02-20T08:48:47.484726-03:00
rendered_js: false
word_count: 88
summary: This document describes the usage of the monitor-work-area-offset command to define custom margins for a specific monitor's tiling area.
tags:
    - komorebi
    - window-management
    - monitor-configuration
    - cli-reference
    - tiling-window-manager
category: reference
---

# monitor-work-area-offset

```
Set offsets for a monitor to exclude parts of the work area from tiling

Usage: komorebic.exe monitor-work-area-offset <MONITOR> <LEFT> <TOP> <RIGHT> <BOTTOM>

Arguments:
  <MONITOR>
          Monitor index (zero-indexed)

  <LEFT>
          Size of the left work area offset (set right to left * 2 to maintain right padding)

  <TOP>
          Size of the top work area offset (set bottom to the same value to maintain bottom padding)

  <RIGHT>
          Size of the right work area offset

  <BOTTOM>
          Size of the bottom work area offset

Options:
  -h, --help
          Print help

```
