---
title: Theme | Walker
url: https://benz.gitbook.io/walker/customization/theme
source: sitemap
fetched_at: 2026-02-01T13:48:43.733225508-03:00
rendered_js: false
word_count: 124
summary: This document explains how to customize and create themes for the Walker application, detailing the required files and configuration methods.
tags:
    - theme
    - customization
    - gtk4
    - configuration
    - walker
category: guide
---

### [hashtag](#general) General

Walker is built using of \[GTK4]([https://docs.gtk.org/gtk4/arrow-up-right](https://docs.gtk.org/gtk4/)). Refer to the \[GTK4 Documentation]([https://docs.gtk.org/gtk4/arrow-up-right](https://docs.gtk.org/gtk4/)) for specific information.

### [hashtag](#themes) Themes

Themes are built out of the following building-blocks:

- `style.css`
- `layout.xml`
- `keybind.xml`
- `preview.xml`
- `item_<provider>.xml`

You don't have to create every file if you want to create a custom theme, only the ones you want to change. These files should be placed in `~/.config/walker/themes/<THEME>`\\

To set the general theme for Walker, change `theme = "<THEME>"` in your `config.toml`. You can tell Walker to use a different theme, by providing the `-t/--theme` flag.

### [hashtag](#important) Important

Changing the `style.css` does NOT require a restart of Walker, while changing any `*.xml` file does.

### [hashtag](#reference) Reference

Have a look at the default theme: [https://github.com/abenz1267/walker/tree/master/resources/themes/defaultarrow-up-right](https://github.com/abenz1267/walker/tree/master/resources/themes/default)

[PreviousProvider Actionschevron-left](https://benz.gitbook.io/walker/customization/provider-actions)[NextCustom Menuschevron-right](https://benz.gitbook.io/walker/customization/custom-menus)

Last updated 3 months ago