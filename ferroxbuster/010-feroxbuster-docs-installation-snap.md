---
title: Snap Install
url: https://epi052.github.io/feroxbuster-docs/installation/snap
source: github_pages
fetched_at: 2026-02-06T10:56:55.009298161-03:00
rendered_js: true
word_count: 70
summary: This document explains how to install feroxbuster using the snap package manager and provides workarounds for wordlist access limitations caused by snap confinement.
tags:
    - feroxbuster
    - snap-installation
    - package-management
    - wordlist-management
    - linux-security
category: guide
---

## Install using snap

[Section titled “Install using snap”](#install-using-snap)

```

sudosnapinstallferoxbuster
```

The snap package can only read wordlists from a few specific locations. There are a few possible solutions, of which two are shown below.

If the wordlist is on the same partition as your home directory, it can be hard-linked into `~/snap/feroxbuster/common`:

```

ln/path/to/the/wordlist~/snap/feroxbuster/common
./feroxbuster-uhttp://localhost-w~/snap/feroxbuster/common/wordlist
```

If the wordlist is on a separate partition, hard-linking won’t work. You’ll need to copy it into the snap directory:

```

cp/path/to/the/wordlist~/snap/feroxbuster/common
./feroxbuster-uhttp://localhost-w~/snap/feroxbuster/common/wordlist
```