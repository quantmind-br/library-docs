---
title: Testing - The Rust Reference
url: https://doc.rust-lang.org/reference/attributes/testing.html#the-should_panic-attribute
source: crawler
fetched_at: 2026-05-06T21:24:55.168254236-03:00
rendered_js: false
word_count: 613
summary: This document describes the attributes used for testing in the Rust programming language, specifically detailing the usage and behavior of test, ignore, and should_panic annotations.
tags:
    - rust
    - testing
    - attributes
    - unit-testing
    - compiler-directives
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Testing attributes](#testing-attributes)

The following [attributes](https://doc.rust-lang.org/reference/attributes.html) are used for specifying functions for performing tests. Compiling a crate in “test” mode enables building the test functions along with a test harness for executing the tests. Enabling the test mode also enables the [`test` conditional compilation option](https://doc.rust-lang.org/reference/conditional-compilation.html#test).

## [The `test` attribute](#the-test-attribute)

The *`test` [attribute](https://doc.rust-lang.org/reference/attributes.html)* marks a function to be executed as a test.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
pub fn add(left: u64, right: u64) -> u64 { left + right }
#[test]
fn it_works() {
    let result = add(2, 2);
    assert_eq!(result, 4);
}
}
> ```

The `test` attribute uses the [MetaWord](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaWord) syntax.

The `test` attribute may only be applied to [free functions](https://doc.rust-lang.org/reference/glossary.html#free-item) that are monomorphic, that take no arguments, and where the return type implements the [`Termination`](https://doc.rust-lang.org/std/process/trait.Termination.html) trait.

> Note
> 
> Some of types that implement the [`Termination`](https://doc.rust-lang.org/std/process/trait.Termination.html) trait include:
> 
> - `()`
> - `Result<T, E> where T: Termination, E: Debug`

Only the first use of `test` on a function has effect.

> Note
> 
> `rustc` lints against any use following the first. This may become an error in the future.

The `test` attribute is exported from the standard library prelude as [`std::prelude::v1::test`](https://doc.rust-lang.org/core/macros/builtin/attr.test.html).

These functions are only compiled when in test mode.

> Note
> 
> The test mode is enabled by passing the `--test` argument to `rustc` or using `cargo test`.

The test harness calls the returned value’s [`report`](https://doc.rust-lang.org/std/process/trait.Termination.html#tymethod.report) method, and classifies the test as passed or failed depending on whether the resulting [`ExitCode`](https://doc.rust-lang.org/std/process/struct.ExitCode.html) represents successful termination. In particular:

- Tests that return `()` pass as long as they terminate and do not panic.
- Tests that return a `Result<(), E>` pass as long as they return `Ok(())`.
- Tests that return `ExitCode::SUCCESS` pass, and tests that return `ExitCode::FAILURE` fail.
- Tests that do not terminate neither pass nor fail.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
use std::io;
fn setup_the_thing() -> io::Result<i32> { Ok(1) }
fn do_the_thing(s: &i32) -> io::Result<()> { Ok(()) }
#[test]
fn test_the_thing() -> io::Result<()> {
    let state = setup_the_thing()?; // expected to succeed
    do_the_thing(&state)?;          // expected to succeed
    Ok(())
}
}
> ```

## [The `ignore` attribute](#the-ignore-attribute)

The *`ignore` [attribute](https://doc.rust-lang.org/reference/attributes.html)* can be used with the [`test` attribute](https://doc.rust-lang.org/reference/attributes/testing.html#r-attributes.testing.test) to tell the test harness to not execute that function as a test.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
#[test]
#[ignore]
fn check_thing() {
    // …
}
}
> ```

> Note
> 
> The `rustc` test harness supports the `--include-ignored` flag to force ignored tests to be run.

The `ignore` attribute uses the [MetaWord](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaWord) and [MetaNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaNameValueStr) syntaxes.

The [MetaNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaNameValueStr) form of the `ignore` attribute provides a way to specify a reason why the test is ignored.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
#[test]
#[ignore = "not yet implemented"]
fn mytest() {
    // …
}
}
> ```

The `ignore` attribute may only be applied to functions annotated with the `test` attribute.

> Note
> 
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

Only the first use of `ignore` on a function has effect.

> Note
> 
> `rustc` lints against any use following the first. This may become an error in the future.

Ignored tests are still compiled when in test mode, but they are not executed.

## [The `should_panic` attribute](#the-should_panic-attribute)

The *`should_panic` [attribute](https://doc.rust-lang.org/reference/attributes.html)* causes a test to pass only if the [test function](https://doc.rust-lang.org/reference/attributes/testing.html#r-attributes.testing.test) to which the attribute is applied panics.

> Example
> 
> ```rust
> #![allow(unused)]
fn main() {
#[test]
#[should_panic(expected = "values don't match")]
fn mytest() {
    assert_eq!(1, 2, "values don't match");
}
}
> ```

The `should_panic` attribute has these forms:

- [MetaWord](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaWord)
  
  > Example
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  #[test]
  #[should_panic]
  fn mytest() { panic!("error: some message, and more"); }
  }
  > ```
- [MetaNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaNameValueStr) — The given string must appear within the panic message for the test to pass.
  
  > Example
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  #[test]
  #[should_panic = "some message"]
  fn mytest() { panic!("error: some message, and more"); }
  }
  > ```
- [MetaListNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaListNameValueStr) — As with the [MetaNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaNameValueStr) syntax, the given string must appear within the panic message.
  
  > Example
  > 
  > ```rust
  > #![allow(unused)]
  fn main() {
  #[test]
  #[should_panic(expected = "some message")]
  fn mytest() { panic!("error: some message, and more"); }
  }
  > ```

The `should_panic` attribute may only be applied to functions annotated with the `test` attribute.

> Note
> 
> `rustc` ignores use in other positions but lints against it. This may become an error in the future.

Only the first use of `should_panic` on a function has effect.

> Note
> 
> `rustc` lints against any use following the first with a future-compatibility warning. This may become an error in the future.

When the [MetaNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaNameValueStr) form or the [MetaListNameValueStr](https://doc.rust-lang.org/reference/attributes.html#grammar-MetaListNameValueStr) form with the `expected` key is used, the given string must appear somewhere within the panic message for the test to pass.

The return type of the test function must be `()`.