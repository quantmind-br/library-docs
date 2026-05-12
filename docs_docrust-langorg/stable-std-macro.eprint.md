---
title: eprint in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.eprint.html
source: crawler
fetched_at: 2026-05-06T21:28:39.489495655-03:00
rendered_js: false
word_count: 85
summary: This document describes the Rust eprint macro, which is used to output formatted text to the standard error stream.
tags:
    - rust
    - macro
    - standard-error
    - io
    - logging
    - formatting
category: reference
---

## Macro eprint

1.19.0 · [Source](https://doc.rust-lang.org/stable/src/std/macros.rs.html#178-182)

```rust
macro_rules! eprint {
    ($($arg:tt)*) => { ... };
}
```

Expand description

Prints to the standard error.

Equivalent to the [`print!`](https://doc.rust-lang.org/stable/std/macro.print.html "macro std::print") macro, except that output goes to [`io::stderr`](https://doc.rust-lang.org/stable/std/io/fn.stderr.html "fn std::io::stderr") instead of [`io::stdout`](https://doc.rust-lang.org/stable/std/io/fn.stdout.html "fn std::io::stdout"). See [`print!`](https://doc.rust-lang.org/stable/std/macro.print.html "macro std::print") for example usage.

Use `eprint!` only for error and progress messages. Use `print!` instead for the primary output of your program.

See the formatting documentation in [`std::fmt`](https://doc.rust-lang.org/stable/std/fmt/index.html "mod std::fmt") for details of the macro argument syntax.

## [§](#panics)Panics

Panics if writing to `io::stderr` fails.

Writing to non-blocking stderr can cause an error, which will lead this macro to panic.

## [§](#examples)Examples

```rust
eprint!("Error: Could not complete task");
```