---
title: Freeze in std::marker - Rust
url: https://doc.rust-lang.org/std/marker/trait.Freeze.html
source: crawler
fetched_at: 2026-05-06T21:24:03.851229248-03:00
rendered_js: false
word_count: 99
summary: This document explains the experimental Freeze trait in Rust, which is used to determine if a type contains interior mutability for memory placement purposes.
tags:
    - rust-language
    - experimental-api
    - interior-mutability
    - memory-management
    - type-system
    - unsafecell
category: reference
---

```rust
pub unsafe auto trait Freeze { }
```

🔬This is a nightly-only experimental API. (`freeze` [#121675](https://github.com/rust-lang/rust/issues/121675))

Expand description

Used to determine whether a type contains any `UnsafeCell` internally, but not through an indirection. This affects, for example, whether a `static` of that type is placed in read-only static memory or writable static memory. This can be used to declare that a constant with a generic type will not contain interior mutability, and subsequently allow placing the constant behind references.

## [§](#safety)Safety

This trait is a core part of the language, it is just expressed as a trait in libcore for convenience. Do *not* implement it for other types.