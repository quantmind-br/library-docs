---
title: Cachix
url: https://wiki.hypr.land/Nix/Cachix/
source: sitemap
fetched_at: 2026-04-26T09:47:46.37943797-03:00
rendered_js: false
word_count: 149
summary: This document explains how to configure a Cachix binary cache for the Hyprland Nix flake to avoid long build times by utilizing pre-compiled binaries.
tags:
    - nix
    - hyprland
    - cachix
    - binary-cache
    - nixos
    - configuration
category: configuration
optimized: true
optimized_at: 2026-04-26T10:00:00Z
---

# Cachix

> [!note]
> This page applies only to the flake package. Skip if using the Nixpkgs package.

The Hyprland flake is not built by Hydra, so it is not cached on [cache.nixos.org](https://cache.nixos.org) like the rest of Nixpkgs. Instead of requiring you to build Hyprland and its dependencies (which may include `mesa`, `ffmpeg`, etc.), a Cachix cache is provided.

The [Hyprland Cachix](https://app.cachix.org/cache/hyprland) caches the `hyprland` package and any dependencies not found in [cache.nixos.org](https://cache.nixos.org).

> [!warning]
> Nix must use the cache **before** the Hyprland flake package is used. Enable it first, then use Hyprland.

## configuration.nix

```nix
{
  nix.settings = {
    substituters = ["https://hyprland.cachix.org"];
    trusted-substituters = ["https://hyprland.cachix.org"];
    trusted-public-keys = ["hyprland.cachix.org-1:a7pgxzMz7+chwVL3/pzj6jIBMioiJM7ypFP8PwtkuGc="];
  };
}
```

> [!warning]
> Do **not** override Hyprland's `nixpkgs` input unless you know what you are doing. Doing so renders the cache useless since you are building from a different Nixpkgs commit.

See also: [[017-nix-hyprland-on-home-manager|Hyprland on Home Manager]], [[020-nix-options-overrides|Options & Overrides]]

#cachix #binary-cache #nixos