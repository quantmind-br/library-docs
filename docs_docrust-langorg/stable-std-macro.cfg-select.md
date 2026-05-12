---
title: cfg_select in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.cfg_select.html
source: crawler
fetched_at: 2026-05-06T21:28:36.827430839-03:00
rendered_js: false
word_count: 90
summary: This document describes the cfg_select macro in Rust, which enables conditional compilation by evaluating cfg predicates to select and emit specific code blocks.
tags:
    - rust
    - macro
    - conditional-compilation
    - compile-time
    - cfg-predicates
category: reference
---

## Macro cfg\_select

1.95.0 · [Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#236)

```rust
pub macro cfg_select($($tt:tt)*) {
    ...
}
```

Expand description

Selects code at compile-time based on `cfg` predicates.

This macro evaluates, at compile-time, a series of `cfg` predicates, selects the first that is true, and emits the code guarded by that predicate. The code guarded by other predicates is not emitted.

An optional trailing `_` wildcard can be used to specify a fallback. If none of the predicates are true, a [`compile_error`](https://doc.rust-lang.org/stable/std/macro.compile_error.html "macro std::compile_error") is emitted.

## [§](#example)Example

```rust
cfg_select! {
    unix => {
        fn foo() { /* unix specific functionality */ }
    }
    target_pointer_width = "32" => {
        fn foo() { /* non-unix, 32-bit functionality */ }
    }
    _ => {
        fn foo() { /* fallback implementation */ }
    }
}
```

The `cfg_select!` macro can also be used in expression position, with or without braces on the right-hand side:

```rust
let _some_string = cfg_select! {
    unix => "With great power comes great electricity bills",
    _ => { "Behind every successful diet is an unwatched pizza" }
};
```