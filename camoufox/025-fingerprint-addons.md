---
title: Addons | Camoufox
url: https://camoufox.com/fingerprint/addons/
source: sitemap
fetched_at: 2026-03-09T16:48:08.759219-03:00
rendered_js: false
word_count: 66
summary: This document explains how to load custom browser extensions using the `addons` parameter in the Camoufox Python library, and how to exclude default extensions like uBlock Origin using `exclude_addons`.
tags:
    - camoufox
    - addons
    - extension-loading
    - python-library
    - default-addons
    - ublock-origin
category: guide
---

In the Camoufox Python library, addons can be loaded with the `addons` parameter.

Camoufox takes extracted addons. To load an `.xpi` file, rename it to a `.zip` file, extract it, and pass the extracted folder.

```python

from camoufox.sync_api import Camoufox

with Camoufox(addons=['/path/to/addon', '/path/to/addon2']) as browser:
    page = browser.new_page()
```

* * *

### [#](#default-addons)Default Addons

Camoufox will automatically download and use the latest [uBlock Origin](https://ublockorigin.com/) with custom privacy/adblock filters to help with ad circumvention.

You can also **exclude** default addons with the `exclude_addons` parameter:

```python

from camoufox.sync_api import Camoufox
from camoufox import DefaultAddons

with Camoufox(exclude_addons=[DefaultAddons.UBO]) as browser:
    page = browser.new_page()
```