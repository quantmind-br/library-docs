---
title: Constant items - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/items/constant-items.html
source: crawler
fetched_at: 2026-05-06T21:26:47.367504069-03:00
rendered_js: false
word_count: 279
summary: This document defines constant items in the Rust programming language, explaining their behavior regarding inlining, lifetime requirements, destructors, and compile-time evaluation.
tags:
    - rust-programming
    - constant-items
    - compile-time-evaluation
    - static-lifetime
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Constant items](#constant-items)

A *constant item* is an optionally named [*constant value*](https://doc.rust-lang.org/stable/reference/const_eval.html#constant-expressions) which is not associated with a specific memory location in the program.

Constants are essentially inlined wherever they are used, meaning that they are copied directly into the relevant context when used. This includes usage of constants from external crates, and non-[`Copy`](https://doc.rust-lang.org/stable/reference/special-types-and-traits.html#copy) types. References to the same constant are not necessarily guaranteed to refer to the same memory address.

The constant declaration defines the constant value in the [value namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html) of the module or block where it is located.

Constants must be explicitly typed. The type must have a `'static` lifetime: any references in the initializer must have `'static` lifetimes. References in the type of a constant default to `'static` lifetime; see [static lifetime elision](https://doc.rust-lang.org/stable/reference/lifetime-elision.html#const-and-static-elision).

A reference to a constant will have `'static` lifetime if the constant value is eligible for [promotion](https://doc.rust-lang.org/stable/reference/destructors.html#r-destructors.scope.const-promotion); otherwise, a temporary will be created.

```rust
#![allow(unused)]
fn main() {
const BIT1: u32 = 1 << 0;
const BIT2: u32 = 1 << 1;

const BITS: [u32; 2] = [BIT1, BIT2];
const STRING: &'static str = "bitstring";

struct BitsNStrings<'a> {
    mybits: [u32; 2],
    mystring: &'a str,
}

const BITS_N_STRINGS: BitsNStrings<'static> = BitsNStrings {
    mybits: BITS,
    mystring: STRING,
};
}
```

The constant expression may only be omitted in a [trait definition](https://doc.rust-lang.org/stable/reference/items/traits.html).

## [Constants with destructors](#constants-with-destructors)

Constants can contain destructors. Destructors are run when the value goes out of scope.

```rust
#![allow(unused)]
fn main() {
struct TypeWithDestructor(i32);

impl Drop for TypeWithDestructor {
    fn drop(&mut self) {
        println!("Dropped. Held {}.", self.0);
    }
}

const ZERO_WITH_DESTRUCTOR: TypeWithDestructor = TypeWithDestructor(0);

fn create_and_drop_zero_with_destructor() {
    let x = ZERO_WITH_DESTRUCTOR;
    // x gets dropped at end of function, calling drop.
    // prints "Dropped. Held 0.".
}
}
```

## [Unnamed constant](#unnamed-constant)

Unlike an [associated constant](https://doc.rust-lang.org/stable/reference/items/associated-items.html#associated-constants), a [free](https://doc.rust-lang.org/stable/reference/glossary.html#free-item) constant may be unnamed by using an underscore instead of the name. For example:

```rust
#![allow(unused)]
fn main() {
const _: () =  { struct _SameNameTwice; };

// OK although it is the same name as above:
const _: () =  { struct _SameNameTwice; };
}
```

As with [underscore imports](https://doc.rust-lang.org/stable/reference/items/use-declarations.html#underscore-imports), macros may safely emit the same unnamed constant in the same scope more than once. For example, the following should not produce an error:

```rust
#![allow(unused)]
fn main() {
macro_rules! m {
    ($item: item) => { $item $item }
}

m!(const _: () = (););
// This expands to:
// const _: () = ();
// const _: () = ();
}
```

## [Evaluation](#evaluation)

[Free](https://doc.rust-lang.org/stable/reference/glossary.html#free-item) constants are always [evaluated](https://doc.rust-lang.org/stable/reference/const_eval.html) at compile-time to surface panics. This happens even within an unused function:

```rust
#![allow(unused)]
fn main() {
// Compile-time panic
const PANIC: () = std::unimplemented!();

fn unused_generic_function<T>() {
    // A failing compile-time assertion
    const _: () = assert!(usize::BITS == 0);
}
}
```