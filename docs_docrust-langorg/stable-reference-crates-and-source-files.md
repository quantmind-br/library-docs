---
title: Crates and source files - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/crates-and-source-files.html#the-no_main-attribute
source: crawler
fetched_at: 2026-05-06T21:37:50.392750062-03:00
rendered_js: false
word_count: 692
summary: This document outlines the fundamental structure of Rust programs, explaining how crates function as units of compilation and describing the requirements for main functions and crate-level attributes.
tags:
    - rust
    - compilation-model
    - crates
    - main-function
    - modules
    - attributes
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Crates and source files](#crates-and-source-files)

> Note
> 
> Although Rust, like any other language, can be implemented by an interpreter as well as a compiler, the only existing implementation is a compiler, and the language has always been designed to be compiled. For these reasons, this section assumes a compiler.

Rust’s semantics obey a *phase distinction* between compile-time and run-time.[1](#footnote-phase-distinction) Semantic rules that have a *static interpretation* govern the success or failure of compilation, while semantic rules that have a *dynamic interpretation* govern the behavior of the program at run-time.

The compilation model centers on artifacts called *crates*. Each compilation processes a single crate in source form, and if successful, produces a single crate in binary form: either an executable or some sort of library.[2](#footnote-cratesourcefile)

A *crate* is a unit of compilation and linking, as well as versioning, distribution, and runtime loading. A crate contains a *tree* of nested [module](https://doc.rust-lang.org/stable/reference/items/modules.html) scopes. The top level of this tree is a module that is anonymous (from the point of view of paths within the module) and any item within a crate has a canonical [module path](https://doc.rust-lang.org/stable/reference/paths.html) denoting its location within the crate’s module tree.

The Rust compiler is always invoked with a single source file as input, and always produces a single output crate. The processing of that source file may result in other source files being loaded as modules. Source files have the extension `.rs`.

A Rust source file describes a module, the name and location of which — in the module tree of the current crate — are defined from outside the source file: either by an explicit [Module](https://doc.rust-lang.org/stable/reference/items/modules.html#grammar-Module) item in a referencing source file, or by the name of the crate itself.

Every source file is a module, but not every module needs its own source file: [module definitions](https://doc.rust-lang.org/stable/reference/items/modules.html) can be nested within one file.

Each source file contains a sequence of zero or more [Item](https://doc.rust-lang.org/stable/reference/items.html#grammar-Item) definitions, and may optionally begin with any number of [attributes](https://doc.rust-lang.org/stable/reference/attributes.html) that apply to the containing module, most of which influence the behavior of the compiler.

The anonymous crate module can have additional attributes that apply to the crate as a whole.

> Note
> 
> The file’s contents may be preceded by a [shebang](https://doc.rust-lang.org/stable/reference/input-format.html#shebang-removal).

```rust
#![allow(unused)]
fn main() {
// Specify the crate name.
#![crate_name = "projx"]

// Specify the type of output artifact.
#![crate_type = "lib"]

// Turn on a warning.
// This can be done in any module, not just the anonymous crate module.
#![warn(non_camel_case_types)]
}
```

## [Main functions](#main-functions)

A crate that contains a `main` [function](https://doc.rust-lang.org/stable/reference/items/functions.html) can be compiled to an executable.

If a `main` function is present, it must take no arguments, must not declare any [trait or lifetime bounds](https://doc.rust-lang.org/stable/reference/trait-bounds.html), must not have any [where clauses](https://doc.rust-lang.org/stable/reference/items/generics.html#where-clauses), and its return type must implement the [`Termination`](https://doc.rust-lang.org/stable/std/process/trait.Termination.html) trait.

```rust
fn main() {}
```

```rust
fn main() -> ! {
    std::process::exit(0);
}
```

```rust
fn main() -> impl std::process::Termination {
    std::process::ExitCode::SUCCESS
}
```

The `main` function may be an import, e.g. from an external crate or from the current one.

```rust
#![allow(unused)]
fn main() {
mod foo {
    pub fn bar() {
        println!("Hello, world!");
    }
}
use foo::bar as main;
}
```

### [Uncaught foreign unwinding](#uncaught-foreign-unwinding)

When a “foreign” unwind (e.g. an exception thrown from C++ code, or a `panic!` in Rust code using a different panic handler) propagates beyond the `main` function, the process will be safely terminated. This may take the form of an abort, in which case it is not guaranteed that any `Drop` calls will be executed, and the error output may be less informative than if the runtime had been terminated by a “native” Rust `panic`.

For more information, see the [panic documentation](https://doc.rust-lang.org/stable/reference/panic.html#unwinding-across-ffi-boundaries).

### [The `no_main` attribute](#the-no_main-attribute)

The *`no_main` [attribute](https://doc.rust-lang.org/stable/reference/attributes.html)* may be applied at the crate level to disable emitting the `main` symbol for an executable binary. This is useful when some other object being linked to defines `main`.

## [The `crate_name` attribute](#the-crate_name-attribute)

The *`crate_name` [attribute](https://doc.rust-lang.org/stable/reference/attributes.html)* may be applied at the crate level to specify the name of the crate with the [MetaNameValueStr](https://doc.rust-lang.org/stable/reference/attributes.html#grammar-MetaNameValueStr) syntax.

```rust
#![allow(unused)]
#![crate_name = "mycrate"]
fn main() {
}
```

The crate name must not be empty, and must only contain [Unicode alphanumeric](https://doc.rust-lang.org/stable/std/primitive.char.html#method.is_alphanumeric) or `_` (U+005F) characters.

* * *

1. This distinction would also exist in an interpreter. Static checks like syntactic analysis, type checking, and lints should happen before the program is executed regardless of when it is executed. [↩](#fr-phase-distinction-1)
2. A crate is somewhat analogous to an *assembly* in the ECMA-335 CLI model, a *library* in the SML/NJ Compilation Manager, a *unit* in the Owens and Flatt module system, or a *configuration* in Mesa. [↩](#fr-cratesourcefile-1)