---
title: Deref in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Deref.html
source: crawler
fetched_at: 2026-05-06T21:22:08.104905845-03:00
rendered_js: false
word_count: 723
summary: This document explains the Rust Deref trait, which enables custom immutable dereferencing behavior and powers the compiler's deref coercion mechanism for smart pointers.
tags:
    - rust
    - traits
    - deref
    - smart-pointers
    - deref-coercion
    - memory-management
category: reference
---

## Trait Deref

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/ops/deref.rs.html#139)

```rust
pub trait Deref {
    type Target: ?Sized;

    // Required method
    fn deref(&self) -> &Self::Target;
}
```

Expand description

Used for immutable dereferencing operations, like `*v`.

In addition to being used for explicit dereferencing operations with the (unary) `*` operator in immutable contexts, `Deref` is also used implicitly by the compiler in many circumstances. This mechanism is called [“`Deref` coercion”](#deref-coercion). In mutable contexts, [`DerefMut`](https://doc.rust-lang.org/std/ops/trait.DerefMut.html "trait std::ops::DerefMut") is used and mutable deref coercion similarly occurs.

**Warning:** Deref coercion is a powerful language feature which has far-reaching implications for every type that implements `Deref`. The compiler will silently insert calls to `Deref::deref`. For this reason, one should be careful about implementing `Deref` and only do so when deref coercion is desirable. See [below](#when-to-implement-deref-or-derefmut) for advice on when this is typically desirable or undesirable.

Types that implement `Deref` or `DerefMut` are often called “smart pointers” and the mechanism of deref coercion has been specifically designed to facilitate the pointer-like behavior that name suggests. Often, the purpose of a “smart pointer” type is to change the ownership semantics of a contained value (for example, [`Rc`](https://doc.rust-lang.org/alloc/rc/struct.Rc.html) or [`Cow`](https://doc.rust-lang.org/alloc/borrow/enum.Cow.html)) or the storage semantics of a contained value (for example, [`Box`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html)).

## [§](#deref-coercion)Deref coercion

If `T` implements `Deref<Target = U>`, and `v` is a value of type `T`, then:

- In immutable contexts, `*v` (where `T` is neither a reference nor a raw pointer) is equivalent to `*Deref::deref(&v)`.
- Values of type `&T` are coerced to values of type `&U`
- `T` implicitly implements all the methods of the type `U` which take the `&self` receiver.

For more details, visit [the chapter in *The Rust Programming Language*](https://doc.rust-lang.org/book/ch15-02-deref.html) as well as the reference sections on [the dereference operator](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator), [method resolution](https://doc.rust-lang.org/reference/expressions/method-call-expr.html), and [type coercions](https://doc.rust-lang.org/reference/type-coercions.html).

## [§](#when-to-implement-deref-or-derefmut)When to implement `Deref` or `DerefMut`

The same advice applies to both deref traits. In general, deref traits **should** be implemented if:

1. a value of the type transparently behaves like a value of the target type;
2. the implementation of the deref function is cheap; and
3. users of the type will not be surprised by any deref coercion behavior.

In general, deref traits **should not** be implemented if:

1. the deref implementations could fail unexpectedly; or
2. the type has methods that are likely to collide with methods on the target type; or
3. committing to deref coercion as part of the public API is not desirable.

Note that there’s a large difference between implementing deref traits generically over many target types, and doing so only for specific target types.

Generic implementations, such as for [`Box<T>`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html) (which is generic over every type and dereferences to `T`) should be careful to provide few or no methods, since the target type is unknown and therefore every method could collide with one on the target type, causing confusion for users. `impl<T> Box<T>` has no methods (though several associated functions), partly for this reason.

Specific implementations, such as for [`String`](https://doc.rust-lang.org/alloc/string/struct.String.html) (whose `Deref` implementation has `Target = str`) can have many methods, since avoiding collision is much easier. `String` and `str` both have many methods, and `String` additionally behaves as if it has every method of `str` because of deref coercion. The implementing type may also be generic while the implementation is still specific in this sense; for example, [`Vec<T>`](https://doc.rust-lang.org/alloc/vec/struct.Vec.html) dereferences to `[T]`, so methods of `T` are not applicable.

Consider also that deref coercion means that deref traits are a much larger part of a type’s public API than any other trait as it is implicitly called by the compiler. Therefore, it is advisable to consider whether this is something you are comfortable supporting as a public API.

The [`AsRef`](https://doc.rust-lang.org/std/convert/trait.AsRef.html "trait std::convert::AsRef") and [`Borrow`](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow") traits have very similar signatures to `Deref`. It may be desirable to implement either or both of these, whether in addition to or rather than deref traits. See their documentation for details.

## [§](#fallibility)Fallibility

**This trait’s method should never unexpectedly fail**. Deref coercion means the compiler will often insert calls to `Deref::deref` implicitly. Failure during dereferencing can be extremely confusing when `Deref` is invoked implicitly. In the majority of uses it should be infallible, though it may be acceptable to panic if the type is misused through programmer error, for example.

However, infallibility is not enforced and therefore not guaranteed. As such, `unsafe` code should not rely on infallibility in general for soundness.

## [§](#examples)Examples

A struct with a single field which is accessible by dereferencing the struct.

```rust
use std::ops::Deref;

struct DerefExample<T> {
    value: T
}

impl<T> Deref for DerefExample<T> {
    type Target = T;

    fn deref(&self) -> &Self::Target {
        &self.value
    }
}

let x = DerefExample { value: 'a' };
assert_eq!('a', *x);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/deref.rs.html#144)

The resulting type after dereferencing.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/deref.rs.html#150)

Dereferences the value.