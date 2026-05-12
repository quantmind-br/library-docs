---
title: Into in std::convert - Rust
url: https://doc.rust-lang.org/stable/std/convert/trait.Into.html
source: crawler
fetched_at: 2026-05-06T21:25:35.373217852-03:00
rendered_js: false
word_count: 300
summary: This document describes the Into trait in Rust, which facilitates value-to-value conversions that consume the input, and provides guidance on when to prefer it over the From trait.
tags:
    - rust
    - trait
    - type-conversion
    - memory-safety
    - generic-programming
    - language-features
category: reference
---

## Trait Into

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#451)

```rust
pub trait Into<T>: Sized {
    // Required method
    fn into(self) -> T;
}
```

Expand description

A value-to-value conversion that consumes the input value. The opposite of [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From").

One should avoid implementing [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") and implement [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") instead. Implementing [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") automatically provides one with an implementation of [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") thanks to the blanket implementation in the standard library.

Prefer using [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") over [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") when specifying trait bounds on a generic function to ensure that types that only implement [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") can be used as well.

**Note: This trait must not fail**. If the conversion can fail, use [`TryInto`](https://doc.rust-lang.org/stable/std/convert/trait.TryInto.html "trait std::convert::TryInto").

## [§](#generic-implementations)Generic Implementations

- [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From")`<T> for U` implies `Into<U> for T`
- [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") is reflexive, which means that `Into<T> for T` is implemented

## [§](#implementing-into-for-conversions-to-external-types-in-old-versions-of-rust)Implementing [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") for conversions to external types in old versions of Rust

Prior to Rust 1.41, if the destination type was not part of the current crate then you couldn’t implement [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") directly. For example, take this code:

```rust
struct Wrapper<T>(Vec<T>);
impl<T> From<Wrapper<T>> for Vec<T> {
    fn from(w: Wrapper<T>) -> Vec<T> {
        w.0
    }
}
```

This will fail to compile in older versions of the language because Rust’s orphaning rules used to be a little bit more strict. To bypass this, you could implement [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") directly:

```rust
struct Wrapper<T>(Vec<T>);
impl<T> Into<Vec<T>> for Wrapper<T> {
    fn into(self) -> Vec<T> {
        self.0
    }
}
```

It is important to understand that [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") does not provide a [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") implementation (as [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") does with [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into")). Therefore, you should always try to implement [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") and then fall back to [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into") if [`From`](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From") can’t be implemented.

## [§](#examples)Examples

[`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html) implements [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into")`<`[`Vec`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html)`<`[`u8`](https://doc.rust-lang.org/stable/std/primitive.u8.html "primitive u8")`>>`:

In order to express that we want a generic function to take all arguments that can be converted to a specified type `T`, we can use a trait bound of [`Into`](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into")`<T>`. For example: The function `is_hello` takes all arguments that can be converted into a [`Vec`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html)`<`[`u8`](https://doc.rust-lang.org/stable/std/primitive.u8.html "primitive u8")`>`.

```rust
fn is_hello<T: Into<Vec<u8>>>(s: T) {
   let bytes = b"hello".to_vec();
   assert_eq!(bytes, s.into());
}

let s = "hello".to_string();
is_hello(s);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#455)

Converts this type into the (usually inferred) input type.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*