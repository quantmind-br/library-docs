---
title: Installation | Camoufox
url: https://camoufox.com/python/installation/
source: sitemap
fetched_at: 2026-03-09T16:47:58.346782-03:00
rendered_js: false
word_count: 44
summary: This document outlines the initial installation process for the `camoufox` package, including an optional geoip dependency, and provides a reference for the available commands within the Camoufox Command Line Interface (CLI).
tags:
    - installation
    - cli-commands
    - package-management
    - geoip-optional
    - camoufox
category: reference
---

First, install the `camoufox` package:

```bash

pip install -U camoufox[geoip]
```

The `geoip` parameter is optional, but heavily recommended if you are using proxies. It will download an extra dataset to determine the user's longitude, latitude, timezone, country, & locale.

### [#](#download-the-browser)Download the browser

To uninstall, run `camoufox remove`.

* * *

### [#](#camoufox-cli)Camoufox CLI

```none

Usage: python -m camoufox [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  fetch    Fetch the latest version of Camoufox
  path     Display the path to the Camoufox executable
  remove   Remove all downloaded files
  server   Launch a Playwright server
  test     Open the Playwright inspector
  version  Display the current version
```