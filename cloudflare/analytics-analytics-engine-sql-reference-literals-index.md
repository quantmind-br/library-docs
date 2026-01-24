---
title: Workers Analytics Engine SQL Reference · Cloudflare Analytics docs
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/literals/index.md
source: llms
fetched_at: 2026-01-24T15:35:29.102944082-03:00
rendered_js: false
word_count: 65
summary: This document defines the supported literal data types and their syntax, covering numeric, string, boolean, and time interval formats.
tags:
    - data-types
    - literals
    - syntax-reference
    - time-intervals
    - query-language
category: reference
---

The following literals are supported:

| Type | Syntax |
| - | - |
| integer | `42`, `-42` |
| double | `4.2`, `-4.2` |
| string | `'so long and thanks for all the fish'` |
| boolean | `true` or `false` |
| time interval | `INTERVAL '42' DAY` Intervals of `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE` and `SECOND` are supported |