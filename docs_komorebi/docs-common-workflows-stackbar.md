---
title: Stackbar
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/stackbar.md
source: git
fetched_at: 2026-02-20T08:51:23.233214-03:00
rendered_js: false
word_count: 69
summary: This document explains how to enable and configure the stackbar feature in komorebi to visualize windows within a container stack.
tags:
    - komorebi
    - stackbar
    - window-management
    - ui-configuration
category: configuration
---

# Stackbar

If you would like to add a visual stackbar to show which windows are in a container
stack ensure the following options are defined in the `komorebi.json` configuration
file.

```json
{
  "stackbar": {
    "height": 40,
    "mode": "OnStack",
    "tabs": {
      "width": 300,
      "focused_text": "#00a542",
      "unfocused_text": "#b3b3b3",
      "background": "#141414"
    }
  }
}
```

This feature is not considered stable, and you may encounter visual artifacts
from time to time.