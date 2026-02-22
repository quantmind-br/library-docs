---
title: Getting Started | Dank Linux
url: https://danklinux.com/docs/1.2/getting-started
source: sitemap
fetched_at: 2026-02-22T18:43:29.133941-03:00
rendered_js: false
word_count: 89
summary: This document provides an introductory guide for installing and configuring the Dank Linux suite, covering repository setup and compositor initialization.
tags:
    - dank-linux
    - installation
    - configuration
    - package-management
    - linux-suite
    - compositor-setup
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

The installer adds the appropriate repository (AUR, COPR, OBS, or PPA) for your distro—updates are managed through your normal package manager afterwards. If you install DMS directly from packages, run `dms setup` to generate starter compositor and terminal configs (niri/Hyprland only). Other compositors like sway, MangoWC, and labwc are supported—see [manual configuration](https://danklinux.com/docs/1.2/dankmaterialshell/installation#post-install).

Manual installation is also supported, and simple. See the installation section for each component: