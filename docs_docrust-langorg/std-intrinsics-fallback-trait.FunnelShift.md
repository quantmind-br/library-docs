---
title: FunnelShift in std::intrinsics::fallback - Rust
url: https://doc.rust-lang.org/std/intrinsics/fallback/trait.FunnelShift.html
source: crawler
fetched_at: 2026-05-06T21:30:13.264719313-03:00
rendered_js: false
word_count: 85
summary: Defines the FunnelShift trait for performing unchecked funnel shift operations across generic types using experimental compiler intrinsics.
tags:
    - rust
    - intrinsics
    - bitwise-operations
    - experimental-api
    - generic-programming
    - trait-definition
category: api
---

```rust
pub trait FunnelShift: Copy + 'static {
    // Required methods
    unsafe fn unchecked_funnel_shl(self, rhs: Self, shift: u32) -> Self;
    unsafe fn unchecked_funnel_shr(self, rhs: Self, shift: u32) -> Self;
}
```

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#154)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::unchecked_funnel_shl`](https://doc.rust-lang.org/std/intrinsics/fn.unchecked_funnel_shl.html "fn std::intrinsics::unchecked_funnel_shl"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

[Source](https://doc.rust-lang.org/src/core/intrinsics/fallback.rs.html#158)

🔬This is a nightly-only experimental API. (`core_intrinsics_fallbacks`)

See [`super::unchecked_funnel_shr`](https://doc.rust-lang.org/std/intrinsics/fn.unchecked_funnel_shr.html "fn std::intrinsics::unchecked_funnel_shr"); we just need the trait indirection to handle different types since calling intrinsics with generics doesn’t work.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*