---
title: Draw a GPU accelerated dock panel on your desktop
title: Panel
word_count: 411
summary: This document explains how to use the kitty terminal emulator's panel kitten to render terminal applications directly onto the desktop as backgrounds, docks, or floating panels.
category: guide
word_count: 411
optimized: true
optimized_at: 2026-05-04T20:44:49Z
---
optimized: true
optimized_at: 2026-05-04T18:00:00Z
# Draw a GPU accelerated dock panel on your desktop

Draw the desktop wallpaper or docks and panels using arbitrary
terminal programs, For example, have `btop
<https://github.com/aristocratos/btop>`__ or `cava
<https://github.com/karlstav/cava/>`__ be your desktop wallpaper.

It is useful for showing status information or notifications on your desktop
using terminal programs instead of GUI toolkits.

The screenshot to the side shows some uses of the panel kitten to draw various
desktop components such as the background, a quick access floating terminal and
a dock panel showing system information (Linux only).

Using this kitten is simple, for example:

```
kitten panel sh -c 'printf "\n\n\nHello, world."; sleep 5s'
```

This will show `Hello, world.` at the top edge of your screen for five
seconds. Here, the terminal program we are running is sh with a script
to print out `Hello, world!`. You can make the terminal program as complex as
you like, as demonstrated in the screenshots.

If you are on Wayland or macOS, you can, for instance, run:

```
kitten panel --edge=background htop
```

to display `htop` as your desktop background. Remember this works in everything
but GNOME and also, in sway, you have to disable the background wallpaper as
sway renders that over the panel kitten surface.

There are projects that make use of this facility to implement generalised
panels and desktop components:

## Controlling panels via remote control

You can control panels via the kitty remote control </remote-control> facility. Create a panel
with remote control enabled:

```
kitten panel -o allow_remote_control=socket-only --lines=2 \
    --listen-on=unix:/tmp/panel kitten run-shell
```

Now you can control this panel using remote control, for example to show/hide
it, use:

```
kitten @ --to=unix:/tmp/panel resize-os-window --action=toggle-visibility
```

To move the panel to the bottom of the screen and increase its height:

```
kitten @ --to=unix:/tmp/panel resize-os-window --action=os-panel \
    --incremental edge=bottom lines=4
```

To create a new panel running the program top, in the same instance
(like creating a new OS window):

```
kitten @ --to=unix:/tmp/panel launch --type=os-panel --os-panel edge=top \
    --os-panel lines=8 top
```

## How the screenshots were generated

The system statistics in the background were created using:

```
kitten panel --edge=background -o background_opacity=0.2 -o background=black btop
```

This creates a kitty background window and inside it runs the `btop
<https://github.com/aristocratos/btop>`__ program to display the statistics.

The floating quick access window was created by running:

```
kitten quick-access-terminal kitten run-shell \
   zsh -c 'printf "\e]66;s=4;Quick access kitty in Hyprland\a\n\n\n\nAlso uses kitty to draw desktop background\n"'
```

This starts the quick access window and inside it runs `kitten run-shell`, which
in turn first runs `zsh` to print out the message and then starts the users login
shell.

The Linux dock panel was:

```
wm bar
```

This is a custom program I wrote for my personal use. It uses kitty's kitten
infrastructure to implement the bar in a `few hundred lines of code
<https://github.com/kovidgoyal/wm/blob/master/bar/main.go>`__.
This was designed for my personal use only, but, there are :ref:`public projects implementing
general purpose panels using kitty <panel_projects>`.

## Compatibility with various platforms
