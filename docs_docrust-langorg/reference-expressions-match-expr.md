---
title: Match expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/match-expr.html
source: crawler
fetched_at: 2026-05-06T21:27:01.669578524-03:00
rendered_js: false
word_count: 895
summary: This document explains the syntax and behavior of Rust match expressions, including the role of scrutinee expressions, pattern matching logic, match guards, and guard chains.
tags:
    - rust
    - match-expression
    - pattern-matching
    - control-flow
    - programming-language
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [`match` expressions](#match-expressions)

A *`match` expression* branches on a pattern. The exact form of matching that occurs depends on the [pattern](https://doc.rust-lang.org/reference/patterns.html).

A `match` expression has a *[scrutinee](https://doc.rust-lang.org/reference/glossary.html#scrutinee) expression*, which is the value to compare to the patterns.

The scrutinee expression and the patterns must have the same type.

A `match` behaves differently depending on whether or not the scrutinee expression is a [place expression or value expression](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions).

If the scrutinee expression is a [value expression](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions), it is first evaluated into a temporary location, and the resulting value is sequentially compared to the patterns in the arms until a match is found. The first arm with a matching pattern is chosen as the branch target of the `match`, any variables bound by the pattern are assigned to local variables in the arm’s block, and control enters the block.

When the scrutinee expression is a [place expression](https://doc.rust-lang.org/reference/expressions.html#place-expressions-and-value-expressions), the match does not allocate a temporary location; however, a by-value binding may copy or move from the memory location. When possible, it is preferable to match on place expressions, as the lifetime of these matches inherits the lifetime of the place expression rather than being restricted to the inside of the match.

An example of a `match` expression:

```rust
#![allow(unused)]
fn main() {
let x = 1;

match x {
    1 => println!("one"),
    2 => println!("two"),
    3 => println!("three"),
    4 => println!("four"),
    5 => println!("five"),
    _ => println!("something else"),
}
}
```

Variables bound within the pattern are scoped to the match guard and the arm’s expression.

The [binding mode](https://doc.rust-lang.org/reference/patterns.html#binding-modes) (move, copy, or reference) depends on the pattern.

Multiple match patterns may be joined with the `|` operator. Each pattern will be tested in left-to-right sequence until a successful match is found.

```rust
#![allow(unused)]
fn main() {
let x = 9;
let message = match x {
    0 | 1  => "not many",
    2 ..= 9 => "a few",
    _      => "lots"
};

assert_eq!(message, "a few");

// Demonstration of pattern match order.
struct S(i32, i32);

match S(1, 2) {
    S(z @ 1, _) | S(_, z @ 2) => assert_eq!(z, 1),
    _ => panic!(),
}
}
```

> Note
> 
> The `2..=9` is a [Range Pattern](https://doc.rust-lang.org/reference/patterns.html#range-patterns), not a [Range Expression](https://doc.rust-lang.org/reference/expressions/range-expr.html). Thus, only those types of ranges supported by range patterns can be used in match arms.

Every binding in each `|` separated pattern must appear in all of the patterns in the arm.

Every binding of the same name must have the same type, and have the same binding mode.

The type of the overall `match` expression is the [least upper bound](https://doc.rust-lang.org/reference/type-coercions.html#r-coerce.least-upper-bound) of the individual match arms.

If there are no match arms, then the `match` expression is [diverging](https://doc.rust-lang.org/reference/divergence.html#r-divergence) and the type is [`!`](https://doc.rust-lang.org/reference/types/never.html#r-type.never).

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
fn make<T>() -> T { loop {} }
enum Empty {}

fn diverging_match_no_arms() -> ! {
    let e: Empty = make();
    match e {}
}
}
> ```

If either the scrutinee expression or all of the match arms diverge, then the entire `match` expression also diverges.

## [Match guards](#match-guards)

Match arms can accept *match guards* to further refine the criteria for matching a case.

Pattern guards appear after the pattern following the `if` keyword and consist of an [Expression](https://doc.rust-lang.org/reference/expressions.html#grammar-Expression) with a [boolean type](https://doc.rust-lang.org/reference/types/boolean.html#r-type.bool) or a conditional `let` match.

When the pattern matches successfully, the pattern guard is executed. If all of the guard condition operands evaluate to `true` and all of the `let` patterns successfully match their [scrutinee](https://doc.rust-lang.org/reference/glossary.html#scrutinee)s, the match arm is successfully matched against and the arm body is executed.

Otherwise, the next pattern, including other matches with the `|` operator in the same arm, is tested.

```rust
#![allow(unused)]
fn main() {
let maybe_digit = Some(0);
fn process_digit(i: i32) { }
fn process_other(i: i32) { }
let message = match maybe_digit {
    Some(x) if x < 10 => process_digit(x),
    Some(x) => process_other(x),
    None => panic!(),
};
}
```

> Note
> 
> Multiple matches using the `|` operator can cause the pattern guard and the side effects it has to execute multiple times. For example:
> 
> ```rust
> #![allow(unused)]
fn main() {
use std::cell::Cell;
let i : Cell<i32> = Cell::new(0);
match 1 {
    1 | _ if { i.set(i.get() + 1); false } => {}
    _ => {}
}
assert_eq!(i.get(), 2);
}
> ```

A pattern guard may refer to the variables bound within the pattern they follow.

Before evaluating the guard, a shared reference is taken to the part of the scrutinee the variable matches on. While evaluating the guard, this shared reference is then used when accessing the variable.

Only when the guard evaluates successfully is the value moved, or copied, from the scrutinee into the variable. This allows shared borrows to be used inside guards without moving out of the scrutinee in case guard fails to match.

Moreover, by holding a shared reference while evaluating the guard, mutation inside guards is also prevented.

Guards can use `let` patterns to conditionally match a scrutinee and to bind new variables into scope when the pattern matches successfully.

> Example
> 
> In this example, the guard condition `let Some(first_char) = name.chars().next()` is evaluated. If the `let` pattern successfully matches (i.e. the string has at least one character), the arm’s body is executed. Otherwise, pattern matching continues to the next arm.
> 
> The `let` pattern creates a new binding (`first_char`), which can be used alongside the original pattern bindings (`name`) in the arm’s body.
> 
> ```rust
> #![allow(unused)]
fn main() {
enum Command {
    Run(String),
    Stop,
}
let cmd = Command::Run("example".to_string());

match cmd {
    Command::Run(name) if let Some(first_char) = name.chars().next() => {
        // Both `name` and `first_char` are available here
        println!("Running: {name} (starts with '{first_char}')");
    }
    Command::Run(name) => {
        println!("{name} is empty");
    }
    _ => {}
}
}
> ```

## [Match guard chains](#match-guard-chains)

Multiple guard condition operands can be separated with `&&`.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
let foo = Some([123]);
let already_checked = false;
match foo {
    Some(xs) if let [single] = xs && !already_checked => { dbg!(single); }
    _ => {}
}
}
> ```

Similar to a `&&` [LazyBooleanExpression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#grammar-LazyBooleanExpression), each operand is evaluated from left-to-right until an operand evaluates as `false` or a `let` match fails, in which case the subsequent operands are not evaluated.

The bindings of each `let` pattern are put into scope to be available for the next condition operand and the match arm body.

If any guard condition operand is a `let` pattern, then none of the condition operands can be a `||` [lazy boolean operator expression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#r-expr.bool-logic) due to ambiguity and precedence with the `let` scrutinee.

> Example
> 
> If a `||` expression is needed, then parentheses can be used. For example:
> 
> ```rust
> #![allow(unused)]
fn main() {
let foo = Some([123]);
match foo {
    // Parentheses are required here.
    Some(xs) if let [x] = xs && (x < -100 || x > 20) => {}
    _ => {}
}
}
> ```

## [Attributes on match arms](#attributes-on-match-arms)

Outer attributes are allowed on match arms. The only attributes that have meaning on match arms are [`cfg`](https://doc.rust-lang.org/reference/conditional-compilation.html) and the [lint check attributes](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes).

[Inner attributes](https://doc.rust-lang.org/reference/attributes.html) are allowed directly after the opening brace of the match expression in the same expression contexts as [attributes on block expressions](https://doc.rust-lang.org/reference/expressions/block-expr.html#attributes-on-block-expressions).