---
title: Installation | Camoufox
url: https://camoufox.com/python/installation/
source: crawler
fetched_at: 2026-02-14T14:05:45.35948-03:00
rendered_js: true
word_count: 44
summary: This document provides instructions for installing the Camoufox library and lists the available commands for its command-line interface.
tags:
    - camoufox
    - python
    - installation
    - browser-automation
    - cli-reference
    - geoip
category: reference
---

First, install the `camoufox` package:

```

pip install -U camoufox[geoip]
```

The `geoip` parameter is optional, but heavily recommended if you are using proxies. It will download an extra dataset to determine the user's longitude, latitude, timezone, country, & locale.

### [#](#download-the-browser)Download the browser

To uninstall, run `camoufox remove`.

* * *

### [#](#camoufox-cli)Camoufox CLI

```

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