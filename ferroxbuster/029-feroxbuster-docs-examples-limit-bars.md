---
title: Limit Number of Progress Bars
url: https://epi052.github.io/feroxbuster-docs/examples/limit-bars
source: github_pages
fetched_at: 2026-02-06T10:55:41.322274179-03:00
rendered_js: true
word_count: 57
summary: Explains how to use the --limit-bars option in feroxbuster to restrict the number of active progress bars displayed during long-running scans.
tags:
    - feroxbuster
    - progress-bars
    - command-line-options
    - scan-optimization
category: guide
---

## Limit the number of progress bars shown at any given time

[Section titled “Limit the number of progress bars shown at any given time”](#limit-the-number-of-progress-bars-shown-at-any-given-time)

Version 2.11.0 introduces the ability to limit the number of progress bars feroxbuster displays at any given time. This is useful for very large and/or long running scans.

## Example

[Section titled “Example”](#example)

```

feroxbuster -u https://some-example-site.com --limit-bars 4
```

![limit-bars-demo](https://epi052.github.io/feroxbuster-docs/images/examples/limit-bars-demo.gif)