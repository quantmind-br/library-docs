---
title: Plugin guidelines
url: https://wiki.hypr.land/Plugins/Development/Plugin-Guidelines/
source: sitemap
fetched_at: 2026-04-26T09:47:26.781365888-03:00
rendered_js: false
word_count: 430
summary: This document provides guidelines for developing compatible plugins for Hyprland, focusing on manifest configuration, build processes, and best practices for stability.
tags:
    - hyprland
    - plugin-development
    - manifest-configuration
    - hyprpm
    - api-best-practices
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

This page documents recommended guidelines for making a stable and neat plugin.

## Making your plugin compatible with hyprpm

For your plugin to be installable by `hyprpm`, you need a manifest. `hyprpm` parses `hyprload` manifests, but the hyprpm manifest is more powerful.

Create `hyprpm.toml` in the repository root.

### Repository metadata

hyprpm.toml

```toml
[repository]
name = "MyPlugin"
authors = ["Me"]
commit_pins = [
    ["3bb9c7c5cf4f2ee30bf821501499f2308d616f94", "efee74a7404495dbda70205824d6e9fc923ccdae"],
    ["d74607e414dcd16911089a6d4b6aeb661c880923", "efee74a7404495dbda70205824d6e9fc923ccdae"]
]
```

`name` and `authors` are required. `commit_pins` are optional.

### Plugins

For each plugin, add a category:

hyprpm.toml

```toml
[plugin-name]
description = "An epic plugin that will change the world!"
authors = ["Me"]
output = "plugin.so"
build = [
    "make all"
]
```

`description` and `authors` are optional. `output` and `build` are required.

- `build` — commands `hyprpm` runs in the repo root. Every command resets cwd to repo root.
- `output` — path to the output `.so` file from repo root.

### Commit pins

Commit pins manage plugin versioning. They are `hash,hash` pairs: first hash is Hyprland commit, second is your plugin's corresponding commit.

For example, `d74607e414dcd16911089a6d4b6aeb661c880923` corresponds to Hyprland's `0.33.1` release. If someone runs `0.33.1`, `hyprpm` resets your plugin to commit `efee74a7404495dbda70205824d6e9fc923ccdae`.

Recommended: add a pin for each Hyprland release. If no pin matches, latest git is used.

## Formatting

Hyprland plugins are not required to follow Hyprland formatting/naming conventions, but keeping code consistent is advisable. See [`.clang-format`](https://github.com/hyprwm/Hyprland/blob/main/.clang-format) in the Hyprland repo.

## Usage of the API

Use API entries whenever possible — they are guaranteed stable as long as version matches.

Using internal methods by including proper headers is possible, but should not be the default. Hyprland internal methods may be changed, removed, or added without notice. Methods that "seem" fundamental (e.g., `focusWindow`, `mouseMoveUnified`) probably are and unlikely to change.

## Function Hooks

Function hooks intercept calls to a function of your choice. Treat them as a last resort — they are the easiest thing to break between updates. Always prefer Event Hooks.

## Threads

The Wayland event loop is strictly single-threaded. Do not create threads in your code unless fully detached from the Hyprland process (e.g., saving a file).

Last updated on April 20, 2026