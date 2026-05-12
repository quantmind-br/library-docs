---
title: std::unsafe_binder - Rust
url: https://doc.rust-lang.org/stable/std/unsafe_binder/index.html
source: crawler
fetched_at: 2026-05-06T21:28:34.213667158-03:00
rendered_js: false
word_count: 42
summary: This document provides an overview of the experimental unsafe_binder module in Rust, which offers operators and macros for converting types into unsafe binders and vice-versa.
tags:
    - rust-language
    - experimental-api
    - unsafe-code
    - macro-definitions
    - type-conversion
category: api
---

[std](https://doc.rust-lang.org/stable/std/index.html)

## Module unsafe\_binder

[Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#312)

🔬This is a nightly-only experimental API. (`unsafe_binders` [#130516](https://github.com/rust-lang/rust/issues/130516))

Expand description

Operators used to turn types into unsafe binders and back.

## Macros[§](#macros)

[unwrap\_binder](https://doc.rust-lang.org/stable/std/unsafe_binder/macro.unwrap_binder.html "macro std::unsafe_binder::unwrap_binder")Experimental

Unwrap an unsafe binder into its underlying type.

[wrap\_binder](https://doc.rust-lang.org/stable/std/unsafe_binder/macro.wrap_binder.html "macro std::unsafe_binder::wrap_binder")Experimental

Wrap a type into an unsafe binder.