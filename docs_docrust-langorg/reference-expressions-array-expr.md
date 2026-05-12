---
title: Array and index expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/array-expr.html
source: crawler
fetched_at: 2026-05-06T21:26:54.989665151-03:00
rendered_js: false
word_count: 455
summary: This document explains the syntax and behavior of array construction expressions and indexing operations within the Rust programming language.
tags:
    - rust
    - arrays
    - indexing
    - language-reference
    - syntax
    - memory-access
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Array and array index expressions](#array-and-array-index-expressions)

## [Array expressions](#array-expressions)

*Array expressions* construct [arrays](https://doc.rust-lang.org/reference/types/array.html). Array expressions come in two forms.

The first form lists out every value in the array.

The syntax for this form is a comma-separated list of expressions of uniform type enclosed in square brackets.

This produces an array containing each of these values in the order they are written.

The syntax for the second form is two expressions separated by a semicolon (`;`) enclosed in square brackets.

The expression before the `;` is called the *repeat operand*.

The expression after the `;` is called the *length operand*.

The length operand must either be an [inferred const](https://doc.rust-lang.org/reference/items/generics.html#r-items.generics.const.inferred) or be a [constant expression](https://doc.rust-lang.org/reference/const_eval.html#constant-expressions) of type `usize` (e.g. a [literal](https://doc.rust-lang.org/reference/tokens.html#literals) or a [constant item](https://doc.rust-lang.org/reference/items/constant-items.html)).

```rust
#![allow(unused)]
fn main() {
const C: usize = 1;
let _: [u8; C] = [0; 1]; // Literal.
let _: [u8; C] = [0; C]; // Constant item.
let _: [u8; C] = [0; _]; // Inferred const.
let _: [u8; C] = [0; (((_)))]; // Inferred const.
}
```

An array expression of this form creates an array with the length of the value of the length operand with each element being a copy of the repeat operand. That is, `[a; b]` creates an array containing `b` copies of the value of `a`.

If the length operand has a value greater than 1 then this requires the repeat operand to have a type that implements [`Copy`](https://doc.rust-lang.org/reference/special-types-and-traits.html#copy), to be a [const block expression](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.const), or to be a [path](https://doc.rust-lang.org/reference/expressions/path-expr.html) to a constant item.

When the repeat operand is a const block or a path to a constant item, it is evaluated the number of times specified in the length operand.

If that value is `0`, then the const block or constant item is not evaluated at all.

For expressions that are neither a const block nor a path to a constant item, it is evaluated exactly once, and then the result is copied the length operand’s value times.

```rust
#![allow(unused)]
fn main() {
[1, 2, 3, 4];
["a", "b", "c", "d"];
[0; 128];              // array with 128 zeros
[0u8, 0u8, 0u8, 0u8,];
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]; // 2D array
const EMPTY: Vec<i32> = Vec::new();
[EMPTY; 2];
}
```

## [Array and slice indexing expressions](#array-and-slice-indexing-expressions)

[Array](https://doc.rust-lang.org/reference/types/array.html) and [slice](https://doc.rust-lang.org/reference/types/slice.html)-typed values can be indexed by writing a square-bracket-enclosed expression of type `usize` (the index) after them. When the array is mutable, the resulting [memory location](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions) can be assigned to.

For other types an index expression `a[b]` is equivalent to `*std::ops::Index::index(&a, b)`, or `*std::ops::IndexMut::index_mut(&mut a, b)` in a mutable place expression context. Just as with methods, Rust will also insert dereference operations on `a` repeatedly to find an implementation.

Indices are zero-based for arrays and slices.

Array access is a [constant expression](https://doc.rust-lang.org/reference/const_eval.html#constant-expressions), so bounds can be checked at compile-time with a constant index value. Otherwise a check will be performed at run-time that will put the thread in a [*panicked state*](https://doc.rust-lang.org/reference/panic.html) if it fails.

```rust
#![allow(unused)]
fn main() {
// lint is deny by default.
#![warn(unconditional_panic)]

([1, 2, 3, 4])[2];        // Evaluates to 3

let b = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
b[1][2];                  // multidimensional array indexing

let x = (["a", "b"])[10]; // warning: index out of bounds

let n = 10;
let y = (["a", "b"])[n];  // panics

let arr = ["a", "b"];
arr[10];                  // warning: index out of bounds
}
```

The array index expression can be implemented for types other than arrays and slices by implementing the [Index](https://doc.rust-lang.org/core/ops/index/trait.Index.html) and [IndexMut](https://doc.rust-lang.org/core/ops/index/trait.IndexMut.html) traits.