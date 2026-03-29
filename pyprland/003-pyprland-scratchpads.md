---
title: scratchpads | Pyprland web
url: https://hyprland-community.github.io/pyprland/scratchpads
source: github_pages
fetched_at: 2026-01-31T16:02:25.529361863-03:00
rendered_js: false
word_count: 517
summary: This document explains how to configure and use scratchpads in Hyprland with Pyprland, covering setup, animations, sizing, positioning, and advanced options for customizing window behavior.
tags:
    - scratchpad
    - hyprland
    - window-management
    - configuration
    - pyprland
    - animations
    - window-positioning
category: guide
---

Easily toggle the visibility of applications you use the most.

Configurable and flexible, while supporting complex setups it's easy to get started with:

toml

```
[scratchpads.name]
command = "command to run"
class = "the window's class"  # check: hyprctl clients | grep class
size = "[width] [height]"  # size of the window relative to the screen size
```

Example

As an example, defining two scratchpads:

- *term* which would be a kitty terminal on upper part of the screen
- *volume* which would be a pavucontrol window on the right part of the screen

toml

```
[scratchpads.term]
animation = "fromTop"
command = "kitty --class kitty-dropterm"
class = "kitty-dropterm"
size = "75% 60%"
max_size = "1920px 100%"
margin = 50

[scratchpads.volume]
animation = "fromRight"
command = "pavucontrol"
class = "org.pulseaudio.pavucontrol"
size = "40% 90%"
unfocus = "hide"
lazy = true
```

Shortcuts are generally needed:

ini

```
bind = $mainMod,V,exec,pypr toggle volume
bind = $mainMod,A,exec,pypr toggle term
bind = $mainMod,Y,exec,pypr attach
```

- If you wish to have a more generic space for any application you may run, check [toggle\_special](https://hyprland-community.github.io/pyprland/toggle_special.html).
- When you create a scratchpad called "name", it will be hidden in `special:scratch_<name>`.
- Providing `class` allows a glitch free experience, mostly noticeable when using animations

## Commands [​](#commands)

Loading commands...

TIP

You can use `"*"` as a *scratchpad name* to target every scratchpad when using `show` or `hide`. You'll need to quote or escape the `*` character to avoid interpretation from your shell.

## Configuration [​](#configuration)

Loading configuration...

### `command` [​](#config-command)

This is the command you wish to run in the scratchpad. It supports [variables](https://hyprland-community.github.io/pyprland/Variables.html).

### `class` [​](#config-class)

Allows *Pyprland* prepare the window for a correct animation and initial positioning. Check your window's class with: `hyprctl clients | grep class`

### `animation` [​](#config-animation)

Type of animation to use:

- `null` / `""` (no animation)
- `fromTop` (stays close to upper screen border)
- `fromBottom` (stays close to lower screen border)
- `fromLeft` (stays close to left screen border)
- `fromRight` (stays close to right screen border)

### `size` [​](#config-size)

Each time scratchpad is shown, window will be resized according to the provided values.

For example on monitor of size `800x600` and `size= "80% 80%"` in config scratchpad always have size `640x480`, regardless of which monitor it was first launched on.

> #### Format [​](#format)
> 
> String with "x y" (or "width height") values using some units suffix:
> 
> - **percents** relative to the focused screen size (`%` suffix), eg: `60% 30%`
> - **pixels** for absolute values (`px` suffix), eg: `800px 600px`
> - a mix is possible, eg: `800px 40%`

### `position` [​](#config-position)

Overrides the automatic margin-based position. Sets the scratchpad client window position relative to the top-left corner.

Same format as `size` (see above)

Example of scratchpad that always sits on the top-right corner of the screen:

toml

```
[scratchpads.term_quake]
command = "wezterm start --class term_quake"
position = "50% 0%"
size = "50% 50%"
class = "term_quake"
```

NOTE

If `position` is not provided, the window is placed according to `margin` on one axis and centered on the other.

### `margin` [​](#config-margin)

Pixels from the screen edge when using animations. Used to position the window along the animation axis.

### `max_size` [​](#config-max-size)

Maximum window size. Same format as `size`. Useful to prevent scratchpads from growing too large on big monitors.

### `multi` [​](#config-multi)

When set to `false`, only one client window is supported for this scratchpad. Otherwise other matching windows will be **attach**ed to the scratchpad. Allows the `attach` command on the scratchpad.

### `lazy` [​](#config-lazy)

When `true`, the scratchpad command is only started on first use instead of at startup.

## Advanced configuration [​](#advanced-configuration)

To go beyond the basic setup and have a look at every configuration item, you can read the following pages:

- [Advanced](https://hyprland-community.github.io/pyprland/scratchpads_advanced.html) contains options for fine-tuners or specific tastes (eg: i3 compatibility)
- [Non-Standard](https://hyprland-community.github.io/pyprland/scratchpads_nonstandard.html) contains options for "broken" applications like progressive web apps (PWA) or emacsclient, use only if you can't get it to work otherwise