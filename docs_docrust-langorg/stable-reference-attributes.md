---
title: Attributes - The Rust Reference
url: https://doc.rust-lang.org/stable/reference/attributes.html
source: crawler
fetched_at: 2026-05-06T21:21:56.947241022-03:00
rendered_js: false
word_count: 1196
summary: This document defines attributes in the Rust programming language, covering their syntax, classification into inner and outer types, and their application to various language items.
tags:
    - rust
    - attributes
    - meta-programming
    - compiler-directives
    - language-reference
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Attributes](#attributes)

An *attribute* is a general, free-form metadatum that is interpreted according to name, convention, language, and compiler version. Attributes are modeled on Attributes in [ECMA-335](https://www.ecma-international.org/publications-and-standards/standards/ecma-335/), with the syntax coming from [ECMA-334](https://www.ecma-international.org/publications-and-standards/standards/ecma-334/) (C#).

*Inner attributes*, written with a bang (`!`) after the hash (`#`), apply to the form that the attribute is declared within.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
// General metadata applied to the enclosing module or crate.
#![crate_type = "lib"]

// Inner attribute applies to the entire function.
fn some_unused_variables() {
  #![allow(unused_variables)]

  let x = ();
  let y = ();
  let z = ();
}
}
> ```

*Outer attributes*, written without the bang after the hash, apply to the form that follows the attribute.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
// A function marked as a unit test
#[test]
fn test_foo() {
    /* ... */
}

// A conditionally-compiled module
#[cfg(target_os = "linux")]
mod bar {
    /* ... */
}

// A lint attribute used to suppress a warning/error
#[allow(non_camel_case_types)]
type int8_t = i8;
}
> ```

The attribute consists of a path to the attribute, followed by an optional delimited token tree whose interpretation is defined by the attribute. Attributes other than macro attributes also allow the input to be an equals sign (`=`) followed by an expression. See the [meta item syntax](#meta-item-attribute-syntax) below for more details.

An attribute may be unsafe to apply. To avoid undefined behavior when using these attributes, certain obligations that cannot be checked by the compiler must be met. To assert these have been, the attribute is wrapped in `unsafe(..)`, e.g. `#[unsafe(no_mangle)]`.

The following attributes are unsafe:

- [`export_name`](https://doc.rust-lang.org/stable/reference/abi.html#the-export_name-attribute)
- [`link_section`](https://doc.rust-lang.org/stable/reference/abi.html#the-link_section-attribute)
- [`naked`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-naked-attribute)
- [`no_mangle`](https://doc.rust-lang.org/stable/reference/abi.html#the-no_mangle-attribute)

Attributes can be classified into the following kinds:

- [Built-in attributes](#built-in-attributes-index)
- [Proc macro attributes](https://doc.rust-lang.org/stable/reference/procedural-macros.html#the-proc_macro_attribute-attribute)
- [Derive macro helper attributes](https://doc.rust-lang.org/stable/reference/procedural-macros.html#derive-macro-helper-attributes)
- [Tool attributes](#tool-attributes)

Attributes may be applied to many forms in the language:

- All [item declarations](https://doc.rust-lang.org/stable/reference/items.html) accept outer attributes while [external blocks](https://doc.rust-lang.org/stable/reference/items/external-blocks.html), [functions](https://doc.rust-lang.org/stable/reference/items/functions.html), [implementations](https://doc.rust-lang.org/stable/reference/items/implementations.html), and [modules](https://doc.rust-lang.org/stable/reference/items/modules.html) accept inner attributes.
- Most [statements](https://doc.rust-lang.org/stable/reference/statements.html) accept outer attributes (see [Expression Attributes](https://doc.rust-lang.org/stable/reference/expressions.html#expression-attributes) for limitations on expression statements).
- [Block expressions](https://doc.rust-lang.org/stable/reference/expressions/block-expr.html) accept outer and inner attributes, but only when they are the outer expression of an [expression statement](https://doc.rust-lang.org/stable/reference/statements.html#expression-statements) or the final expression of another block expression.
- [Enum](https://doc.rust-lang.org/stable/reference/items/enumerations.html) variants and [struct](https://doc.rust-lang.org/stable/reference/items/structs.html) and [union](https://doc.rust-lang.org/stable/reference/items/unions.html) fields accept outer attributes.
- [Match expression arms](https://doc.rust-lang.org/stable/reference/expressions/match-expr.html) accept outer attributes.
- [Generic lifetime or type parameter](https://doc.rust-lang.org/stable/reference/items/generics.html) accept outer attributes.
- Expressions accept outer attributes in limited situations, see [Expression Attributes](https://doc.rust-lang.org/stable/reference/expressions.html#expression-attributes) for details.
- [Function](https://doc.rust-lang.org/stable/reference/items/functions.html), [closure](https://doc.rust-lang.org/stable/reference/expressions/closure-expr.html) and [function pointer](https://doc.rust-lang.org/stable/reference/types/function-pointer.html) parameters accept outer attributes. This includes attributes on variadic parameters denoted with `...` in function pointers and [external blocks](https://doc.rust-lang.org/stable/reference/items/external-blocks.html#variadic-functions).
- [Inline assembly](https://doc.rust-lang.org/stable/reference/inline-assembly.html) template strings and operands accept outer attributes. Only certain attributes are accepted semantically; for details, see [asm.attributes.supported-attributes](https://doc.rust-lang.org/stable/reference/inline-assembly.html#r-asm.attributes.supported-attributes).

A “meta item” is the syntax used for the [Attr](https://doc.rust-lang.org/stable/reference/attributes.html#grammar-Attr) rule by most [built-in attributes](#built-in-attributes-index). It has the following grammar:

Expressions in meta items must macro-expand to literal expressions, which must not include integer or float type suffixes. Expressions which are not literal expressions will be syntactically accepted (and can be passed to proc-macros), but will be rejected after parsing.

Note that if the attribute appears within another macro, it will be expanded after that outer macro. For example, the following code will expand the `Serialize` proc-macro first, which must preserve the `include_str!` call in order for it to be expanded:

```rust
#[derive(Serialize)]
struct Foo {
    #[doc = include_str!("x.md")]
    x: u32
}
```

Additionally, macros in attributes will be expanded only after all other attributes applied to the item:

```rust
#[macro_attr1] // expanded first
#[doc = mac!()] // `mac!` is expanded fourth.
#[macro_attr2] // expanded second
#[derive(MacroDerive1, MacroDerive2)] // expanded third
fn foo() {}
```

Various built-in attributes use different subsets of the meta item syntax to specify their inputs. The following grammar rules show some commonly used forms:

Some examples of meta items are:

## [Active and inert attributes](#active-and-inert-attributes)

An attribute is either active or inert. During attribute processing, *active attributes* remove themselves from the form they are on while *inert attributes* stay on.

The [`cfg`](https://doc.rust-lang.org/stable/reference/conditional-compilation.html#the-cfg-attribute) and [`cfg_attr`](https://doc.rust-lang.org/stable/reference/conditional-compilation.html#the-cfg_attr-attribute) attributes are active. [Attribute macros](https://doc.rust-lang.org/stable/reference/procedural-macros.html#the-proc_macro_attribute-attribute) are active. All other attributes are inert.

The compiler may allow attributes for external tools where each tool resides in its own module in the [tool prelude](https://doc.rust-lang.org/stable/reference/names/preludes.html#tool-prelude). The first segment of the attribute path is the name of the tool, with one or more additional segments whose interpretation is up to the tool.

When a tool is not in use, the tool’s attributes are accepted without a warning. When the tool is in use, the tool is responsible for processing and interpretation of its attributes.

Tool attributes are not available if the [`no_implicit_prelude`](https://doc.rust-lang.org/stable/reference/names/preludes.html#the-no_implicit_prelude-attribute) attribute is used.

```rust
#![allow(unused)]
fn main() {
// Tells the rustfmt tool to not format the following element.
#[rustfmt::skip]
struct S {
}

// Controls the "cyclomatic complexity" threshold for the clippy tool.
#[clippy::cyclomatic_complexity = "100"]
pub fn f() {}
}
```

> Note
> 
> `rustc` currently recognizes the tools “clippy”, “rustfmt”, “diagnostic”, “miri”, and “rust\_analyzer”.

## [Built-in attributes index](#built-in-attributes-index)

The following is an index of all built-in attributes.

- Conditional compilation
  
  - [`cfg`](https://doc.rust-lang.org/stable/reference/conditional-compilation.html#the-cfg-attribute) — Controls conditional compilation.
  - [`cfg_attr`](https://doc.rust-lang.org/stable/reference/conditional-compilation.html#the-cfg_attr-attribute) — Conditionally includes attributes.
- Testing
  
  - [`test`](https://doc.rust-lang.org/stable/reference/attributes/testing.html#the-test-attribute) — Marks a function as a test.
  - [`ignore`](https://doc.rust-lang.org/stable/reference/attributes/testing.html#the-ignore-attribute) — Disables a test function.
  - [`should_panic`](https://doc.rust-lang.org/stable/reference/attributes/testing.html#the-should_panic-attribute) — Indicates a test should generate a panic.
- Derive
  
  - [`derive`](https://doc.rust-lang.org/stable/reference/attributes/derive.html) — Automatic trait implementations.
  - [`automatically_derived`](https://doc.rust-lang.org/stable/reference/attributes/derive.html#the-automatically_derived-attribute) — Marker for implementations created by `derive`.
- Macros
  
  - [`macro_export`](https://doc.rust-lang.org/stable/reference/macros-by-example.html#the-macro_export-attribute) — Exports a `macro_rules` macro for cross-crate usage.
  - [`macro_use`](https://doc.rust-lang.org/stable/reference/macros-by-example.html#the-macro_use-attribute) — Expands macro visibility, or imports macros from other crates.
  - [`proc_macro`](https://doc.rust-lang.org/stable/reference/procedural-macros.html#the-proc_macro-attribute) — Defines a function-like macro.
  - [`proc_macro_derive`](https://doc.rust-lang.org/stable/reference/procedural-macros.html#r-macro.proc.derive) — Defines a derive macro.
  - [`proc_macro_attribute`](https://doc.rust-lang.org/stable/reference/procedural-macros.html#the-proc_macro_attribute-attribute) — Defines an attribute macro.
- Diagnostics
  
  - [`allow`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#lint-check-attributes), [`expect`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#lint-check-attributes), [`warn`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#lint-check-attributes), [`deny`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#lint-check-attributes), [`forbid`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#lint-check-attributes) — Alters the default lint level.
  - [`deprecated`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#the-deprecated-attribute) — Generates deprecation notices.
  - [`must_use`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#the-must_use-attribute) — Generates a lint for unused values.
  - [`diagnostic::on_unimplemented`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#the-diagnosticon_unimplemented-attribute) — Hints the compiler to emit a certain error message if a trait is not implemented.
  - [`diagnostic::do_not_recommend`](https://doc.rust-lang.org/stable/reference/attributes/diagnostics.html#the-diagnosticdo_not_recommend-attribute) — Hints the compiler to not show a certain trait impl in error messages.
- ABI, linking, symbols, and FFI
  
  - [`link`](https://doc.rust-lang.org/stable/reference/items/external-blocks.html#the-link-attribute) — Specifies a native library to link with an `extern` block.
  - [`link_name`](https://doc.rust-lang.org/stable/reference/items/external-blocks.html#the-link_name-attribute) — Specifies the name of the symbol for functions or statics in an `extern` block.
  - [`link_ordinal`](https://doc.rust-lang.org/stable/reference/items/external-blocks.html#the-link_ordinal-attribute) — Specifies the ordinal of the symbol for functions or statics in an `extern` block.
  - [`no_link`](https://doc.rust-lang.org/stable/reference/items/extern-crates.html#the-no_link-attribute) — Prevents linking an extern crate.
  - [`repr`](https://doc.rust-lang.org/stable/reference/type-layout.html#representations) — Controls type layout.
  - [`crate_type`](https://doc.rust-lang.org/stable/reference/linkage.html) — Specifies the type of crate (library, executable, etc.).
  - [`no_main`](https://doc.rust-lang.org/stable/reference/crates-and-source-files.html#the-no_main-attribute) — Disables emitting the `main` symbol.
  - [`export_name`](https://doc.rust-lang.org/stable/reference/abi.html#the-export_name-attribute) — Specifies the exported symbol name for a function or static.
  - [`link_section`](https://doc.rust-lang.org/stable/reference/abi.html#the-link_section-attribute) — Specifies the section of an object file to use for a function or static.
  - [`no_mangle`](https://doc.rust-lang.org/stable/reference/abi.html#the-no_mangle-attribute) — Disables symbol name encoding.
  - [`used`](https://doc.rust-lang.org/stable/reference/abi.html#the-used-attribute) — Forces the compiler to keep a static item in the output object file.
  - [`crate_name`](https://doc.rust-lang.org/stable/reference/crates-and-source-files.html#the-crate_name-attribute) — Specifies the crate name.
- Code generation
  
  - [`inline`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-inline-attribute) — Hint to inline code.
  - [`cold`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-cold-attribute) — Hint that a function is unlikely to be called.
  - [`naked`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-naked-attribute) — Prevent the compiler from emitting a function prologue and epilogue.
  - [`no_builtins`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-no_builtins-attribute) — Disables use of certain built-in functions.
  - [`target_feature`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-target_feature-attribute) — Configure platform-specific code generation.
  - [`track_caller`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-track_caller-attribute) — Pass the parent call location to `std::panic::Location::caller()`.
  - [`instruction_set`](https://doc.rust-lang.org/stable/reference/attributes/codegen.html#the-instruction_set-attribute) — Specify the instruction set used to generate a function’s code.
- Documentation
  
  - `doc` — Specifies documentation. See [The Rustdoc Book](https://doc.rust-lang.org/stable/rustdoc/the-doc-attribute.html) for more information. [Doc comments](https://doc.rust-lang.org/stable/reference/comments.html#doc-comments) are transformed into `doc` attributes.
- Preludes
  
  - [`no_std`](https://doc.rust-lang.org/stable/reference/names/preludes.html#the-no_std-attribute) — Removes std from the prelude.
  - [`no_implicit_prelude`](https://doc.rust-lang.org/stable/reference/names/preludes.html#the-no_implicit_prelude-attribute) — Disables prelude lookups within a module.
- Modules
  
  - [`path`](https://doc.rust-lang.org/stable/reference/items/modules.html#the-path-attribute) — Specifies the filename for a module.
- Limits
  
  - [`recursion_limit`](https://doc.rust-lang.org/stable/reference/attributes/limits.html#the-recursion_limit-attribute) — Sets the maximum recursion limit for certain compile-time operations.
  - [`type_length_limit`](https://doc.rust-lang.org/stable/reference/attributes/limits.html#the-type_length_limit-attribute) — Sets the maximum size of a polymorphic type.
- Runtime
  
  - [`panic_handler`](https://doc.rust-lang.org/stable/reference/panic.html#the-panic_handler-attribute) — Sets the function to handle panics.
  - [`global_allocator`](https://doc.rust-lang.org/stable/reference/runtime.html#the-global_allocator-attribute) — Sets the global memory allocator.
  - [`windows_subsystem`](https://doc.rust-lang.org/stable/reference/runtime.html#the-windows_subsystem-attribute) — Specifies the windows subsystem to link with.
- Features
  
  - `feature` — Used to enable unstable or experimental compiler features. See [The Unstable Book](https://doc.rust-lang.org/stable/unstable-book/index.html) for features implemented in `rustc`.
- Type System
  
  - [`non_exhaustive`](https://doc.rust-lang.org/stable/reference/attributes/type_system.html#the-non_exhaustive-attribute) — Indicate that a type will have more fields/variants added in future.
- Debugger
  
  - [`debugger_visualizer`](https://doc.rust-lang.org/stable/reference/attributes/debugger.html#the-debugger_visualizer-attribute) — Embeds a file that specifies debugger output for a type.
  - [`collapse_debuginfo`](https://doc.rust-lang.org/stable/reference/attributes/debugger.html#the-collapse_debuginfo-attribute) — Controls how macro invocations are encoded in debuginfo.