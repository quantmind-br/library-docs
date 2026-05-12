---
title: Join in std::slice - Rust
url: https://doc.rust-lang.org/std/slice/trait.Join.html#associatedtype.Output
source: crawler
fetched_at: 2026-05-06T21:27:30.238908038-03:00
rendered_js: false
word_count: 57
summary: This document defines the Join trait, an experimental Rust interface for concatenating slices with a separator.
tags:
    - rust-trait
    - slice-concatenation
    - experimental-api
    - nightly-rust
    - type-system
category: api
---

```rust
pub trait Join<Separator> {
    type Output;

    // Required method
    fn join(slice: &Self, sep: Separator) -> Self::Output;
}
```

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

Expand description

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#717)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

The resulting type after concatenation

[Source](https://doc.rust-lang.org/src/alloc/slice.rs.html#721)

🔬This is a nightly-only experimental API. (`slice_concat_trait` [#27747](https://github.com/rust-lang/rust/issues/27747))

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*