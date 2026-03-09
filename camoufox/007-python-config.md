---
title: Passing Config | Camoufox
url: https://camoufox.com/python/config/
source: sitemap
fetched_at: 2026-03-09T16:48:01.789105-03:00
rendered_js: false
word_count: 48
summary: This document explains how to override or pass custom configuration data, such as WebRTC settings, to the Camoufox client via the 'config' parameter.
tags:
    - camoufox
    - configuration
    - custom-settings
    - webrtc
    - python-library
category: reference
---

If needed, Camoufox [config data](https://github.com/daijro/camoufox?tab=readme-ov-file#fingerprint-injection) can be overridden/passed as a dictionary to the `config` parameter. This can be used to enable features that have not yet been implemented into the Python library.

* * *

```python

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