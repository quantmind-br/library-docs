---
title: column in std - Rust
url: https://doc.rust-lang.org/std/macro.column.html
source: crawler
fetched_at: 2026-05-06T21:32:30.179592536-03:00
rendered_js: false
word_count: 124
summary: This document describes the column! macro in Rust, which returns the 1-based column number where the macro was invoked to assist in debugging and source location tracking.
tags:
    - rust-macro
    - debugging-utilities
    - source-location
    - programming-tools
    - language-features
category: reference
---

## Macro column

1.38.0 · [Source](https://doc.rust-lang.org/src/core/macros/mod.rs.html#1218)

```rust
macro_rules! column {
    () => { ... };
}
```

Expand description

Expands to the column number at which it was invoked.

With [`line!`](https://doc.rust-lang.org/std/macro.line.html "macro std::line") and [`file!`](https://doc.rust-lang.org/std/macro.file.html "macro std::file"), these macros provide debugging information for developers about the location within the source.

The expanded expression has type `u32` and is 1-based, so the first column in each line evaluates to 1, the second to 2, etc. This is consistent with error messages by common compilers or popular editors. The returned column is *not necessarily* the line of the `column!` invocation itself, but rather the first macro invocation leading up to the invocation of the `column!` macro.

## [§](#examples)Examples

```rust
let current_col = column!();
println!("defined on column: {current_col}");
```

`column!` counts Unicode code points, not bytes or graphemes. As a result, the first two invocations return the same value, but the third does not.

```rust
let a = ("foobar", column!()).1;
let b = ("人之初性本善", column!()).1;
let c = ("f̅o̅o̅b̅a̅r̅", column!()).1; // Uses combining overline (U+0305)

assert_eq!(a, b);
assert_ne!(b, c);
```