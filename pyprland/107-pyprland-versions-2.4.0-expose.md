---
title: expose | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.4.0/expose
source: github_pages
fetched_at: 2026-01-31T16:04:44.351453798-03:00
rendered_js: false
word_count: 104
summary: Provides instructions for implementing an 'expose' effect in Hyprland that displays all client windows on the focused screen, with configuration options and key bindings.
tags:
    - hyprland
    - window-management
    - key-binding
    - workspace
    - expose-effect
    - pyprland
category: guide
---

Implements the "expose" effect, showing every client window on the focused screen.

For a similar feature using a menu, try the [fetch\_client\_menu](https://hyprland-community.github.io/pyprland/versions/2.4.0/fetch_client_menu.html) plugin (less intrusive).

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

If you are looking for `toggle_minimized`, check the [toggle\_special](https://hyprland-community.github.io/pyprland/versions/2.4.0/toggle_special.html) plugin

## Command [​](#command)

- `expose`  Expose every client on the active workspace. If expose is already active, then restores everything and move to the focused window.

## Configuration [​](#configuration)

### `include_special` [​](#include-special)

default value is `false`

Also include windows in the special workspaces during the expose.