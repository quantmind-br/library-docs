---
title: Field access expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/field-expr.html
source: crawler
fetched_at: 2026-05-06T21:26:57.773735779-03:00
rendered_js: false
word_count: 242
summary: This document explains the syntax, behavior, and borrowing rules for field access expressions in the Rust programming language, including automatic dereferencing.
tags:
    - rust
    - field-access
    - structs
    - unions
    - borrowing
    - autoderef
    - expressions
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Field access expressions](#field-access-expressions)

A *field expression* is a [place expression](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions) that evaluates to the location of a field of a [struct](https://doc.rust-lang.org/reference/items/structs.html) or [union](https://doc.rust-lang.org/reference/items/unions.html).

When the operand is [mutable](https://doc.rust-lang.org/reference/expressions.html#mutability), the field expression is also mutable.

The syntax for a field expression is an expression, called the *container operand*, then a `.`, and finally an [identifier](https://doc.rust-lang.org/reference/identifiers.html).

Field expressions cannot be followed by a parenthetical comma-separated list of expressions, as that is instead parsed as a [method call expression](https://doc.rust-lang.org/reference/expressions/method-call-expr.html). That is, they cannot be the function operand of a [call expression](https://doc.rust-lang.org/reference/expressions/call-expr.html).

> Note
> 
> Wrap the field expression in a [parenthesized expression](https://doc.rust-lang.org/reference/expressions/grouped-expr.html) to use it in a call expression.
> 
> ```rust
> #![allow(unused)]
fn main() {
struct HoldsCallable<F: Fn()> { callable: F }
let holds_callable = HoldsCallable { callable: || () };

// Invalid: Parsed as calling the method "callable"
// holds_callable.callable();

// Valid
(holds_callable.callable)();
}
> ```

Examples:

```rust
mystruct.myfield;
foo().x;
(Struct {a: 10, b: 20}).a;
(mystruct.function_field)() // Call expression containing a field expression
```

## [Automatic dereferencing](#automatic-dereferencing)

If the type of the container operand implements [`Deref`](https://doc.rust-lang.org/reference/special-types-and-traits.html#deref-and-derefmut) or [`DerefMut`](https://doc.rust-lang.org/reference/special-types-and-traits.html#deref-and-derefmut) depending on whether the operand is [mutable](https://doc.rust-lang.org/reference/expressions.html#mutability), it is *automatically dereferenced* as many times as necessary to make the field access possible. This process is also called *autoderef* for short.

## [Borrowing](#borrowing)

The fields of a struct or a reference to a struct are treated as separate entities when borrowing. If the struct does not implement [`Drop`](https://doc.rust-lang.org/reference/special-types-and-traits.html#drop) and is stored in a local variable, this also applies to moving out of each of its fields. This also does not apply if automatic dereferencing is done through user-defined types other than [`Box`](https://doc.rust-lang.org/reference/special-types-and-traits.html#boxt).

```rust
#![allow(unused)]
fn main() {
struct A { f1: String, f2: String, f3: String }
let mut x: A;
x = A {
    f1: "f1".to_string(),
    f2: "f2".to_string(),
    f3: "f3".to_string()
};
let a: &mut String = &mut x.f1; // x.f1 borrowed mutably
let b: &String = &x.f2;         // x.f2 borrowed immutably
let c: &String = &x.f2;         // Can borrow again
let d: String = x.f3;           // Move out of x.f3
}
```