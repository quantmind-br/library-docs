---
title: Prerelease Builds - Install
url: https://ghostty.org/docs/install/pre
source: crawler
fetched_at: 2026-02-11T01:43:19.769338-03:00
rendered_js: true
word_count: 415
summary: This document provides instructions for installing and updating to prerelease versions of Ghostty on macOS and Linux. it covers automatic update configuration, Homebrew commands, and Nix flake usage.
tags:
    - ghostty
    - prerelease-builds
    - installation
    - macos
    - linux
    - software-testing
    - homebrew
    - nix-flakes
category: guide
---

Help test the latest features and get the most recent bug fixes by running prerelease builds of Ghostty.

If you're comfortable with running prerelease software, you can help test the latest features and get the most recent bug fixes by running prerelease builds of Ghostty. This helps the project significantly by providing feedback on new features and addressing possible issues before they are released to the public.

> During the private beta period of Ghostty, testers daily drove prerelease builds using this same process. Many didn't have a single issue for months or even over a year. The prerelease builds are generally stable, but users should always be prepared for the possibility of stability issues.

An overview of how to install prerelease builds is provided below with more details in the sections following the table.

PlatformDescriptionmacOS`auto-update-channel` to get the latest prerelease buildsNixStandard `flake.nix` in the Ghostty repositoryLinux[Build from source](https://ghostty.org/docs/install/build)

For macOS, the Ghostty project provides signed and notarized builds for the latest commit on the `main` branch. These are available via [GitHub Releases](https://github.com/ghostty-org/ghostty/releases/tag/tip) but also via the standard macOS auto-update mechanism.

If you are on a release build, you can switch to the prerelease channel by setting [`auto-update-channel`](https://ghostty.org/docs/config/reference#auto-update-channel) to `tip`.

```
auto-update-channel = tip
```

> Don't forget to restart Ghostty after changing the `auto-update-channel` setting! This setting does not take effect until Ghostty is restarted.

> While you can set this setting back to `stable` at any time, this will only take effect when a later stable release is available. If you want to downgrade back to the previous stable release, you must [re-download](https://ghostty.org/download) Ghostty.

> **Why is this setting called "tip"?** The term "tip" is a common term to refer to the latest commit on a branch in Git. Since we build prerelease builds from the latest commit on the `main` branch, we use the term "tip" to refer to the latest prerelease build rather than something like "nightly".

You can also install prerelease builds using Homebrew using the `@tip` version.

```
brew install --cask ghostty@tip
```

> This is community-maintained. The `auto-update-channel` setting is an official distribution channel.

For Nix users on Linux, there is a standard [`flake.nix` in the Ghostty repository](https://github.com/ghostty-org/ghostty/blob/main/flake.nix). Follow the same instructions as the [Nix Flake](https://ghostty.org/docs/install/build#building-with-nix) section on the building from source page.

> **The package in the flake only supports Linux.** Building macOS app bundles is not well supported by Nix, so the package in the flake only supports Linux. If you want to contribute a macOS package to the flake, feel free to make a pull request!

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/install/pre.mdx)

- [macOS](#macos)
- [Homebrew](#homebrew)
- [Nix](#nix)