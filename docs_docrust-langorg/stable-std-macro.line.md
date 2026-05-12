---
title: line in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.line.html
source: crawler
fetched_at: 2026-05-06T21:28:40.771007447-03:00
rendered_js: false
word_count: 99
summary: This document describes the Rust line! macro, which returns the line number where the macro was invoked as a 1-based u32 value for debugging purposes.
tags:
    - rust-macro
    - debugging-tools
    - source-code-location
    - rust-language
    - development-utilities
category: reference
---

## Macro line

1.38.0 · [Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#1179)

```rust
macro_rules! line {
    () => { ... };
}
```

Expand description

Expands to the line number on which it was invoked.

With [`column!`](https://doc.rust-lang.org/stable/std/macro.column.html "macro std::column") and [`file!`](https://doc.rust-lang.org/stable/std/macro.file.html "macro std::file"), these macros provide debugging information for developers about the location within the source.

The expanded expression has type `u32` and is 1-based, so the first line in each file evaluates to 1, the second to 2, etc. This is consistent with error messages by common compilers or popular editors. The returned line is *not necessarily* the line of the `line!` invocation itself, but rather the first macro invocation leading up to the invocation of the `line!` macro.

## [§](#examples)Examples

```rust
let current_line = line!();
println!("defined on line: {current_line}");
```