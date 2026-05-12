---
title: IndexMut in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.IndexMut.html
source: crawler
fetched_at: 2026-05-06T21:22:32.1841756-03:00
rendered_js: false
word_count: 174
summary: The IndexMut trait provides a mechanism for performing mutable indexing operations on custom types using the square bracket syntax.
tags:
    - rust
    - traits
    - indexing
    - mutable-access
    - operator-overloading
category: reference
---

## Trait IndexMut

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/ops/index.rs.html#170)

```rust
pub trait IndexMut<Idx>: Index<Idx>
where
    Idx: ?Sized,{
    // Required method
    fn index_mut(&mut self, index: Idx) -> &mut Self::Output;
}
```

Expand description

Used for indexing operations (`container[index]`) in mutable contexts.

`container[index]` is actually syntactic sugar for `*container.index_mut(index)`, but only when used as a mutable value. If an immutable value is requested, the [`Index`](https://doc.rust-lang.org/std/ops/trait.Index.html "trait std::ops::Index") trait is used instead. This allows nice things such as `v[index] = value`.

## [§](#examples)Examples

A very simple implementation of a `Balance` struct that has two sides, where each can be indexed mutably and immutably.

```rust
use std::ops::{Index, IndexMut};

#[derive(Debug)]
enum Side {
    Left,
    Right,
}

#[derive(Debug, PartialEq)]
enum Weight {
    Kilogram(f32),
    Pound(f32),
}

struct Balance {
    pub left: Weight,
    pub right: Weight,
}

impl Index<Side> for Balance {
    type Output = Weight;

    fn index(&self, index: Side) -> &Self::Output {
        println!("Accessing {index:?}-side of balance immutably");
        match index {
            Side::Left => &self.left,
            Side::Right => &self.right,
        }
    }
}

impl IndexMut<Side> for Balance {
    fn index_mut(&mut self, index: Side) -> &mut Self::Output {
        println!("Accessing {index:?}-side of balance mutably");
        match index {
            Side::Left => &mut self.left,
            Side::Right => &mut self.right,
        }
    }
}

let mut balance = Balance {
    right: Weight::Kilogram(2.5),
    left: Weight::Pound(1.5),
};

// In this case, `balance[Side::Right]` is sugar for
// `*balance.index(Side::Right)`, since we are only *reading*
// `balance[Side::Right]`, not writing it.
assert_eq!(balance[Side::Right], Weight::Kilogram(2.5));

// However, in this case `balance[Side::Left]` is sugar for
// `*balance.index_mut(Side::Left)`, since we are writing
// `balance[Side::Left]`.
balance[Side::Left] = Weight::Kilogram(3.0);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/index.rs.html#179)

Performs the mutable indexing (`container[index]`) operation.

##### [§](#panics)Panics

May panic if the index is out of bounds.