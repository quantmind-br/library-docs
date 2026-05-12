---
title: NixOS Flake Installation | Dank Linux
url: https://danklinux.com/docs/dankgreeter/nixos-flake
source: sitemap
fetched_at: 2026-04-26T08:38:25.572840742-03:00
rendered_js: false
word_count: 250
summary: This document provides instructions for installing and configuring the DankGreeter login manager on NixOS using a flake-based approach.
tags:
    - nixos
    - dankgreeter
    - flake
    - linux
    - system-configuration
    - login-manager
category: guide
optimized: true
optimized_at: 2026-04-26T12:00:00Z
---

DankGreeter can be installed on NixOS using the NixOS module. This guide covers the flake-based installation method.

> [!info]
> DankGreeter is now available in nixpkgs unstable! If you're on NixOS unstable (26.05), see [[051-docs-dankgreeter-nixos|NixOS Installation]] for the native nixpkgs installation method which doesn't require flakes. Use the Flake option if you want quicker updates or home-manager modules.

## Installation

### 1. Add Flake Inputs

Add the required flake inputs to your `flake.nix`:

```nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    dms = {
      url = "github:AvengeMedia/DankMaterialShell/stable";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
}
```

> [!tip]
> To use the unstable (-git) version from the master branch:
>
> ```nix
> dms.url = "github:AvengeMedia/DankMaterialShell";
> ```
>
> The documentation may not be updated for the latest changes. Check the nix source code in the repository directly — it may not work properly.

### 2. Import the NixOS Module

Add the DankGreeter module to your NixOS configuration imports:

```nix
imports = [
  inputs.dms.nixosModules.greeter
];
```

> [!note]
> DankGreeter is only available as a NixOS module (not as a home-manager module), since it needs to run at the system level for login management.

### 3. Enable DankGreeter

Enable and configure the greeter in your NixOS configuration:

```nix
programs.dank-material-shell.greeter = {
  enable = true;
  compositor.name = "niri"; # Or "hyprland" or "sway"
};
```

> [!info]
> Unlike DankMaterialShell which can be installed via either the NixOS module or home-manager module, DankGreeter must be configured in your NixOS system configuration (not in home-manager).

> [!warning]
> Compositors must be installed via NixOS configuration to appear in DankGreeter, not via home-manager.

## Configuration Options

```nix
programs.dank-material-shell.greeter = {
  compositor = {
    name = "niri"; # Required. Can also be "hyprland" or "sway"
    customConfig = ''
      # Optional custom compositor configuration
    '';
  };
  # Sync your user's DankMaterialShell theme with the greeter. You'll probably want this
  configHome = "/home/yourusername";
  # Custom config files for non-standard config locations
  configFiles = [
    "/home/yourusername/.config/DankMaterialShell/settings.json"
  ];
  # Save the logs to a file
  logs = {
    save = true;
    path = "/tmp/dms-greeter.log";
  };
  # Custom Quickshell Package
  quickshell.package = pkgs.quickshell;
};
```

## Rebuilding

After making configuration changes, rebuild your configuration:

```bash
sudo nixos-rebuild switch
```

#dankgreeter #nixos #flake #installation
