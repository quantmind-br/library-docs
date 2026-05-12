---
title: Window Rules
url: https://wiki.hypr.land/Configuring/Window-Rules/
source: sitemap
fetched_at: 2026-04-26T09:48:19.112333198-03:00
rendered_js: false
word_count: 2190
summary: This document explains how to configure window rules in Hyprland to control window behavior, appearance, and placement based on specific properties.
tags:
    - hyprland
    - window-management
    - configuration
    - window-rules
    - linux-desktop
    - regex
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

> [!warning]
> Rules are evaluated top to bottom, so order matters! See [[#notes]].

## Window Rules

Window rules control window behavior, appearance, and placement based on window properties.

### Syntax

Named rule:

```ini
windowrule {
  name = apply-something
  match:class = my-window
  border_size = 10
}
```

Anonymous rule:

```ini
windowrule = match:class my-window, border_size 10
```

Rules have two parameter categories: **props** (match conditions) and **effects** (applied changes). All props must match for a rule to apply. Multiple props and effects per rule are allowed in any order, as long as only one of each type is specified and at least one prop exists.

### Props

| Field | Argument | Description |
|-------|----------|-------------|
| `match:class` | RegEx | Windows with `class` matching RegEx |
| `match:title` | RegEx | Windows with `title` matching RegEx |
| `match:initial_class` | RegEx | Windows with `initialClass` matching RegEx |
| `match:initial_title` | RegEx | Windows with `initialTitle` matching RegEx |
| `match:tag` | name | Windows with matching `tag` |
| `match:xwayland` | bool | Xwayland windows |
| `match:float` | bool | Floating windows |
| `match:fullscreen` | bool | Fullscreen windows |
| `match:pin` | bool | Pinned windows |
| `match:focus` | bool | Currently focused window |
| `match:group` | bool | Grouped windows |
| `match:modal` | bool | Modal windows (e.g. "Are you sure" popups) |
| `match:fullscreen_state_client` | client | `fullscreenstate`: `0` none, `1` maximize, `2` fullscreen, `3` maximize+fullscreen |
| `match:fullscreen_state_internal` | internal | `fullscreenstate`: same values as above |
| `match:workspace` | workspace | Windows on matching workspace (`w` = id, `name:string`, or workspace selector) |
| `match:content` | int | Content type: `0` none, `1` photo, `2` video, `3` game |
| `match:xdg_tag` | RegEx | Match by xdgTag (see `hyprctl clients`) |

> [!note]
> Use `hyprctl clients` to get window class, title, XWayland status, and size.
> `fullscreen` in `hyprctl clients` output = `fullscreen_state_internal`; `fullscreenClient` = `fullscreen_state_client`.

### RegEx writing

Hyprland uses [Google's RE2](https://github.com/google/re2) — polynomial-time-only operations will not work. See [RE2 wiki](https://github.com/google/re2/wiki/Syntax).

To negate a RegEx (pass when RegEx fails), prefix with `negative:`, e.g.: `negative:kitty`.

## Effects

### Static effects

Static effects are evaluated once at window open. Always uses `initialTitle` and `initialClass` for matching.

> [!warning]
> Cannot `float` or apply other static rules based on title changes after window creation.

| Effect | Argument | Description |
|--------|----------|-------------|
| `float` | on | Floats the window |
| `tile` | on | Tiles the window |
| `fullscreen` | on | Fullscreens the window |
| `maximize` | on | Maximizes the window |
| `fullscreen_state` | internal client | Sets fullscreen mode where `0` none, `1` maximize, `2` fullscreen, `3` maximize+fullscreen |
| `move` | expr expr | Moves floating window to monitor-local coordinates (space-separated) |
| `size` | expr expr | Resizes floating window (space-separated) |
| `center` | on | Centers floating window |
| `pseudo` | on | Pseudotiles the window |
| `monitor` | id | Monitor for window (`id` number or name e.g. `DP-1`) |
| `workspace` | w | Workspace for window (see [[061-configuring-dispatchers/#workspaces]]); `unset` clears rules; add `silent` for silent open |
| `no_initial_focus` | on | Disables initial focus |
| `pin` | on | Pins window to all workspaces (floating only) |
| `group` | options | Set window group properties — see [[#group-window-rule-options]] |
| `suppress_event` | types... | Ignores events: `fullscreen`, `maximize`, `activate`, `activatefocus`, `fullscreenoutput` (space-separated) |
| `content` | none\|photo\|video\|game | Sets content type |
| `no_close_for` | ms | Window uncloseable with `killactive` dispatcher for ms on open |
| `scrolling_width` | float | Set column width for scrolling layout |

#### Expressions

Math expressions, space-separated (no spaces in math). Variables:

- `monitor_w`, `monitor_h` — monitor size
- `window_x`, `window_y` — window position
- `window_w`, `window_h` — window size
- `cursor_x`, `cursor_y` — cursor position

Examples:
- `window_w*0.5`
- `(monitor_w/2)+17`
- `(monitor_w*0.5) (monitor_h*0.5)`
- `((monitor_w*0.5)+17) (monitor_h*0.2)`

### Dynamic effects

Dynamic effects re-evaluate when window properties change.

| Effect | Argument | Description |
|--------|----------|-------------|
| `persistent_size` | on | Floating windows: store size; restore for new windows with same class/title |
| `no_max_size` | on | Removes max size limits — useful for windows with invalid max sizes (e.g. winecfg) |
| `stay_focused` | on | Forces focus while visible |
| `animation` | style (opt) | Forces animation style with optional opt |
| `border_color` | c | Sets border color/gradient. Options: `color` or `color ... color angle` (active); `color color` or `color ... color angle color ... color [angle]` (active+inactive). See [[067-configuring-variables/#variable-types]] |
| `idle_inhibit` | mode | Idle inhibit rule. Modes: `none`, `always`, `focus`, `fullscreen` |
| `opacity` | a | Opacity multiplier. `float` = overall; `float float` = active/inactive; `float float float` = active/inactive/fullscreen |
| `tag` | name | Applies tag. Prefix `+`/`-` to set/unset, no prefix to toggle |
| `max_size` | w h | Max size for floating windows (use `misc:size_limits_tiled` for tiled) |
| `min_size` | w h | Min size for floating windows (use `misc:size_limits_tiled` for tiled) |
| `border_size` | int | Border size |
| `rounding` | int | Force X pixels rounding (ignores `decoration:rounding`) |
| `rounding_power` | float | Override rounding power (see `decoration:rounding_power`) |
| `allows_input` | on | Force XWayland window to receive input (fixes some game launcher focus issues) |
| `dim_around` | on | Dims everything around window (for floating windows; tiled may behave strangely) |
| `decorate` | on | Whether to draw decorations (default true) |
| `focus_on_activate` | on | Focus window requesting focus (`activate` request) |
| `keep_aspect_ratio` | on | Force aspect ratio during mouse resize |
| `nearest_neighbor` | on | Force [nearest neighbor](https://en.wikipedia.org/wiki/Image_scaling#Nearest-neighbor_interpolation) filtering |
| `no_anim` | on | Disable animations |
| `no_blur` | on | Disable blur |
| `no_dim` | on | Disable dimming |
| `no_focus` | on | Disable focus |
| `no_follow_mouse` | on | Prevent focus when mouse moves over (with `input:follow_mouse=1`) |
| `no_shadow` | on | Disable shadows |
| `no_shortcuts_inhibit` | on | Allow [shortcuts](https://wayland.app/protocols/keyboard-shortcuts-inhibit-unstable-v1) inhibition |
| `no_screen_share` | on | Hide window from screen sharing (black rectangles) |
| `no_vrr` | on | Disable VRR (only works when `misc:vrr` is `2` or `3`) |
| `opaque` | on | Force opaque |
| `force_rgbx` | on | Ignore alpha channel, make fully opaque |
| `sync_fullscreen` | on | Fullscreen mode always matches window's (takes effect on next change) |
| `immediate` | on | Allow tearing — see [[047-configuring-tearing]] |
| `xray` | on | Blur xray mode |
| `render_unfocused` | on | Render window even when not visible — see [[067-configuring-variables/#misc]] for `render_unfocused_fps` |
| `scroll_mouse` | float | Override `input:scroll_factor` |
| `scroll_touchpad` | float | Override `input:touchpad:scroll_factor` |

All dynamic effects can be set with `setprop` — see [[061-configuring-dispatchers/#setprop]].

### Group window rule options

- `set` (`always`) — Open as group
- `new` — Shorthand for `barred set`
- `lock` (`always`) — Lock the group that added window (use with `set` or `new`)
- `barred` — Do not auto-group into focused unlocked group
- `deny` — Cannot be toggled as or added to a group (see `denywindowfromgroup` dispatcher)
- `invade` — Force open in locked group
- `override` other options — Override other `group` rules
- `unset` — Clear all `group` rules

> [!note]
> `group` without options = shorthand for `group set`. `set` and `lock` affect new windows once by default; `always` qualifier makes them persistent.

### Tags

Windows may have static or dynamic tags (dynamic have `*` suffix). Check tags with `hyprctl clients`.

`tagwindow` dispatcher — static tags:

```bash
hyprctl dispatch tagwindow +code     # Add tag to current window
hyprctl dispatch tagwindow -- -code  # Remove tag (use `--` for leading `-`)
hyprctl dispatch tagwindow code      # Toggle tag
# Tag windows by RegEx:
hyprctl dispatch tagwindow +music deadbeef
hyprctl dispatch tagwindow +media title:Celluloid
```

`tag` rule — dynamic tags:

```ini
windowrule = tag +term, match:class footclient  # Add dynamic tag `term*`
windowrule = tag term, match:class footclient   # Toggle dynamic tag `term*`
windowrule = tag +code, match:tag cpp           # Add `code*` to window tagged `cpp`
windowrule = opacity 0.8, match:tag code        # Set opacity for `code` or `code*`
windowrule = opacity 0.7, match:tag cpp         # `cpp` matches both, last wins
windowrule = opacity 0.6, match:tag term*       # Only `term*` matches (exact)
windowrule = tag -code, match:tag  term          # Remove `code*` from `term` or `term*`
```

Keybind convenience:

```ini
bind = $mod Ctrl, 2, tagwindow, alpha_0.2
bind = $mod Ctrl, 4, tagwindow, alpha_0.4
windowrule = opacity 0.2 override, match:tag alpha_0.2
windowrule = opacity 0.4 override, match:tag alpha_0.4
```

> [!note]
> `tag` rule manipulates dynamic tags only; `tagwindow` dispatcher works with static tags only (calling dispatcher clears dynamic tags).

### Example Rules

```ini
# Move kitty to 100 100 with animation
windowrule {
  name = move-kitty
  match:class = kitty
  move = 100 100
  animation = popin
}
windowrule = no_blur on, match:class firefox
windowrule = move (cursor_x-(window_w*0.5)) (cursor_y-(window_h*0.5)), match:class kitty
windowrule = border_color rgb(FF0000) rgb(880808), match:fullscreen 1
windowrule = border_color rgb(FFFF00), match:title .*Hyprland.*
windowrule = opacity 1.0 override 0.5 override 0.8 override, match:class kitty
windowrule = match:class kitty, rounding 10
windowrule = match:class (pinentry-)(.*), stay_focused on
```

### Notes

Dynamic effects re-evaluate when matching properties change. Effects process top to bottom; **last match wins**.

```ini
windowrule = opacity 0.8 0.8, match:class kitty
windowrule = opacity 0.5 0.5, match:float yes
```
Non-fullscreen kitty → `0.8` opacity; floating kitty → `0.5` (last rule wins).

```ini
windowrule = opacity 0.5 0.5, match:float true
windowrule = opacity 0.8 0.8, match:class kitty
```
All kitty windows → `0.8` (including floating).

> [!important]
> Named rules take precedence over anonymous ones. All named rules evaluate first, then all anonymous rules.

> [!note]
> Opacity multiplies by default. `active_opacity=0.5` + `opacity=0.5` = `0.25` total. Products over `1.0` cause glitches (e.g. `0.5*4=2`). Use `override` for exact values:

```ini
windowrule = match:class kitty, opacity 0.8 override 0.8 override 1.0 override
```

### Dynamically enabling / disabling / changing rules

Only **named** rules support dynamic changes.

Enable/disable:

```sh
hyprctl keyword 'windowrule[my-rule-name]:enable false'
```

Change properties:

```sh
hyprctl keyword 'windowrule[my-rule-name]:match:class kitty'
```

> [!note]
> Singlequotes are required to prevent shell parsing.

## Layer Rules

Layers (app launchers, status bars, wallpapers) use similar syntax but separate props/effects.

### Props

| Field | Argument | Description |
|-------|----------|-------------|
| `match:namespace` | RegEx | Layer namespace (check `hyprctl layers`) |

### Effects

| Effect | Argument | Description |
|--------|----------|-------------|
| `no_anim` | on | Disable animations |
| `blur` | on | Enable blur |
| `blur_popups` | on | Enable blur for popups |
| `ignore_alpha` | a | Blur ignores pixels with opacity ≤ a (float 0-1; `0` if unspecified) |
| `dim_around` | on | Dim everything behind layer |
| `xray` | on | Blur xray mode: `0` off, `1` on, `unset` default |
| `animation` | style | Set animation style |
| `order` | n | Stacking order relative to other layers; higher = closer to monitor edge; can be negative (`0` if unspecified) |
| `above_lock` | 0/1/2 | Render above lockscreen: `1` = above, `2` = interact on lockscreen |
| `no_screen_share` | on | Hide from screen sharing (black rectangle) |

### Examples

```
layerrule = blur on, match:namespace waybar

layerrule {
  name = no_anim_for_selection
  no_anim = on
  match:namespace = selection
}
```
