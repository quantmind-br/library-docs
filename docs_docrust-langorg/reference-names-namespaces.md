---
title: Namespaces - The Rust Reference
url: https://doc.rust-lang.org/reference/names/namespaces.html
source: crawler
fetched_at: 2026-05-06T21:25:12.093779474-03:00
rendered_js: false
word_count: 546
summary: This document defines the concept of namespaces in the Rust programming language, categorizing entities into type, value, macro, lifetime, and label namespaces to resolve naming conflicts.
tags:
    - rust-language
    - namespaces
    - name-resolution
    - type-system
    - programming-concepts
    - scope
category: concept
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Namespaces](#namespaces)

A *namespace* is a logical grouping of declared [names](https://doc.rust-lang.org/reference/names.html). Names are segregated into separate namespaces based on the kind of entity the name refers to. Namespaces allow the occurrence of a name in one namespace to not conflict with the same name in another namespace.

There are several different namespaces that each contain different kinds of entities. The usage of a name will look for the declaration of that name in different namespaces, based on the context, as described in the [name resolution](https://doc.rust-lang.org/reference/names/name-resolution.html) chapter.

The following is a list of namespaces, with their corresponding entities:

- Type Namespace
  
  - [Module declarations](https://doc.rust-lang.org/reference/items/modules.html)
  - [External crate declarations](https://doc.rust-lang.org/reference/items/extern-crates.html)
  - [External crate prelude](https://doc.rust-lang.org/reference/names/preludes.html#extern-prelude) items
  - [Struct](https://doc.rust-lang.org/reference/items/structs.html), [union](https://doc.rust-lang.org/reference/items/unions.html), [enum](https://doc.rust-lang.org/reference/items/enumerations.html), enum variant declarations
  - [Trait item declarations](https://doc.rust-lang.org/reference/items/traits.html)
  - [Type aliases](https://doc.rust-lang.org/reference/items/type-aliases.html)
  - [Associated type declarations](https://doc.rust-lang.org/reference/items/associated-items.html#associated-types)
  - Built-in types: [boolean](https://doc.rust-lang.org/reference/types/boolean.html), [numeric](https://doc.rust-lang.org/reference/types/numeric.html), [`char`](https://doc.rust-lang.org/reference/types/char.html), and [`str`](https://doc.rust-lang.org/reference/types/str.html)
  - [Generic type parameters](https://doc.rust-lang.org/reference/items/generics.html)
  - [`Self` type](https://doc.rust-lang.org/reference/paths.html#self-1)
  - [Tool attribute modules](https://doc.rust-lang.org/reference/attributes.html#tool-attributes)
- Value Namespace
  
  - [Function declarations](https://doc.rust-lang.org/reference/items/functions.html)
  - [Constant item declarations](https://doc.rust-lang.org/reference/items/constant-items.html)
  - [Static item declarations](https://doc.rust-lang.org/reference/items/static-items.html)
  - [Struct constructors](https://doc.rust-lang.org/reference/items/structs.html)
  - [Enum variant constructors](https://doc.rust-lang.org/reference/items/enumerations.html)
  - [`Self` constructors](https://doc.rust-lang.org/reference/paths.html#self-1)
  - [Generic const parameters](https://doc.rust-lang.org/reference/items/generics.html#const-generics)
  - [Associated const declarations](https://doc.rust-lang.org/reference/items/associated-items.html#associated-constants)
  - [Associated function declarations](https://doc.rust-lang.org/reference/items/associated-items.html#associated-functions-and-methods)
  - Local bindings — [`let`](https://doc.rust-lang.org/reference/statements.html#let-statements), [`if let`](https://doc.rust-lang.org/reference/expressions/if-expr.html#if-let-patterns), [`while let`](https://doc.rust-lang.org/reference/expressions/loop-expr.html#while-let-patterns), [`for`](https://doc.rust-lang.org/reference/expressions/loop-expr.html#iterator-loops), [`match`](https://doc.rust-lang.org/reference/expressions/match-expr.html) arms, [function parameters](https://doc.rust-lang.org/reference/items/functions.html#function-parameters), [closure parameters](https://doc.rust-lang.org/reference/expressions/closure-expr.html)
  - Captured [closure](https://doc.rust-lang.org/reference/expressions/closure-expr.html) variables
- Macro Namespace
  
  - [`macro_rules` declarations](https://doc.rust-lang.org/reference/macros-by-example.html)
  - [Built-in attributes](https://doc.rust-lang.org/reference/attributes.html#built-in-attributes-index)
  - [Tool attributes](https://doc.rust-lang.org/reference/attributes.html#tool-attributes)
  - [Function-like procedural macros](https://doc.rust-lang.org/reference/procedural-macros.html#the-proc_macro-attribute)
  - [Derive macros](https://doc.rust-lang.org/reference/procedural-macros.html#r-macro.proc.derive)
  - [Derive macro helpers](https://doc.rust-lang.org/reference/procedural-macros.html#derive-macro-helper-attributes)
  - [Attribute macros](https://doc.rust-lang.org/reference/procedural-macros.html#the-proc_macro_attribute-attribute)
- Lifetime Namespace
  
  - [Generic lifetime parameters](https://doc.rust-lang.org/reference/items/generics.html)
- Label Namespace
  
  - [Loop labels](https://doc.rust-lang.org/reference/expressions/loop-expr.html#loop-labels)
  - [Block labels](https://doc.rust-lang.org/reference/expressions/loop-expr.html#r-expr.loop.block-labels)

An example of how overlapping names in different namespaces can be used unambiguously:

```rust
#![allow(unused)]
fn main() {
// Foo introduces a type in the type namespace and a constructor in the value
// namespace.
struct Foo(u32);

// The `Foo` macro is declared in the macro namespace.
macro_rules! Foo {
    () => {};
}

// `Foo` in the `f` parameter type refers to `Foo` in the type namespace.
// `'Foo` introduces a new lifetime in the lifetime namespace.
fn example<'Foo>(f: Foo) {
    // `Foo` refers to the `Foo` constructor in the value namespace.
    let ctor = Foo;
    // `Foo` refers to the `Foo` macro in the macro namespace.
    Foo!{}
    // `'Foo` introduces a label in the label namespace.
    'Foo: loop {
        // `'Foo` refers to the `'Foo` lifetime parameter, and `Foo`
        // refers to the type namespace.
        let x: &'Foo Foo;
        // `'Foo` refers to the label.
        break 'Foo;
    }
}
}
```

## [Named entities without a namespace](#named-entities-without-a-namespace)

The following entities have explicit names, but the names are not a part of any specific namespace.

### [Fields](#fields)

Even though struct, enum, and union fields are named, the named fields do not live in an explicit namespace. They can only be accessed via a [field expression](https://doc.rust-lang.org/reference/expressions/field-expr.html), which only inspects the field names of the specific type being accessed.

### [Use declarations](#use-declarations)

A [use declaration](https://doc.rust-lang.org/reference/items/use-declarations.html) has named aliases that it imports into scope, but the `use` item itself does not belong to a specific namespace. Instead, it can introduce aliases into multiple namespaces, depending on the item kind being imported.

## [Sub-namespaces](#sub-namespaces)

The macro namespace is split into two sub-namespaces: one for [bang-style macros](https://doc.rust-lang.org/reference/macros.html) and one for [attributes](https://doc.rust-lang.org/reference/attributes.html). When an attribute is resolved, any bang-style macros in scope will be ignored. And conversely resolving a bang-style macro will ignore attribute macros in scope. This prevents one style from shadowing another.

For example, the [`cfg` attribute](https://doc.rust-lang.org/reference/conditional-compilation.html#the-cfg-attribute) and the [`cfg` macro](https://doc.rust-lang.org/reference/conditional-compilation.html#the-cfg-macro) are two different entities with the same name in the macro namespace, but they can still be used in their respective context.

> Note
> 
> `use` imports still cannot create duplicate bindings of the same name in a module or block, regardless of sub-namespace.
> 
> ```rust
> #[macro_export]
macro_rules! mymac {
    () => {};
}

use myattr::mymac; // error[E0252]: the name `mymac` is defined multiple times.
> ```