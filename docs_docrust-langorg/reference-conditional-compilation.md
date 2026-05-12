---
title: Conditional compilation - The Rust Reference
url: https://doc.rust-lang.org/reference/conditional-compilation.html#debug_assertions
source: crawler
fetched_at: 2026-05-06T21:25:00.387534351-03:00
rendered_js: false
word_count: 1445
summary: This document explains the mechanics of conditional compilation in Rust, detailing how source code can be selectively compiled based on configuration predicates and system-defined options.
tags:
    - rust
    - conditional-compilation
    - cfg
    - compiler-flags
    - compilation-targets
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Conditional compilation](#conditional-compilation)

*Conditionally compiled source code* is source code that is compiled only under certain conditions.

Source code can be made conditionally compiled using the [`cfg`](#the-cfg-attribute) and [`cfg_attr`](#the-cfg_attr-attribute) [attributes](https://doc.rust-lang.org/reference/attributes.html) and the built-in [`cfg!`](#the-cfg-macro) and [`cfg_select!`](#the-cfg_select-macro) [macros](https://doc.rust-lang.org/reference/macros.html).

Whether to compile can depend on the target architecture of the compiled crate, arbitrary values passed to the compiler, and other things further described below.

Each form of conditional compilation takes a *configuration predicate* that evaluates to true or false. The predicate is one of the following:

- A configuration option. The predicate is true if the option is set, and false if it is unset.

<!--THE END-->

- `all()` with a comma-separated list of configuration predicates. It is true if all of the given predicates are true, or if the list is empty.

<!--THE END-->

- `any()` with a comma-separated list of configuration predicates. It is true if at least one of the given predicates is true. If there are no predicates, it is false.

<!--THE END-->

- `not()` with a configuration predicate. It is true if its predicate is false and false if its predicate is true.

<!--THE END-->

- `true` or `false` literals, which are always true or false respectively.

*Configuration options* are either names or key-value pairs, and are either set or unset.

Names are written as a single identifier, such as `unix`.

Key-value pairs are written as an identifier, `=`, and then a string, such as `target_arch = "x86_64"`.

> Note
> 
> Whitespace around the `=` is ignored, so `foo="bar"` and `foo = "bar"` are equivalent.

Keys do not need to be unique. For example, both `feature = "std"` and `feature = "serde"` can be set at the same time.

## [Set configuration options](#set-configuration-options)

Which configuration options are set is determined statically during the compilation of the crate.

Some options are *compiler-set* based on data about the compilation.

Other options are *arbitrarily-set* based on input passed to the compiler outside of the code.

It is not possible to set a configuration option from within the source code of the crate being compiled.

> Note
> 
> For `rustc`, arbitrary-set configuration options are set using the [`--cfg`](https://doc.rust-lang.org/rustc/command-line-arguments.html#--cfg-configure-the-compilation-environment) flag. Configuration values for a specified target can be displayed with `rustc --print cfg --target $TARGET`.

> Note
> 
> Configuration options with the key `feature` are a convention used by [Cargo](https://doc.rust-lang.org/cargo/reference/features.html) for specifying compile-time options and optional dependencies.

### [`target_arch`](#target_arch)

Key-value option set once with the target’s CPU architecture. The value is similar to the first element of the platform’s target triple, but not identical.

Example values:

- `"x86"`
- `"x86_64"`
- `"mips"`
- `"powerpc"`
- `"powerpc64"`
- `"arm"`
- `"aarch64"`

### [`target_feature`](#target_feature)

Key-value option set for each platform feature available for the current compilation target.

Example values:

- `"avx"`
- `"avx2"`
- `"crt-static"`
- `"rdrand"`
- `"sse"`
- `"sse2"`
- `"sse4.1"`

See the [`target_feature` attribute](https://doc.rust-lang.org/reference/attributes/codegen.html#the-target_feature-attribute) for more details on the available features.

An additional feature of `crt-static` is available to the `target_feature` option to indicate that a [static C runtime](https://doc.rust-lang.org/reference/linkage.html#static-and-dynamic-c-runtimes) is available.

### [`target_os`](#target_os)

Key-value option set once with the target’s operating system. This value is similar to the second and third element of the platform’s target triple.

Example values:

- `"windows"`
- `"macos"`
- `"ios"`
- `"linux"`
- `"android"`
- `"freebsd"`
- `"dragonfly"`
- `"openbsd"`
- `"netbsd"`
- `"none"` (typical for embedded targets)

### [`target_family`](#target_family)

Key-value option providing a more generic description of a target, such as the family of the operating systems or architectures that the target generally falls into. Any number of `target_family` key-value pairs can be set.

Example values:

- `"unix"`
- `"windows"`
- `"wasm"`
- Both `"unix"` and `"wasm"`

### [`unix` and `windows`](#unix-and-windows)

`unix` is set if `target_family = "unix"` is set.

`windows` is set if `target_family = "windows"` is set.

### [`target_env`](#target_env)

Key-value option set with further disambiguating information about the target platform with information about the ABI or `libc` used. For historical reasons, this value is only defined as not the empty-string when actually needed for disambiguation. Thus, for example, on many GNU platforms, this value will be empty. This value is similar to the fourth element of the platform’s target triple. One difference is that embedded ABIs such as `gnueabihf` will simply define `target_env` as `"gnu"`.

Example values:

- `""`
- `"gnu"`
- `"msvc"`
- `"musl"`
- `"sgx"`
- `"sim"`
- `"macabi"`

### [`target_abi`](#target_abi)

Key-value option set to further disambiguate the target with information about the target ABI.

For historical reasons, this value is only defined as not the empty-string when actually needed for disambiguation. Thus, for example, on many GNU platforms, this value will be empty.

Example values:

- `""`
- `"llvm"`
- `"eabihf"`
- `"abi64"`

### [`target_endian`](#target_endian)

Key-value option set once with either a value of “little” or “big” depending on the endianness of the target’s CPU.

### [`target_pointer_width`](#target_pointer_width)

Key-value option set once with the target’s pointer width in bits.

Example values:

- `"16"`
- `"32"`
- `"64"`

### [`target_vendor`](#target_vendor)

Key-value option set once with the vendor of the target.

Example values:

- `"apple"`
- `"fortanix"`
- `"pc"`
- `"unknown"`

### [`target_has_atomic`](#target_has_atomic)

Key-value option set for each bit width that the target supports atomic loads, stores, and compare-and-swap operations.

When this cfg is present, all of the stable [`core::sync::atomic`](https://doc.rust-lang.org/core/sync/atomic/index.html) APIs are available for the relevant atomic width.

Possible values:

- `"8"`
- `"16"`
- `"32"`
- `"64"`
- `"128"`
- `"ptr"`

### [`test`](#test)

Enabled when compiling the test harness. Done with `rustc` by using the [`--test`](https://doc.rust-lang.org/rustc/command-line-arguments.html#--test-build-a-test-harness) flag. See [Testing](https://doc.rust-lang.org/reference/attributes/testing.html) for more on testing support.

### [`debug_assertions`](#debug_assertions)

Enabled by default when compiling without optimizations. This can be used to enable extra debugging code in development but not in production. For example, it controls the behavior of the standard library’s [`debug_assert!`](https://doc.rust-lang.org/core/macro.debug_assert.html) macro.

### [`proc_macro`](#proc_macro)

Set when the crate being compiled is being compiled with the `proc_macro` [crate type](https://doc.rust-lang.org/reference/linkage.html).

### [`panic`](#panic)

Key-value option set depending on the [panic strategy](https://doc.rust-lang.org/reference/panic.html#panic-strategy). Note that more values may be added in the future.

Example values:

- `"abort"`
- `"unwind"`

## [Forms of conditional compilation](#forms-of-conditional-compilation)

### [The `cfg` attribute](#the-cfg-attribute)

The *`cfg` [attribute](https://doc.rust-lang.org/reference/attributes.html)* conditionally includes the form to which it is attached based on a configuration predicate.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
// The function is only included in the build when compiling for macOS
#[cfg(target_os = "macos")]
fn macos_only() {
  // ...
}

// This function is only included when either foo or bar is defined
#[cfg(any(foo, bar))]
fn needs_foo_or_bar() {
  // ...
}

// This function is only included when compiling for a unixish OS with a 32-bit
// architecture
#[cfg(all(unix, target_pointer_width = "32"))]
fn on_32bit_unix() {
  // ...
}

// This function is only included when foo is not defined
#[cfg(not(foo))]
fn needs_not_foo() {
  // ...
}

// This function is only included when the panic strategy is set to unwind
#[cfg(panic = "unwind")]
fn when_unwinding() {
  // ...
}
}
> ```

The syntax for the `cfg` attribute is:

The `cfg` attribute may be used anywhere attributes are allowed.

The `cfg` attribute may be used any number of times on a form. The form to which the attributes are attached will not be included if any of the `cfg` predicates are false except as described in [cfg.attr.crate-level-attrs](https://doc.rust-lang.org/reference/conditional-compilation.html#r-cfg.attr.crate-level-attrs).

If the predicates are true, the form is rewritten to not have the `cfg` attributes on it. If any predicate is false, the form is removed from the source code.

When a crate-level `cfg` has a false predicate, the crate itself still exists. Any crate attributes preceding the `cfg` are kept, and any crate attributes following the `cfg` are removed as well as removing all of the following crate contents.

> Example
> 
> The behavior of not removing the preceding attributes allows you to do things such as include `#![no_std]` to avoid linking `std` even if a `#![cfg(...)]` has otherwise removed the contents of the crate. For example:
> 
> ```rust
> // This `no_std` attribute is kept even though the crate-level `cfg`
// attribute is false.
#![no_std]
#![cfg(false)]

// This function is not included.
pub fn example() {}
> ```

### [The `cfg_attr` attribute](#the-cfg_attr-attribute)

The *`cfg_attr` [attribute](https://doc.rust-lang.org/reference/attributes.html)* conditionally includes attributes based on a configuration predicate.

> Example
> 
> The following module will either be found at `linux.rs` or `windows.rs` based on the target.
> 
> ```rust
> #[cfg_attr(target_os = "linux", path = "linux.rs")]
#[cfg_attr(windows, path = "windows.rs")]
mod os;
> ```

The syntax for the `cfg_attr` attribute is:

The `cfg_attr` attribute may be used anywhere attributes are allowed.

The `cfg_attr` attribute may be used any number of times on a form.

The [`crate_type`](https://doc.rust-lang.org/reference/linkage.html) and [`crate_name`](https://doc.rust-lang.org/reference/crates-and-source-files.html#the-crate_name-attribute) attributes cannot be used with `cfg_attr`.

When the configuration predicate is true, `cfg_attr` expands out to the attributes listed after the predicate.

Zero, one, or more attributes may be listed. Multiple attributes will each be expanded into separate attributes.

> Example
> 
> ```rust
> #[cfg_attr(feature = "magic", sparkles, crackles)]
fn bewitched() {}

// When the `magic` feature flag is enabled, the above will expand to:
#[sparkles]
#[crackles]
fn bewitched() {}
> ```

> Note
> 
> The `cfg_attr` can expand to another `cfg_attr`. For example, `#[cfg_attr(target_os = "linux", cfg_attr(feature = "multithreaded", some_other_attribute))]` is valid. This example would be equivalent to `#[cfg_attr(all(target_os = "linux", feature = "multithreaded"), some_other_attribute)]`.

### [The `cfg` macro](#the-cfg-macro)

The built-in `cfg` macro takes in a single configuration predicate and evaluates to the `true` literal when the predicate is true and the `false` literal when it is false.

For example:

```rust
#![allow(unused)]
fn main() {
let machine_kind = if cfg!(unix) {
  "unix"
} else if cfg!(windows) {
  "windows"
} else {
  "unknown"
};

println!("I'm running on a {} machine!", machine_kind);
}
```

### [The `cfg_select` macro](#the-cfg_select-macro)

The built-in [`cfg_select!`](https://doc.rust-lang.org/core/macros/macro.cfg_select.html) macro can be used to select code at compile-time based on multiple configuration predicates.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
cfg_select! {
    unix => {
        fn foo() { /* unix specific functionality */ }
    }
    target_pointer_width = "32" => {
        fn foo() { /* non-unix, 32-bit functionality */ }
    }
    _ => {
        fn foo() { /* fallback implementation */ }
    }
}

let is_unix_str = cfg_select! {
    unix => "unix",
    _ => "not unix",
};
}
> ```

`cfg_select` expands to the payload of the first arm whose configuration predicate evaluates to true.

If the entire payload is wrapped in curly braces, the braces are removed during expansion.

The configuration predicate `_` always evaluates to true.

It is a compile error if none of the predicates evaluate to true.

Each right-hand side must be a syntactically valid expansion for the position in which the macro is invoked.