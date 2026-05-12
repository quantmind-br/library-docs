---
title: Expressions - The Rust Reference
url: https://doc.rust-lang.org/reference/expressions.html
source: crawler
fetched_at: 2026-05-06T21:26:54.684975898-03:00
rendered_js: false
word_count: 1335
summary: This document defines the rules for Rust expressions, covering evaluation order, operator precedence, and the distinction between place, value, and assignee expressions.
tags:
    - rust-programming
    - expression-evaluation
    - memory-location
    - lvalues-rvalues
    - operator-precedence
    - move-semantics
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Expressions](#expressions)

An expression may have two roles: it always produces a *value*, and it may have *effects* (otherwise known as “side effects”).

An expression *evaluates to* a value, and has effects during *evaluation*.

Many expressions contain sub-expressions, called the *operands* of the expression.

The meaning of each kind of expression dictates several things:

- Whether or not to evaluate the operands when evaluating the expression
- The order in which to evaluate the operands
- How to combine the operands’ values to obtain the value of the expression

In this way, the structure of expressions dictates the structure of execution. Blocks are just another kind of expression, so blocks, statements, expressions, and blocks again can recursively nest inside each other to an arbitrary depth.

> Note
> 
> We give names to the operands of expressions so that we may discuss them, but these names are not stable and may be changed.

## [Expression precedence](#expression-precedence)

The precedence of Rust operators and expressions is ordered as follows, going from strong to weak. Binary Operators at the same precedence level are grouped in the order given by their associativity.

## [Evaluation order of operands](#evaluation-order-of-operands)

The following list of expressions all evaluate their operands the same way, as described after the list. Other expressions either don’t take operands or evaluate them conditionally as described on their respective pages.

- Dereference expression
- Error propagation expression
- Negation expression
- Arithmetic and logical binary operators
- Comparison operators
- Type cast expression
- Grouped expression
- Array expression
- Await expression
- Index expression
- Tuple expression
- Tuple index expression
- Struct expression
- Call expression
- Method call expression
- Field expression
- Break expression
- Range expression
- Return expression

The operands of these expressions are evaluated prior to applying the effects of the expression. Expressions taking multiple operands are evaluated left to right as written in the source code.

> Note
> 
> Which subexpressions are the operands of an expression is determined by expression precedence as per the previous section.

For example, the two `next` method calls will always be called in the same order:

```rust
#![allow(unused)]
fn main() {
// Using vec instead of array to avoid references
// since there is no stable owned array iterator
// at the time this example was written.
let mut one_two = vec![1, 2].into_iter();
assert_eq!(
    (1, 2),
    (one_two.next().unwrap(), one_two.next().unwrap())
);
}
```

> Note
> 
> Since this is applied recursively, these expressions are also evaluated from innermost to outermost, ignoring siblings until there are no inner subexpressions.

## [Place expressions and value expressions](#place-expressions-and-value-expressions)

Expressions are divided into two main categories: place expressions and value expressions; there is also a third, minor category of expressions called assignee expressions. Within each expression, operands may likewise occur in either place context or value context. The evaluation of an expression depends both on its own category and the context it occurs within.

A *place expression* is an expression that represents a memory location.

These expressions are [paths](https://doc.rust-lang.org/reference/expressions/path-expr.html) which refer to local variables, [static variables](https://doc.rust-lang.org/reference/items/static-items.html), [dereferences](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator) (`*expr`), [array indexing](https://doc.rust-lang.org/reference/expressions/array-expr.html#array-and-slice-indexing-expressions) expressions (`expr[expr]`), [field](https://doc.rust-lang.org/reference/expressions/field-expr.html) references (`expr.f`) and parenthesized place expressions.

All other expressions are value expressions.

A *value expression* is an expression that represents an actual value.

[\[expr.place-value.place-context\]](#r-expr.place-value.place-context "expr.place-value.place-context")

The following contexts are *place expression* contexts:

- The left operand of a [compound assignment](https://doc.rust-lang.org/reference/expressions/operator-expr.html#compound-assignment-expressions) expression.
- The operand of a unary [borrow](https://doc.rust-lang.org/reference/expressions/operator-expr.html#borrow-operators), [raw borrow](https://doc.rust-lang.org/reference/expressions/operator-expr.html#raw-borrow-operators) or [dereference](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator) operator.
- The operand of a field expression.
- The indexed operand of an array indexing expression.
- The operand of any [implicit borrow](#implicit-borrows).
- The initializer of a [let statement](https://doc.rust-lang.org/reference/statements.html#let-statements).
- The [scrutinee](https://doc.rust-lang.org/reference/glossary.html#scrutinee) of an [`if let`](https://doc.rust-lang.org/reference/expressions/if-expr.html#if-let-patterns), [`match`](https://doc.rust-lang.org/reference/expressions/match-expr.html), or [`while let`](https://doc.rust-lang.org/reference/expressions/loop-expr.html#while-let-patterns) expression.
- The base of a [functional update](https://doc.rust-lang.org/reference/expressions/struct-expr.html#functional-update-syntax) struct expression.

> Note
> 
> Historically, place expressions were called *lvalues* and value expressions were called *rvalues*.

An *assignee expression* is an expression that appears in the left operand of an [assignment](https://doc.rust-lang.org/reference/expressions/operator-expr.html#assignment-expressions) expression. Explicitly, the assignee expressions are:

- Place expressions.
- [Underscores](https://doc.rust-lang.org/reference/expressions/underscore-expr.html).
- [Tuples](https://doc.rust-lang.org/reference/expressions/tuple-expr.html) of assignee expressions.
- [Slices](https://doc.rust-lang.org/reference/expressions/array-expr.html#r-expr.array.index) of assignee expressions.
- [Tuple structs](https://doc.rust-lang.org/reference/items/structs.html#r-items.struct.tuple) of assignee expressions.
- [Structs](https://doc.rust-lang.org/reference/expressions/struct-expr.html#r-expr.struct) of assignee expressions (with optionally named fields).
- [Unit structs](https://doc.rust-lang.org/reference/items/structs.html#r-items.struct.unit)

Arbitrary parenthesisation is permitted inside assignee expressions.

### [Moved and copied types](#moved-and-copied-types)

When a place expression is evaluated in a value expression context, or is bound by value in a pattern, it denotes the value held *in* that memory location.

If the type of that value implements [`Copy`](https://doc.rust-lang.org/reference/special-types-and-traits.html#copy), then the value will be copied.

In the remaining situations, if that type is [`Sized`](https://doc.rust-lang.org/reference/special-types-and-traits.html#sized), then it may be possible to move the value.

Only the following place expressions may be moved out of:

- [Variables](https://doc.rust-lang.org/reference/variables.html) which are not currently borrowed.
- [Temporary values](#temporaries).
- [Fields](https://doc.rust-lang.org/reference/expressions/field-expr.html) of a place expression which can be moved out of and don’t implement [`Drop`](https://doc.rust-lang.org/reference/special-types-and-traits.html#drop).
- The result of [dereferencing](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator) an expression with type [`Box<T>`](https://doc.rust-lang.org/alloc/boxed/struct.Box.html) and that can also be moved out of.

After moving out of a place expression that evaluates to a local variable, the location is deinitialized and cannot be read from again until it is reinitialized.

In all other cases, trying to use a place expression in a value expression context is an error.

### [Mutability](#mutability)

For a place expression to be [assigned](https://doc.rust-lang.org/reference/expressions/operator-expr.html#assignment-expressions) to, mutably [borrowed](https://doc.rust-lang.org/reference/expressions/operator-expr.html#borrow-operators), [implicitly mutably borrowed](#implicit-borrows), or bound to a pattern containing `ref mut`, it must be *mutable*. We call these *mutable place expressions*. In contrast, other place expressions are called *immutable place expressions*.

The following expressions can be mutable place expression contexts:

- Mutable [variables](https://doc.rust-lang.org/reference/variables.html) which are not currently borrowed.
- [Mutable `static` items](https://doc.rust-lang.org/reference/items/static-items.html#mutable-statics).
- [Temporary values](#temporaries).
- [Fields](https://doc.rust-lang.org/reference/expressions/field-expr.html): this evaluates the subexpression in a mutable place expression context.
- [Dereferences](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator) of a `*mut T` pointer.
- Dereference of a variable, or field of a variable, with type `&mut T`. Note: This is an exception to the requirement of the next rule.
- Dereferences of a type that implements `DerefMut`: this then requires that the value being dereferenced is evaluated in a mutable place expression context.
- [Array indexing](https://doc.rust-lang.org/reference/expressions/array-expr.html#array-and-slice-indexing-expressions) of a type that implements `IndexMut`: this then evaluates the value being indexed, but not the index, in mutable place expression context.

### [Temporaries](#temporaries)

When using a value expression in most place expression contexts, a temporary unnamed memory location is created and initialized to that value. The expression evaluates to that location instead, except if [promoted](https://doc.rust-lang.org/reference/destructors.html#constant-promotion) to a `static`. The [drop scope](https://doc.rust-lang.org/reference/destructors.html#drop-scopes) of the temporary is usually the end of the enclosing statement.

### [Super macros](#super-macros)

Certain built-in macros may create [temporaries](https://doc.rust-lang.org/reference/expressions.html#r-expr.temporary) whose [scopes](https://doc.rust-lang.org/reference/destructors.html#r-destructors.scope.temporary) may be [extended](https://doc.rust-lang.org/reference/destructors.html#r-destructors.scope.lifetime-extension). These temporaries are *super temporaries* and these macros are *super macros*. [Invocations](https://doc.rust-lang.org/reference/macros.html#r-macro.invocation) of these macros are *super macro call expressions*. Arguments to these macros may be *super operands*.

#### [`format_args!`](#format_args)

Except for the format string argument, all arguments passed to [`format_args!`](https://doc.rust-lang.org/core/macro.format_args.html) are *super operands*.

```rust
#![allow(unused)]
fn main() {
fn temp() -> String { String::from("") }
// Due to the call being an extending expression and the argument
// being a super operand, the inner block is an extending expression,
// so the scope of the temporary created in its trailing expression
// is extended.
let _ = format_args!("{}", { &temp() }); // OK
}
```

The super operands of [`format_args!`](https://doc.rust-lang.org/core/macro.format_args.html) are [implicitly borrowed](https://doc.rust-lang.org/reference/expressions.html#r-expr.implicit-borrow) and are therefore [place expression contexts](https://doc.rust-lang.org/reference/expressions.html#r-expr.place-value). When a [value expression](https://doc.rust-lang.org/reference/expressions.html#r-expr.place-value) is passed as an argument, it creates a *super temporary*.

```rust
#![allow(unused)]
fn main() {
fn temp() -> String { String::from("") }
let x = format_args!("{}", temp());
x; // <-- The temporary is extended, allowing use here.
}
```

The expansion of a call to [`format_args!`](https://doc.rust-lang.org/core/macro.format_args.html) sometimes creates other internal *super temporaries*.

```rust
#![allow(unused)]
fn main() {
let x = {
    // This call creates an internal temporary.
    let x = format_args!("{:?}", 0);
    x // <-- The temporary is extended, allowing its use here.
}; // <-- The temporary is dropped here.
x; // ERROR
}
```

```rust
#![allow(unused)]
fn main() {
// This call doesn't create an internal temporary.
let x = { let x = format_args!("{}", 0); x };
x; // OK
}
```

> Note
> 
> The details of when [`format_args!`](https://doc.rust-lang.org/core/macro.format_args.html) does or does not create internal temporaries are currently unspecified.

#### [`pin!`](#pin)

The argument to [`pin!`](https://doc.rust-lang.org/core/pin/macro.pin.html) is a *super operand*.

```rust
#![allow(unused)]
fn main() {
use core::pin::pin;
fn temp() {}
// As above for `format_args!`.
let _ = pin!({ &temp() }); // OK
}
```

The argument to [`pin!`](https://doc.rust-lang.org/core/pin/macro.pin.html) is a [value expression context](https://doc.rust-lang.org/reference/expressions.html#r-expr.place-value) and creates a *super temporary*.

```rust
#![allow(unused)]
fn main() {
use core::pin::pin;
fn temp() {}
// The argument is evaluated into a super temporary.
let x = pin!(temp());
// The temporary is extended, allowing its use here.
x; // OK
}
```

### [Implicit borrows](#implicit-borrows)

Certain expressions will treat an expression as a place expression by implicitly borrowing it. For example, it is possible to compare two unsized [slices](https://doc.rust-lang.org/reference/types/slice.html) for equality directly, because the `==` operator implicitly borrows its operands:

```rust
#![allow(unused)]
fn main() {
let c = [1, 2, 3];
let d = vec![1, 2, 3];
let a: &[i32];
let b: &[i32];
a = &c;
b = &d;
// ...
*a == *b;
// Equivalent form:
::std::cmp::PartialEq::eq(&*a, &*b);
}
```

Implicit borrows may be taken in the following expressions:

- Left operand in [method-call](https://doc.rust-lang.org/reference/expressions/method-call-expr.html) expressions.
- Left operand in [field](https://doc.rust-lang.org/reference/expressions/field-expr.html) expressions.
- Left operand in [call expressions](https://doc.rust-lang.org/reference/expressions/call-expr.html).
- Left operand in [array indexing](https://doc.rust-lang.org/reference/expressions/array-expr.html#array-and-slice-indexing-expressions) expressions.
- Operand of the [dereference operator](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-dereference-operator) (`*`).
- Operands of [comparison](https://doc.rust-lang.org/reference/expressions/operator-expr.html#comparison-operators).
- Left operands of the [compound assignment](https://doc.rust-lang.org/reference/expressions/operator-expr.html#compound-assignment-expressions).
- Arguments to [`format_args!`](https://doc.rust-lang.org/core/macro.format_args.html) except the format string.

## [Overloading traits](#overloading-traits)

Many of the following operators and expressions can also be overloaded for other types using traits in `std::ops` or `std::cmp`. These traits also exist in `core::ops` and `core::cmp` with the same names.

## [Expression attributes](#expression-attributes)

[Outer attributes](https://doc.rust-lang.org/reference/attributes.html) before an expression are allowed only in a few specific cases:

- Before an expression used as a [statement](https://doc.rust-lang.org/reference/statements.html).
- Elements of [array expressions](https://doc.rust-lang.org/reference/expressions/array-expr.html), [tuple expressions](https://doc.rust-lang.org/reference/expressions/tuple-expr.html), [call expressions](https://doc.rust-lang.org/reference/expressions/call-expr.html), and tuple-style [struct](https://doc.rust-lang.org/reference/expressions/struct-expr.html) expressions.
- The tail expression of [block expressions](https://doc.rust-lang.org/reference/expressions/block-expr.html).

They are never allowed before:

- [Range](https://doc.rust-lang.org/reference/expressions/range-expr.html) expressions.
- Binary operator expressions ([ArithmeticOrLogicalExpression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#grammar-ArithmeticOrLogicalExpression), [ComparisonExpression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#grammar-ComparisonExpression), [LazyBooleanExpression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#grammar-LazyBooleanExpression), [TypeCastExpression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#grammar-TypeCastExpression), [AssignmentExpression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#grammar-AssignmentExpression), [CompoundAssignmentExpression](https://doc.rust-lang.org/reference/expressions/operator-expr.html#grammar-CompoundAssignmentExpression)).