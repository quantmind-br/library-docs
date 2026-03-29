---
title: wallpapers | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.5.x/wallpapers
source: github_pages
fetched_at: 2026-01-31T16:00:00.463048911-03:00
rendered_js: false
word_count: 383
summary: Configures automatic background image cycling from specified folders with support for multiple display outputs and custom commands.
tags:
    - background-image
    - wallpaper
    - automation
    - hyprland
    - configuration
    - randomization
category: configuration
---

Search folders for images and sets the background image at a regular interval. Pictures are selected randomly from the full list of images found.

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
```

Note that for applications like `swww`, you'll need to start a daemon separately (eg: from `hyprland.conf`).

## Commands [​](#commands)

- `wall next`  Changes the current background image, resume cycling if paused

<!--THE END-->

- `wall clear`  Removes the current background image and pause cycling

<!--THE END-->

- `wall pause`  Stop cycling the wallpaper after a delay

## Configuration [​](#configuration)

### `path` (REQUIRED) [​](#path-required)

path to a folder or list of folders that will be searched. Can also be a list, eg:

toml

```
path = ["~/Pictures/Portraits/", "~/Pictures/Landscapes/"]
```

### `interval` [​](#interval)

defaults to `10`

How long (in minutes) a background should stay in place

### `command` [​](#command)

Overrides the default command to set the background image.

NOTE

Will use an optimized **hyprpaper** usage if no command is provided on &gt; 2.5.1

[variables](https://hyprland-community.github.io/pyprland/versions/2.5.x/Variables.html) are replaced with the appropriate values, you must use a `"[file]"` placeholder for the image path and `"[output]"` for the screen. eg:

```
swaybg -i '[file]' -o '[output]'
```

or

```
swww img --outputs [output]  [file]
```

### `clear_command` [​](#clear-command)

By default `clear` command kills the `command` program.

Instead of that, you can provide a command to clear the background. eg:

```
clear_command = "swaybg clear"
```

### `post_command` [​](#post-command)

Executes a command after a wallpaper change. Can use `[file]`, eg:

```
post_command = "matugen image '[file]'"
```

### `radius` [​](#radius)

When set, adds rounded borders to the wallpapers. Expressed in pixels. Disabled by default.

For this feature to work, you must use '\[output]' in your `command` to specify the screen port name to use in the command.

eg:

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