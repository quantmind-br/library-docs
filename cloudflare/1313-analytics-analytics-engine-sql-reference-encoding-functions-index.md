---
title: SQL Reference · Cloudflare Analytics docs
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/encoding-functions/index.md
source: llms
fetched_at: 2026-01-24T15:35:25.716711355-03:00
rendered_js: false
word_count: 67
summary: Provides documentation and usage instructions for the bin and hex functions used to convert expressions into binary and hexadecimal string representations.
tags:
    - sql-functions
    - binary-conversion
    - hexadecimal-conversion
    - data-transformation
    - string-manipulation
category: reference
---

## bin New

Usage:

```sql
bin(<expression>)
```

`bin` returns a string containing the binary representation of its argument.

Examples:

```sql
-- get the binary representation of 1
bin(1)
-- get the binary representation of a string`
bin('abc')
```

## hex New

Usage:

```sql
hex(<expression>)
```

`hex` returns a string containing the hexadecimal representation of its argument.

Examples:

```sql
-- get the hexadecimal representation of 1
hex(1)
-- get the hexadecimal representation of a string`
hex('abc')
```