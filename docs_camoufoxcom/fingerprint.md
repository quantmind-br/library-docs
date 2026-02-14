---
title: Fingerprint Injection | Camoufox
url: https://camoufox.com/fingerprint/
source: crawler
fetched_at: 2026-02-14T14:05:49.126778-03:00
rendered_js: true
word_count: 77
summary: This document explains how Camoufox handles browser fingerprint spoofing at the C++ level and provides instructions on configuring spoofed properties via its Python interface.
tags:
    - camoufox
    - browser-fingerprinting
    - anti-detection
    - python-api
    - fingerprint-spoofing
    - stealth-browsing
category: guide
---

In Camoufox, data is intercepted at the C++ implementation level, making the changes undetectable through JavaScript inspection.

To spoof fingerprint properties, pass a JSON containing properties to spoof to the [Python interface](https://github.com/daijro/camoufox/tree/main/pythonlib#camoufox-python-interface):

```

>>> with Camoufox(config={"property": "value"}) as browser:
```

Config data not set by the user will be automatically populated using [BrowserForge](https://github.com/daijro/browserforge) fingerprints, which mimic the statistical distribution of device characteristics in real-world traffic.

* * *

### [#](#getting-started)Getting started

Camoufox accepts the following properties:

Cursor Movement

cursor-movement/

Geolocation & Intl

geolocation/

Media & Audio

media-audio/

Miscellaneous

miscellaneous/