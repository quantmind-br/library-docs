---
title: Getting Started | Dank Linux
url: https://danklinux.com/docs/getting-started
source: sitemap
fetched_at: 2026-02-22T18:46:06.438351-03:00
rendered_js: false
word_count: 105
summary: This document introduces the Dank Linux suite and provides initial instructions for installing, configuring, and deploying components like the Dank Material Shell across various distributions.
tags:
    - dank-linux
    - installation
    - package-management
    - dank-material-shell
    - compositor-configuration
    - system-setup
category: guide
---

```
██████╗  █████╗ ███╗   ██╗██╗  ██╗    ██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗
██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝    ██║     ██║████╗  ██║██║   ██║╚██╗██╔╝
██║  ██║███████║██╔██╗ ██║█████╔╝     ██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝
██║  ██║██╔══██║██║╚██╗██║██╔═██╗     ██║     ██║██║╚██╗██║██║   ██║ ██╔██╗
██████╔╝██║  ██║██║ ╚████║██║  ██╗    ███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝
```

Welcome to Dank Linux! This guide will help you get started with installing and configuring the Dank Linux suite on your system.

tip

The installer adds the appropriate repository (AUR, COPR, OBS, or PPA) for your distro—updates are managed through your normal package manager afterwards. If you install DMS directly from packages, run [`dms setup`](https://danklinux.com/docs/dankmaterialshell/cli-setup) to generate starter compositor and terminal configs (niri/Hyprland only). You can also deploy individual configs like `dms setup binds` or `dms setup colors`. Other compositors like sway, MangoWC, labwc, and Miracle WM are supported—see [manual configuration](https://danklinux.com/docs/dankmaterialshell/installation#post-install).

Manual installation is also supported, and simple. See the installation section for each component: