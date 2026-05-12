---
title: module_path in std - Rust
url: https://doc.rust-lang.org/std/macro.module_path.html
source: crawler
fetched_at: 2026-05-06T21:32:33.743634063-03:00
rendered_js: false
word_count: 55
summary: This document describes the module_path! macro, which provides the full hierarchical module path of the current execution context.
tags:
    - rust
    - macro
    - module-path
    - standard-library
    - introspection
category: reference
---

[std](https://doc.rust-lang.org/std/index.html)

## Macro module\_path

1.38.0 · [Source](https://doc.rust-lang.org/src/core/macros/mod.rs.html#1386)

```rust
macro_rules! module_path {
    () => { ... };
}
```

Expand description

Expands to a string that represents the current module path.

The current module path can be thought of as the hierarchy of modules leading back up to the crate root. The first component of the path returned is the name of the crate currently being compiled.

## [§](#examples)Examples

```rust
mod test {
    pub fn foo() {
        assert!(module_path!().ends_with("test"));
    }
}

test::foo();
```