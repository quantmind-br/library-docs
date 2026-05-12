---
title: NixOS Installation | Dank Linux
url: https://danklinux.com/docs/dankmaterialshell/nixos
source: sitemap
fetched_at: 2026-04-26T08:39:11.671740891-03:00
rendered_js: false
word_count: 553
summary: This guide details the installation and configuration of DankMaterialShell on NixOS using native nixpkgs modules and flakes, including plugin management and feature toggles.
tags:
    - nixos
    - dankmaterialshell
    - linux-configuration
    - shell-customization
    - flake-modules
category: configuration
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

```
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║██╔════╝
██║  ██║██╔████╔██║███████╗
██║  ██║██║╚██╔╝██║╚════██║
██████╔╝██║ ╚═╝ ██║███████║
╚═════╝ ╚═╝     ╚═╝╚══════╝
```

DankMaterialShell installs via the NixOS module on NixOS unstable.

> [!info] NixOS Unstable Required
> DankMaterialShell is only in **unstable**. NixOS stable (25.11) must use [[010-docs-dankmaterialshell-nixos-flake|the Flake Installation method]].

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

### 2. Enable DankMaterialShell

```nix
programs.dms-shell.enable = true;
```

Rebuild: `sudo nixos-rebuild switch`

## Configuration Options

### Feature Toggles

```nix
programs.dms-shell ={
  enable = true;
  systemd ={
    enable = true;               # Systemd service for auto-start
    restartIfChanged = true;      # Auto-restart dms.service when dms-shell changes
  };
  # Core features
  enableSystemMonitoring = true;  # System monitoring widgets (dgop)
  enableVPN = true;              # VPN management widget
  enableDynamicTheming = true;    # Wallpaper-based theming (matugen)
  enableAudioWavelength = true; # Audio visualizer (cava)
  enableCalendarEvents = true;    # Calendar integration (khal)
  enableClipboardPaste = true;    # Pasting from clipboard history (wtype)
};
```

### Custom Quickshell Package

```nix
programs.dms-shell ={
  enable = true;
  quickshell.package = pkgs.quickshell; # or your custom package
};
```

#### Using Quickshell from Source

> [!tip] Recommended for Latest Features
> Many DMS features rely on unreleased Quickshell features. Use Quickshell built from source for best experience.

```nix
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

```nix
programs.dms-shell ={
  enable = true;
  quickshell.package = inputs.quickshell.packages.${pkgs.stdenv.hostPlatform.system}.quickshell;
};
```

### Using Flake Package with NixOS Module

Get quicker updates while keeping module configuration:

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
> Replace with `github:AvengeMedia/DankMaterialShell` for master branch. May contain breaking changes.

```nix
programs.dms-shell ={
  enable = true;
  package = inputs.dms.packages.${pkgs.stdenv.hostPlatform.system}.default;
};
```

> [!warning]
> Some dependencies may not auto-enable when using the flake package with the native module.

### Plugins

#### Method 1: Plugin Registry (Recommended)

The [dms-plugin-registry](https://github.com/AvengeMedia/dms-plugin-registry) flake provides all community plugins with daily updates.

```nix
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

```nix
{
  imports =[ inputs.dms-plugin-registry.modules.default ];
  programs.dms-shell ={
    enable = true;
    plugins ={
      dankBatteryAlerts.enable = true;
      dockerManager.enable = true;
    };
  };
}
```

Plugin IDs are the last part of the install URL from the [[https://danklinux.com/plugins|plugin store]] (e.g., `dms://plugin/install/dankBatteryAlerts` → `dankBatteryAlerts`).

#### Method 2: Manual Installation from Source

```nix
programs.dms-shell ={
  enable = true;
  plugins ={
    dockerManager ={
      src = pkgs.fetchFromGitHub {
        owner ="LuckShiba";
        repo ="DmsDockerManager";
        rev ="v1.2.0";
        sha256 ="sha256-VoJCaygWnKpv0s0pqTOmzZnPM922qPDMHk4EPcgVnaU=";
      };
    };
  };
};
```

## Compositor Config Files

The NixOS module installs DMS but doesn't generate compositor-specific configs. Use [[052-docs-dankmaterialshell-cli-setup|`dms setup`]] to deploy defaults:

```bash
dms setup        # Deploy all defaults
dms setup binds  # Or pick individual configs
dms setup colors
dms setup layout
```

## Advanced Configuration

Check [[https://github.com/NixOS/nixpkgs/blob/nixos-unstable/nixos/modules/programs/wayland/dms-shell.nix|the module file]] in nixpkgs for all available options.

## Rebuilding

```bash
sudo nixos-rebuild switch
```

## Troubleshooting

### DMS doesn't start automatically

```nix
programs.dms-shell ={
  enable = true;
  systemd.enable = true;
};
```

### Missing dependencies

Each feature has its own dependency set. Enable the corresponding option (e.g., `enableClipboardPaste = true` installs `wtype`).

## Next Steps

- [[062-docs-dankmaterialshell-application-themes|Configure themes]]
- [[075-docs-dankmaterialshell-keybinds-ipc|Set up keybindings]]
- [[004-docs-dankmaterialshell-plugins-overview|Add plugins]]
