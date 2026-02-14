---
title: Virtual Display | Camoufox
url: https://camoufox.com/python/virtual-display/
source: crawler
fetched_at: 2026-02-14T14:05:29.624623-03:00
rendered_js: true
word_count: 71
summary: This document explains how to use a virtual display buffer to run Camoufox headlessly, helping to prevent bot detection on Linux systems.
tags:
    - camoufox
    - headless-browser
    - xvfb
    - virtual-display
    - bot-detection
    - linux-setup
category: guide
---

While Camoufox includes patches to prevent headless detection, running in headless mode may still be detectable in the future. It's recommended to use a virtual display buffer to run Camoufox headlessly.

If you are running Linux, and would like to run Camoufox headlessly in a virtual display, install `xvfb`:

```

sudo apt-get install xvfb
```

#### [#](#confirm-xvfb-is-installed)Confirm `Xvfb` is installed:

```

$ which Xvfb
/usr/bin/Xvfb
```

* * *

## [#](#usage)Usage

Passing `headless="virtual"` will spawn a new lightweight virtual display in the background for Camoufox to run in.

```

from camoufox.sync_api import Camoufox

with Camoufox(
    headless="virtual"
) as browser:
    page = browser.new_page()
    page.goto("https://example.com")
```