---
title: CloneFromCell in std::cell - Rust
url: https://doc.rust-lang.org/stable/std/cell/trait.CloneFromCell.html
source: crawler
fetched_at: 2026-05-06T21:26:21.731101543-03:00
rendered_js: false
word_count: 110
summary: Defines an unsafe trait for types that support sound cloning from a Cell container, ensuring safe interior mutability patterns.
tags:
    - rust-lang
    - memory-safety
    - cell-api
    - unsafe-rust
    - trait-definition
category: reference
---

## Trait CloneFromCell

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#799)

```rust
pub unsafe trait CloneFromCell: Clone { }
```

🔬This is a nightly-only experimental API. (`cell_get_cloned` [#145329](https://github.com/rust-lang/rust/issues/145329))

Expand description

Types for which cloning `Cell<Self>` is sound.

## [§](#safety)Safety

Implementing this trait for a type is sound if and only if the following code is sound for T = that type.

```rust
#![feature(cell_get_cloned)]
fn clone_from_cell<T: CloneFromCell>(cell: &Cell<T>) -> T {
    unsafe { T::clone(&*cell.as_ptr()) }
}
```

Importantly, you can’t just implement `CloneFromCell` for any arbitrary `Copy` type, e.g. the following is unsound:

```rust

#[derive(Copy, Debug)]
pub struct Bad<'a>(Option<&'a Cell<Bad<'a>>>, u8);

impl Clone for Bad<'_> {
    fn clone(&self) -> Self {
        let a: &u8 = &self.1;
        // when self.0 points to self, we write to self.1 while we have a live `&u8` pointing to
        // it -- this is UB
        self.0.unwrap().set(Self(None, 1));
        dbg!((a, self));
        Self(None, 0)
    }
}

// this is not sound
// unsafe impl CloneFromCell for Bad<'_> {}
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*