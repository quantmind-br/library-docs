---
title: Glossary - The Rust Reference
url: https://doc.rust-lang.org/reference/glossary.html#r-glossary.abi
source: crawler
fetched_at: 2026-05-06T21:25:14.146657006-03:00
rendered_js: false
word_count: 1725
summary: This document provides a comprehensive glossary of technical terminology used throughout the Rust programming language reference.
tags:
    - rust
    - programming-glossary
    - language-reference
    - technical-definitions
    - compiler-concepts
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Glossary](#glossary)

### [Abstract syntax tree](#abstract-syntax-tree)

An ‘abstract syntax tree’, or ‘AST’, is an intermediate representation of the structure of the program when the compiler is compiling it.

### [Alignment](#alignment)

The alignment of a value specifies what addresses values are preferred to start at. Always a power of two. References to a value must be aligned. [More](https://doc.rust-lang.org/reference/type-layout.html#size-and-alignment).

### [Application binary interface (ABI)](#application-binary-interface-abi)

An *application binary interface* (ABI) defines how compiled code interacts with other compiled code. With [`extern` blocks](https://doc.rust-lang.org/reference/items/external-blocks.html#r-items.extern) and [`extern fn`](https://doc.rust-lang.org/reference/items/functions.html#r-items.fn.extern), *ABI strings* affect:

- **Calling convention**: How function arguments are passed, values are returned (e.g., in registers or on the stack), and who is responsible for cleaning up the stack.
- **Unwinding**: Whether stack unwinding is allowed. For example, the `"C-unwind"` ABI allows unwinding across the FFI boundary, while the `"C"` ABI does not.

### [Arity](#arity)

Arity refers to the number of arguments a function or operator takes. For some examples, `f(2, 3)` and `g(4, 6)` have arity 2, while `h(8, 2, 6)` has arity 3. The `!` operator has arity 1.

### [Array](#array)

An array, sometimes also called a fixed-size array or an inline array, is a value describing a collection of elements, each selected by an index that can be computed at run time by the program. It occupies a contiguous region of memory.

### [Associated item](#associated-item)

An associated item is an item that is associated with another item. Associated items are defined in [implementations](https://doc.rust-lang.org/reference/items/implementations.html) and declared in [traits](https://doc.rust-lang.org/reference/items/traits.html). Only functions, constants, and type aliases can be associated. Contrast to a [free item](#free-item).

### [Blanket implementation](#blanket-implementation)

Any implementation where a type appears [uncovered](#uncovered-type). `impl<T> Foo for T`, `impl<T> Bar<T> for T`, `impl<T> Bar<Vec<T>> for T`, and `impl<T> Bar<T> for Vec<T>` are considered blanket impls. However, `impl<T> Bar<Vec<T>> for Vec<T>` is not a blanket impl, as all instances of `T` which appear in this `impl` are covered by `Vec`.

### [Bound](#bound)

Bounds are constraints on a type or trait. For example, if a bound is placed on the argument a function takes, types passed to that function must abide by that constraint.

### [Combinator](#combinator)

Combinators are higher-order functions that apply only functions and earlier defined combinators to provide a result from its arguments. They can be used to manage control flow in a modular fashion.

### [Crate](#crate)

A crate is the unit of compilation and linking. There are different [types of crates](https://doc.rust-lang.org/reference/linkage.html), such as libraries or executables. Crates may link and refer to other library crates, called external crates. A crate has a self-contained tree of [modules](https://doc.rust-lang.org/reference/items/modules.html), starting from an unnamed root module called the crate root. [Items](https://doc.rust-lang.org/reference/items.html) may be made visible to other crates by marking them as public in the crate root, including through [paths](https://doc.rust-lang.org/reference/paths.html) of public modules. [More](https://doc.rust-lang.org/reference/crates-and-source-files.html).

### [Dispatch](#dispatch)

Dispatch is the mechanism to determine which specific version of code is actually run when it involves polymorphism. Two major forms of dispatch are static dispatch and dynamic dispatch. Rust supports dynamic dispatch through the use of [trait objects](https://doc.rust-lang.org/reference/types/trait-object.html#r-type.trait-object).

### [Dynamically sized type](#dynamically-sized-type)

A dynamically sized type (DST) is a type without a statically known size or alignment.

### [Entity](#entity)

An [*entity*](https://doc.rust-lang.org/reference/names.html) is a language construct that can be referred to in some way within the source program, usually via a [path](https://doc.rust-lang.org/reference/paths.html). Entities include [types](https://doc.rust-lang.org/reference/types.html), [items](https://doc.rust-lang.org/reference/items.html), [generic parameters](https://doc.rust-lang.org/reference/items/generics.html), [variable bindings](https://doc.rust-lang.org/reference/patterns.html), [loop labels](https://doc.rust-lang.org/reference/tokens.html#lifetimes-and-loop-labels), [lifetimes](https://doc.rust-lang.org/reference/tokens.html#lifetimes-and-loop-labels), [fields](https://doc.rust-lang.org/reference/expressions/field-expr.html), [attributes](https://doc.rust-lang.org/reference/attributes.html), and [lints](https://doc.rust-lang.org/reference/attributes/diagnostics.html#lint-check-attributes).

### [Expression](#expression)

An expression is a combination of values, constants, variables, operators and functions that evaluate to a single value, with or without side-effects.

For example, `2 + (3 * 4)` is an expression that returns the value 14.

### [Free item](#free-item)

An [item](https://doc.rust-lang.org/reference/items.html) that is not a member of an [implementation](https://doc.rust-lang.org/reference/items/implementations.html), such as a *free function* or a *free const*. Contrast to an [associated item](#associated-item).

### [Fundamental traits](#fundamental-traits)

A fundamental trait is one where adding an impl of it for an existing type is a breaking change. The `Fn` traits and `Sized` are fundamental.

### [Fundamental type constructors](#fundamental-type-constructors)

A fundamental type constructor is a type where implementing a [blanket implementation](#blanket-implementation) over it is a breaking change. `&`, `&mut`, `Box`, and `Pin` are fundamental.

Any time a type `T` is considered [local](#local-type), `&T`, `&mut T`, `Box<T>`, and `Pin<T>` are also considered local. Fundamental type constructors cannot [cover](#uncovered-type) other types. Any time the term “covered type” is used, the `T` in `&T`, `&mut T`, `Box<T>`, and `Pin<T>` is not considered covered.

### [Inhabited](#inhabited)

A type is inhabited if it has constructors and therefore can be instantiated. An inhabited type is not “empty” in the sense that there can be values of the type. Opposite of [Uninhabited](#uninhabited).

### [Inherent implementation](#inherent-implementation)

An [implementation](https://doc.rust-lang.org/reference/items/implementations.html) that applies to a nominal type, not to a trait-type pair. [More](https://doc.rust-lang.org/reference/items/implementations.html#inherent-implementations).

### [Inherent method](#inherent-method)

A [method](https://doc.rust-lang.org/reference/items/associated-items.html#methods) defined in an [inherent implementation](https://doc.rust-lang.org/reference/items/implementations.html#inherent-implementations), not in a trait implementation.

### [Initialized](#initialized)

A variable is initialized if it has been assigned a value and hasn’t since been moved from. All other memory locations are assumed to be uninitialized. Only unsafe Rust can create a memory location without initializing it.

### [Local trait](#local-trait)

A `trait` which was defined in the current crate. A trait definition is local or not independent of applied type arguments. Given `trait Foo<T, U>`, `Foo` is always local, regardless of the types substituted for `T` and `U`.

### [Local type](#local-type)

A `struct`, `enum`, or `union` which was defined in the current crate. This is not affected by applied type arguments. `struct Foo` is considered local, but `Vec<Foo>` is not. `LocalType<ForeignType>` is local. Type aliases do not affect locality.

### [Module](#module)

A module is a container for zero or more [items](https://doc.rust-lang.org/reference/items.html). Modules are organized in a tree, starting from an unnamed module at the root called the crate root or the root module. [Paths](https://doc.rust-lang.org/reference/paths.html) may be used to refer to items from other modules, which may be restricted by [visibility rules](https://doc.rust-lang.org/reference/visibility-and-privacy.html). [More](https://doc.rust-lang.org/reference/items/modules.html)

### [Name](#name)

A [*name*](https://doc.rust-lang.org/reference/names.html) is an [identifier](https://doc.rust-lang.org/reference/identifiers.html) or [lifetime or loop label](https://doc.rust-lang.org/reference/tokens.html#lifetimes-and-loop-labels) that refers to an [entity](#entity). A *name binding* is when an entity declaration introduces an identifier or label associated with that entity. [Paths](https://doc.rust-lang.org/reference/paths.html), identifiers, and labels are used to refer to an entity.

### [Name resolution](#name-resolution)

[*Name resolution*](https://doc.rust-lang.org/reference/names/name-resolution.html) is the compile-time process of tying [paths](https://doc.rust-lang.org/reference/paths.html), [identifiers](https://doc.rust-lang.org/reference/identifiers.html), and [labels](https://doc.rust-lang.org/reference/tokens.html#lifetimes-and-loop-labels) to [entity](#entity) declarations.

### [Namespace](#namespace)

A *namespace* is a logical grouping of declared [names](#name) based on the kind of [entity](#entity) the name refers to. Namespaces allow the occurrence of a name in one namespace to not conflict with the same name in another namespace.

Within a namespace, names are organized in a hierarchy, where each level of the hierarchy has its own collection of named entities.

### [Nominal types](#nominal-types)

Types that can be referred to by a path directly. Specifically [enums](https://doc.rust-lang.org/reference/items/enumerations.html), [structs](https://doc.rust-lang.org/reference/items/structs.html), [unions](https://doc.rust-lang.org/reference/items/unions.html), and [trait object types](https://doc.rust-lang.org/reference/types/trait-object.html).

### [Dyn-compatible traits](#dyn-compatible-traits)

[Traits](https://doc.rust-lang.org/reference/items/traits.html) that can be used in [trait object types](https://doc.rust-lang.org/reference/types/trait-object.html) (`dyn Trait`). Only traits that follow specific [rules](https://doc.rust-lang.org/reference/items/traits.html#dyn-compatibility) are *dyn compatible*.

These were formerly known as *object safe* traits.

### [Path](#path)

A [*path*](https://doc.rust-lang.org/reference/paths.html) is a sequence of one or more path segments used to refer to an [entity](#entity) in the current scope or other levels of a [namespace](#namespace) hierarchy.

### [Prelude](#prelude)

Prelude, or The Rust Prelude, is a small collection of items - mostly traits - that are imported into every module of every crate. The traits in the prelude are pervasive.

### [Scope](#scope)

A [*scope*](https://doc.rust-lang.org/reference/names/scopes.html) is the region of source text where a named [entity](#entity) may be referenced with that name.

### [Scrutinee](#scrutinee)

A scrutinee is the expression that is matched on in `match` expressions and similar pattern matching constructs. For example, in `match x { A => 1, B => 2 }`, the expression `x` is the scrutinee.

### [Size](#size)

The size of a value has two definitions.

The first is that it is how much memory must be allocated to store that value.

The second is that it is the offset in bytes between successive elements in an array with that item type.

It is a multiple of the alignment, including zero. The size can change depending on compiler version (as new optimizations are made) and target platform (similar to how `usize` varies per-platform).

[More](https://doc.rust-lang.org/reference/type-layout.html#size-and-alignment).

### [Slice](#slice)

A slice is dynamically-sized view into a contiguous sequence, written as `[T]`.

It is often seen in its borrowed forms, either mutable or shared. The shared slice type is `&[T]`, while the mutable slice type is `&mut [T]`, where `T` represents the element type.

### [Statement](#statement)

A statement is the smallest standalone element of a programming language that commands a computer to perform an action.

### [String literal](#string-literal)

A string literal is a string stored directly in the final binary, and so will be valid for the `'static` duration.

Its type is `'static` duration borrowed string slice, `&'static str`.

### [String slice](#string-slice)

A string slice is the most primitive string type in Rust, written as `str`. It is often seen in its borrowed forms, either mutable or shared. The shared string slice type is `&str`, while the mutable string slice type is `&mut str`.

Strings slices are always valid UTF-8.

### [Trait](#trait)

A trait is a language item that is used for describing the functionalities a type must provide. It allows a type to make certain promises about its behavior.

Generic functions and generic structs can use traits to constrain, or bound, the types they accept.

### [Turbofish](#turbofish)

Paths with generic parameters in expressions must prefix the opening brackets with a `::`. Combined with the angular brackets for generics, this looks like a fish `::<>`. As such, this syntax is colloquially referred to as turbofish syntax.

Examples:

```rust
#![allow(unused)]
fn main() {
let ok_num = Ok::<_, ()>(5);
let vec = [1, 2, 3].iter().map(|n| n * 2).collect::<Vec<_>>();
}
```

This `::` prefix is required to disambiguate generic paths with multiple comparisons in a comma-separate list. See [the bastion of the turbofish](https://github.com/rust-lang/rust/blob/1.58.0/src/test/ui/parser/bastion-of-the-turbofish.rs) for an example where not having the prefix would be ambiguous.

### [Uncovered type](#uncovered-type)

A type which does not appear as an argument to another type. For example, `T` is uncovered, but the `T` in `Vec<T>` is covered. This is only relevant for type arguments.

### [Undefined behavior](#undefined-behavior)

Compile-time or run-time behavior that is not specified. This may result in, but is not limited to: process termination or corruption; improper, incorrect, or unintended computation; or platform-specific results. [More](https://doc.rust-lang.org/reference/behavior-considered-undefined.html).

### [Uninhabited](#uninhabited)

A type is uninhabited if it has no constructors and therefore can never be instantiated. An uninhabited type is “empty” in the sense that there are no values of the type. The canonical example of an uninhabited type is the [never type](https://doc.rust-lang.org/reference/types/never.html) `!`, or an enum with no variants `enum Never { }`. Opposite of [Inhabited](#inhabited).