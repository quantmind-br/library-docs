---
title: Compositor Blur | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/compositor-blur
source: sitemap
fetched_at: 2026-04-26T08:38:55.465122767-03:00
rendered_js: false
word_count: 177
summary: This document explains how to configure and enable background blur effects for DMS surfaces, including requirements for compositor protocol support and visual adjustments for transparency and edge smoothing.
tags:
    - background-blur
    - dms-configuration
    - ui-customization
    - wayland-compositor
    - visual-styling
    - personalization
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

# Compositor Blur

On compositors that support the `ext-bg-effect-v1` protocol (such as [niri](https://github.com/YaLTeR/niri)), DMS can ask the compositor to blur whatever sits behind its surfaces — bars, popouts, modals, and notifications.

## Enabling

Toggle **Background Blur** under **Settings > Personalization > Theme & Colors**.

![Background Blur settings panel](https://danklinux.com/img/blur_light.png)
![Background Blur settings panel](https://danklinux.com/img/blur_dark.png)

This requires compositor support. If your compositor doesn't implement `ext-bg-effect-v1`, the toggle has no effect.

> [!info] Hyprland and other compositors
> On compositors without `ext-bg-effect-v1` support — such as Hyprland — you may still blur DMS surfaces via compositor-side layer rules. See [[064-docs-dankmaterialshell-layers|Layer Namespaces]] for per-namespace blur examples.

## Making It Visible

Blur only shows through transparent pixels. Lower the opacity on surfaces under **Theme & Colors > Widget Styling**. Fully opaque surfaces will look the same as before.

## Blur Border

Surfaces with rounded corners can look rough along the edge where the blur meets the radius. The **Blur Border Color** and **Blur Border Opacity** options paint a subtle outline that smooths those edges — recommended when using corner rounding.

#background-blur #visual-styling #dms-configuration
