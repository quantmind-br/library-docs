---
title: Paths - The Rust Reference
url: https://doc.rust-lang.org/reference/paths.html#railroad-SimplePath
source: crawler
fetched_at: 2026-05-06T21:38:44.467348486-03:00
rendered_js: false
word_count: 1055
summary: This document provides a technical definition of paths in the Rust programming language, covering path segments, syntax for generics, qualified paths, and various path resolution qualifiers.
tags:
    - rust
    - programming-language
    - paths
    - syntax
    - generics
    - language-reference
    - turbofish
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Paths](#paths)

A *path* is a sequence of one or more path segments separated by `::` tokens. Paths are used to refer to [items](https://doc.rust-lang.org/reference/items.html), values, [types](https://doc.rust-lang.org/reference/types.html), [macros](https://doc.rust-lang.org/reference/macros.html), and [attributes](https://doc.rust-lang.org/reference/attributes.html).

Two examples of simple paths consisting of only identifier segments:

```rust
x;
x::y::z;
```

## [Types of paths](#types-of-paths)

### [Simple paths](#simple-paths)

Simple paths are used in [visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html) markers, [attributes](https://doc.rust-lang.org/reference/attributes.html), [macros](https://doc.rust-lang.org/reference/macros-by-example.html), and [`use`](https://doc.rust-lang.org/reference/items/use-declarations.html) items. For example:

```rust
#![allow(unused)]
fn main() {
use std::io::{self, Write};
mod m {
    #[clippy::cyclomatic_complexity = "0"]
    pub (in super) fn f1() {}
}
}
```

### [Paths in expressions](#paths-in-expressions)

Paths in expressions allow for paths with generic arguments to be specified. They are used in various places in [expressions](https://doc.rust-lang.org/reference/expressions.html) and [patterns](https://doc.rust-lang.org/reference/patterns.html).

The `::` token is required before the opening `<` for generic arguments to avoid ambiguity with the less-than operator. This is colloquially known as “turbofish” syntax.

```rust
#![allow(unused)]
fn main() {
(0..10).collect::<Vec<_>>();
Vec::<u8>::with_capacity(1024);
}
```

The order of generic arguments is restricted to lifetime arguments, then type arguments, then const arguments, then equality constraints.

Const arguments must be surrounded by braces unless they are a [literal](https://doc.rust-lang.org/reference/expressions/literal-expr.html), an [inferred const](https://doc.rust-lang.org/reference/items/generics.html#r-items.generics.const.inferred), or a single segment path. An [inferred const](https://doc.rust-lang.org/reference/items/generics.html#r-items.generics.const.inferred) may not be surrounded by braces.

```rust
#![allow(unused)]
fn main() {
mod m {
    pub const C: usize = 1;
}
const C: usize = m::C;
fn f<const N: usize>() -> [u8; N] { [0; N] }

let _ = f::<1>(); // Literal.
let _: [_; 1] = f::<_>(); // Inferred const.
let _: [_; 1] = f::<(((_)))>(); // Inferred const.
let _ = f::<C>(); // Single segment path.
let _ = f::<{ m::C }>(); // Multi-segment path must be braced.
}
```

```rust
#![allow(unused)]
fn main() {
fn f<const N: usize>() -> [u8; N] { [0; _] }
let _: [_; 1] = f::<{ _ }>();
//                    ^ ERROR `_` not allowed here
}
```

The synthetic type parameters corresponding to `impl Trait` types are implicit, and these cannot be explicitly specified.

## [Qualified paths](#qualified-paths)

Fully qualified paths allow for disambiguating the path for [trait implementations](https://doc.rust-lang.org/reference/items/implementations.html#trait-implementations) and for specifying [canonical paths](#canonical-paths). When used in a type specification, it supports using the type syntax specified below.

```rust
#![allow(unused)]
fn main() {
struct S;
impl S {
    fn f() { println!("S"); }
}
trait T1 {
    fn f() { println!("T1 f"); }
}
impl T1 for S {}
trait T2 {
    fn f() { println!("T2 f"); }
}
impl T2 for S {}
S::f();  // Calls the inherent impl.
<S as T1>::f();  // Calls the T1 trait function.
<S as T2>::f();  // Calls the T2 trait function.
}
```

### [Paths in types](#paths-in-types)

Type paths are used within type definitions, trait bounds, type parameter bounds, and qualified paths.

Although the `::` token is allowed before the generics arguments, it is not required because there is no ambiguity like there is in [PathInExpression](https://doc.rust-lang.org/reference/paths.html#grammar-PathInExpression).

```rust
#![allow(unused)]
fn main() {
mod ops {
    pub struct Range<T> {f1: T}
    pub trait Index<T> {}
    pub struct Example<'a> {f1: &'a i32}
}
struct S;
impl ops::Index<ops::Range<usize>> for S { /*...*/ }
fn i<'a>() -> impl Iterator<Item = ops::Example<'a>> {
    // ...
   const EXAMPLE: Vec<ops::Example<'static>> = Vec::new();
   EXAMPLE.into_iter()
}
type G = std::boxed::Box<dyn std::ops::FnOnce(isize) -> isize>;
}
```

## [Path qualifiers](#path-qualifiers)

Paths can be denoted with various leading qualifiers to change the meaning of how it is resolved.

> Note
> 
> [`use` declarations](https://doc.rust-lang.org/reference/items/use-declarations.html) have additional behaviors and restrictions for `self`, `super`, `crate`, and `$crate`.

### [`::`](#)

Paths starting with `::` are considered to be *global paths* where the segments of the path start being resolved from a place which differs based on edition. Each identifier in the path must resolve to an item.

> 2018 Edition differences
> 
> In the 2015 Edition, identifiers resolve from the “crate root” (`crate::` in the 2018 edition), which contains a variety of different items, including external crates, default crates such as `std` or `core`, and items in the top level of the crate (including `use` imports).
> 
> Beginning with the 2018 Edition, paths starting with `::` resolve from crates in the [extern prelude](https://doc.rust-lang.org/reference/names/preludes.html#extern-prelude). That is, they must be followed by the name of a crate.

```rust
#![allow(unused)]
fn main() {
pub fn foo() {
    // In the 2018 edition, this accesses `std` via the extern prelude.
    // In the 2015 edition, this accesses `std` via the crate root.
    let now = ::std::time::Instant::now();
    println!("{:?}", now);
}
}
```

```rust
// 2015 Edition
mod a {
    pub fn foo() {}
}
mod b {
    pub fn foo() {
        ::a::foo(); // call `a`'s foo function
        // In Rust 2018, `::a` would be interpreted as the crate `a`.
    }
}
fn main() {}
```

### [`self`](#self)

`self` resolves the path relative to the current module.

`self` can only be used as the first segment, without a preceding `::`.

In a method body, a path which consists of a single `self` segment resolves to the method’s self parameter.

```rust
fn foo() {}
fn bar() {
    self::foo();
}
struct S(bool);
impl S {
  fn baz(self) {
        self.0;
    }
}
fn main() {}
```

### [`Self`](#self-1)

`Self`, with a capital “S”, is used to refer to the current type being implemented or defined. It may be used in the following situations:

- In a [trait](https://doc.rust-lang.org/reference/items/traits.html) definition, it refers to the type implementing the trait.

<!--THE END-->

- In an [implementation](https://doc.rust-lang.org/reference/items/implementations.html), it refers to the type being implemented. When implementing a tuple or unit [struct](https://doc.rust-lang.org/reference/items/structs.html), it also refers to the constructor in the [value namespace](https://doc.rust-lang.org/reference/names/namespaces.html).

<!--THE END-->

- In the definition of a [struct](https://doc.rust-lang.org/reference/items/structs.html), [enumeration](https://doc.rust-lang.org/reference/items/enumerations.html), or [union](https://doc.rust-lang.org/reference/items/unions.html), it refers to the type being defined. The definition is not allowed to be infinitely recursive (there must be an indirection).

The scope of `Self` behaves similarly to a generic parameter; see the [`Self` scope](https://doc.rust-lang.org/reference/names/scopes.html#self-scope) section for more details.

`Self` can only be used as the first segment, without a preceding `::`.

The `Self` path cannot include generic arguments (as in `Self::<i32>`).

```rust
#![allow(unused)]
fn main() {
trait T {
    type Item;
    const C: i32;
    // `Self` will be whatever type that implements `T`.
    fn new() -> Self;
    // `Self::Item` will be the type alias in the implementation.
    fn f(&self) -> Self::Item;
}
struct S;
impl T for S {
    type Item = i32;
    const C: i32 = 9;
    fn new() -> Self {           // `Self` is the type `S`.
        S
    }
    fn f(&self) -> Self::Item {  // `Self::Item` is the type `i32`.
        Self::C                  // `Self::C` is the constant value `9`.
    }
}

// `Self` is in scope within the generics of a trait definition,
// to refer to the type being defined.
trait Add<Rhs = Self> {
    type Output;
    // `Self` can also reference associated items of the
    // type being implemented.
    fn add(self, rhs: Rhs) -> Self::Output;
}

struct NonEmptyList<T> {
    head: T,
    // A struct can reference itself (as long as it is not
    // infinitely recursive).
    tail: Option<Box<Self>>,
}
}
```

### [`super`](#super)

`super` in a path resolves to the parent module.

It may only be used in leading segments of the path, possibly after an initial `self` segment.

```rust
mod a {
    pub fn foo() {}
}
mod b {
    pub fn foo() {
        super::a::foo(); // call a's foo function
    }
}
fn main() {}
```

`super` may be repeated several times after the first `super` or `self` to refer to ancestor modules.

```rust
mod a {
    fn foo() {}

    mod b {
        mod c {
            fn foo() {
                super::super::foo(); // call a's foo function
                self::super::super::foo(); // call a's foo function
            }
        }
    }
}
fn main() {}
```

### [`crate`](#crate)

`crate` resolves the path relative to the current crate.

`crate` can only be used as the first segment, without a preceding `::`.

```rust
fn foo() {}
mod a {
    fn bar() {
        crate::foo();
    }
}
fn main() {}
```

### [`$crate`](#crate-1)

[`$crate`](https://doc.rust-lang.org/reference/macros-by-example.html#r-macro.decl.hygiene.crate) is only used within [macro transcribers](https://doc.rust-lang.org/reference/macros-by-example.html), and can only be used as the first segment, without a preceding `::`.

[`$crate`](https://doc.rust-lang.org/reference/macros-by-example.html#r-macro.decl.hygiene.crate) will expand to a path to access items from the top level of the crate where the macro is defined, regardless of which crate the macro is invoked.

```rust
pub fn increment(x: u32) -> u32 {
    x + 1
}

#[macro_export]
macro_rules! inc {
    ($x:expr) => ( $crate::increment($x) )
}
fn main() { }
```

## [Canonical paths](#canonical-paths)

Each item defined in a module or implementation has a *canonical path* that corresponds to where within its crate it is defined.

All other paths to these items are aliases.

The canonical path is defined as a *path prefix* appended by the path segment the item itself defines.

[Implementations](https://doc.rust-lang.org/reference/items/implementations.html) and [use declarations](https://doc.rust-lang.org/reference/items/use-declarations.html) do not have canonical paths, although the items that implementations define do have them. Items defined in block expressions do not have canonical paths. Items defined in a module that does not have a canonical path do not have a canonical path. Associated items defined in an implementation that refers to an item without a canonical path, e.g. as the implementing type, the trait being implemented, a type parameter or bound on a type parameter, do not have canonical paths.

The path prefix for modules is the canonical path to that module.

For bare implementations, it is the canonical path of the item being implemented surrounded by angle (`<>`) brackets.

For [trait implementations](https://doc.rust-lang.org/reference/items/implementations.html#trait-implementations), it is the canonical path of the item being implemented followed by `as` followed by the canonical path to the trait all surrounded in angle (`<>`) brackets.

The canonical path is only meaningful within a given crate. There is no global namespace across crates; an item’s canonical path merely identifies it within the crate.

```rust
// Comments show the canonical path of the item.

mod a { // crate::a
    pub struct Struct; // crate::a::Struct

    pub trait Trait { // crate::a::Trait
        fn f(&self); // crate::a::Trait::f
    }

    impl Trait for Struct {
        fn f(&self) {} // <crate::a::Struct as crate::a::Trait>::f
    }

    impl Struct {
        fn g(&self) {} // <crate::a::Struct>::g
    }
}

mod without { // crate::without
    fn canonicals() { // crate::without::canonicals
        struct OtherStruct; // None

        trait OtherTrait { // None
            fn g(&self); // None
        }

        impl OtherTrait for OtherStruct {
            fn g(&self) {} // None
        }

        impl OtherTrait for crate::a::Struct {
            fn g(&self) {} // None
        }

        impl crate::a::Trait for OtherStruct {
            fn f(&self) {} // None
        }
    }
}

fn main() {}
```