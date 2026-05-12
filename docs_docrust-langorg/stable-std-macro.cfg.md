---
title: cfg in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.cfg.html
source: crawler
fetched_at: 2026-05-06T21:28:36.42137392-03:00
rendered_js: false
word_count: 95
summary: This document explains the usage of the cfg! macro in Rust, which allows for compile-time evaluation of boolean configuration flags within expression blocks.
tags:
    - rust
    - macros
    - conditional-compilation
    - compile-time
    - configuration-flags
category: reference
---

## Macro cfg

1.38.0 · [Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#1419)

```rust
macro_rules! cfg {
    ($($cfg:tt)*) => { ... };
}
```

Expand description

Evaluates boolean combinations of configuration flags at compile-time.

In addition to the `#[cfg]` attribute, this macro is provided to allow boolean expression evaluation of configuration flags. This frequently leads to less duplicated code.

The syntax given to this macro is the same syntax as the [`cfg`](https://doc.rust-lang.org/stable/reference/conditional-compilation.html#the-cfg-attribute) attribute.

`cfg!`, unlike `#[cfg]`, does not remove any code and only evaluates to true or false. For example, all blocks in an if/else expression need to be valid when `cfg!` is used for the condition, regardless of what `cfg!` is evaluating.

## [§](#examples)Examples

```rust
let my_directory = if cfg!(windows) {
    "windows-specific-directory"
} else {
    "unix-directory"
};
```