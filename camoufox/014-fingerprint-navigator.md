---
title: Navigator | Camoufox
url: https://camoufox.com/fingerprint/navigator/
source: sitemap
fetched_at: 2026-03-09T16:48:04.18674-03:00
rendered_js: false
word_count: 69
summary: This document outlines the capabilities and safety of spoofing Navigator properties in Firefox, noting specific behaviors and potential leakage points when emulating Chrome.
tags:
    - navigator-properties
    - firefox-spoofing
    - user-agent
    - privacy-settings
    - webdriver
category: guide
---

Navigator properties can be fully spoofed to other Firefox fingerprints, and it is **completely safe**!

* * *

## [#](#properties)Properties

* * *

##### Note

- **navigator.webdriver** is set to false at all times.
- `navigator.language` & `navigator.languages` will fall back to the `locale:language`/`locale:region` values if not set.
- When spoofing Chrome fingerprints, the following may leak:
  
  - navigator.userAgentData missing.
  - navigator.deviceMemory missing.
- Changing the presented Firefox version can be detected by some testing websites, but typically will not flag production WAFs.