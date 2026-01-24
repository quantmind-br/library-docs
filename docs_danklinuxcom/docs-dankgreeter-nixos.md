---
title: NixOS Installation | Dank Linux
url: https://danklinux.com/docs/dankgreeter/nixos
source: sitemap
fetched_at: 2026-01-24T13:33:09.183043906-03:00
rendered_js: false
word_count: 258
summary: This document provides instructions for installing and configuring the DankGreeter display manager on NixOS using native nixpkgs modules or flakes.
tags:
    - nixos
    - dankgreeter
    - display-manager
    - nix-flakes
    - nixpkgs-unstable
    - system-configuration
category: guide
---

```
██████╗  █████╗ ███╗   ██╗██╗  ██╗ ██████╗ ██████╗ ███████╗███████╗████████╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝ ██╔══██╗██╔════╝██╔════╝╚══██╔══╝
██║  ██║███████║██╔██╗ ██║█████╔╝ ██║  ███╗██████╔╝█████╗  █████╗     ██║
██║  ██║██╔══██║██║╚██╗██║██╔═██╗ ██║   ██║██╔══██╗██╔══╝  ██╔══╝     ██║
██████╔╝██║  ██║██║ ╚████║██║  ██╗╚██████╔╝██║  ██║███████╗███████╗   ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝
                                                                          
```

DankGreeter can be installed on NixOS using the native nixpkgs module. This is the recommended installation method for users on NixOS unstable.

NixOS Unstable Required

DankGreeter is currently only available in the **unstable** branch of nixpkgs. If you're on NixOS stable (currently version 25.11), you'll need to use the [Flake Installation](https://danklinux.com/docs/dankgreeter/nixos-flake) method instead.

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

### 2. Enable DankGreeter[​](#2-enable-dankgreeter "Direct link to 2. Enable DankGreeter")

Enable and configure the greeter in your NixOS configuration:

```
services.displayManager.dms-greeter ={
  enable =true;
  compositor.name ="niri";# Or "hyprland" or "sway"
};
```

warning

Compositors must be installed via NixOS configuration to appear in DankGreeter, not via home-manager.

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

```
services.displayManager.dms-greeter ={
  compositor ={
    name ="niri";# Required. Can be also "hyprland" or "sway"
    customConfig =''
      # Optional custom compositor configuration
    '';
};

# Sync your user's DankMaterialShell theme with the greeter. You'll probably want this
  configHome ="/home/yourusername";

# Custom config files for non-standard config locations
  configFiles =[
"/home/yourusername/.config/DankMaterialShell/settings.json"
];

# Save the logs to a file
  logs ={
    save =true;
    path ="/tmp/dms-greeter.log";
};

# Custom Quickshell Package    
  quickshell.package = pkgs.quickshell;
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
services.displayManager.dms-greeter ={
  enable =true;
  compositor.name ="niri";
  package = inputs.dms.packages.${pkgs.stdenv.hostPlatform.system}.default;
};
```

warning

When using the flake package with the native nixpkgs module, some dependencies may not be automatically enabled by default, and certain configurations might be missing. You may need to manually install optional dependencies or adjust settings to match your needs.

## Rebuilding[​](#rebuilding "Direct link to Rebuilding")

After making configuration changes, don't forget to rebuild your configuration:

```
sudo nixos-rebuild switch
```