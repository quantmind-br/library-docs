---
title: ToOwned in std::borrow - Rust
url: https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#associatedtype.Owned
source: crawler
fetched_at: 2026-05-06T21:24:11.944507885-03:00
rendered_js: false
word_count: 127
summary: The ToOwned trait provides a mechanism to generalize the cloning process by constructing owned data types from borrowed references.
tags:
    - rust-language
    - memory-management
    - trait-system
    - borrowing
    - cloning
category: reference
---

## Trait ToOwned

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#27)

```rust
pub trait ToOwned {
    type Owned: Borrow<Self>;

    // Required method
    fn to_owned(&self) -> Self::Owned;

    // Provided method
    fn clone_into(&self, target: &mut Self::Owned) { ... }
}
```

Expand description

A generalization of `Clone` to borrowed data.

Some types make it possible to go from borrowed to owned, usually by implementing the `Clone` trait. But `Clone` works only for going from `&T` to `T`. The `ToOwned` trait generalizes `Clone` to construct owned data from any borrow of a given type.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#30)

The resulting type after obtaining ownership.

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#48)

Creates owned data from borrowed data, usually by cloning.

##### [§](#examples)Examples

Basic usage:

```rust
let s: &str = "a";
let ss: String = s.to_owned();

let v: &[i32] = &[1, 2];
let vv: Vec<i32> = v.to_owned();
```

1.63.0 · [Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#66)

Uses borrowed data to replace owned data, usually by cloning.

This is borrow-generalized version of [`Clone::clone_from`](https://doc.rust-lang.org/std/clone/trait.Clone.html#method.clone_from "method std::clone::Clone::clone_from").

##### [§](#examples-1)Examples

Basic usage:

```rust
let mut s: String = String::new();
"hello".clone_into(&mut s);

let mut v: Vec<i32> = Vec::new();
[1, 2][..].clone_into(&mut v);
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*