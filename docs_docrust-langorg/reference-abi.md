---
title: Application binary interface - The Rust Reference
url: https://doc.rust-lang.org/reference/abi.html
source: crawler
fetched_at: 2026-05-06T21:27:01.77470659-03:00
rendered_js: false
word_count: 541
summary: This document describes Rust language attributes that influence the Application Binary Interface (ABI) and symbol handling during compilation, such as control over name mangling, memory sections, and symbol exportation.
tags:
    - rust
    - abi
    - attributes
    - compiler-directives
    - symbol-mangling
    - memory-layout
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Application binary interface (ABI)](#application-binary-interface-abi)

This section documents features that affect the ABI of the compiled output of a crate.

See [*extern functions*](https://doc.rust-lang.org/reference/items/functions.html#extern-function-qualifier) for information on specifying the ABI for exporting functions. See [*external blocks*](https://doc.rust-lang.org/reference/items/external-blocks.html) for information on specifying the ABI for linking external libraries.

## [The `used` attribute](#the-used-attribute)

The *`used` attribute* can only be applied to [`static` items](https://doc.rust-lang.org/reference/items/static-items.html). This [attribute](https://doc.rust-lang.org/reference/attributes.html) forces the compiler to keep the variable in the output object file (.o, .rlib, etc. excluding final binaries) even if the variable is not used, or referenced, by any other item in the crate. However, the linker is still free to remove such an item.

Below is an example that shows under what conditions the compiler keeps a `static` item in the output object file.

```rust
#![allow(unused)]
fn main() {
// foo.rs

// This is kept because of `#[used]`:
#[used]
static FOO: u32 = 0;

// This is removable because it is unused:
#[allow(dead_code)]
static BAR: u32 = 0;

// This is kept because it is publicly reachable:
pub static BAZ: u32 = 0;

// This is kept because it is referenced by a public, reachable function:
static QUUX: u32 = 0;

pub fn quux() -> &'static u32 {
    &QUUX
}

// This is removable because it is referenced by a private, unused (dead) function:
static CORGE: u32 = 0;

#[allow(dead_code)]
fn corge() -> &'static u32 {
    &CORGE
}
}
```

```console
$ rustc -O --emit=obj --crate-type=rlib foo.rs

$ nm -C foo.o
0000000000000000 R foo::BAZ
0000000000000000 r foo::FOO
0000000000000000 R foo::QUUX
0000000000000000 T foo::quux
```

## [The `no_mangle` attribute](#the-no_mangle-attribute)

The *`no_mangle` attribute* may be used on any [item](https://doc.rust-lang.org/reference/items.html) to disable standard symbol name mangling. The symbol for the item will be the identifier of the item’s name.

Additionally, the item will be publicly exported from the produced library or object file, similar to the [`used` attribute](#the-used-attribute).

This attribute is unsafe as an unmangled symbol may collide with another symbol with the same name (or with a well-known symbol), leading to undefined behavior.

```rust
#![allow(unused)]
fn main() {
#[unsafe(no_mangle)]
extern "C" fn foo() {}
}
```

> 2024 Edition differences
> 
> Before the 2024 edition it is allowed to use the `no_mangle` attribute without the `unsafe` qualification.

## [The `link_section` attribute](#the-link_section-attribute)

The *`link_section` attribute* specifies the section of the object file that a [function](https://doc.rust-lang.org/reference/items/functions.html) or [static](https://doc.rust-lang.org/reference/items/static-items.html)’s content will be placed into.

The `link_section` attribute uses the [MetaNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaNameValueStr) syntax to specify the section name.

```rust
#![allow(unused)]
fn main() {
#[unsafe(no_mangle)]
#[unsafe(link_section = ".example_section")]
pub static VAR1: u32 = 1;
}
```

This attribute is unsafe as it allows users to place data and code into sections of memory not expecting them, such as mutable data into read-only areas.

> 2024 Edition differences
> 
> Before the 2024 edition it is allowed to use the `link_section` attribute without the `unsafe` qualification.

## [The `export_name` attribute](#the-export_name-attribute)

The *`export_name` attribute* specifies the name of the symbol that will be exported on a [function](https://doc.rust-lang.org/reference/items/functions.html) or [static](https://doc.rust-lang.org/reference/items/static-items.html).

The `export_name`attribute uses the [MetaNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaNameValueStr) syntax to specify the symbol name.

```rust
#![allow(unused)]
fn main() {
#[unsafe(export_name = "exported_symbol_name")]
pub fn name_in_rust() { }
}
```

This attribute is unsafe as a symbol with a custom name may collide with another symbol with the same name (or with a well-known symbol), leading to undefined behavior.

> 2024 Edition differences
> 
> Before the 2024 edition it is allowed to use the `export_name` attribute without the `unsafe` qualification.