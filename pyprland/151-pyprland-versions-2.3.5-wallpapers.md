---
title: wallpapers | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.3.5/wallpapers
source: github_pages
fetched_at: 2026-01-31T16:04:53.223268255-03:00
rendered_js: false
word_count: 292
summary: Configures automatic wallpaper cycling with random image selection from specified folders, supporting custom commands and multi-monitor setups.
tags:
    - wallpaper
    - background
    - automation
    - hyprland
    - configuration
    - random
    - image
    - monitor
category: guide
---

Search folders for images and sets the background image at a regular interval. Images are selected randomly from the full list of images found.

It serves two purposes:

- adding support for random images to any background setting tool
- quickly testing different tools with a minimal effort

It allows "zapping" current backgrounds, clearing it to go distraction free and optionally make them different for each screen.

> *Added in version 2.2.0, format changed in 2.2.5*

Minimal example (requires **swaybg** by default)

toml

```
[wallpapers]
path = "~/Images/wallpapers/" # path to the folder with background images
unique = true # set a different wallpaper for each screen
```

More complex, using **swww** as a backend (not recommended because of its stability)

toml

```
[wallpapers]
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

- `wall next`: Changes the current background image
- `wall clear`: Removes the current background image

## Configuration [​](#configuration)

### `path` [​](#path)

path to a folder or list of folders that will be searched. Can also be a list, eg:

toml

```
path = ["~/Images/Portraits/", "~/Images/Landscapes/"]
```

### `interval` (optional) [​](#interval-optional)

defaults to `10`

How long (in minutes) a background should stay in place

### `command` (optional) [​](#command-optional)

Overrides the default command to set the background image.

[variables](https://hyprland-community.github.io/pyprland/versions/2.3.5/Variables.html) are replaced with the appropriate values, you must use a `"[file]"` placeholder for the image path. eg:

```
swaybg -m fill -i "[file]"
```

### `clear_command` (optional) [​](#clear-command-optional)

By default `clear` command kills the `command` program.

Instead of that, you can provide a command to clear the background. eg:

```
clear_command = "swaybg clear"
```

### `extensions` (optional) [​](#extensions-optional)

defaults to `["png", "jpg", "jpeg"]`

List of valid wallpaper image extensions.

### `recurse` (optional) [​](#recurse-optional)

defaults to `false`

When enabled, will also search sub-directories recursively.

### `unique` (optional) [​](#unique-optional)

> *Added in 2.2.5*

defaults to `false`

When enabled, will set a different wallpaper for each screen.

If you are not using the default application, ensure you are using `"[output]"` in the [command](#command) template.

Example for swaybg: `swaybg -o "[output]" -m fill -i "[file]"`