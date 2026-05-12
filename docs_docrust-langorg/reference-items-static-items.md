---
title: Static items - The Rust Reference
url: https://doc.rust-lang.org/reference/items/static-items.html#grammar-StaticItem
source: crawler
fetched_at: 2026-05-06T21:25:08.385563175-03:00
rendered_js: false
word_count: 677
summary: This document explains the definition, lifetime, and usage rules of static items in the Rust programming language, including distinctions between constant and mutable static declarations.
tags:
    - rust
    - static-items
    - memory-management
    - programming-language-reference
    - mutable-statics
    - concurrency-safety
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Static items](#static-items)

A *static item* is similar to a [constant](https://doc.rust-lang.org/reference/items/constant-items.html), except that it represents an allocation in the program that is initialized with the initializer expression. All references and raw pointers to the static refer to the same allocation.

Static items have the `static` lifetime, which outlives all other lifetimes in a Rust program. Static items do not call [`drop`](https://doc.rust-lang.org/reference/destructors.html) at the end of the program.

If the `static` has a size of at least 1 byte, this allocation is disjoint from all other such `static` allocations as well as heap allocations and stack-allocated variables. However, the storage of immutable `static` items can overlap with allocations that do not themselves have a unique address, such as [promoteds](https://doc.rust-lang.org/reference/destructors.html#constant-promotion) and [`const` items](https://doc.rust-lang.org/reference/items/constant-items.html).

The static declaration defines a static value in the [value namespace](https://doc.rust-lang.org/reference/names/namespaces.html) of the module or block where it is located.

The static initializer is a [constant expression](https://doc.rust-lang.org/reference/const_eval.html#constant-expressions) evaluated at compile time. Static initializers may refer to and read from other statics. When reading from mutable statics, they read the initial value of that static.

Non-`mut` static items that contain a type that is not [interior mutable](https://doc.rust-lang.org/reference/interior-mutability.html) may be placed in read-only memory.

All access to a static is safe, but there are a number of restrictions on statics:

- The type must have the [`Sync`](https://doc.rust-lang.org/core/marker/trait.Sync.html) trait bound to allow thread-safe access.

The initializer expression must be omitted in an [external block](https://doc.rust-lang.org/reference/items/external-blocks.html), and must be provided for free static items.

The `safe` and `unsafe` qualifiers are semantically only allowed when used in an [external block](https://doc.rust-lang.org/reference/items/external-blocks.html).

## [Statics & generics](#statics--generics)

A static item defined in a generic scope (for example in a blanket or default implementation) will result in exactly one static item being defined, as if the static definition was pulled out of the current scope into the module. There will *not* be one item per monomorphization.

This code:

```rust
use std::sync::atomic::{AtomicUsize, Ordering};

trait Tr {
    fn default_impl() {
        static COUNTER: AtomicUsize = AtomicUsize::new(0);
        println!("default_impl: counter was {}", COUNTER.fetch_add(1, Ordering::Relaxed));
    }

    fn blanket_impl();
}

struct Ty1 {}
struct Ty2 {}

impl<T> Tr for T {
    fn blanket_impl() {
        static COUNTER: AtomicUsize = AtomicUsize::new(0);
        println!("blanket_impl: counter was {}", COUNTER.fetch_add(1, Ordering::Relaxed));
    }
}

fn main() {
    <Ty1 as Tr>::default_impl();
    <Ty2 as Tr>::default_impl();
    <Ty1 as Tr>::blanket_impl();
    <Ty2 as Tr>::blanket_impl();
}
```

prints

```text
default_impl: counter was 0
default_impl: counter was 1
blanket_impl: counter was 0
blanket_impl: counter was 1
```

## [Mutable statics](#mutable-statics)

If a static item is declared with the `mut` keyword, then it is allowed to be modified by the program. One of Rust’s goals is to make concurrency bugs hard to run into, and this is obviously a very large source of race conditions or other bugs.

For this reason, an `unsafe` block is required when either reading or writing a mutable static variable. Care should be taken to ensure that modifications to a mutable static are safe with respect to other threads running in the same process.

Mutable statics are still very useful, however. They can be used with C libraries and can also be bound from C libraries in an `extern` block.

```rust
#![allow(unused)]
fn main() {
fn atomic_add(_: *mut u32, _: u32) -> u32 { 2 }

static mut LEVELS: u32 = 0;

// This violates the idea of no shared state, and this doesn't internally
// protect against races, so this function is `unsafe`
unsafe fn bump_levels_unsafe() -> u32 {
    unsafe {
        let ret = LEVELS;
        LEVELS += 1;
        return ret;
    }
}

// As an alternative to `bump_levels_unsafe`, this function is safe, assuming
// that we have an atomic_add function which returns the old value. This
// function is safe only if no other code accesses the static in a non-atomic
// fashion. If such accesses are possible (such as in `bump_levels_unsafe`),
// then this would need to be `unsafe` to indicate to the caller that they
// must still guard against concurrent access.
fn bump_levels_safe() -> u32 {
    unsafe {
        return atomic_add(&raw mut LEVELS, 1);
    }
}
}
```

Mutable statics have the same restrictions as normal statics, except that the type does not have to implement the `Sync` trait.

## [Using statics or consts](#using-statics-or-consts)

It can be confusing whether or not you should use a constant item or a static item. Constants should, in general, be preferred over statics unless one of the following are true:

- Large amounts of data are being stored.
- The single-address property of statics is required.
- Interior mutability is required.

* * *

1. The `safe` and `unsafe` function qualifiers are only allowed semantically within `extern` blocks. [↩](#fr-extern-safety-1)