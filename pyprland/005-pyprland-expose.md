---
title: expose | Pyprland web
url: https://hyprland-community.github.io/pyprland/expose
source: github_pages
fetched_at: 2026-01-31T16:03:30.299568118-03:00
rendered_js: false
word_count: 70
summary: This document explains how to implement an 'expose' effect in Hyprland using the pyprland plugin, which shows all client windows on the focused screen and provides configuration instructions.
tags:
    - hyprland
    - window-management
    - pyprland
    - expose-effect
    - key-binding
    - workspace-rules
category: guide
---

Implements the "expose" effect, showing every client window on the focused screen.

For a similar feature using a menu, try the [fetch\_client\_menu](https://hyprland-community.github.io/pyprland/fetch_client_menu.html) plugin (less intrusive).

Sample `hyprland.conf`:

bash

```
# Setup the key binding
bind = $mainMod, B, exec, pypr expose

# Add some style to the "exposed" workspace
workspace = special:exposed,gapsout:60,gapsin:30,bordersize:5,border:true,shadow:false
```

`MOD+B` will bring every client to the focused workspace, pressed again it will go to this workspace.

Check [workspace rules](https://wiki.hyprland.org/Configuring/Workspace-Rules/#rules) for styling options.

NOTE

If you are looking for `toggle_minimized`, check the [toggle\_special](https://hyprland-community.github.io/pyprland/toggle_special.html) plugin

## Commands [​](#commands)

Loading commands...

## Configuration [​](#configuration)

Loading configuration...