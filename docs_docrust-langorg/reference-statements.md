---
title: Statements - The Rust Reference
url: https://doc.rust-lang.org/reference/statements.html#let-statements
source: crawler
fetched_at: 2026-05-06T21:26:56.259787968-03:00
rendered_js: false
word_count: 550
summary: This document defines the syntax and behavior of statements in the Rust programming language, covering declaration statements, expression statements, and their usage within blocks.
tags:
    - rust
    - programming-language
    - syntax
    - statements
    - variables
    - declarations
    - expressions
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Statements](#statements)

A *statement* is a component of a [block](https://doc.rust-lang.org/reference/expressions/block-expr.html), which is in turn a component of an outer [expression](https://doc.rust-lang.org/reference/expressions.html) or [function](https://doc.rust-lang.org/reference/items/functions.html).

Rust has two kinds of statement: [declaration statements](#declaration-statements) and [expression statements](#expression-statements).

## [Declaration statements](#declaration-statements)

A *declaration statement* is one that introduces one or more *names* into the enclosing statement block. The declared names may denote new variables or new [items](https://doc.rust-lang.org/reference/items.html).

The two kinds of declaration statements are item declarations and `let` statements.

### [Item declarations](#item-declarations)

An *item declaration statement* has a syntactic form identical to an [item declaration](https://doc.rust-lang.org/reference/items.html) within a [module](https://doc.rust-lang.org/reference/items/modules.html).

Declaring an item within a statement block restricts its [scope](https://doc.rust-lang.org/reference/names/scopes.html) to the block containing the statement. The item is not given a [canonical path](https://doc.rust-lang.org/reference/paths.html#canonical-paths) nor are any sub-items it may declare.

The exception to this is that associated items defined by [implementations](https://doc.rust-lang.org/reference/items/implementations.html) are still accessible in outer scopes as long as the item and, if applicable, trait are accessible. It is otherwise identical in meaning to declaring the item inside a module.

There is no implicit capture of the containing function’s generic parameters, parameters, and local variables. For example, `inner` may not access `outer_var`.

```rust
#![allow(unused)]
fn main() {
fn outer() {
  let outer_var = true;

  fn inner() { /* outer_var is not in scope here */ }

  inner();
}
}
```

### [`let` statements](#let-statements)

A *`let` statement* introduces a new set of [variables](https://doc.rust-lang.org/reference/variables.html), given by a [pattern](https://doc.rust-lang.org/reference/patterns.html). The pattern is followed optionally by a type annotation and then either ends, or is followed by an initializer expression plus an optional `else` block.

When no type annotation is given, the compiler will infer the type, or signal an error if insufficient type information is available for definite inference.

Any variables introduced by a variable declaration are visible from the point of declaration until the end of the enclosing block scope, except when they are shadowed by another variable declaration.

If an `else` block is not present, the pattern must be irrefutable. If an `else` block is present, the pattern may be refutable.

If the pattern does not match (this requires it to be refutable), the `else` block is executed. The `else` block must always diverge (evaluate to the [never type](https://doc.rust-lang.org/reference/types/never.html)).

```rust
#![allow(unused)]
fn main() {
let (mut v, w) = (vec![1, 2, 3], 42); // The bindings may be mut or const
let Some(t) = v.pop() else { // Refutable patterns require an else block
    panic!(); // The else block must diverge
};
let [u, v] = [v[0], v[1]] else { // This pattern is irrefutable, so the compiler
                                 // will lint as the else block is redundant.
    panic!();
};
}
```

## [Expression statements](#expression-statements)

An *expression statement* is one that evaluates an [expression](https://doc.rust-lang.org/reference/expressions.html) and ignores its result. As a rule, an expression statement’s purpose is to trigger the effects of evaluating its expression.

An expression that consists of only a [block expression](https://doc.rust-lang.org/reference/expressions/block-expr.html) or control flow expression, if used in a context where a statement is permitted, can omit the trailing semicolon. This can cause an ambiguity between it being parsed as a standalone statement and as a part of another expression; in this case, it is parsed as a statement.

The type of [ExpressionWithBlock](https://doc.rust-lang.org/reference/expressions.html#grammar-ExpressionWithBlock) expressions when used as statements must be the unit type.

```rust
#![allow(unused)]
fn main() {
let mut v = vec![1, 2, 3];
v.pop();          // Ignore the element returned from pop
if v.is_empty() {
    v.push(5);
} else {
    v.remove(0);
}                 // Semicolon can be omitted.
[1];              // Separate expression statement, not an indexing expression.
}
```

When the trailing semicolon is omitted, the result must be type `()`.

```rust
#![allow(unused)]
fn main() {
// bad: the block's type is i32, not ()
// Error: expected `()` because of default return type
// if true {
//   1
// }

// good: the block's type is i32
if true {
  1
} else {
  2
};
}
```

## [Attributes on statements](#attributes-on-statements)

Statements accept [outer attributes](https://doc.rust-lang.org/reference/attributes.html). The attributes that have meaning on a statement are [`cfg`](https://doc.rust-lang.org/reference/conditional-compilation.html), and [the lint check attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes).