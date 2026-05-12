---
title: Options & Overrides
url: https://wiki.hypr.land/Nix/Options-Overrides/
source: sitemap
fetched_at: 2026-04-26T09:48:00.598550144-03:00
rendered_js: false
word_count: 130
summary: Override Hyprland package build options using Nix .override, .overrideAttrs, or NixOS/Home Manager modules.
tags:
    - nixos
    - home-manager
    - hyprland
    - nix-packaging
    - package-overrides
    - xwayland
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## Package Overrides

Use `.override` or `.overrideAttrs` to customize the Hyprland package build.

### NixOS / Home Manager

```nix
{
  programs.hyprland = { # or wayland.windowManager.hyprland
    enable = true;
    xwayland.enable = true;
  };
}
```

### Package (standalone)

```nix
(pkgs.hyprland.override { # or inputs.hyprland.packages.${pkgs.stdenv.hostPlatform.system}.hyprland
  enableXWayland = true;  # enable XWayland
  withSystemd = true;     # build with systemd support
})
```

> [!info] XWayland is enabled by default in the Nix package. Disable via package `.override` or module options.

## Nix REPL Overrides

For Nix (non-NixOS/non-HM) overrides:

```nix
$ nix repl
nix-repl> :lf github:hyprwm/Hyprland
nix-repl> :bl outputs.packages.x86_64-linux.hyprland.override { /* flag here */ }
```

Use `overrideAttrs` to override `mkDerivation` arguments (e.g. `cmakeBuildType`):

```nix
nix-repl> :bl outputs.packages.x86_64-linux.hyprland.overrideAttrs (self: super: { cmakeBuildType = "Debug" })
```

> [!info] Last updated: April 20, 2026

[[058-nix-cachix|Cachix]] [[021-nix-plugins|Plugins]]

#nixos #home-manager #hyprland
