---
title: Path expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/path-expr.html
source: crawler
fetched_at: 2026-05-06T21:26:55.243385823-03:00
rendered_js: false
word_count: 89
summary: This document defines the syntax and semantic rules for path expressions in Rust, explaining how they resolve to local variables, static items, and value or place expressions.
tags:
    - rust-language
    - path-expressions
    - place-expressions
    - value-expressions
    - static-variables
    - syntax-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Path expressions](#path-expressions)

A [path](https://doc.rust-lang.org/reference/paths.html) used as an expression context denotes either a local variable or an item.

Path expressions that resolve to local or static variables are [place expressions](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions); other paths are [value expressions](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions).

Using a [`static mut`](https://doc.rust-lang.org/reference/items/static-items.html#mutable-statics) variable requires an [`unsafe` block](https://doc.rust-lang.org/reference/expressions/block-expr.html#unsafe-blocks).

```rust
#![allow(unused)]
fn main() {
mod globals {
    pub static STATIC_VAR: i32 = 5;
    pub static mut STATIC_MUT_VAR: i32 = 7;
}
let local_var = 3;
local_var;
globals::STATIC_VAR;
unsafe { globals::STATIC_MUT_VAR };
let some_constructor = Some::<i32>;
let push_integer = Vec::<i32>::push;
let slice_reverse = <[i32]>::reverse;
}
```

Evaluation of associated constants is handled the same way as [`const` blocks](https://doc.rust-lang.org/reference/expressions/block-expr.html#const-blocks).