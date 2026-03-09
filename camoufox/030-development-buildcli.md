---
title: Building in CLI | Camoufox
url: https://camoufox.com/development/buildcli/
source: sitemap
fetched_at: 2026-03-09T16:48:11.40463-03:00
rendered_js: false
word_count: 51
summary: This document outlines the command-line options available for executing a multi-platform build script, specifying targets and architectures.
tags:
    - command-line
    - build-system
    - target-platforms
    - architectures
    - options
    - script-execution
category: reference
---

`Options: -h, --help show this help message and exit --target {linux,windows,macos} [{linux,windows,macos} ...] Target platforms to build --arch {x86_64,arm64,i686} [{x86_64,arm64,i686} ...] Target architectures to build for each platform --bootstrap Bootstrap the build system --clean Clean the build directory before starting Example: $ python3 multibuild.py --target linux windows macos --arch x86_64 arm64`