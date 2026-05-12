---
title: println in std - Rust
url: https://doc.rust-lang.org/std/macro.println.html
source: crawler
fetched_at: 2026-05-06T21:21:47.381785048-03:00
rendered_js: false
word_count: 142
summary: This document describes the println! macro in Rust, which is used to print formatted text to the standard output followed by a newline character.
tags:
    - rust
    - standard-library
    - macros
    - input-output
    - stdout
    - formatting
category: reference
---

## Macro println

1.0.0 · [Source](https://doc.rust-lang.org/src/std/macros.rs.html#138-145)

```rust
macro_rules! println {
    () => { ... };
    ($($arg:tt)*) => { ... };
}
```

Expand description

Prints to the standard output, with a newline.

On all platforms, the newline is the LINE FEED character (`\n`/`U+000A`) alone (no additional CARRIAGE RETURN (`\r`/`U+000D`)).

This macro uses the same syntax as [`format!`](https://doc.rust-lang.org/std/macro.format.html "macro std::format"), but writes to the standard output instead. See [`std::fmt`](https://doc.rust-lang.org/std/fmt/index.html "mod std::fmt") for more information.

The `println!` macro will lock the standard output on each call. If you call `println!` within a hot loop, this behavior may be the bottleneck of the loop. To avoid this, lock stdout with [`io::stdout().lock()`](https://doc.rust-lang.org/std/io/struct.Stdout.html "struct std::io::Stdout"):

```rust
use std::io::{stdout, Write};

let mut lock = stdout().lock();
writeln!(lock, "hello world").unwrap();
```

Use `println!` only for the primary output of your program. Use [`eprintln!`](https://doc.rust-lang.org/std/macro.eprintln.html "macro std::eprintln") instead to print error and progress messages.

See the formatting documentation in [`std::fmt`](https://doc.rust-lang.org/std/fmt/index.html "mod std::fmt") for details of the macro argument syntax.

## [§](#panics)Panics

Panics if writing to [`io::stdout`](https://doc.rust-lang.org/std/io/fn.stdout.html "fn std::io::stdout") fails.

Writing to non-blocking stdout can cause an error, which will lead this macro to panic.

## [§](#examples)Examples

```rust
println!(); // prints just a newline
println!("hello there!");
println!("format {} arguments", "some");
let local_variable = "some";
println!("format {local_variable} arguments");
```