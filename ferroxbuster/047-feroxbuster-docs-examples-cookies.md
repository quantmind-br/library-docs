---
title: Specify Cookies
url: https://epi052.github.io/feroxbuster-docs/examples/cookies
source: github_pages
fetched_at: 2026-02-06T10:55:05.471625022-03:00
rendered_js: true
word_count: 36
summary: This document explains the usage of the -b and --cookies flags in feroxbuster for specifying HTTP cookies directly as a simplified alternative to using headers.
tags:
    - feroxbuster
    - http-cookies
    - cli-options
    - web-scanning
    - authentication
category: reference
---

## Specify Cookies Directly

[Section titled “Specify Cookies Directly”](#specify-cookies-directly)

Version 2.5.0 gave http cookies their own flag, separate from `-H, --headers`. The new `-b, --cookies` is simply syntactic sugar around `-H, --headers`.

## Example

[Section titled “Example”](#example)

```

feroxbuster -u https://some-example-site.com -b sessionId=38afes7a8
```

![session-cookie](https://epi052.github.io/feroxbuster-docs/images/examples/session-cookie.png)