---
title: Download a Release
url: https://epi052.github.io/feroxbuster-docs/installation/download-release
source: github_pages
fetched_at: 2026-02-06T10:56:48.794631546-03:00
rendered_js: true
word_count: 51
summary: This document provides installation instructions and command-line scripts for setting up feroxbuster on multiple operating systems including Linux, MacOS, and Windows.
tags:
    - installation
    - feroxbuster
    - cross-platform
    - shell-script
    - powershell
    - command-line-tool
category: guide
---

Most OS/architecture combinations can be installed dynamically using one of the methods shown below.

## Linux (32 and 64-bit) & MacOS

[Section titled “Linux (32 and 64-bit) & MacOS”](#linux-32-and-64-bit--macos)

```

curl-sLhttps://raw.githubusercontent.com/epi052/feroxbuster/master/install-nix.sh|bash
```

```

https://github.com/epi052/feroxbuster/releases/latest/download/x86-windows-feroxbuster.exe.zip
Expand-Archive .\feroxbuster.zip
.\feroxbuster\feroxbuster.exe-V
```

```

Invoke-WebRequest https://github.com/epi052/feroxbuster/releases/latest/download/x86_64-windows-feroxbuster.exe.zip -OutFile feroxbuster.zip
Expand-Archive .\feroxbuster.zip
.\feroxbuster\feroxbuster.exe-V
```

## All other releases

[Section titled “All other releases”](#all-other-releases)

Releases for `armv7`, `aarch64`, and an `x86_64 .deb` can be found in the [Releases](https://github.com/epi052/feroxbuster/releases) section.