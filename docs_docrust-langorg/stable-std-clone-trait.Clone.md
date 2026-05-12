---
title: Clone in std::clone - Rust
url: https://doc.rust-lang.org/stable/std/clone/trait.Clone.html
source: crawler
fetched_at: 2026-05-06T21:25:30.688300777-03:00
rendered_js: false
word_count: 731
summary: The Clone trait in Rust provides a mechanism for explicit value duplication, offering a way to create a new instance of an object that may involve deep copies or reference sharing.
tags:
    - rust
    - trait
    - clone
    - memory-management
    - smart-pointers
    - language-features
category: reference
---

## Trait Clone

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#194)

```rust
pub trait Clone: Sized {
    // Required method
    fn clone(&self) -> Self;

    // Provided method
    fn clone_from(&mut self, source: &Self) { ... }
}
```

Expand description

A common trait that allows explicit creation of a duplicate value.

Calling [`clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") always produces a new value. However, for types that are references to other data (such as smart pointers or references), the new value may still point to the same underlying data, rather than duplicating it. See [`Clone::clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") for more details.

This distinction is especially important when using `#[derive(Clone)]` on structs containing smart pointers like `Arc<Mutex<T>>` - the cloned struct will share mutable state with the original.

Differs from [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy") in that [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy") is implicit and an inexpensive bit-wise copy, while `Clone` is always explicit and may or may not be expensive. [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy") has no methods, so you cannot change its behavior, but when implementing `Clone`, the `clone` method you provide may run arbitrary code.

Since `Clone` is a supertrait of [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy"), any type that implements `Copy` must also implement `Clone`.

### [§](#derivable)Derivable

This trait can be used with `#[derive]` if all fields are `Clone`. The `derive`d implementation of [`Clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") calls [`clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone") on each field.

For a generic struct, `#[derive]` implements `Clone` conditionally by adding bound `Clone` on generic parameters.

```rust
// `derive` implements Clone for Reading<T> when T is Clone.
#[derive(Clone)]
struct Reading<T> {
    frequency: T,
}
```

### [§](#how-can-i-implement-clone)How can I implement `Clone`?

Types that are [`Copy`](https://doc.rust-lang.org/stable/std/marker/trait.Copy.html "trait std::marker::Copy") should have a trivial implementation of `Clone`. More formally: if `T: Copy`, `x: T`, and `y: &T`, then `let x = y.clone();` is equivalent to `let x = *y;`. Manual implementations should be careful to uphold this invariant; however, unsafe code must not rely on it to ensure memory safety.

An example is a generic struct holding a function pointer. In this case, the implementation of `Clone` cannot be `derive`d, but can be implemented as:

```rust
struct Generate<T>(fn() -> T);

impl<T> Copy for Generate<T> {}

impl<T> Clone for Generate<T> {
    fn clone(&self) -> Self {
        *self
    }
}
```

If we `derive`:

```rust
#[derive(Copy, Clone)]
struct Generate<T>(fn() -> T);
```

the auto-derived implementations will have unnecessary `T: Copy` and `T: Clone` bounds:

```rust

// Automatically derived
impl<T: Copy> Copy for Generate<T> { }

// Automatically derived
impl<T: Clone> Clone for Generate<T> {
    fn clone(&self) -> Generate<T> {
        Generate(Clone::clone(&self.0))
    }
}
```

The bounds are unnecessary because clearly the function itself should be copy- and cloneable even if its return type is not:

[ⓘ](# "This example deliberately fails to compile")

```rust
#[derive(Copy, Clone)]
struct Generate<T>(fn() -> T);

struct NotCloneable;

fn generate_not_cloneable() -> NotCloneable {
    NotCloneable
}

Generate(generate_not_cloneable).clone(); // error: trait bounds were not satisfied
// Note: With the manual implementations the above line will compile.
```

### [§](#clone-and-partialeqeq)`Clone` and `PartialEq`/`Eq`

`Clone` is intended for the duplication of objects. Consequently, when implementing both `Clone` and [`PartialEq`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq"), the following property is expected to hold:

In other words, if an object compares equal to itself, its clone must also compare equal to the original.

For types that also implement [`Eq`](https://doc.rust-lang.org/stable/std/cmp/trait.Eq.html "trait std::cmp::Eq") – for which `x == x` always holds – this implies that `x.clone() == x` must always be true. Standard library collections such as [`HashMap`](https://doc.rust-lang.org/stable/std/collections/struct.HashMap.html), [`HashSet`](https://doc.rust-lang.org/stable/std/collections/struct.HashSet.html), [`BTreeMap`](https://doc.rust-lang.org/stable/std/collections/struct.BTreeMap.html), [`BTreeSet`](https://doc.rust-lang.org/stable/std/collections/struct.BTreeSet.html) and [`BinaryHeap`](https://doc.rust-lang.org/stable/std/collections/struct.BinaryHeap.html) rely on their keys respecting this property for correct behavior. Furthermore, these collections require that cloning a key preserves the outcome of the [`Hash`](https://doc.rust-lang.org/stable/std/hash/derive.Hash.html "derive std::hash::Hash") and [`Ord`](https://doc.rust-lang.org/stable/std/cmp/trait.Ord.html "trait std::cmp::Ord") methods. Thankfully, this follows automatically from `x.clone() == x` if `Hash` and `Ord` are correctly implemented according to their own requirements.

When deriving both `Clone` and [`PartialEq`](https://doc.rust-lang.org/stable/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") using `#[derive(Clone, PartialEq)]` or when additionally deriving [`Eq`](https://doc.rust-lang.org/stable/std/cmp/trait.Eq.html "trait std::cmp::Eq") using `#[derive(Clone, PartialEq, Eq)]`, then this property is automatically upheld – provided that it is satisfied by the underlying types.

Violating this property is a logic error. The behavior resulting from a logic error is not specified, but users of the trait must ensure that such logic errors do *not* result in undefined behavior. This means that `unsafe` code **must not** rely on this property being satisfied.

### [§](#additional-implementors)Additional implementors

In addition to the [implementors listed below](#implementors), the following types also implement `Clone`:

- Function item types (i.e., the distinct types defined for each function)
- Function pointer types (e.g., `fn() -> i32`)
- Closure types, if they capture no value from the environment or if all such captured values implement `Clone` themselves. Note that variables captured by shared reference always implement `Clone` (even if the referent doesn’t), while variables captured by mutable reference never implement `Clone`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#236)

Returns a duplicate of the value.

Note that what “duplicate” means varies by type:

- For most types, this creates a deep, independent copy
- For reference types like `&T`, this creates another reference to the same value
- For smart pointers like [`Arc`](https://doc.rust-lang.org/stable/std/sync/struct.Arc.html) or [`Rc`](https://doc.rust-lang.org/stable/std/rc/struct.Rc.html), this increments the reference count but still points to the same underlying data

##### [§](#examples)Examples

```rust
let hello = "Hello"; // &str implements Clone

assert_eq!("Hello", hello.clone());
```

Example with a reference-counted type:

```rust
use std::sync::{Arc, Mutex};

let data = Arc::new(Mutex::new(vec![1, 2, 3]));
let data_clone = data.clone(); // Creates another Arc pointing to the same Mutex

{
    let mut lock = data.lock().unwrap();
    lock.push(4);
}

// Changes are visible through the clone because they share the same underlying data
assert_eq!(*data_clone.lock().unwrap(), vec![1, 2, 3, 4]);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#245-247)

Performs copy-assignment from `source`.

`a.clone_from(&b)` is equivalent to `a = b.clone()` in functionality, but can be overridden to reuse the resources of `a` to avoid unnecessary allocations.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*