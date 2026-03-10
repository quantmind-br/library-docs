---
title: Linux
url: https://ghostty.org/docs/linux
source: crawler
fetched_at: 2026-03-10T06:35:15.720492-03:00
rendered_js: true
word_count: 483
summary: This document provides Linux-specific instructions and prerequisites for installing and running the Ghostty terminal emulator, focusing on installation methods and minimum required GTK and Adwaita versions.
tags:
    - linux
    - installation
    - gtk
    - adwaita
    - dependencies
    - wayland
    - x11
category: guide
---

Ghostty works great on Linux, with support for both Wayland and X11 and packages across a variety of distributions and formats.

Ghostty works really hard to "just work" on Linux, with detection and code covering a wide variety of scenarios, but due to the diversity of Linux distributions, desktop environments, launchers, etc. we can't be perfect and some environments require additional notes.

This section covers Linux-specific information, including Linux-only features of Ghostty, documentation on integrating Ghostty with specific Linux distributions and environments, etc.

> This section is dedicated to Linux for Linux users but Ghostty is just as first-class on macOS, as well, with a native application written in Swift and built with Xcode.

Options for installing Ghostty on Linux include pre-built packages on most popular distributions or building from source. Both of these options are well documented at the links below.

- [**Binaries and Packages**  
  \
  Pre-built packages for quick setup on most popular Linux distributions.](https://ghostty.org/docs/install/binary)
- [**Build from Source**  
  \
  Download a source tarball and build Ghostty from source.](https://ghostty.org/docs/install/build)

The table below shows the minimum required GTK and Adwaita versions for specific Ghostty versions.

Ghostty VersionGTK VersionAdwaita Version1.2.x4.141.51.1.x4.81.2

The minimum required GTK and Adwaita versions for Ghostty is the minimum version that is available in the most recent LTS releases of Debian, Fedora, and Ubuntu at the time of a Ghostty minor release. In a Ghostty version number `X.Y.Z`, the `Y` is a minor release.

Patch releases will never bump dependency requirements, so users can always safely and confidently update to the latest patch release within the same minor release. In a Ghostty version number `X.Y.Z`, the `Z` is a patch release.

Ghostty supports many more distributions, but we explicitly specify Debian, Fedora, and Ubuntu since they tend to have the most conservative package repository practices that typically contain the oldest versions of any other popular distributions.

> **Why not continue to support older GTK/Adwaita versions?** Backporting feature support to older GTK/Adwaita versions is impractical from a maintenance perspective. Beyond a certain point, it overcomplicates the widget tree and the version sprawl becomes harder and harder to test against. We don't currently have a robust system for testing GUI interactions on older GTK/Adwaita versions beyond manual testing.

> **So if I have an older version of GTK/Adwaita, I can't use Ghostty?** Not necessarily. You can continue to use the specified Ghostty versions in the table above that match your GTK/Adwaita versions. If your GTK/Adwaita versions are older than the minimum required versions in the table, then unfortunately you will not be able to use Ghostty. Sorry.

Our other dependencies are typically much more API-stable so we tend to support a wider range of versions than GTK and Adwaita. As a matter of policy, we follow the same policy as stated above for all dependencies, but we're more likely to be flexible with other dependencies.

[Edit on GitHub](https://github.com/ghostty-org/website/edit/main/docs/linux/index.mdx)

- [Installing on Linux](#installing-on-linux)
- [Supported GTK/Adwaita Versions](#supported-gtkadwaita-versions)
- [Policy](#policy)
- [Other Dependencies](#other-dependencies)