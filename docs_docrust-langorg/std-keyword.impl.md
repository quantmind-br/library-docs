---
title: impl - Rust
url: https://doc.rust-lang.org/std/keyword.impl.html
source: crawler
fetched_at: 2026-05-06T21:32:39.161758004-03:00
rendered_js: false
word_count: 278
summary: This document explains the usage of the Rust 'impl' keyword for defining inherent implementations, implementing traits for types, and utilizing 'impl Trait' syntax for type abstraction.
tags:
    - rust
    - programming-language
    - trait-implementation
    - method-syntax
    - impl-trait
    - type-systems
category: concept
---

Expand description

Implementations of functionality for a type, or a type implementing some functionality.

There are two uses of the keyword `impl`:

- An `impl` block is an item that is used to implement some functionality for a type.
- An `impl Trait` in a type-position can be used to designate a type that implements a trait called `Trait`.

## [§](#implementing-functionality-for-a-type)Implementing Functionality for a Type

The `impl` keyword is primarily used to define implementations on types. Inherent implementations are standalone, while trait implementations are used to implement traits for types, or other traits.

An implementation consists of definitions of functions and consts. A function defined in an `impl` block can be standalone, meaning it would be called like `Vec::new()`. If the function takes `self`, `&self`, or `&mut self` as its first argument, it can also be called using method-call syntax, a familiar feature to any object-oriented programmer, like `vec.len()`.

### [§](#inherent-implementations)Inherent Implementations

```rust
struct Example {
    number: i32,
}

impl Example {
    fn boo() {
        println!("boo! Example::boo() was called!");
    }

    fn answer(&mut self) {
        self.number += 42;
    }

    fn get_number(&self) -> i32 {
        self.number
    }
}
```

It matters little where an inherent implementation is defined; its functionality is in scope wherever its implementing type is.

### [§](#trait-implementations-1)Trait Implementations

```rust
struct Example {
    number: i32,
}

trait Thingy {
    fn do_thingy(&self);
}

impl Thingy for Example {
    fn do_thingy(&self) {
        println!("doing a thing! also, number is {}!", self.number);
    }
}
```

It matters little where a trait implementation is defined; its functionality can be brought into scope by importing the trait it implements.

For more information on implementations, see the [Rust book](https://doc.rust-lang.org/book/ch05-03-method-syntax.html) or the [Reference](https://doc.rust-lang.org/reference/items/implementations.html).

## [§](#designating-a-type-that-implements-some-functionality)Designating a Type that Implements Some Functionality

The other use of the `impl` keyword is in `impl Trait` syntax, which can be understood to mean “any (or some) concrete type that implements Trait”. It can be used as the type of a variable declaration, in [argument position](https://rust-lang.github.io/rfcs/1951-expand-impl-trait.html) or in [return position](https://rust-lang.github.io/rfcs/3425-return-position-impl-trait-in-traits.html). One pertinent use case is in working with closures, which have unnameable types.

```rust
fn thing_returning_closure() -> impl Fn(i32) -> bool {
    println!("here's a closure for you!");
    |x: i32| x % 3 == 0
}
```

For more information on `impl Trait` syntax, see the [Rust book](https://doc.rust-lang.org/book/ch10-02-traits.html#returning-types-that-implement-traits).