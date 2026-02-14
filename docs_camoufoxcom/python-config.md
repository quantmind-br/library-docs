---
title: Passing Config | Camoufox
url: https://camoufox.com/python/config/
source: crawler
fetched_at: 2026-02-14T14:05:43.791406-03:00
rendered_js: true
word_count: 48
summary: This document explains how to manually override or pass additional configuration data to Camoufox using the config dictionary parameter.
tags:
    - camoufox
    - browser-configuration
    - python-library
    - webrtc-spoofing
    - fingerprint-injection
category: guide
---

If needed, Camoufox [config data](https://github.com/daijro/camoufox?tab=readme-ov-file#fingerprint-injection) can be overridden/passed as a dictionary to the `config` parameter. This can be used to enable features that have not yet been implemented into the Python library.

* * *

```

from camoufox.sync_api import Camoufox

with Camoufox(
    config={
        'webrtc:ipv4': '123.45.67.89',
        'webrtc:ipv6': 'e791:d37a:88f6:48d1:2cad:2667:4582:1d6d',
    }
) as browser:
    page = browser.new_page()
    page.goto("https://www.browserscan.net/webrtc")
```

Camoufox will warn you if you are manually setting properties that the Python library handles internally.