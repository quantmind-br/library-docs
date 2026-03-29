---
title: wallpapers | Pyprland web
url: https://hyprland-community.github.io/pyprland/wallpapers
source: github_pages
fetched_at: 2026-01-31T16:03:12.454517906-03:00
rendered_js: false
word_count: 570
summary: Configures automated wallpaper cycling with random image selection and supports various background setting tools across different desktop environments.
tags:
    - wallpaper
    - background
    - automation
    - hyprland
    - configuration
    - randomization
    - image-processing
    - pyprland
category: guide
---

Search folders for images and sets the background image at a regular interval. Pictures are selected randomly from the full list of images found.

It serves few purposes:

- adding support for random images to any background setting tool
- quickly testing different tools with a minimal effort
- adding rounded corners to each wallpaper screen
- generating a wallpaper-compliant color scheme usable to generate configurations for any application (matugen/pywal alike)

It allows "zapping" current backgrounds, clearing it to go distraction free and optionally make them different for each screen.

TIP

Uses **hyprpaper** by default on Hyprland, but can be configured to use any other application. You'll need to run hyprpaper separately for now. (eg: `uwsm app -- hyprpaper`)

IMPORTANT

The `command` option is **required** for all environments except Hyprland. On Hyprland, it defaults to using hyprpaper.

NOTE

On environments other than Hyprland and Niri, pyprland uses `wlr-randr` (Wayland) or `xrandr` (X11) for monitor detection. This provides full wallpaper functionality but without automatic refresh on monitor hotplug.

Cached images (rounded corners, online downloads) are stored in subfolders within your configured `path` directory.

Minimal example using defaults (requires **hyprpaper**)

toml

```
[wallpapers]
path = "~/Pictures/wallpapers/" # path to the folder with background images
```

More complete, using the custom **swww** command (not recommended because of its stability)

toml

```
[wallpapers]
unique = true # set a different wallpaper for each screen
path = "~/Pictures/wallpapers/"
interval = 60 # change every hour
extensions = ["jpg", "jpeg"]
recurse = true
clear_command = "swww clear"
command = "swww img --outputs '[output]'  '[file]'"
```

Note that for applications like `swww`, you'll need to start a daemon separately (eg: from `hyprland.conf`).

## Commands [​](#commands)

Loading commands...

TIP

The `color` and `palette` commands are used for templating. See [Templates](https://hyprland-community.github.io/pyprland/wallpapers_templates.html#commands) for details.

## Configuration [​](#configuration)

Loading configuration...

### `path` [​](#config-path)

**Required.** Path to a folder or list of folders that will be searched for wallpaper images.

toml

```
path = ["~/Pictures/Portraits/", "~/Pictures/Landscapes/"]
```

### `interval` [​](#config-interval)

How long (in minutes) a background should stay in place before changing.

### `command` [​](#config-command)

Overrides the default command to set the background image.

IMPORTANT

**Required** for all environments except Hyprland. On Hyprland, defaults to using hyprpaper if not specified.

[Variables](https://hyprland-community.github.io/pyprland/Variables.html) are replaced with the appropriate values. Use `[file]` for the image path and `[output]` for the monitor name:

NOTE

The `[output]` variable requires monitor detection (available on Hyprland, Niri, and fallback environments with `wlr-randr` or `xrandr`).

sh

```
swaybg -i '[file]' -o '[output]'
```

or

sh

```
swww img --outputs [output] [file]
```

### `clear_command` [​](#config-clear-command)

Overrides the default behavior which kills the `command` program. Use this to provide a command to clear the background:

toml

```
clear_command = "swaybg clear"
```

### `post_command` [​](#config-post-command)

Executes a command after a wallpaper change. Can use `[file]`:

toml

```
post_command = "matugen image '[file]'"
```

### `radius` [​](#config-radius)

When set, adds rounded borders to the wallpapers. Expressed in pixels. Disabled by default.

Requires monitor detection (available on Hyprland, Niri, and fallback environments with `wlr-randr` or `xrandr`). For this feature to work, you must use `[output]` in your `command` to specify the screen port name.

### `extensions` [​](#config-extensions)

List of valid wallpaper image extensions.

### `recurse` [​](#config-recurse)

When enabled, will also search sub-directories recursively.

### `unique` [​](#config-unique)

When enabled, will set a different wallpaper for each screen.

NOTE

Requires monitor detection (available on Hyprland, Niri, and fallback environments with `wlr-randr` or `xrandr`). Usage with [templates](https://hyprland-community.github.io/pyprland/wallpapers_templates.html) is not recommended.

If you are not using the default application, ensure you are using `[output]` in the [command](#config-command) template.

Example for swaybg: `swaybg -o "[output]" -m fill -i "[file]"`

## Online Wallpapers [​](#online-wallpapers)

Pyprland can fetch wallpapers from free online sources like Unsplash, Wallhaven, Reddit, and more. Downloaded images are stored locally and become part of your collection.

See [Online Wallpapers](https://hyprland-community.github.io/pyprland/wallpapers_online.html) for configuration options and available backends.

## Templates [​](#templates)

Generate config files with colors extracted from your wallpaper - similar to matugen/pywal. Automatically theme your terminal, window borders, GTK apps, and more.

See [Templates](https://hyprland-community.github.io/pyprland/wallpapers_templates.html) for full documentation including syntax, color reference, and examples.