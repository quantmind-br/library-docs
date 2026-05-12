---
title: unchecked_funnel_shl in std::intrinsics - Rust
url: https://doc.rust-lang.org/std/intrinsics/fn.unchecked_funnel_shl.html
source: crawler
fetched_at: 2026-05-06T21:30:14.107473277-03:00
rendered_js: false
word_count: 96
summary: This document describes the experimental unchecked_funnel_shl intrinsic, which performs a funnel shift left operation on two integers of the same type.
tags:
    - rust
    - intrinsic
    - bit-manipulation
    - funnel-shift
    - nightly-api
    - unsafe-code
category: reference
---

## Function unchecked\_funnel\_shl

[Source](https://doc.rust-lang.org/src/core/intrinsics/mod.rs.html#2144-2148)

```rust
pub const unsafe fn unchecked_funnel_shl<T>(a: T, b: T, shift: u32) -> T
where
    T: FunnelShift,
```

🔬This is a nightly-only experimental API. (`funnel_shifts` [#145686](https://github.com/rust-lang/rust/issues/145686))

Expand description

Funnel Shift left.

Concatenates `a` and `b` (with `a` in the most significant half), creating an integer twice as wide. Then shift this integer left by `shift`), and extract the most significant half. If `a` and `b` are the same, this is equivalent to a rotate left operation.

It is undefined behavior if `shift` is greater than or equal to the bit size of `T`.

Safe versions of this intrinsic are available on the integer primitives via the `funnel_shl` method. For example, [`u32::funnel_shl`](https://doc.rust-lang.org/std/primitive.u32.html#method.funnel_shl "method u32::funnel_shl").