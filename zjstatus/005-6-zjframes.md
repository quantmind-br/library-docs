---
title: 6 Zjframes
url: https://github.com/dj95/zjstatus/wiki/6---zjframes
source: wiki
fetched_at: 2026-04-30T12:58:31.423229696-03:00
rendered_js: false
word_count: 312
summary: This document describes the installation and configuration of the zjframes plugin for Zellij, which allows users to dynamically manage and toggle pane frame visibility based on specific conditions.
tags:
    - zellij
    - plugin
    - terminal-emulator
    - pane-management
    - configuration
    - window-manager
category: configuration
---

zjframes is an additional plugin, based on zjstatus hide frames features, that runs in the background. It just controls pane frames based on certain conditions for users, who want to user other status bars, but display frames based on different conditions.


> [!IMPORTANT]
> zjframes is only supported for zellij 0.41.0 or higher!


> [!CAUTION]
> Please disable pane_frames in your global zellij configs as zjframes will activate them in certain scenarios. Otherwise weird behavior might occur as zellij will reset the frames on each event cycle and causes conflicts.


## 📦 Installation

*zjframes*  has to be installed either as a file or via https locations within the *config.kdl*.

```javascript
// Plugins to load in the background when a new session starts
load_plugins {
    "file:./path/to/zjframes.wasm" {
        hide_frame_for_single_pane       "false"
        hide_frame_except_for_search     "true"
        hide_frame_except_for_fullscreen "true"
    }

    // or

    "https://github.com/dj95/zjstatus/releases/latest/download/zjframes.wasm" {
        hide_frame_for_single_pane       "false"
        hide_frame_except_for_search     "true"
        hide_frame_except_for_fullscreen "true"
    }
}
```

### ⚙️ Configuration

Configuration is done in the block (`{ ... }`) behind the location in the *config.kdl*. Options can also be combined.


```javascript
// Plugins to load in the background when a new session starts
load_plugins {
    "https://github.com/dj95/zjstatus/releases/latest/download/zjframes.wasm" {
        hide_frame_for_single_pane       "false"
        hide_frame_except_for_search     "true"
        hide_frame_except_for_fullscreen "true"
    }
}
```

#### Hide pane frames for tabs single panes

The option `hide_frame_for_single_pane` will toggle the pane frames depending on how many panes (not plugin panes) are shown.
This will effectively hide the frame border, when only one pane, like an editor, is shown. Pane frames are toggled as soon
as there is another pane created.

#### Hide pane frames except for search

The option `hide_frame_except_for_search ` will toggle the pane frames only on, when search mode is enabled. Otherwise it will toggle the pane frames off.

#### Hide pane frames except for fullscreen

The option `hide_frame_except_for_fullscreen` will toggle the pane frames only to on, when the current active pane is in fullscreen mode. Otherwise the frames are off.
