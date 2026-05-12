---
title: Eq in std::cmp - Rust
url: https://doc.rust-lang.org/std/cmp/trait.Eq.html
source: crawler
fetched_at: 2026-05-06T21:24:02.333975282-03:00
rendered_js: false
word_count: 258
summary: This document defines the Eq trait in Rust, which extends PartialEq by requiring that comparisons adhere to the reflexive property of equivalence relations.
tags:
    - rust
    - traits
    - equivalence-relation
    - comparison
    - partial-eq
    - type-system
category: reference
---

## Trait Eq

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#338)

```rust
pub trait Eq: PartialEq { }
```

Expand description

Trait for comparisons corresponding to [equivalence relations](https://en.wikipedia.org/wiki/Equivalence_relation).

The primary difference to [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") is the additional requirement for reflexivity. A type that implements [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") guarantees that for all `a`, `b` and `c`:

- symmetric: `a == b` implies `b == a` and `a != b` implies `!(a == b)`
- transitive: `a == b` and `b == c` implies `a == c`

`Eq`, which builds on top of [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") also implies:

- reflexive: `a == a`

This property cannot be checked by the compiler, and therefore `Eq` is a trait without methods.

Violating this property is a logic error. The behavior resulting from a logic error is not specified, but users of the trait must ensure that such logic errors do *not* result in undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these methods.

Floating point types such as [`f32`](https://doc.rust-lang.org/std/primitive.f32.html "primitive f32") and [`f64`](https://doc.rust-lang.org/std/primitive.f64.html "primitive f64") implement only [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") but *not* `Eq` because `NaN` != `NaN`.

### [§](#derivable)Derivable

This trait can be used with `#[derive]`. When `derive`d, because `Eq` has no extra methods, it is only informing the compiler that this is an equivalence relation rather than a partial equivalence relation. Note that the `derive` strategy requires all fields are `Eq`, which isn’t always desired.

### [§](#how-can-i-implement-eq)How can I implement `Eq`?

If you cannot use the `derive` strategy, specify that your type implements `Eq`, which has no extra methods:

```rust
enum BookFormat {
    Paperback,
    Hardback,
    Ebook,
}

struct Book {
    isbn: i32,
    format: BookFormat,
}

impl PartialEq for Book {
    fn eq(&self, other: &Self) -> bool {
        self.isbn == other.isbn
    }
}

impl Eq for Book {}
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*