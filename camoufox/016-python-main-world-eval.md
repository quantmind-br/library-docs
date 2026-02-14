---
title: Main World Execution | Camoufox
url: https://camoufox.com/python/main-world-eval/
source: crawler
fetched_at: 2026-02-14T14:05:40.232129-03:00
rendered_js: true
word_count: 103
summary: This document explains how to interact with and modify the DOM using Camoufox by switching between isolated and main world JavaScript execution scopes.
tags:
    - camoufox
    - dom-manipulation
    - javascript-execution
    - browser-automation
    - web-scraping
category: guide
---

* * *

### [#](#reading-the-dom---isolated-world)Reading the DOM - Isolated World

By default, all JavaScript execution is ran in an isolated scope, invisible to the page.

This makes it impossible for the page to detect JavaScript reading the DOM:

```

>>> page.goto("https://example.com/")
>>> page.evaluate("document.querySelector('h1').innerText")
'Example Domain'
```

However, your JavaScript will **not** be able to modify the DOM:

```

>>> page.evaluate("document.querySelector('h1').remove()")
# Will not work!
```

* * *

### [#](#modifying-the-dom---main-world)Modifying the DOM - Main World

To be able to modify the DOM, run JavaScript in the **main world**—the non-isolated scope.

* * *

To enable main world execution, set the `main_world_eval` parameter to `True`:

```

with Camoufox(main_world_eval=True) as browser:
    page = browser.new_page()
    page.goto("https://example.com/")
```

Now, you can inject JavaScript in the main world by prefixing the code with `mw:`

```

>>> page.evaluate("mw:document.querySelector('h1').remove()")
# h1 is now removed!
```

You can also return JSON serializable data from the main world:

```

>>> page.evaluate("mw:{key: 'value'}")
{'key': 'value'}
```