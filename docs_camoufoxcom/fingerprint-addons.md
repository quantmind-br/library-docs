---
title: Addons | Camoufox
url: https://camoufox.com/fingerprint/addons/#default-addons
source: crawler
fetched_at: 2026-02-14T14:05:50.635993-03:00
rendered_js: true
word_count: 66
summary: This document explains how to manage browser extensions in the Camoufox library, covering how to load custom extracted addons and exclude default ones like uBlock Origin.
tags:
    - camoufox
    - python
    - browser-extensions
    - ublock-origin
    - browser-automation
category: guide
---

In the Camoufox Python library, addons can be loaded with the `addons` parameter.

Camoufox takes extracted addons. To load an `.xpi` file, rename it to a `.zip` file, extract it, and pass the extracted folder.

```

from camoufox.sync_api import Camoufox

with Camoufox(addons=['/path/to/addon', '/path/to/addon2']) as browser:
    page = browser.new_page()
```

* * *

### [#](#default-addons)Default Addons

Camoufox will automatically download and use the latest [uBlock Origin](https://ublockorigin.com/) with custom privacy/adblock filters to help with ad circumvention.

You can also **exclude** default addons with the `exclude_addons` parameter:

```

from camoufox.sync_api import Camoufox
from camoufox import DefaultAddons

with Camoufox(exclude_addons=[DefaultAddons.UBO]) as browser:
    page = browser.new_page()
```