---
title: wallpapers | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.4.0/wallpapers
source: github_pages
fetched_at: 2026-01-31T16:00:52.198708332-03:00
rendered_js: false
word_count: 291
summary: Configures automated background image switching with random selection from specified folders, supporting custom commands and multi-monitor setups.
tags:
    - background-image
    - random-wallpaper
    - automation
    - swaybg
    - swww
    - hyprland
    - desktop-customization
    - configuration
category: guide
---

Search folders for images and sets the background image at a regular interval. Images are selected randomly from the full list of images found.

It serves two purposes:

- adding support for random images to any background setting tool
- quickly testing different tools with a minimal effort

It allows "zapping" current backgrounds, clearing it to go distraction free and optionally make them different for each screen.

TIP

Uses **swaybg** by default, but can be configured to use any other application.

Minimal example using defaults(requires **swaybg**)

toml

```
[wallpapers]
path = "~/Images/wallpapers/" # path to the folder with background images
```

More complete, using the custom **swww** command (not recommended because of its stability)

toml

```
[wallpapers]
unique = true # set a different wallpaper for each screen
path = "~/Images/wallpapers/"
interval = 60 # change every hour
extensions = ["jpg", "jpeg"]
recurse = true
## Using swww
command = 'swww img --transition-type any "[file]"'
clear_command = "swww clear"
```

Note that for applications like `swww`, you'll need to start a daemon separately (eg: from `hyprland.conf`).

## Commands [​](#commands)

- `wall next`  Changes the current background image

<!--THE END-->

- `wall clear`  Removes the current background image

## Configuration [​](#configuration)

### `path` (REQUIRED) [​](#path-required)

path to a folder or list of folders that will be searched. Can also be a list, eg:

toml

```
path = ["~/Images/Portraits/", "~/Images/Landscapes/"]
```

### `interval` [​](#interval)

defaults to `10`

How long (in minutes) a background should stay in place

### `command` [​](#command)

Overrides the default command to set the background image.

[variables](https://hyprland-community.github.io/pyprland/versions/2.4.0/Variables.html) are replaced with the appropriate values, you must use a `"[file]"` placeholder for the image path. eg:

```
swaybg -m fill -i "[file]"
```

### `clear_command` [​](#clear-command)

By default `clear` command kills the `command` program.

Instead of that, you can provide a command to clear the background. eg:

```
clear_command = "swaybg clear"
```

### `extensions` [​](#extensions)

defaults to `["png", "jpg", "jpeg"]`

List of valid wallpaper image extensions.

### `recurse` [​](#recurse)

defaults to `false`

When enabled, will also search sub-directories recursively.

### `unique` [​](#unique)

defaults to `false`

When enabled, will set a different wallpaper for each screen.

If you are not using the default application, ensure you are using `"[output]"` in the [command](#command) template.

Example for swaybg: `swaybg -o "[output]" -m fill -i "[file]"`