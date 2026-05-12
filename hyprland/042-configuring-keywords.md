---
title: Keywords
url: https://wiki.hypr.land/Configuring/Keywords/
source: sitemap
fetched_at: 2026-04-26T09:47:38.753832573-03:00
rendered_js: false
word_count: 579
summary: Hyprland configuration keywords for execution commands, multi-file sourcing, per-device input settings, and environment variable management.
tags:
    - hyprland
    - configuration
    - shell-execution
    - input-devices
    - environment-variables
    - config-files
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Keywords are commands (not variables) for advanced configuration. See sidebar for keywords controlling binds, animations, monitors, etc.

> [!warning]
> For ALL arguments separated by comma, empty values require a comma: `A, , C` is OK, `A, C` is NOT OK.

## Executing[](#executing)

Execute shell scripts at compositor lifecycle events:

| Keyword | Trigger | Supports rules |
|---------|---------|----------------|
| `exec-once` | launch | yes |
| `execr-once` | launch | no |
| `exec` | each reload | yes |
| `execr` | each reload | no |
| `exec-shutdown` | shutdown | n/a |

See [[061-configuring-dispatchers#executing-with-rules|Executing with rules]] for rule syntax.

## Sourcing (multi-file)[](#sourcing-multi-file)

The `source` keyword includes another file. Globbing is supported:

```ini
source = ~/.config/hypr/myColors.conf
source = ~/.config/hypr/custom/*
```

> [!note]
> Parsing is linear: lines above `source =` are parsed first, then sourced file contents, then lines below.

## Gestures[](#gestures)

Use [libinput-gestures](https://github.com/bulletmark/libinput-gestures) with `hyprctl` to extend Hyprland gestures beyond [[067-configuring-variables| Variables]] options.

## Per-device input configs[](#per-device-input-configs)

Per-device options overwrite those in the `input` section. Only explicitly changed values are overwritten.

Add a per-device category:

```ini
device {
    name = ...
    # options ...
}
```

Obtain `name` from `hyprctl devices` output.

All `input` options (including subcategories like `input:touchpad`) work in device blocks, **except**:
- `force_no_accel`
- `follow_mouse`
- `float_switch_override_focus`

Property name mappings:

```plain
touchdevice:transform -> transform
touchdevice:output -> output
```

Tablets use `output` to bind to specific outputs by `Tablet` name (not `Tablet Pad` or `Tablet tool`).

Additional per-device-only properties:

- `enabled` — enables/disables device (mouse/touchpad/touchdevice/keyboard). Default: enabled.
- `keybinds` — enables/disables keybinds for the device. Default: enabled.

Example:

```ini
device {
    name = royuan-akko-multi-modes-keyboard-b
    repeat_rate = 50
    repeat_delay = 500
    middle_button_emulation = 0
}
```

Modify per-device config via `hyprctl`:

```bash
hyprctl -r -- keyword device[my-device]:sensitivity -1
```

> [!note]
> Per-device layouts do not alter keybind keymap by default. A global keymap of `us` with per-device `fr` keeps binds acting as `us`. Set `resolve_binds_by_sym = 1` to change this — binds then activate by the symbol you type.

## Wallpapers[](#wallpapers)

The "Hyprland background" on first start is **NOT a wallpaper** — it is the default image at the bottom of the render stack.

Set wallpapers with utilities like [hyprpaper](https://github.com/hyprwm/hyprpaper) or [swaybg](https://github.com/swaywm/swaybg). See [[082-useful-utilities| Useful Utilities]] for more options.

## Setting the environment[](#setting-the-environment)

> [!note]
> Environment changes affect only newly spawned processes. Running apps do not pick up changes.

The `env` keyword sets environment variables:

```ini
env = QT_QPA_PLATFORM,wayland
```

Add a `d` flag to export via D-Bus (systemd only):

```ini
env = LIBVA_DRI_DEVICE_PATH,/dev/dri/card1,d
```

> [!warning]
> Hyprland passes raw strings to env vars. Do **not** quote values:

```ini
env = QT_QPA_PLATFORM,wayland  # correct
env = QT_QPA_PLATFORM,"wayland"  # wrong
```