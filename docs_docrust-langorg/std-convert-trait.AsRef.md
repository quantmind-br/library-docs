---
title: AsRef in std::convert - Rust
url: https://doc.rust-lang.org/std/convert/trait.AsRef.html#tymethod.as_ref
source: crawler
fetched_at: 2026-05-06T21:23:06.144696217-03:00
rendered_js: false
word_count: 465
summary: This document defines the AsRef trait in Rust, which is used for performing cheap, infallible reference-to-reference conversions. It explains the trait's purpose, its differences from the Borrow trait, and how it enables generic interfaces.
tags:
    - rust
    - traits
    - type-conversion
    - memory-management
    - generic-programming
category: reference
---

## Trait AsRef

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#220)

```rust
pub trait AsRef<T>
where
    T: ?Sized,{
    // Required method
    fn as_ref(&self) -> &T;
}
```

Expand description

Used to do a cheap reference-to-reference conversion.

This trait is similar to [`AsMut`](https://doc.rust-lang.org/std/convert/trait.AsMut.html "trait std::convert::AsMut") which is used for converting between mutable references. If you need to do a costly conversion it is better to implement [`From`](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From") with type `&T` or write a custom function.

## [§](#relation-to-borrow)Relation to `Borrow`

`AsRef` has the same signature as [`Borrow`](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow"), but [`Borrow`](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow") is different in a few aspects:

- Unlike `AsRef`, [`Borrow`](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow") has a blanket impl for any `T`, and can be used to accept either a reference or a value. (See also note on `AsRef`’s reflexibility below.)
- [`Borrow`](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow") also requires that [`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html "trait std::hash::Hash"), [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq") and [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") for a borrowed value are equivalent to those of the owned value. For this reason, if you want to borrow only a single field of a struct you can implement `AsRef`, but not [`Borrow`](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow").

**Note: This trait must not fail**. If the conversion can fail, use a dedicated method which returns an [`Option<T>`](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option") or a [`Result<T, E>`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result").

## [§](#generic-implementations)Generic Implementations

`AsRef` auto-dereferences if the inner type is a reference or a mutable reference (e.g.: `foo.as_ref()` will work the same if `foo` has type `&mut Foo` or `&&mut Foo`).

Note that due to historic reasons, the above currently does not hold generally for all [dereferenceable types](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref"), e.g. `foo.as_ref()` will *not* work the same as `Box::new(foo).as_ref()`. Instead, many smart pointers provide an `as_ref` implementation which simply returns a reference to the [pointed-to value](https://doc.rust-lang.org/std/ops/trait.Deref.html#associatedtype.Target "associated type std::ops::Deref::Target") (but do not perform a cheap reference-to-reference conversion for that value). However, [`AsRef::as_ref`](https://doc.rust-lang.org/std/convert/trait.AsRef.html#tymethod.as_ref "method std::convert::AsRef::as_ref") should not be used for the sole purpose of dereferencing; instead [‘`Deref` coercion’](https://doc.rust-lang.org/std/ops/trait.Deref.html#deref-coercion "trait std::ops::Deref") can be used:

```rust
let x = Box::new(5i32);
// Avoid this:
// let y: &i32 = x.as_ref();
// Better just write:
let y: &i32 = &x;
```

Types which implement [`Deref`](https://doc.rust-lang.org/std/ops/trait.Deref.html "trait std::ops::Deref") should consider implementing `AsRef<T>` as follows:

```rust
impl<T> AsRef<T> for SomeType
where
    T: ?Sized,
    <SomeType as Deref>::Target: AsRef<T>,
{
    fn as_ref(&self) -> &T {
        self.deref().as_ref()
    }
}
```

## [§](#reflexivity)Reflexivity

Ideally, `AsRef` would be reflexive, i.e. there would be an `impl<T: ?Sized> AsRef<T> for T` with [`as_ref`](https://doc.rust-lang.org/std/convert/trait.AsRef.html#tymethod.as_ref "method std::convert::AsRef::as_ref") simply returning its argument unchanged. Such a blanket implementation is currently *not* provided due to technical restrictions of Rust’s type system (it would be overlapping with another existing blanket implementation for `&T where T: AsRef<U>` which allows `AsRef` to auto-dereference, see “Generic Implementations” above).

A trivial implementation of `AsRef<T> for T` must be added explicitly for a particular type `T` where needed or desired. Note, however, that not all types from `std` contain such an implementation, and those cannot be added by external code due to orphan rules.

## [§](#examples)Examples

By using trait bounds we can accept arguments of different types as long as they can be converted to the specified type `T`.

For example: By creating a generic function that takes an `AsRef<str>` we express that we want to accept all references that can be converted to [`&str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") as an argument. Since both [`String`](https://doc.rust-lang.org/std/string/struct.String.html) and [`&str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") implement `AsRef<str>` we can accept both as input argument.

```rust
fn is_hello<T: AsRef<str>>(s: T) {
   assert_eq!("hello", s.as_ref());
}

let s = "hello";
is_hello(s);

let s = "hello".to_string();
is_hello(s);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#223)

Converts this type into a shared reference of the (usually inferred) input type.