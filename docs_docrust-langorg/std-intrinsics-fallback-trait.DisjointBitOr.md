---
title: DisjointBitOr in std::intrinsics::fallback - Rust
url: https://doc.rust-lang.org/std/intrinsics/fallback/trait.DisjointBitOr.html
source: crawler
fetched_at: 2026-05-06T21:30:04.169251719-03:00
rendered_js: false
word_count: 61
summary: This document defines the DisjointBitOr trait, an experimental nightly-only Rust API used to facilitate bitwise OR operations on disjoint types where standard generic intrinsic calls are not supported.
tags:
    - rust
    - trait
    - bit-manipulation
    - intrinsics
    - nightly-api
    - experimental
category: reference
---

## Trait DisjointBitOr

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#114)

```rust
pub trait DisjointBitOr: Copy + 'static {
    // Required method
    unsafe fn disjoint_bitor(self, other: Self) -> Self;
}
```

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#117)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::disjoint_bitor`](https://doc.rust-lang.org/std/intrinsics/fn.disjoint_bitor.html "fn std::intrinsics::disjoint_bitor"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*