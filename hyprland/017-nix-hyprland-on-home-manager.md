---
title: Hyprland on Home Manager
url: https://wiki.hypr.land/Nix/Hyprland-on-Home-Manager/
source: sitemap
fetched_at: 2026-04-26T09:47:34.649105028-03:00
rendered_js: false
word_count: 392
summary: Installing and configuring Hyprland via NixOS and Home Manager modules, with plugin support and troubleshooting guidance.
tags:
    - hyprland
    - nix
    - nixos
    - home-manager
    - wayland
    - declarative-configuration
    - window-manager
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

For available options, see the [Home Manager options documentation](https://nix-community.github.io/home-manager/options.xhtml#opt-wayland.windowManager.hyprland.enable).

> [!warning]
> **Required:** NixOS module enables critical components for Hyprland. Without it, display managers may lack session files.
> **Optional:** Home Manager module enables declarative Hyprland configuration without system-level changes (handled by the NixOS module).

## Installation[](#installation)

## Usage[](#usage)

Declarative Hyprland configuration via Home Manager:

```nix
{
  wayland.windowManager.hyprland.settings = {
    "$mod" = "SUPER";
    bind =
      [
        "$mod, F, exec, firefox"
        ", Print, exec, grimblast copy area"
      ]
      ++ (
        # workspaces
        # binds $mod + [shift +] {1..9} to [move to] workspace {1..9}
        builtins.concatLists (builtins.genList (i:
            let ws = i + 1;
            in [
              "$mod, code:1${toString i}, workspace, ${toString ws}"
              "$mod SHIFT, code:1${toString i}, movetoworkspace, ${toString ws}"
            ]
          )
          9)
      );
  };
}
```

## Plugins[](#plugins)

Add plugins via the `plugins` option:

```nix
{
  wayland.windowManager.hyprland.plugins = [
    inputs.hyprland-plugins.packages.${pkgs.stdenv.hostPlatform.system}.hyprbars
    "/absolute/path/to/plugin.so"
  ];
}
```

For building plugins with Nix, see [[021-nix-plugins|Nix/Plugins]].

## FAQ[](#faq)

### Fixing problems with themes[](#fixing-problems-with-themes)

Set cursor, icons, and window themes via `home.pointerCursor` and `gtk.theme` which enable compatibility options:

```nix
{
  home.pointerCursor = {
    gtk.enable = true;
    package = pkgs.bibata-cursors;
    name = "Bibata-Modern-Classic";
    size = 16;
  };
  gtk = {
    enable = true;
    theme = {
      package = pkgs.flat-remix-gtk;
      name = "Flat-Remix-GTK-Grey-Darkest";
    };
    iconTheme = {
      package = pkgs.adwaita-icon-theme;
      name = "Adwaita";
    };
    font = {
      name = "Sans";
      size = 11;
    };
  };
}
```

### Using the Home-Manager module with NixOS[](#using-the-home-manager-module-with-nixos)

For Home Manager `5dc1c2e40410f7dabef3ba8bf4fdb3145eae3ceb` or later, set `package` and `portalPackage` to `null` to use NixOS module packages:

```nix
{
  wayland.windowManager.hyprland = {
    enable = true;
    package = null;
    portalPackage = null;
  };
}
```

> [!warning]
> Do not mix versions of Hyprland and XDPH. Use XDPH from the same source as your NixOS Hyprland.

### Programs don\'t work in systemd services[](#programs-dont-work-in-systemd-services-but-do-on-the-terminal)

Systemd does not import environment by default, so `PATH` is unavailable to services. This commonly affects `hypridle` and `swayidle`.

Fix by adding:

```nix
{
  wayland.windowManager.hyprland.systemd.variables = ["--all"];
}
```

This produces:

```ini
exec-once = dbus-update-activation-environment --systemd --all
```

Without Home Manager, manually add the above command to your Hyprland config.

#### NixOS UWSM[](#nixos-uwsm)

For NixOS module with UWSM (`programs.hyprland.withUWSM = true`), set environment variables:

```nix
{
  xdg.configFile."uwsm/env".source = "${config.home.sessionVariablesPackage}/etc/profile.d/hm-session-vars.sh";
}
```