---
title: never - Rust
url: https://doc.rust-lang.org/stable/std/primitive.never.html
source: crawler
fetched_at: 2026-05-06T21:25:52.348663668-03:00
rendered_js: false
word_count: 1293
summary: This document explains the Rust 'never' type (!), which represents computations that never return, its ability to coerce into any other type, and its practical application in generic programming and trait implementations.
tags:
    - rust
    - never-type
    - type-theory
    - generics
    - error-handling
    - primitive-types
category: concept
---

## Primitive Type never

🔬This is a nightly-only experimental API. (`never_type` [#35121](https://github.com/rust-lang/rust/issues/35121))

Expand description

The `!` type, also called “never”.

`!` represents the type of computations which never resolve to any value at all. For example, the [`exit`](https://doc.rust-lang.org/stable/std/process/fn.exit.html) function `fn exit(code: i32) -> !` exits the process without ever returning, and so returns `!`.

`break`, `continue` and `return` expressions also have type `!`. For example we are allowed to write:

```rust
#![feature(never_type)]
let x: ! = {
    return 123
};
```

Although the `let` is pointless here, it illustrates the meaning of `!`. Since `x` is never assigned a value (because `return` returns from the entire function), `x` can be given type `!`. We could also replace `return 123` with a `panic!` or a never-ending `loop` and this code would still be valid.

A more realistic usage of `!` is in this code:

```rust
let num: u32 = match get_a_number() {
    Some(num) => num,
    None => break,
};
```

Both match arms must produce values of type [`u32`](https://doc.rust-lang.org/stable/std/primitive.u32.html "primitive u32"), but since `break` never produces a value at all we know it can never produce a value which isn’t a [`u32`](https://doc.rust-lang.org/stable/std/primitive.u32.html "primitive u32"). This illustrates another behavior of the `!` type - expressions with type `!` will coerce into any other type.

## [§](#-and-generics)`!` and generics

### [§](#infallible-errors)Infallible errors

The main place you’ll see `!` used explicitly is in generic code. Consider the [`FromStr`](https://doc.rust-lang.org/stable/std/str/trait.FromStr.html "trait std::str::FromStr") trait:

```rust
trait FromStr: Sized {
    type Err;
    fn from_str(s: &str) -> Result<Self, Self::Err>;
}
```

When implementing this trait for [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html) we need to pick a type for [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err"). And since converting a string into a string will never result in an error, the appropriate type is `!`. (Currently the type actually used is an enum with no variants, though this is only because `!` was added to Rust at a later date and it may change in the future.) With an [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") type of `!`, if we have to call [`String::from_str`](https://doc.rust-lang.org/stable/std/str/trait.FromStr.html#tymethod.from_str "associated function std::str::FromStr::from_str") for some reason the result will be a [`Result<String, !>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") which we can unpack like this:

```rust
use std::str::FromStr;
let Ok(s) = String::from_str("hello");
```

Since the [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") variant contains a `!`, it can never occur. This means we can exhaustively match on [`Result<T, !>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") by just taking the [`Ok`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") variant. This illustrates another behavior of `!` - it can be used to “delete” certain enum variants from generic types like `Result`.

### [§](#infinite-loops)Infinite loops

While [`Result<T, !>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") is very useful for removing errors, `!` can also be used to remove successes as well. If we think of [`Result<T, !>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") as “if this function returns, it has not errored,” we get a very intuitive idea of [`Result<!, E>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") as well: if the function returns, it *has* errored.

For example, consider the case of a simple web server, which can be simplified to:

[ⓘ](# "This example is not tested")

```rust
loop {
    let (client, request) = get_request().expect("disconnected");
    let response = request.process();
    response.send(client);
}
```

Currently, this isn’t ideal, because we simply panic whenever we fail to get a new connection. Instead, we’d like to keep track of this error, like this:

[ⓘ](# "This example is not tested")

```rust
loop {
    match get_request() {
        Err(err) => break err,
        Ok((client, request)) => {
            let response = request.process();
            response.send(client);
        },
    }
}
```

Now, when the server disconnects, we exit the loop with an error instead of panicking. While it might be intuitive to simply return the error, we might want to wrap it in a [`Result<!, E>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") instead:

[ⓘ](# "This example is not tested")

```rust
fn server_loop() -> Result<!, ConnectionError> {
    loop {
        let (client, request) = get_request()?;
        let response = request.process();
        response.send(client);
    }
}
```

Now, we can use `?` instead of `match`, and the return type makes a lot more sense: if the loop ever stops, it means that an error occurred. We don’t even have to wrap the loop in an `Ok` because `!` coerces to `Result<!, ConnectionError>` automatically.

## [§](#-and-traits)`!` and traits

When writing your own traits, `!` should have an `impl` whenever there is an obvious `impl` which doesn’t `panic!`. The reason is that functions returning an `impl Trait` where `!` does not have an `impl` of `Trait` cannot diverge as their only possible code path. In other words, they can’t return `!` from every code path. As an example, this code doesn’t compile:

[ⓘ](# "This example deliberately fails to compile")

```rust
use std::ops::Add;

fn foo() -> impl Add<u32> {
    unimplemented!()
}
```

But this code does:

```rust
use std::ops::Add;

fn foo() -> impl Add<u32> {
    if true {
        unimplemented!()
    } else {
        0
    }
}
```

The reason is that, in the first example, there are many possible types that `!` could coerce to, because many types implement `Add<u32>`. However, in the second example, the `else` branch returns a `0`, which the compiler infers from the return type to be of type `u32`. Since `u32` is a concrete type, `!` can and will be coerced to it. See issue [#36375](https://github.com/rust-lang/rust/issues/36375) for more information on this quirk of `!`.

As it turns out, though, most traits can have an `impl` for `!`. Take [`Debug`](https://doc.rust-lang.org/stable/std/fmt/trait.Debug.html "trait std::fmt::Debug") for example:

```rust
#![feature(never_type)]
impl Debug for ! {
    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        *self
    }
}
```

Once again we’re using `!`’s ability to coerce into any other type, in this case [`fmt::Result`](https://doc.rust-lang.org/stable/std/fmt/type.Result.html "type std::fmt::Result"). Since this method takes a `&!` as an argument we know that it can never be called (because there is no value of type `!` for it to be called with). Writing `*self` essentially tells the compiler “We know that this code can never be run, so just treat the entire function body as having type [`fmt::Result`](https://doc.rust-lang.org/stable/std/fmt/type.Result.html "type std::fmt::Result")”. This pattern can be used a lot when implementing traits for `!`. Generally, any trait which only has methods which take a `self` parameter should have such an impl.

On the other hand, one trait which would not be appropriate to implement is [`Default`](https://doc.rust-lang.org/stable/std/default/trait.Default.html "trait std::default::Default"):

```rust
trait Default {
    fn default() -> Self;
}
```

Since `!` has no values, it has no default value either. It’s true that we could write an `impl` for this which simply panics, but the same is true for any type (we could `impl Default` for (eg.) [`File`](https://doc.rust-lang.org/stable/std/fs/struct.File.html) by just making [`default()`](https://doc.rust-lang.org/stable/std/default/trait.Default.html#tymethod.default "associated function std::default::Default::default") panic.)

## [§](#never-type-fallback)Never type fallback

When the compiler sees a value of type `!` in a [coercion site](https://doc.rust-lang.org/reference/type-coercions.html#coercion-sites), it implicitly inserts a coercion to allow the type checker to infer any type:

[ⓘ](# "This example is not tested")

```rust
// this
let x: u8 = panic!();

// is (essentially) turned by the compiler into
let x: u8 = absurd(panic!());

// where absurd is a function with the following signature
// (it's sound, because `!` always marks unreachable code):
fn absurd<T>(_: !) -> T { ... }
```

This can lead to compilation errors if the type cannot be inferred:

[ⓘ](# "This example deliberately fails to compile")

```rust
// this
{ panic!() };

// gets turned into this
{ absurd(panic!()) }; // error: can't infer the type of `absurd`
```

To prevent such errors, the compiler remembers where it inserted `absurd` calls, and if it can’t infer the type, it uses the fallback type instead:

[ⓘ](# "This example is not tested")

```rust
type Fallback = /* An arbitrarily selected type! */;
{ absurd::<Fallback>(panic!()) }
```

This is what is known as “never type fallback”.

Historically, the fallback type was [`()`](https://doc.rust-lang.org/stable/std/primitive.unit.html "primitive unit"), causing confusing behavior where `!` spontaneously coerced to `()`, even when it would not infer `()` without the fallback. The fallback was changed to `!` in the [2024 edition](https://doc.rust-lang.org/edition-guide/rust-2024/never-type-fallback.html), and will be changed in all editions at a later date.

[Source](https://doc.rust-lang.org/stable/src/core/clone.rs.html#636)[§](#impl-Clone-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/mod.rs.html#2878)[§](#impl-Debug-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/fmt/mod.rs.html#2886)[§](#impl-Display-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#272)[§](#impl-Error-for-!)

1.30.0 · [Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#111)[§](#method.source)

Returns the lower-level source of this error, if any. [Read more](https://doc.rust-lang.org/stable/std/error/trait.Error.html#method.source)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#137)[§](#method.description)

👎Deprecated since 1.42.0: use the Display impl or to\_string()

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#147)[§](#method.cause)

👎Deprecated since 1.33.0: replaced by Error::source, which can support downcasting

[Source](https://doc.rust-lang.org/stable/src/core/error.rs.html#260)[§](#method.provide)

🔬This is a nightly-only experimental API. (`error_generic_member_access` [#99301](https://github.com/rust-lang/rust/issues/99301))

Provides type-based access to context intended for error reports. [Read more](https://doc.rust-lang.org/stable/std/error/trait.Error.html#method.provide)

1.34.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#987)[§](#impl-From%3C!%3E-for-Infallible)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#989)[§](#method.from-1)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/stable/src/core/num/error.rs.html#32)[§](#impl-From%3C!%3E-for-TryFromIntError)

[Source](https://doc.rust-lang.org/stable/src/core/num/error.rs.html#34)[§](#method.from)

Converts to this type from the input type.

1.29.0 · [Source](https://doc.rust-lang.org/stable/src/core/hash/mod.rs.html#870)[§](#impl-Hash-for-!)

1.60.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143802 "Tracking issue for const_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/ops/bit.rs.html#76)[§](#impl-Not-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2106)[§](#impl-Ord-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2084)[§](#impl-PartialEq-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2086)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2097)[§](#impl-PartialOrd-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2099)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.61.0 · [Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#2587-2591)[§](#impl-Termination-for-!)

[Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#2588-2590)[§](#method.report)

Is called to get the representation of the value as status code. This status code is returned to the operating system.

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#487)[§](#impl-Copy-for-!)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2093)[§](#impl-Eq-for-!)

[§](#impl-Freeze-for-!)

[§](#impl-RefUnwindSafe-for-!)

[§](#impl-Send-for-!)

[§](#impl-Sync-for-!)

[§](#impl-Unpin-for-!)

[§](#impl-UnsafeUnpin-for-!)

[§](#impl-UnwindSafe-for-!)