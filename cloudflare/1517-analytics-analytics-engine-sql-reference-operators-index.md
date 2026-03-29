---
title: Workers Analytics Engine SQL Reference · Cloudflare Analytics docs
url: https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/index.md
source: llms
fetched_at: 2026-01-24T15:35:29.571068173-03:00
rendered_js: false
word_count: 338
summary: This document provides a comprehensive reference of the arithmetic, comparison, pattern matching, boolean, and unary operators supported for data querying and filtering.
tags:
    - sql-operators
    - comparison-operators
    - pattern-matching
    - arithmetic-operators
    - boolean-operators
    - query-syntax
category: reference
---

The following operators are supported:

## Arithmetic operators

| Operator | Description |
| - | - |
| `+` | addition |
| `-` | subtraction |
| `*` | multiplication |
| `/` | division |
| `%` | modulus |

## Comparison operators

| Operator | Description |
| - | - |
| `=` | equals |
| `<` | less than |
| `>` | greater than |
| `<=` | less than or equal to |
| `>=` | greater than or equal to |
| `<>` or `!=` | not equal |
| `IN` | true if the preceding expression's value is in the list `column IN ('a', 'list', 'of', 'values')` |
| `NOT IN` | true if the preceding expression's value is not in the list `column NOT IN ('a', 'list', 'of', 'values')` |

We also support the `BETWEEN` operator for checking a value is in an inclusive range: `a [NOT] BETWEEN b AND c`.

### Pattern matching operators New

| Operator | Description |
| - | - |
| `LIKE` | true if the string matches the pattern (case-sensitive) `column LIKE 'pattern%'` |
| `NOT LIKE` | true if the string does not match the pattern (case-sensitive) `column NOT LIKE 'pattern%'` |
| `ILIKE` | true if the string matches the pattern (case-insensitive) `column ILIKE 'pattern%'` |
| `NOT ILIKE` | true if the string does not match the pattern (case-insensitive) `column NOT ILIKE 'pattern%'` |

Pattern matching supports two wildcard characters:

* `%` matches any sequence of zero or more characters
* `_` matches any single character

Examples:

```sql
-- Match strings starting with "error"
WHERE blob1 LIKE 'error%'


-- Match strings ending with ".jpg" (case-insensitive)
WHERE blob2 ILIKE '%.jpg'


-- Match strings containing "test" anywhere
WHERE blob3 LIKE '%test%'


-- Match exactly 5 characters starting with "log"
WHERE blob4 LIKE 'log__'


-- Exclude strings containing "debug" (case-insensitive)
WHERE blob5 NOT ILIKE '%debug%'
```

## Boolean operators

| Operator | Description |
| - | - |
| `AND` | boolean "AND" (true if both sides are true) |
| `OR` | boolean "OR" (true if either side or both sides are true) |
| `NOT` | boolean "NOT" (true if following expression is false and visa-versa) |

## Unary operators

| Operator | Description |
| - | - |
| `-` | negation operator (for example, `-42`) |