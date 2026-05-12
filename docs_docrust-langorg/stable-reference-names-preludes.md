---
title: Preludes - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/names/preludes.html#macro_use-prelude
source: crawler
fetched_at: 2026-05-06T21:32:08.416414305-03:00
rendered_js: false
word_count: 836
summary: This document explains the concept of preludes in the Rust programming language, describing the various collections of names automatically brought into scope and how attributes like no_std and no_implicit_prelude control these behaviors.
tags:
    - rust
    - prelude
    - scope
    - no-std
    - name-resolution
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Preludes](#preludes)

A *prelude* is a collection of names that are automatically brought into scope of every module in a crate.

These prelude names are not part of the module itself: they are implicitly queried during [name resolution](https://doc.rust-lang.org/stable/reference/names/name-resolution.html). For example, even though something like [`Box`](https://doc.rust-lang.org/stable/alloc/boxed/struct.Box.html) is in scope in every module, you cannot refer to it as `self::Box` because it is not a member of the current module.

There are several different preludes:

- [Standard library prelude](https://doc.rust-lang.org/stable/reference/names/preludes.html#r-names.preludes.std)
- [Extern prelude](#extern-prelude)
- [Language prelude](#language-prelude)
- [`macro_use` prelude](#macro_use-prelude)
- [Tool prelude](#tool-prelude)

## [Standard library prelude](#standard-library-prelude)

Each crate has a standard library prelude, which consists of the names from a single standard library module.

The module used depends on the crate’s edition, and on whether the [`no_std` attribute](#the-no_std-attribute) is applied to the crate:

## [Extern prelude](#extern-prelude)

External crates imported with [`extern crate`](https://doc.rust-lang.org/stable/reference/items/extern-crates.html) in the root module or provided to the compiler (as with the `--extern` flag with `rustc`) are added to the *extern prelude*. If imported with an alias such as `extern crate orig_name as new_name`, then the symbol `new_name` is instead added to the prelude.

The [`core`](https://doc.rust-lang.org/stable/core/index.html) crate is always added to the extern prelude.

The [`std`](https://doc.rust-lang.org/stable/std/index.html) crate is added as long as the [`no_std` attribute](#the-no_std-attribute) is not specified in the crate root.

> 2018 Edition differences
> 
> In the 2015 edition, crates in the extern prelude cannot be referenced via [use declarations](https://doc.rust-lang.org/stable/reference/items/use-declarations.html), so it is generally standard practice to include `extern crate` declarations to bring them into scope.
> 
> Beginning in the 2018 edition, [use declarations](https://doc.rust-lang.org/stable/reference/items/use-declarations.html) can reference crates in the extern prelude, so it is considered unidiomatic to use `extern crate`.

> Note
> 
> Additional crates that ship with `rustc`, such as [`alloc`](https://doc.rust-lang.org/stable/alloc/index.html), and [`test`](https://doc.rust-lang.org/stable/test/index.html), are not automatically included with the `--extern` flag when using Cargo. They must be brought into scope with an `extern crate` declaration, even in the 2018 edition.
> 
> ```rust
> #![allow(unused)]
fn main() {
extern crate alloc;
use alloc::rc::Rc;
}
> ```
> 
> Cargo does bring in `proc_macro` to the extern prelude for proc-macro crates only.

### [The `no_std` attribute](#the-no_std-attribute)

The *`no_std` [attribute](https://doc.rust-lang.org/stable/reference/attributes.html#r-attributes)* causes the [`std`](https://doc.rust-lang.org/stable/std/index.html) crate to not be linked automatically and the [standard library prelude](https://doc.rust-lang.org/stable/reference/names/preludes.html#r-names.preludes.std) to instead use the `core` prelude.

> Note
> 
> Using `no_std` is useful when either the crate is targeting a platform that does not support the standard library or is purposefully not using the capabilities of the standard library. Those capabilities are mainly dynamic memory allocation (e.g. `Box` and `Vec`) and file and network capabilities (e.g. `std::fs` and `std::io`).

> Warning
> 
> Using `no_std` does not prevent the standard library from being linked. It is still valid to write `extern crate std` in the crate or in one of its dependencies; this will cause the compiler to link the `std` crate into the program.

The `no_std` attribute uses the [MetaWord](https://doc.rust-lang.org/stable/reference/attributes.html#grammar-MetaWord) syntax.

The `no_std` attribute may only be applied to the crate root.

The `no_std` attribute may be used any number of times on a form.

> Note
> 
> `rustc` lints against any use following the first.

The `no_std` attribute changes the [standard library prelude](https://doc.rust-lang.org/stable/reference/names/preludes.html#r-names.preludes.std) to use the `core` prelude instead of the `std` prelude.

> 2018 Edition differences
> 
> Before the 2018 edition, `std` is injected into the crate root by default. If `no_std` is specified, `core` is injected instead. Starting with the 2018 edition, regardless of `no_std` being specified, neither is injected into the crate root.

## [Language prelude](#language-prelude)

The language prelude includes names of types and attributes that are built-in to the language. The language prelude is always in scope.

It includes the following:

- [Type namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html)
  
  - [Boolean type](https://doc.rust-lang.org/stable/reference/types/boolean.html) — `bool`
  - [`char`](https://doc.rust-lang.org/stable/reference/types/char.html)
  - [`str`](https://doc.rust-lang.org/stable/reference/types/str.html)
  - [Integer types](https://doc.rust-lang.org/stable/reference/types/numeric.html#integer-types) — `i8`, `i16`, `i32`, `i64`, `i128`, `u8`, `u16`, `u32`, `u64`, `u128`
  - [Machine-dependent integer types](https://doc.rust-lang.org/stable/reference/types/numeric.html#machine-dependent-integer-types) — `usize` and `isize`
  - [floating-point types](https://doc.rust-lang.org/stable/reference/types/numeric.html#floating-point-types) — `f32` and `f64`
- [Macro namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html)
  
  - [Built-in attributes](https://doc.rust-lang.org/stable/reference/attributes.html#built-in-attributes-index)
  - [Built-in derive macros](https://doc.rust-lang.org/stable/reference/attributes/derive.html#r-attributes.derive.built-in)

## [`macro_use` prelude](#macro_use-prelude)

The `macro_use` prelude includes macros from external crates that were imported by the [`macro_use` attribute](https://doc.rust-lang.org/stable/reference/macros-by-example.html#the-macro_use-attribute) applied to an [`extern crate`](https://doc.rust-lang.org/stable/reference/items/extern-crates.html).

The tool prelude includes tool names for external tools in the [type namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html). See the [tool attributes](https://doc.rust-lang.org/stable/reference/attributes.html#tool-attributes) section for more details.

## [The `no_implicit_prelude` attribute](#the-no_implicit_prelude-attribute)

The *`no_implicit_prelude` [attribute](https://doc.rust-lang.org/stable/reference/attributes.html)* is used to prevent implicit preludes from being brought into scope.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
// The attribute can be applied to the crate root to affect
// all modules.
#![no_implicit_prelude]

// Or it can be applied to a module to only affect that module
// and its descendants.
#[no_implicit_prelude]
mod example {
    // ...
}
}
> ```

The `no_implicit_prelude` attribute uses the [MetaWord](https://doc.rust-lang.org/stable/reference/attributes.html#grammar-MetaWord) syntax.

The `no_implicit_prelude` attribute may only be applied to the crate or to a module.

> Note
> 
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

The `no_implicit_prelude` attribute may be used any number of times on a form.

> Note
> 
> `rustc` lints against any use following the first.

The `no_implicit_prelude` attribute prevents the [standard library prelude](https://doc.rust-lang.org/stable/reference/names/preludes.html#r-names.preludes.std), [extern prelude](#extern-prelude), [`macro_use` prelude](#macro_use-prelude), and the [tool prelude](#tool-prelude) from being brought into scope for the module and its descendants.

The `no_implicit_prelude` attribute does not affect the [language prelude](#language-prelude).

> 2018 Edition differences
> 
> In the 2015 edition, the `no_implicit_prelude` attribute does not affect the [`macro_use` prelude](#macro_use-prelude), and all macros exported from the standard library are still included in the `macro_use` prelude. Starting in the 2018 edition, the attribute does remove the `macro_use` prelude.