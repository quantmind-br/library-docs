---
title: const_format_args in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.const_format_args.html
source: crawler
fetched_at: 2026-05-06T21:28:46.721821896-03:00
rendered_js: false
word_count: 48
summary: This document describes the const_format_args macro in Rust, an experimental feature that allows for string formatting within constant contexts.
tags:
    - rust-language
    - macro
    - const-context
    - experimental-api
    - string-formatting
category: api
---

[std](https://doc.rust-lang.org/stable/std/index.html)

## Macro const\_format\_args

[Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#1013)

```rust
macro_rules! const_format_args {
    ($fmt:expr) => { ... };
    ($fmt:expr, $($args:tt)*) => { ... };
}
```

🔬This is a nightly-only experimental API. (`const_format_args`)

Expand description

Same as [`format_args`](https://doc.rust-lang.org/stable/std/macro.format_args.html "macro std::format_args"), but can be used in some const contexts.

This macro is used by the panic macros for the `const_panic` feature.

This macro will be removed once `format_args` is allowed in const contexts.