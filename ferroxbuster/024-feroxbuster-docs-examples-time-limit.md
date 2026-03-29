---
title: Enforce Time Limit
url: https://epi052.github.io/feroxbuster-docs/examples/time-limit
source: github_pages
fetched_at: 2026-02-06T10:56:14.686325142-03:00
rendered_js: true
word_count: 101
summary: This document explains how to use the time-limit feature in feroxbuster to automatically terminate a scan after a specified duration.
tags:
    - feroxbuster
    - time-limit
    - scan-management
    - command-line
    - security-scanning
category: guide
---

## Enforce a Time Limit on Your Scan

[Section titled “Enforce a Time Limit on Your Scan”](#enforce-a-time-limit-on-your-scan)

Version 1.10.0 adds the ability to set a maximum runtime, or time limit, on your scan. The usage is pretty simple: a number followed directly by a single character representing seconds, minutes, hours, or days. `feroxbuster` refers to this combination as a time\_spec.

Examples of possible time\_specs:

- `30s` - 30 seconds
- `20m` - 20 minutes
- `1h` - 1 hour
- `1d` - 1 day (why??)

A valid time\_spec can be passed to `--time-limit` in order to force a shutdown after the given time has elapsed.

![time-limit](https://epi052.github.io/feroxbuster-docs/images/examples/time-limit.gif)