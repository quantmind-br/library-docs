---
title: Using plugins
url: https://wiki.hypr.land/Plugins/Using-Plugins/
source: sitemap
fetched_at: 2026-04-26T09:47:19.180122653-03:00
rendered_js: false
word_count: 497
summary: This document provides instructions on how to install, manage, and load plugins for the Hyprland window manager using the hyprpm manager or manual methods.
tags:
    - hyprland
    - plugins
    - hyprpm
    - window-manager
    - installation-guide
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Plugins extend Hyprland by loading shared objects (`.so` files). Hyprland has no default plugins — install only what you need.

> [!warning]
> Plugins run as part of Hyprland (C++). Always read source code before installing. A plugin can easily wipe your system. Never trust random `.so` files.

## Getting plugins[](#getting-plugins)

Plugins are distributed as `.so` files. Find repositories yourself — Hyprland has no official plugin registry. Start at [hypr.land/plugins](https://hypr.land/plugins/) or [awesome-hyprland](https://github.com/hyprland-community/awesome-hyprland#plugins).

## Installing / Using plugins[](#installing--using-plugins)

Use the Hyprland Plugin Manager (`hyprpm`). For manual instructions, see [Manual](#manual) below.

### hyprpm[](#hyprpm)

> [!note]
> With [[045-configuring-permissions|permission management]], allow hyprpm to load plugins:
> ```ini
> permission = /usr/(bin|local/bin)/hyprpm, plugin, allow
> ```
> Without this, a popup appears every time hyprpm tries to load a plugin.

Dependencies: `cpio`, `cmake`, `git`, `meson`, `gcc`. Distros that split binaries and headers (Fedora, Debian) may need `-dev` packages of Hyprland's dependencies.

```sh
hyprpm add https://github.com/hyprwm/hyprland-plugins
hyprpm list        # list installed plugins
hyprpm enable name # enable a plugin
hyprpm disable name # disable a plugin
hyprpm reload      # load plugins into Hyprland
```

Add `exec-once = hyprpm reload` to load plugins at startup. Add `-n` for a success notification (warnings/errors always notify).

Update plugins with `hyprpm update`. See all options with `hyprpm -h`.

### Manual[](#manual)

Different plugins have different build methods — follow their instructions. Without Hyprland headers installed:

1. Clone Hyprland, checkout to your version, build, run `sudo make installheaders`.
2. Build your plugin(s).
3. Load with `hyprctl plugin load path`.
4. Unload with `hyprctl plugin unload path`.

## FAQ[](#faq-about-plugins)

**My Hyprland crashes!** — Usually a broken plugin. Run `hyprpm disable` to isolate.

**How do I list loaded plugins?** — `hyprctl plugin list`

**How do I make my own plugin?** — See [[005-plugins-development-getting-started|Getting started]].

**Where do I find plugins?** — [hypr.land/plugins](https://hypr.land/plugins/), [awesome-hyprland](https://github.com/hyprland-community/awesome-hyprland#plugins), or search GitHub for `"hyprland plugin"`.

**Are plugins safe?** — Only if you read and trust the source code.

**Do plugins decrease stability?** — Hyprland unloads crashing plugins when possible. Well-designed plugins should not affect stability.
