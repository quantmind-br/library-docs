---
title: Variables
url: https://wiki.hypr.land/Configuring/Variables/
source: sitemap
fetched_at: 2026-04-26T09:47:30.597697207-03:00
rendered_js: false
word_count: 4638
summary: This document provides a comprehensive reference for configuring Hyprland options, including definitions for variable types, color formats, and available configuration sections like general settings, decorations, and snap behavior.
tags:
    - hyprland
    - configuration
    - wayland
    - compositor
    - desktop-environment
    - reference-guide
category: reference
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

For basic syntax, see [[031-configuring|Configuring Hyprland]].

This page documents Hyprland "options". For binds, monitors, animations, etc. see the sidebar. For anything else, see [[042-configuring-keywords|Keywords]].

Layout-specific options are documented in their respective layout pages (see Sidebar for Dwindle and Master layouts).

## Variable types

| Type | Description |
|------|-------------|
| `int` | integer |
| `bool` | boolean — `true`/`false` (`yes`/`no`, `on`/`off`, `0`/`1`). Any value other than `0` or `1` causes undefined behavior. |
| `float` | floating point number |
| `color` | color (see color options below) |
| `vec2` | vector with 2 float values, separated by a space (e.g. `0 0` or `-10.9 99.1`) |
| `MOD` | string modmask (e.g. `SUPER`, `SUPERSHIFT`, `SUPER + SHIFT`, `SUPER and SHIFT`, `CTRL_SHIFT`, or empty for none). Any separator except `,` is allowed. |
| `str` | string |
| `gradient` | gradient in the form `color color ... [angle]` where `color` is a color and `angle` is in degrees (e.g. `45deg`). Angle defaults to `0deg`. Example: `rgba(11ee11ff) rgba(1111eeff) 45deg` |
| `font_weight` | integer 100–1000, or presets: `thin`, `ultralight`, `light`, `semilight`, `book`, `normal`, `medium`, `semibold`, `bold`, `ultrabold`, `heavy`, `ultraheavy` |

**Colors**

- `rgba()`, e.g. `rgba(b3ff1aee)` or decimal `rgba(179,255,26,0.933)` (no spaces)
- `rgb()`, e.g. `rgb(b3ff1a)` or decimal `rgb(179,255,26)`
- legacy: `0xeeb3ff1a` → ARGB order

**Mod list**

```ini
SHIFT CAPS CTRL/CONTROL ALT MOD2 MOD3 SUPER/WIN/LOGO/MOD4 MOD5
```

## Sections

### General

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `border_size` | border radius around windows | int | 1 |
| `gaps_in` | gaps between windows (also supports CSS-style: `top, right, bottom, left`) | int | 5 |
| `gaps_out` | gaps between windows and monitor edges (CSS-style supported) | int | 20 |
| `float_gaps` | gaps for floating windows (CSS-style supported). `-1` = default | int | 0 |
| `gaps_workspace` | gaps between workspaces. Stacks with `gaps_out` | int | 0 |
| `col.inactive_border` | inactive window border color | gradient | `0xff444444` |
| `col.active_border` | active window border color | gradient | `0xffffffff` |
| `col.nogroup_border` | inactive border for windows that cannot be grouped (see `denywindowfromgroup` dispatcher) | gradient | `0xffaaffff` |
| `col.nogroup_border_active` | active border for windows that cannot be grouped | gradient | `0xffff00ff` |
| `layout` | layout mode: `[dwindle/master/scrolling/monocle]` | str | `dwindle` |
| `no_focus_fallback` | if true, do not fall back to next available window when moving focus in a direction with no window | bool | false |
| `resize_on_border` | enable resizing by clicking and dragging on borders and gaps | bool | false |
| `extend_border_grab_area` | extends the area for click-and-drag resizing (only when `resize_on_border` is on) | int | 15 |
| `hover_icon_on_border` | show cursor icon when hovering over borders (only when `resize_on_border` is on) | bool | true |
| `allow_tearing` | master switch for tearing. See [[047-configuring-tearing|the Tearing page]] | bool | false |
| `resize_corner` | corner for forced floating windows during resize (1–4 clockwise from top-left, 0 to disable) | int | 0 |
| `modal_parent_blocking` | whether parent windows of modals will be interactive | bool | true |
| `locale` | overrides system locale (e.g. `en_US`, `es`) | str | `[[Empty]]` |

#### Snap

*Subcategory `general:snap:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `enabled` | enable snapping for floating windows | bool | false |
| `window_gap` | minimum gap in pixels between windows before snapping | int | 10 |
| `monitor_gap` | minimum gap in pixels between window and monitor edges before snapping | int | 10 |
| `border_overlap` | if true, windows snap with only one border's worth of space between them | bool | false |
| `respect_gaps` | if true, snapping respects `gaps_in` | bool | false |

> [!note]
> A subcategory is a nested category:
> ```ini
> general {
>     # ...
>     snap {
>         # ...
>     }
> }
> ```
> Doing `general:snap {` is **invalid**!

### Decoration

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `rounding` | rounded corners radius in layout px | int | 0 |
| `rounding_power` | curve exponent for rounding corners: 2.0 = circle, 4.0 = squircle, 1.0 = triangular. Range [1.0 - 10.0] | float | 2.0 |
| `active_opacity` | active window opacity [0.0 - 1.0] | float | 1.0 |
| `inactive_opacity` | inactive window opacity [0.0 - 1.0] | float | 1.0 |
| `fullscreen_opacity` | fullscreen window opacity [0.0 - 1.0] | float | 1.0 |
| `dim_modal` | enable dimming of parents of modal windows | bool | true |
| `dim_inactive` | enable dimming of inactive windows | bool | false |
| `dim_strength` | dim amount for inactive windows [0.0 - 1.0] | float | 0.5 |
| `dim_special` | dim amount when a special workspace is open [0.0 - 1.0] | float | 0.2 |
| `dim_around` | dim amount for `dim_around` window rule [0.0 - 1.0] | float | 0.4 |
| `screen_shader` | path to a custom shader applied at end of rendering. See `examples/screenShader.frag` | str | `[[Empty]]` |
| `border_part_of_window` | window border is part of the window | bool | true |

#### Blur

*Subcategory `decoration:blur:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `enabled` | enable kawase window background blur | bool | true |
| `size` | blur size (distance) | int | 8 |
| `passes` | number of passes (at least 1 required) | int | 1 |
| `ignore_opacity` | make blur layer ignore window opacity | bool | true |
| `new_optimizations` | enable further blur optimizations. Recommended to leave on | bool | true |
| `xray` | floating windows ignore tiled windows in their blur (only when `new_optimizations` is true) | bool | false |
| `noise` | noise amount [0.0 - 1.0] | float | 0.0117 |
| `contrast` | contrast modulation [0.0 - 2.0] | float | 0.8916 |
| `brightness` | brightness modulation [0.0 - 2.0] | float | 0.8172 |
| `vibrancy` | saturation boost for blurred colors [0.0 - 1.0] | float | 0.1696 |
| `vibrancy_darkness` | vibrancy strength on dark areas [0.0 - 1.0] | float | 0.0 |
| `special` | blur behind special workspace (expensive) | bool | false |
| `popups` | blur popups (e.g. right-click menus) | bool | false |
| `popups_ignore_alpha` | skip blur if pixel opacity is below value [0.0 - 1.0] | float | 0.2 |
| `input_methods` | blur input methods (e.g. fcitx5) | bool | false |
| `input_methods_ignore_alpha` | skip blur if pixel opacity is below value [0.0 - 1.0] | float | 0.2 |

> [!note]
> `blur:size` and `blur:passes` must be at least 1.
>
> Higher `blur:passes` prevents blur looking wrong on higher `blur:size` values, but requires more GPU strain.

#### Shadow

*Subcategory `decoration:shadow:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `enabled` | enable drop shadows on windows | bool | true |
| `range` | shadow range ("size") in layout px | int | 4 |
| `render_power` | falloff render power (higher = faster falloff) [1 - 4] | int | 3 |
| `sharp` | enable sharp shadows (infinite render power) | bool | false |
| `color` | shadow color. Alpha controls opacity | color | `0xee1a1a1a` |
| `color_inactive` | inactive shadow color (falls back to `color` if unset) | color | unset |
| `offset` | shadow rendering offset | vec2 | `[0, 0]` |
| `scale` | shadow scale [0.0 - 1.0] | float | 1.0 |

#### Glow

*Subcategory `decoration:glow:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `enabled` | enable inner glow on windows | bool | false |
| `range` | glow range ("size") in layout px | int | 10 |
| `render_power` | falloff render power (higher = faster falloff) [1 - 4] | int | 3 |
| `color` | glow color. Alpha controls opacity | color | `0xee1a1a1a` |
| `color_inactive` | inactive glow color (falls back to `color` if unset) | color | unset |

### Animations

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `enabled` | enable animations | bool | true |
| `workspace_wraparound` | enable workspace wraparound — directional workspace animations treat first and last workspaces as adjacent | bool | false |

### Input

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `kb_model` | XKB keymap `model` parameter | str | `[[Empty]]` |
| `kb_layout` | XKB keymap `layout` parameter | str | `us` |
| `kb_variant` | XKB keymap `variant` parameter | str | `[[Empty]]` |
| `kb_options` | XKB keymap `options` parameter | str | `[[Empty]]` |
| `kb_rules` | XKB keymap `rules` parameter | str | `[[Empty]]` |
| `kb_file` | path to custom `.xkb` file | str | `[[Empty]]` |
| `numlock_by_default` | engage numlock by default | bool | false |
| `resolve_binds_by_sym` | if true, keybinds specified by symbols are activated when typing that symbol with current layout. If false, keybinds always act as if first layout is active | bool | false |
| `repeat_rate` | key repeat rate in repeats per second | int | 25 |
| `repeat_delay` | delay before key repeat in milliseconds | int | 600 |
| `sensitivity` | mouse input sensitivity. Clamped to -1.0 to 1.0. See [libinput pointer acceleration](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration) | float | 0.0 |
| `accel_profile` | cursor acceleration profile: `adaptive`, `flat`, or `custom`. Leave empty to use libinput default. See [libinput](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration) | str | `[[Empty]]` |
| `force_no_accel` | force no cursor acceleration. **Enabling not recommended due to potential cursor desynchronization** | bool | false |
| `rotation` | device rotation in degrees clockwise. Clamped to 0–359 | int | 0 |
| `left_handed` | switches RMB and LMB | bool | false |
| `scroll_points` | scroll acceleration profile when `accel_profile` is `custom`. Form: `<step> <points>`. Leave empty for flat scroll curve | str | `[[Empty]]` |
| `scroll_method` | scroll method: `2fg` (2 fingers), `edge`, `on_button_down`, `no_scroll`. See [libinput scrolling](https://wayland.freedesktop.org/libinput/doc/latest/scrolling.html) | str | `[[Empty]]` |
| `scroll_button` | scroll button as int (check `wev` for ID). 0 = default | int | 0 |
| `scroll_button_lock` | if enabled, button press toggles lock — while locked, motion events are converted to scroll | bool | false |
| `scroll_factor` | scroll movement multiplier for external mice (separate from touchpad setting) | float | 1.0 |
| `natural_scroll` | invert scrolling direction | bool | false |
| `follow_mouse` | cursor movement effect on window focus: 0 = never, 1 = always, 2 = click moves keyboard focus, 3 = completely separate | int | 1 |
| `follow_mouse_shrink` | shrink inactive window hitboxes by this many pixels for focus detection (creates dead zone in gaps). Only with `follow_mouse = 1` | int | 0 |
| `follow_mouse_threshold` | minimum distance in logical pixels mouse must travel for window to get focused. Only with `follow_mouse = 1` | float | 0.0 |
| `focus_on_close` | window focus behavior on close: 0 = next candidate, 1 = window under cursor, 2 = most recently used | int | 0 |
| `mouse_refocus` | if disabled, mouse focus won't switch to hovered window unless mouse crosses a window boundary with `follow_mouse=1` | bool | true |
| `float_switch_override_focus` | if enabled (1 or 2), focus changes to window under cursor when switching tiled-to-floating or vice versa. If 2, focus also follows mouse on float-to-float switches | int | 1 |
| `special_fallthrough` | if enabled, floating windows in special workspace will not block focusing windows in regular workspace | bool | false |
| `off_window_axis_events` | handles axis events around focused window: 0 = ignore, 1 = send out-of-bound, 2 = fake pointer to closest point inside, 3 = warp cursor | int | 1 |
| `emulate_discrete_scroll` | emulate discrete scrolling from high resolution events: 0 = disable, 1 = non-standard events only, 2 = force enable all | int | 1 |

**Follow Mouse Cursor**

- 0 — cursor movement will not change focus
- 1 — cursor movement always changes focus to window under cursor
- 2 — cursor focus detached from keyboard focus. Clicking moves keyboard focus
- 3 — cursor focus completely separate from keyboard focus. Clicking does not change keyboard focus

**Custom Accel Profiles**

#### `accel_profile`

`custom <step> <points...>`

Example: `custom 200 0.0 0.5`

#### `scroll_points`

Only works when `accel_profile` is set to `custom`.

`<step> <points...>`

Example: `0.2 0.0 0.5 1 1.2 1.5`

To mimic Windows acceleration curves, see [this script](https://gist.github.com/fufexan/de2099bc3086f3a6c83d61fc1fcc06c9).

See [the libinput doc](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html) for more insights.

#### Touchpad

*Subcategory `input:touchpad:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `disable_while_typing` | disable touchpad while typing | bool | true |
| `natural_scroll` | invert scrolling direction | bool | false |
| `scroll_factor` | scroll movement multiplier | float | 1.0 |
| `middle_button_emulation` | LMB + RMB simultaneously = middle click. Disables any touchpad area that would normally send middle click based on location. See [libinput](https://wayland.freedesktop.org/libinput/doc/latest/middle-button-emulation.html) | bool | false |
| `tap_button_map` | tap button mapping: `lrm` (default) or `lmr` (Left, Middle, Right) | str | `[[Empty]]` |
| `clickfinger_behavior` | 1/2/3 fingers = LMB/RMB/MMB. Disables location-based click interpretation. See [libinput](https://wayland.freedesktop.org/libinput/doc/latest/clickpad-softbuttons.html#clickfinger-behavior) | bool | false |
| `tap_to_click` | tapping with 1/2/3 fingers sends LMB/RMB/MMB | bool | true |
| `drag_lock` | lifting finger during drag does not drop dragged item: 0 = disabled, 1 = enabled with timeout, 2 = enabled sticky. See [libinput](https://wayland.freedesktop.org/libinput/doc/latest/tapping.html#tap-and-drag) | int | 0 |
| `tap-and-drag` | tap and drag mode for touchpad | bool | true |
| `flip_x` | invert horizontal touchpad movement | bool | false |
| `flip_y` | invert vertical touchpad movement | bool | false |
| `drag_3fg` | three finger drag: 0 = disabled, 1 = 3 fingers, 2 = 4 fingers. See [libinput](https://wayland.freedesktop.org/libinput/doc/latest/drag-3fg.html) | int | 0 |

#### Touchdevice

*Subcategory `input:touchdevice:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `transform` | transform input from touchdevices. Same transformations as [monitors](https://wiki.hypr.land/Configuring/Monitors/#rotating). `-1` = unset | int | -1 |
| `output` | monitor to bind touch devices. Default is auto-detection. Use empty string or `[[Empty]]` to stop auto-detection | str | `[[Auto]]` |
| `enabled` | enable input for touch devices | bool | true |

#### Virtualkeyboard

*Subcategory `input:virtualkeyboard:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `share_states` | unify key down and modifier states with other keyboards: 0 = no, 1 = yes, 2 = yes unless IME client | int | 2 |
| `release_pressed_on_close` | release all pressed keys on virtual keyboard close | bool | false |

#### Tablet

*Subcategory `input:tablet:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `transform` | transform input from tablets. Same transformations as [monitors](https://wiki.hypr.land/Configuring/Monitors/#rotating). `-1` = unset | int | -1 |
| `output` | monitor to bind tablets: `current` or monitor name. Leave empty to map across all monitors | str | `[[Empty]]` |
| `region_position` | position of mapped region relative to top-left of bound monitor(s) | vec2 | `[0, 0]` |
| `absolute_region_position` | treat `region_position` as absolute position in monitor layout. Only when `output` is empty | bool | false |
| `region_size` | size of mapped region. `[0, 0]` or invalid = unset | vec2 | `[0, 0]` |
| `relative_input` | input should be relative | bool | false |
| `left_handed` | rotate tablet 180 degrees | bool | false |
| `active_area_size` | tablet active area size in mm | vec2 | `[0, 0]` |
| `active_area_position` | tablet active area position in mm | vec2 | `[0, 0]` |

### Per-device input config

Described in [[042-configuring-keywords#per-device-input-configs]].

### Gestures

*Subcategory `gestures:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `workspace_swipe_distance` | touchpad gesture distance in px | int | 300 |
| `workspace_swipe_touch` | enable workspace swiping from edge of touchscreen | bool | false |
| `workspace_swipe_invert` | invert direction (touchpad only) | bool | true |
| `workspace_swipe_touch_invert` | invert direction (touchscreen only) | bool | false |
| `workspace_swipe_min_speed_to_force` | minimum speed in px per timepoint to force change ignoring `cancel_ratio`. `0` disables this mechanic | int | 30 |
| `workspace_swipe_cancel_ratio` | swipe progress required to commence (0.7 → if > 0.7 * distance, switch, else revert) [0.0 - 1.0] | float | 0.5 |
| `workspace_swipe_create_new` | swipe right on last workspace creates a new one | bool | true |
| `workspace_swipe_direction_lock` | lock direction when swiping past `direction_lock_threshold` (touchpad only) | bool | true |
| `workspace_swipe_direction_lock_threshold` | distance in px before direction lock activates (touchpad only) | int | 10 |
| `workspace_swipe_forever` | swiping will not clamp at neighboring workspaces, continues further | bool | false |
| `workspace_swipe_use_r` | swiping uses `r` prefix instead of `m` for finding workspaces | bool | false |
| `close_max_timeout` | timeout for window to close on 1:1 gesture, in ms | int | 1000 |

> [!note]
> `workspace_swipe`, `workspace_swipe_fingers` and `workspace_swipe_min_fingers` were removed in favor of the new gestures system.
>
> Add this to replicate swiping with 3 fingers. See [[041-configuring-gestures|gestures]] page:
> ```ini
> gesture = 3, horizontal, workspace
> ```

### Group

*Subcategory `group:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `auto_group` | new windows automatically grouped into focused unlocked group. To disable for specific windows, use [[048-configuring-window-rules#group-window-rule-options|the "group barred" window rule]] | bool | true |
| `insert_after_current` | new windows in a group spawn after current or at group tail | bool | true |
| `focus_removed_window` | focus the window that was moved out of the group | bool | true |
| `drag_into_group` | dragging a window into an unlocked group merges them: 0 (disabled), 1 (enabled), 2 (only into groupbar) | int | 1 |
| `merge_groups_on_drag` | window groups can be dragged into other groups | bool | true |
| `merge_groups_on_groupbar` | groups merge when dragged into another group's groupbar | bool | true |
| `merge_floated_into_tiled_on_groupbar` | dragging floating window into tiled window groupbar merges them | bool | false |
| `group_on_movetoworkspace` | `movetoworkspace[silent]` merges window into workspace's solitary unlocked group | bool | false |
| `col.border_active` | active group border color | gradient | `0x66ffff00` |
| `col.border_inactive` | inactive group border color | gradient | `0x66777700` |
| `col.border_locked_active` | active locked group border color | gradient | `0x66ff5500` |
| `col.border_locked_inactive` | inactive locked group border color | gradient | `0x6775500` |

#### Groupbar

*Subcategory `group:groupbar:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `enabled` | enable groupbars | bool | true |
| `font_family` | font for groupbar titles. Use `misc:font_family` if not specified | str | `[[Empty]]` |
| `font_size` | groupbar title font size | int | 8 |
| `font_weight_active` | active groupbar title font weight | font_weight | `font_weight` |
| `font_weight_inactive` | inactive groupbar title font weight | font_weight | `font_weight` |
| `gradients` | enable gradients | bool | false |
| `height` | groupbar height | int | 14 |
| `indicator_gap` | gap between groupbar indicator and title | int | 0 |
| `indicator_height` | groupbar indicator height | int | 3 |
| `stacked` | render groupbar as vertical stack | bool | false |
| `priority` | decoration priority for groupbars | int | 3 |
| `render_titles` | render titles in group bar decoration | bool | true |
| `text_offset` | vertical position offset for titles | int | 0 |
| `text_padding` | horizontal padding for titles | int | 0 |
| `scrolling` | scrolling in groupbar changes group active window | bool | true |
| `rounding` | indicator rounding | int | 1 |
| `rounding_power` | curve exponent for rounding: 2.0 = circle, 4.0 = squircle, 1.0 = triangular. Range [1.0 - 10.0] | float | 2.0 |
| `gradient_rounding` | gradient rounding | int | 2 |
| `gradient_rounding_power` | curve exponent for gradient rounding: 2.0 = circle, 4.0 = squircle, 1.0 = triangular. Range [1.0 - 10.0] | float | 2.0 |
| `round_only_edges` | round only indicator edges of entire groupbar | bool | true |
| `gradient_round_only_edges` | round only gradient edges of entire groupbar | bool | true |
| `text_color` | window title color in groupbar | color | `0xffffffff` |
| `text_color_inactive` | inactive windows' title color (defaults to `text_color`) | color | unset |
| `text_color_locked_active` | active window's title color in locked group (defaults to `text_color`) | color | unset |
| `text_color_locked_inactive` | inactive windows' title color in locked groups (defaults to `text_color_inactive`) | color | unset |
| `col.active` | active group bar background color | gradient | `0x66ffff00` |
| `col.inactive` | inactive group bar background color | gradient | `0x66777700` |
| `col.locked_active` | active locked group bar background color | gradient | `0x66ff5500` |
| `col.locked_inactive` | inactive locked group bar background color | gradient | `0x6775500` |
| `gaps_in` | gap size between gradients | int | 2 |
| `gaps_out` | gap size between gradients and window | int | 2 |
| `keep_upper_gap` | add or remove upper gap | bool | true |
| `blur` | apply blur to groupbar indicators and gradients | bool | false |

### Misc

*Subcategory `misc:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `disable_hyprland_logo` | disable random Hyprland logo / anime girl background | bool | false |
| `disable_splash_rendering` | disable Hyprland splash rendering (requires monitor reload) | bool | false |
| `disable_scale_notification` | disable notification popup when monitor fails to set suitable scale | bool | false |
| `col.splash` | splash text color (requires monitor reload) | color | `0xffffffff` |
| `font_family` | global default font for debug fps/notifications/config errors, selected from system fonts | str | `Sans` |
| `splash_font_family` | font for splash text (requires monitor reload) | str | `[[Empty]]` |
| `force_default_wallpaper` | enforce default wallpapers: `0` or `1` disables anime background, `-1` = random. [-1/0/1/2] | int | -1 |
| `vrr` | VRR (Adaptive Sync): 0 = off, 1 = on, 2 = fullscreen only, 3 = fullscreen with `video`/`game` content type | int | 0 |
| `mouse_move_enables_dpms` | wake up monitors on mouse move if DPMS is off | bool | false |
| `key_press_enables_dpms` | wake up monitors on key press if DPMS is off | bool | false |
| `name_vk_after_proc` | name virtual keyboards after creating process (e.g. `/usr/bin/fcitx5` → `hl-virtual-keyboard-fcitx5`) | bool | true |
| `always_follow_on_dnd` | make mouse focus follow mouse during drag and drop. Recommended to leave enabled | bool | true |
| `layers_hog_keyboard_focus` | if true, keyboard-interactive layers (e.g. wofi, bemenu) keep focus on mouse move | bool | true |
| `animate_manual_resizes` | animate manual window resizes/moves | bool | false |
| `animate_mouse_windowdragging` | animate windows being dragged by mouse (can cause weird behavior on some curves) | bool | false |
| `disable_autoreload` | config will not reload automatically on save — requires `hyprctl reload` | bool | false |
| `enable_swallow` | enable window swallowing | bool | false |
| `swallow_regex` | *class* regex for windows to swallow (usually a terminal). For regex list, see [this cheatsheet](https://github.com/ziishaned/learn-regex/blob/master/README.md) | str | `[[Empty]]` |
| `swallow_exception_regex` | *title* regex for windows to *not* swallow (matched against parent window's title) | str | `[[Empty]]` |
| `focus_on_activate` | focus app that requests focus (`activate` request) | bool | false |
| `mouse_move_focuses_monitor` | mouse moving into different monitor focuses it | bool | true |
| `allow_session_lock_restore` | allow restarting a lockscreen app if it crashes | bool | false |
| `session_lock_xray` | keep rendering workspaces below lockscreen | bool | false |
| `background_color` | background color (requires `disable_hyprland_logo`) | color | `0x111111` |
| `close_special_on_empty` | close special workspace if last window removed | bool | true |
| `on_focus_under_fullscreen` | behavior when tiled window requests focus with fullscreen/maximized window: 0 = ignore, 1 = takes over, 2 = unfullscreen/unmaximize | int | 2 |
| `exit_window_retains_fullscreen` | closing a fullscreen window makes next focused window fullscreen | bool | false |
| `initial_workspace_tracking` | windows open on the workspace they were invoked on: 0 = disabled, 1 = single-shot, 2 = persistent (all children) | int | 1 |
| `middle_click_paste` | enable middle-click-paste (primary selection) | bool | true |
| `render_unfocused_fps` | max fps for `render_unfocused` windows in background (see also [[048-configuring-window-rules#dynamic-effects|Window-Rules `render_unfocused`]]) | int | 15 |
| `disable_xdg_env_checks` | disable warning if XDG environment is externally managed | bool | false |
| `disable_hyprland_qtutils_check` | disable warning if hyprland-qtutils is not installed | bool | false |
| `lockdead_screen_delay` | delay before "lockdead" screen appears if lockscreen app fails to cover all outputs (5 seconds max) | int | 1000 |
| `enable_anr_dialog` | show ANR (app not responding) dialog when apps hang | bool | true |
| `anr_missed_pings` | missed pings before showing ANR dialog | int | 5 |
| `size_limits_tiled` | apply min_size and max_size rules to tiled windows | bool | false |
| `disable_watchdog_warning` | disable warning about not using start-hyprland | bool | false |

### Layout

*Subcategory `layout:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `single_window_aspect_ratio` | add padding so single window on screen conforms to specified aspect ratio. `4 3` on 16:9 screen creates 4:3 window with side padding | Vec2 | `0 0` |
| `single_window_aspect_ratio_tolerance` | tolerance for `single_window_aspect_ratio`: if padding would be smaller than specified fraction of height/width, don't adjust | float | 0.1 |

### Binds

*Subcategory `binds:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `pass_mouse_when_bound` | if disabled, mouse events are not passed to apps / window dragging when a keybind has been triggered | bool | false |
| `scroll_event_delay` | ms to wait after scroll event before passing another for binds | int | 300 |
| `workspace_back_and_forth` | switching to focused workspace switches to previous workspace (i3-style `auto_back_and_forth`) | bool | false |
| `hide_special_on_workspace_change` | changing active workspace hides special workspace on that monitor | bool | false |
| `allow_workspace_cycles` | workspaces remember previous workspace, enabling cycles | bool | false |
| `workspace_center_on` | workspace switching centers cursor on workspace (0) or on last active window (1) | int | 0 |
| `focus_preferred_method` | preferred focus finding method for `focuswindow`/`movewindow`/etc with direction: 0 = history (recent priority), 1 = length (longer shared edges priority) | int | 0 |
| `ignore_group_lock` | if enabled, `moveintogroup`, `moveoutofgroup`, `movewindoworgroup` dispatchers ignore group lock | bool | false |
| `movefocus_cycles_fullscreen` | if enabled, `movefocus` cycles fullscreen on fullscreen window, otherwise moves in direction | bool | false |
| `movefocus_cycles_groupfirst` | if enabled, `movefocus` cycles windows in groups first, then moves to other windows/groups at each tab end | bool | false |
| `window_direction_monitor_fallback` | moving window or focus over monitor edge moves to next monitor in that direction | bool | true |
| `disable_keybind_grabbing` | apps that request keybinds disabled (e.g. VMs) will not be able to do so | bool | false |
| `allow_pin_fullscreen` | allow fullscreen on pinned windows, restore pinned status afterwards | bool | false |
| `drag_threshold` | movement threshold in pixels for window dragging and `c`/`g` bind flags. 0 = grab on mousedown | int | 0 |

### XWayland

*Subcategory `xwayland:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `enabled` | allow running X11 applications | bool | true |
| `use_nearest_neighbor` | use nearest neighbor filtering for XWayland apps (pixelated, not blurry) | bool | true |
| `force_zero_scaling` | force scale of 1 on XWayland windows on scaled displays | bool | false |
| `create_abstract_socket` | create [abstract Unix domain socket](https://wiki.hypr.land/Configuring/XWayland/#abstract-unix-domain-socket) for XWayland connections (requires XWayland restart; Linux only) | bool | false |

### OpenGL

*Subcategory `opengl:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `nvidia_anti_flicker` | reduces flickering on Nvidia at cost of possible frame drops on lower-end GPUs. Ignored on non-Nvidia | bool | true |

### Render

*Subcategory `render:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `direct_scanout` | direct scanout reduces lag for single fullscreen app on screen (e.g. game). Recommended to set false if graphical glitches appear: 0 = off, 1 = on, 2 = auto (on with content type 'game') | int | 0 |
| `expand_undersized_textures` | expand undersized textures along edge, or stretch entire texture | bool | true |
| `xp_mode` | disables back buffer and bottom layer rendering | bool | false |
| `ctm_animation` | fade animation for CTM changes (hyprsunset): 2 = auto (disables on Nvidia) | int | 2 |
| `cm_enabled` | enable color management pipeline (requires Hyprland restart) | bool | true |
| `send_content_type` | report content type to allow monitor profile autoswitch (may cause black screen during switch) | bool | true |
| `cm_auto_hdr` | auto-switch to HDR in fullscreen when needed: 0 = off, 1 = switch to `cm, hdr`, 2 = switch to `cm, hdredid` | int | 1 |
| `new_render_scheduling` | automatically use triple buffering when needed, improves FPS on underpowered devices | bool | false |
| `non_shader_cm` | enable CM without shader: 0 = disable, 1 = whenever possible, 2 = DS and passthrough only, 3 = disable and ignore CM issues | int | 2 |
| `non_shader_cm_interop` | external ctm (hypersunset, etc.) in fullscreen: 0 = disabled, 1 = enabled, 2 = disabled for photo/video/game content types | int | 2 |
| `cm_sdr_eotf` | default transfer function for SDR apps: `default` (sRGB), `gamma22`, `gamma22force`, `srgb` | str | `default` |
| `commit_timing_enabled` | enable commit timing proto (requires restart) | bool | true |
| `use_fp16` | use FP16 buffers internally: 0 = disabled, 1 = enabled, 2 = enabled in HDR mode | int | 2 |
| `keep_unmodified_copy` | keep unmodified SDR frame copy for screenshots: 0 = disabled, 1 = on, 2 = auto (enabled in HDR with SDR modifiers). Set to 1 if screenshots are transparent | int | 2 |
| `use_shader_blur_blend` | use experimental blurred bg blending (glitched on rotated screens). Set to true if blur is missing with fp16 or `keep_unmodified_copy` | bool | false |

> [!info]
> `cm_auto_hdr` requires `--target-colorspace-hint-mode=source` mpv option to work with mpv versions greater than v0.40.0

### Cursor

*Subcategory `cursor:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `invisible` | don't render cursors | bool | false |
| `sync_gsettings_theme` | sync xcursor theme with gsettings — applies `cursor-theme` and `cursor-size` on theme load, making most CSD GTK clients use same xcursor theme and size | bool | true |
| `no_hardware_cursors` | hardware cursors: 0 = use if possible, 1 = don't use, 2 = auto (disable when tearing) | int | 2 |
| `no_break_fs_vrr` | disable scheduling new frames on cursor movement for fullscreen VRR apps to avoid framerate spikes (may require `no_hardware_cursors = true`): 0 = off, 1 = on, 2 = auto (on with content type 'game') | int | 2 |
| `min_refresh_rate` | minimum refresh rate for cursor movement when `no_break_fs_vrr` is active. Set to minimum supported refresh rate or higher | int | 24 |
| `hotspot_padding` | padding in logical px between screen edges and cursor | int | 1 |
| `inactive_timeout` | seconds after cursor inactivity to hide it. `0` = never | float | 0 |
| `no_warps` | do not warp cursor in many cases (focusing, keybinds, etc.) | bool | false |
| `persistent_warps` | when window is refocused, cursor returns to its last position relative to that window, not center | bool | false |
| `warp_on_change_workspace` | move cursor to last focused window after changing workspace: 0 (Disabled), 1 (Enabled), 2 (Force — ignores `cursor:no_warps`) | int | 0 |
| `warp_on_toggle_special` | move cursor to last focused window when toggling special workspace: 0 (Disabled), 1 (Enabled), 2 (Force — ignores `cursor:no_warps`) | int | 0 |
| `default_monitor` | default monitor for cursor on startup (see `hyprctl monitors` for names) | str | `[[EMPTY]]` |
| `zoom_factor` | zoom factor around cursor (magnifying glass). Minimum 1.0 (no zoom) | float | 1.0 |
| `zoom_rigid` | zoom follows cursor rigidly (cursor always centered if possible) or loosely | bool | false |
| `zoom_detached_camera` | detach camera from mouse when zoomed in — only move camera to keep mouse in view when it goes past screen edges | bool | true |
| `enable_hyprcursor` | enable hyprcursor support | bool | true |
| `hide_on_key_press` | hide cursor when any key is pressed until mouse is moved | bool | false |
| `hide_on_touch` | hide cursor when last input was touch until mouse input is done | bool | false |
| `hide_on_tablet` | hide cursor when last input was tablet until tablet input is done | bool | false |
| `use_cpu_buffer` | make HW cursors use CPU buffer. Required on Nvidia for HW cursors: 0 = off, 1 = on, 2 = auto (Nvidia only) | int | 2 |
| `warp_back_after_non_mouse_input` | warp cursor back to where it was after using non-mouse input, then returning to mouse | bool | false |
| `zoom_disable_aa` | disable antialiasing when zooming (pixelated instead of blurry) | bool | false |

### Ecosystem

*Subcategory `ecosystem:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `no_update_news` | disable popup on Hyprland update | bool | false |
| `no_donation_nag` | disable semi-annual donation popup | bool | false |
| `enforce_permissions` | enable [[045-configuring-permissions|permission control]] | bool | false |

### Quirks

*Subcategory `quirks:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `prefer_hdr` | report HDR mode as preferred: 0 = off, 1 = always, 2 = gamescope only | int | 0 |

> [!warning]
> Some clients expect monitor in HDR mode prior to client start. This breaks auto HDR activation and can cause whitescreen and flickering. Use `prefer_hdr` to fix it.

### Debug

*Subcategory `debug:`*

| Name | Description | Type | Default |
|------|-------------|------|---------|
| `overlay` | print debug performance overlay. Disable VFR for accurate results | bool | false |
| `damage_blink` | (epilepsy warning!) flash areas updated with damage tracking | bool | false |
| `gl_debugging` | enable OpenGL debugging with glGetError and EGL_KHR_debug (requires restart) | bool | false |
| `vfr` | VFR status of Hyprland. Recommended to leave enabled to conserve resources | bool | true |
| `disable_logs` | disable logging to file | bool | true |
| `disable_time` | disable time logging | bool | true |
| `damage_tracking` | redraw only needed bits of display. Do **not** change: `full-2` = default, `monitor-1`, `none-0` | int | 2 |
| `enable_stdout_logs` | enable logging to stdout | bool | false |
| `manual_crash` | set to 1 then back to 0 to crash Hyprland | int | 0 |
| `suppress_errors` | do not display config file parsing errors | bool | false |
| `watchdog_timeout` | watchdog timeout in seconds to abort processing of main thread signal. `0` to disable | int | 5 |
| `disable_scale_checks` | disable verification of scale factors (will result in pixel alignment and rounding errors) | bool | false |
| `error_limit` | limit displayed config file parsing errors | int | 5 |
| `error_position` | error bar position: top = 0, bottom = 1 | int | 0 |
| `colored_stdout_logs` | enable colors in stdout logs | bool | true |
| `pass` | enable render pass debugging | bool | false |
| `full_cm_proto` | claim support for all cm proto features (requires restart) | bool | false |
| `debug:invalidate_fp16` | allow fp16 buffer invalidation (improves performance but produces glitches on some systems): 0 = not allowed, 1 = allowed, 2 = not allowed on Nvidia | int | 2 |

### More

More config options are described in other pages — layout- or circumstance-specific. See the sidebar for more pages.
