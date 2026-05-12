---
title: log_syntax in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.log_syntax.html
source: crawler
fetched_at: 2026-05-06T21:28:47.028600636-03:00
rendered_js: true
word_count: 24
summary: This document describes the experimental log_syntax macro in Rust, which is used to output tokens to the standard output during compilation.
tags:
    - rust
    - macro
    - experimental-api
    - debugging
    - token-output
category: reference
---

[std](https://doc.rust-lang.org/stable/std/index.html)

## Macro log\_syntax

[Source](https://doc.rust-lang.org/stable/src/core/macros/mod.rs.html#1704)

[Search](https://doc.rust-lang.org/stable/std/macro.log_syntax.html?search=)

[Settings](https://doc.rust-lang.org/stable/settings.html)

[Help](https://doc.rust-lang.org/stable/help.html)

```rust
macro_rules! log_syntax {
    ($($arg:tt)*) => { ... };
}
```

🔬This is a nightly-only experimental API. (`log_syntax` [#29598](https://github.com/rust-lang/rust/issues/29598))

Expand description

Prints passed tokens into the standard output.