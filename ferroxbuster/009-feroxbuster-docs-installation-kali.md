---
title: Kali Install
url: https://epi052.github.io/feroxbuster-docs/installation/kali
source: github_pages
fetched_at: 2026-02-06T10:56:53.660721832-03:00
rendered_js: true
word_count: 47
summary: This document provides instructions for installing feroxbuster on Kali Linux using the official repositories and outlines the additional components included in the package.
tags:
    - feroxbuster
    - kali-linux
    - installation
    - apt
    - package-management
category: guide
---

`feroxbuster` is available in the official Kali Linux repos!

If you’re using Kali, this is the preferred install method. Installing from the repos adds a [ferox-config.toml](https://epi052.github.io/feroxbuster-docs/configuration/ferox-config-toml/) in `/etc/feroxbuster/`, adds command completion for bash, fish, and zsh, includes a man page entry, and installs `feroxbuster` itself.

Terminal window

```

sudoaptupdate && sudoaptinstall-yferoxbuster
```