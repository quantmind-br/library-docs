---
title: NixOS Installation | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/nixos
source: sitemap
fetched_at: 2026-01-24T13:35:57.353017138-03:00
rendered_js: false
word_count: 504
summary: This document provides a comprehensive guide for installing and configuring DankMaterialShell on NixOS, covering both nixpkgs and flake-based methods. It details how to enable core features, manage plugins, and customize system integration using the NixOS module.
tags:
    - nixos
    - dank-material-shell
    - nixpkgs
    - nix-flakes
    - linux-desktop
    - system-configuration
category: tutorial
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

DankMaterialShell can be installed on NixOS using the NixOS module. This guide covers the native nixpkgs installation method.

NixOS Unstable Required

DankMaterialShell is currently only available in the **unstable** branch of nixpkgs. If you're on NixOS stable (currently 25.11), you'll need to use the [Flake Installation](https://danklinux.com/docs/dankmaterialshell/nixos-flake) method instead.

## Installation[​](#installation "Direct link to Installation")

### 1. Enable NixOS Unstable[​](#1-enable-nixos-unstable "Direct link to 1. Enable NixOS Unstable")

Ensure you're using NixOS unstable by setting your channel or flake input:

**Using channels:**

```
sudo nix-channel --add https://nixos.org/channels/nixos-unstable nixos
sudo nix-channel --update
```

**Using flakes (in `flake.nix`):**

```
{
  inputs ={
    nixpkgs.url ="github:NixOS/nixpkgs/nixos-unstable";
};
}
```

### 2. Enable DankMaterialShell[​](#2-enable-dankmaterialshell "Direct link to 2. Enable DankMaterialShell")

In your NixOS configuration, enable DankMaterialShell:

```
programs.dms-shell.enable =true;
```

That's it! Rebuild your system and DankMaterialShell will be installed with sensible defaults.

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

DankMaterialShell provides numerous configuration options to customize your installation. Here are the main options:

### Feature Toggles[​](#feature-toggles "Direct link to Feature Toggles")

```
programs.dms-shell ={
  enable =true;

  systemd ={
    enable =true;# Systemd service for auto-start
    restartIfChanged =true;# Auto-restart dms.service when dms-shell changes
};

# Core features
  enableSystemMonitoring =true;# System monitoring widgets (dgop)
  enableVPN =true;# VPN management widget
  enableDynamicTheming =true;# Wallpaper-based theming (matugen)
  enableAudioWavelength =true;# Audio visualizer (cava)
  enableCalendarEvents =true;# Calendar integration (khal)
  enableClipboardPaste =true;# Pasting from the clipboard history (wtype)
};
```

### Custom Quickshell Package[​](#custom-quickshell-package "Direct link to Custom Quickshell Package")

If you need a specific version of Quickshell:

```
programs.dms-shell ={
  enable =true;
  quickshell.package = pkgs.quickshell;# or your custom package
};
```

#### Using Quickshell from Source[​](#using-quickshell-from-source "Direct link to Using Quickshell from Source")

Recommended for Latest Features

Many features in DankMaterialShell rely on unreleased Quickshell features. For the best experience, you may want to use Quickshell built from source.

To use Quickshell from source, add it as a flake input:

```
{
  inputs ={
    nixpkgs.url ="github:NixOS/nixpkgs/nixos-unstable";

    quickshell ={
      url ="git+https://git.outfoxxed.me/quickshell/quickshell";
      inputs.nixpkgs.follows ="nixpkgs";
};
};
}
```

Then use it in your configuration:

```
programs.dms-shell ={
  enable =true;
  quickshell.package = inputs.quickshell.packages.${pkgs.stdenv.hostPlatform.system}.quickshell;
};
```

### Using Flake Package with NixOS Module[​](#using-flake-package-with-nixos-module "Direct link to Using Flake Package with NixOS Module")

You can use the package from the DankMaterialShell flake while still using the native NixOS module. This allows you to get quicker updates while keeping the module configuration:

First, add the flake input to your `flake.nix`:

```
{
  inputs ={
    nixpkgs.url ="github:NixOS/nixpkgs/nixos-unstable";

    dms ={
      url ="github:AvengeMedia/DankMaterialShell/stable";
      inputs.nixpkgs.follows ="nixpkgs";
};
};
}
```

Using Unstable Version

If you want to use the unstable (-git) version from the master branch for quicker updates, remove `/stable` from the URL:

```
dms.url ="github:AvengeMedia/DankMaterialShell";
```

However, be aware that the unstable version may not work properly and could contain breaking changes. The documentation may not reflect the latest changes in the unstable version.

Then use the flake package with the native module:

```
programs.dms-shell ={
  enable =true;
  package = inputs.dms.packages.${pkgs.stdenv.hostPlatform.system}.default;
};
```

warning

When using the flake package with the native nixpkgs module, some dependencies may not be automatically enabled by default, and certain configurations might be missing. You may need to manually install optional dependencies or adjust feature toggles to match your needs.

### Plugins[​](#plugins "Direct link to Plugins")

Install DankMaterialShell plugins declaratively. There are two methods:

#### Method 1: Using the Plugin Registry (Recommended)[​](#method-1-using-the-plugin-registry-recommended "Direct link to Method 1: Using the Plugin Registry (Recommended)")

The [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) flake provides all community plugins as packages with daily updates. This is the simplest way to install plugins.

First, add the plugin registry as a flake input:

```
{
  inputs ={
    nixpkgs.url ="github:NixOS/nixpkgs/nixos-unstable";

    dms-plugin-registry ={
      url ="github:AvengeMedia/dms-plugin-registry";
      inputs.nixpkgs.follows ="nixpkgs";
};
};
}
```

Then import the module and enable plugins:

```
{
  imports =[ inputs.dms-plugin-registry.modules.default ];

  programs.dms-shell ={
    enable =true;

    plugins ={
# Simply enable plugins by their ID (from the registry)
      dankBatteryAlerts.enable =true;
      dockerManager.enable =true;
};
};
}
```

The plugin IDs can be found in the [plugin store](https://danklinux.com/plugins) - it's the last part of the install URL. For example, `dms://plugin/install/dankBatteryAlerts` has the ID `dankBatteryAlerts`.

#### Method 2: Manual Installation from Source[​](#method-2-manual-installation-from-source "Direct link to Method 2: Manual Installation from Source")

If you don't want to use the registry flake, you can install plugins manually by providing the source:

```
programs.dms-shell ={
  enable =true;

  plugins ={
    dockerManager ={
      src = pkgs.fetchFromGitHub {
        owner ="LuckShiba";
        repo ="DmsDockerManager";
        rev ="v1.2.0";
        sha256 ="sha256-VoJCaygWnKpv0s0pqTOmzZnPM922qPDMHk4EPcgVnaU=";
};
};
    anotherPlugin ={
      enable =true;
      src = pkgs.another-plugin;
};
};
};
```

## Advanced Configuration[​](#advanced-configuration "Direct link to Advanced Configuration")

For a complete list of available options, check [the module file](https://github.com/NixOS/nixpkgs/blob/nixos-unstable/nixos/modules/programs/wayland/dms-shell.nix) in nixpkgs.

## Rebuilding[​](#rebuilding "Direct link to Rebuilding")

After making configuration changes, rebuild your system:

```
sudo nixos-rebuild switch
```

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### DMS doesn't start automatically[​](#dms-doesnt-start-automatically "Direct link to DMS doesn't start automatically")

Make sure you have `systemd.enable = true` set:

```
programs.dms-shell ={
  enable =true;
  systemd.enable =true;
};
```

### Missing dependencies[​](#missing-dependencies "Direct link to Missing dependencies")

Each feature has its own dependency set. If a feature isn't working, ensure the corresponding `enable` option is set to `true`. For example, clipboard history pasting requires `enableClipboardPaste = true` which installs `wtype`.

## Next Steps[​](#next-steps "Direct link to Next Steps")

- Configure your preferences via [Themes](https://danklinux.com/docs/dankmaterialshell/application-themes)
- Set up compositor keybindings in [Keybinds & IPC](https://danklinux.com/docs/dankmaterialshell/keybinds-ipc)
- Extend functionality with [Plugins](https://danklinux.com/docs/dankmaterialshell/plugins-overview)