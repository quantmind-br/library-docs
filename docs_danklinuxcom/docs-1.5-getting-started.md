---
title: Getting Started | Dank Linux
url: https://danklinux.com/docs/1.5/getting-started
source: sitemap
fetched_at: 2026-02-22T18:44:48.131048-03:00
rendered_js: false
word_count: 105
summary: This document provides an overview and initial steps for installing and configuring the Dank Linux suite and Dank Material Shell on various Linux distributions. It covers automated installation via repositories, post-install setup for compositors, and manual configuration options.
tags:
    - dank-linux
    - installation-guide
    - dank-material-shell
    - linux-configuration
    - compositor-setup
    - package-management
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

The installer adds the appropriate repository (AUR, COPR, OBS, or PPA) for your distro—updates are managed through your normal package manager afterwards. If you install DMS directly from packages, run [`dms setup`](https://danklinux.com/docs/1.5/dankmaterialshell/cli-setup) to generate starter compositor and terminal configs (niri/Hyprland only). You can also deploy individual configs like `dms setup binds` or `dms setup colors`. Other compositors like sway, MangoWC, labwc, and Miracle WM are supported—see [manual configuration](https://danklinux.com/docs/1.5/dankmaterialshell/installation#post-install).

Manual installation is also supported, and simple. See the installation section for each component: