---
title: Enumerations - The Rust Reference
url: https://doc.rust-lang.org/reference/items/enumerations.html
source: crawler
fetched_at: 2026-05-06T21:27:01.44952633-03:00
rendered_js: false
word_count: 646
summary: This document explains the definition, structure, and discriminant handling of enumerations in the Rust programming language.
tags:
    - rust
    - enums
    - data-types
    - discriminants
    - memory-layout
    - programming-language
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Enumerations](#enumerations)

An *enumeration*, also referred to as an *enum*, is a simultaneous definition of a nominal [enumerated type](https://doc.rust-lang.org/reference/types/enum.html) as well as a set of *constructors*, that can be used to create or pattern-match values of the corresponding enumerated type.

Enumerations are declared with the keyword `enum`.

The `enum` declaration defines the enumeration type in the [type namespace](https://doc.rust-lang.org/reference/names/namespaces.html) of the module or block where it is located.

An example of an `enum` item and its use:

```rust
#![allow(unused)]
fn main() {
enum Animal {
    Dog,
    Cat,
}

let mut a: Animal = Animal::Dog;
a = Animal::Cat;
}
```

Enum constructors can have either named or unnamed fields:

```rust
#![allow(unused)]
fn main() {
enum Animal {
    Dog(String, f64),
    Cat { name: String, weight: f64 },
}

let mut a: Animal = Animal::Dog("Cocoa".to_string(), 37.2);
a = Animal::Cat { name: "Spotty".to_string(), weight: 2.7 };
}
```

In this example, `Cat` is a *struct-like enum variant*, whereas `Dog` is simply called an enum variant.

An enum where no constructors contain fields is called a *field-less enum*. For example, this is a fieldless enum:

```rust
#![allow(unused)]
fn main() {
enum Fieldless {
    Tuple(),
    Struct{},
    Unit,
}
}
```

If a field-less enum only contains unit variants, the enum is called an *unit-only enum*. For example:

```rust
#![allow(unused)]
fn main() {
enum Enum {
    Foo = 3,
    Bar = 2,
    Baz = 1,
}
}
```

Variant constructors are similar to [struct](https://doc.rust-lang.org/reference/items/structs.html) definitions, and can be referenced by a path from the enumeration name, including in [use declarations](https://doc.rust-lang.org/reference/items/use-declarations.html).

Each variant defines its type in the [type namespace](https://doc.rust-lang.org/reference/names/namespaces.html), though that type cannot be used as a type specifier. Tuple-like and unit-like variants also define a constructor in the [value namespace](https://doc.rust-lang.org/reference/names/namespaces.html).

A struct-like variant can be instantiated with a [struct expression](https://doc.rust-lang.org/reference/expressions/struct-expr.html).

A tuple-like variant can be instantiated with a [call expression](https://doc.rust-lang.org/reference/expressions/call-expr.html) or a [struct expression](https://doc.rust-lang.org/reference/expressions/struct-expr.html).

A unit-like variant can be instantiated with a [path expression](https://doc.rust-lang.org/reference/expressions/path-expr.html) or a [struct expression](https://doc.rust-lang.org/reference/expressions/struct-expr.html). For example:

```rust
#![allow(unused)]
fn main() {
enum Examples {
    UnitLike,
    TupleLike(i32),
    StructLike { value: i32 },
}

use Examples::*; // Creates aliases to all variants.
let x = UnitLike; // Path expression of the const item.
let x = UnitLike {}; // Struct expression.
let y = TupleLike(123); // Call expression.
let y = TupleLike { 0: 123 }; // Struct expression using integer field names.
let z = StructLike { value: 123 }; // Struct expression.
}
```

## [Discriminants](#discriminants)

Each enum instance has a *discriminant*: an integer logically associated to it that is used to determine which variant it holds.

Under the [`Rust` representation](https://doc.rust-lang.org/reference/type-layout.html#the-rust-representation), the discriminant is interpreted as an `isize` value. However, the compiler is allowed to use a smaller type (or another means of distinguishing variants) in its actual memory layout.

### [Assigning discriminant values](#assigning-discriminant-values)

#### [Explicit discriminants](#explicit-discriminants)

In two circumstances, the discriminant of a variant may be explicitly set by following the variant name with `=` and a [constant expression](https://doc.rust-lang.org/reference/const_eval.html#constant-expressions):

1. if the enumeration is “[unit-only](#unit-only-enum)”.

<!--THE END-->

2. if a [primitive representation](https://doc.rust-lang.org/reference/type-layout.html#primitive-representations) is used. For example:
   
   ```rust
   #![allow(unused)]
   fn main() {
   #[repr(u8)]
   enum Enum {
       Unit = 3,
       Tuple(u16),
       Struct {
           a: u8,
           b: u16,
       } = 1,
   }
   }
   ```

#### [Implicit discriminants](#implicit-discriminants)

If a discriminant for a variant is not specified, then it is set to one higher than the discriminant of the previous variant in the declaration. If the discriminant of the first variant in the declaration is unspecified, then it is set to zero.

```rust
#![allow(unused)]
fn main() {
enum Foo {
    Bar,            // 0
    Baz = 123,      // 123
    Quux,           // 124
}

let baz_discriminant = Foo::Baz as u32;
assert_eq!(baz_discriminant, 123);
}
```

#### [Restrictions](#restrictions)

It is an error when two variants share the same discriminant.

```rust
#![allow(unused)]
fn main() {
enum SharedDiscriminantError {
    SharedA = 1,
    SharedB = 1
}

enum SharedDiscriminantError2 {
    Zero,       // 0
    One,        // 1
    OneToo = 1  // 1 (collision with previous!)
}
}
```

It is also an error to have an unspecified discriminant where the previous discriminant is the maximum value for the size of the discriminant.

```rust
#![allow(unused)]
fn main() {
#[repr(u8)]
enum OverflowingDiscriminantError {
    Max = 255,
    MaxPlusOne // Would be 256, but that overflows the enum.
}

#[repr(u8)]
enum OverflowingDiscriminantError2 {
    MaxMinusOne = 254, // 254
    Max,               // 255
    MaxPlusOne         // Would be 256, but that overflows the enum.
}
}
```

### [Accessing discriminant](#accessing-discriminant)

#### [Via `mem::discriminant`](#via-memdiscriminant)

[`std::mem::discriminant`](https://doc.rust-lang.org/core/mem/fn.discriminant.html) returns an opaque reference to the discriminant of an enum value which can be compared. This cannot be used to get the value of the discriminant.

#### [Casting](#casting)

If an enumeration is [unit-only](#unit-only-enum) (with no tuple and struct variants), then its discriminant can be directly accessed with a [numeric cast](https://doc.rust-lang.org/reference/expressions/operator-expr.html#semantics); e.g.:

```rust
#![allow(unused)]
fn main() {
enum Enum {
    Foo,
    Bar,
    Baz,
}

assert_eq!(0, Enum::Foo as isize);
assert_eq!(1, Enum::Bar as isize);
assert_eq!(2, Enum::Baz as isize);
}
```

[Field-less enums](#field-less-enum) can be cast if they do not have explicit discriminants, or where only unit variants are explicit.

```rust
#![allow(unused)]
fn main() {
enum Fieldless {
    Tuple(),
    Struct{},
    Unit,
}

assert_eq!(0, Fieldless::Tuple() as isize);
assert_eq!(1, Fieldless::Struct{} as isize);
assert_eq!(2, Fieldless::Unit as isize);

#[repr(u8)]
enum FieldlessWithDiscriminants {
    First = 10,
    Tuple(),
    Second = 20,
    Struct{},
    Unit,
}

assert_eq!(10, FieldlessWithDiscriminants::First as u8);
assert_eq!(11, FieldlessWithDiscriminants::Tuple() as u8);
assert_eq!(20, FieldlessWithDiscriminants::Second as u8);
assert_eq!(21, FieldlessWithDiscriminants::Struct{} as u8);
assert_eq!(22, FieldlessWithDiscriminants::Unit as u8);
}
```

#### [Pointer casting](#pointer-casting)

If the enumeration specifies a [primitive representation](https://doc.rust-lang.org/reference/type-layout.html#primitive-representations), then the discriminant may be reliably accessed via unsafe pointer casting:

```rust
#![allow(unused)]
fn main() {
#[repr(u8)]
enum Enum {
    Unit,
    Tuple(bool),
    Struct{a: bool},
}

impl Enum {
    fn discriminant(&self) -> u8 {
        unsafe { *(self as *const Self as *const u8) }
    }
}

let unit_like = Enum::Unit;
let tuple_like = Enum::Tuple(true);
let struct_like = Enum::Struct{a: false};

assert_eq!(0, unit_like.discriminant());
assert_eq!(1, tuple_like.discriminant());
assert_eq!(2, struct_like.discriminant());
}
```

## [Zero-variant enums](#zero-variant-enums)

Enums with zero variants are known as *zero-variant enums*. As they have no valid values, they cannot be instantiated.

```rust
#![allow(unused)]
fn main() {
enum ZeroVariants {}
}
```

Zero-variant enums are equivalent to the [never type](https://doc.rust-lang.org/reference/types/never.html), but they cannot be coerced into other types.

```rust
#![allow(unused)]
fn main() {
enum ZeroVariants {}
let x: ZeroVariants = panic!();
let y: u32 = x; // mismatched type error
}
```

## [Variant visibility](#variant-visibility)

Enum variants syntactically allow a [Visibility](https://doc.rust-lang.org/reference/visibility-and-privacy.html#grammar-Visibility) annotation, but this is rejected when the enum is validated. This allows items to be parsed with a unified syntax across different contexts where they are used.

```rust
#![allow(unused)]
fn main() {
macro_rules! mac_variant {
    ($vis:vis $name:ident) => {
        enum $name {
            $vis Unit,

            $vis Tuple(u8, u16),

            $vis Struct { f: u8 },
        }
    }
}

// Empty `vis` is allowed.
mac_variant! { E }

// This is allowed, since it is removed before being validated.
#[cfg(false)]
enum E {
    pub U,
    pub(crate) T(u8),
    pub(super) T { f: String }
}
}
```