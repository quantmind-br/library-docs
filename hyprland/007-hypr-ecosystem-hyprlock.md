---
title: hyprlock
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprlock/
source: sitemap
fetched_at: 2026-04-26T09:47:58.755353504-03:00
rendered_js: false
word_count: 1659
summary: GPU-accelerated screen locker for Hyprland with PAM/fingerprint auth, animations, and widget-based UI configuration.
tags:
    - hyprland
    - hyprlock
    - wayland
    - screen-lock
    - configuration
    - linux-security
category: guide
optimized: true
optimized_at: 2026-04-26T18:00:00.000Z
---

[hyprlock](https://github.com/hyprwm/hyprlock) is a GPU-accelerated screen locker for Hyprland.

> [!warning]
>If no config file is found, hyprlock **exits with an error** and the session will not be locked.

Use the [example config](https://github.com/hyprwm/hyprlock/blob/main/assets/example.conf) for quick start.

## Command-line Arguments

See also: `hyprlock --help`.

| Argument | Description |
|---|---|
| `-v`, `--verbose` | Enable verbose logging |
| `-q`, `--quiet` | Disable logging |
| `-c` FILE, `--config` FILE | Specify config file |
| `--display` NAME | Specify Wayland display |
| `--grace` SECONDS | Grace period before requiring auth |
| `--immediate-render` | Do not wait for resources before drawing (same as `general:immediate_render`) |
| `--no-fade-in` | Disable fade-in animation |
| `-V`, `--version` | Show version and exit |
| `-h`, `--help` | Show help and exit |

## Configuration

Config file `hyprlock.conf` is searched in this order:

1. `$XDG_CONFIG_HOME/hypr/hyprlock.conf`
2. `$HOME/.config/hypr/hyprlock.conf`
3. `$XDG_CONFIG_DIRS/hypr/hyprlock.conf` (e.g. `<dir>/hypr/hyprlock.conf`)
4. `/etc/xdg/hypr/hyprlock.conf`

Use `--config <path>` to specify an explicit path.

### Variable Types

Hyprlock extends [[067-configuring-variables| Hyprland's variable types]] with:

- **layoutxy** — vec2 with optional `%` suffix for percentage-of-output sizing. Floats supported with `%`; raw pixels are rounded.

### General

| Variable | Type | Default | Description |
|---|---|---|---|
| `hide_cursor` | bool | `false` | Hide cursor instead of making it visible |
| `ignore_empty_input` | bool | `false` | Skip validation when no password provided |
| `immediate_render` | bool | `false` | Start drawing widgets immediately; backgrounds render `background:color` until `background:path` resource is available |
| `text_trim` | bool | `true` | Trim text (useful to avoid trailing newline in command output) |
| `fractional_scaling` | int | `2` | `0`: disabled, `1`: enabled, `2`: auto |
| `screencopy_mode` | int | `0` | `0`: GPU accelerated, `1`: CPU based (slow) |
| `fail_timeout` | int | `2000` | Milliseconds until UI resets after failed auth |

### Authentication

> [!note]
>At least one authentication method must be enabled.

| Variable | Type | Default | Description |
|---|---|---|---|
| `pam:enabled` | bool | `true` | Enable PAM authentication |
| `pam:module` | str | `hyprlock` | PAM module; falls back to "su" if not found in `/etc/pam.d` |
| `fingerprint:enabled` | bool | `false` | Enable parallel fingerprint auth with fprintd |
| `fingerprint:ready_message` | str | `(Scan fingerprint to unlock)` | Message when fprintd is ready |
| `fingerprint:present_message` | str | `Scanning fingerprint` | Message when finger is on scanner |
| `fingerprint:retry_delay` | int | `250` | Delay in ms after unrecognized finger |

### Animations

| Variable | Type | Default | Description |
|---|---|---|---|
| `enabled` | bool | `true` | Enable animations |

`animation` and `bezier` keywords work like in `hyprland.conf`:

```ini
bezier = linear, 1, 1, 0, 0
animation = fade, 1, 1.8, linear
```

Available animations (see [[039-configuring-animations| Animations]] for details):

```txt
global
  ↳ fade
    ↳ fadeIn - fade to lockscreen
    ↳ fadeOut - fade back to Wayland session
  ↳ inputField
    ↳ inputFieldColors - fade between colors/gradients
    ↳ inputFieldFade - fade_on_empty animation
    ↳ inputFieldWidth - adaptive width animation
    ↳ inputFieldDots - fade in/out for individual dots
```

The optional `STYLE` parameter for `animation` is currently unused.

### System Configuration

On Arch Linux, hyprlock integrates with [pambase](https://archlinux.org/packages/?name=pambase) via `pam_faillock.so` — 10 minute timeout after 3 failed unlocks. Change via `/etc/security/faillock.conf` (`unlock_time`, `fail_interval`, `deny`).

## Keyboard Shortcuts

| Input | Action |
|---|---|
| `ESC` | Clear password buffer |
| `Ctrl + u` | Clear password buffer |
| `Ctrl + Backspace` | Clear password buffer |

The [[012-configuring-binds#bind-flags | `l` bind flag]] allows Hyprland keybinds (brightness/volume/media) to work while hyprlock is active.

## Widgets

Configuration is entirely widget-based:

```ini
widget_name {
    monitor =    # further options
}
```

### Monitor Selection

`monitor` is available for all widgets (empty = all monitors). Use port name (e.g. `eDP-1`) or monitor description (e.g. `desc:Chimei Innolux Corporation 0x150C`).

See [[043-configuring-monitors| Monitors]].

### Variable Substitution

- `$USER` — username (e.g. `linux-user`)
- `$DESC` — user description (e.g. `Linux User`)
- `$TIME` — current time 24-hour (e.g. `13:37`)
- `$TIME12` — current time 12-hour (e.g. `1:37 PM`)
- `$LAYOUT` — current keyboard layout
- `$ATTEMPTS` — failed auth attempts
- `$FAIL` — last auth fail reason
- `$PAMPROMPT` — PAM auth last prompt
- `$PAMFAIL` — PAM auth last fail reason
- `$FPRINTPROMPT` — fingerprint auth last prompt
- `$FPRINTFAIL` — fingerprint auth last fail reason

## Widget List

### General Remarks

- All text supports [pango markup](https://docs.gtk.org/Pango/pango_markup.html); `<br/>` for linebreaks (enable with `allow_breaks="true"`)
- Positioning: `halign` (`left`, `center`, `right`, `none`), `valign` (`top`, `center`, `bottom`, `none`), `position` (offset from alignment result), `zindex` (higher = on top; default 0, background -1)
- `position` and `size`: pixels (`10, 10` or `10px, 10px`), percentages (`10%, 10.5%`), or mixed (`10%, 5px`)
- Supported images: png, jpg, webp (no animations)

### Shadowable Widgets

Some widgets support shadow configuration:

| Variable | Type | Default | Description |
|---|---|---|---|
| `shadow_passes` | int | `0` | Shadow passes; 0 disables |
| `shadow_size` | int | `3` | Shadow size |
| `shadow_color` | color | `rgb(0,0,0)` | Shadow color |
| `shadow_boost` | float | `1.2` | Shadow opacity boost |

### Clickable Widgets

`label`, `image`, and `shape` widgets accept `onclick` to run arbitrary commands:

| Variable | Type | Default | Description |
|---|---|---|---|
| `onclick` | str | empty | Command to run when clicked |

### Background

Draws a background image or fills with color. If `path` is empty, uses `color`. If `path` is `screenshot`, captures desktop at launch.

| Variable | Type | Default | Description |
|---|---|---|---|
| `monitor` | str | empty | Monitor to draw on |
| `path` | str | empty | Image path, `screenshot`, or empty to fill with `color` |
| `color` | color | `rgba(17, 17, 17, 1.0)` | Fallback background color |
| `blur_passes` | int | `0` | Blur passes; 0 disables |
| `blur_size` | int | `7` | Blur distance |
| `noise` | float | `0.0117` | Noise amount |
| `contrast` | float | `0.8916` | Blur contrast |
| `brightness` | float | `0.8172` | Blur brightness |
| `vibrancy` | float | `0.1696` | Saturation of blurred colors |
| `vibrancy_darkness` | float | `0.05` | Vibrancy strength on dark areas |
| `reload_time` | int | `-1` | Seconds between reloads; `0` uses `SIGUSR2`; ignored for `screenshot` |
| `reload_cmd` | str | empty | Command to get new path |
| `crossfade_time` | float | `-1.0` | Cross-fade seconds on reload; negative = no cross-fade |
| `zindex` | int | `-1` | z-index |

### Image

Shadowable, Clickable. Empty `path` = nothing shown.

| Variable | Type | Default | Description |
|---|---|---|---|
| `monitor` | str | empty | Monitor |
| `path` | str | empty | Image path |
| `size` | int | `150` | Size scale based on lesser side |
| `rounding` | int | `-1` | Negative = circle |
| `border_size` | int | `4` | Border size |
| `border_color` | gradient | `rgba(221, 221, 221, 1.0)` | Border color |
| `rotate` | int | `0` | Rotation in degrees (counter-clockwise) |
| `reload_time` | int | `-1` | Seconds between reloads; `0` uses `SIGUSR2` |
| `reload_cmd` | str | empty | Command to get new path |
| `position` | layoutxy | `0, 0` | Position |
| `halign` | str | `center` | Horizontal alignment |
| `valign` | str | `center` | Vertical alignment |
| `zindex` | int | `0` | z-index |

### Shape

Shadowable, Clickable.

| Variable | Type | Default | Description |
|---|---|---|---|
| `monitor` | str | empty | Monitor |
| `size` | layoutxy | `100, 100` | Shape size |
| `color` | color | `rgba(17, 17, 17, 1.0)` | Shape color |
| `rounding` | int | `-1` | Negative = circle |
| `rotate` | int | `0` | Rotation in degrees |
| `border_size` | int | `0` | Border size |
| `border_color` | gradient | `rgba(0, 207, 230, 1.0)` | Border color |
| `xray` | bool | `false` | If true, make a "hole" in background (no rotation) |
| `position` | layoutxy | `0, 0` | Position |
| `halign` | str | `center` | Horizontal alignment |
| `valign` | str | `center` | Vertical alignment |
| `zindex` | int | `0` | z-index |

### Input Field

Shadowable. Password input field.

| Variable | Type | Default | Description |
|---|---|---|---|
| `monitor` | str | empty | Monitor |
| `size` | layoutxy | `400, 90` | Field size |
| `outline_thickness` | int | `4` | Outline thickness |
| `dots_size` | float | `0.25` | Dot size \[0.001 - 0.8] |
| `dots_spacing` | float | `0.15` | Dot spacing \[-1.0 - 1.0] |
| `dots_center` | bool | `true` | Center dots; else align left |
| `dots_rounding` | int | `-1` | Dot rounding |
| `dots_text_format` | str | empty | Text character(s) for input indicator |
| `outer_color` | gradient | `rgba(17, 17, 17, 1.0)` | Border color |
| `inner_color` | color | `rgba(200, 200, 200, 1.0)` | Inner box color |
| `font_color` | color | `rgba(10, 10, 10, 1.0)` | Font color |
| `font_family` | str | `Noto Sans` | Font family |
| `fade_on_empty` | bool | `true` | Fade field when empty |
| `fade_timeout` | int | `2000` | ms before `fade_on_empty` triggers |
| `placeholder_text` | str | `<i>Input Password...</i>` | Text when empty |
| `hide_input` | bool | `false` | Render indicator like swaylock instead of dots |
| `hide_input_base_color` | color | `rgba(153, 170, 187)` | Base hue for random rotation (oklab) |
| `rounding` | int | `-1` | `-1` = complete rounding (circle/oval) |
| `check_color` | gradient | `rgba(204, 136, 34, 1.0)` | Color while waiting for auth result |
| `check_text` | str | empty | Text while waiting |
| `fail_color` | gradient | `rgba(204, 34, 34, 1.0)` | Color on auth failure |
| `fail_text` | str | `<i>$FAIL <b>($ATTEMPTS)</b></i>` | Text on auth failure |
| `capslock_color` | gradient | empty | Color when capslock active |
| `numlock_color` | gradient | empty | Color when numlock active |
| `bothlock_color` | gradient | empty | Color when both active |
| `invert_numlock` | bool | `false` | Change color if numlock off |
| `swap_font_color` | bool | `false` | Swap font/inner colors on color change events |
| `position` | layoutxy | `0, 0` | Position |
| `halign` | str | `center` | Horizontal alignment |
| `valign` | str | `center` | Vertical alignment |
| `zindex` | int | `0` | z-index |

**Colors behavior:**
- `outline_thickness` = `0`: inner box color changes instead of outer; if `swap_font_color` is set, font color swaps with inner on color change events
- `outline_thickness` != `0`: font and inner colors swap on password check and auth failure
- `swap_font_color` narrows gradient to first specified color

`placeholder_text` and `fail_text` support variable substitution.

### Label

Shadowable, Clickable.

| Variable | Type | Default | Description |
|---|---|---|---|
| `monitor` | str | empty | Monitor |
| `text` | str | `Sample Text` | Text to render |
| `text_align` | str | `center` | Multi-line alignment (`center`, `right`, or default left) |
| `color` | color | `rgba(254, 254, 254, 1.0)` | Text color |
| `font_size` | int | `16` | Font size |
| `font_family` | str | `Sans` | Font family |
| `rotate` | int | `0` | Rotation in degrees |
| `position` | layoutxy | `0, 0` | Position |
| `halign` | str | `center` | Horizontal alignment |
| `valign` | str | `center` | Vertical alignment |

#### Dynamic Labels

`text` supports variable substitution and shell commands:

```ini
text = cmd[update:1000] echo "<span foreground='##ff2222'>$(date)</span>"
```

> [!note]
- `update:` time is in ms
- Force update: `update:<time>:1` or `update:<time>:true` + `SIGUSR2` to hyprlock; `<time>` can be `0`
- `$ATTEMPTS[<string>]` shows `<string>` when no failed attempts (can be empty to hide)
- `$LAYOUT[<str0>,<str1>,...]` replaces indexed layouts; use `!` to hide default, e.g. `$LAYOUT[!]`
- `$TIME`/`$TIME12` use `TZ` environment variable; fallback to system timezone, then UTC
- Variables parsed *before* command runs
- **Do not** run commands that never exit — hangs `AsyncResourceGatherer`

## User Signals

- `SIGUSR1` — Unlocks hyprlock (e.g. `pkill -USR1 hyprlock` from another TTY)
- `SIGUSR2` — Updates labels and images

#hyprlock #screen-lock #wayland #configuration
