---
title: Filter by Regex
url: https://epi052.github.io/feroxbuster-docs/examples/filter-regex
source: github_pages
fetched_at: 2026-02-06T10:55:23.9174354-03:00
rendered_js: true
word_count: 102
summary: This document explains how to use regular expressions to filter web scan responses by matching patterns in both the response body and headers.
tags:
    - feroxbuster
    - regex-filter
    - content-filtering
    - web-security
    - response-headers
category: guide
---

## Filter Response Using a Regular Expression

[Section titled “Filter Response Using a Regular Expression”](#filter-response-using-a-regular-expression)

Version 1.3.0 included an overhaul to the filtering system which allows for a wide array of filters to be added with minimal effort. The latest addition is a Regular Expression Filter. As responses come back from the scanned server, the **body** and **headers** of the response are checked against the filter’s regular expression. If the expression is found in the body, then that response is filtered out.

Version 2.10.4 added the ability to use regex to filter on the content of headers, in addition to the response’s body.

```

./feroxbuster -u http://127.1 --filter-regex '[aA]ccess [dD]enied.?' --output results.txt --json
```