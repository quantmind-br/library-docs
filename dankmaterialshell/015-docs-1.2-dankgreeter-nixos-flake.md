---
title: NixOS Installation (Flake) | Dank Linux
url: https://danklinux.com/docs/1.2/dankgreeter/nixos-flake
source: sitemap
fetched_at: 2026-02-22T18:42:28.833771-03:00
rendered_js: false
word_count: 248
summary: This document provides instructions for installing and configuring DankGreeter on NixOS using the Nix flake-based module. It explains how to set up flake inputs, enable the service, and customize compositor and theme settings for the login management system.
tags:
    - nixos
    - nix-flakes
    - dankgreeter
    - login-manager
    - system-configuration
category: guide
---

Version: 1.2

```
██████╗  █████╗ ███╗   ██╗██╗  ██╗ ██████╗ ██████╗ ███████╗███████╗████████╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██╔════╝ ██╔══██╗██╔════╝██╔════╝╚══██╔══╝
██║  ██║███████║██╔██╗ ██║█████╔╝ ██║  ███╗██████╔╝█████╗  █████╗     ██║
██║  ██║██╔══██║██║╚██╗██║██╔═██╗ ██║   ██║██╔══██╗██╔══╝  ██╔══╝     ██║
██████╔╝██║  ██║██║ ╚████║██║  ██╗╚██████╔╝██║  ██║███████╗███████╗   ██║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝
                                                                          
```

DankGreeter can be installed on NixOS using the NixOS module. This guide covers the flake-based installation method.

Native NixOS module Available

DankGreeter is now available in nixpkgs unstable! If you're on NixOS unstable (26.05), see [Installation - NixOS](https://danklinux.com/docs/1.2/dankgreeter/nixos) for the native nixpkgs installation method which doesn't require flakes. It is advised to use the Flake option if you want to get quicker updates or if you want to use the home-manager modules.

## Installation[​](#installation "Direct link to Installation")

### 1. Add Flake Inputs[​](#1-add-flake-inputs "Direct link to 1. Add Flake Inputs")

Add the required flake inputs to your `flake.nix` if you haven't yet:

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

If you want to use the unstable (-git) version from the master branch, you can use:

```
dms.url ="github:AvengeMedia/DankMaterialShell";
```

However, be aware that the documentation may not be updated for the latest changes. You're advised to check the nix source code in the repository directly, and note that it may not work properly.

### 2. Import the NixOS Module[​](#2-import-the-nixos-module "Direct link to 2. Import the NixOS Module")

Add the DankGreeter module to your NixOS configuration imports:

```
imports =[
  inputs.dms.nixosModules.greeter
];
```

note

DankGreeter is only available as a NixOS module (not as a home-manager module), since it needs to run at the system level for login management.

### 3. Enable DankGreeter[​](#3-enable-dankgreeter "Direct link to 3. Enable DankGreeter")

Enable and configure the greeter in your NixOS configuration:

```
programs.dank-material-shell.greeter ={
  enable =true;
  compositor.name ="niri";# Or "hyprland" or "sway"
};
```

info

Unlike DankMaterialShell which can be installed via either the NixOS module or home-manager module, DankGreeter must be configured in your NixOS system configuration (not in home-manager).

warning

Compositors must be installed via NixOS configuration to appear in DankGreeter, not via home-manager.

## Configuration Options[​](#configuration-options "Direct link to Configuration Options")

```
programs.dank-material-shell.greeter ={
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

## Rebuilding[​](#rebuilding "Direct link to Rebuilding")

After making configuration changes, don't forget to rebuild your configuration:

```
sudo nixos-rebuild switch
```