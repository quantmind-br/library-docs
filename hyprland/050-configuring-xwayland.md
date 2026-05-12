---
title: XWayland
url: https://wiki.hypr.land/Configuring/XWayland/
source: sitemap
fetched_at: 2026-04-26T09:49:22.630588751-03:00
rendered_js: false
word_count: 199
summary: This document provides configuration details for managing XWayland behavior in Hyprland, specifically addressing HiDPI scaling issues and Unix domain socket security settings.
tags:
    - xwayland
    - hidpi
    - scaling
    - unix-sockets
    - configuration
    - wayland
    - linux
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# XWayland

XWayland bridges legacy Xorg programs and Wayland compositors.

## HiDPI XWayland

XWayland looks pixelated on HiDPI screens because Xorg cannot scale. Use [`xwayland:force_zero_scaling`](https://wiki.hypr.land/Configuring/Variables/#xwayland) to prevent XWayland windows from being scaled — this removes the pixelated look but does not scale applications properly. Each toolkit has its own scaling mechanism.

```ini
# change monitor to high resolution, the last argument is the scale factor
monitor = , highres, auto, 2
# unscale XWayland
xwayland {
  force_zero_scaling = true
}
# toolkit-specific scale
env = GDK_SCALE,2
env = XCURSOR_SIZE,32
```

`GDK_SCALE` does not conflict with Wayland-native GTK programs.

> [!warning]
> XWayland HiDPI patches are no longer supported. Do not use them.

## Abstract Unix Domain Socket

X11 applications communicate with XWayland via Unix domain sockets. On Linux, libX11 prefers the abstract Unix domain socket, which uses a separate namespace independent of the host filesystem. This makes abstract sockets more flexible but harder to isolate for sandboxes like Flatpak. However, removing the abstract socket has potential security and compatibility issues.

The [`xwayland:create_abstract_socket`](https://wiki.hypr.land/Configuring/Variables/#xwayland) option controls this. When disabled, only the regular Unix domain socket is created.

> [!info]
> Abstract Unix domain sockets are available only on Linux-based systems.

#xwayland #hidpi #unix-sockets