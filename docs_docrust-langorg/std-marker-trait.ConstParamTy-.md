---
title: ConstParamTy_ in std::marker - Rust
url: https://doc.rust-lang.org/std/marker/trait.ConstParamTy_.html
source: crawler
fetched_at: 2026-05-06T21:28:06.350600795-03:00
rendered_js: false
word_count: 89
summary: This document defines the ConstParamTy_ marker trait, which specifies the requirements for types used as const generic parameters in Rust's nightly experimental features.
tags:
    - rust
    - const-generics
    - marker-trait
    - type-system
    - nightly-api
category: reference
---

## Trait ConstParamTy_

[Source](https://doc.rust-lang.org/src/core/marker.rs.html#1089)

```rust
pub trait ConstParamTy_: StructuralPartialEq + Eq { }
```

🔬This is a nightly-only experimental API. (`unsized_const_params` [#95174](https://github.com/rust-lang/rust/issues/95174))

Expand description

A marker for types which can be used as types of `const` generic parameters.

These types must have a proper equivalence relation (`Eq`) and it must be automatically derived (`StructuralPartialEq`). There’s a hard-coded check in the compiler ensuring that all fields are also `ConstParamTy`, which implies that recursively, all fields are `StructuralPartialEq`.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*