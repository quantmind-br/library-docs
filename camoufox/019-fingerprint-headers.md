---
title: HTTP Headers | Camoufox
url: https://camoufox.com/fingerprint/headers/
source: sitemap
fetched_at: 2026-03-09T16:48:07.794469-03:00
rendered_js: false
word_count: 32
summary: This document lists the specific network headers that Camoufox is capable of overriding within its configuration settings.
tags:
    - camoufox
    - network-headers
    - user-agent
    - accept-language
    - accept-encoding
    - configuration
category: reference
---

#### [#](#camoufox-can-override-the-following-network-headers)Camoufox can override the following network headers.

* * *

## [#](#properties)Properties

PropertyTypeDescription`headers.User-Agent`strBrowser and system information`headers.Accept-Language`strAcceptable languages for the response`headers.Accept-Encoding`strAcceptable encodings for the response

* * *

##### Note

If `headers.User-Agent` is not set, it will fall back to `navigator.userAgent`.