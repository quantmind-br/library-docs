---
title: Limit Number of Scans
url: https://epi052.github.io/feroxbuster-docs/examples/limit-scans
source: github_pages
fetched_at: 2026-02-06T10:55:46.10000984-03:00
rendered_js: true
word_count: 55
summary: This document explains how to restrict the number of simultaneous scans in feroxbuster using the --scan-limit flag to manage resources during recursive directory discovery.
tags:
    - feroxbuster
    - concurrency-limit
    - recursive-scanning
    - cli-options
    - resource-management
category: configuration
---

## Limit Total Number of Concurrent Scans

[Section titled “Limit Total Number of Concurrent Scans”](#limit-total-number-of-concurrent-scans)

Limit the number of scans permitted to run at any given time. Recursion will still identify new directories, but newly discovered directories can only begin scanning when the total number of active scans drops below the value passed to `--scan-limit`.

```

./feroxbuster -u http://127.1 --scan-limit 2
```

![limit-demo](https://epi052.github.io/feroxbuster-docs/images/examples/limit-demo.gif)