---
title: Configuration
url: https://github.com/asmvik/yabai/wiki/Configuration
source: wiki
fetched_at: 2026-02-11T07:34:25.375176-03:00
rendered_js: false
word_count: 1143
summary: This document provides a comprehensive guide to configuring the yabai window manager for macOS, detailing setup procedures, tiling behaviors, and user interface customizations.
tags:
    - yabai
    - macos-customization
    - window-management
    - tiling-layout
    - configuration-guide
category: configuration
---

A short and concise overview of options available with your current installation is available using `man yabai` or for the current development version as a [&rightarrow;&nbsp;rendered document][docs-config].

### Configuration file

The per-user yabai configuration file is just a shell script that's ran before yabai launches. It is executed using `/usr/bin/env sh -c <config_file>` if the exec-bit is set, or interpreted using `/usr/bin/env sh <config_file>` if not. It must be placed at one of the following places (in order):

 - `$XDG_CONFIG_HOME/yabai/yabairc`
 - `$HOME/.config/yabai/yabairc`
 - `$HOME/.yabairc`

```sh
# create empty configuration file and make it executable
touch ~/.yabairc
chmod +x ~/.yabairc
```

All of the configuration options can be changed at runtime as well.

### Debug output and error reporting

In the case that something is not working as you're expecting, please make sure to take a look in the output and error log. To enable debug output make sure that your configuration file contains `yabai -m config debug_output on` or that yabai is launched with the `--verbose` flag. If you are running yabai as a service, the output and error log can be viewed as follows: 

```sh
# view the last lines of the error log 
tail -f /tmp/yabai_$USER.err.log

# view the last lines of the debug log
tail -f /tmp/yabai_$USER.out.log
```

### Tiling options

#### Layout

Layout defines whether windows are tiled ("managed", "bsp") by yabai or left alone ("float"). This setting can be defined on a per–space basis.

```sh
# bsp or float (default: float)
yabai -m config layout bsp

# Override default layout for space 2 only
yabai -m config --space 2 layout float
```

By default, new windows become the right or bottom split when tiled, which can be changed to left or top.

```
# New window spawns to the left if vertical split, or top if horizontal split
yabai -m config window_placement first_child

# New window spawns to the right if vertical split, or bottom if horizontal split
yabai -m config window_placement second_child
```

#### Padding and gaps

When tiling windows, yabai can maintain gaps between windows and padding towards menu bar, dock and screen edges. This setting can be defined on a per–space basis.

```sh
# Set all padding and gaps to 20pt (default: 0)
yabai -m config top_padding    20
yabai -m config bottom_padding 20
yabai -m config left_padding   20
yabai -m config right_padding  20
yabai -m config window_gap     20

# Override gaps for space 2 only
yabai -m config --space 2 window_gap 0
```

#### Split ratios

Auto balance makes it so all windows always occupy the same space, independent of how deeply nested they are in the window tree. When a new window is inserted or a window is removed, the split ratios will be automatically adjusted.

```sh
# on or off (default: off)
yabai -m config auto_balance off
```

If auto balance is disabled, the split ratio defines how much space each window occupies after a new split is created. A value of 0.5 means that both old and new window occupy the same space; a value of 0.2 means that the old window occupies 20% of the available space and the new window occupies 80% of the available space. New windows are inserted at the right or bottom side. The ratio needs to be between 0 and 1.

```sh
# Floating point value between 0 and 1 (default: 0.5)
yabai -m config split_ratio 0.5
```

### Mouse support

If you resize a tiled window, yabai will attempt to adjust splits to fit automatically.

When you drag a tiled window onto another, yabai will either swap their positions in the window tree, or modify the window tree by splitting the region occupied by the window. The action is determined by drop-zones; 25% of the region towards a particular edge will result in a warp operation towards that direction, and the center (50%) of the window will trigger either a swap or stack operation (based on the value of `yabai -m config mouse_drop_action`). See [this picture](https://user-images.githubusercontent.com/4488655/61372700-23c32e00-a898-11e9-8052-aeb5db9f4e13.png) for a visual illustration.

Additionally, yabai can enable you to move and resize windows by clicking anywhere on them while holding a modifier key.

```sh
# set mouse interaction modifier key (default: fn)
yabai -m config mouse_modifier fn

# set modifier + left-click drag to move window (default: move)
yabai -m config mouse_action1 move

# set modifier + right-click drag to resize window (default: resize)
yabai -m config mouse_action2 resize
```

With focus follows mouse, you can also focus windows without having to click on them. This can be set to either autofocus (window gets focused, but not raised) or autoraise (window gets raised as if it was clicked on). Focus follows mouse is disabled while holding the mouse modifier key so that you can access the menu bar easily.

```sh
# set focus follows mouse mode (default: off, options: off, autoraise, autofocus)
yabai -m config focus_follows_mouse autoraise
```

Mouse follows focus makes it so that when yabai focuses another window (e.g. through a focus command), the mouse cursor gets moved to the center of the focused window.

```sh
# set mouse follows focus mode (default: off)
yabai -m config mouse_follows_focus on
```

### Window modifications

yabai allows modifying the way macOS presents windows. 

```sh
# modify window shadows (default: on, options: on, off, float)
# example: show shadows only for floating windows
yabai -m config window_shadow float

# window opacity (default: off)
# example: render all unfocused windows with 90% opacity
yabai -m config window_opacity on
yabai -m config active_window_opacity 1.0
yabai -m config normal_window_opacity 0.9
```

### Status bar

Third-party tools like [&rightarrow;&nbsp;Übersicht][gh-uebersicht] and [&rightarrow;&nbsp;Sketchybar][gh-sketchybar] can be used to create custom status bars.

There is also an option to integrate your custom bar with the padding functionality (specifically: `space --toggle padding`)  that yabai provides. Note that you do not need to include this padding in the regular space settings.

```sh
# add 20 padding to the top and 0 padding to the bottom of every space located on the main display
yabai -m config external_bar main:20:0
# add 20 padding to the top and bottom of all spaces regardless of the display it belongs to
yabai -m config external_bar all:20:20
``` 

You can turn on autohiding of the macOS menubar so that it only shows up when you move your cursor to access it: 

```
macOS Big Sur:
System Preferences -> General -> Automatically hide and show the menu bar.

macOS Monterey:
System Preferences -> Dock & Menu bar -> Select Dock & Menu bar in left sidebar

macOS Ventura:
System Settings -> Desktop & Dock -> Scroll down to the Menu Bar heading

macOS Sonoma:
System Settings -> Control Centre -> Scroll down to "Automatically Hide and Show the menu bar"
```

In yabai v6.0.12+ you can also completely disable the menubar using `yabai -m config menubar_opacity 0.0`regardless this setting.

[docs-config]: ./009-yabai-docs.md#config
[gh-uebersicht]: https://github.com/felixhageloh/uebersicht
[gh-sketchybar]: https://github.com/felixkratz/sketchybar