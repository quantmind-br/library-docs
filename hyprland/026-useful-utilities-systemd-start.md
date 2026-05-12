---
title: Systemd startup
url: https://wiki.hypr.land/Useful-Utilities/Systemd-start/
source: sitemap
fetched_at: 2026-04-26T09:49:02.79851865-03:00
rendered_js: false
word_count: 319
summary: This document provides instructions on using the Universal Wayland Session Manager (UWSM) to wrap Wayland compositors like Hyprland into systemd units for improved session management.
tags:
    - wayland
    - session-management
    - systemd
    - hyprland
    - linux-desktop
    - xdg-autostart
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

UWSM (Universal Wayland Session Manager) wraps standalone Wayland compositors into systemd units, providing robust session management including environment, XDG autostart support, bi-directional binding with login session, and clean shutdown.

> [!warning]
> UWSM is for advanced users and has its own issues and additional quirks.

## Installation

**Arch**

**Nix/NixOS**

## Launching Hyprland with uwsm

### In tty

**GNOME Keyring PAM setup**

Add to shell profile:

```
if uwsm check may-start && uwsm select; then
	exec uwsm start default
fi
```

This brings the uwsm compositor selection menu after tty1 login. Choose `Hyprland` entry.

To bypass selection menu and launch Hyprland directly:

```
if uwsm check may-start; then
    exec uwsm start hyprland.desktop
fi
```

### Using a display manager

Choose `Hyprland (uwsm-managed)` entry in the display manager selection menu.

## Launching applications inside session

Systemd-managed sessions run applications as units. Prefix startup commands with `uwsm app --`. Supports launching Desktop Entries by IDs or paths. See `man uwsm` or `uwsm app --help`.

```ini
exec-once = uwsm app -- mycommand --arg1 --arg2
bind = SUPER, E, exec, uwsm app -- pcmanfm-qt.desktop
```

Faster alternatives:
- `uwsm-app` — shell client with on-demand daemon (optional part of uwsm)
- `app2unit` — [pure shell alternative](https://github.com/Vladimir-csp/app2unit), file opener, usually feature-ahead
- `runapp` — [C++ alternative](https://github.com/c4rlo/runapp/), even faster, features may vary

## Autostart

XDG Autostart is handled by systemd; its target is activated in uwsm-managed session automatically.

Applications with native systemd user units may need explicit enabling via `systemctl --user enable [some-app.service]`. If the unit lacks `[Install]` section, enable more directly: `systemctl --user add-wants graphical-session.target [some-app.service]`. Ensure the unit has `After=graphical-session.target` ordering (can be added via drop-in).

More examples and tricks: [uwsm example-units](https://github.com/Vladimir-csp/uwsm/tree/master/example-units).

Last updated on April 20, 2026

[[038-useful-utilities-hypr-ecosystem|Hypr Ecosystem]]