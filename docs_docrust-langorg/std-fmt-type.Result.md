---
title: Result in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/type.Result.html
source: crawler
fetched_at: 2026-05-06T21:24:26.342588717-03:00
rendered_js: false
word_count: 25
summary: Defines the Result type alias used specifically by Rust formatting methods to indicate success or failure during display operations.
tags:
    - rust
    - fmt
    - type-alias
    - result-type
    - error-handling
category: reference
---

## Type Alias Result

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#72)

```rust
pub type Result = Result<(), Error>;
```

Expand description

The type returned by formatter methods.

## [§](#examples)Examples

```rust
use std::fmt;

#[derive(Debug)]
struct Triangle {
    a: f32,
    b: f32,
    c: f32
}

impl fmt::Display for Triangle {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {}, {})", self.a, self.b, self.c)
    }
}

let pythagorean_triple = Triangle { a: 3.0, b: 4.0, c: 5.0 };

assert_eq!(format!("{pythagorean_triple}"), "(3, 4, 5)");
```

```rust
pub enum Result {
    Ok(()),
    Err(Error),
}
```

[§](#variant.Ok)1.0.0

Contains the success value

[§](#variant.Err)1.0.0

Contains the error value