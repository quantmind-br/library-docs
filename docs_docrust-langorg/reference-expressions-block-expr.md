---
title: Block expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/block-expr.html
source: crawler
fetched_at: 2026-05-06T21:26:56.798253064-03:00
rendered_js: false
word_count: 1152
summary: This document defines the syntax, evaluation rules, and scoping behaviors of block expressions in the Rust programming language, including standard blocks and asynchronous blocks.
tags:
    - rust
    - block-expressions
    - async-blocks
    - control-flow
    - scoping
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Block expressions](#block-expressions)

A *block expression*, or *block*, is a control flow expression and anonymous namespace scope for items and variable declarations.

As a control flow expression, a block sequentially executes its component non-item declaration statements and then its final optional expression.

As an anonymous namespace scope, item declarations are only in scope inside the block itself and variables declared by `let` statements are in scope from the next statement until the end of the block. See the [scopes](https://doc.rust-lang.org/reference/names/scopes.html) chapter for more details.

The syntax for a block is `{`, then any [inner attributes](https://doc.rust-lang.org/reference/attributes.html), then any number of [statements](https://doc.rust-lang.org/reference/statements.html), then an optional expression, called the final operand, and finally a `}`.

Statements are usually required to be followed by a semicolon, with two exceptions:

1. Item declaration statements do not need to be followed by a semicolon.
2. Expression statements usually require a following semicolon except if its outer expression is a flow control expression.

Furthermore, extra semicolons between statements are allowed, but these semicolons do not affect semantics.

When evaluating a block expression, each statement, except for item declaration statements, is executed sequentially.

Then the final operand is executed, if given.

When a block contains a [final operand](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.inner-attributes), the block has the type and value of that final operand.

```rust
#![allow(unused)]
fn main() {
let x: u8 = { 0u8 }; // `0u8` is the final operand.
assert_eq!(x, 0);
let x: u8 = { (); 0u8 }; // As above.
assert_eq!(x, 0);
}
```

When a block does not contain a [final operand](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.inner-attributes) and the block does not diverge, the block has [unit type](https://doc.rust-lang.org/reference/types/tuple.html#r-type.tuple.unit) and [unit value](https://doc.rust-lang.org/reference/types/tuple.html#r-type.tuple.unit).

```rust
#![allow(unused)]
fn main() {
let x: () = {}; // Has no final operand.
assert_eq!(x, ());
let x: () = { 0u8; }; // As above.
assert_eq!(x, ());
}
```

When a block does not contain a [final operand](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.inner-attributes) and the block [diverges](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.diverging), the block has the [never type](https://doc.rust-lang.org/reference/types/never.html#r-type.never) and has no final value (because its type is [uninhabited](https://doc.rust-lang.org/reference/glossary.html#r-glossary.uninhabited)).

```rust
#![allow(unused)]
fn main() {
fn f() -> ! { loop {}; } // Diverges and has no final operand.
//          ^^^^^^^^^^^^
// The body of a function is a block expression.
}
```

> Note
> 
> Observe that a block having no final operand is distinct from having an explicit final operand with unit type. E.g., even though this block diverges, the type of the block is [unit](https://doc.rust-lang.org/reference/types/tuple.html#r-type.tuple.unit) rather than [never](https://doc.rust-lang.org/reference/types/never.html#r-type.never).
> 
> ```rust
> #![allow(unused)]
fn main() {
fn f() -> ! { loop {}; () } // ERROR: Mismatched types.
//          ^^^^^^^^^^^^^^^ This block has unit type.
}
> ```

> Note
> 
> As a control flow expression, if a block expression is the outer expression of an expression statement, the expected type is `()` unless it is followed immediately by a semicolon.

A block is considered to be [diverging](https://doc.rust-lang.org/reference/divergence.html#r-divergence) if all reachable control flow paths contain a diverging expression, unless that expression is a [place expression](https://doc.rust-lang.org/reference/expressions.html#r-expr.place-value.place-memory-location) that is not read from.

```rust
#![allow(unused)]
fn main() {
#![ feature(never_type) ]
fn no_control_flow() -> ! {
    // There are no conditional statements, so this entire function body is diverging.
    loop {}
}

fn control_flow_diverging() -> ! {
    // All paths are diverging, so this entire function body is diverging.
    if true {
        loop {}
    } else {
        loop {}
    }
}

fn control_flow_not_diverging() -> () {
    // Some paths are not diverging, so this entire block is not diverging.
    if true {
        ()
    } else {
        loop {}
    }
}

// Note: This makes use of the unstable never type which is only available on
// Rust's nightly channel. This is done for illustration purposes. It is
// possible to encounter this scenario in stable Rust, but requires a more
// convoluted example.
struct Foo {
    x: !,
}

fn make<T>() -> T { loop {} }

fn diverging_place_read() -> ! {
    let foo = Foo { x: make() };
    // A read of a place expression produces a diverging block.
    let _x = foo.x;
}
}
```

```rust
#![allow(unused)]
fn main() {
#![ feature(never_type) ]
fn make<T>() -> T { loop {} }
struct Foo {
    x: !,
}
fn diverging_place_not_read() -> ! {
    let foo = Foo { x: make() };
    // Assignment to `_` means the place is not read.
    let _ = foo.x;
} // ERROR: Mismatched types.
}
```

Blocks are always [value expressions](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions) and evaluate the last operand in value expression context.

> Note
> 
> This can be used to force moving a value if really needed. For example, the following example fails on the call to `consume_self` because the struct was moved out of `s` in the block expression.
> 
> ```rust
> #![allow(unused)]
fn main() {
struct Struct;

impl Struct {
    fn consume_self(self) {}
    fn borrow_self(&self) {}
}

fn move_by_block_expression() {
    let s = Struct;

    // Move the value out of `s` in the block expression.
    (&{ s }).borrow_self();

    // Fails to execute because `s` is moved out of.
    s.consume_self();
}
}
> ```

## [`async` blocks](#async-blocks)

An *async block* is a variant of a block expression which evaluates to a future.

The final expression of the block, if present, determines the result value of the future.

Executing an async block is similar to executing a closure expression: its immediate effect is to produce and return an anonymous type.

Whereas closures return a type that implements one or more of the [`std::ops::Fn`](https://doc.rust-lang.org/core/ops/function/trait.Fn.html) traits, however, the type returned for an async block implements the [`std::future::Future`](https://doc.rust-lang.org/core/future/future/trait.Future.html) trait.

The actual data format for this type is unspecified.

> Note
> 
> The future type that rustc generates is roughly equivalent to an enum with one variant per `await` point, where each variant stores the data needed to resume from its corresponding point.

> 2018 Edition differences
> 
> Async blocks are only available beginning with Rust 2018.

### [Capture modes](#capture-modes)

Async blocks capture variables from their environment using the same [capture modes](https://doc.rust-lang.org/reference/types/closure.html#capture-modes) as closures. Like closures, when written `async { .. }` the capture mode for each variable will be inferred from the content of the block. `async move { .. }` blocks however will move all referenced variables into the resulting future.

[\[expr.block.async.context\]](#r-expr.block.async.context "expr.block.async.context")

### [Async context](#async-context)

Because async blocks construct a future, they define an **async context** which can in turn contain [`await` expressions](https://doc.rust-lang.org/reference/expressions/await-expr.html). Async contexts are established by async blocks as well as the bodies of async functions, whose semantics are defined in terms of async blocks.

### [Control-flow operators](#control-flow-operators)

Async blocks act like a function boundary, much like closures.

Therefore, the `?` operator and `return` expressions both affect the output of the future, not the enclosing function or other context. That is, `return <expr>` from within an async block will return the result of `<expr>` as the output of the future. Similarly, if `<expr>?` propagates an error, that error is propagated as the result of the future.

Finally, the `break` and `continue` keywords cannot be used to branch out from an async block. Therefore the following is illegal:

```rust
#![allow(unused)]
fn main() {
loop {
    async move {
        break; // error[E0267]: `break` inside of an `async` block
    }
}
}
```

## [`const` blocks](#const-blocks)

A *const block* is a variant of a block expression whose body evaluates at compile-time instead of at runtime.

[\[expr.block.const.context\]](#r-expr.block.const.context "expr.block.const.context")

Const blocks allows you to define a constant value without having to define new [constant items](https://doc.rust-lang.org/reference/items/constant-items.html), and thus they are also sometimes referred as *inline consts*. It also supports type inference so there is no need to specify the type, unlike [constant items](https://doc.rust-lang.org/reference/items/constant-items.html).

Const blocks have the ability to reference generic parameters in scope, unlike [free](https://doc.rust-lang.org/reference/glossary.html#free-item) constant items. They are desugared to constant items with generic parameters in scope (similar to associated constants, but without a trait or type they are associated with). For example, this code:

```rust
#![allow(unused)]
fn main() {
fn foo<T>() -> usize {
    const { std::mem::size_of::<T>() + 1 }
}
}
```

is equivalent to:

```rust
#![allow(unused)]
fn main() {
fn foo<T>() -> usize {
    {
        struct Const<T>(T);
        impl<T> Const<T> {
            const CONST: usize = std::mem::size_of::<T>() + 1;
        }
        Const::<T>::CONST
    }
}
}
```

If the const block expression is executed at runtime, then the constant is guaranteed to be evaluated, even if its return value is ignored:

```rust
#![allow(unused)]
fn main() {
fn foo<T>() -> usize {
    // If this code ever gets executed, then the assertion has definitely
    // been evaluated at compile-time.
    const { assert!(std::mem::size_of::<T>() > 0); }
    // Here we can have unsafe code relying on the type being non-zero-sized.
    /* ... */
    42
}
}
```

If the const block expression is not executed at runtime, it may or may not be evaluated:

```rust
#![allow(unused)]
fn main() {
if false {
    // The panic may or may not occur when the program is built.
    const { panic!(); }
}
}
```

## [`unsafe` blocks](#unsafe-blocks)

*See [`unsafe` blocks](https://doc.rust-lang.org/reference/unsafe-keyword.html#unsafe-blocks-unsafe-) for more information on when to use `unsafe`* .

A block of code can be prefixed with the `unsafe` keyword to permit [unsafe operations](https://doc.rust-lang.org/reference/unsafety.html). Examples:

```rust
#![allow(unused)]
fn main() {
unsafe {
    let b = [13u8, 17u8];
    let a = &b[0] as *const u8;
    assert_eq!(*a, 13);
    assert_eq!(*a.offset(1), 17);
}

unsafe fn an_unsafe_fn() -> i32 { 10 }
let a = unsafe { an_unsafe_fn() };
}
```

## [Labeled block expressions](#labeled-block-expressions)

Labeled block expressions are documented in the [Loops and other breakable expressions](https://doc.rust-lang.org/reference/expressions/loop-expr.html#r-expr.loop.block-labels) section.

## [Attributes on block expressions](#attributes-on-block-expressions)

[Inner attributes](https://doc.rust-lang.org/reference/attributes.html) are allowed directly after the opening brace of a block expression in the following situations:

- [Function](https://doc.rust-lang.org/reference/items/functions.html) and [method](https://doc.rust-lang.org/reference/items/associated-items.html#methods) bodies.
- Loop bodies ([`loop`](https://doc.rust-lang.org/reference/expressions/loop-expr.html#infinite-loops), [`while`](https://doc.rust-lang.org/reference/expressions/loop-expr.html#predicate-loops), and [`for`](https://doc.rust-lang.org/reference/expressions/loop-expr.html#iterator-loops)).
- Block expressions used as a [statement](https://doc.rust-lang.org/reference/statements.html).
- Block expressions as elements of [array expressions](https://doc.rust-lang.org/reference/expressions/array-expr.html), [tuple expressions](https://doc.rust-lang.org/reference/expressions/tuple-expr.html), [call expressions](https://doc.rust-lang.org/reference/expressions/call-expr.html), and tuple-style [struct](https://doc.rust-lang.org/reference/expressions/struct-expr.html) expressions.
- A block expression as the tail expression of another block expression.

The attributes that have meaning on a block expression are [`cfg`](https://doc.rust-lang.org/reference/conditional-compilation.html) and [the lint check attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes).

For example, this function returns `true` on unix platforms and `false` on other platforms.

```rust
#![allow(unused)]
fn main() {
fn is_unix_platform() -> bool {
    #[cfg(unix)] { true }
    #[cfg(not(unix))] { false }
}
}
```