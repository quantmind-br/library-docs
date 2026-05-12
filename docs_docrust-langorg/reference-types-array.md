---
title: Array types - The Rust Reference
url: https://doc.rust-lang.org/reference/types/array.html
source: crawler
fetched_at: 2026-05-06T21:27:00.97273061-03:00
rendered_js: false
word_count: 100
summary: This document defines the syntax and properties of fixed-size array types in the Rust programming language.
tags:
    - rust
    - data-types
    - arrays
    - fixed-size-sequence
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Array types](#array-types)

An array is a fixed-size sequence of `N` elements of type `T`. The array type is written as `[T; N]`.

The size is a [constant expression](https://doc.rust-lang.org/reference/const_eval.html#constant-expressions) that evaluates to a [`usize`](https://doc.rust-lang.org/reference/types/numeric.html#machine-dependent-integer-types).

Examples:

```rust
#![allow(unused)]
fn main() {
// A stack-allocated array
let array: [i32; 3] = [1, 2, 3];

// A heap-allocated array, coerced to a slice
let boxed_array: Box<[i32]> = Box::new([1, 2, 3]);
}
```

All elements of arrays are always initialized, and access to an array is always bounds-checked in safe methods and operators.

> Note
> 
> The [`Vec<T>`](https://doc.rust-lang.org/alloc/vec/struct.Vec.html) standard library type provides a heap-allocated resizable array type.