---
title: RangePattern in core::pat - Rust
url: https://doc.rust-lang.org/core/pat/trait.RangePattern.html#associatedconstant.MAX
source: crawler
fetched_at: 2026-05-06T21:29:24.346000438-03:00
rendered_js: false
word_count: 117
summary: The RangePattern trait is an experimental Rust component used to define minimum and maximum constants and subtraction logic for integer and character types to support range-based pattern matching.
tags:
    - rust
    - experimental-api
    - trait
    - pattern-matching
    - generics
    - integer-types
category: api
---

## Trait RangePattern

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#28-41)

```rust
pub trait RangePattern {
    const MIN: Self;
    const MAX: Self;

    // Required method
    fn sub_one(self) -> Self;
}
```

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Expand description

A trait implemented for integer types and `char`. Useful in the future for generic pattern types, but used right now to simplify ast lowering of pattern type ranges.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#31)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#35)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

Trait version of the inherent `MIN` assoc const.

[Source](https://doc.rust-lang.org/src/core/pat.rs.html#40)

🔬This is a nightly-only experimental API. (`pattern_type_range_trait` [#123646](https://github.com/rust-lang/rust/issues/123646))

A compile-time helper to subtract 1 for exclusive ranges.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*