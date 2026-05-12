---
title: eprintln in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.eprintln.html
source: crawler
fetched_at: 2026-05-06T21:27:05.797867908-03:00
rendered_js: false
word_count: 88
summary: This document describes the eprintln! macro, which prints formatted text to the standard error stream followed by a newline.
tags:
    - rust
    - macro
    - standard-error
    - console-output
    - debugging
    - io-operations
category: reference
---

## Macro eprintln

1.19.0 · [Source](https://doc.rust-lang.org/stable/src/std/macros.rs.html#216-223)

```rust
macro_rules! eprintln {
    () => { ... };
    ($($arg:tt)*) => { ... };
}
```

Expand description

Prints to the standard error, with a newline.

Equivalent to the [`println!`](https://doc.rust-lang.org/stable/std/macro.println.html "macro std::println") macro, except that output goes to [`io::stderr`](https://doc.rust-lang.org/stable/std/io/fn.stderr.html "fn std::io::stderr") instead of [`io::stdout`](https://doc.rust-lang.org/stable/std/io/fn.stdout.html "fn std::io::stdout"). See [`println!`](https://doc.rust-lang.org/stable/std/macro.println.html "macro std::println") for example usage.

Use `eprintln!` only for error and progress messages. Use `println!` instead for the primary output of your program.

See the formatting documentation in [`std::fmt`](https://doc.rust-lang.org/stable/std/fmt/index.html "mod std::fmt") for details of the macro argument syntax.

## [§](#panics)Panics

Panics if writing to `io::stderr` fails.

Writing to non-blocking stderr can cause an error, which will lead this macro to panic.

## [§](#examples)Examples

```rust
eprintln!("Error: Could not complete task");
```