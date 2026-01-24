---
title: SQL Reference · Cloudflare Analytics docs
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/conditional-functions/index.md
source: llms
fetched_at: 2026-01-24T15:35:23.886002056-03:00
rendered_js: false
word_count: 13
summary: This document explains the usage and syntax of the conditional IF function used to return specific values based on a boolean evaluation.
tags:
    - sql-functions
    - conditional-logic
    - expression-syntax
    - data-processing
    - query-language
category: reference
---

## if

Usage:

```sql
if(<condition>, <true_expression>, <false_expression>)
```

Returns `<true_expression>` if `<condition>` evaluates to true, else returns `<false_expression>`.

Example:

```sql
if(temp > 20, 'It is warm', 'Bring a jumper')
```