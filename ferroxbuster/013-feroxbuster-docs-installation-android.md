---
title: Android/Termux Install
url: https://epi052.github.io/feroxbuster-docs/installation/android
source: github_pages
fetched_at: 2026-02-06T10:56:31.25851716-03:00
rendered_js: true
word_count: 71
summary: This document provides step-by-step instructions for compiling and installing feroxbuster from source on Android devices using the Termux environment.
tags:
    - android
    - termux
    - feroxbuster
    - rust
    - compilation
    - arm32
    - build-from-source
category: guide
---

This guide covers building `feroxbuster` from source on Android using Termux, particularly for 32-bit ARM devices (armeabi-v7a) where prebuilt binaries are not available.

> Tested on armeabi-v7a (ARM32) architecture using Rust from the Termux repository

## Install Dependencies

[Section titled “Install Dependencies”](#install-dependencies)

Update Termux packages and install required build dependencies:

```

pkgupdate && pkgupgrade-y
pkginstallgitclangmakecmakepkg-configpythonrust-y
```

Clone the repository and build from source:

```

gitclonehttps://github.com/epi052/feroxbuster.git
cdferoxbuster
cargobuild--release
```

Copy the compiled binary to your PATH:

```

cptarget/release/feroxbuster$PREFIX/bin/
chmod+x$PREFIX/bin/feroxbuster
```

## Verify Installation

[Section titled “Verify Installation”](#verify-installation)

* * *

Contributed by [@pg9051](https://github.com/pg9051)