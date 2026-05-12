---
title: BorrowMut in std::borrow - Rust
url: https://doc.rust-lang.org/stable/std/borrow/trait.BorrowMut.html#tymethod.borrow_mut
source: crawler
fetched_at: 2026-05-06T21:26:24.965476338-03:00
rendered_js: false
word_count: 56
summary: This document defines the BorrowMut trait in Rust, which allows types to be mutably borrowed as an underlying type.
tags:
    - rust
    - trait
    - borrowing
    - memory-management
    - mutable-reference
category: reference
---

## Trait BorrowMut

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#190)

```rust
pub trait BorrowMut<Borrowed>: Borrow<Borrowed>where
    Borrowed: ?Sized,{
    // Required method
    fn borrow_mut(&mut self) -> &mut Borrowed;
}
```

Expand description

A trait for mutably borrowing data.

As a companion to [`Borrow<T>`](https://doc.rust-lang.org/stable/std/borrow/trait.Borrow.html "trait std::borrow::Borrow") this trait allows a type to borrow as an underlying type by providing a mutable reference. See [`Borrow<T>`](https://doc.rust-lang.org/stable/std/borrow/trait.Borrow.html "trait std::borrow::Borrow") for more information on borrowing as another type.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#207)

Mutably borrows from an owned value.

##### [§](#examples)Examples

```rust
use std::borrow::BorrowMut;

fn check<T: BorrowMut<[i32]>>(mut v: T) {
    assert_eq!(&mut [1, 2, 3], v.borrow_mut());
}

let v = vec![1, 2, 3];

check(v);
```