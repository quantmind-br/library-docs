---
title: Generic parameters - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/items/generics.html#railroad-WhereClause
source: crawler
fetched_at: 2026-05-06T21:26:44.982249093-03:00
rendered_js: false
word_count: 924
summary: This document describes the syntax and usage of generic parameters in the Rust programming language, including support for types, lifetimes, and const parameters.
tags:
    - rust
    - generics
    - const-generics
    - lifetime-parameters
    - programming-language
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Generic parameters](#generic-parameters)

[Functions](https://doc.rust-lang.org/stable/reference/items/functions.html), [type aliases](https://doc.rust-lang.org/stable/reference/items/type-aliases.html), [structs](https://doc.rust-lang.org/stable/reference/items/structs.html), [enumerations](https://doc.rust-lang.org/stable/reference/items/enumerations.html), [unions](https://doc.rust-lang.org/stable/reference/items/unions.html), [traits](https://doc.rust-lang.org/stable/reference/items/traits.html), and [implementations](https://doc.rust-lang.org/stable/reference/items/implementations.html) may be *parameterized* by types, constants, and lifetimes. These parameters are listed in angle brackets (`<...>`), usually immediately after the name of the item and before its definition. For implementations, which don’t have a name, they come directly after `impl`.

The order of generic parameters is restricted to lifetime parameters and then type and const parameters intermixed.

The same parameter name may not be declared more than once in a [GenericParams](https://doc.rust-lang.org/stable/reference/items/generics.html#grammar-GenericParams) list.

Some examples of items with type, const, and lifetime parameters:

```rust
#![allow(unused)]
fn main() {
fn foo<'a, T>() {}
trait A<U> {}
struct Ref<'a, T> where T: 'a { r: &'a T }
struct InnerArray<T, const N: usize>([T; N]);
struct EitherOrderWorks<const N: bool, U>(U);
}
```

Generic parameters are in scope within the item definition where they are declared. They are not in scope for items declared within the body of a function as described in [item declarations](https://doc.rust-lang.org/stable/reference/statements.html#item-declarations). See [generic parameter scopes](https://doc.rust-lang.org/stable/reference/names/scopes.html#generic-parameter-scopes) for more details.

[References](https://doc.rust-lang.org/stable/reference/types/pointer.html#shared-references-), [raw pointers](https://doc.rust-lang.org/stable/reference/types/pointer.html#raw-pointers-const-and-mut), [arrays](https://doc.rust-lang.org/stable/reference/types/array.html), [slices](https://doc.rust-lang.org/stable/reference/types/slice.html), [tuples](https://doc.rust-lang.org/stable/reference/types/tuple.html), and [function pointers](https://doc.rust-lang.org/stable/reference/types/function-pointer.html) have lifetime or type parameters as well, but are not referred to with path syntax.

`'_` and `'static` are not valid lifetime parameter names.

### [Const generics](#const-generics)

*Const generic parameters* allow items to be generic over constant values.

The const identifier introduces a name in the [value namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html) for the constant parameter, and all instances of the item must be instantiated with a value of the given type.

The only allowed types of const parameters are `u8`, `u16`, `u32`, `u64`, `u128`, `usize`, `i8`, `i16`, `i32`, `i64`, `i128`, `isize`, `char` and `bool`.

Const parameters can be used anywhere a [const item](https://doc.rust-lang.org/stable/reference/items/constant-items.html) can be used, with the exception that when used in a [type](https://doc.rust-lang.org/stable/reference/types.html) or [array repeat expression](https://doc.rust-lang.org/stable/reference/expressions/array-expr.html), it must be standalone (as described below). That is, they are allowed in the following places:

1. As an applied const to any type which forms a part of the signature of the item in question.
2. As part of a const expression used to define an [associated const](https://doc.rust-lang.org/stable/reference/items/associated-items.html#associated-constants), or as a parameter to an [associated type](https://doc.rust-lang.org/stable/reference/items/associated-items.html#associated-types).
3. As a value in any runtime expression in the body of any functions in the item.
4. As a parameter to any type used in the body of any functions in the item.
5. As a part of the type of any fields in the item.

```rust
#![allow(unused)]
fn main() {
// Examples where const generic parameters can be used.

// Used in the signature of the item itself.
fn foo<const N: usize>(arr: [i32; N]) {
    // Used as a type within a function body.
    let x: [i32; N];
    // Used as an expression.
    println!("{}", N * 2);
}

// Used as a field of a struct.
struct Foo<const N: usize>([i32; N]);

impl<const N: usize> Foo<N> {
    // Used as an associated constant.
    const CONST: usize = N * 4;
}

trait Trait {
    type Output;
}

impl<const N: usize> Trait for Foo<N> {
    // Used as an associated type.
    type Output = [i32; N];
}
}
```

```rust
#![allow(unused)]
fn main() {
// Examples where const generic parameters cannot be used.
fn foo<const N: usize>() {
    // Cannot use in item definitions within a function body.
    const BAD_CONST: [usize; N] = [1; N];
    static BAD_STATIC: [usize; N] = [1; N];
    fn inner(bad_arg: [usize; N]) {
        let bad_value = N * 2;
    }
    type BadAlias = [usize; N];
    struct BadStruct([usize; N]);
}
}
```

As a further restriction, const parameters may only appear as a standalone argument inside of a [type](https://doc.rust-lang.org/stable/reference/types.html) or [array repeat expression](https://doc.rust-lang.org/stable/reference/expressions/array-expr.html). In those contexts, they may only be used as a single segment [path expression](https://doc.rust-lang.org/stable/reference/expressions/path-expr.html), possibly inside a [block](https://doc.rust-lang.org/stable/reference/expressions/block-expr.html) (such as `N` or `{N}`). That is, they cannot be combined with other expressions.

```rust
#![allow(unused)]
fn main() {
// Examples where const parameters may not be used.

// Not allowed to combine in other expressions in types, such as the
// arithmetic expression in the return type here.
fn bad_function<const N: usize>() -> [u8; {N + 1}] {
    // Similarly not allowed for array repeat expressions.
    [1; {N + 1}]
}
}
```

A const argument in a [path](https://doc.rust-lang.org/stable/reference/paths.html) specifies the const value to use for that item.

The argument must either be an [inferred const](https://doc.rust-lang.org/stable/reference/items/generics.html#r-items.generics.const.inferred) or be a [const expression](https://doc.rust-lang.org/stable/reference/const_eval.html#constant-expressions) of the type ascribed to the const parameter. The const expression must be a [block expression](https://doc.rust-lang.org/stable/reference/expressions/block-expr.html) (surrounded with braces) unless it is a single path segment (an [IDENTIFIER](https://doc.rust-lang.org/stable/reference/identifiers.html#grammar-IDENTIFIER)) or a [literal](https://doc.rust-lang.org/stable/reference/expressions/literal-expr.html) (with a possibly leading `-` token).

> Note
> 
> This syntactic restriction is necessary to avoid requiring infinite lookahead when parsing an expression inside of a type.

```rust
#![allow(unused)]
fn main() {
struct S<const N: i64>;
const C: i64 = 1;
fn f<const N: i64>() -> S<N> { S }

let _ = f::<1>(); // Literal.
let _ = f::<-1>(); // Negative literal.
let _ = f::<{ 1 + 2 }>(); // Constant expression.
let _ = f::<C>(); // Single segment path.
let _ = f::<{ C + 1 }>(); // Constant expression.
let _: S<1> = f::<_>(); // Inferred const.
let _: S<1> = f::<(((_)))>(); // Inferred const.
}
```

Where a const argument is expected, an `_` (optionally surrounded by any number of matching parentheses), called the *inferred const* ([path rules](https://doc.rust-lang.org/stable/reference/paths.html#r-paths.expr.complex-const-params), [array expression rules](https://doc.rust-lang.org/stable/reference/expressions/array-expr.html#r-expr.array.length-restriction)), can be used instead. This asks the compiler to infer the const argument if possible based on surrounding information.

```rust
#![allow(unused)]
fn main() {
fn make_buf<const N: usize>() -> [u8; N] {
    [0; _]
    //  ^ Infers `N`.
}
let _: [u8; 1024] = make_buf::<_>();
//                             ^ Infers `1024`.
}
```

> Note
> 
> An [inferred const](https://doc.rust-lang.org/stable/reference/items/generics.html#r-items.generics.const.inferred) is not semantically an [expression](https://doc.rust-lang.org/stable/reference/expressions.html#grammar-Expression) and so is not accepted within braces.
> 
> ```rust
> #![allow(unused)]
fn main() {
fn f<const N: usize>() -> [u8; N] { [0; _] }
let _: [_; 1] = f::<{ _ }>();
//                    ^ ERROR `_` not allowed here
}
> ```

The inferred const cannot be used in item signatures.

```rust
#![allow(unused)]
fn main() {
fn f<const N: usize>(x: [u8; N]) -> [u8; _] { x }
//                                       ^ ERROR not allowed
}
```

When there is ambiguity if a generic argument could be resolved as either a type or const argument, it is always resolved as a type. Placing the argument in a block expression can force it to be interpreted as a const argument.

```rust
#![allow(unused)]
fn main() {
type N = u32;
struct Foo<const N: usize>;
// The following is an error, because `N` is interpreted as the type alias `N`.
fn foo<const N: usize>() -> Foo<N> { todo!() } // ERROR
// Can be fixed by wrapping in braces to force it to be interpreted as the `N`
// const parameter:
fn bar<const N: usize>() -> Foo<{ N }> { todo!() } // ok
}
```

Unlike type and lifetime parameters, const parameters can be declared without being used inside of a parameterized item, with the exception of implementations as described in [generic implementations](https://doc.rust-lang.org/stable/reference/items/implementations.html#generic-implementations):

```rust
#![allow(unused)]
fn main() {
// ok
struct Foo<const N: usize>;
enum Bar<const M: usize> { A, B }

// ERROR: unused parameter
struct Baz<T>;
struct Biz<'a>;
struct Unconstrained;
impl<const N: usize> Unconstrained {}
}
```

When resolving a trait bound obligation, the exhaustiveness of all implementations of const parameters is not considered when determining if the bound is satisfied. For example, in the following, even though all possible const values for the `bool` type are implemented, it is still an error that the trait bound is not satisfied:

```rust
#![allow(unused)]
fn main() {
struct Foo<const B: bool>;
trait Bar {}
impl Bar for Foo<true> {}
impl Bar for Foo<false> {}

fn needs_bar(_: impl Bar) {}
fn generic<const B: bool>() {
    let v = Foo::<B>;
    needs_bar(v); // ERROR: trait bound `Foo<B>: Bar` is not satisfied
}
}
```

## [Where clauses](#where-clauses)

*Where clauses* provide another way to specify bounds on type and lifetime parameters as well as a way to specify bounds on types that aren’t type parameters.

The `for` keyword can be used to introduce [higher-ranked lifetimes](https://doc.rust-lang.org/stable/reference/trait-bounds.html#higher-ranked-trait-bounds). It only allows [LifetimeParam](https://doc.rust-lang.org/stable/reference/items/generics.html#grammar-LifetimeParam) parameters.

```rust
#![allow(unused)]
fn main() {
struct A<T>
where
    T: Iterator,            // Could use A<T: Iterator> instead
    T::Item: Copy,          // Bound on an associated type
    String: PartialEq<T>,   // Bound on `String`, using the type parameter
    i32: Default,           // Allowed, but not useful
{
    f: T,
}
}
```

## [Attributes](#attributes)

Generic lifetime and type parameters allow [attributes](https://doc.rust-lang.org/stable/reference/attributes.html) on them. There are no built-in attributes that do anything in this position, although custom derive attributes may give meaning to it.

This example shows using a custom derive attribute to modify the meaning of a generic parameter.

```rust
// Assume that the derive for MyFlexibleClone declared `my_flexible_clone` as
// an attribute it understands.
#[derive(MyFlexibleClone)]
struct Foo<#[my_flexible_clone(unbounded)] H> {
    a: *const H
}
```