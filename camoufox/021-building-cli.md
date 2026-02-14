---
title: Building in CLI | Camoufox
url: https://camoufox.com/development/buildcli/
source: crawler
fetched_at: 2026-02-14T14:05:26.033899-03:00
rendered_js: true
word_count: 51
summary: This document outlines the command-line options and usage for a cross-platform build script used to target multiple operating systems and hardware architectures.
tags:
    - build-system
    - cross-platform
    - cli-reference
    - compilation
    - multibuild-py
category: reference
---

`Options: -h, --help show this help message and exit --target {linux,windows,macos} [{linux,windows,macos} ...] Target platforms to build --arch {x86_64,arm64,i686} [{x86_64,arm64,i686} ...] Target architectures to build for each platform --bootstrap Bootstrap the build system --clean Clean the build directory before starting Example: $ python3 multibuild.py --target linux windows macos --arch x86_64 arm64`