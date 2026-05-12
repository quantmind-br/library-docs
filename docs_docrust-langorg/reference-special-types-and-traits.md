---
title: Special types and traits - The Rust Reference
url: https://doc.rust-lang.org/reference/special-types-and-traits.html#arct
source: crawler
fetched_at: 2026-05-06T21:36:04.908992612-03:00
rendered_js: false
word_count: 881
summary: This document outlines special types and traits in the Rust standard library that are recognized by the compiler and possess unique behaviors. It details key features such as operator overloading, thread safety traits, and auto traits like Send and Sync.
tags:
    - rust
    - programming-language
    - standard-library
    - traits
    - compiler-behavior
    - memory-management
    - concurrency
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Special types and traits](#special-types-and-traits)

Certain types and traits that exist in [the standard library](https://doc.rust-lang.org/std/index.html) are known to the Rust compiler. This chapter documents the special features of these types and traits.

## [`Box<T>`](#boxt)

[`Box<T>`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html) has a few special features that Rust doesn’t currently allow for user defined types.

- The [dereference operator](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator) for `Box<T>` produces a place which can be moved from. This means that the `*` operator and the destructor of `Box<T>` are built-in to the language.

<!--THE END-->

- [Methods](https://doc.rust-lang.org/reference/items/associated-items.html#associated-functions-and-methods) can take `Box<Self>` as a receiver.

<!--THE END-->

- A trait may be implemented for `Box<T>` in the same crate as `T`, which the [orphan rules](https://doc.rust-lang.org/reference/items/implementations.html#trait-implementation-coherence) prevent for other generic types.

## [`Rc<T>`](#rct)

[Methods](https://doc.rust-lang.org/reference/items/associated-items.html#associated-functions-and-methods) can take [`Rc<Self>`](https://doc.rust-lang.org/alloc/rc/struct.Rc.html) as a receiver.

## [`Arc<T>`](#arct)

[Methods](https://doc.rust-lang.org/reference/items/associated-items.html#associated-functions-and-methods) can take [`Arc<Self>`](https://doc.rust-lang.org/alloc/sync/struct.Arc.html) as a receiver.

## [`Pin<P>`](#pinp)

[Methods](https://doc.rust-lang.org/reference/items/associated-items.html#associated-functions-and-methods) can take [`Pin<P>`](https://doc.rust-lang.org/core/pin/struct.Pin.html) as a receiver.

## [`UnsafeCell<T>`](#unsafecellt)

[`std::cell::UnsafeCell<T>`](https://doc.rust-lang.org/core/cell/struct.UnsafeCell.html) is used for [interior mutability](https://doc.rust-lang.org/reference/interior-mutability.html). It ensures that the compiler doesn’t perform optimisations that are incorrect for such types.

It also ensures that [`static` items](https://doc.rust-lang.org/reference/items/static-items.html) which have a type with interior mutability aren’t placed in memory marked as read only.

## [`PhantomData<T>`](#phantomdatat)

[`std::marker::PhantomData<T>`](https://doc.rust-lang.org/core/marker/struct.PhantomData.html) is a zero-sized, minimum alignment, type that is considered to own a `T` for the purposes of [variance](https://doc.rust-lang.org/reference/subtyping.html#variance), [drop check](https://doc.rust-lang.org/nomicon/dropck.html), and [auto traits](#auto-traits).

## [Operator traits](#operator-traits)

The traits in [`std::ops`](https://doc.rust-lang.org/core/ops/index.html) and [`std::cmp`](https://doc.rust-lang.org/core/cmp/index.html) are used to overload [operators](https://doc.rust-lang.org/reference/expressions/operator-expr.html), [indexing expressions](https://doc.rust-lang.org/reference/expressions/array-expr.html#array-and-slice-indexing-expressions), and [call expressions](https://doc.rust-lang.org/reference/expressions/call-expr.html).

## [`Deref` and `DerefMut`](#deref-and-derefmut)

As well as overloading the unary `*` operator, [`Deref`](https://doc.rust-lang.org/core/ops/deref/trait.Deref.html) and [`DerefMut`](https://doc.rust-lang.org/core/ops/deref/trait.DerefMut.html) are also used in [method resolution](https://doc.rust-lang.org/reference/expressions/method-call-expr.html) and [deref coercions](https://doc.rust-lang.org/reference/type-coercions.html#coercion-types).

## [`Drop`](#drop)

The [`Drop`](https://doc.rust-lang.org/core/ops/drop/trait.Drop.html) trait provides a [destructor](https://doc.rust-lang.org/reference/destructors.html), to be run whenever a value of this type is to be destroyed.

## [`Copy`](#copy)

The [`Copy`](https://doc.rust-lang.org/core/marker/trait.Copy.html) trait changes the semantics of a type implementing it.

Values whose type implements `Copy` are copied rather than moved upon assignment.

`Copy` can only be implemented for types which do not implement `Drop`, and whose fields are all `Copy`. For enums, this means all fields of all variants have to be `Copy`. For unions, this means all variants have to be `Copy`.

`Copy` is implemented by the compiler for

- [Tuples](https://doc.rust-lang.org/reference/types/tuple.html) of `Copy` types

<!--THE END-->

- [Function pointers](https://doc.rust-lang.org/reference/types/function-pointer.html)

<!--THE END-->

- [Function items](https://doc.rust-lang.org/reference/types/function-item.html)

<!--THE END-->

- [Closures](https://doc.rust-lang.org/reference/types/closure.html) that capture no values or that only capture values of `Copy` types

## [`Clone`](#clone)

The [`Clone`](https://doc.rust-lang.org/core/clone/trait.Clone.html) trait is a supertrait of `Copy`, so it also needs compiler generated implementations.

It is implemented by the compiler for the following types:

- Types with a built-in `Copy` implementation (see above)

<!--THE END-->

- [Tuples](https://doc.rust-lang.org/reference/types/tuple.html) of `Clone` types

<!--THE END-->

- [Closures](https://doc.rust-lang.org/reference/types/closure.html) that only capture values of `Clone` types or capture no values from the environment

## [`Send`](#send)

The [`Send`](https://doc.rust-lang.org/core/marker/trait.Send.html) trait indicates that a value of this type is safe to send from one thread to another.

## [`Sync`](#sync)

The [`Sync`](https://doc.rust-lang.org/core/marker/trait.Sync.html) trait indicates that a value of this type is safe to share between multiple threads.

This trait must be implemented for all types used in immutable [`static` items](https://doc.rust-lang.org/reference/items/static-items.html).

## [`Termination`](#termination)

The [`Termination`](https://doc.rust-lang.org/std/process/trait.Termination.html) trait indicates the acceptable return types for the [main function](https://doc.rust-lang.org/reference/crates-and-source-files.html#main-functions) and [test functions](https://doc.rust-lang.org/reference/attributes/testing.html#the-test-attribute).

## [Auto traits](#auto-traits)

The [`Send`](https://doc.rust-lang.org/core/marker/trait.Send.html), [`Sync`](https://doc.rust-lang.org/core/marker/trait.Sync.html), [`Unpin`](https://doc.rust-lang.org/core/marker/trait.Unpin.html), [`UnwindSafe`](https://doc.rust-lang.org/core/panic/unwind_safe/trait.UnwindSafe.html), and [`RefUnwindSafe`](https://doc.rust-lang.org/core/panic/unwind_safe/trait.RefUnwindSafe.html) traits are *auto traits*. Auto traits have special properties.

If no explicit implementation or negative implementation is written out for an auto trait for a given type, then the compiler implements it automatically according to the following rules:

- `&T`, `&mut T`, `*const T`, `*mut T`, `[T; n]`, and `[T]` implement the trait if `T` does.

<!--THE END-->

- Function item types and function pointers automatically implement the trait.

<!--THE END-->

- Structs, enums, unions, and tuples implement the trait if all of their fields do.

<!--THE END-->

- Closures implement the trait if the types of all of their captures do. A closure that captures a `T` by shared reference and a `U` by value implements any auto traits that both `&T` and `U` do.

For generic types (counting the built-in types above as generic over `T`), if a generic implementation is available, then the compiler does not automatically implement it for types that could use the implementation except that they do not meet the requisite trait bounds. For instance, the standard library implements `Send` for all `&T` where `T` is `Sync`; this means that the compiler will not implement `Send` for `&T` if `T` is `Send` but not `Sync`.

Auto traits can also have negative implementations, shown as `impl !AutoTrait for T` in the standard library documentation, that override the automatic implementations. For example `*mut T` has a negative implementation of `Send`, and so `*mut T` is not `Send`, even if `T` is. There is currently no stable way to specify additional negative implementations; they exist only in the standard library.

Auto traits may be added as an additional bound to any [trait object](https://doc.rust-lang.org/reference/types/trait-object.html), even though normally only one trait is allowed. For instance, `Box<dyn Debug + Send + UnwindSafe>` is a valid type.

## [`Sized`](#sized)

The [`Sized`](https://doc.rust-lang.org/core/marker/trait.Sized.html) trait indicates that the size of this type is known at compile-time; that is, it’s not a [dynamically sized type](https://doc.rust-lang.org/reference/dynamically-sized-types.html).

[Type parameters](https://doc.rust-lang.org/reference/types/parameters.html) (except `Self` in traits) are `Sized` by default, as are [associated types](https://doc.rust-lang.org/reference/items/associated-items.html#associated-types).

`Sized` is always implemented automatically by the compiler, not by [implementation items](https://doc.rust-lang.org/reference/items/implementations.html).

These implicit `Sized` bounds may be relaxed by using the special `?Sized` bound.