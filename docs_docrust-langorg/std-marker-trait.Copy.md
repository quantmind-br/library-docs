---
title: Copy in std::marker - Rust
url: https://doc.rust-lang.org/std/marker/trait.Copy.html
source: crawler
fetched_at: 2026-05-06T21:24:39.984694058-03:00
rendered_js: false
word_count: 744
summary: This document explains the Copy trait in Rust, which allows for bit-wise duplication of types, and details how it differs from Clone and the requirements for implementing it.
tags:
    - rust
    - copy-trait
    - move-semantics
    - memory-safety
    - trait-implementation
    - clone-trait
category: concept
---

## Trait Copy

1.0.0 · [Source](https://doc.rust-lang.org/src/core/marker.rs.html#457)

```rust
pub trait Copy: Clone { }
```

Expand description

Types whose values can be duplicated simply by copying bits.

By default, variable bindings have ‘move semantics.’ In other words:

```rust
#[derive(Debug)]
struct Foo;

let x = Foo;

let y = x;

// `x` has moved into `y`, and so cannot be used

// println!("{x:?}"); // error: use of moved value
```

However, if a type implements `Copy`, it instead has ‘copy semantics’:

```rust
// We can derive a `Copy` implementation. `Clone` is also required, as it's
// a supertrait of `Copy`.
#[derive(Debug, Copy, Clone)]
struct Foo;

let x = Foo;

let y = x;

// `y` is a copy of `x`

println!("{x:?}"); // A-OK!
```

It’s important to note that in these two examples, the only difference is whether you are allowed to access `x` after the assignment. Under the hood, both a copy and a move can result in bits being copied in memory, although this is sometimes optimized away.

### [§](#how-can-i-implement-copy)How can I implement `Copy`?

There are two ways to implement `Copy` on your type. The simplest is to use `derive`:

```rust
#[derive(Copy, Clone)]
struct MyStruct;
```

You can also implement `Copy` and `Clone` manually:

```rust
struct MyStruct;

impl Copy for MyStruct { }

impl Clone for MyStruct {
    fn clone(&self) -> MyStruct {
        *self
    }
}
```

There is a small difference between the two. The `derive` strategy will also place a `Copy` bound on type parameters:

```rust
#[derive(Clone)]
struct MyStruct<T>(T);

impl<T: Copy> Copy for MyStruct<T> { }
```

This isn’t always desired. For example, shared references (`&T`) can be copied regardless of whether `T` is `Copy`. Likewise, a generic struct containing markers such as [`PhantomData`](https://doc.rust-lang.org/std/marker/struct.PhantomData.html "struct std::marker::PhantomData") could potentially be duplicated with a bit-wise copy.

### [§](#whats-the-difference-between-copy-and-clone)What’s the difference between `Copy` and `Clone`?

Copies happen implicitly, for example as part of an assignment `y = x`. The behavior of `Copy` is not overloadable; it is always a simple bit-wise copy.

Cloning is an explicit action, `x.clone()`. The implementation of [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") can provide any type-specific behavior necessary to duplicate values safely. For example, the implementation of [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") for [`String`](https://doc.rust-lang.org/std/string/struct.String.html) needs to copy the pointed-to string buffer in the heap. A simple bitwise copy of [`String`](https://doc.rust-lang.org/std/string/struct.String.html) values would merely copy the pointer, leading to a double free down the line. For this reason, [`String`](https://doc.rust-lang.org/std/string/struct.String.html) is [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") but not `Copy`.

[`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") is a supertrait of `Copy`, so everything which is `Copy` must also implement [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone"). If a type is `Copy` then its [`Clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") implementation only needs to return `*self` (see the example above).

### [§](#when-can-my-type-be-copy)When can my type be `Copy`?

A type can implement `Copy` if all of its components implement `Copy`. For example, this struct can be `Copy`:

```rust
#[derive(Copy, Clone)]
struct Point {
   x: i32,
   y: i32,
}
```

A struct can be `Copy`, and [`i32`](https://doc.rust-lang.org/std/primitive.i32.html "primitive i32") is `Copy`, therefore `Point` is eligible to be `Copy`. By contrast, consider

```rust
struct PointList {
    points: Vec<Point>,
}
```

The struct `PointList` cannot implement `Copy`, because [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html) is not `Copy`. If we attempt to derive a `Copy` implementation, we’ll get an error:

```text
the trait `Copy` cannot be implemented for this type; field `points` does not implement `Copy`
```

Shared references (`&T`) are also `Copy`, so a type can be `Copy`, even when it holds shared references of types `T` that are *not* `Copy`. Consider the following struct, which can implement `Copy`, because it only holds a *shared reference* to our non-`Copy` type `PointList` from above:

```rust
#[derive(Copy, Clone)]
struct PointListWrapper<'a> {
    point_list_ref: &'a PointList,
}
```

### [§](#when-cant-my-type-be-copy)When *can’t* my type be `Copy`?

Some types can’t be copied safely. For example, copying `&mut T` would create an aliased mutable reference. Copying [`String`](https://doc.rust-lang.org/std/string/struct.String.html) would duplicate responsibility for managing the [`String`](https://doc.rust-lang.org/std/string/struct.String.html)’s buffer, leading to a double free.

Generalizing the latter case, any type implementing [`Drop`](https://doc.rust-lang.org/std/ops/trait.Drop.html "trait std::ops::Drop") can’t be `Copy`, because it’s managing some resource besides its own [`size_of::<T>`](https://doc.rust-lang.org/std/mem/fn.size_of.html "fn std::mem::size_of") bytes.

If you try to implement `Copy` on a struct or enum containing non-`Copy` data, you will get the error [E0204](https://doc.rust-lang.org/error_codes/E0204.html).

### [§](#when-should-my-type-be-copy)When *should* my type be `Copy`?

Generally speaking, if your type *can* implement `Copy`, it should. Keep in mind, though, that implementing `Copy` is part of the public API of your type. If the type might become non-`Copy` in the future, it could be prudent to omit the `Copy` implementation now, to avoid a breaking API change.

### [§](#additional-implementors)Additional implementors

In addition to the [implementors listed below](#implementors), the following types also implement `Copy`:

- Function item types (i.e., the distinct types defined for each function)
- Function pointer types (e.g., `fn() -> i32`)
- Closure types, if they capture no value from the environment or if all such captured values implement `Copy` themselves. Note that variables captured by shared reference always implement `Copy` (even if the referent doesn’t), while variables captured by mutable reference never implement `Copy`.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*