---
title: Items - The Rust Reference
url: https://doc.rust-lang.org/reference/items.html
source: crawler
fetched_at: 2026-05-06T21:38:46.40764242-03:00
rendered_js: false
word_count: 189
summary: This document defines the concept of items in the Rust programming language, explaining how they are organized within crates, modules, and their behavior at compile-time.
tags:
    - rust-language
    - items
    - crate-structure
    - modules
    - programming-concepts
    - language-reference
category: concept
---

## [Items](#items)

An *item* is a component of a crate. Items are organized within a crate by a nested set of [modules](https://doc.rust-lang.org/reference/items/modules.html). Every crate has a single “outermost” anonymous module; all further items within the crate have [paths](https://doc.rust-lang.org/reference/paths.html) within the module tree of the crate.

Items are entirely determined at compile-time, generally remain fixed during execution, and may reside in read-only memory.

There are several kinds of items:

- [modules](https://doc.rust-lang.org/reference/items/modules.html)
- [`extern crate` declarations](https://doc.rust-lang.org/reference/items/extern-crates.html)
- [`use` declarations](https://doc.rust-lang.org/reference/items/use-declarations.html)
- [function definitions](https://doc.rust-lang.org/reference/items/functions.html)
- [type alias definitions](https://doc.rust-lang.org/reference/items/type-aliases.html)
- [struct definitions](https://doc.rust-lang.org/reference/items/structs.html)
- [enumeration definitions](https://doc.rust-lang.org/reference/items/enumerations.html)
- [union definitions](https://doc.rust-lang.org/reference/items/unions.html)
- [constant items](https://doc.rust-lang.org/reference/items/constant-items.html)
- [static items](https://doc.rust-lang.org/reference/items/static-items.html)
- [trait definitions](https://doc.rust-lang.org/reference/items/traits.html)
- [implementations](https://doc.rust-lang.org/reference/items/implementations.html)
- [`extern` blocks](https://doc.rust-lang.org/reference/items/external-blocks.html)

Items may be declared in the [root of the crate](https://doc.rust-lang.org/reference/crates-and-source-files.html), a [module](https://doc.rust-lang.org/reference/items/modules.html), or a [block expression](https://doc.rust-lang.org/reference/expressions/block-expr.html).

A subset of items, called [associated items](https://doc.rust-lang.org/reference/items/associated-items.html), may be declared in [traits](https://doc.rust-lang.org/reference/items/traits.html) and [implementations](https://doc.rust-lang.org/reference/items/implementations.html).

A subset of items, called external items, may be declared in [`extern` blocks](https://doc.rust-lang.org/reference/items/external-blocks.html).

Items may be defined in any order, with the exception of [`macro_rules`](https://doc.rust-lang.org/reference/macros-by-example.html) which has its own scoping behavior.

[Name resolution](https://doc.rust-lang.org/reference/names/name-resolution.html) of item names allows items to be defined before or after where the item is referred to in the module or block.

See [item scopes](https://doc.rust-lang.org/reference/names/scopes.html#item-scopes) for information on the scoping rules of items.