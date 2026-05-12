---
title: Hyprland on NixOS
url: https://wiki.hypr.land/Nix/Hyprland-on-NixOS/
source: sitemap
fetched_at: 2026-04-26T09:47:17.182410151-03:00
rendered_js: false
word_count: 196
summary: Configure Hyprland on NixOS using official modules, with optional Home Manager for declarative config.
tags:
    - nixos
    - hyprland
    - configuration
    - wayland
    - home-manager
    - linux-desktop
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

The NixOS module enables critical components: polkit, xdg-desktop-portal-hyprland, graphics drivers, fonts, dconf, XWayland, and Desktop Entry for your display manager.

> [!warning] The **NixOS module** is required — without it, display managers may lack session files.

> [!tip] The **Home Manager module** is optional — configures Hyprland declaratively and adds it to `$PATH`, but does not add session files (handled by the NixOS module).

See [NixOS module options](https://search.nixos.org/options?channel=unstable&size=50&sort=relevance&type=packages&query=hyprland).

## Fixing Theme Problems

For cursor, icon, or window theme issues, see [[017-nix-hyprland-on-home-manager|Hyprland on Home Manager]].

For GTK themes without Home Manager:

```nix
{
  programs.dconf.profiles.user.databases = [
    {
      settings."org/gnome/desktop/interface" = {
        gtk-theme = "Adwaita";
        icon-theme = "Flat-Remix-Red-Dark";
        font-name = "Noto Sans Medium 11";
        document-font-name = "Noto Sans Medium 11";
        monospace-font-name = "Noto Sans Mono Medium 11";
      };
    }
  ];
}
```

## Upstream Module

The [upstream module](https://github.com/hyprwm/Hyprland/blob/main/nix/module.nix) provides options similar to the Home Manager module:

```nix
{inputs, ...}: {
  imports = [inputs.hyprland.nixosModules.default];
  programs.hyprland = {
    plugins = [ # ... ];
    settings = { # ... };
  };
}
```

> [!info] Last updated: April 20, 2026

[[019-nix-hyprland-on-other-distros|Hyprland on Other Distros]]

#nixos #configuration #hyprland
