---
title: Build System | Camoufox
url: https://camoufox.com/development/overview/
source: crawler
fetched_at: 2026-02-14T14:05:32.421262-03:00
rendered_js: true
word_count: 22
summary: This document provides an overview of the Camoufox build system architecture and the specific make commands used to compile and package the browser for multiple platforms.
tags:
    - camoufox
    - build-system
    - makefile
    - software-packaging
    - firefox-based
category: guide
---

Here is a diagram of the build system, and its associated make commands:

* * *

```
Localmake buildmake package-linuxmake package-windowsmake package-macosmake fetchmake dirCamoufox RepositoryFingerprint masking patchesuBlock & B.P.C.Debloat/optimizationsWin, Mac, Linux fontsPatched JugglerFirefox SourcePatched SourceBuiltLinux PortableWindows PortablemacOS Portable
```

This was originally based on the LibreWolf build system.