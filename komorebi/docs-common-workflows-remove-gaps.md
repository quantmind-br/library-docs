---
title: Remove gaps
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/remove-gaps.md
source: git
fetched_at: 2026-02-20T08:51:20.613194-03:00
rendered_js: false
word_count: 53
summary: This document provides instructions on how to remove gaps between windows and monitor edges by modifying padding settings in the komorebi configuration file.
tags:
    - komorebi
    - window-management
    - configuration
    - padding
    - workspace-settings
    - customization
category: configuration
---

# Remove Gaps

If you would like to remove all gaps by default, both between windows
themselves, and between the monitor edges and the windows, you can set the
following configuration options to `0` and `-1` in the `komorebi.json`
configuration file.

```json
{
  "default_workspace_padding": 0,
  "default_container_padding": -1,
}
```

[![Watch the tutorial video](https://img.youtube.com/vi/6QYLao953XE/hqdefault.jpg)](https://www.youtube.com/watch?v=6QYLao953XE)
