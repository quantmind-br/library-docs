---
title: std::io::prelude - Rust
url: https://doc.rust-lang.org/stable/std/io/prelude/index.html
source: crawler
fetched_at: 2026-05-06T21:25:21.70401102-03:00
rendered_js: false
word_count: 50
summary: This document describes the Rust standard library I/O prelude module, which simplifies common I/O operations by grouping essential traits for easy import.
tags:
    - rust
    - io-module
    - prelude
    - standard-library
    - traits
    - imports
category: reference
---

[std](https://doc.rust-lang.org/stable/std/index.html)::[io](https://doc.rust-lang.org/stable/std/io/index.html)

## Module prelude

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/prelude.rs.html#1-14)

Expand description

The I/O Prelude.

The purpose of this module is to alleviate imports of many common I/O traits by adding a glob import to the top of I/O heavy modules:

```rust
use std::io::prelude::*;
```

## Re-exports[§](#reexports)

`pub use super::BufRead;`

`pub use super::Read;`

`pub use super::Seek;`

`pub use super::Write;`