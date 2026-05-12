---
title: Animations
url: https://wiki.hypr.land/Configuring/Animations/
source: sitemap
fetched_at: 2026-04-26T09:48:28.63571901-03:00
rendered_js: false
word_count: 286
summary: This document explains how to configure animation settings, including bezier curves and the hierarchical animation tree, within the Hyprland window manager.
tags:
    - hyprland
    - configuration
    - animations
    - bezier-curves
    - window-manager
    - ui-customization
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Animations are declared with the `animation` keyword:

```ini
animation = NAME, ONOFF, SPEED, CURVE [,STYLE]
```

- `ONOFF`: `0` = disable, `1` = enable. If `0`, remaining args can be omitted.
- `SPEED`: animation duration in ds (1ds = 100ms).
- `CURVE`: bezier curve name (see [Curves](#curves)).
- `STYLE` (optional): animation style.

Animations form a tree; unset animations inherit parent values.

### Examples

```ini
animation = workspaces, 1, 8, default
animation = windows, 1, 10, myepiccurve, slide
animation = fade, 0
```

### Animation tree

```txt
global
  ↳ windows - styles: slide, popin, gnomed
    ↳ windowsIn - window open - styles: same as windows
    ↳ windowsOut - window close - styles: same as windows
    ↳ windowsMove - moving, dragging, resizing
  ↳ layers - styles: slide, popin, fade
    ↳ layersIn - layer open
    ↳ layersOut - layer close
  ↳ fade
    ↳ fadeIn - fade in for window open
    ↳ fadeOut - fade out for window close
    ↳ fadeSwitch - fade on changing activewindow and its opacity
    ↳ fadeShadow - fade on changing activewindow for shadows
    ↳ fadeDim - easing of dimming inactive windows
    ↳ fadeLayers - fade on layers
      ↳ fadeLayersIn - fade in for layer open
      ↳ fadeLayersOut - fade out for layer close
    ↳ fadePopups - fade on wayland popups
      ↳ fadePopupsIn - fade in for wayland popup open
      ↳ fadePopupsOut - fade out for wayland popup close
    ↳ fadeDpms - fade when dpms is toggled
  ↳ border - border color switch animation
  ↳ borderangle - border gradient angle - styles: once (default), loop
  ↳ workspaces - styles: slide, slidevert, fade, slidefade, slidefadevert
    ↳ workspacesIn - styles: same as workspaces
    ↳ workspacesOut - styles: same as workspaces
    ↳ specialWorkspace - styles: same as workspaces
      ↳ specialWorkspaceIn - styles: same as workspaces
      ↳ specialWorkspaceOut - styles: same as workspaces
  ↳ zoomFactor - screen zoom animation
  ↳ monitorAdded - monitor added zoom animation
```

> [!warning]
> `loop` style for `borderangle` forces Hyprland to render constantly at refresh rate (e.g. 60fps on 60Hz), impacting CPU/GPU/battery even if animations are disabled or borders not visible.

## Curves

Define custom [Bézier curves](https://en.wikipedia.org/wiki/B%C3%A9zier_curve) with the `bezier` keyword:

```ini
bezier = NAME, X0, Y0, X1, Y1
```

Design curves at [cssportal.com](https://www.cssportal.com/css-cubic-bezier-generator/) or browse pre-made curves at [easings.net](https://easings.net).

```ini
bezier = overshoot, 0.05, 0.9, 0.1, 1.1
```

### Extras

**popin** in `windows` — specify minimum percentage to start from:

```ini
animation = windows, 1, 8, default, popin 80%
```

**slide / slidevert / slidefade / slidefadevert** in `workspaces` — specify movement percentage:

```ini
animation = workspaces, 1, 8, default, slidefade 20%
```

**slide** in `windows` and `layers` — choose forced side (`top`, `bottom`, `left`, `right`):

```ini
animation = windows, 1, 8, default, slide left
```

[[049-configuring-workspace-rules|Workspace Rules]] [[041-configuring-gestures|Gestures]]

Last updated on April 20, 2026