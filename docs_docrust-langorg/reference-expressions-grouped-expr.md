---
title: Grouped expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/grouped-expr.html
source: crawler
fetched_at: 2026-05-06T21:27:00.755026694-03:00
rendered_js: false
word_count: 147
summary: This document defines the syntax and semantic behavior of parenthesized expressions in the Rust programming language, including their impact on operator precedence and expression classification.
tags:
    - rust
    - expressions
    - syntax
    - operator-precedence
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Grouped expressions](#grouped-expressions)

A *parenthesized expression* wraps a single expression, evaluating to that expression. The syntax for a parenthesized expression is a `(`, then an expression, called the *enclosed operand*, and then a `)`.

Parenthesized expressions evaluate to the value of the enclosed operand.

A parenthesized expression is a [place expression](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions) if the enclosed operand is a place expression, and is a value expression if the enclosed operand is a value expression.

Parentheses can be used to explicitly modify the precedence order of subexpressions within an expression.

An example of a parenthesized expression:

```rust
#![allow(unused)]
fn main() {
let x: i32 = 2 + 3 * 4; // not parenthesized
let y: i32 = (2 + 3) * 4; // parenthesized
assert_eq!(x, 14);
assert_eq!(y, 20);
}
```

An example of a necessary use of parentheses is when calling a function pointer that is a member of a struct:

```rust
#![allow(unused)]
fn main() {
struct A {
   f: fn() -> &'static str
}
impl A {
   fn f(&self) -> &'static str {
       "The method f"
   }
}
let a = A{f: || "The field f"};
assert_eq!( a.f (), "The method f");
assert_eq!((a.f)(), "The field f");
}
```