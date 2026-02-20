---
title: Workspace work area offset
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/workspace-work-area-offset.md
source: git
fetched_at: 2026-02-20T08:50:59.104671-03:00
rendered_js: false
word_count: 93
summary: This document details the usage and parameters for the komorebic command that defines work area offsets for specific monitors and workspaces.
tags:
    - komorebi
    - tiling-window-manager
    - workspace-offsets
    - monitor-configuration
    - cli-reference
category: reference
---

# workspace-work-area-offset

```
Set offsets for a workspace to exclude parts of the work area from tiling

Usage: komorebic.exe workspace-work-area-offset <MONITOR> <WORKSPACE> <LEFT> <TOP> <RIGHT> <BOTTOM>

Arguments:
  <MONITOR>
          Monitor index (zero-indexed)

  <WORKSPACE>
          Workspace index (zero-indexed)

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
