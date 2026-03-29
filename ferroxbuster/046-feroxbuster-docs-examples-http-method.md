---
title: Specify HTTP Request Method
url: https://epi052.github.io/feroxbuster-docs/examples/http-method
source: github_pages
fetched_at: 2026-02-06T10:55:40.485008781-03:00
rendered_js: true
word_count: 54
summary: This document explains how to specify one or multiple HTTP request methods using the command-line interface in feroxbuster version 2.5.0.
tags:
    - feroxbuster
    - http-methods
    - command-line-options
    - web-security
    - network-scanning
category: guide
---

## Specify HTTP Request Method

[Section titled “Specify HTTP Request Method”](#specify-http-request-method)

Version 2.5.0 introduces the ability to specify the HTTP request method sent in each request. Some additional info:

- multiple methods may be used (i.e. `-m POST GET`)
- anything can be specified, not just valid http verbs (i.e. `-m derp`)

## Example

[Section titled “Example”](#example)

```

feroxbuster -u https://some-example-site.com -m POST GET dErP
```

![http-method](https://epi052.github.io/feroxbuster-docs/images/examples/http-method.gif)