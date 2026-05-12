---
title: Sized in std::marker - Rust
url: https://doc.rust-lang.org/stable/std/marker/trait.Sized.html
source: crawler
fetched_at: 2026-05-06T21:25:23.093849735-03:00
rendered_js: false
word_count: 183
summary: Explains the Rust Sized trait, which identifies types with a constant size at compile time and discusses the ?Sized syntax and dyn compatibility implications.
tags:
    - rust-lang
    - sized-trait
    - compile-time
    - type-bounds
    - dyn-compatibility
category: reference
---

## Trait Sized

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#161)

```rust
pub trait Sized { }
```

Expand description

Types with a constant size known at compile time.

All type parameters have an implicit bound of `Sized`. The special syntax `?Sized` can be used to remove this bound if it’s not appropriate.

```rust
struct Foo<T>(T);
struct Bar<T: ?Sized>(T);

// struct FooUse(Foo<[i32]>); // error: Sized is not implemented for [i32]
struct BarUse(Bar<[i32]>); // OK
```

The one exception is the implicit `Self` type of a trait. A trait does not have an implicit `Sized` bound as this is incompatible with [trait object](https://doc.rust-lang.org/stable/book/ch17-02-trait-objects.html)s where, by definition, the trait needs to work with all possible implementors, and thus could be any size.

Although Rust will let you bind `Sized` to a trait, you won’t be able to use it to form a trait object later:

```rust
trait Foo { }
trait Bar: Sized { }

struct Impl;
impl Foo for Impl { }
impl Bar for Impl { }

let x: &dyn Foo = &Impl;    // OK
// let y: &dyn Bar = &Impl; // error: the trait `Bar` cannot be made into an object
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*