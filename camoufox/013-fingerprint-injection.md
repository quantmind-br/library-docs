---
title: Fingerprint Injection | Camoufox
url: https://camoufox.com/fingerprint/
source: sitemap
fetched_at: 2026-03-09T16:47:52.459072-03:00
rendered_js: false
word_count: 77
summary: This document explains how to use the Camoufox library, specifically its Python interface, to spoof browser fingerprint properties by passing configuration data.
tags:
    - fingerprinting
    - spoofing
    - python-interface
    - browser-configuration
    - c++-implementation
category: guide
---

In Camoufox, data is intercepted at the C++ implementation level, making the changes undetectable through JavaScript inspection.

To spoof fingerprint properties, pass a JSON containing properties to spoof to the [Python interface](https://github.com/daijro/camoufox/tree/main/pythonlib#camoufox-python-interface):

```python

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