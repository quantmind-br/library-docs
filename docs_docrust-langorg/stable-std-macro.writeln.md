---
title: writeln in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.writeln.html
source: crawler
fetched_at: 2026-05-06T21:28:44.375778227-03:00
rendered_js: false
word_count: 49
summary: This document provides the technical specification and usage details for the writeln macro in Rust, which is used to write formatted text followed by a newline character to a buffer.
tags:
    - rust
    - macro
    - io-formatting
    - string-manipulation
    - standard-library
category: reference
---

## Macro writeln

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#644)

```rust
macro_rules! writeln {
    ($dst:expr $(,)?) => { ... };
    ($dst:expr, $($arg:tt)*) => { ... };
    ($($arg:tt)*) => { ... };
}
```

Expand description

Writes formatted data into a buffer, with a newline appended.

On all platforms, the newline is the LINE FEED character (`\n`/`U+000A`) alone (no additional CARRIAGE RETURN (`\r`/`U+000D`).

For more information, see [`write!`](https://doc.rust-lang.org/stable/std/macro.write.html "macro std::write"). For information on the format string syntax, see [`std::fmt`](https://doc.rust-lang.org/stable/std/fmt/index.html).

## [§](#examples)Examples

```rust
use std::io::{Write, Result};

fn main() -> Result<()> {
    let mut w = Vec::new();
    writeln!(&mut w)?;
    writeln!(&mut w, "test")?;
    writeln!(&mut w, "formatted {}", "arguments")?;

    assert_eq!(&w[..], "\ntest\nformatted arguments\n".as_bytes());
    Ok(())
}
```