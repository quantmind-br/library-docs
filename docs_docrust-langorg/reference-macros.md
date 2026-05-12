---
title: Macros - The Rust Reference
url: https://doc.rust-lang.org/reference/macros.html#railroad-MacroInvocationSemi
source: crawler
fetched_at: 2026-05-06T21:25:10.786190482-03:00
rendered_js: false
word_count: 308
summary: This document provides an overview of Rust macro definitions, invocation syntax, and their usage contexts within the language.
tags:
    - rust
    - macros
    - procedural-macros
    - macro-rules
    - syntax-extension
    - compile-time
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Macros](#macros)

The functionality and syntax of Rust can be extended with custom definitions called macros. They are given names, and invoked through a consistent syntax: `some_extension!(...)`.

There are two ways to define new macros:

- [Macros by Example](https://doc.rust-lang.org/reference/macros-by-example.html) define new syntax in a higher-level, declarative way.
- [Procedural Macros](https://doc.rust-lang.org/reference/procedural-macros.html) define function-like macros, custom derives, and custom attributes using functions that operate on input tokens.

## [Macro invocation](#macro-invocation)

A macro invocation expands a macro at compile time and replaces the invocation with the result of the macro. Macros may be invoked in the following situations:

- [Expressions](https://doc.rust-lang.org/reference/expressions.html) and [statements](https://doc.rust-lang.org/reference/statements.html)

<!--THE END-->

- [Patterns](https://doc.rust-lang.org/reference/patterns.html)

<!--THE END-->

- [Types](https://doc.rust-lang.org/reference/types.html)

<!--THE END-->

- [Items](https://doc.rust-lang.org/reference/items.html) including [associated items](https://doc.rust-lang.org/reference/items/associated-items.html)

<!--THE END-->

- [`macro_rules`](https://doc.rust-lang.org/reference/macros-by-example.html) transcribers

<!--THE END-->

- [External blocks](https://doc.rust-lang.org/reference/items/external-blocks.html)

When used as an item or a statement, the [MacroInvocationSemi](https://doc.rust-lang.org/reference/macros.html#grammar-MacroInvocationSemi) form is used where a semicolon is required at the end when not using curly braces. [Visibility qualifiers](https://doc.rust-lang.org/reference/visibility-and-privacy.html) are never allowed before a macro invocation or [`macro_rules`](https://doc.rust-lang.org/reference/macros-by-example.html) definition.

```rust
#![allow(unused)]
fn main() {
// Used as an expression.
let x = vec![1,2,3];

// Used as a statement.
println!("Hello!");

// Used in a pattern.
macro_rules! pat {
    ($i:ident) => (Some($i))
}

if let pat!(x) = Some(1) {
    assert_eq!(x, 1);
}

// Used in a type.
macro_rules! Tuple {
    { $A:ty, $B:ty } => { ($A, $B) };
}

type N2 = Tuple!(i32, i32);

// Used as an item.
use std::cell::RefCell;
thread_local!(static FOO: RefCell<u32> = RefCell::new(1));

// Used as an associated item.
macro_rules! const_maker {
    ($t:ty, $v:tt) => { const CONST: $t = $v; };
}
trait T {
    const_maker!{i32, 7}
}

// Macro calls within macros.
macro_rules! example {
    () => { println!("Macro call in a macro!") };
}
// Outer macro `example` is expanded, then inner macro `println` is expanded.
example!();
}
```

Macros invocations can be resolved via two kinds of scopes:

- Textual Scope
  
  - [Textual scope `macro_rules`](https://doc.rust-lang.org/reference/macros-by-example.html#r-macro.decl.scope.textual)
- Path-based scope
  
  - [Path-based scope `macro_rules`](https://doc.rust-lang.org/reference/macros-by-example.html#r-macro.decl.scope.path-based)
  - [Procedural macros](https://doc.rust-lang.org/reference/procedural-macros.html)