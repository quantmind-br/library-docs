---
title: apt Install
url: https://epi052.github.io/feroxbuster-docs/installation/apt
source: github_pages
fetched_at: 2026-02-06T10:56:34.021100744-03:00
rendered_js: true
word_count: 19
summary: This document provides step-by-step instructions for downloading and installing the feroxbuster tool on Debian-based systems using a .deb package.
tags:
    - feroxbuster
    - installation
    - debian
    - package-management
    - linux
    - security-tools
category: guide
---

Download `feroxbuster_amd64.deb` from the [Releases](https://github.com/epi052/feroxbuster/releases) section. After that, use your favorite package manager to install the `.deb`.

Terminal window

```

curl-sLOhttps://github.com/epi052/feroxbuster/releases/latest/download/feroxbuster_amd64.deb.zip
unzipferoxbuster_amd64.deb.zip
sudoaptinstall./feroxbuster_*_amd64.deb
```