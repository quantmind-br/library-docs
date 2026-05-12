---
title: AsMut in std::convert - Rust
url: https://doc.rust-lang.org/stable/std/convert/trait.AsMut.html
source: crawler
fetched_at: 2026-05-06T21:25:35.153345055-03:00
rendered_js: false
word_count: 435
summary: The AsMut trait defines a contract for performing cheap, infallible mutable-to-mutable reference conversions between types in Rust.
tags:
    - rust
    - traits
    - type-conversion
    - mutable-reference
    - generic-programming
    - standard-library
category: reference
---

## Trait AsMut

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#372)

```rust
pub trait AsMut<T>
where
    T: ?Sized,{
    // Required method
    fn as_mut(&mut self) -> &mut T;
}
```

Expand description

Used to do a cheap mutable-to-mutable reference conversion.

This trait is similar to [`AsRef`](https://doc.rust-lang.org/stable/std/convert/trait.AsRef.html "trait std::convert::AsRef") but used for converting between mutable references. If you need to do a costly conversion it is better to implement [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") with type `&mut T` or write a custom function.

**Note: This trait must not fail**. If the conversion can fail, use a dedicated method which returns an [`Option<T>`](https://doc.rust-lang.org/stable/std/option/enum.Option.html "enum std::option::Option") or a [`Result<T, E>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result").

## [§](#generic-implementations)Generic Implementations

`AsMut` auto-dereferences if the inner type is a mutable reference (e.g.: `foo.as_mut()` will work the same if `foo` has type `&mut Foo` or `&mut &mut Foo`).

Note that due to historic reasons, the above currently does not hold generally for all [mutably dereferenceable types](https://doc.rust-lang.org/stable/std/ops/trait.DerefMut.html "trait std::ops::DerefMut"), e.g. `foo.as_mut()` will *not* work the same as `Box::new(foo).as_mut()`. Instead, many smart pointers provide an `as_mut` implementation which simply returns a reference to the [pointed-to value](https://doc.rust-lang.org/stable/std/ops/trait.Deref.html#associatedtype.Target "associated type std::ops::Deref::Target") (but do not perform a cheap reference-to-reference conversion for that value). However, [`AsMut::as_mut`](https://doc.rust-lang.org/stable/std/convert/trait.AsMut.html#tymethod.as_mut "method std::convert::AsMut::as_mut") should not be used for the sole purpose of mutable dereferencing; instead [‘`Deref` coercion’](https://doc.rust-lang.org/stable/std/ops/trait.DerefMut.html#mutable-deref-coercion "trait std::ops::DerefMut") can be used:

```rust
let mut x = Box::new(5i32);
// Avoid this:
// let y: &mut i32 = x.as_mut();
// Better just write:
let y: &mut i32 = &mut x;
```

Types which implement [`DerefMut`](https://doc.rust-lang.org/stable/std/ops/trait.DerefMut.html "trait std::ops::DerefMut") should consider to add an implementation of `AsMut<T>` as follows:

```rust
impl<T> AsMut<T> for SomeType
where
    <SomeType as Deref>::Target: AsMut<T>,
{
    fn as_mut(&mut self) -> &mut T {
        self.deref_mut().as_mut()
    }
}
```

## [§](#reflexivity)Reflexivity

Ideally, `AsMut` would be reflexive, i.e. there would be an `impl<T: ?Sized> AsMut<T> for T` with [`as_mut`](https://doc.rust-lang.org/stable/std/convert/trait.AsMut.html#tymethod.as_mut "method std::convert::AsMut::as_mut") simply returning its argument unchanged. Such a blanket implementation is currently *not* provided due to technical restrictions of Rust’s type system (it would be overlapping with another existing blanket implementation for `&mut T where T: AsMut<U>` which allows `AsMut` to auto-dereference, see “Generic Implementations” above).

A trivial implementation of `AsMut<T> for T` must be added explicitly for a particular type `T` where needed or desired. Note, however, that not all types from `std` contain such an implementation, and those cannot be added by external code due to orphan rules.

## [§](#examples)Examples

Using `AsMut` as trait bound for a generic function, we can accept all mutable references that can be converted to type `&mut T`. Unlike [dereference](https://doc.rust-lang.org/stable/std/ops/trait.DerefMut.html "trait std::ops::DerefMut"), which has a single [target type](https://doc.rust-lang.org/stable/std/ops/trait.Deref.html#associatedtype.Target "associated type std::ops::Deref::Target"), there can be multiple implementations of `AsMut` for a type. In particular, `Vec<T>` implements both `AsMut<Vec<T>>` and `AsMut<[T]>`.

In the following, the example functions `caesar` and `null_terminate` provide a generic interface which works with any type that can be converted by cheap mutable-to-mutable conversion into a byte slice (`[u8]`) or a byte vector (`Vec<u8>`), respectively.

```rust
struct Document {
    info: String,
    content: Vec<u8>,
}

impl<T: ?Sized> AsMut<T> for Document
where
    Vec<u8>: AsMut<T>,
{
    fn as_mut(&mut self) -> &mut T {
        self.content.as_mut()
    }
}

fn caesar<T: AsMut<[u8]>>(data: &mut T, key: u8) {
    for byte in data.as_mut() {
        *byte = byte.wrapping_add(key);
    }
}

fn null_terminate<T: AsMut<Vec<u8>>>(data: &mut T) {
    // Using a non-generic inner function, which contains most of the
    // functionality, helps to minimize monomorphization overhead.
    fn doit(data: &mut Vec<u8>) {
        let len = data.len();
        if len == 0 || data[len-1] != 0 {
            data.push(0);
        }
    }
    doit(data.as_mut());
}

fn main() {
    let mut v: Vec<u8> = vec![1, 2, 3];
    caesar(&mut v, 5);
    assert_eq!(v, [6, 7, 8]);
    null_terminate(&mut v);
    assert_eq!(v, [6, 7, 8, 0]);
    let mut doc = Document {
        info: String::from("Example"),
        content: vec![17, 19, 8],
    };
    caesar(&mut doc, 1);
    assert_eq!(doc.content, [18, 20, 9]);
    null_terminate(&mut doc);
    assert_eq!(doc.content, [18, 20, 9, 0]);
}
```

Note, however, that APIs don’t need to be generic. In many cases taking a `&mut [u8]` or `&mut Vec<u8>`, for example, is the better choice (callers need to pass the correct type then).

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#375)

Converts this type into a mutable reference of the (usually inferred) input type.