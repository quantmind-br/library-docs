---
title: std::clone - Rust
url: https://doc.rust-lang.org/stable/std/clone/index.html
source: crawler
fetched_at: 2026-05-06T21:25:30.8216118-03:00
rendered_js: false
word_count: 171
summary: This document explains the purpose and implementation of the Clone trait in Rust, which is used for creating explicit duplicates of types that are not implicitly copyable.
tags:
    - rust
    - trait
    - clone
    - memory-management
    - type-system
    - programming-concepts
category: concept
---

## Module clone

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#272)

Expand description

The `Clone` trait for types that cannot be ‘implicitly copied’.

In Rust, some simple types are “implicitly copyable” and when you assign them or pass them as arguments, the receiver will get a copy, leaving the original value in place. These types do not require allocation to copy and do not have finalizers (i.e., they do not contain owned boxes or implement [`Drop`](https://doc.rust-lang.org/stable/std/ops/trait.Drop.html "trait std::ops::Drop")), so the compiler considers them cheap and safe to copy. For other types copies must be made explicitly, by convention implementing the [`Clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") trait and calling the [`clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") method.

Basic usage example:

```rust
let s = String::new(); // String type implements Clone
let copy = s.clone(); // so we can clone it
```

To easily implement the Clone trait, you can also use `#[derive(Clone)]`. Example:

```rust
#[derive(Clone)] // we add the Clone trait to Morpheus struct
struct Morpheus {
   blue_pill: f32,
   red_pill: i64,
}

fn main() {
   let f = Morpheus { blue_pill: 0.0, red_pill: 0 };
   let copy = f.clone(); // and now we can clone it!
}
```

[Clone](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html "trait std::clone::Clone")

A common trait that allows explicit creation of a duplicate value.

[CloneToUninit](https://doc.rust-lang.org/stable/std/clone/trait.CloneToUninit.html "trait std::clone::CloneToUninit")Experimental

A generalization of [`Clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html "trait std::clone::Clone") to [dynamically-sized types](https://doc.rust-lang.org/reference/dynamically-sized-types.html) stored in arbitrary containers.

[TrivialClone](https://doc.rust-lang.org/stable/std/clone/trait.TrivialClone.html "trait std::clone::TrivialClone")Experimental

Indicates that the `Clone` implementation is identical to copying the value.

[UseCloned](https://doc.rust-lang.org/stable/std/clone/trait.UseCloned.html "trait std::clone::UseCloned")Experimental

Trait for objects whose [`Clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html "trait std::clone::Clone") impl is lightweight (e.g. reference-counted)

[Clone](https://doc.rust-lang.org/stable/std/clone/derive.Clone.html "derive std::clone::Clone")

Derive macro generating an impl of the trait `Clone`.