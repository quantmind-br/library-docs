---
title: Permissions
url: https://wiki.hypr.land/Configuring/Permissions/
source: sitemap
fetched_at: 2026-04-26T09:49:16.592313607-03:00
rendered_js: false
word_count: 481
summary: This document explains how to configure and manage the permission system in Hyprland to control sensitive compositor access for applications.
tags:
    - hyprland
    - permissions
    - security
    - compositor
    - configuration
    - access-control
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Hyprland's permission system (requires `hyprland-guiutils`) works like Android permissions — sensitive compositor actions trigger a notification asking for approval.

> [!note]
> Enable permissions first: set `ecosystem:enforce_permissions = true` (disabled by default).

## Configuring permissions

> [!important]
> Permissions are **not** reloaded on-the-fly — require a Hyprland restart for security reasons.

```ini
permission = regex, permission, mode
```

Examples:

```ini
permission = /usr/bin/grim, screencopy, allow    # always allow grim to capture screen
permission = /usr/bin/appsuite-.*, screencopy, allow  # allow any app starting with /usr/bin/appsuite-
```

### Permission modes

- `allow` — don't ask, always allow
- `ask` — notify every time. Popup options: Deny, Allow until app exits, Allow until Hyprland exits
- `deny` — don't ask, always deny

### Permission list

**`screencopy`** — Default: **ASK**
- Access to screen *without* xdg-desktop-portal-hyprland (e.g. `grim`, `wl-screenrec`, `wf-recorder`)
- Denied: renders black screen with "permission denied" text
- Purpose: block apps/scripts maliciously capturing screen via wayland protocols

**`plugin`** — Default: **ASK**
- Access to load a plugin (regex for app binary or plugin path)
- Do *not* allow `hyprctl` to load plugins by default — attacker could issue `hyprctl plugin load /tmp/my-malicious-plugin.so`; use `deny` or `ask`

**`keyboard`** — Default: **ALLOW**
- Access to connect a new keyboard (regex of device name)
- To disable all non-matching keyboards: set `DENY` for `.*` as the **last** keyboard permission rule
- Purpose: block rubber duckies, malicious virtual/USB keyboards

## Notes

**xdg-desktop-portal** implementations (including xdph) are regular applications subject to permissions. Add a rule like:

```ini
permission = /usr/(lib|libexec|lib64)/xdg-desktop-portal-hyprland, screencopy, allow
```

**NixOS** has no static binary paths — use regex. Example rules for `grim` and `xdg-desktop-portal-hyprland`:

```ini
permission = /nix/store/[a-z0-9]{32}-grim-[0-9.]*/bin/grim, screencopy, allow
permission = /nix/store/[a-z0-9]{32}-xdg-desktop-portal-hyprland-[0-9.]*/libexec/.xdg-desktop-portal-hyprland-wrapped, screencopy, allow
```

String interpolation (escape regex special chars like `+`):

```ini
permission = ${lib.getExe pkgs.grim}, screencopy, allow
permission = ${lib.escapeRegex (lib.getExe config.programs.hyprlock.package)}, screencopy, allow
permission = ${pkgs.xdg-desktop-portal-hyprland}/libexec/.xdg-desktop-portal-hyprland-wrapped, screencopy, allow
```

**BSD** systems with path issues — disable permissions entirely:

```ini
ecosystem {
  enforce_permissions = false
}
```

Otherwise, no config control over permissions (popups still work, but no paths shown, "remember" unavailable).

[[064-configuring-monocle-layout|Monocle Layout]] [[066-configuring-using-hyprctl|Using hyprctl]]

Last updated on April 20, 2026