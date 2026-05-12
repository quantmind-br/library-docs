---
title: CarrylessMul in std::intrinsics::fallback - Rust
url: https://doc.rust-lang.org/std/intrinsics/fallback/trait.CarrylessMul.html
source: crawler
fetched_at: 2026-05-06T21:30:01.909869689-03:00
rendered_js: false
word_count: 61
summary: This document defines the CarrylessMul trait, an experimental Rust interface used to provide generic access to carryless multiplication intrinsics.
tags:
    - rust
    - trait
    - carryless-multiplication
    - experimental-api
    - intrinsics
    - generic-programming
category: reference
---

## Trait CarrylessMul

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#223)

```rust
pub trait CarrylessMul: Copy + 'static {
    // Required method
    fn carryless_mul(self, rhs: Self) -> Self;
}
```

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#226)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::carryless_mul`](https://doc.rust-lang.org/std/intrinsics/fn.carryless_mul.html "fn std::intrinsics::carryless_mul"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*