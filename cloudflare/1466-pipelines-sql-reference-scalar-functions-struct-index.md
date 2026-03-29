---
title: Struct functions · Cloudflare Pipelines Docs
url: https://developers.cloudflare.com/pipelines/sql-reference/scalar-functions/struct/index.md
source: llms
fetched_at: 2026-01-24T15:19:43.770190624-03:00
rendered_js: false
word_count: 95
summary: This document describes the struct scalar function in Cloudflare Pipelines, explaining how to create Arrow structs from multiple input expressions using standard naming conventions.
tags:
    - cloudflare-pipelines
    - scalar-functions
    - apache-datafusion
    - data-types
    - sql-reference
category: reference
---

*Cloudflare Pipelines scalar function implementations are based on [Apache DataFusion](https://arrow.apache.org/datafusion/) (via [Arroyo](https://www.arroyo.dev/)) and these docs are derived from the DataFusion function reference.*

## `struct`

Returns an Arrow struct using the specified input expressions. Fields in the returned struct use the `cN` naming convention. For example: `c0`, `c1`, `c2`, etc.

```plaintext
struct(expression1[, ..., expression_n])
```

For example, this query converts two columns `a` and `b` to a single column with a struct type of fields `c0` and `c1`:

```plaintext
select * from t;
+---+---+
| a | b |
+---+---+
| 1 | 2 |
| 3 | 4 |
+---+---+


select struct(a, b) from t;
+-----------------+
| struct(t.a,t.b) |
+-----------------+
| {c0: 1, c1: 2}  |
| {c0: 3, c1: 4}  |
+-----------------+
```

#### Arguments

* **expression\_n**: Expression to include in the output struct. Can be a constant, column, or function, and any combination of arithmetic or string operators.