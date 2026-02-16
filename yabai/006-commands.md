---
title: Commands
url: https://github.com/asmvik/yabai/wiki/Commands
source: wiki
fetched_at: 2026-02-11T07:34:20.500284-03:00
rendered_js: false
word_count: 1825
summary: This document provides a detailed reference for the yabai message passing interface and specific commands used to manage displays, spaces, and windows on macOS.
tags:
    - yabai
    - macos
    - window-management
    - cli-interface
    - tiling-window-manager
    - automation
category: reference
---

This wiki page aims to explain some of the available commands in detail. 

A short and concise overview of all commands available with your current installation is available using `man yabai` or for the current development version as a [&rightarrow;&nbsp;rendered document][docs-display].

### Message passing interface

Messages can be passed to a running yabai instance using `yabai --message` (or `yabai -m` in short). These messages aim to have a very intuitive format that should be easy to remember. 

The format for commands is `yabai -m <category> <command>`. 

You might remember this format from the previous chapter about [&rightarrow;&nbsp;configuration options][wiki-config], which used the same message passing interface. 

The [&rightarrow;&nbsp;example&nbsp;skhdrc][example-skhdrc] shows how you can integrate these commands with [&rightarrow;&nbsp;skhd][gh-skhd], a hotkey utility for macOS. This file is an example showing how to control yabai using keyboard shortcuts. Note that it is not a good example for all keyboard layouts and is highly opinionated. It is recommended to build your own skhdrc file from scratch to suit your needs.

Most commands will return a non-zero exit code upon failure, which is useful for scripting purposes.

### Display commands

The arrangement indices for displays can be seen in the Displays > Arrangement preference pane in the System Preferences.

#### Focus display

```sh
# Focus display focused before the current one (so you can alternate)
yabai -m display --focus recent

# Focus previous display by arrangement index
yabai -m display --focus prev

# Focus next display by arrangement index
yabai -m display --focus next

# Focus display with arrangement index 2
yabai -m display --focus 2
```

### Space commands

The mission-control indices for spaces can be seen when mission control is active.

#### Focus space

```sh
# Focus space focused before the current one (so you can alternate)
yabai -m space --focus recent

# Focus previous space by mission-control index
yabai -m space --focus prev

# Focus next space by mission-control index
yabai -m space --focus next

# Focus space with mission-control index 2
yabai -m space --focus 2

# Focus next space by mission-control index if one exists, otherwise focus the first space
yabai -m space --focus next || yabai -m space --focus first

# Focus previous space by mission-control index if one exists, otherwise focus the last space
yabai -m space --focus prev || yabai -m space --focus last
```

#### Create and destroy spaces

```sh
# Create space on the active display
yabai -m space --create

# Delete focused space and focus first space on display
yabai -m space --destroy
```

#### Move spaces

```sh
# Move space left
yabai -m space --move prev

# Move space right
yabai -m space --move next

# Send space to display 2 (by display arrangement index)
yabai -m space --display 2
```

#### Label Spaces

Spaces can be given labels, which allow referring to a space by the given label in subsequent commands. 

To label a space use the `--label` command:

```
yabai -m space 1 --label main
yabai -m space 2 --label sm

yabai -m space --focus main
```

#### Modify window tree

In bsp spaces commands can be used to modify the window tree, affecting all windows on the space.

```sh
# Balance out all windows both horizontally and vertically 
#   to occupy the same space
yabai -m space --balance

# Flip the tree horizontally
yabai -m space --mirror x-axis

# Flip the tree vertically
yabai -m space --mirror y-axis

# Rotate the window tree clock-wise (options: 90, 180, 270 degree)
yabai -m space --rotate 90
```

#### Modify space layout

```sh
# Set layout of the space (options: bsp, float)
yabai -m space --layout bsp
```

#### Modify padding and gaps

```sh
# toggle padding on the current space
yabai -m space --toggle padding

# add 10 to the top padding, subtract 5 from the left and right padding
# format: top:bottom:left:right (rel = relative)
yabai -m space --padding rel:10:0:-5:-5

# set all padding to 20 (abs = absolute)
yabai -m space --padding abs:20:20:20:20

# toggle gap between windows on the current space
yabai -m space --toggle gap

# add 10 to gap between windows (rel = relative)
yabai -m space --gap rel:10

# set gap between windows to 0 (abs = absolute)
yabai -m space --gap abs:0
```

### Window commands

Window commands are special in that they can either be operated on the focused window or on any visible window if a) the window id is supplied and b) the command makes sense. 

If you want to operate on an unfocused, visible window, replace `yabai -m window` with `yabai -m window window-id` below. This is mostly for automation. Window identifiers can be obtained through signals and the query system. 

#### Focus window

```sh
# focus window in direction of focused window (options: north, east, south, west)
yabai -m window --focus east

# focus window that was previously focused
yabai -m window --focus recent

# focus previous or next window in window tree (options: prev, next)
yabai -m window --focus prev

# focus first or last window in window tree (options: first, last)
yabai -m window --focus first

# focus window under cursor
yabai -m window --focus mouse
```

#### Move window

Tiled window can be swapped with other windows.

```sh
# swap window position and size with window in direction of focused window
#   (options: north, east, south, west)
yabai -m window --swap north

# swap with previously focused window
yabai -m window --swap recent

# swap with previous or next window in window tree (options: prev, next)
yabai -m window --swap prev

# swap with first or last window in window tree (options: first, last)
yabai -m window --swap first

# swap with window under cursor
yabai -m window --swap mouse
```

The following illustrates how you can use the swap operation to implement window cycling.

cycle_clockwise.sh:
```sh
#!/bin/bash

win=$(yabai -m query --windows --window last | jq '.id')

while : ; do
    yabai -m window $win --swap prev &> /dev/null
    if [ $? -eq 1 ](./-$?--eq-1-.md); then
        break
    fi
done
```

cycle_counterclockwise.sh
```sh
#!/bin/bash

win=$(yabai -m query --windows --window first | jq '.id')

while : ; do
    yabai -m window $win --swap next &> /dev/null
    if [ $? -eq 1 ](./-$?--eq-1-.md); then
        break
    fi
done
```

Tiled windows can also be re-inserted ("warped") at other windows. 

```sh
# warp at window in direction of focused window
#   (options: north, east, south, west)
yabai -m window --warp north

# warp at previously focused window
yabai -m window --warp recent

# warp at previous or next window in window tree (options: prev, next)
yabai -m window --warp prev

# warp at first or last window in window tree (options: first, last)
yabai -m window --warp first

# warp at window under cursor
yabai -m window --warp mouse
```

Floating windows can be moved and resized to absolute coordinates and sizes.

```sh
# move focused window to (100, 200)
yabai -m window --move abs:100:200

# change window size to (500, 800)
yabai -m window --resize abs:500:800
```

Floating windows can also be moved and resized using relative coordinates and sizes.

```sh
# move focused window 100 to the right, 200 up
yabai -m window --move rel:100:-200

# grow window by 100 to the right, shrink by 200 at the bottom
#   (options: top, left, bottom, right, top_left, top_right, bottom_right, bottom_left)
yabai -m window --resize bottom_right:100:-200

# change window size to (500, 800)
yabai -m window --resize abs:500:800
```

Floating windows can also be moved and resized at the same time by placing them on a grid. The grid format is `<rows>:<cols>:<start-x>:<start-y>:<width>:<height>`, where rows and cols are how many rows and columns there are in total, start-x and start-y are the start indices for the row and column and width and height are how many rows and columns the window spans. 

The grid respects the padding enabled for the space.

```
# move focused window to occupy the left two thirds of the screen. 
yabai -m window --grid 1:3:0:0:2:1
```

Move window to another space or display. As with other commands this works using prev, next, last and mission-control index or arrangement index respectively.

```sh
# move window to previous space
yabai -m window --space prev

# move window to display focused before the current one
yabai -m window --display recent

# move window to space 2
yabai -m window --space 2

# move window to space 2 and switch to space 2 (works with both SIP enabled and disabled)
yabai -m window --space 2 --focus
```

Tiled windows may also be zoomed to either occupy the parent nodes space or the full screen, and windows may also be moved into their own space ("native fullscreen").

```sh
# options: zoom-parent, zoom-fullscreen, native-fullscreen
yabai -m window --toggle zoom-parent
```

Whether a window is split vertically or horizontally with its parent node can be toggled as well.

```sh
yabai -m window --toggle split
```

#### Toggle window properties

You can also toggle some other window properties.

```sh
# toggle whether the focused window should be tiled (only on bsp spaces)
yabai -m window --toggle float

# toggle whether the focused window should be shown on all spaces
yabai -m window --toggle sticky
```

### Automation with rules and signals

Rules and signals can be used to automate window management. Rules define how windows that match app name and optionally title with the rule should be managed, and signals are asynchronous external actions that can be triggered on window management events, e.g. when a window is destroyed or the space is changed.

The [&rightarrow;&nbsp;rules docs][docs-rule] and [&rightarrow;&nbsp;signals docs][docs-signal] have detailed information on these. If you need help creating such an automation, feel free to search the issue board and, if no result was found, create an issue asking for help. 

Here are some example rules and signals.

```sh
# float system preferences
yabai -m rule --add app="^System Preferences$" manage=off

# show digital colour meter topmost and on all spaces
yabai -m rule --add app="^Digital Colou?r Meter$" sticky=on

# refresh my Übersicht bar when the space changes
yabai -m signal --add event=space_changed \
    action="osascript -e 'tell application \"Übersicht\" to refresh widget id \"spaces-widget\"'"
```

### Querying information

yabai can also query information about displays, spaces and windows. There are a total of 12 queries available, which can be enhanced easily using [&rightarrow;&nbsp;jq][gh-jq] to filter the JSON formatted output.

||`yabai -m query --displays`|`yabai -m query --spaces`|`yabai -m query --windows`|
|-:|-|-|-|
||Query all displays|Query all spaces|Query all windows|
|`--display [arrangement index]`|Query focused/selected display|Query all spaces on focused/selected display|Query all windows on focused/selected display|
|`--space [mission-control index]`|Query display with focused/selected space|Query focused/selected space|Query all windows on focused/selected space|
|`--window [window id]`|Query display with focused/selected window|Query space with focused/selected window|Query focused/selected window|

For example, to get the window identifiers of all windows on space 2, you could run the following command:

```sh
yabai -m query --windows --space 2 | jq '.[].id'
```

[docs-display]: ./009-yabai-docs.md#display
[wiki-config]: https://github.com/asmvik/yabai/wiki/Configuration
[example-skhdrc]: https://github.com/asmvik/yabai/blob/master/examples/skhdrc
[docs-rule]: ./009-yabai-docs.md#rule
[docs-signal]: ./009-yabai-docs.md#signal
[gh-skhd]: https://github.com/asmvik/skhd
[gh-jq]: https://github.com/stedolan/jq