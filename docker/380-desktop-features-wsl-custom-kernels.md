---
title: Custom kernels on WSL
url: https://docs.docker.com/desktop/features/wsl/custom-kernels/
source: llms
fetched_at: 2026-01-24T14:18:38.912301032-03:00
rendered_js: false
word_count: 182
summary: This document outlines the considerations and recommended practices for using a custom Linux kernel with Docker Desktop on WSL 2, despite it being officially unsupported.
tags:
    - docker-desktop
    - wsl2
    - linux-kernel
    - custom-kernel
    - kernel-configuration
category: guide
---

Docker Desktop depends on several kernel features built into the default WSL 2 Linux kernel distributed by Microsoft. Consequently, using a custom kernel with Docker Desktop on WSL 2 is not officially supported and may cause issues with Docker Desktop startup or operation.

However, in some cases it may be necessary to run custom kernels; Docker Desktop does not block their use, and some users have reported success using them.

If you choose to use a custom kernel, it is recommended you start from the kernel tree distributed by Microsoft from their [official repository](https://github.com/microsoft/WSL2-Linux-Kernel) and then add the features you need on top of that.

It's also recommended that you:

- Use the same kernel version as the one distributed by the latest WSL2 release. You can find the version by running `wsl.exe --system uname -r` in a terminal.
- Start from the default kernel configuration as provided by Microsoft from their [repository](https://github.com/microsoft/WSL2-Linux-Kernel) and add the features you need on top of that.
- Make sure that your kernel build environment includes `pahole` and its version is properly reflected in the corresponding kernel config (`CONFIG_PAHOLE_VERSION`).