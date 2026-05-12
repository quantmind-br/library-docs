---
title: StructuralPartialEq in std::marker - Rust
url: https://doc.rust-lang.org/std/marker/trait.StructuralPartialEq.html
source: crawler
fetched_at: 2026-05-06T21:24:03.035766291-03:00
rendered_js: false
word_count: 133
summary: The StructuralPartialEq trait is an experimental Rust mechanism used to validate that a type's constant values can be safely used in pattern matching by ensuring structural equality.
tags:
    - rust
    - trait
    - structural-equality
    - pattern-matching
    - experimental-api
    - constants
category: reference
---

## Trait StructuralPartialEq

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#260)

```rust
pub trait StructuralPartialEq { }
```

🔬This is a nightly-only experimental API. (`structural_match` [#31434](https://github.com/rust-lang/rust/issues/31434))

Expand description

Required trait for constants used in pattern matches.

Constants are only allowed as patterns if (a) their type implements `PartialEq`, and (b) interpreting the value of the constant as a pattern is equivalent to calling `PartialEq`. This ensures that constants used as patterns cannot expose implementation details in an unexpected way or cause semver hazards.

This trait ensures point (b). Any type that derives `PartialEq` automatically implements this trait.

Implementing this trait (which is unstable) is a way for type authors to explicitly allow comparing const values of this type; that operation will recursively compare all fields (including private fields), even if that behavior differs from `PartialEq`. This can make it semver-breaking to add further private fields to a type.