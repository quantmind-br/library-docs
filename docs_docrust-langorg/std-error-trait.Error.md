---
title: Error in std::error - Rust
url: https://doc.rust-lang.org/std/error/trait.Error.html
source: crawler
fetched_at: 2026-05-06T21:23:26.079040101-03:00
rendered_js: false
word_count: 690
summary: The Error trait defines the standard interface for error types in Rust, enabling consistent error reporting, source chain tracking, and type-based context retrieval.
tags:
    - rust
    - error-handling
    - trait
    - std-library
    - debugging
category: reference
---

## Trait Error

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#59)

```rust
pub trait Error: Debug + Display {
    // Provided methods
    fn source(&self) -> Option<&(dyn Error + 'static)> { ... }
    fn description(&self) -> &str { ... }
    fn cause(&self) -> Option<&dyn Error> { ... }
    fn provide<'a>(&'a self, request: &mut Request<'a>) { ... }
}
```

Expand description

`Error` is a trait representing the basic expectations for error values, i.e., values of type `E` in [`Result<T, E>`](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result").

Errors must describe themselves through the [`Display`](https://doc.rust-lang.org/std/fmt/trait.Display.html "trait std::fmt::Display") and [`Debug`](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug") traits. Error messages are typically concise lowercase sentences without trailing punctuation:

```rust
let err = "NaN".parse::<u32>().unwrap_err();
assert_eq!(err.to_string(), "invalid digit found in string");
```

## [§](#error-source)Error source

Errors may provide cause information. [`Error::source()`](https://doc.rust-lang.org/std/error/trait.Error.html#method.source "method std::error::Error::source") is generally used when errors cross “abstraction boundaries”. If one module must report an error that is caused by an error from a lower-level module, it can allow accessing that error via `Error::source()`. This makes it possible for the high-level module to provide its own errors while also revealing some of the implementation for debugging.

In error types that wrap an underlying error, the underlying error should be either returned by the outer error’s `Error::source()`, or rendered by the outer error’s `Display` implementation, but not both.

## [§](#example)Example

Implementing the `Error` trait only requires that `Debug` and `Display` are implemented too.

```rust
use std::error::Error;
use std::fmt;
use std::path::PathBuf;

#[derive(Debug)]
struct ReadConfigError {
    path: PathBuf
}

impl fmt::Display for ReadConfigError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let path = self.path.display();
        write!(f, "unable to read configuration at {path}")
    }
}

impl Error for ReadConfigError {}
```

1.30.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#111)

Returns the lower-level source of this error, if any.

##### [§](#examples)Examples

```rust
use std::error::Error;
use std::fmt;

#[derive(Debug)]
struct SuperError {
    source: SuperErrorSideKick,
}

impl fmt::Display for SuperError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "SuperError is here!")
    }
}

impl Error for SuperError {
    fn source(&self) -> Option<&(dyn Error + 'static)> {
        Some(&self.source)
    }
}

#[derive(Debug)]
struct SuperErrorSideKick;

impl fmt::Display for SuperErrorSideKick {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "SuperErrorSideKick is here!")
    }
}

impl Error for SuperErrorSideKick {}

fn get_super_error() -> Result<(), SuperError> {
    Err(SuperError { source: SuperErrorSideKick })
}

fn main() {
    match get_super_error() {
        Err(e) => {
            println!("Error: {e}");
            println!("Caused by: {}", e.source().unwrap());
        }
        _ => println!("No error"),
    }
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#137)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

```rust
if let Err(e) = "xc".parse::<u32>() {
    // Print `e` itself, no need for description().
    eprintln!("Error: {e}");
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#147)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/src/core/error.rs.html#260)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports.

Used in conjunction with [`Request::provide_value`](https://doc.rust-lang.org/std/error/struct.Request.html#method.provide_value "method std::error::Request::provide_value") and [`Request::provide_ref`](https://doc.rust-lang.org/std/error/struct.Request.html#method.provide_ref "method std::error::Request::provide_ref") to extract references to member variables from `dyn Error` trait objects.

##### [§](#example-1)Example

```rust
#![feature(error_generic_member_access)]
use core::fmt;
use core::error::{request_ref, Request};

#[derive(Debug)]
enum MyLittleTeaPot {
    Empty,
}

#[derive(Debug)]
struct MyBacktrace {
    // ...
}

impl MyBacktrace {
    fn new() -> MyBacktrace {
        // ...
    }
}

#[derive(Debug)]
struct Error {
    backtrace: MyBacktrace,
}

impl fmt::Display for Error {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "Example Error")
    }
}

impl std::error::Error for Error {
    fn provide<'a>(&'a self, request: &mut Request<'a>) {
        request
            .provide_ref::<MyBacktrace>(&self.backtrace);
    }
}

fn main() {
    let backtrace = MyBacktrace::new();
    let error = Error { backtrace };
    let dyn_error = &error as &dyn std::error::Error;
    let backtrace_ref = request_ref::<MyBacktrace>(dyn_error).unwrap();

    assert!(core::ptr::eq(&error.backtrace, backtrace_ref));
    assert!(request_ref::<MyLittleTeaPot>(dyn_error).is_none());
}
```

##### [§](#delegating-impls)Delegating Impls

**Warning**: We recommend implementors avoid delegating implementations of `provide` to source error implementations.

This method should expose context from the current piece of the source chain only, not from sources that are exposed in the chain of sources. Delegating `provide` implementations cause the same context to be provided by multiple errors in the chain of sources which can cause unintended duplication of information in error reports or require heuristics to deduplicate.

In other words, the following implementation pattern for `provide` is discouraged and should not be used for [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") types exposed in public APIs to third parties.

```rust
struct MyError {
    source: Error,
}

impl std::error::Error for MyError {
    fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
        Some(&self.source)
    }

    fn provide<'a>(&'a self, request: &mut Request<'a>) {
        self.source.provide(request) // <--- Discouraged
    }
}
```

[Source](https://doc.rust-lang.org/src/core/error.rs.html#275)[§](#impl-dyn+Error)

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#279)

Returns `true` if the inner type is the same as `T`.

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#294)

Returns some reference to the inner value if it is of type `T`, or `None` if it isn’t.

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#307)

Returns some mutable reference to the inner value if it is of type `T`, or `None` if it isn’t.

[Source](https://doc.rust-lang.org/src/core/error.rs.html#317)[§](#impl-dyn+Error+%2B+Send)

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#321)

Forwards to the method defined on the type `dyn Error`.

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#328)

Forwards to the method defined on the type `dyn Error`.

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#335)

Forwards to the method defined on the type `dyn Error`.

[Source](https://doc.rust-lang.org/src/core/error.rs.html#340)[§](#impl-dyn+Error+%2B+Send+%2B+Sync)

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#344)

Forwards to the method defined on the type `dyn Error`.

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#351)

Forwards to the method defined on the type `dyn Error`.

1.3.0 · [Source](https://doc.rust-lang.org/src/core/error.rs.html#358)

Forwards to the method defined on the type `dyn Error`.

[Source](https://doc.rust-lang.org/src/core/error.rs.html#363)[§](#impl-dyn+Error-1)

[Source](https://doc.rust-lang.org/src/core/error.rs.html#417)

🔬This is a nightly-only experimental API. (`error_iter` [#58520](https://github.com/rust-lang/rust/issues/58520))

Returns an iterator starting with the current error and continuing with recursively calling [`Error::source`](https://doc.rust-lang.org/std/error/trait.Error.html#method.source "method std::error::Error::source").

If you want to omit the current error and only use its sources, use `skip(1)`.

##### [§](#examples-1)Examples

```rust
#![feature(error_iter)]
use std::error::Error;
use std::fmt;

#[derive(Debug)]
struct A;

#[derive(Debug)]
struct B(Option<Box<dyn Error + 'static>>);

impl fmt::Display for A {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "A")
    }
}

impl fmt::Display for B {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "B")
    }
}

impl Error for A {}

impl Error for B {
    fn source(&self) -> Option<&(dyn Error + 'static)> {
        self.0.as_ref().map(|e| e.as_ref())
    }
}

let b = B(Some(Box::new(A)));

// let err : Box<Error> = b.into(); // or
let err = &b as &dyn Error;

let mut iter = err.sources();

assert_eq!("B".to_string(), iter.next().unwrap().to_string());
assert_eq!("A".to_string(), iter.next().unwrap().to_string());
assert!(iter.next().is_none());
assert!(iter.next().is_none());
```

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#705)[§](#impl-dyn+Error-2)

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#710)

Attempts to downcast the box to a concrete type.

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#722)[§](#impl-dyn+Error+%2B+Send-1)

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#727)

Attempts to downcast the box to a concrete type.

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#736)[§](#impl-dyn+Error+%2B+Send+%2B+Sync-1)

1.3.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#741)

Attempts to downcast the box to a concrete type.

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#645)[§](#impl-From%3C%26str%3E-for-Box%3Cdyn+Error%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#659)[§](#method.from-5)

Converts a [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error").

##### [§](#examples-7)Examples

```rust
use std::error::Error;

let a_str_error = "a str error";
let a_boxed_error = Box::<dyn Error>::from(a_str_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#622)[§](#impl-From%3C%26str%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#638)[§](#method.from-4)

Converts a [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync").

##### [§](#examples-6)Examples

```rust
use std::error::Error;

let a_str_error = "a str error";
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_str_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```

1.22.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#687)[§](#impl-From%3CCow%3C'b,+str%3E%3E-for-Box%3Cdyn+Error%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#700)[§](#method.from-7)

Converts a [`Cow`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "enum std::borrow::Cow") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error").

##### [§](#examples-9)Examples

```rust
use std::error::Error;
use std::borrow::Cow;

let a_cow_str_error = Cow::from("a str error");
let a_boxed_error = Box::<dyn Error>::from(a_cow_str_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.22.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#666)[§](#impl-From%3CCow%3C'b,+str%3E%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#680)[§](#method.from-6)

Converts a [`Cow`](https://doc.rust-lang.org/std/borrow/enum.Cow.html "enum std::borrow::Cow") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync").

##### [§](#examples-8)Examples

```rust
use std::error::Error;
use std::borrow::Cow;

let a_cow_str_error = Cow::from("a str error");
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_cow_str_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#493)[§](#impl-From%3CE%3E-for-Box%3Cdyn+Error%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#518)[§](#method.from)

Converts a type of [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error").

##### [§](#examples-2)Examples

```rust
use std::error::Error;
use std::fmt;

#[derive(Debug)]
struct AnError;

impl fmt::Display for AnError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "An error")
    }
}

impl Error for AnError {}

let an_error = AnError;
assert!(0 == size_of_val(&an_error));
let a_boxed_error = Box::<dyn Error>::from(an_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#525)[§](#impl-From%3CE%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#556)[§](#method.from-1)

Converts a type of [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync").

##### [§](#examples-3)Examples

```rust
use std::error::Error;
use std::fmt;

#[derive(Debug)]
struct AnError;

impl fmt::Display for AnError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "An error")
    }
}

impl Error for AnError {}

unsafe impl Send for AnError {}

unsafe impl Sync for AnError {}

let an_error = AnError;
assert!(0 == size_of_val(&an_error));
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(an_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```

1.6.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#601)[§](#impl-From%3CString%3E-for-Box%3Cdyn+Error%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#613)[§](#method.from-3)

Converts a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error").

##### [§](#examples-5)Examples

```rust
use std::error::Error;

let a_string_error = "a string error".to_string();
let a_boxed_error = Box::<dyn Error>::from(a_string_error);
assert!(size_of::<Box<dyn Error>>() == size_of_val(&a_boxed_error))
```

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#563)[§](#impl-From%3CString%3E-for-Box%3Cdyn+Error+%2B+Send+%2B+Sync%3E)

[Source](https://doc.rust-lang.org/src/alloc/boxed/convert.rs.html#577)[§](#method.from-2)

Converts a [`String`](https://doc.rust-lang.org/std/string/struct.String.html "struct std::string::String") into a box of dyn [`Error`](https://doc.rust-lang.org/std/error/trait.Error.html "trait std::error::Error") + [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") + [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync").

##### [§](#examples-4)Examples

```rust
use std::error::Error;

let a_string_error = "a string error".to_string();
let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_string_error);
assert!(
    size_of::<Box<dyn Error + Send + Sync>>() == size_of_val(&a_boxed_error))
```