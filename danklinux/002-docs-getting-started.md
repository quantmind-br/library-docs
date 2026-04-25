---
title: Getting Started | Dank Linux
url: https://danklinux.com/docs/getting-started
source: sitemap
fetched_at: 2026-04-07T21:33:37.705762487-03:00
rendered_js: false
word_count: 105
summary: This guide provides instructions on how to install and configure the Dank Linux suite across various distributions. It details methods for setting up repositories and offers commands for generating starter configurations or deploying individual settings.
tags:
    - dank-linux
    - installation-guide
    - system-setup
    - compositor-config
    - repository-management
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