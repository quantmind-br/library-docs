---
title: DerefMut in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.DerefMut.html
source: crawler
fetched_at: 2026-05-06T21:23:16.988228859-03:00
rendered_js: false
word_count: 371
summary: This document defines the Rust DerefMut trait, which enables mutable dereferencing operations and facilitates implicit mutable deref coercion for smart pointer types.
tags:
    - rust
    - traits
    - derefmut
    - memory-management
    - smart-pointers
    - type-coercion
category: reference
---

## Trait DerefMut

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/ops/deref.rs.html#270)

```rust
pub trait DerefMut: Deref {
    // Required method
    fn deref_mut(&mut self) -> &mut Self::Target;
}
```

Expand description

Used for mutable dereferencing operations, like in `*v = 1;`.

In addition to being used for explicit dereferencing operations with the (unary) `*` operator in mutable contexts, `DerefMut` is also used implicitly by the compiler in many circumstances. This mechanism is called [“mutable deref coercion”](#mutable-deref-coercion). In immutable contexts, [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref") is used.

**Warning:** Deref coercion is a powerful language feature which has far-reaching implications for every type that implements `DerefMut`. The compiler will silently insert calls to `DerefMut::deref_mut`. For this reason, one should be careful about implementing `DerefMut` and only do so when mutable deref coercion is desirable. See [the `Deref` docs](https://doc.rust-lang.org/std/ops/trait.Deref.html#when-to-implement-deref-or-derefmut "trait std::ops::Deref") for advice on when this is typically desirable or undesirable.

Types that implement `DerefMut` or `Deref` are often called “smart pointers” and the mechanism of deref coercion has been specifically designed to facilitate the pointer-like behavior that name suggests. Often, the purpose of a “smart pointer” type is to change the ownership semantics of a contained value (for example, [`Rc`](https://doc.rust-lang.org/alloc/rc/struct.Rc.html) or [`Cow`](https://doc.rust-lang.org/alloc/borrow/enum.Cow.html)) or the storage semantics of a contained value (for example, [`Box`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html)).

## [§](#mutable-deref-coercion)Mutable deref coercion

If `T` implements `DerefMut<Target = U>`, and `v` is a value of type `T`, then:

- In mutable contexts, `*v` (where `T` is neither a reference nor a raw pointer) is equivalent to `*DerefMut::deref_mut(&mut v)`.
- Values of type `&mut T` are coerced to values of type `&mut U`
- `T` implicitly implements all the (mutable) methods of the type `U`.

For more details, visit [the chapter in *The Rust Programming Language*](https://doc.rust-lang.org/book/ch15-02-deref.html) as well as the reference sections on [the dereference operator](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator), [method resolution](https://doc.rust-lang.org/reference/expressions/method-call-expr.html) and [type coercions](https://doc.rust-lang.org/reference/type-coercions.html).

## [§](#fallibility)Fallibility

**This trait’s method should never unexpectedly fail**. Deref coercion means the compiler will often insert calls to `DerefMut::deref_mut` implicitly. Failure during dereferencing can be extremely confusing when `DerefMut` is invoked implicitly. In the majority of uses it should be infallible, though it may be acceptable to panic if the type is misused through programmer error, for example.

However, infallibility is not enforced and therefore not guaranteed. As such, `unsafe` code should not rely on infallibility in general for soundness.

## [§](#examples)Examples

A struct with a single field which is modifiable by dereferencing the struct.

```rust
use std::ops::{Deref, DerefMut};

struct DerefMutExample<T> {
    value: T
}

impl<T> Deref for DerefMutExample<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.value
    }
}

impl<T> DerefMut for DerefMutExample<T> {
    fn deref_mut(&mut self) -> &mut Self::Target {
        &mut self.value
    }
}

let mut x = DerefMutExample { value: 'a' };
*x = 'b';
assert_eq!('b', x.value);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/deref.rs.html#274)

Mutably dereferences the value.