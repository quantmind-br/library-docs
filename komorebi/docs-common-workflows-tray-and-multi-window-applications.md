---
title: Tray and multi window applications
url: https://github.com/LGUG2Z/komorebi/blob/master/docs/common-workflows/tray-and-multi-window-applications.md
source: git
fetched_at: 2026-02-20T08:51:23.413929-03:00
rendered_js: false
word_count: 92
summary: This document explains how to configure komorebi to handle applications that minimize to the system tray or use multiple windows to prevent leaving blank tiles.
tags:
    - komorebi
    - window-management
    - system-tray
    - multi-window
    - configuration
category: configuration
---

# Tray and Multi-Window Applications

❗️**NOTE**: A significant number of tray and multi-window application rules for
the most common applications are [already generated for
you](https://github.com/LGUG2Z/komorebi/#generating-common-application-specific-configurations)

If you are experiencing behaviour where closing a window leaves a blank tile,
but minimizing the same window does not, you have probably enabled a
'close/minimize to tray' option for that application. You can tell `komorebi`
to handle this application appropriately by identifying it via the executable
name or the window class.

```json
{
  "tray_and_multi_window_applications": [
    {
      "kind": "Class",
      "id": "SDL_app",
      "matching_strategy": "Equals"
    }
  ]
}
```
