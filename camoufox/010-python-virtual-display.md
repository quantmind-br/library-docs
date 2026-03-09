---
title: Virtual Display | Camoufox
url: https://camoufox.com/python/virtual-display/
source: sitemap
fetched_at: 2026-03-09T16:47:56.541191-03:00
rendered_js: false
word_count: 71
summary: This document explains how to run the Camoufox library headlessly on Linux systems using a virtual display buffer like Xvfb to improve stealthiness.
tags:
    - camoufox
    - headless-mode
    - xvfb
    - virtual-display
    - linux-setup
category: guide
---

While Camoufox includes patches to prevent headless detection, running in headless mode may still be detectable in the future. It's recommended to use a virtual display buffer to run Camoufox headlessly.

If you are running Linux, and would like to run Camoufox headlessly in a virtual display, install `xvfb`:

```bash

sudo apt-get install xvfb
```

#### [#](#confirm-xvfb-is-installed)Confirm `Xvfb` is installed:

```bash

$ which Xvfb
/usr/bin/Xvfb
```

* * *

## [#](#usage)Usage

Passing `headless="virtual"` will spawn a new lightweight virtual display in the background for Camoufox to run in.

```python

from camoufox.sync_api import Camoufox

with Camoufox(
    headless="virtual"
) as browser:
    page = browser.new_page()
    page.goto("https://example.com")
```