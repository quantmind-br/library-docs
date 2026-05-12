---
title: External blocks - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/items/external-blocks.html#abi
source: crawler
fetched_at: 2026-05-06T21:22:01.530122684-03:00
rendered_js: false
word_count: 2409
summary: This document explains the usage of external blocks in Rust, which allow for the declaration of functions and static items defined in foreign languages, including details on ABI specifications and safety requirements.
tags:
    - rust
    - ffi
    - external-blocks
    - abi
    - foreign-function-interface
    - unsafe-rust
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [External blocks](#external-blocks)

External blocks provide *declarations* of items that are not *defined* in the current crate and are the basis of Rust’s foreign function interface. These are akin to unchecked imports.

Two kinds of item *declarations* are allowed in external blocks: [functions](https://doc.rust-lang.org/stable/reference/items/functions.html) and [statics](https://doc.rust-lang.org/stable/reference/items/static-items.html).

Calling unsafe functions or accessing unsafe statics that are declared in external blocks is only allowed in an [`unsafe` context](https://doc.rust-lang.org/stable/reference/unsafe-keyword.html).

The external block defines its functions and statics in the [value namespace](https://doc.rust-lang.org/stable/reference/names/namespaces.html) of the module or block where it is located.

The `unsafe` keyword is semantically required to appear before the `extern` keyword on external blocks.

> 2024 Edition differences
> 
> Prior to the 2024 edition, the `unsafe` keyword is optional. The `safe` and `unsafe` item qualifiers are only allowed if the external block itself is marked as `unsafe`.

## [Functions](#functions)

Functions within external blocks are declared in the same way as other Rust functions, with the exception that they must not have a body and are instead terminated by a semicolon.

Patterns are not allowed in parameters, only [IDENTIFIER](https://doc.rust-lang.org/stable/reference/identifiers.html#grammar-IDENTIFIER) or `_` may be used.

The `safe` and `unsafe` function qualifiers are allowed, but other function qualifiers (e.g. `const`, `async`, `extern`) are not.

Functions within external blocks may be called by Rust code, just like functions defined in Rust. The Rust compiler automatically translates between the Rust ABI and the foreign ABI.

A function declared in an extern block is implicitly `unsafe` unless the `safe` function qualifier is present.

When coerced to a function pointer, a function declared in an extern block has type `extern "abi" for<'l1, ..., 'lm> fn(A1, ..., An) -> R`, where `'l1`, … `'lm` are its lifetime parameters, `A1`, …, `An` are the declared types of its parameters, and `R` is the declared return type.

## [Statics](#statics)

Statics within external blocks are declared in the same way as [statics](https://doc.rust-lang.org/stable/reference/items/static-items.html) outside of external blocks, except that they do not have an expression initializing their value.

Unless a static item declared in an extern block is qualified as `safe`, it is `unsafe` to access that item, whether or not it’s mutable, because there is nothing guaranteeing that the bit pattern at the static’s memory is valid for the type it is declared with, since some arbitrary (e.g. C) code is in charge of initializing the static.

Extern statics can be either immutable or mutable just like [statics](https://doc.rust-lang.org/stable/reference/items/static-items.html) outside of external blocks.

An immutable static *must* be initialized before any Rust code is executed. It is not enough for the static to be initialized before Rust code reads from it. Once Rust code runs, mutating an immutable static (from inside or outside Rust) is UB, except if the mutation happens to bytes inside of an `UnsafeCell`.

## [ABI](#abi)

The `extern` keyword can be followed by an optional [ABI](https://doc.rust-lang.org/stable/reference/glossary.html#r-glossary.abi) string. The ABI specifies the calling convention of the functions in the block. The calling convention defines a low-level interface for functions, such as how arguments are placed in registers or on the stack, how return values are passed, and who is responsible for cleaning up the stack.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
// Interface to the Windows API.
unsafe extern "system" { /* ... */ }
}
> ```

If the ABI string is not specified, it defaults to `"C"`.

> Note
> 
> The `extern` syntax without an explicit ABI is being phased out, so it’s better to always write the ABI explicitly.
> 
> For more details, see [Rust issue #134986](https://github.com/rust-lang/rust/issues/134986).

The following ABI strings are supported on all platforms:

- `unsafe extern "Rust"` — The native calling convention for Rust functions and closures. This is the default when a function is declared without using [`extern fn`](https://doc.rust-lang.org/stable/reference/items/functions.html#r-items.fn.extern). The Rust ABI offers no stability guarantees.

<!--THE END-->

- `unsafe extern "C"` — The “C” ABI matches the default ABI chosen by the dominant C compiler for the target.

<!--THE END-->

- `unsafe extern "system"` — This is equivalent to `extern "C"` except on Windows x86\_32 where it is equivalent to `"stdcall"` for non-variadic functions, and equivalent to `"C"` for variadic functions.
  
  > Note
  > 
  > As the correct underlying ABI on Windows is target-specific, it’s best to use `extern "system"` when attempting to link Windows API functions that don’t use an explicitly defined ABI.

<!--THE END-->

- `extern "C-unwind"` and `extern "system-unwind"` — Identical to `"C"` and `"system"`, respectively, but with [different behavior](https://doc.rust-lang.org/stable/reference/items/functions.html#unwinding) when the callee unwinds (by panicking or throwing a C++ style exception).

There are also some platform-specific ABI strings:

- `unsafe extern "cdecl"` — The calling convention typically used with x86\_32 C code.
  
  - Only available on x86\_32 targets.
  - Corresponds to MSVC’s `__cdecl` and GCC and clang’s `__attribute__((cdecl))`.

<!--THE END-->

- `unsafe extern "stdcall"` — The calling convention typically used by the [Win32 API](https://learn.microsoft.com/en-us/windows/win32/api/) on x86\_32.
  
  - Only available on x86\_32 targets.
  - Corresponds to MSVC’s `__stdcall` and GCC and clang’s `__attribute__((stdcall))`.

<!--THE END-->

- `unsafe extern "win64"` — The Windows x64 ABI.
  
  - Only available on x86\_64 targets.
  - “win64” is the same as the “C” ABI on Windows x86\_64 targets.
  - Corresponds to GCC and clang’s `__attribute__((ms_abi))`.

<!--THE END-->

- `unsafe extern "sysv64"` — The System V ABI.
  
  - Only available on x86\_64 targets.
  - “sysv64” is the same as the “C” ABI on non-Windows x86\_64 targets.
  - Corresponds to GCC and clang’s `__attribute__((sysv_abi))`.

<!--THE END-->

- `unsafe extern "aapcs"` — The soft-float ABI for ARM.
  
  - Only available on ARM32 targets.
  - “aapcs” is the same as the “C” ABI on soft-float ARM32.
  - Corresponds to clang’s `__attribute__((pcs("aapcs")))`.

<!--THE END-->

- `unsafe extern "fastcall"` — A “fast” variant of stdcall that passes some arguments in registers.
  
  - Only available on x86\_32 targets.
  - Corresponds to MSVC’s `__fastcall` and GCC and clang’s `__attribute__((fastcall))`.

<!--THE END-->

- `unsafe extern "thiscall"` — The calling convention typically used on C++ class member functions on x86\_32 MSVC.
  
  - Only available on x86\_32 targets.
  - Corresponds to MSVC’s `__thiscall` and GCC and clang’s `__attribute__((thiscall))`.

<!--THE END-->

- `unsafe extern "efiapi"` — The ABI used for [UEFI](https://uefi.org/specifications) functions.
  
  - Only available on x86 and ARM targets (32bit and 64bit).

Like `"C"` and `"system"`, most platform-specific ABI strings also have a [corresponding `-unwind` variant](https://doc.rust-lang.org/stable/reference/items/functions.html#unwinding); specifically, these are:

- `"aapcs-unwind"`
- `"cdecl-unwind"`
- `"fastcall-unwind"`
- `"stdcall-unwind"`
- `"sysv64-unwind"`
- `"thiscall-unwind"`
- `"win64-unwind"`

## [Variadic functions](#variadic-functions)

Functions within external blocks may be variadic by specifying `...` as the last argument. The variadic parameter may optionally be specified with an identifier.

```rust
#![allow(unused)]
fn main() {
unsafe extern "C" {
    unsafe fn foo(...);
    unsafe fn bar(x: i32, ...);
    unsafe fn with_name(format: *const u8, args: ...);
    // SAFETY: This function guarantees it will not access
    // variadic arguments.
    safe fn ignores_variadic_arguments(x: i32, ...);
}
}
```

> Warning
> 
> The `safe` qualifier should not be used on a function in an `extern` block unless that function guarantees that it will not access the variadic arguments at all. Passing an unexpected number of arguments or arguments of unexpected type to a variadic function may lead to [undefined behavior](https://doc.rust-lang.org/stable/reference/behavior-considered-undefined.html#r-undefined).

Variadic parameters can only be specified within `extern` blocks with the following ABI strings or their corresponding [`-unwind` variants](https://doc.rust-lang.org/stable/reference/items/functions.html#r-items.fn.extern.unwind):

- `"aapcs"`
- `"C"`
- `"cdecl"`
- `"efiapi"`
- `"system"`
- `"sysv64"`
- `"win64"`

## [Attributes on extern blocks](#attributes-on-extern-blocks)

The following [attributes](https://doc.rust-lang.org/stable/reference/attributes.html) control the behavior of external blocks.

### [The `link` attribute](#the-link-attribute)

The *`link` attribute* specifies the name of a native library that the compiler should link with for the items within an `extern` block.

It uses the [MetaListNameValueStr](https://doc.rust-lang.org/stable/reference/attributes.html#grammar-MetaListNameValueStr) syntax to specify its inputs. The `name` key is the name of the native library to link. The `kind` key is an optional value which specifies the kind of library with the following possible values:

- `dylib` — Indicates a dynamic library. This is the default if `kind` is not specified.

<!--THE END-->

- `static` — Indicates a static library.

<!--THE END-->

- `framework` — Indicates a macOS framework. This is only valid for macOS targets.

<!--THE END-->

- `raw-dylib` — Indicates a dynamic library where the compiler will generate an import library to link against (see [`dylib` versus `raw-dylib`](#dylib-versus-raw-dylib) below for details). This is only valid for Windows targets.

The `name` key must be included if `kind` is specified.

The optional `modifiers` argument is a way to specify linking modifiers for the library to link.

Modifiers are specified as a comma-delimited string with each modifier prefixed with either a `+` or `-` to indicate that the modifier is enabled or disabled, respectively.

Specifying multiple `modifiers` arguments in a single `link` attribute, or multiple identical modifiers in the same `modifiers` argument is not currently supported. Example: `#[link(name = "mylib", kind = "static", modifiers = "+whole-archive")]`.

The `wasm_import_module` key may be used to specify the [WebAssembly module](https://webassembly.github.io/spec/core/syntax/modules.html) name for the items within an `extern` block when importing symbols from the host environment. The default module name is `env` if `wasm_import_module` is not specified.

```rust
#[link(name = "crypto")]
unsafe extern {
    // …
}

#[link(name = "CoreFoundation", kind = "framework")]
unsafe extern {
    // …
}

#[link(wasm_import_module = "foo")]
unsafe extern {
    // …
}
```

It is valid to add the `link` attribute on an empty extern block. You can use this to satisfy the linking requirements of extern blocks elsewhere in your code (including upstream crates) instead of adding the attribute to each extern block.

#### [Linking modifiers: `bundle`](#linking-modifiers-bundle)

This modifier is only compatible with the `static` linking kind. Using any other kind will result in a compiler error.

When building a rlib or staticlib `+bundle` means that the native static library will be packed into the rlib or staticlib archive, and then retrieved from there during linking of the final binary.

When building a rlib `-bundle` means that the native static library is registered as a dependency of that rlib “by name”, and object files from it are included only during linking of the final binary, the file search by that name is also performed during final linking. When building a staticlib `-bundle` means that the native static library is simply not included into the archive and some higher level build system will need to add it later during linking of the final binary.

This modifier has no effect when building other targets like executables or dynamic libraries.

The default for this modifier is `+bundle`.

More implementation details about this modifier can be found in [`bundle` documentation for rustc](https://doc.rust-lang.org/stable/rustc/command-line-arguments.html#linking-modifiers-bundle).

#### [Linking modifiers: `whole-archive`](#linking-modifiers-whole-archive)

This modifier is only compatible with the `static` linking kind. Using any other kind will result in a compiler error.

`+whole-archive` means that the static library is linked as a whole archive without throwing any object files away.

The default for this modifier is `-whole-archive`.

More implementation details about this modifier can be found in [`whole-archive` documentation for rustc](https://doc.rust-lang.org/stable/rustc/command-line-arguments.html#linking-modifiers-whole-archive).

### [Linking modifiers: `verbatim`](#linking-modifiers-verbatim)

This modifier is compatible with all linking kinds.

`+verbatim` means that rustc itself won’t add any target-specified library prefixes or suffixes (like `lib` or `.a`) to the library name, and will try its best to ask for the same thing from the linker.

`-verbatim` means that rustc will either add a target-specific prefix and suffix to the library name before passing it to linker, or won’t prevent linker from implicitly adding it.

The default for this modifier is `-verbatim`.

More implementation details about this modifier can be found in [`verbatim` documentation for rustc](https://doc.rust-lang.org/stable/rustc/command-line-arguments.html#linking-modifiers-verbatim).

#### [`dylib` versus `raw-dylib`](#dylib-versus-raw-dylib)

On Windows, linking against a dynamic library requires that an import library is provided to the linker: this is a special static library that declares all of the symbols exported by the dynamic library in such a way that the linker knows that they have to be dynamically loaded at runtime.

Specifying `kind = "dylib"` instructs the Rust compiler to link an import library based on the `name` key. The linker will then use its normal library resolution logic to find that import library. Alternatively, specifying `kind = "raw-dylib"` instructs the compiler to generate an import library during compilation and provide that to the linker instead.

`raw-dylib` is only supported on Windows. Using it when targeting other platforms will result in a compiler error.

#### [The `import_name_type` key](#the-import_name_type-key)

On x86 Windows, names of functions are “decorated” (i.e., have a specific prefix and/or suffix added) to indicate their calling convention. For example, a `stdcall` calling convention function with the name `fn1` that has no arguments would be decorated as `_fn1@0`. However, the [PE Format](https://learn.microsoft.com/windows/win32/debug/pe-format#import-name-type) does also permit names to have no prefix or be undecorated. Additionally, the MSVC and GNU toolchains use different decorations for the same calling conventions which means, by default, some Win32 functions cannot be called using the `raw-dylib` link kind via the GNU toolchain.

To allow for these differences, when using the `raw-dylib` link kind you may also specify the `import_name_type` key with one of the following values to change how functions are named in the generated import library:

- `decorated`: The function name will be fully-decorated using the MSVC toolchain format.
- `noprefix`: The function name will be decorated using the MSVC toolchain format, but skipping the leading `?`, `@`, or optionally `_`.
- `undecorated`: The function name will not be decorated.

If the `import_name_type` key is not specified, then the function name will be fully-decorated using the target toolchain’s format.

Variables are never decorated and so the `import_name_type` key has no effect on how they are named in the generated import library.

The `import_name_type` key is only supported on x86 Windows. Using it when targeting other platforms will result in a compiler error.

### [The `link_name` attribute](#the-link_name-attribute)

The *`link_name` [attribute](https://doc.rust-lang.org/stable/reference/attributes.html)* may be applied to declarations inside an `extern` block to specify the symbol to import for the given function or static.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
unsafe extern "C" {
    #[link_name = "actual_symbol_name"]
    safe fn name_in_rust();
}
}
> ```

The `link_name` attribute uses the [MetaNameValueStr](https://doc.rust-lang.org/stable/reference/attributes.html#grammar-MetaNameValueStr) syntax.

The `link_name` attribute may only be applied to a function or static item in an `extern` block.

> Note
> 
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

Only the last use of `link_name` on an item has effect.

> Note
> 
> `rustc` lints against any use preceding the last. This may become an error in the future.

The `link_name` attribute may not be used with the [`link_ordinal`](https://doc.rust-lang.org/stable/reference/items/external-blocks.html#r-items.extern.attributes.link_ordinal) attribute.

### [The `link_ordinal` attribute](#the-link_ordinal-attribute)

The *`link_ordinal` attribute* can be applied on declarations inside an `extern` block to indicate the numeric ordinal to use when generating the import library to link against. An ordinal is a unique number per symbol exported by a dynamic library on Windows and can be used when the library is being loaded to find that symbol rather than having to look it up by name.

> Warning
> 
> `link_ordinal` should only be used in cases where the ordinal of the symbol is known to be stable: if the ordinal of a symbol is not explicitly set when its containing binary is built then one will be automatically assigned to it, and that assigned ordinal may change between builds of the binary.

```rust
#![allow(unused)]
fn main() {
#[cfg(all(windows, target_arch = "x86"))]
#[link(name = "exporter", kind = "raw-dylib")]
unsafe extern "stdcall" {
    #[link_ordinal(15)]
    safe fn imported_function_stdcall(i: i32);
}
}
```

This attribute is only used with the `raw-dylib` linking kind. Using any other kind will result in a compiler error.

Using this attribute with the `link_name` attribute will result in a compiler error.

### [Attributes on function parameters](#attributes-on-function-parameters)

Attributes on extern function parameters follow the same rules and restrictions as [regular function parameters](https://doc.rust-lang.org/stable/reference/items/functions.html#attributes-on-function-parameters).

* * *

1. Starting with the 2024 Edition, the `unsafe` keyword is required semantically. [↩](#fr-unsafe-2024-1)