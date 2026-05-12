---
title: Loop expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions/loop-expr.html#infinite-loops
source: crawler
fetched_at: 2026-05-06T21:27:00.830600071-03:00
rendered_js: false
word_count: 1118
summary: This document describes the syntax and semantics of various loop expressions in the Rust programming language, including infinite, predicate, and iterator-based loops, as well as loop labeling and control flow constructs.
tags:
    - rust
    - loops
    - control-flow
    - programming-language
    - reference
    - iteration
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Loops and other breakable expressions](#loops-and-other-breakable-expressions)

Rust supports four loop expressions:

- A [`loop` expression](#infinite-loops) denotes an infinite loop.
- A [`while` expression](#predicate-loops) loops until a predicate is false.
- A [`for` expression](#iterator-loops) extracts values from an iterator, looping until the iterator is empty.
- A [labeled block expression](https://doc.rust-lang.org/reference/expressions/loop-expr.html#r-expr.loop.block-labels) runs a loop exactly once, but allows exiting the loop early with `break`.

All four types of loop support [`break` expressions](#break-expressions), and [labels](#loop-labels).

All except labeled block expressions support [`continue` expressions](#continue-expressions).

Only `loop` and labeled block expressions support [evaluation to non-trivial values](#break-and-loop-values).

## [Infinite loops](#infinite-loops)

A `loop` expression repeats execution of its body continuously: `loop { println!("I live."); }`.

A `loop` expression without an associated `break` expression is [diverging](https://doc.rust-lang.org/reference/divergence.html#r-divergence) and has type [`!`](https://doc.rust-lang.org/reference/types/never.html#r-type.never).

A `loop` expression containing associated [`break` expression(s)](#break-expressions) may terminate, and must have type compatible with the value of the `break` expression(s).

## [Predicate loops](#predicate-loops)

A `while` loop expression allows repeating the evaluation of a block while a set of conditions remain true.

Condition operands must be either an [Expression](https://doc.rust-lang.org/reference/expressions.html#grammar-Expression) with a [boolean type](https://doc.rust-lang.org/reference/types/boolean.html) or a conditional `let` match. If all of the condition operands evaluate to `true` and all of the `let` patterns successfully match their [scrutinee](https://doc.rust-lang.org/reference/glossary.html#scrutinee)s, then the loop body block executes.

After the loop body successfully executes, the condition operands are re-evaluated to determine if the body should be executed again.

If any condition operand evaluates to `false` or any `let` pattern does not match its scrutinee, the body is not executed and execution continues after the `while` expression.

A `while` expression evaluates to `()`.

An example:

```rust
#![allow(unused)]
fn main() {
let mut i = 0;

while i < 10 {
    println!("hello");
    i = i + 1;
}
}
```

### [`while let` patterns](#while-let-patterns)

`let` patterns in a `while` condition allow binding new variables into scope when the pattern matches successfully. The following examples illustrate bindings using `let` patterns:

```rust
#![allow(unused)]
fn main() {
let mut x = vec![1, 2, 3];

while let Some(y) = x.pop() {
    println!("y = {}", y);
}

while let _ = 5 {
    println!("Irrefutable patterns are always true");
    break;
}
}
```

A `while let` loop is equivalent to a `loop` expression containing a [`match` expression](https://doc.rust-lang.org/reference/expressions/match-expr.html) as follows.

```rust
'label: while let PATS = EXPR {
    /* loop body */
}
```

is equivalent to

```rust
'label: loop {
    match EXPR {
        PATS => { /* loop body */ },
        _ => break,
    }
}
```

Multiple patterns may be specified with the `|` operator. This has the same semantics as with `|` in `match` expressions:

```rust
#![allow(unused)]
fn main() {
let mut vals = vec![2, 3, 1, 2, 2];
while let Some(v @ 1) | Some(v @ 2) = vals.pop() {
    // Prints 2, 2, then 1
    println!("{}", v);
}
}
```

### [`while` condition chains](#while-condition-chains)

Multiple condition operands can be separated with `&&`. These have the same semantics and restrictions as [`if` condition chains](https://doc.rust-lang.org/reference/expressions/if-expr.html#chains-of-conditions).

The following is an example of chaining multiple expressions, mixing `let` bindings and boolean expressions, and with expressions able to reference pattern bindings from previous expressions:

```rust
fn main() {
    let outer_opt = Some(Some(1i32));

    while let Some(inner_opt) = outer_opt
        && let Some(number) = inner_opt
        && number == 1
    {
        println!("Peek a boo");
        break;
    }
}
```

## [Iterator loops](#iterator-loops)

A `for` expression is a syntactic construct for looping over elements provided by an implementation of `std::iter::IntoIterator`.

If the iterator yields a value, that value is matched against the irrefutable pattern, the body of the loop is executed, and then control returns to the head of the `for` loop. If the iterator is empty, the `for` expression completes.

An example of a `for` loop over the contents of an array:

```rust
#![allow(unused)]
fn main() {
let v = &["apples", "cake", "coffee"];

for text in v {
    println!("I like {}.", text);
}
}
```

An example of a for loop over a series of integers:

```rust
#![allow(unused)]
fn main() {
let mut sum = 0;
for n in 1..11 {
    sum += n;
}
assert_eq!(sum, 55);
}
```

A `for` loop is equivalent to a `loop` expression containing a [`match` expression](https://doc.rust-lang.org/reference/expressions/match-expr.html) as follows:

```rust
'label: for PATTERN in iter_expr {
    /* loop body */
}
```

is equivalent to

```rust
{
    let result = match IntoIterator::into_iter(iter_expr) {
        mut iter => 'label: loop {
            let mut next;
            match Iterator::next(&mut iter) {
                Option::Some(val) => next = val,
                Option::None => break,
            };
            let PATTERN = next;
            let () = { /* loop body */ };
        },
    };
    result
}
```

`IntoIterator`, `Iterator`, and `Option` are always the standard library items here, not whatever those names resolve to in the current scope.

The variable names `next`, `iter`, and `val` are for exposition only, they do not actually have names the user can type.

> Note
> 
> The outer `match` is used to ensure that any [temporary values](https://doc.rust-lang.org/reference/expressions.html#temporaries) in `iter_expr` don’t get dropped before the loop is finished. `next` is declared before being assigned because it results in types being inferred correctly more often.

## [Loop labels](#loop-labels)

A loop expression may optionally have a *label*. The label is written as a lifetime preceding the loop expression, as in `'foo: loop { break 'foo; }`, `'bar: while false {}`, `'humbug: for _ in 0..0 {}`.

If a label is present, then labeled `break` and `continue` expressions nested within this loop may exit out of this loop or return control to its head. See [break expressions](#break-expressions) and [continue expressions](#continue-expressions).

Labels follow the hygiene and shadowing rules of local variables. For example, this code will print “outer loop”:

```rust
#![allow(unused)]
fn main() {
'a: loop {
    'a: loop {
        break 'a;
    }
    print!("outer loop");
    break 'a;
}
}
```

`'_` is not a valid loop label.

## [`break` expressions](#break-expressions)

When `break` is encountered, execution of the associated loop body is immediately terminated, for example:

```rust
#![allow(unused)]
fn main() {
let mut last = 0;
for x in 1..100 {
    if x > 12 {
        break;
    }
    last = x;
}
assert_eq!(last, 12);
}
```

A `break` expression is [diverging](https://doc.rust-lang.org/reference/divergence.html#r-divergence) and has a type of [`!`](https://doc.rust-lang.org/reference/types/never.html#r-type.never).

A `break` expression is normally associated with the innermost `loop`, `for` or `while` loop enclosing the `break` expression, but a [label](#loop-labels) can be used to specify which enclosing loop is affected. Example:

```rust
#![allow(unused)]
fn main() {
'outer: loop {
    while true {
        break 'outer;
    }
}
}
```

A `break` expression is only permitted in the body of a loop, and has one of the forms `break`, `break 'label` or ([see below](#break-and-loop-values)) `break EXPR` or `break 'label EXPR`.

In a [`loop` with break expressions](https://doc.rust-lang.org/reference/expressions/loop-expr.html#r-expr.loop.break-value) or a [labeled block expression](https://doc.rust-lang.org/reference/expressions/loop-expr.html#r-expr.loop.block-labels), a `break` without an expression is equivalent to `break ()`.

## [Labeled block expressions](#labeled-block-expressions)

Labeled block expressions are exactly like block expressions, except that they allow using `break` expressions within the block.

Unlike loops, `break` expressions within a labeled block expression *must* have a label (i.e. the label is not optional).

Similarly, labeled block expressions *must* begin with a label.

```rust
#![allow(unused)]
fn main() {
fn do_thing() {}
fn condition_not_met() -> bool { true }
fn do_next_thing() {}
fn do_last_thing() {}
let result = 'block: {
    do_thing();
    if condition_not_met() {
        break 'block 1;
    }
    do_next_thing();
    if condition_not_met() {
        break 'block 2;
    }
    do_last_thing();
    3
};
}
```

The type of a labeled block expression is the [least upper bound](https://doc.rust-lang.org/reference/type-coercions.html#r-coerce.least-upper-bound) of all of the break operands and the final operand. If the final operand is omitted, the type of the final operand defaults to the [unit type](https://doc.rust-lang.org/reference/types/tuple.html#r-type.tuple.unit), unless the block [diverges](https://doc.rust-lang.org/reference/expressions/block-expr.html#r-expr.block.diverging), in which case it is the [never type](https://doc.rust-lang.org/reference/types/never.html#r-type.never).

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
fn example(condition: bool) {
    let s = String::from("owned");

    let _: &str = 'block: {
        if condition {
            break 'block &s;  // &String coerced to &str via Deref
        }
        break 'block "literal";  // &'static str coerced to &str
    };
}
}
> ```

## [`continue` expressions](#continue-expressions)

When `continue` is encountered, the current iteration of the associated loop body is immediately terminated, returning control to the loop *head*.

A `continue` expression is [diverging](https://doc.rust-lang.org/reference/divergence.html#r-divergence) and has a type of [`!`](https://doc.rust-lang.org/reference/types/never.html#r-type.never).

In the case of a `while` loop, the head is the conditional operands controlling the loop.

In the case of a `for` loop, the head is the call-expression controlling the loop.

Like `break`, `continue` is normally associated with the innermost enclosing loop, but `continue 'label` may be used to specify the loop affected.

A `continue` expression is only permitted in the body of a loop.

## [`break` and loop values](#break-and-loop-values)

When associated with a `loop`, a break expression may be used to return a value from that loop, via one of the forms `break EXPR` or `break 'label EXPR`, where `EXPR` is an expression whose result is returned from the `loop`. For example:

```rust
#![allow(unused)]
fn main() {
let (mut a, mut b) = (1, 1);
let result = loop {
    if b > 10 {
        break b;
    }
    let c = a + b;
    a = b;
    b = c;
};
// first number in Fibonacci sequence over 10:
assert_eq!(result, 13);
}
```

The type of a `loop` with associated `break` expressions is the [least upper bound](https://doc.rust-lang.org/reference/type-coercions.html#r-coerce.least-upper-bound) of all of the break operands.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
fn example(condition: bool) {
    let s = String::from("owned");

    let _: &str = loop {
        if condition {
            break &s; // &String coerced to &str via Deref
        }
        break "literal"; // &'static str coerced to &str
    };
}
}
> ```

A `loop` with associated `break` expressions does not [diverge](https://doc.rust-lang.org/reference/divergence.html#r-divergence) if any of the break operands do not diverge. If all of the `break` operands diverge, then the `loop` expression also diverges.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
fn diverging_loop_with_break(condition: bool) -> ! {
    // This loop is diverging because all `break` operands are diverging.
    loop {
        if condition {
            break loop {};
        } else {
            break panic!();
        }
    }
}
}
> ```
> 
> ```rust
> #![allow(unused)]
fn main() {
fn loop_with_non_diverging_break(condition: bool) -> ! {
    // The type of this loop is i32 even though one of the breaks is
    // diverging.
    loop {
        if condition {
            break loop {};
        } else {
            break 123i32;
        }
    } // ERROR: expected `!`, found `i32`
}
}
> ```