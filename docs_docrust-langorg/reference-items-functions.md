---
title: Functions - The Rust Reference
url: https://doc.rust-lang.org/reference/items/functions.html#unwinding
source: crawler
fetched_at: 2026-05-06T21:25:12.559586516-03:00
rendered_js: false
word_count: 1648
summary: This document provides a technical specification for defining and using functions in the Rust programming language, covering syntax, parameters, generics, and ABI configuration.
tags:
    - rust
    - programming-language
    - functions
    - generics
    - abi
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Functions](#functions)

A *function* consists of a [block](https://doc.rust-lang.org/reference/expressions/block-expr.html) (that’s the *body* of the function), along with a name, a set of parameters, and an output type. Other than a name, all these are optional.

Functions are declared with the keyword `fn` which defines the given name in the [value namespace](https://doc.rust-lang.org/reference/names/namespaces.html) of the module or block where it is located.

Functions may declare a set of *input* [*variables*](https://doc.rust-lang.org/reference/variables.html) as parameters, through which the caller passes arguments into the function, and the *output* [*type*](https://doc.rust-lang.org/reference/types.html#type-expressions) of the value the function will return to its caller on completion.

If the output type is not explicitly stated, it is the [unit type](https://doc.rust-lang.org/reference/types/tuple.html).

When referred to, a *function* yields a first-class *value* of the corresponding zero-sized [*function item type*](https://doc.rust-lang.org/reference/types/function-item.html), which when called evaluates to a direct call to the function.

For example, this is a simple function:

```rust
#![allow(unused)]
fn main() {
fn answer_to_life_the_universe_and_everything() -> i32 {
    return 42;
}
}
```

The `safe` function is semantically only allowed when used in an [`extern` block](https://doc.rust-lang.org/reference/items/external-blocks.html).

## [Function parameters](#function-parameters)

Function parameters are irrefutable [patterns](https://doc.rust-lang.org/reference/patterns.html), so any pattern that is valid in an else-less `let` binding is also valid as a parameter:

```rust
#![allow(unused)]
fn main() {
fn first((value, _): (i32, i32)) -> i32 { value }
}
```

If the first parameter is a [SelfParam](https://doc.rust-lang.org/reference/items/functions.html#grammar-SelfParam), this indicates that the function is a [method](https://doc.rust-lang.org/reference/items/associated-items.html#methods).

Functions with a self parameter may only appear as an [associated function](https://doc.rust-lang.org/reference/items/associated-items.html#associated-functions-and-methods) in a [trait](https://doc.rust-lang.org/reference/items/traits.html) or [implementation](https://doc.rust-lang.org/reference/items/implementations.html).

A parameter with the `...` token indicates a [variadic function](https://doc.rust-lang.org/reference/items/external-blocks.html#variadic-functions), and may only be used as the last parameter of an [external block](https://doc.rust-lang.org/reference/items/external-blocks.html) function. The variadic parameter may have an optional identifier, such as `args: ...`.

## [Function body](#function-body)

The body block of a function is conceptually wrapped in another block that first binds the argument patterns and then `return`s the value of the function’s body. This means that the tail expression of the block, if evaluated, ends up being returned to the caller. As usual, an explicit return expression within the body of the function will short-cut that implicit return, if reached.

For example, the function above behaves as if it was written as:

```rust
// argument_0 is the actual first argument passed from the caller
let (value, _) = argument_0;
return {
    value
};
```

Functions without a body block are terminated with a semicolon. This form may only appear in a [trait](https://doc.rust-lang.org/reference/items/traits.html) or [external block](https://doc.rust-lang.org/reference/items/external-blocks.html).

## [Generic functions](#generic-functions)

A *generic function* allows one or more *parameterized types* to appear in its signature. Each type parameter must be explicitly declared in an angle-bracket-enclosed and comma-separated list, following the function name.

```rust
#![allow(unused)]
fn main() {
// foo is generic over A and B

fn foo<A, B>(x: A, y: B) {
}
}
```

Inside the function signature and body, the name of the type parameter can be used as a type name.

[Trait](https://doc.rust-lang.org/reference/items/traits.html) bounds can be specified for type parameters to allow methods with that trait to be called on values of that type. This is specified using the `where` syntax:

```rust
#![allow(unused)]
fn main() {
use std::fmt::Debug;
fn foo<T>(x: T) where T: Debug {
}
}
```

When a generic function is referenced, its type is instantiated based on the context of the reference. For example, calling the `foo` function here:

```rust
#![allow(unused)]
fn main() {
use std::fmt::Debug;

fn foo<T>(x: &[T]) where T: Debug {
    // details elided
}

foo(&[1, 2]);
}
```

will instantiate type parameter `T` with `i32`.

The type parameters can also be explicitly supplied in a trailing [path](https://doc.rust-lang.org/reference/paths.html) component after the function name. This might be necessary if there is not sufficient context to determine the type parameters. For example, `mem::size_of::<u32>() == 4`.

## [Extern function qualifier](#extern-function-qualifier)

The `extern` function qualifier allows providing function *definitions* that can be called with a particular ABI:

```rust
extern "ABI" fn foo() { /* ... */ }
```

These are often used in combination with [external block](https://doc.rust-lang.org/reference/items/external-blocks.html) items which provide function *declarations* that can be used to call functions without providing their *definition*:

```rust
unsafe extern "ABI" {
  unsafe fn foo(); /* no body */
  safe fn bar(); /* no body */
}
unsafe { foo() };
bar();
```

When `"extern" Abi?*` is omitted from `FunctionQualifiers` in function items, the ABI `"Rust"` is assigned. For example:

```rust
#![allow(unused)]
fn main() {
fn foo() {}
}
```

is equivalent to:

```rust
#![allow(unused)]
fn main() {
extern "Rust" fn foo() {}
}
```

Functions can be called by foreign code, and using an ABI that differs from Rust allows, for example, to provide functions that can be called from other programming languages like C:

```rust
#![allow(unused)]
fn main() {
// Declares a function with the "C" ABI
extern "C" fn new_i32() -> i32 { 0 }

// Declares a function with the "stdcall" ABI
#[cfg(any(windows, target_arch = "x86"))]
extern "stdcall" fn new_i32_stdcall() -> i32 { 0 }
}
```

Just as with [external block](https://doc.rust-lang.org/reference/items/external-blocks.html), when the `extern` keyword is used and the `"ABI"` is omitted, the ABI used defaults to `"C"`. That is, this:

```rust
#![allow(unused)]
fn main() {
extern fn new_i32() -> i32 { 0 }
let fptr: extern fn() -> i32 = new_i32;
}
```

is equivalent to:

```rust
#![allow(unused)]
fn main() {
extern "C" fn new_i32() -> i32 { 0 }
let fptr: extern "C" fn() -> i32 = new_i32;
}
```

### [Unwinding](#unwinding)

Most ABI strings come in two variants, one with an `-unwind` suffix and one without. The `Rust` ABI always permits unwinding, so there is no `Rust-unwind` ABI. The choice of ABI, together with the runtime [panic handler](https://doc.rust-lang.org/reference/panic.html#the-panic_handler-attribute), determines the behavior when unwinding out of a function.

The table below indicates the behavior of an unwinding operation reaching each type of ABI boundary (function declaration or definition using the corresponding ABI string). Note that the Rust runtime is not affected by, and cannot have an effect on, any unwinding that occurs entirely within another language’s runtime, that is, unwinds that are thrown and caught without reaching a Rust ABI boundary.

The `panic`-unwind column refers to [panicking](https://doc.rust-lang.org/reference/panic.html) via the `panic!` macro and similar standard library mechanisms, as well as to any other Rust operations that cause a panic, such as out-of-bounds array indexing or integer overflow.

The “unwinding” ABI category refers to `"Rust"` (the implicit ABI of Rust functions not marked `extern`), `"C-unwind"`, and any other ABI with `-unwind` in its name. The “non-unwinding” ABI category refers to all other ABI strings, including `"C"` and `"stdcall"`.

Native unwinding is defined per-target. On targets that support throwing and catching C++ exceptions, it refers to the mechanism used to implement this feature. Some platforms implement a form of unwinding referred to as [“forced unwinding”](https://rust-lang.github.io/rfcs/2945-c-unwind-abi.html#forced-unwinding); `longjmp` on Windows and `pthread_exit` in `glibc` are implemented this way. Forced unwinding is explicitly excluded from the “Native unwind” column in the table.

panic runtimeABI`panic`-unwindNative unwind (unforced) `panic=unwind`unwindingunwindunwind `panic=unwind`non-unwindingabort (see notes below)[undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) `panic=abort`unwinding`panic` aborts without unwindingabort `panic=abort`non-unwinding`panic` aborts without unwinding[undefined behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html)

With `panic=unwind`, when a `panic` is turned into an abort by a non-unwinding ABI boundary, either no destructors (`Drop` calls) will run, or all destructors up until the ABI boundary will run. It is unspecified which of those two behaviors will happen.

For other considerations and limitations regarding unwinding across FFI boundaries, see the [relevant section in the Panic documentation](https://doc.rust-lang.org/reference/panic.html#unwinding-across-ffi-boundaries).

## [Const functions](#const-functions)

See [const functions](https://doc.rust-lang.org/reference/const_eval.html#const-functions) for the definition of const functions.

## [Async functions](#async-functions)

Functions may be qualified as async, and this can also be combined with the `unsafe` qualifier:

```rust
#![allow(unused)]
fn main() {
async fn regular_example() { }
async unsafe fn unsafe_example() { }
}
```

Async functions do no work when called: instead, they capture their arguments into a future. When polled, that future will execute the function’s body.

An async function is roughly equivalent to a function that returns [`impl Future`](https://doc.rust-lang.org/reference/types/impl-trait.html) and with an [`async move` block](https://doc.rust-lang.org/reference/expressions/block-expr.html#async-blocks) as its body:

```rust
#![allow(unused)]
fn main() {
// Source
async fn example(x: &str) -> usize {
    x.len()
}
}
```

is roughly equivalent to:

```rust
#![allow(unused)]
fn main() {
use std::future::Future;
// Desugared
fn example<'a>(x: &'a str) -> impl Future<Output = usize> + 'a {
    async move { x.len() }
}
}
```

The actual desugaring is more complex:

- The return type in the desugaring is assumed to capture all lifetime parameters from the `async fn` declaration. This can be seen in the desugared example above, which explicitly outlives, and hence captures, `'a`.

<!--THE END-->

- The [`async move` block](https://doc.rust-lang.org/reference/expressions/block-expr.html#async-blocks) in the body captures all function parameters, including those that are unused or bound to a `_` pattern. This ensures that function parameters are dropped in the same order as they would be if the function were not async, except that the drop occurs when the returned future has been fully awaited.

For more information on the effect of async, see [`async` blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#async-blocks).

> 2018 Edition differences
> 
> Async functions are only available beginning with Rust 2018.

### [Combining `async` and `unsafe`](#combining-async-and-unsafe)

It is legal to declare a function that is both async and unsafe. The resulting function is unsafe to call and (like any async function) returns a future. This future is just an ordinary future and thus an `unsafe` context is not required to “await” it:

```rust
#![allow(unused)]
fn main() {
// Returns a future that, when awaited, dereferences `x`.
//
// Soundness condition: `x` must be safe to dereference until
// the resulting future is complete.
async unsafe fn unsafe_example(x: *const i32) -> i32 {
  *x
}

async fn safe_example() {
    // An `unsafe` block is required to invoke the function initially:
    let p = 22;
    let future = unsafe { unsafe_example(&p) };

    // But no `unsafe` block required here. This will
    // read the value of `p`:
    let q = future.await;
}
}
```

Note that this behavior is a consequence of the desugaring to a function that returns an `impl Future` – in this case, the function we desugar to is an `unsafe` function, but the return value remains the same.

Unsafe is used on an async function in precisely the same way that it is used on other functions: it indicates that the function imposes some additional obligations on its caller to ensure soundness. As in any other unsafe function, these conditions may extend beyond the initial call itself – in the snippet above, for example, the `unsafe_example` function took a pointer `x` as argument, and then (when awaited) dereferenced that pointer. This implies that `x` would have to be valid until the future is finished executing, and it is the caller’s responsibility to ensure that.

## [Attributes on functions](#attributes-on-functions)

[Outer attributes](https://doc.rust-lang.org/reference/attributes.html) are allowed on functions. [Inner attributes](https://doc.rust-lang.org/reference/attributes.html) are allowed directly after the `{` inside its body [block](https://doc.rust-lang.org/reference/expressions/block-expr.html).

This example shows an inner attribute on a function. The function is documented with just the word “Example”.

```rust
#![allow(unused)]
fn main() {
fn documented() {
    #![doc = "Example"]
}
}
```

> Note
> 
> Except for lints, it is idiomatic to only use outer attributes on function items.

The attributes that have meaning on a function are:

- [`cfg_attr`](https://doc.rust-lang.org/reference/conditional-compilation.html#the-cfg_attr-attribute)
- [`cfg`](https://doc.rust-lang.org/reference/conditional-compilation.html#the-cfg-attribute)
- [`cold`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-cold-attribute)
- [`deprecated`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-deprecated-attribute)
- [`doc`](https://doc.rust-lang.org/rustdoc/the-doc-attribute.html)
- [`export_name`](https://doc.rust-lang.org/reference/abi.html#the-export_name-attribute)
- [`inline`](https://doc.rust-lang.org/reference/attributes/codegen.html#the-inline-attribute)
- [`link_section`](https://doc.rust-lang.org/reference/abi.html#the-link_section-attribute)
- [`must_use`](https://doc.rust-lang.org/reference/attributes/diagnostics.html#the-must_use-attribute)
- [`no_mangle`](https://doc.rust-lang.org/reference/abi.html#the-no_mangle-attribute)
- [Lint check attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes)
- [Procedural macro attributes](https://doc.rust-lang.org/reference/procedural-macros.html#r-macro.proc.attribute)
- [Testing attributes](https://doc.rust-lang.org/reference/attributes/testing.html)

## [Attributes on function parameters](#attributes-on-function-parameters)

[Outer attributes](https://doc.rust-lang.org/reference/attributes.html) are allowed on function parameters and the permitted [built-in attributes](https://doc.rust-lang.org/reference/attributes.html#built-in-attributes-index) are restricted to `cfg`, `cfg_attr`, `allow`, `warn`, `deny`, and `forbid`.

```rust
#![allow(unused)]
fn main() {
fn len(
    #[cfg(windows)] slice: &[u16],
    #[cfg(not(windows))] slice: &[u8],
) -> usize {
    slice.len()
}
}
```

Inert helper attributes used by procedural macro attributes applied to items are also allowed but be careful to not include these inert attributes in your final `TokenStream`.

For example, the following code defines an inert `some_inert_attribute` attribute that is not formally defined anywhere and the `some_proc_macro_attribute` procedural macro is responsible for detecting its presence and removing it from the output token stream.

```rust
#[some_proc_macro_attribute]
fn foo_oof(#[some_inert_attribute] arg: u8) {
}
```

* * *

1. The `async` qualifier is not allowed in the 2015 edition. [↩](#fr-async-edition-1)
2. *Relevant to editions earlier than Rust 2024*: Within `extern` blocks, the `safe` or `unsafe` function qualifier is only allowed when the `extern` is qualified as `unsafe`. [↩](#fr-extern-qualifiers-1)
3. The `safe` function qualifier is only allowed semantically within `extern` blocks. [↩](#fr-extern-safe-1)
4. Function parameters with only a type are only allowed in an associated function of a [trait item](https://doc.rust-lang.org/reference/items/traits.html) in the 2015 edition. [↩](#fr-fn-param-2015-1)