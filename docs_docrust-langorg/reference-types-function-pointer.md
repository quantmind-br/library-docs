---
title: Function pointer types - The Rust Reference
url: https://doc.rust-lang.org/reference/types/function-pointer.html
source: crawler
fetched_at: 2026-05-06T21:38:49.754115579-03:00
rendered_js: false
word_count: 144
summary: This document defines the syntax and behavioral characteristics of function pointer types in the Rust programming language, including support for unsafe and extern qualifiers.
tags:
    - rust
    - function-pointers
    - type-system
    - programming-languages
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Function pointer types](#function-pointer-types)

A function pointer type, written using the `fn` keyword, refers to a function whose identity is not necessarily known at compile-time.

An example where `Binop` is defined as a function pointer type:

```rust
#![allow(unused)]
fn main() {
fn add(x: i32, y: i32) -> i32 {
    x + y
}

let mut x = add(5,7);

type Binop = fn(i32, i32) -> i32;
let bo: Binop = add;
x = bo(5,7);
}
```

Function pointers can be created via a coercion from both [function items](https://doc.rust-lang.org/reference/types/function-item.html) and non-capturing, non-async [closures](https://doc.rust-lang.org/reference/types/closure.html).

The `unsafe` qualifier indicates that the type’s value is an [unsafe function](https://doc.rust-lang.org/reference/unsafe-keyword.html), and the `extern` qualifier indicates it is an [extern function](https://doc.rust-lang.org/reference/items/functions.html#extern-function-qualifier).

For the function to be variadic, its `extern` ABI must be one of those listed in [items.extern.variadic.conventions](https://doc.rust-lang.org/reference/items/external-blocks.html#r-items.extern.variadic.conventions).

## [Attributes on function pointer parameters](#attributes-on-function-pointer-parameters)

Attributes on function pointer parameters follow the same rules and restrictions as [regular function parameters](https://doc.rust-lang.org/reference/items/functions.html#attributes-on-function-parameters).