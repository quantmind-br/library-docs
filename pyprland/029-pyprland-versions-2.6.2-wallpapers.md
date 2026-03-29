---
title: wallpapers | Pyprland web
url: https://hyprland-community.github.io/pyprland/versions/2.6.2/wallpapers
source: github_pages
fetched_at: 2026-01-31T16:01:40.796226475-03:00
rendered_js: false
word_count: 636
summary: Configures automatic wallpaper cycling with random image selection from specified folders, supporting custom commands and background tools like hyprpaper or swww.
tags:
    - wallpaper
    - background
    - automation
    - hyprpaper
    - swww
    - random
    - image
    - configuration
category: guide
---

Search folders for images and sets the background image at a regular interval. Pictures are selected randomly from the full list of images found.

It serves two purposes:

- adding support for random images to any background setting tool
- quickly testing different tools with a minimal effort

It allows "zapping" current backgrounds, clearing it to go distraction free and optionally make them different for each screen.

TIP

Uses **hyprpaper** by default, but can be configured to use any other application. You'll need to run hyprpaper separately for now. (eg: `uwsm app -- hyprpaper`)

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

- `wall next`  Changes the current background image, resume activity if paused

<!--THE END-->

- `wall clear`  Removes the current background image and pause cycling

<!--THE END-->

- `wall pause`  Stops updating the wallpaper automatically

<!--THE END-->

- `wall color "#ff0000"`  Re-generate the [templates](#templates) with the given color

<!--THE END-->

- `wall color "#ff0000" neutral`  Re-generate the templates with the given color and [color scheme](#color-scheme) (color filter)

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

Uses an optimized **hyprpaper** usage if *no command* is provided on version &gt; 2.5.1

[variables](https://hyprland-community.github.io/pyprland/versions/2.6.2/Variables.html) are replaced with the appropriate values, you must use a `"[file]"` placeholder for the image path and `"[output]"` for the screen. eg:

sh

```
swaybg -i '[file]' -o '[output]'
```

or

sh

```
swww img --outputs [output]  [file]
```

### `clear_command` [​](#clear-command)

By default `clear` command kills the `command` program.

Instead of that, you can provide a command to clear the background. eg:

toml

```
clear_command = "swaybg clear"
```

### `post_command` [​](#post-command)

Executes a command after a wallpaper change. Can use `[file]`, eg:

toml

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

When enabled, will set a different wallpaper for each screen (Usage with [templates](#templates) is not recommended).

If you are not using the default application, ensure you are using `"[output]"` in the [command](#command) template.

Example for swaybg: `swaybg -o "[output]" -m fill -i "[file]"`

### `templates` [​](#templates)

Minimal *matugen* or *pywal* feature, mostly compatible with *matugen* syntax.

Open a ticket if misses a feature you are used to.

Example:

toml

```
[wallpapers.templates.hyprland]
input_path = "~/color_configs/hyprlandcolors.sh"
output_path = "/tmp/hyprlandcolors.sh"
post_hook = "sh /tmp/hyprlandcolors.sh"
```

Where the input\_path would contain

sh

```
hyprctl keyword general:col.active_border "rgb({{colors.primary.default.hex_stripped}}) rgb({{colors.tertiary.default.hex_stripped}}) 30deg"
hyprctl keyword decoration:shadow:color "rgb({{colors.primary.default.hex_stripped}})"
```

#### Supported transformations: [​](#supported-transformations)

- set\_lightness
- set\_alpha

#### Supported color formats: [​](#supported-color-formats)

- hex
- hex\_stripped
- rgb
- rgba

#### Supported colors: [​](#supported-colors)

- source
- primary
- on\_primary
- primary\_container
- on\_primary\_container
- secondary
- on\_secondary
- secondary\_container
- on\_secondary\_container
- tertiary
- on\_tertiary
- tertiary\_container
- on\_tertiary\_container
- error
- on\_error
- error\_container
- on\_error\_container
- surface
- surface\_bright
- surface\_dim
- surface\_container\_lowest
- surface\_container\_low
- surface\_container
- surface\_container\_high
- surface\_container\_highest
- on\_surface
- surface\_variant
- on\_surface\_variant
- background
- on\_background
- outline
- outline\_variant
- inverse\_primary
- inverse\_surface
- inverse\_on\_surface
- surface\_tint
- scrim
- shadow
- white
- primary\_fixed
- primary\_fixed\_dim
- on\_primary\_fixed
- on\_primary\_fixed\_variant
- secondary\_fixed
- secondary\_fixed\_dim
- on\_secondary\_fixed
- on\_secondary\_fixed\_variant
- tertiary\_fixed
- tertiary\_fixed\_dim
- on\_tertiary\_fixed
- on\_tertiary\_fixed\_variant
- red
- green
- yellow
- blue
- magenta
- cyan

### `color_scheme` [​](#color-scheme)

Optional modification of the base color used in the [templates](#templates). One of:

- **pastel** a bit more washed colors
- **fluo** or **fluorescent** for high color saturation
- **neutral** for low color saturation
- **earth** a bit more dark, a bit less blue
- **vibrant** for moderate to high saturation
- **mellow** for lower saturation

### `variant` [​](#variant)

Changes the algorithm in use to pick the primary, secondary and tertiary colors.

- "islands" will use the 3 most popular colors of the wallpaper image

otherwise it will only pick the "main" color and shift the hue to get the secondary and tertiary colors.