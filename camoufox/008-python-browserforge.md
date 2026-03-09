---
title: BrowserForge Integration | Camoufox
url: https://camoufox.com/python/browserforge/
source: sitemap
fetched_at: 2026-03-09T16:48:04.216784-03:00
rendered_js: false
word_count: 103
summary: This document explains how Camoufox interacts with BrowserForge fingerprints, covering both the default random generation based on constraints and how to inject custom Fingerprint objects.
tags:
    - camoufox
    - browserforge
    - fingerprint
    - configuration
    - api-usage
category: guide
---

Camoufox is compatible with [BrowserForge](https://github.com/daijro/browserforge) fingerprints.

By default, Camoufox will generate an use a random BrowserForge fingerprint based on the target `os` & `screen` constraints.

```python

from camoufox.sync_api import Camoufox
from browserforge.fingerprints import Screen

with Camoufox(
    os=('windows', 'macos', 'linux'),
    screen=Screen(max_width=1920, max_height=1080),
) as browser:
    page = browser.new_page()
    page.goto("https://example.com/")
```

If Camoufox is being ran in headful mode, the max screen size will be generated based on your monitor's dimensions unless otherwise specified.

* * *

Injecting custom Fingerprint objects...

You can also inject your own Firefox BrowserForge fingerprint into Camoufox.

```python

from camoufox.sync_api import Camoufox
from browserforge.fingerprints import FingerprintGenerator

fg = FingerprintGenerator(browser='firefox')

# Launch Camoufox with a random Firefox fingerprint
with Camoufox(fingerprint=fg.generate()) as browser:
    page = browser.new_page()
    page.goto("https://example.com/")
```

**Note:** As of now, some properties from BrowserForge fingerprints will not be passed to Camoufox. This is due to the outdated fingerprint dataset from Apify's fingerprint-suite (see [here](https://github.com/apify/fingerprint-suite/discussions/308)). Properties will be re-enabled as soon as an updated dataset is available.