---
title: hyprlauncher
url: https://wiki.hypr.land/Hypr-Ecosystem/hyprlauncher/
source: sitemap
fetched_at: 2026-01-22T22:15:07.463429494-03:00
rendered_js: false
word_count: 172
summary: This document introduces hyprlauncher, a daemon-based multipurpose launcher for Hyprland, detailing its installation, execution, and extensive configuration options.
tags:
    - hyprlauncher
    - hyprland
    - app-launcher
    - linux-wm
    - configuration-guide
    - desktop-finder
category: configuration
---

[hyprlauncher](https://github.com/hyprwm/hyprlauncher) is a multipurpose and versatile launcher / picker for hyprland. It’s fast, simple, and provides various modules.

## Usage[](#usage)

Hyprlauncher is *always* a daemon. Launching it spawns a daemon that will listen to requests. If launched with `hyprlauncher -d`, it will not open a window for the first launch.

To open hyprlauncher, just bind `hyprlauncher` to a key.

## Configuration[](#configuration)

### Theming[](#theming)

Theme follows your [hyprtoolkit](https://wiki.hypr.land/Hypr-Ecosystem/hyprtoolkit) theme.

### Config[](#config)

`~/.config/hypr/hyprlauncher.conf`

Config categories and their values:

#### General[](#general)

OptionDescriptionTypeDefault`grab_focus`Whether to force a full keyboard focus grab.bool`true`

#### Cache[](#cache)

OptionDescriptionTypeDefaultenabledControls whether modules keep a cache of often used entries.  
That history is stored on your disk, in plain text, in `~/.local/share/hyprlauncher`.bool`true`

#### Finders[](#finders)

Available finders: `math`, `desktop`, `unicode`.

Prefixes can only be one character.

optiondescriptiontypedefault`default_finder`Controls the default finder used.string`desktop``desktop_prefix`Prefix for the desktop finder to be used.stringempty`unicode_prefix`Prefix for the unicode finder to be used.string`.``math_prefix`Prefix for the math finder to be used.string`=``font_prefix`Prefix for the font finder to be used.string`'``desktop_launch_prefix`Launch prefix for each desktop app, e.g. `uwsm app --`.stringempty`desktop_icons`Whether to enable desktop icons in the results.bool`true`

#### UI[](#ui)

optiondescriptiontypedefaultwindow\_sizethe size of the launchervec2`400 260`