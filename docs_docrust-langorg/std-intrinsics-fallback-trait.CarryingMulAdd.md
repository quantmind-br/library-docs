---
title: CarryingMulAdd in std::intrinsics::fallback - Rust
url: https://doc.rust-lang.org/std/intrinsics/fallback/trait.CarryingMulAdd.html#associatedtype.Unsigned
source: crawler
fetched_at: 2026-05-06T21:30:00.232826828-03:00
rendered_js: false
word_count: 50
summary: Defines an experimental nightly-only trait for performing combined multiplication and addition operations with carry handling in Rust.
tags:
    - rust-lang
    - trait
    - nightly-api
    - arithmetic
    - core-intrinsics
    - experimental
category: api
---

## Trait CarryingMulAdd

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#11)

```rust
pub trait CarryingMulAdd: Copy + 'static {
    type Unsigned: Copy + 'static;

    // Required method
    fn carrying_mul_add(
        self,
        multiplicand: Self,
        addend: Self,
        carry: Self,
    ) -> (Self::Unsigned, Self);
}
```

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#12)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#13-18)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*