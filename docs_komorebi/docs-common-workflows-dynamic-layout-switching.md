---
title: Dynamic layout switching
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/dynamic-layout-switching.md
source: git
fetched_at: 2026-02-20T08:51:05.958064-03:00
rendered_js: false
word_count: 137
summary: This document explains how to configure automatic layout switching in komorebi based on the number of open window containers. It also describes how to clear these rules to enable manual layout changes on a workspace.
tags:
    - komorebi
    - dynamic-layout
    - workspace-configuration
    - window-management
    - layout-rules
category: configuration
---

# Dynamic Layout Switching

With `komorebi` it is possible to define rules to automatically change the
layout on a specified workspace when a threshold of window containers is met.

```json
{
  "monitors": [
    {
      "workspaces": [
        {
          "name": "personal",
          "layout_rules": {
            "1": "BSP"
          }
          "custom_layout_rules": {
            "5": "C:/Users/LGUG2Z/my-custom-layout.json"
          }
        },
      ]
    }
  ]
}
```

In this example, when there are one or more window containers visible on the
screen, the BSP layout is used, and when there are five or more window
containers visible, a custom layout is used.

However, if you add workspace layout rules, you will not be able to manually
change the layout of a workspace until all layout rules for that workspace have
been cleared.

```powershell
# for example, to clear rules from monitor 0, workspace 0
komorebic clear-workspace-layout-rules 0 0
```
