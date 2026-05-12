---
title: std::alloc - Rust
url: https://doc.rust-lang.org/stable/std/alloc/index.html
source: crawler
fetched_at: 2026-05-06T21:28:20.78063164-03:00
rendered_js: false
word_count: 313
summary: This document outlines the Rust memory allocation API, providing instructions on how to define and register a custom global memory allocator using the global_allocator attribute.
tags:
    - rust
    - memory-management
    - allocator
    - global-allocator
    - systems-programming
category: reference
---

## Module alloc

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/std/alloc.rs.html#1-490)

Expand description

Memory allocation APIs.

In a given program, the standard library has one “global” memory allocator that is used for example by `Box<T>` and `Vec<T>`.

Currently the default global allocator is unspecified. Libraries, however, like `cdylib`s and `staticlib`s are guaranteed to use the [`System`](https://doc.rust-lang.org/stable/std/alloc/struct.System.html "struct std::alloc::System") by default.

## [§](#the-global_allocator-attribute)The `#[global_allocator]` attribute

This attribute allows configuring the choice of global allocator. You can use this to implement a completely custom global allocator to route all[1](#fn1) default allocation requests to a custom object.

```rust
use std::alloc::{GlobalAlloc, System, Layout};

struct MyAllocator;

unsafe impl GlobalAlloc for MyAllocator {
    unsafe fn alloc(&self, layout: Layout) -> *mut u8 {
        unsafe { System.alloc(layout) }
    }

    unsafe fn dealloc(&self, ptr: *mut u8, layout: Layout) {
        unsafe { System.dealloc(ptr, layout) }
    }
}

#[global_allocator]
static GLOBAL: MyAllocator = MyAllocator;

fn main() {
    // This `Vec` will allocate memory through `GLOBAL` above
    let mut v = Vec::new();
    v.push(1);
}
```

The attribute is used on a `static` item whose type implements the [`GlobalAlloc`](https://doc.rust-lang.org/stable/std/alloc/trait.GlobalAlloc.html "trait std::alloc::GlobalAlloc") trait. This type can be provided by an external library:

[ⓘ](# "This example is not tested")

```rust
use jemallocator::Jemalloc;

#[global_allocator]
static GLOBAL: Jemalloc = Jemalloc;

fn main() {}
```

The `#[global_allocator]` can only be used once in a crate or its recursive dependencies.

[Layout](https://doc.rust-lang.org/stable/std/alloc/struct.Layout.html "struct std::alloc::Layout")

Layout of a block of memory.

[LayoutError](https://doc.rust-lang.org/stable/std/alloc/struct.LayoutError.html "struct std::alloc::LayoutError")

The `LayoutError` is returned when the parameters given to `Layout::from_size_align` or some other `Layout` constructor do not satisfy its documented constraints.

[System](https://doc.rust-lang.org/stable/std/alloc/struct.System.html "struct std::alloc::System")

The default memory allocator provided by the operating system.

[AllocError](https://doc.rust-lang.org/stable/std/alloc/struct.AllocError.html "struct std::alloc::AllocError")Experimental

The `AllocError` error indicates an allocation failure that may be due to resource exhaustion or to something wrong when combining the given input arguments with this allocator.

[Global](https://doc.rust-lang.org/stable/std/alloc/struct.Global.html "struct std::alloc::Global")Experimental

The global memory allocator.

[GlobalAlloc](https://doc.rust-lang.org/stable/std/alloc/trait.GlobalAlloc.html "trait std::alloc::GlobalAlloc")

A memory allocator that can be registered as the standard library’s default through the `#[global_allocator]` attribute.

[Allocator](https://doc.rust-lang.org/stable/std/alloc/trait.Allocator.html "trait std::alloc::Allocator")Experimental

An implementation of `Allocator` can allocate, grow, shrink, and deallocate arbitrary blocks of data described via [`Layout`](https://doc.rust-lang.org/stable/std/alloc/struct.Layout.html "struct std::alloc::Layout").

[alloc](https://doc.rust-lang.org/stable/std/alloc/fn.alloc.html "fn std::alloc::alloc")⚠

Allocates memory with the global allocator.

[alloc\_zeroed](https://doc.rust-lang.org/stable/std/alloc/fn.alloc_zeroed.html "fn std::alloc::alloc_zeroed")⚠

Allocates zero-initialized memory with the global allocator.

[dealloc](https://doc.rust-lang.org/stable/std/alloc/fn.dealloc.html "fn std::alloc::dealloc")⚠

Deallocates memory with the global allocator.

[handle\_alloc\_error](https://doc.rust-lang.org/stable/std/alloc/fn.handle_alloc_error.html "fn std::alloc::handle_alloc_error")

Signals a memory allocation error.

[realloc](https://doc.rust-lang.org/stable/std/alloc/fn.realloc.html "fn std::alloc::realloc")⚠

Reallocates memory with the global allocator.

[set\_alloc\_error\_hook](https://doc.rust-lang.org/stable/std/alloc/fn.set_alloc_error_hook.html "fn std::alloc::set_alloc_error_hook")Experimental

Registers a custom allocation error hook, replacing any that was previously registered.

[take\_alloc\_error\_hook](https://doc.rust-lang.org/stable/std/alloc/fn.take_alloc_error_hook.html "fn std::alloc::take_alloc_error_hook")Experimental

Unregisters the current allocation error hook, returning it.

[LayoutErr](https://doc.rust-lang.org/stable/std/alloc/type.LayoutErr.html "type std::alloc::LayoutErr")Deprecated