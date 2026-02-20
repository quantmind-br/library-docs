---
title: Named workspace layout rule
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/cli/named-workspace-layout-rule.md
source: git
fetched_at: 2026-02-20T08:48:59.552948-03:00
rendered_js: false
word_count: 54
summary: This document provides the usage instructions for the named-workspace-layout-rule command, which defines dynamic layout triggers for specific workspaces based on container count.
tags:
    - komorebi
    - window-management
    - layout-configuration
    - workspace-rules
    - tiling-window-manager
category: reference
---

# named-workspace-layout-rule

```
Add a dynamic layout rule for the specified workspace

Usage: komorebic.exe named-workspace-layout-rule <WORKSPACE> <AT_CONTAINER_COUNT> <LAYOUT>

Arguments:
  <WORKSPACE>
          Target workspace name

  <AT_CONTAINER_COUNT>
          The number of window containers on-screen required to trigger this layout rule

  <LAYOUT>
          [possible values: bsp, columns, rows, vertical-stack, horizontal-stack, ultrawide-vertical-stack, grid, right-main-vertical-stack, scrolling]

Options:
  -h, --help
          Print help

```
