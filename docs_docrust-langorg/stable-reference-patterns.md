---
title: Patterns - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/patterns.html#grammar-Pattern
source: crawler
fetched_at: 2026-05-06T21:32:03.975938069-03:00
rendered_js: false
word_count: 3709
summary: This document explains the syntax and semantics of pattern matching in Rust, covering destructuring, refutability, literal matching, and variable binding.
tags:
    - rust
    - pattern-matching
    - destructuring
    - refutability
    - binding
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Patterns](#patterns)

Patterns are used to match values against structures and to, optionally, bind variables to values inside these structures. They are also used in variable declarations and parameters for functions and closures.

The pattern in the following example does four things:

- Tests if `person` has the `car` field filled with something.
- Tests if the person’s `age` field is between 13 and 19, and binds its value to the `person_age` variable.
- Binds a reference to the `name` field to the variable `person_name`.
- Ignores the rest of the fields of `person`. The remaining fields can have any value and are not bound to any variables.

```rust
#![allow(unused)]
fn main() {
struct Car;
struct Computer;
struct Person {
    name: String,
    car: Option<Car>,
    computer: Option<Computer>,
    age: u8,
}
let person = Person {
    name: String::from("John"),
    car: Some(Car),
    computer: None,
    age: 15,
};
if let
    Person {
        car: Some(_),
        age: person_age @ 13..=19,
        name: ref person_name,
        ..
    } = person
{
    println!("{} has a car and is {} years old.", person_name, person_age);
}
}
```

Patterns are used in:

- [`let` declarations](https://doc.rust-lang.org/stable/reference/statements.html#let-statements)

<!--THE END-->

- [Function](https://doc.rust-lang.org/stable/reference/items/functions.html) and [closure](https://doc.rust-lang.org/stable/reference/expressions/closure-expr.html) parameters

<!--THE END-->

- [`match` expressions](https://doc.rust-lang.org/stable/reference/expressions/match-expr.html)

<!--THE END-->

- [`if let` expressions](https://doc.rust-lang.org/stable/reference/expressions/if-expr.html)

<!--THE END-->

- [`while let` expressions](https://doc.rust-lang.org/stable/reference/expressions/loop-expr.html#while-let-patterns)

<!--THE END-->

- [`for` expressions](https://doc.rust-lang.org/stable/reference/expressions/loop-expr.html#iterator-loops)

## [Destructuring](#destructuring)

Patterns can be used to *destructure* [structs](https://doc.rust-lang.org/stable/reference/items/structs.html), [enums](https://doc.rust-lang.org/stable/reference/items/enumerations.html), and [tuples](https://doc.rust-lang.org/stable/reference/types/tuple.html). Destructuring breaks up a value into its component pieces. The syntax used is almost the same as when creating such values.

In a pattern whose [scrutinee](https://doc.rust-lang.org/stable/reference/glossary.html#scrutinee) expression has a `struct`, `enum` or `tuple` type, a [wildcard pattern](#wildcard-pattern) (`_`) stands in for a *single* data field, whereas an [et cetera](#grammar-StructPatternEtCetera) or [rest pattern](https://doc.rust-lang.org/stable/reference/patterns.html#r-patterns.rest) (`..`) stands in for *all* the remaining fields of a particular variant.

When destructuring a data structure with named (but not numbered) fields, it is allowed to write `fieldname` as a shorthand for `fieldname: fieldname`.

```rust
#![allow(unused)]
fn main() {
enum Message {
    Quit,
    WriteString(String),
    Move { x: i32, y: i32 },
    ChangeColor(u8, u8, u8),
}
let message = Message::Quit;
match message {
    Message::Quit => println!("Quit"),
    Message::WriteString(write) => println!("{}", &write),
    Message::Move{ x, y: 0 } => println!("move {} horizontally", x),
    Message::Move{ .. } => println!("other move"),
    Message::ChangeColor { 0: red, 1: green, 2: _ } => {
        println!("color change, red: {}, green: {}", red, green);
    }
};
}
```

## [Refutability](#refutability)

A pattern is said to be *refutable* when it has the possibility of not being matched by the value it is being matched against. *Irrefutable* patterns, on the other hand, always match the value they are being matched against. Examples:

```rust
#![allow(unused)]
fn main() {
let (x, y) = (1, 2);               // "(x, y)" is an irrefutable pattern

if let (a, 3) = (1, 2) {           // "(a, 3)" is refutable, and will not match
    panic!("Shouldn't reach here");
} else if let (a, 4) = (3, 4) {    // "(a, 4)" is refutable, and will match
    println!("Matched ({}, 4)", a);
}
}
```

## [Literal patterns](#literal-patterns)

*Literal patterns* match exactly the same value as what is created by the literal. Since negative numbers are not [literals](https://doc.rust-lang.org/stable/reference/expressions/literal-expr.html), literals in patterns may be prefixed by an optional minus sign, which acts like the negation operator.

> Warning
> 
> C string and raw C string literals are accepted in literal patterns, but `&CStr` doesn’t implement structural equality (`#[derive(Eq, PartialEq)]`) and therefore any such `match` on a `&CStr` will be rejected with a type error.

Literal patterns are always refutable.

Examples:

```rust
#![allow(unused)]
fn main() {
for i in -2..5 {
    match i {
        -1 => println!("It's minus one"),
        1 => println!("It's a one"),
        2|4 => println!("It's either a two or a four"),
        _ => println!("Matched none of the arms"),
    }
}
}
```

## [Identifier patterns](#identifier-patterns)

Identifier patterns bind the value they match to a variable in the [value namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html#r-names.namespaces.kinds).

The identifier must be unique within the pattern.

The variable will shadow any variables of the same name in scope. The [scope](https://doc.rust-lang.org/stable/reference/names/scopes.html) of the new binding depends on the context of where the pattern is used (such as a `let` binding or a `match` arm).

Patterns that consist of only an identifier, possibly with a `mut`, match any value and bind it to that identifier. This is the most commonly used pattern in variable declarations and parameters for functions and closures.

```rust
#![allow(unused)]
fn main() {
let mut variable = 10;
fn sum(x: i32, y: i32) -> i32 {
   x + y
}
}
```

To bind the matched value of a pattern to a variable, use the syntax `variable @ subpattern`. For example, the following binds the value 2 to `e` (not the entire range: the range here is a range subpattern).

```rust
#![allow(unused)]
fn main() {
let x = 2;

match x {
    e @ 1 ..= 5 => println!("got a range element {}", e),
    _ => println!("anything"),
}
}
```

By default, identifier patterns bind a variable to a copy of or move from the matched value depending on whether the matched value implements [`Copy`](https://doc.rust-lang.org/stable/reference/special-types-and-traits.html#copy).

This can be changed to bind to a reference by using the `ref` keyword, or to a mutable reference using `ref mut`. For example:

```rust
#![allow(unused)]
fn main() {
let a = Some(10);
match a {
    None => (),
    Some(value) => (),
}

match a {
    None => (),
    Some(ref value) => (),
}
}
```

In the first match expression, the value is copied (or moved). In the second match, a reference to the same memory location is bound to the variable value. This syntax is needed because in destructuring subpatterns the `&` operator can’t be applied to the value’s fields. For example, the following is not valid:

```rust
#![allow(unused)]
fn main() {
struct Person {
   name: String,
   age: u8,
}
let value = Person { name: String::from("John"), age: 23 };
if let Person { name: &person_name, age: 18..=150 } = value { }
}
```

To make it valid, write the following:

```rust
#![allow(unused)]
fn main() {
struct Person {
   name: String,
   age: u8,
}
let value = Person { name: String::from("John"), age: 23 };
if let Person { name: ref person_name, age: 18..=150 } = value { }
}
```

Thus, `ref` is not something that is being matched against. Its objective is exclusively to make the matched binding a reference, instead of potentially copying or moving what was matched.

[Path patterns](#path-patterns) take precedence over identifier patterns.

> Note
> 
> When a pattern is a single-segment identifier, the grammar is ambiguous whether it means an [IdentifierPattern](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-IdentifierPattern) or a [PathPattern](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-PathPattern). This ambiguity can only be resolved after [name resolution](https://doc.rust-lang.org/stable/reference/names/name-resolution.html).
> 
> ```rust
> #![allow(unused)]
fn main() {
const EXPECTED_VALUE: u8 = 42;
//    ^^^^^^^^^^^^^^ That this constant is in scope affects how the
//                   patterns below are treated.

fn check_value(x: u8) -> Result<u8, u8> {
    match x {
        EXPECTED_VALUE => Ok(x),
    //  ^^^^^^^^^^^^^^ Parsed as a `PathPattern` that resolves to
    //                 the constant `42`.
        other_value => Err(x),
    //  ^^^^^^^^^^^ Parsed as an `IdentifierPattern`.
    }
}

// If `EXPECTED_VALUE` were treated as an `IdentifierPattern` above,
// that pattern would always match, making the function always return
// `Ok(_) regardless of the input.
assert_eq!(check_value(42), Ok(42));
assert_eq!(check_value(43), Err(43));
}
> ```

It is an error if `ref` or `ref mut` is specified and the identifier shadows a constant.

Identifier patterns are irrefutable if the `@` subpattern is irrefutable or the subpattern is not specified.

### [Binding modes](#binding-modes)

To service better ergonomics, patterns operate in different *binding modes* in order to make it easier to bind references to values. When a reference value is matched by a non-reference pattern, it will be automatically treated as a `ref` or `ref mut` binding. Example:

```rust
#![allow(unused)]
fn main() {
let x: &Option<i32> = &Some(3);
if let Some(y) = x {
    // y was converted to `ref y` and its type is &i32
}
}
```

*Non-reference patterns* include all patterns except bindings, [wildcard patterns](#wildcard-pattern) (`_`), [`const` patterns](#path-patterns) of reference types, and [reference patterns](#reference-patterns).

If a binding pattern does not explicitly have `ref`, `ref mut`, or `mut`, then it uses the *default binding mode* to determine how the variable is bound.

The default binding mode starts in “move” mode which uses move semantics.

When matching a pattern, the compiler starts from the outside of the pattern and works inwards.

Each time a reference is matched using a non-reference pattern, it will automatically dereference the value and update the default binding mode.

References will set the default binding mode to `ref`.

Mutable references will set the mode to `ref mut` unless the mode is already `ref` in which case it remains `ref`.

If the automatically dereferenced value is still a reference, it is dereferenced and this process repeats.

The binding pattern may only explicitly specify a `ref` or `ref mut` binding mode, or specify mutability with `mut`, when the default binding mode is “move”. For example, these are not accepted:

```rust
#![allow(unused)]
fn main() {
let [mut x] = &[()]; //~ ERROR
let [ref x] = &[()]; //~ ERROR
let [ref mut x] = &mut [()]; //~ ERROR
}
```

> 2024 Edition differences
> 
> Before the 2024 edition, bindings could explicitly specify a `ref` or `ref mut` binding mode even when the default binding mode was not “move”, and they could specify mutability on such bindings with `mut`. In these editions, specifying `mut` on a binding set the binding mode to “move” regardless of the current default binding mode.

Similarly, a reference pattern may only appear when the default binding mode is “move”. For example, this is not accepted:

```rust
#![allow(unused)]
fn main() {
let [&x] = &[&()]; //~ ERROR
}
```

> 2024 Edition differences
> 
> Before the 2024 edition, reference patterns could appear even when the default binding mode was not “move”, and had both the effect of matching against the scrutinee and of causing the default binding mode to be reset to “move”.

Move bindings and reference bindings can be mixed together in the same pattern. Doing so will result in partial move of the object bound to and the object cannot be used afterwards. This applies only if the type cannot be copied.

In the example below, `name` is moved out of `person`. Trying to use `person` as a whole or `person.name` would result in an error because of *partial move*.

Example:

```rust
#![allow(unused)]
fn main() {
struct Person {
   name: String,
   age: u8,
}
let person = Person{ name: String::from("John"), age: 23 };
// `name` is moved from person and `age` referenced
let Person { name, ref age } = person;
}
```

## [Wildcard pattern](#wildcard-pattern)

The *wildcard pattern* (an underscore symbol) matches any value. It is used to ignore values when they don’t matter.

Inside other patterns it matches a single data field (as opposed to the `..` which matches the remaining fields).

Unlike identifier patterns, it does not copy, move or borrow the value it matches.

Examples:

```rust
#![allow(unused)]
fn main() {
let x = 20;
let (a, _) = (10, x);   // the x is always matched by _
assert_eq!(a, 10);

// ignore a function/closure param
let real_part = |a: f64, _: f64| { a };

// ignore a field from a struct
struct RGBA {
   r: f32,
   g: f32,
   b: f32,
   a: f32,
}
let color = RGBA{r: 0.4, g: 0.1, b: 0.9, a: 0.5};
let RGBA{r: red, g: green, b: blue, a: _} = color;
assert_eq!(color.r, red);
assert_eq!(color.g, green);
assert_eq!(color.b, blue);

// accept any Some, with any value
let x = Some(10);
if let Some(_) = x {}
}
```

The wildcard pattern is always irrefutable.

## [Rest pattern](#rest-pattern)

The *rest pattern* (the `..` token) acts as a variable-length pattern which matches zero or more elements that haven’t been matched already before and after.

It may only be used in [tuple](#tuple-patterns), [tuple struct](#tuple-struct-patterns), and [slice](#slice-patterns) patterns, and may only appear once as one of the elements in those patterns. It is also allowed in an [identifier pattern](#identifier-patterns) for [slice patterns](#slice-patterns) only.

The rest pattern is always irrefutable.

Examples:

```rust
#![allow(unused)]
fn main() {
let words = vec!["a", "b", "c"];
let slice = &words[..];
match slice {
    [] => println!("slice is empty"),
    [one] => println!("single element {}", one),
    [head, tail @ ..] => println!("head={} tail={:?}", head, tail),
}

match slice {
    // Ignore everything but the last element, which must be "!".
    [.., "!"] => println!("!!!"),

    // `start` is a slice of everything except the last element, which must be "z".
    [start @ .., "z"] => println!("starts with: {:?}", start),

    // `end` is a slice of everything but the first element, which must be "a".
    ["a", end @ ..] => println!("ends with: {:?}", end),

    // 'whole' is the entire slice and `last` is the final element
    whole @ [.., last] => println!("the last element of {:?} is {}", whole, last),

    rest => println!("{:?}", rest),
}

if let [.., penultimate, _] = slice {
    println!("next to last is {}", penultimate);
}

let tuple = (1, 2, 3, 4, 5);
// The rest pattern may also be used in tuple and tuple
// struct patterns.
match tuple {
    (1, .., y, z) => println!("y={} z={}", y, z),
    (.., 5) => println!("tail must be 5"),
    (..) => println!("matches everything else"),
}
}
```

## [Range patterns](#range-patterns)

*Range patterns* match scalar values within the range defined by their bounds. They comprise a *sigil* (`..` or `..=`) and a bound on one or both sides.

A bound on the left of the sigil is called a *lower bound*. A bound on the right is called an *upper bound*.

The *exclusive range pattern* matches all values from the lower bound up to, but not including the upper bound. It is written as its lower bound, followed by `..`, followed by the upper bound.

For example, a pattern `'m'..'p'` will match only `'m'`, `'n'` and `'o'`, specifically **not** including `'p'`.

The *inclusive range pattern* matches all values from the lower bound up to and including the upper bound. It is written as its lower bound, followed by `..=`, followed by the upper bound.

For example, a pattern `'m'..='p'` will match only the values `'m'`, `'n'`, `'o'`, and `'p'`.

The *from range pattern* matches all values greater than or equal to the lower bound. It is written as its lower bound followed by `..`.

For example, `1..` will match any integer greater than or equal to 1, such as 1, 9, or 9001, or 9007199254740991 (if it is of an appropriate size), but not 0, and not negative numbers for signed integers.

The *to exclusive range pattern* matches all values less than the upper bound. It is written as `..` followed by the upper bound.

For example, `..10` will match any integer less than 10, such as 9, 1, 0, and for signed integer types, all negative values.

The *to inclusive range pattern* matches all values less than or equal to the upper bound. It is written as `..=` followed by the upper bound.

For example, `..=10` will match any integer less than or equal to 10, such as 10, 1, 0, and for signed integer types, all negative values.

A range pattern must be nonempty; it must span at least one value in the set of possible values for its type. In other words:

- In `a..=b`, a ≤ b must be the case. For example, it is an error to have a range pattern `10..=0`, but `10..=10` is allowed.
- In `a..b`, a &lt; b must be the case. For example, it is an error to have a range pattern `10..0` or `10..10`.
- In `..b`, b must not be the smallest value of its type. For example, it is an error to have a range pattern `..-128i8` or `..f64::NEG_INFINITY`.

A bound is written as one of:

- A character, byte, integer, or float literal.
- A `-` followed by an integer or float literal.
- A [path](https://doc.rust-lang.org/stable/reference/expressions/path-expr.html).

> Note
> 
> We syntactically accept more than this for a [*RangePatternBound*](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-RangePatternBound). We later reject the other things semantically.

If a bound is written as a path, after macro resolution, the path must resolve to a constant item of the type `char`, an integer type, or a float type.

The range pattern matches the type of its upper and lower bounds, which must be the same type.

If a bound is a [path](https://doc.rust-lang.org/stable/reference/expressions/path-expr.html), the bound matches the type and has the value of the [constant](https://doc.rust-lang.org/stable/reference/items/constant-items.html) the path resolves to.

If a bound is a literal, the bound matches the type and has the value of the corresponding [literal expression](https://doc.rust-lang.org/stable/reference/expressions/literal-expr.html).

If a bound is a literal preceded by a `-`, the bound matches the same type as the corresponding [literal expression](https://doc.rust-lang.org/stable/reference/expressions/literal-expr.html) and has the value of [negating](https://doc.rust-lang.org/stable/reference/expressions/operator-expr.html#negation-operators) the value of the corresponding literal expression.

For float range patterns, the constant may not be a `NaN`.

Examples:

```rust
#![allow(unused)]
fn main() {
let c = 'f';
let valid_variable = match c {
    'a'..='z' => true,
    'A'..='Z' => true,
    'α'..='ω' => true,
    _ => false,
};

let ph = 10;
println!("{}", match ph {
    0..7 => "acid",
    7 => "neutral",
    8..=14 => "base",
    _ => unreachable!(),
});

let uint: u32 = 5;
match uint {
    0 => "zero!",
    1.. => "positive number!",
};

// using paths to constants:
const TROPOSPHERE_MIN : u8 = 6;
const TROPOSPHERE_MAX : u8 = 20;
const STRATOSPHERE_MIN : u8 = TROPOSPHERE_MAX + 1;
const STRATOSPHERE_MAX : u8 = 50;
const MESOSPHERE_MIN : u8 = STRATOSPHERE_MAX + 1;
const MESOSPHERE_MAX : u8 = 85;
let altitude = 70;
println!("{}", match altitude {
    TROPOSPHERE_MIN..=TROPOSPHERE_MAX => "troposphere",
    STRATOSPHERE_MIN..=STRATOSPHERE_MAX => "stratosphere",
    MESOSPHERE_MIN..=MESOSPHERE_MAX => "mesosphere",
    _ => "outer space, maybe",
});

pub mod binary {
    pub const MEGA : u64 = 1024*1024;
    pub const GIGA : u64 = 1024*1024*1024;
}
let n_items = 20_832_425;
let bytes_per_item = 12;
if let size @ binary::MEGA..=binary::GIGA = n_items * bytes_per_item {
    println!("It fits and occupies {} bytes", size);
}

trait MaxValue {
    const MAX: u64;
}
impl MaxValue for u8 {
    const MAX: u64 = (1 << 8) - 1;
}
impl MaxValue for u16 {
    const MAX: u64 = (1 << 16) - 1;
}
impl MaxValue for u32 {
    const MAX: u64 = (1 << 32) - 1;
}
// using qualified paths:
println!("{}", match 0xfacade {
    0 ..= <u8 as MaxValue>::MAX => "fits in a u8",
    0 ..= <u16 as MaxValue>::MAX => "fits in a u16",
    0 ..= <u32 as MaxValue>::MAX => "fits in a u32",
    _ => "too big",
});
}
```

Range patterns for fix-width integer and `char` types are irrefutable when they span the entire set of possible values of a type. For example, `0u8..=255u8` is irrefutable.

The range of values for an integer type is the closed range from its minimum to maximum value.

The range of values for a `char` type are precisely those ranges containing all Unicode Scalar Values: `'\u{0000}'..='\u{D7FF}'` and `'\u{E000}'..='\u{10FFFF}'`.

[RangeFromPattern](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-RangeFromPattern) cannot be used as a top-level pattern for subpatterns in [slice patterns](#slice-patterns). For example, the pattern `[1.., _]` is not a valid pattern.

> 2021 Edition differences
> 
> Before the 2021 edition, range patterns with both a lower and upper bound may also be written using `...` in place of `..=`, with the same meaning.

## [Reference patterns](#reference-patterns)

Reference patterns dereference the pointers that are being matched and, thus, borrow them.

For example, these two matches on `x: &i32` are equivalent:

```rust
#![allow(unused)]
fn main() {
let int_reference = &3;

let a = match *int_reference { 0 => "zero", _ => "some" };
let b = match int_reference { &0 => "zero", _ => "some" };

assert_eq!(a, b);
}
```

The grammar production for reference patterns has to match the token `&&` to match a reference to a reference because it is a token by itself, not two `&` tokens.

Adding the `mut` keyword dereferences a mutable reference. The mutability must match the mutability of the reference.

Reference patterns are always irrefutable.

## [Struct patterns](#struct-patterns)

Struct patterns match struct, enum, and union values that match all criteria defined by its subpatterns. They are also used to [destructure](#destructuring) a struct, enum, or union value.

On a struct pattern, the fields are referenced by name, index (in the case of tuple structs) or ignored by use of `..`:

```rust
#![allow(unused)]
fn main() {
struct Point {
    x: u32,
    y: u32,
}
let s = Point {x: 1, y: 1};
match s {
    Point {x: 10, y: 20} => (),
    Point {y: 10, x: 20} => (),    // order doesn't matter
    Point {x: 10, ..} => (),
    Point {..} => (),
}

struct PointTuple (
    u32,
    u32,
);
let t = PointTuple(1, 2);
match t {
    PointTuple {0: 10, 1: 20} => (),
    PointTuple {1: 10, 0: 20} => (),   // order doesn't matter
    PointTuple {0: 10, ..} => (),
    PointTuple {..} => (),
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
}
let m = Message::Quit;
match m {
    Message::Quit => (),
    Message::Move {x: 10, y: 20} => (),
    Message::Move {..} => (),
}
}
```

If `..` is not used, a struct pattern used to match a struct is required to specify all fields:

```rust
#![allow(unused)]
fn main() {
struct Struct {
   a: i32,
   b: char,
   c: bool,
}
let mut struct_value = Struct{a: 10, b: 'X', c: false};
match struct_value {
    Struct{a: 10, b: 'X', c: false} => (),
    Struct{a: 10, b: 'X', ref c} => (),
    Struct{a: 10, b: 'X', ref mut c} => (),
    Struct{a: 10, b: 'X', c: _} => (),
    Struct{a: _, b: _, c: _} => (),
}
}
```

A struct pattern used to match a union must specify exactly one field (see [Pattern matching on unions](https://doc.rust-lang.org/stable/reference/items/unions.html#pattern-matching-on-unions)).

The [IDENTIFIER](https://doc.rust-lang.org/stable/reference/identifiers.html#grammar-IDENTIFIER) syntax matches any value and binds it to a variable with the same name as the given field. It is a shorthand for `fieldname: fieldname`. The `ref` and `mut` qualifiers can be included with the behavior as described in [patterns.ident.ref](https://doc.rust-lang.org/stable/reference/patterns.html#r-patterns.ident.ref).

```rust
#![allow(unused)]
fn main() {
struct Struct {
   a: i32,
   b: char,
   c: bool,
}
let struct_value = Struct{a: 10, b: 'X', c: false};
let Struct { a, b, c } = struct_value;
}
```

A struct pattern is refutable if the [PathInExpression](https://doc.rust-lang.org/stable/reference/paths.html#grammar-PathInExpression) resolves to a constructor of an enum with more than one variant, or one of its subpatterns is refutable.

A struct pattern matches against the struct, union, or enum variant whose constructor is resolved from [PathInExpression](https://doc.rust-lang.org/stable/reference/paths.html#grammar-PathInExpression) in the [type namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html#r-names.namespaces.kinds). See [patterns.tuple-struct.namespace](https://doc.rust-lang.org/stable/reference/patterns.html#r-patterns.tuple-struct.namespace) for more details.

## [Tuple struct patterns](#tuple-struct-patterns)

Tuple struct patterns match tuple struct and enum values that match all criteria defined by its subpatterns. They are also used to [destructure](#destructuring) a tuple struct or enum value.

A tuple struct pattern is refutable if the [PathInExpression](https://doc.rust-lang.org/stable/reference/paths.html#grammar-PathInExpression) resolves to a constructor of an enum with more than one variant, or one of its subpatterns is refutable.

A tuple struct pattern matches against the tuple struct or [tuple-like enum variant](https://doc.rust-lang.org/stable/reference/items/enumerations.html#r-items.enum.tuple-expr) whose constructor is resolved from [PathInExpression](https://doc.rust-lang.org/stable/reference/paths.html#grammar-PathInExpression) in the [value namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html#r-names.namespaces.kinds).

> Note
> 
> Conversely, a struct pattern for a tuple struct or [tuple-like enum variant](https://doc.rust-lang.org/stable/reference/items/enumerations.html#r-items.enum.tuple-expr), e.g. `S { 0: _ }`, matches against the tuple struct or variant whose constructor is resolved in the [type namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html#r-names.namespaces.kinds).
> 
> ```rust
> enum E1 { V(u16) }
enum E2 { V(u32) }

// Import `E1::V` from the type namespace only.
mod _0 {
    const V: () = (); // For namespace masking.
    pub(super) use super::E1::*;
}
use _0::*;

// Import `E2::V` from the value namespace only.
mod _1 {
    struct V {} // For namespace masking.
    pub(super) use super::E2::*;
}
use _1::*;

fn f() {
    // This struct pattern matches against the tuple-like
    // enum variant whose constructor was found in the type
    // namespace.
    let V { 0: ..=u16::MAX } = (loop {}) else { loop {} };
    // This tuple struct pattern matches against the tuple-like
    // enum variant whose constructor was found in the value
    // namespace.
    let V(..=u32::MAX) = (loop {}) else { loop {} };
}
// Required due to the odd behavior of `super` within functions.
fn main() {}
> ```
> 
> The Lang team has made certain decisions, such as in [PR #138458](https://github.com/rust-lang/rust/pull/138458), that raise questions about the desirability of using the value namespace in this way for patterns, as described in [PR #140593](https://github.com/rust-lang/rust/pull/140593#issuecomment-2972338457). It might be prudent to not intentionally rely on this nuance in your code.

## [Tuple patterns](#tuple-patterns)

Tuple patterns match tuple values that match all criteria defined by its subpatterns. They are also used to [destructure](#destructuring) a tuple.

The form `(..)` with a single [RestPattern](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-RestPattern) is a special form that does not require a comma, and matches a tuple of any size.

The tuple pattern is refutable when one of its subpatterns is refutable.

An example of using tuple patterns:

```rust
#![allow(unused)]
fn main() {
let pair = (10, "ten");
let (a, b) = pair;

assert_eq!(a, 10);
assert_eq!(b, "ten");
}
```

## [Grouped patterns](#grouped-patterns)

Enclosing a pattern in parentheses can be used to explicitly control the precedence of compound patterns. For example, a reference pattern next to a range pattern such as `&0..=5` is ambiguous and is not allowed, but can be expressed with parentheses.

```rust
#![allow(unused)]
fn main() {
let int_reference = &3;
match int_reference {
    &(0..=5) => (),
    _ => (),
}
}
```

## [Slice patterns](#slice-patterns)

Slice patterns can match both arrays of fixed size and slices of dynamic size.

```rust
#![allow(unused)]
fn main() {
// Fixed size
let arr = [1, 2, 3];
match arr {
    [1, _, _] => "starts with one",
    [a, b, c] => "starts with something else",
};
}
```

```rust
#![allow(unused)]
fn main() {
// Dynamic size
let v = vec![1, 2, 3];
match v[..] {
    [a, b] => { /* this arm will not apply because the length doesn't match */ }
    [a, b, c] => { /* this arm will apply */ }
    _ => { /* this wildcard is required, since the length is not known statically */ }
};
}
```

Slice patterns are irrefutable when matching an array as long as each element is irrefutable.

When matching a slice, it is irrefutable only in the form with a single `..` [rest pattern](https://doc.rust-lang.org/stable/reference/patterns.html#r-patterns.rest) or [identifier pattern](#identifier-patterns) with the `..` rest pattern as a subpattern.

Within a slice, a range pattern without both lower and upper bound must be enclosed in parentheses, as in `(a..)`, to clarify it is intended to match against a single slice element. A range pattern with both lower and upper bound, like `a..=b`, is not required to be enclosed in parentheses.

## [Path patterns](#path-patterns)

*Path patterns* are patterns that refer either to constant values or to structs or enum variants that have no fields.

Unqualified path patterns can refer to:

- enum variants
- structs
- constants
- associated constants

Qualified path patterns can only refer to associated constants.

Path patterns are irrefutable when they refer to structs or an enum variant when the enum has only one variant or a constant whose type is irrefutable. They are refutable when they refer to refutable constants or enum variants for enums with multiple variants.

### [Constant patterns](#constant-patterns)

When a constant `C` of type `T` is used as a pattern, we first check that `T: PartialEq`.

Furthermore we require that the value of `C` *has (recursive) structural equality*, which is defined recursively as follows:

- Integers as well as `str`, `bool` and `char` values always have structural equality.

<!--THE END-->

- Tuples, arrays, and slices have structural equality if all their fields/elements have structural equality. (In particular, `()` and `[]` always have structural equality.)

<!--THE END-->

- References have structural equality if the value they point to has structural equality.

<!--THE END-->

- A value of `struct` or `enum` type has structural equality if its `PartialEq` instance is derived via `#[derive(PartialEq)]`, and all fields (for enums: of the active variant) have structural equality.

<!--THE END-->

- A raw pointer has structural equality if it was defined as a constant integer (and then cast/transmuted).

<!--THE END-->

- A float value has structural equality if it is not a `NaN`.

<!--THE END-->

- Nothing else has structural equality.

In particular, the value of `C` must be known at pattern-building time (which is pre-monomorphization). This means that associated consts that involve generic parameters cannot be used as patterns.

The value of `C` must not contain any references to mutable statics (`static mut` items or interior mutable `static` items) or `extern` statics.

After ensuring all conditions are met, the constant value is translated into a pattern, and now behaves exactly as-if that pattern had been written directly. In particular, it fully participates in exhaustiveness checking. (For raw pointers, constants are the only way to write such patterns. Only `_` is ever considered exhaustive for these types.)

## [Or-patterns](#or-patterns)

*Or-patterns* are patterns that match on one of two or more sub-patterns (for example `A | B | C`). They can nest arbitrarily. Syntactically, or-patterns are allowed in any of the places where other patterns are allowed (represented by the [Pattern](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-Pattern) production), with the exceptions of `let`-bindings and function and closure parameters (represented by the [PatternNoTopAlt](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-PatternNoTopAlt) production).

### [Static semantics](#static-semantics)

1. Given a pattern `p | q` at some depth for some arbitrary patterns `p` and `q`, the pattern is considered ill-formed if:
   
   - the type inferred for `p` does not unify with the type inferred for `q`, or
   - the same set of bindings are not introduced in `p` and `q`, or
   - the type of any two bindings with the same name in `p` and `q` do not unify with respect to types or binding modes.
   
   Unification of types is in all instances aforementioned exact and implicit [type coercions](https://doc.rust-lang.org/stable/reference/type-coercions.html) do not apply.

<!--THE END-->

2. When type checking an expression `match e_s { a_1 => e_1, ... a_n => e_n }`, for each match arm `a_i` which contains a pattern of form `p_i | q_i`, the pattern `p_i | q_i` is considered ill formed if, at the depth `d` where it exists the fragment of `e_s` at depth `d`, the type of the expression fragment does not unify with `p_i | q_i`.

<!--THE END-->

3. With respect to exhaustiveness checking, a pattern `p | q` is considered to cover `p` as well as `q`. For some constructor `c(x, ..)` the distributive law applies such that `c(p | q, ..rest)` covers the same set of value as `c(p, ..rest) | c(q, ..rest)` does. This can be applied recursively until there are no more nested patterns of form `p | q` other than those that exist at the top level.
   
   Note that by *“constructor”* we do not refer to tuple struct patterns, but rather we refer to a pattern for any product type. This includes enum variants, tuple structs, structs with named fields, arrays, tuples, and slices.

### [Dynamic semantics](#dynamic-semantics)

1. The dynamic semantics of pattern matching a scrutinee expression `e_s` against a pattern `c(p | q, ..rest)` at depth `d` where `c` is some constructor, `p` and `q` are arbitrary patterns, and `rest` is optionally any remaining potential factors in `c`, is defined as being the same as that of `c(p, ..rest) | c(q, ..rest)`.

### [Precedence with other undelimited patterns](#precedence-with-other-undelimited-patterns)

As shown elsewhere in this chapter, there are several types of patterns that are syntactically undelimited, including identifier patterns, reference patterns, and or-patterns. Or-patterns always have the lowest-precedence. This allows us to reserve syntactic space for a possible future type ascription feature and also to reduce ambiguity. For example, `x @ A(..) | B(..)` will result in an error that `x` is not bound in all patterns. `&A(x) | B(x)` will result in a type mismatch between `x` in the different subpatterns.

* * *

1. The [ObsoleteRangePattern](https://doc.rust-lang.org/stable/reference/patterns.html#grammar-ObsoleteRangePattern) syntax has been removed in the 2021 edition. [↩](#fr-obsolete-range-edition-1)