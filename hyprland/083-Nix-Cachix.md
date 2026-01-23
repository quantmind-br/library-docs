---
title: Cachix
url: https://wiki.hypr.land/Nix/Cachix/
source: sitemap
fetched_at: 2026-01-22T22:15:02.340721756-03:00
rendered_js: false
word_count: 149
summary: This document explains how to use the Hyprland Cachix binary cache to speed up installation and avoid rebuilding the Hyprland flake and its dependencies.
tags:
    - hyprland
    - nix-flakes
    - cachix
    - binary-cache
    - performance-optimization
    - nixos
category: configuration
---

Note

This page only applies to the flake package.  
You can safely skip this if you use the Nixpkgs package.

The Hyprland flake is not built by Hydra, so it is not cached in [cache.nixos.org](https://cache.nixos.org), like the rest of Nixpkgs.

Instead of requiring you to build Hyprland (and its dependencies, which may include `mesa`, `ffmpeg`, etc), we provide a Cachix cache that you can add to your Nix configuration.

The [Hyprland Cachix](https://app.cachix.org/cache/hyprland) exists to cache the `hyprland` packages and any dependencies not found in [cache.nixos.org](https://cache.nixos.org).

Warning

In order for Nix to take advantage of the cache, it has to be enabled **before** using the Hyprland flake package.

Warning

Do **not** override Hyprland’s `nixpkgs` input unless you know what you are doing.  
Doing so will render the cache useless, since you’re building from a different Nixpkgs commit.

Last updated on January 21, 2026

[Hyprland on Home Manager](https://wiki.hypr.land/Nix/Hyprland-on-Home-Manager/ "Hyprland on Home Manager")[Hyprland on Other Distros](https://wiki.hypr.land/Nix/Hyprland-on-other-distros/ "Hyprland on Other Distros")