---
title: DerefPure in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.DerefPure.html
source: crawler
fetched_at: 2026-05-06T21:24:03.626955555-03:00
rendered_js: false
word_count: 81
summary: This document defines the unstable DerefPure marker trait in Rust, which is used to indicate that dereference operations on a type are well-behaved and idempotent for pattern-matching soundness.
tags:
    - rust
    - unsafe-trait
    - nightly-api
    - deref
    - pattern-matching
    - compiler-internals
category: reference
---

```rust
pub unsafe trait DerefPure { }
```

🔬This is a nightly-only experimental API. (`deref_pure_trait` [#87121](https://github.com/rust-lang/rust/issues/87121))

Expand description

Perma-unstable marker trait. Indicates that the type has a well-behaved [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref") (and, if applicable, [`DerefMut`](https://doc.rust-lang.org/std/ops/trait.DerefMut.html "trait std::ops::DerefMut")) implementation. This is relied on for soundness of deref patterns.

FIXME(deref\_patterns): The precise semantics are undecided; the rough idea is that successive calls to `deref`/`deref_mut` without intermediate mutation should be idempotent, in the sense that they return the same value as far as pattern-matching is concerned. Calls to `deref`/`deref_mut` must leave the pointer itself likewise unchanged.