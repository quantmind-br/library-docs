---
title: Result in std::io - Rust
url: https://doc.rust-lang.org/std/io/type.Result.html
source: crawler
fetched_at: 2026-05-06T21:23:53.869882399-03:00
rendered_js: false
word_count: 119
summary: This document defines the io::Result type alias in Rust, which is a specialized version of the standard Result type used for I/O operations to simplify error handling.
tags:
    - rust
    - io-error
    - result-type
    - type-alias
    - error-handling
    - standard-library
category: reference
---

## Type Alias Result

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/error.rs.html#59)

```rust
pub type Result<T> = Result<T, Error>;
```

Expand description

A specialized [`Result`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result") type for I/O operations.

This type is broadly used across [`std::io`](https://doc.rust-lang.org/std/io/index.html "mod std::io") for any operation which may produce an error.

This type alias is generally used to avoid writing out [`io::Error`](https://doc.rust-lang.org/std/io/struct.Error.html "struct std::io::Error") directly and is otherwise a direct mapping to [`Result`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result").

While usual Rust style is to import types directly, aliases of [`Result`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result") often are not, to make it easier to distinguish between them. [`Result`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result") is generally assumed to be [`std::result::Result`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result"), and so users of this alias will generally use `io::Result` instead of shadowing the [prelude](https://doc.rust-lang.org/std/prelude/index.html "mod std::prelude")’s import of [`std::result::Result`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result").

## [§](#examples)Examples

A convenience function that bubbles an `io::Result` to its caller:

```rust
use std::io;

fn get_string() -> io::Result<String> {
    let mut buffer = String::new();

    io::stdin().read_line(&mut buffer)?;

    Ok(buffer)
}
```

```rust
pub enum Result<T> {
    Ok(T),
    Err(Error),
}
```

[§](#variant.Ok)1.0.0

Contains the success value

[§](#variant.Err)1.0.0

Contains the error value