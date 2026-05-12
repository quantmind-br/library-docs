---
title: NixOS Installation | Dank Linux
url: https://danklinux.com/docs/dankgreeter/nixos
source: sitemap
fetched_at: 2026-04-26T08:38:23.527884148-03:00
rendered_js: false
word_count: 264
summary: This document provides instructions for installing and configuring the DankGreeter display manager module on NixOS systems, including setup via nixpkgs and flake-based configurations.
tags:
    - nixos
    - dankgreeter
    - display-manager
    - linux-configuration
    - nix-flakes
    - system-administration
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

```
██████╗  █████╗ ███╗   ██╗██╗  ██╗ ██████╗ ██████╗ ███████╗███████╗████████╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝ ██╔══██╗██╔════╝██╔════╝╚══██╔══╝
██║  ██║███████║██╔██╗ ██║█████╔╝ ██║  ███╗██████╔╝█████╗  █████╗     ██║
██║  ██║██╔══██║██║╚██╗██║██╔═██╗ ██║   ██║██╔══██╗██╔══╝  ██╔══╝     ██║
██████╔╝██║  ██║██║ ╚████║██║  ██╗╚██████╔╝██║  ██║███████╗███████╗   ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝
```

DankGreeter installs via the native nixpkgs module on NixOS unstable.

> [!info] NixOS Unstable Required
> DankGreeter is only in the **unstable** branch of nixpkgs. NixOS stable (25.11) must use [[036-docs-dankgreeter-nixos-flake|the Flake Installation method]].

## Installation

### 1. Enable NixOS Unstable

**Channels:**
```bash
sudo nix-channel --add https://nixos.org/channels/nixos-unstable nixos
sudo nix-channel --update
```

**Flakes** (`flake.nix`):
```nix
{
  inputs ={
    nixpkgs.url ="github:NixOS/nixpkgs/nixos-unstable";
  };
}
```

### 2. Enable DankGreeter

```nix
services.displayManager.dms-greeter ={
  enable =true;
  compositor.name ="niri"; # or "hyprland" or "sway"
};
```

> [!warning]
> Compositors must be installed via NixOS configuration, not home-manager.

## Configuration Options

```nix
services.displayManager.dms-greeter ={
  compositor ={
    name ="niri";
    customConfig =''
      # Optional custom compositor configuration
    '';
  };
  configHome ="/home/yourusername";  # Sync user's DankMaterialShell theme
  configFiles =[
    "/home/yourusername/.config/DankMaterialShell/settings.json"
  ];
  logs ={
    save =true;
    path ="/tmp/dms-greeter.log";
  };
  quickshell.package = pkgs.quickshell;
};
```

### Using Flake Package with NixOS Module

Add the flake input:
```nix
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

> [!tip] Unstable Version
> Replace `dms.url` with `github:AvengeMedia/DankMaterialShell` for master branch. May contain breaking changes.

Then use the flake package:
```nix
services.displayManager.dms-greeter ={
  enable =true;
  compositor.name ="niri";
  package = inputs.dms.packages.${pkgs.stdenv.hostPlatform.system}.default;
};
```

> [!warning]
> Some dependencies may not auto-enable when using the flake package with the native module.

## Rebuilding

```bash
sudo nixos-rebuild switch
```
