---
title: ZeroablePrimitive in std::num - Rust
url: https://doc.rust-lang.org/std/num/trait.ZeroablePrimitive.html#associatedtype.NonZeroInner
source: crawler
fetched_at: 2026-05-06T21:29:32.011049611-03:00
rendered_js: false
word_count: 131
summary: This document defines the ZeroablePrimitive trait, an internal, unstable Rust marker trait used to facilitate the safe conversion of primitive types into non-zero representations.
tags:
    - rust-language
    - nonzero-types
    - experimental-api
    - primitive-types
    - trait-definition
    - memory-safety
category: reference
---

## Trait ZeroablePrimitive

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#33)

```rust
pub unsafe trait ZeroablePrimitive:
    Sized
    + Copy
    + Sealed {
    type NonZeroInner: Copy;
}
```

🔬This is a nightly-only experimental API. (`nonzero_internals`)

Expand description

A marker trait for primitive types which can be zero.

This is an implementation detail for `NonZero<T>` which may disappear or be replaced at any time.

## [§](#safety)Safety

Types implementing this trait must be primitives that are valid when zeroed.

The associated `Self::NonZeroInner` type must have the same size+align as `Self`, but with a niche and bit validity making it so the following `transmutes` are sound:

- `Self::NonZeroInner` to `Option<Self::NonZeroInner>`
- `Option<Self::NonZeroInner>` to `Self`

(And, consequently, `Self::NonZeroInner` to `Self`.)

[Source](https://doc.rust-lang.org/src/core/num/nonzero.rs.html#35)

🔬This is a nightly-only experimental API. (`nonzero_internals`)

A type like `Self` but with a niche that includes zero.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*