---
title: Hyprland on Other Distros
url: https://wiki.hypr.land/Nix/Hyprland-on-other-distros/
source: sitemap
fetched_at: 2026-04-26T09:47:20.03087349-03:00
rendered_js: false
word_count: 205
summary: Install and run Hyprland via Nix on non-NixOS distros using nixGL for hardware compatibility.
tags:
    - hyprland
    - nix
    - linux
    - window-manager
    - nixgl
    - package-management
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Installation

Install `nix` via your package manager (`apt`, `pacman`, `dnf`, etc.), then enable the daemon:

```sh
sudo systemctl enable --now nix-daemon
```

> [!tip] Advanced users may want [[017-nix-hyprland-on-home-manager|Home Manager]].

Enable flakes in `/etc/nix/nix.conf` or `~/.config/nix/nix.conf`:

```ini
experimental-features = nix-command flakes
```

Install Hyprland:

```sh
nix profile install github:hyprwm/hyprland
```

## Graphics Drivers (nixGL)

Outside NixOS, Hyprland cannot auto-detect graphics drivers. Use [nixGL](https://github.com/guibou/nixGL):

```sh
sudo nix profile add --profile /nix/var/nix/profiles/default github:guibou/nixGL --impure
```

> [!info] `--impure` is required because nixGL relies on hardware information. Since 0.53.2, `start-hyprland` auto-uses nixGL if needed. Earlier versions require `nixGL start-hyprland`.

## Login Manager Session File

For SDDM, GDM, etc., symlink the desktop file:

```sh
sudo mkdir -p /usr/share/wayland-sessions
sudo ln -sf /nix/var/nix/profiles/default/share/wayland-sessions/hyprland.desktop /usr/share/wayland-sessions/hyprland.desktop
```

## Upgrading

```sh
sudo nix profile upgrade --profile /nix/var/nix/profiles/default '.*'
```

See [nix profile upgrade docs](https://nixos.org/manual/nix/stable/command-ref/new-cli/nix3-profile.html) for other options.

> [!info] Last updated: April 20, 2026

[[018-nix-hyprland-on-nixos|Hyprland on NixOS]] [[017-nix-hyprland-on-home-manager|Hyprland on Home Manager]]

#nix #installation #hyprland
