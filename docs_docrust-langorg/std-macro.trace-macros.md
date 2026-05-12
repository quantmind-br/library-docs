---
title: trace_macros in std - Rust
url: https://doc.rust-lang.org/std/macro.trace_macros.html
source: crawler
fetched_at: 2026-05-06T21:32:38.858224426-03:00
rendered_js: true
word_count: 27
summary: This document describes the trace_macros experimental feature in Rust, which allows developers to debug macro expansion by enabling or disabling tracing output.
tags:
    - rust
    - macro-debugging
    - experimental-api
    - compiler-tools
    - metaprogramming
category: reference
---

[std](https://doc.rust-lang.org/std/index.html)

## Macro trace\_macros

[Source](https://doc.rust-lang.org/src/core/macros/mod.rs.html#1718)

[Search](https://doc.rust-lang.org/std/macro.trace_macros.html?search=)

[Settings](https://doc.rust-lang.org/settings.html)

[Help](https://doc.rust-lang.org/help.html)

```rust
macro_rules! trace_macros {
    (true) => { ... };
    (false) => { ... };
}
```

🔬This is a nightly-only experimental API. (`trace_macros` [#29598](https://github.com/rust-lang/rust/issues/29598))

Expand description

Enables or disables tracing functionality used for debugging other macros.