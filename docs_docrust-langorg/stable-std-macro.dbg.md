---
title: dbg in std - Rust
url: https://doc.rust-lang.org/stable/std/macro.dbg.html
source: crawler
fetched_at: 2026-05-06T21:21:58.236181126-03:00
rendered_js: false
word_count: 351
summary: This document describes the Rust standard library's dbg! macro, which is used for printing the value, source location, and code representation of expressions to stderr during debugging.
tags:
    - rust
    - debugging
    - macro
    - stderr
    - development-tools
category: reference
---

## Macro dbg

1.32.0 · [Source](https://doc.rust-lang.org/stable/src/std/macros.rs.html#352-381)

```rust
macro_rules! dbg {
    () => { ... };
    ($val:expr $(,)?) => { ... };
    ($($val:expr),+ $(,)?) => { ... };
}
```

Expand description

Prints and returns the value of a given expression for quick and dirty debugging.

An example:

```rust
let a = 2;
let b = dbg!(a * 2) + 1;
//      ^-- prints: [src/main.rs:2:9] a * 2 = 4
assert_eq!(b, 5);
```

The macro works by using the `Debug` implementation of the type of the given expression to print the value to [stderr](https://en.wikipedia.org/wiki/Standard_streams#Standard_error_%28stderr%29) along with the source location of the macro invocation as well as the source code of the expression.

Invoking the macro on an expression moves and takes ownership of it before returning the evaluated expression unchanged. If the type of the expression does not implement `Copy` and you don’t want to give up ownership, you can instead borrow with `dbg!(&expr)` for some expression `expr`.

The `dbg!` macro works exactly the same in release builds. This is useful when debugging issues that only occur in release builds or when debugging in release mode is significantly faster.

Note that the macro is intended as a debugging tool and therefore you should avoid having uses of it in version control for long periods (other than in tests and similar). Debug output from production code is better done with other facilities such as the [`debug!`](https://docs.rs/log/*/log/macro.debug.html) macro from the [`log`](https://crates.io/crates/log) crate.

## [§](#stability)Stability

The exact output printed by this macro should not be relied upon and is subject to future changes.

## [§](#panics)Panics

Panics if writing to `io::stderr` fails.

## [§](#further-examples)Further examples

With a method call:

```rust
fn foo(n: usize) {
    if let Some(_) = dbg!(n.checked_sub(4)) {
        // ...
    }
}

foo(3)
```

This prints to [stderr](https://en.wikipedia.org/wiki/Standard_streams#Standard_error_%28stderr%29):

```text
[src/main.rs:2:22] n.checked_sub(4) = None
```

Naive factorial implementation:

```rust
fn factorial(n: u32) -> u32 {
    if dbg!(n <= 1) {
        dbg!(1)
    } else {
        dbg!(n * factorial(n - 1))
    }
}

dbg!(factorial(4));
```

This prints to [stderr](https://en.wikipedia.org/wiki/Standard_streams#Standard_error_%28stderr%29):

```text
[src/main.rs:2:8] n <= 1 = false
[src/main.rs:2:8] n <= 1 = false
[src/main.rs:2:8] n <= 1 = false
[src/main.rs:2:8] n <= 1 = true
[src/main.rs:3:9] 1 = 1
[src/main.rs:7:9] n * factorial(n - 1) = 2
[src/main.rs:7:9] n * factorial(n - 1) = 6
[src/main.rs:7:9] n * factorial(n - 1) = 24
[src/main.rs:9:1] factorial(4) = 24
```

The `dbg!(..)` macro moves the input:

[ⓘ](# "This example deliberately fails to compile")

```rust
/// A wrapper around `usize` which importantly is not Copyable.
#[derive(Debug)]
struct NoCopy(usize);

let a = NoCopy(42);
let _ = dbg!(a); // <-- `a` is moved here.
let _ = dbg!(a); // <-- `a` is moved again; error!
```

You can also use `dbg!()` without a value to just print the file and line whenever it’s reached.

Finally, if you want to `dbg!(..)` multiple values, it will treat them as a tuple (and return it, too):

```rust
assert_eq!(dbg!(1usize, 2u32), (1, 2));
```

However, a single argument with a trailing comma will still not be treated as a tuple, following the convention of ignoring trailing commas in macro invocations. You can use a 1-tuple directly if you need one:

```rust
assert_eq!(1, dbg!(1u32,)); // trailing comma ignored
assert_eq!((1,), dbg!((1u32,))); // 1-tuple
```