---
title: Traits - The Rust Reference
url: https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility
source: crawler
fetched_at: 2026-05-06T21:21:51.249881446-03:00
rendered_js: false
word_count: 1078
summary: This document defines traits in the Rust programming language, covering their structure, associated items, generic parameters, and the requirements for dyn compatibility in trait objects.
tags:
    - rust
    - traits
    - dyn-compatibility
    - generics
    - type-system
    - programming-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Traits](#traits)

A *trait* describes an abstract interface that types can implement. This interface consists of [associated items](https://doc.rust-lang.org/reference/items/associated-items.html), which come in three varieties:

- [functions](https://doc.rust-lang.org/reference/items/associated-items.html#associated-functions-and-methods)
- [types](https://doc.rust-lang.org/reference/items/associated-items.html#associated-types)
- [constants](https://doc.rust-lang.org/reference/items/associated-items.html#associated-constants)

The trait declaration defines a trait in the [type namespace](https://doc.rust-lang.org/reference/names/namespaces.html) of the module or block where it is located.

Associated items are defined as members of the trait within their respective namespaces. Associated types are defined in the type namespace. Associated constants and associated functions are defined in the value namespace.

All traits define an implicit type parameter `Self` that refers to “the type that is implementing this interface”. Traits may also contain additional type parameters. These type parameters, including `Self`, may be constrained by other traits and so forth [as usual](https://doc.rust-lang.org/reference/items/generics.html).

Traits are implemented for specific types through separate [implementations](https://doc.rust-lang.org/reference/items/implementations.html).

Trait functions may omit the function body by replacing it with a semicolon. This indicates that the implementation must define the function. If the trait function defines a body, this definition acts as a default for any implementation which does not override it. Similarly, associated constants may omit the equals sign and expression to indicate implementations must define the constant value. Associated types must never define the type, the type may only be specified in an implementation.

```rust
#![allow(unused)]
fn main() {
// Examples of associated trait items with and without definitions.
trait Example {
    const CONST_NO_DEFAULT: i32;
    const CONST_WITH_DEFAULT: i32 = 99;
    type TypeNoDefault;
    fn method_without_default(&self);
    fn method_with_default(&self) {}
}
}
```

Trait functions are not allowed to be [`const`](https://doc.rust-lang.org/reference/items/functions.html#const-functions).

## [Trait bounds](#trait-bounds)

Generic items may use traits as [bounds](https://doc.rust-lang.org/reference/trait-bounds.html) on their type parameters.

## [Generic traits](#generic-traits)

Type parameters can be specified for a trait to make it generic. These appear after the trait name, using the same syntax used in [generic functions](https://doc.rust-lang.org/reference/items/functions.html#generic-functions).

```rust
#![allow(unused)]
fn main() {
trait Seq<T> {
    fn len(&self) -> u32;
    fn elt_at(&self, n: u32) -> T;
    fn iter<F>(&self, f: F) where F: Fn(T);
}
}
```

## [Dyn compatibility](#dyn-compatibility)

A dyn-compatible trait can be the base trait of a [trait object](https://doc.rust-lang.org/reference/types/trait-object.html). A trait is *dyn compatible* if it has the following qualities:

- All [supertraits](#supertraits) must also be dyn compatible.

<!--THE END-->

- `Sized` must not be a [supertrait](#supertraits). In other words, it must not require `Self: Sized`.

<!--THE END-->

- It must not have any associated constants.

<!--THE END-->

- It must not have any associated types with generics.

<!--THE END-->

- All associated functions must either be dispatchable from a trait object or be explicitly non-dispatchable:
  
  - Dispatchable functions must:
    
    - Not have any type parameters (although lifetime parameters are allowed).
    - Be a [method](https://doc.rust-lang.org/reference/items/associated-items.html#methods) that does not use `Self` except in the type of the receiver.
    - Have a receiver with one of the following types:
      
      - `&Self` (i.e. `&self`)
      - `&mut Self` (i.e `&mut self`)
      - [`Box<Self>`](https://doc.rust-lang.org/reference/special-types-and-traits.html#boxt)
      - [`Rc<Self>`](https://doc.rust-lang.org/reference/special-types-and-traits.html#rct)
      - [`Arc<Self>`](https://doc.rust-lang.org/reference/special-types-and-traits.html#arct)
      - [`Pin<P>`](https://doc.rust-lang.org/reference/special-types-and-traits.html#pinp) where `P` is one of the types above
    - Not have an opaque return type; that is,
      
      - Not be an `async fn` (which has a hidden `Future` type).
      - Not have a return position `impl Trait` type (`fn example(&self) -> impl Trait`).
    - Not have a `where Self: Sized` bound (receiver type of `Self` (i.e. `self`) implies this).
  - Explicitly non-dispatchable functions require:
    
    - Have a `where Self: Sized` bound (receiver type of `Self` (i.e. `self`) implies this).

<!--THE END-->

- The [`AsyncFn`](https://doc.rust-lang.org/core/ops/async_function/trait.AsyncFn.html), [`AsyncFnMut`](https://doc.rust-lang.org/core/ops/async_function/trait.AsyncFnMut.html), and [`AsyncFnOnce`](https://doc.rust-lang.org/core/ops/async_function/trait.AsyncFnOnce.html) traits are not dyn-compatible.

> Note
> 
> This concept was formerly known as *object safety*.

```rust
#![allow(unused)]
fn main() {
use std::rc::Rc;
use std::sync::Arc;
use std::pin::Pin;
// Examples of dyn compatible methods.
trait TraitMethods {
    fn by_ref(self: &Self) {}
    fn by_ref_mut(self: &mut Self) {}
    fn by_box(self: Box<Self>) {}
    fn by_rc(self: Rc<Self>) {}
    fn by_arc(self: Arc<Self>) {}
    fn by_pin(self: Pin<&Self>) {}
    fn with_lifetime<'a>(self: &'a Self) {}
    fn nested_pin(self: Pin<Arc<Self>>) {}
}
struct S;
impl TraitMethods for S {}
let t: Box<dyn TraitMethods> = Box::new(S);
}
```

```rust
#![allow(unused)]
fn main() {
// This trait is dyn compatible, but these methods cannot be dispatched on a trait object.
trait NonDispatchable {
    // Non-methods cannot be dispatched.
    fn foo() where Self: Sized {}
    // Self type isn't known until runtime.
    fn returns(&self) -> Self where Self: Sized;
    // `other` may be a different concrete type of the receiver.
    fn param(&self, other: Self) where Self: Sized {}
    // Generics are not compatible with vtables.
    fn typed<T>(&self, x: T) where Self: Sized {}
}

struct S;
impl NonDispatchable for S {
    fn returns(&self) -> Self where Self: Sized { S }
}
let obj: Box<dyn NonDispatchable> = Box::new(S);
obj.returns(); // ERROR: cannot call with Self return
obj.param(S);  // ERROR: cannot call with Self parameter
obj.typed(1);  // ERROR: cannot call with generic type
}
```

```rust
#![allow(unused)]
fn main() {
use std::rc::Rc;
// Examples of dyn-incompatible traits.
trait DynIncompatible {
    const CONST: i32 = 1;  // ERROR: cannot have associated const

    fn foo() {}  // ERROR: associated function without Sized
    fn returns(&self) -> Self; // ERROR: Self in return type
    fn typed<T>(&self, x: T) {} // ERROR: has generic type parameters
    fn nested(self: Rc<Box<Self>>) {} // ERROR: nested receiver cannot be dispatched on
}

struct S;
impl DynIncompatible for S {
    fn returns(&self) -> Self { S }
}
let obj: Box<dyn DynIncompatible> = Box::new(S); // ERROR
}
```

```rust
#![allow(unused)]
fn main() {
// `Self: Sized` traits are dyn-incompatible.
trait TraitWithSize where Self: Sized {}

struct S;
impl TraitWithSize for S {}
let obj: Box<dyn TraitWithSize> = Box::new(S); // ERROR
}
```

```rust
#![allow(unused)]
fn main() {
// Dyn-incompatible if `Self` is a type argument.
trait Super<A> {}
trait WithSelf: Super<Self> where Self: Sized {}

struct S;
impl<A> Super<A> for S {}
impl WithSelf for S {}
let obj: Box<dyn WithSelf> = Box::new(S); // ERROR: cannot use `Self` type parameter
}
```

## [Supertraits](#supertraits)

**Supertraits** are traits that are required to be implemented for a type to implement a specific trait. Furthermore, anywhere a [generic](https://doc.rust-lang.org/reference/items/generics.html) or [trait object](https://doc.rust-lang.org/reference/types/trait-object.html) is bounded by a trait, it has access to the associated items of its supertraits.

Supertraits are declared by trait bounds on the `Self` type of a trait and transitively the supertraits of the traits declared in those trait bounds. It is an error for a trait to be its own supertrait.

The trait with a supertrait is called a **subtrait** of its supertrait.

The following is an example of declaring `Shape` to be a supertrait of `Circle`.

```rust
#![allow(unused)]
fn main() {
trait Shape { fn area(&self) -> f64; }
trait Circle: Shape { fn radius(&self) -> f64; }
}
```

And the following is the same example, except using [where clauses](https://doc.rust-lang.org/reference/items/generics.html#where-clauses).

```rust
#![allow(unused)]
fn main() {
trait Shape { fn area(&self) -> f64; }
trait Circle where Self: Shape { fn radius(&self) -> f64; }
}
```

This next example gives `radius` a default implementation using the `area` function from `Shape`.

```rust
#![allow(unused)]
fn main() {
trait Shape { fn area(&self) -> f64; }
trait Circle where Self: Shape {
    fn radius(&self) -> f64 {
        // A = pi * r^2
        // so algebraically,
        // r = sqrt(A / pi)
        (self.area() / std::f64::consts::PI).sqrt()
    }
}
}
```

This next example calls a supertrait method on a generic parameter.

```rust
#![allow(unused)]
fn main() {
trait Shape { fn area(&self) -> f64; }
trait Circle: Shape { fn radius(&self) -> f64; }
fn print_area_and_radius<C: Circle>(c: C) {
    // Here we call the area method from the supertrait `Shape` of `Circle`.
    println!("Area: {}", c.area());
    println!("Radius: {}", c.radius());
}
}
```

Similarly, here is an example of calling supertrait methods on trait objects.

```rust
#![allow(unused)]
fn main() {
trait Shape { fn area(&self) -> f64; }
trait Circle: Shape { fn radius(&self) -> f64; }
struct UnitCircle;
impl Shape for UnitCircle { fn area(&self) -> f64 { std::f64::consts::PI } }
impl Circle for UnitCircle { fn radius(&self) -> f64 { 1.0 } }
let circle = UnitCircle;
let circle = Box::new(circle) as Box<dyn Circle>;
let nonsense = circle.radius() * circle.area();
}
```

## [Unsafe traits](#unsafe-traits)

Traits items that begin with the `unsafe` keyword indicate that *implementing* the trait may be [unsafe](https://doc.rust-lang.org/reference/unsafety.html). It is safe to use a correctly implemented unsafe trait. The [trait implementation](https://doc.rust-lang.org/reference/items/implementations.html#trait-implementations) must also begin with the `unsafe` keyword.

[`Sync`](https://doc.rust-lang.org/reference/special-types-and-traits.html#sync) and [`Send`](https://doc.rust-lang.org/reference/special-types-and-traits.html#send) are examples of unsafe traits.

## [Parameter patterns](#parameter-patterns)

[\[items.traits.params.patterns-no-body\]](#r-items.traits.params.patterns-no-body "items.traits.params.patterns-no-body")

Parameters in associated functions without a body only allow [IDENTIFIER](https://doc.rust-lang.org/reference/identifiers.html#grammar-IDENTIFIER) or `_` [wild card](https://doc.rust-lang.org/reference/patterns.html#wildcard-pattern) patterns, as well as the form allowed by [SelfParam](https://doc.rust-lang.org/reference/items/functions.html#grammar-SelfParam). `mut` [IDENTIFIER](https://doc.rust-lang.org/reference/identifiers.html#grammar-IDENTIFIER) is currently allowed, but it is deprecated and will become a hard error in the future.

```rust
#![allow(unused)]
fn main() {
trait T {
    fn f1(&self);
    fn f2(x: Self, _: i32);
}
}
```

```rust
#![allow(unused)]
fn main() {
trait T {
    fn f2(&x: &i32); // ERROR: patterns aren't allowed in functions without bodies
}
}
```

[\[items.traits.params.patterns-with-body\]](#r-items.traits.params.patterns-with-body "items.traits.params.patterns-with-body")

Parameters in associated functions with a body only allow irrefutable patterns.

```rust
#![allow(unused)]
fn main() {
trait T {
    fn f1((a, b): (i32, i32)) {} // OK: is irrefutable
}
}
```

```rust
#![allow(unused)]
fn main() {
trait T {
    fn f1(123: i32) {} // ERROR: pattern is refutable
    fn f2(Some(x): Option<i32>) {} // ERROR: pattern is refutable
}
}
```

> 2018 Edition differences
> 
> Prior to the 2018 edition, the pattern for an associated function parameter is optional:
> 
> ```rust
> #![allow(unused)]
fn main() {
// 2015 Edition
trait T {
    fn f(i32); // OK: parameter identifiers are not required
}
}
> ```
> 
> Beginning in the 2018 edition, patterns are no longer optional.

> 2018 Edition differences
> 
> Prior to the 2018 edition, parameters in associated functions with a body are limited to the following kinds of patterns:
> 
> - [IDENTIFIER](https://doc.rust-lang.org/reference/identifiers.html#grammar-IDENTIFIER)
> - `mut` [IDENTIFIER](https://doc.rust-lang.org/reference/identifiers.html#grammar-IDENTIFIER)
> - [`_`](https://doc.rust-lang.org/reference/patterns.html#wildcard-pattern)
> - `&` [IDENTIFIER](https://doc.rust-lang.org/reference/identifiers.html#grammar-IDENTIFIER)
> - `&&` [IDENTIFIER](https://doc.rust-lang.org/reference/identifiers.html#grammar-IDENTIFIER)
> 
> ```rust
> #![allow(unused)]
fn main() {
// 2015 Edition
trait T {
    fn f1((a, b): (i32, i32)) {} // ERROR: pattern not allowed
}
}
> ```
> 
> Beginning in 2018, all irrefutable patterns are allowed as described in [items.traits.params.patterns-with-body](https://doc.rust-lang.org/reference/items/traits.html#r-items.traits.params.patterns-with-body).

## [Item visibility](#item-visibility)

Trait items syntactically allow a [Visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html#grammar-Visibility) annotation, but this is rejected when the trait is validated. This allows items to be parsed with a unified syntax across different contexts where they are used. As an example, an empty `vis` macro fragment specifier can be used for trait items, where the macro rule may be used in other situations where visibility is allowed.

```rust
macro_rules! create_method {
    ($vis:vis $name:ident) => {
        $vis fn $name(&self) {}
    };
}

trait T1 {
    // Empty `vis` is allowed.
    create_method! { method_of_t1 }
}

struct S;

impl S {
    // Visibility is allowed here.
    create_method! { pub method_of_s }
}

impl T1 for S {}

fn main() {
    let s = S;
    s.method_of_t1();
    s.method_of_s();
}
```