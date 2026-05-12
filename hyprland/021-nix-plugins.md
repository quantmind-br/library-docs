---
title: Plugins
url: https://wiki.hypr.land/Nix/Plugins/
source: sitemap
fetched_at: 2026-04-26T09:48:08.421160428-03:00
rendered_js: false
word_count: 219
summary: This document explains the standard procedures for managing, installing, and building Hyprland plugins within the Nix ecosystem.
tags:
    - nix
    - hyprland
    - plugin-management
    - nixpkgs
    - flakes
    - linux-desktop
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Hyprland plugins are managed differently on Nix than on other distros. `hyprpm` is unsupported, but Nix has its own building and managing plugins.

## Using plugins from Nixpkgs

Nixpkgs packages Hyprland plugins for the Nixpkgs Hyprland version:

home.nix

```nix
{pkgs, ...}: {
  wayland.windowManager.hyprland.plugins = [
    pkgs.hyprlandPlugins.<plugin>
  ];
}
```

Find available plugins with `nix search nixpkgs#hyprlandPlugins ^`.

## hyprland-plugins

Official plugins made/maintained by vaxry. Recommended for use with the Hyprland flake (not Nixpkgs version).

Add the flake to inputs:

flake.nix

```nix
{
  inputs = {
    hyprland.url = "github:hyprwm/Hyprland";
    hyprland-plugins = {
      url = "github:hyprwm/hyprland-plugins";
      inputs.hyprland.follows = "hyprland";
    };
  };
}
```

`inputs.hyprland.follows` ensures hyprland-plugins uses the exact Hyprland revision you have locked, preventing version mismatches when updating both inputs.

Add plugins to Hyprland:

home.nix

```nix
{inputs, pkgs, ...}: {
  wayland.windowManager.hyprland = {
    enable = true;
    plugins = [
      inputs.hyprland-plugins.packages.${pkgs.stdenv.hostPlatform.system}.<plugin>
    ];
  };
}
```

## Building plugins with Nix

Plugins in Nixpkgs and `hyprland-plugins` are built with `mkHyprlandPlugin`. Any plugin can use it:

plugin.nix

```nix
{
  lib,
  fetchFromGitHub,
  cmake,
  hyprland,
  hyprlandPlugins,
}:
hyprlandPlugins.mkHyprlandPlugin (finalAttrs: {
  pluginName = "hy3";
  version = "0.39.1";
  src = fetchFromGitHub {
    owner = "outfoxxed";
    repo = "hy3";
    rev = "hl${finalAttrs.version}";
    hash = "sha256-PqVld+oFziSt7VZTNBomPyboaMEAIkerPQFwNJL/Wjw=";
  };
  nativeBuildInputs = [cmake];
  buildInputs = [];
  meta = {
    homepage = "https://github.com/outfoxxed/hy3";
    description = "Hyprland plugin for an i3 / sway like manual tiling layout";
    license = lib.licenses.gpl3;
    platforms = lib.platforms.linux;
  };
})
```

home.nix

```nix
{pkgs, ...}: {
  wayland.windowManager.hyprland.plugins = [
    (pkgs.callPackage ./plugin.nix {})
  ];
}
```

`mkHyprlandPlugin` takes an attrset similar to `stdenv.mkDerivation` — it is a wrapper around it.

Last updated on April 20, 2026

[[020-nix-options-overrides|Options & Overrides]] [[091-nix-contributing-and-debugging|Contributing and Debugging]]