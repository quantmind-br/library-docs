---
title: SQL Reference · Cloudflare Analytics docs
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/type-conversion-functions/index.md
source: llms
fetched_at: 2026-01-24T15:35:33.169887949-03:00
rendered_js: false
word_count: 57
summary: This document describes the usage and behavior of functions for converting numeric or string expressions into unsigned 8-bit and 32-bit integers.
tags:
    - type-conversion
    - sql-functions
    - unsigned-integers
    - data-types
category: reference
---

## toUInt8 New

Usage:

```sql
toUInt8(<expression>)
```

Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 8 bit integer.

Behaviour for negative numbers is undefined.

## toUInt32

Usage:

```sql
toUInt32(<expression>)
```

Converts any numeric expression, or expression resulting in a string representation of a decimal, into an unsigned 32 bit integer.

Behaviour for negative numbers is undefined.