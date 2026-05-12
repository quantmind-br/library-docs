---
title: Option in std::option - Rust
url: https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_or_else
source: crawler
fetched_at: 2026-05-06T21:22:00.132159852-03:00
rendered_js: false
word_count: 2876
summary: This document provides reference documentation for the Rust 'Option' enum, detailing its variants and the various methods available for inspecting, transforming, and extracting values from it.
tags:
    - rust
    - option
    - enum
    - standard-library
    - api-reference
    - functional-programming
category: reference
---

## Enum Option

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#600)

```rust
pub enum Option<T> {
    None,
    Some(T),
}
```

Expand description

[§](#variant.None)1.0.0

No value.

[§](#variant.Some)1.0.0

Some value of type `T`.

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#615)[§](#impl-Option%3CT%3E)

1.0.0 (const: 1.48.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#635)

Returns `true` if the option is a [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value.

##### [§](#examples)Examples

```rust
let x: Option<u32> = Some(2);
assert_eq!(x.is_some(), true);

let x: Option<u32> = None;
assert_eq!(x.is_some(), false);
```

1.70.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#661)

Returns `true` if the option is a [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") and the value inside of it matches a predicate.

##### [§](#examples-1)Examples

```rust
let x: Option<u32> = Some(2);
assert_eq!(x.is_some_and(|x| x > 1), true);

let x: Option<u32> = Some(0);
assert_eq!(x.is_some_and(|x| x > 1), false);

let x: Option<u32> = None;
assert_eq!(x.is_some_and(|x| x > 1), false);

let x: Option<String> = Some("ownership".to_string());
assert_eq!(x.as_ref().is_some_and(|x| x.len() > 1), true);
println!("still alive {:?}", x);
```

1.0.0 (const: 1.48.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#684)

Returns `true` if the option is a [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") value.

##### [§](#examples-2)Examples

```rust
let x: Option<u32> = Some(2);
assert_eq!(x.is_none(), false);

let x: Option<u32> = None;
assert_eq!(x.is_none(), true);
```

1.82.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#710)

Returns `true` if the option is a [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") or the value inside of it matches a predicate.

##### [§](#examples-3)Examples

```rust
let x: Option<u32> = Some(2);
assert_eq!(x.is_none_or(|x| x > 1), true);

let x: Option<u32> = Some(0);
assert_eq!(x.is_none_or(|x| x > 1), false);

let x: Option<u32> = None;
assert_eq!(x.is_none_or(|x| x > 1), true);

let x: Option<String> = Some("ownership".to_string());
assert_eq!(x.as_ref().is_none_or(|x| x.len() > 1), true);
println!("still alive {:?}", x);
```

1.0.0 (const: 1.48.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#744)

Converts from `&Option<T>` to `Option<&T>`.

##### [§](#examples-4)Examples

Calculates the length of an `Option<String>` as an `Option<usize>` without moving the [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "String"). The [`map`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.map "method std::option::Option::map") method takes the `self` argument by value, consuming the original, so this technique uses `as_ref` to first take an `Option` to a reference to the value inside the original.

```rust
let text: Option<String> = Some("Hello, world!".to_string());
// First, cast `Option<String>` to `Option<&String>` with `as_ref`,
// then consume *that* with `map`, leaving `text` on the stack.
let text_length: Option<usize> = text.as_ref().map(|s| s.len());
println!("still can print text: {text:?}");
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#766)

Converts from `&mut Option<T>` to `Option<&mut T>`.

##### [§](#examples-5)Examples

```rust
let mut x = Some(2);
match x.as_mut() {
    Some(v) => *v = 42,
    None => {},
}
assert_eq!(x, Some(42));
```

1.33.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#780)

Converts from `Pin<&Option<T>>` to `Option<Pin<&T>>`.

1.33.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#797)

Converts from `Pin<&mut Option<T>>` to `Option<Pin<&mut T>>`.

1.75.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#844)

Returns a slice of the contained value, if any. If this is `None`, an empty slice is returned. This can be useful to have a single type of iterator over an `Option` or slice.

Note: Should you have an `Option<&T>` and wish to get a slice of `T`, you can unpack it via `opt.map_or(&[], std::slice::from_ref)`.

##### [§](#examples-6)Examples

```rust
assert_eq!(
    [Some(1234).as_slice(), None.as_slice()],
    [&[1234][..], &[][..]],
);
```

The inverse of this function is (discounting borrowing) [`[_]::first`](https://doc.rust-lang.org/stable/std/primitive.slice.html#method.first "method slice::first"):

```rust
for i in [Some(1234_u16), None] {
    assert_eq!(i.as_ref(), i.as_slice().first());
}
```

1.75.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#899)

Returns a mutable slice of the contained value, if any. If this is `None`, an empty slice is returned. This can be useful to have a single type of iterator over an `Option` or slice.

Note: Should you have an `Option<&mut T>` instead of a `&mut Option<T>`, which this method takes, you can obtain a mutable slice via `opt.map_or(&mut [], std::slice::from_mut)`.

##### [§](#examples-7)Examples

```rust
assert_eq!(
    [Some(1234).as_mut_slice(), None.as_mut_slice()],
    [&mut [1234][..], &mut [][..]],
);
```

The result is a mutable slice of zero or one items that points into our original `Option`:

```rust
let mut x = Some(1234);
x.as_mut_slice()[0] += 1;
assert_eq!(x, Some(1235));
```

The inverse of this method (discounting borrowing) is [`[_]::first_mut`](https://doc.rust-lang.org/stable/std/primitive.slice.html#method.first_mut "method slice::first_mut"):

```rust
assert_eq!(Some(123).as_mut_slice().first_mut(), Some(&mut 123))
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#968)

Returns the contained [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value, consuming the `self` value.

##### [§](#panics)Panics

Panics if the value is a [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") with a custom panic message provided by `msg`.

##### [§](#examples-8)Examples

```rust
let x = Some("value");
assert_eq!(x.expect("fruits are healthy"), "value");
```

[ⓘ](# "This example panics")

```rust
let x: Option<&str> = None;
x.expect("fruits are healthy"); // panics with `fruits are healthy`
```

##### [§](#recommended-message-style)Recommended Message Style

We recommend that `expect` messages are used to describe the reason you *expect* the `Option` should be `Some`.

[ⓘ](# "This example panics")

```rust
let item = slice.get(0)
    .expect("slice should not be empty");
```

**Hint**: If you’re having trouble remembering how to phrase expect error messages remember to focus on the word “should” as in “env variable should be set by blah” or “the given binary should be available and executable by the current user”.

For more detail on expect message styles and the reasoning behind our recommendation please refer to the section on [“Common Message Styles”](https://doc.rust-lang.org/stable/std/error/index.html#common-message-styles) in the [`std::error`](https://doc.rust-lang.org/stable/std/error/index.html) module docs.

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1013)

Returns the contained [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value, consuming the `self` value.

Because this function may panic, its use is generally discouraged. Panics are meant for unrecoverable errors, and [may abort the entire program](https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic.html).

Instead, prefer to use pattern matching and handle the [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") case explicitly, or call [`unwrap_or`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_or "method std::option::Option::unwrap_or"), [`unwrap_or_else`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_or_else "method std::option::Option::unwrap_or_else"), or [`unwrap_or_default`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_or_default "method std::option::Option::unwrap_or_default"). In functions returning `Option`, you can use [the `?` (try) operator](https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#where-the--operator-can-be-used).

##### [§](#panics-1)Panics

Panics if the self value equals [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None").

##### [§](#examples-9)Examples

```rust
let x = Some("air");
assert_eq!(x.unwrap(), "air");
```

[ⓘ](# "This example panics")

```rust
let x: Option<&str> = None;
assert_eq!(x.unwrap(), "air"); // fails
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1038-1040)

Returns the contained [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value or a provided default.

Arguments passed to `unwrap_or` are eagerly evaluated; if you are passing the result of a function call, it is recommended to use [`unwrap_or_else`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.unwrap_or_else "method std::option::Option::unwrap_or_else"), which is lazily evaluated.

##### [§](#examples-10)Examples

```rust
assert_eq!(Some("car").unwrap_or("bike"), "car");
assert_eq!(None.unwrap_or("bike"), "bike");
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1061-1063)

Returns the contained [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value or computes it from a closure.

##### [§](#examples-11)Examples

```rust
let k = 10;
assert_eq!(Some(4).unwrap_or_else(|| 2 * k), 4);
assert_eq!(None.unwrap_or_else(|| 2 * k), 20);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1093-1095)

Returns the contained [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value or a default.

Consumes the `self` argument then, if [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some"), returns the contained value, otherwise if [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), returns the [default value](https://doc.rust-lang.org/stable/std/default/trait.Default.html#tymethod.default "associated function std::default::Default::default") for that type.

##### [§](#examples-12)Examples

```rust
let x: Option<u32> = None;
let y: Option<u32> = Some(12);

assert_eq!(x.unwrap_or_default(), 0);
assert_eq!(y.unwrap_or_default(), 12);
```

1.58.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1128)

Returns the contained [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") value, consuming the `self` value, without checking that the value is not [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None").

##### [§](#safety)Safety

Calling this method on [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is [*undefined behavior*](https://doc.rust-lang.org/reference/behavior-considered-undefined.html).

##### [§](#examples-13)Examples

```rust
let x = Some("air");
assert_eq!(unsafe { x.unwrap_unchecked() }, "air");
```

```rust
let x: Option<&str> = None;
assert_eq!(unsafe { x.unwrap_unchecked() }, "air"); // Undefined behavior!
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1160-1162)

Maps an `Option<T>` to `Option<U>` by applying a function to a contained value (if `Some`) or returns `None` (if `None`).

##### [§](#examples-14)Examples

Calculates the length of an `Option<String>` as an `Option<usize>`, consuming the original:

```rust
let maybe_some_string = Some(String::from("Hello, World!"));
// `Option::map` takes self *by value*, consuming `maybe_some_string`
let maybe_some_len = maybe_some_string.map(|s| s.len());
assert_eq!(maybe_some_len, Some(13));

let x: Option<&str> = None;
assert_eq!(x.map(|s| s.len()), None);
```

1.76.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1191-1193)

Calls a function with a reference to the contained value if [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some").

Returns the original option.

##### [§](#examples-15)Examples

```rust
let list = vec![1, 2, 3];

// prints "got: 2"
let x = list
    .get(1)
    .inspect(|x| println!("got: {x}"))
    .expect("list should be long enough");

// prints nothing
list.get(5).inspect(|x| println!("got: {x}"));
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1224-1227)

Returns the provided default result (if none), or applies a function to the contained value (if any).

Arguments passed to `map_or` are eagerly evaluated; if you are passing the result of a function call, it is recommended to use [`map_or_else`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.map_or_else "method std::option::Option::map_or_else"), which is lazily evaluated.

##### [§](#examples-16)Examples

```rust
let x = Some("foo");
assert_eq!(x.map_or(42, |v| v.len()), 3);

let x: Option<&str> = None;
assert_eq!(x.map_or(42, |v| v.len()), 42);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1271-1274)

Computes a default function result (if none), or applies a different function to the contained value (if any).

##### [§](#basic-examples)Basic examples

```rust
let k = 21;

let x = Some("foo");
assert_eq!(x.map_or_else(|| 2 * k, |v| v.len()), 3);

let x: Option<&str> = None;
assert_eq!(x.map_or_else(|| 2 * k, |v| v.len()), 42);
```

##### [§](#handling-a-result-based-fallback)Handling a Result-based fallback

A somewhat common occurrence when dealing with optional values in combination with [`Result<T, E>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") is the case where one wants to invoke a fallible fallback if the option is not present. This example parses a command line argument (if present), or the contents of a file to an integer. However, unlike accessing the command line argument, reading the file is fallible, so it must be wrapped with `Ok`.

```rust
let v: u64 = std::env::args()
   .nth(1)
   .map_or_else(|| std::fs::read_to_string("/etc/someconfig.conf"), Ok)?
   .parse()?;
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1302-1305)

🔬This is a nightly-only experimental API. (`result_option_map_or_default` [#138099](https://github.com/rust-lang/rust/issues/138099))

Maps an `Option<T>` to a `U` by applying function `f` to the contained value if the option is [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some"), otherwise if [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), returns the [default value](https://doc.rust-lang.org/stable/std/default/trait.Default.html#tymethod.default "associated function std::default::Default::default") for the type `U`.

##### [§](#examples-17)Examples

```rust
#![feature(result_option_map_or_default)]

let x: Option<&str> = Some("hi");
let y: Option<&str> = None;

assert_eq!(x.map_or_default(|x| x.len()), 2);
assert_eq!(y.map_or_default(|y| y.len()), 0);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1337)

Transforms the `Option<T>` into a [`Result<T, E>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result"), mapping [`Some(v)`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") to [`Ok(v)`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") and [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") to [`Err(err)`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err").

Arguments passed to `ok_or` are eagerly evaluated; if you are passing the result of a function call, it is recommended to use [`ok_or_else`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.ok_or_else "method std::option::Option::ok_or_else"), which is lazily evaluated.

##### [§](#examples-18)Examples

```rust
let x = Some("foo");
assert_eq!(x.ok_or(0), Ok("foo"));

let x: Option<&str> = None;
assert_eq!(x.ok_or(0), Err(0));
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1363-1365)

Transforms the `Option<T>` into a [`Result<T, E>`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result"), mapping [`Some(v)`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") to [`Ok(v)`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") and [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") to [`Err(err())`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err").

##### [§](#examples-19)Examples

```rust
let x = Some("foo");
assert_eq!(x.ok_or_else(|| 0), Ok("foo"));

let x: Option<&str> = None;
assert_eq!(x.ok_or_else(|| 0), Err(0));
```

1.40.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1390-1392)

Converts from `Option<T>` (or `&Option<T>`) to `Option<&T::Target>`.

Leaves the original Option in-place, creating a new one with a reference to the original one, additionally coercing the contents via [`Deref`](https://doc.rust-lang.org/stable/std/ops/trait.Deref.html "trait std::ops::Deref").

##### [§](#examples-20)Examples

```rust
let x: Option<String> = Some("hey".to_owned());
assert_eq!(x.as_deref(), Some("hey"));

let x: Option<String> = None;
assert_eq!(x.as_deref(), None);
```

1.40.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1414-1416)

Converts from `Option<T>` (or `&mut Option<T>`) to `Option<&mut T::Target>`.

Leaves the original `Option` in-place, creating a new one containing a mutable reference to the inner type’s [`Deref::Target`](https://doc.rust-lang.org/stable/std/ops/trait.Deref.html#associatedtype.Target "associated type std::ops::Deref::Target") type.

##### [§](#examples-21)Examples

```rust
let mut x: Option<String> = Some("hey".to_owned());
assert_eq!(x.as_deref_mut().map(|x| {
    x.make_ascii_uppercase();
    x
}), Some("HEY".to_owned().as_mut_str()));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1438)

Returns an iterator over the possibly contained value.

##### [§](#examples-22)Examples

```rust
let x = Some(4);
assert_eq!(x.iter().next(), Some(&4));

let x: Option<u32> = None;
assert_eq!(x.iter().next(), None);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1459)

Returns a mutable iterator over the possibly contained value.

##### [§](#examples-23)Examples

```rust
let mut x = Some(4);
match x.iter_mut().next() {
    Some(v) => *v = 42,
    None => {},
}
assert_eq!(x, Some(42));

let mut x: Option<u32> = None;
assert_eq!(x.iter_mut().next(), None);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1497-1500)

Returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the option is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), otherwise returns `optb`.

Arguments passed to `and` are eagerly evaluated; if you are passing the result of a function call, it is recommended to use [`and_then`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.and_then "method std::option::Option::and_then"), which is lazily evaluated.

##### [§](#examples-24)Examples

```rust
let x = Some(2);
let y: Option<&str> = None;
assert_eq!(x.and(y), None);

let x: Option<u32> = None;
let y = Some("foo");
assert_eq!(x.and(y), None);

let x = Some(2);
let y = Some("foo");
assert_eq!(x.and(y), Some("foo"));

let x: Option<u32> = None;
let y: Option<&str> = None;
assert_eq!(x.and(y), None);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1541-1543)

Returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the option is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), otherwise calls `f` with the wrapped value and returns the result.

Some languages call this operation flatmap.

##### [§](#examples-25)Examples

```rust
fn sq_then_to_string(x: u32) -> Option<String> {
    x.checked_mul(x).map(|sq| sq.to_string())
}

assert_eq!(Some(2).and_then(sq_then_to_string), Some(4.to_string()));
assert_eq!(Some(1_000_000).and_then(sq_then_to_string), None); // overflowed!
assert_eq!(None.and_then(sq_then_to_string), None);
```

Often used to chain fallible operations that may return [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None").

```rust
let arr_2d = [["A0", "A1"], ["B0", "B1"]];

let item_0_1 = arr_2d.get(0).and_then(|row| row.get(1));
assert_eq!(item_0_1, Some(&"A1"));

let item_2_0 = arr_2d.get(2).and_then(|row| row.get(0));
assert_eq!(item_2_0, None);
```

1.27.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1578-1581)

Returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if the option is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), otherwise calls `predicate` with the wrapped value and returns:

- [`Some(t)`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") if `predicate` returns `true` (where `t` is the wrapped value), and
- [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") if `predicate` returns `false`.

This function works similar to [`Iterator::filter()`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html#method.filter "method std::iter::Iterator::filter"). You can imagine the `Option<T>` being an iterator over one or zero elements. `filter()` lets you decide which elements to keep.

##### [§](#examples-26)Examples

```rust
fn is_even(n: &i32) -> bool {
    n % 2 == 0
}

assert_eq!(None.filter(is_even), None);
assert_eq!(Some(3).filter(is_even), None);
assert_eq!(Some(4).filter(is_even), Some(4));
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1621-1623)

Returns the option if it contains a value, otherwise returns `optb`.

Arguments passed to `or` are eagerly evaluated; if you are passing the result of a function call, it is recommended to use [`or_else`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.or_else "method std::option::Option::or_else"), which is lazily evaluated.

##### [§](#examples-27)Examples

```rust
let x = Some(2);
let y = None;
assert_eq!(x.or(y), Some(2));

let x = None;
let y = Some(100);
assert_eq!(x.or(y), Some(100));

let x = Some(2);
let y = Some(100);
assert_eq!(x.or(y), Some(2));

let x: Option<u32> = None;
let y = None;
assert_eq!(x.or(y), None);
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1647-1652)

Returns the option if it contains a value, otherwise calls `f` and returns the result.

##### [§](#examples-28)Examples

```rust
fn nobody() -> Option<&'static str> { None }
fn vikings() -> Option<&'static str> { Some("vikings") }

assert_eq!(Some("barbarians").or_else(vikings), Some("barbarians"));
assert_eq!(None.or_else(vikings), Some("vikings"));
assert_eq!(None.or_else(nobody), None);
```

1.37.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1684-1686)

Returns [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") if exactly one of `self`, `optb` is [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some"), otherwise returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None").

##### [§](#examples-29)Examples

```rust
let x = Some(2);
let y: Option<u32> = None;
assert_eq!(x.xor(y), Some(2));

let x: Option<u32> = None;
let y = Some(2);
assert_eq!(x.xor(y), Some(2));

let x = Some(2);
let y = Some(2);
assert_eq!(x.xor(y), None);

let x: Option<u32> = None;
let y: Option<u32> = None;
assert_eq!(x.xor(y), None);
```

1.53.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1722-1724)

Inserts `value` into the option, then returns a mutable reference to it.

If the option already contains a value, the old value is dropped.

See also [`Option::get_or_insert`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.get_or_insert "method std::option::Option::get_or_insert"), which doesn’t update the value if the option already contains [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some").

##### [§](#example)Example

```rust
let mut opt = None;
let val = opt.insert(1);
assert_eq!(*val, 1);
assert_eq!(opt.unwrap(), 1);
let val = opt.insert(2);
assert_eq!(*val, 2);
*val = 3;
assert_eq!(opt.unwrap(), 3);
```

1.20.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1754)

Inserts `value` into the option if it is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then returns a mutable reference to the contained value.

See also [`Option::insert`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.insert "method std::option::Option::insert"), which updates the value even if the option already contains [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some").

##### [§](#examples-30)Examples

```rust
let mut x = None;

{
    let y: &mut u32 = x.get_or_insert(5);
    assert_eq!(y, &5);

    *y = 7;
}

assert_eq!(x, Some(7));
```

1.83.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1778-1780)

Inserts the default value into the option if it is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then returns a mutable reference to the contained value.

##### [§](#examples-31)Examples

```rust
let mut x = None;

{
    let y: &mut u32 = x.get_or_insert_default();
    assert_eq!(y, &0);

    *y = 7;
}

assert_eq!(x, Some(7));
```

1.20.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1805-1808)

Inserts a value computed from `f` into the option if it is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), then returns a mutable reference to the contained value.

##### [§](#examples-32)Examples

```rust
let mut x = None;

{
    let y: &mut u32 = x.get_or_insert_with(|| 5);
    assert_eq!(y, &5);

    *y = 7;
}

assert_eq!(x, Some(7));
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1845-1851)

🔬This is a nightly-only experimental API. (`option_get_or_try_insert_with` [#143648](https://github.com/rust-lang/rust/issues/143648))

If the option is `None`, calls the closure and inserts its output if successful.

If the closure returns a residual value such as `Err` or `None`, that residual value is returned and nothing is inserted.

If the option is `Some`, nothing is inserted.

Unless a residual is returned, a mutable reference to the value of the option will be output.

##### [§](#examples-33)Examples

```rust
#![feature(option_get_or_try_insert_with)]
let mut o1: Option<u32> = None;
let mut o2: Option<u8> = None;

let number = "12345";

assert_eq!(o1.get_or_try_insert_with(|| number.parse()).copied(), Ok(12345));
assert!(o2.get_or_try_insert_with(|| number.parse()).is_err());
assert_eq!(o1, Some(12345));
assert_eq!(o2, None);
```

1.0.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1884)

Takes the value out of the option, leaving a [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") in its place.

##### [§](#examples-34)Examples

```rust
let mut x = Some(2);
let y = x.take();
assert_eq!(x, None);
assert_eq!(y, Some(2));

let mut x: Option<u32> = None;
let y = x.take();
assert_eq!(x, None);
assert_eq!(y, None);
```

1.80.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1916-1918)

Takes the value out of the option, but only if the predicate evaluates to `true` on a mutable reference to the value.

In other words, replaces `self` with `None` if the predicate returns `true`. This method operates similar to [`Option::take`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.take "method std::option::Option::take") but conditional.

##### [§](#examples-35)Examples

```rust
let mut x = Some(42);

let prev = x.take_if(|v| if *v == 42 {
    *v += 1;
    false
} else {
    false
});
assert_eq!(x, Some(43));
assert_eq!(prev, None);

let prev = x.take_if(|v| *v == 43);
assert_eq!(x, None);
assert_eq!(prev, Some(43));
```

1.31.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1943)

Replaces the actual value in the option by the value given in parameter, returning the old value if present, leaving a [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some") in its place without deinitializing either one.

##### [§](#examples-36)Examples

```rust
let mut x = Some(2);
let old = x.replace(5);
assert_eq!(x, Some(5));
assert_eq!(old, Some(2));

let mut x = None;
let old = x.replace(3);
assert_eq!(x, Some(3));
assert_eq!(old, None);
```

1.46.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143956 "Tracking issue for const_option_ops")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#1964-1967)

Zips `self` with another `Option`.

If `self` is `Some(s)` and `other` is `Some(o)`, this method returns `Some((s, o))`. Otherwise, `None` is returned.

##### [§](#examples-37)Examples

```rust
let x = Some(1);
let y = Some("hi");
let z = None::<u8>;

assert_eq!(x.zip(y), Some((1, "hi")));
assert_eq!(x.zip(z), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2005-2009)

🔬This is a nightly-only experimental API. (`option_zip` [#70086](https://github.com/rust-lang/rust/issues/70086))

Zips `self` and another `Option` with function `f`.

If `self` is `Some(s)` and `other` is `Some(o)`, this method returns `Some(f(s, o))`. Otherwise, `None` is returned.

##### [§](#examples-38)Examples

```rust
#![feature(option_zip)]

#[derive(Debug, PartialEq)]
struct Point {
    x: f64,
    y: f64,
}

impl Point {
    fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }
}

let x = Some(17.5);
let y = Some(42.7);

assert_eq!(x.zip_with(y, Point::new), Some(Point { x: 17.5, y: 42.7 }));
assert_eq!(x.zip_with(None, Point::new), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2039-2043)

🔬This is a nightly-only experimental API. (`option_reduce` [#144273](https://github.com/rust-lang/rust/issues/144273))

Reduces two options into one, using the provided function if both are `Some`.

If `self` is `Some(s)` and `other` is `Some(o)`, this method returns `Some(f(s, o))`. Otherwise, if only one of `self` and `other` is `Some`, that one is returned. If both `self` and `other` are `None`, `None` is returned.

##### [§](#examples-39)Examples

```rust
#![feature(option_reduce)]

let s12 = Some(12);
let s17 = Some(17);
let n = None;
let f = |a, b| a + b;

assert_eq!(s12.reduce(s17, f), Some(29));
assert_eq!(s12.reduce(n, f), Some(12));
assert_eq!(n.reduce(s17, f), Some(17));
assert_eq!(n.reduce(n, f), None);
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2054)[§](#impl-Option%3CT%3E-1)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2070-2072)

🔬This is a nightly-only experimental API. (`option_into_flat_iter` [#148441](https://github.com/rust-lang/rust/issues/148441))

Transforms an optional iterator into an iterator.

If `self` is `None`, the resulting iterator is empty. Otherwise, an iterator is made from the `Some` value and returned.

##### [§](#examples-40)Examples

```rust
#![feature(option_into_flat_iter)]

let o1 = Some([1, 2]);
let o2 = None::<&[usize]>;

assert_eq!(o1.into_flat_iter().collect::<Vec<_>>(), [1, 2]);
assert_eq!(o2.into_flat_iter().collect::<Vec<_>>(), Vec::<&usize>::new());
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2078)[§](#impl-Option%3C%28T,+U%29%3E)

1.66.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2095)

Unzips an option containing a tuple of two options.

If `self` is `Some((a, b))` this method returns `(Some(a), Some(b))`. Otherwise, `(None, None)` is returned.

##### [§](#examples-41)Examples

```rust
let x = Some((1, "hi"));
let y = None::<(u8, u32)>;

assert_eq!(x.unzip(), (Some(1), Some("hi")));
assert_eq!(y.unzip(), (None, None));
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2103)[§](#impl-Option%3C%26T%3E)

1.35.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2119-2121)

Maps an `Option<&T>` to an `Option<T>` by copying the contents of the option.

##### [§](#examples-42)Examples

```rust
let x = 12;
let opt_x = Some(&x);
assert_eq!(opt_x, Some(&12));
let copied = opt_x.copied();
assert_eq!(copied, Some(12));
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2145-2147)

Maps an `Option<&T>` to an `Option<T>` by cloning the contents of the option.

##### [§](#examples-43)Examples

```rust
let x = 12;
let opt_x = Some(&x);
assert_eq!(opt_x, Some(&12));
let cloned = opt_x.cloned();
assert_eq!(cloned, Some(12));
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2153)[§](#impl-Option%3C%26mut+T%3E)

1.35.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2169-2171)

Maps an `Option<&mut T>` to an `Option<T>` by copying the contents of the option.

##### [§](#examples-44)Examples

```rust
let mut x = 12;
let opt_x = Some(&mut x);
assert_eq!(opt_x, Some(&mut 12));
let copied = opt_x.copied();
assert_eq!(copied, Some(12));
```

1.26.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2193-2195)

Maps an `Option<&mut T>` to an `Option<T>` by cloning the contents of the option.

##### [§](#examples-45)Examples

```rust
let mut x = 12;
let opt_x = Some(&mut x);
assert_eq!(opt_x, Some(&mut 12));
let cloned = opt_x.cloned();
assert_eq!(cloned, Some(12));
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2201)[§](#impl-Option%3CResult%3CT,+E%3E%3E)

1.33.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2222)

Transposes an `Option` of a [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") into a [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") of an `Option`.

`Some(Ok(_))` is mapped to `Ok(Some(_))`, `Some(Err(_))` is mapped to `Err(_)`, and [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") will be mapped to `Ok(None)`.

##### [§](#examples-46)Examples

```rust
#[derive(Debug, Eq, PartialEq)]
struct SomeErr;

let x: Option<Result<i32, SomeErr>> = Some(Ok(5));
let y: Result<Option<i32>, SomeErr> = Ok(Some(5));
assert_eq!(x.transpose(), y);
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2802)[§](#impl-Option%3COption%3CT%3E%3E)

1.40.0 (const: 1.83.0) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2831)

Converts from `Option<Option<T>>` to `Option<T>`.

##### [§](#examples-47)Examples

Basic usage:

```rust
let x: Option<Option<u32>> = Some(Some(6));
assert_eq!(Some(6), x.flatten());

let x: Option<Option<u32>> = Some(None);
assert_eq!(None, x.flatten());

let x: Option<Option<u32>> = None;
assert_eq!(None, x.flatten());
```

Flattening only removes one level of nesting at a time:

```rust
let x: Option<Option<Option<u32>>> = Some(Some(Some(6)));
assert_eq!(Some(Some(6)), x.flatten());
assert_eq!(Some(6), x.flatten().flatten());
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2840)[§](#impl-Option%3C%26Option%3CT%3E%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2861)

🔬This is a nightly-only experimental API. (`option_reference_flattening` [#149221](https://github.com/rust-lang/rust/issues/149221))

Converts from `Option<&Option<T>>` to `Option<&T>`.

##### [§](#examples-48)Examples

Basic usage:

```rust
#![feature(option_reference_flattening)]

let x: Option<&Option<u32>> = Some(&Some(6));
assert_eq!(Some(&6), x.flatten_ref());

let x: Option<&Option<u32>> = Some(&None);
assert_eq!(None, x.flatten_ref());

let x: Option<&Option<u32>> = None;
assert_eq!(None, x.flatten_ref());
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2869)[§](#impl-Option%3C%26mut+Option%3CT%3E%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2892)

🔬This is a nightly-only experimental API. (`option_reference_flattening` [#149221](https://github.com/rust-lang/rust/issues/149221))

Converts from `Option<&mut Option<T>>` to `&Option<T>`.

##### [§](#examples-49)Examples

Basic usage:

```rust
#![feature(option_reference_flattening)]

let y = &mut Some(6);
let x: Option<&mut Option<u32>> = Some(y);
assert_eq!(Some(&6), x.flatten_ref());

let y: &mut Option<u32> = &mut None;
let x: Option<&mut Option<u32>> = Some(y);
assert_eq!(None, x.flatten_ref());

let x: Option<&mut Option<u32>> = None;
assert_eq!(None, x.flatten_ref());
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2921)

🔬This is a nightly-only experimental API. (`option_reference_flattening` [#149221](https://github.com/rust-lang/rust/issues/149221))

Converts from `Option<&mut Option<T>>` to `Option<&mut T>`.

##### [§](#examples-50)Examples

Basic usage:

```rust
#![feature(option_reference_flattening)]

let y: &mut Option<u32> = &mut Some(6);
let x: Option<&mut Option<u32>> = Some(y);
assert_eq!(Some(&mut 6), x.flatten_mut());

let y: &mut Option<u32> = &mut None;
let x: Option<&mut Option<u32>> = Some(y);
assert_eq!(None, x.flatten_mut());

let x: Option<&mut Option<u32>> = None;
assert_eq!(None, x.flatten_mut());
```

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/142757 "Tracking issue for const_clone")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2254-2258)[§](#impl-Clone-for-Option%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#594)[§](#impl-Debug-for-Option%3CT%3E)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2287)[§](#impl-Default-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2297)[§](#method.default)

Returns [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None").

##### [§](#examples-51)Examples

```rust
let opt: Option<u32> = Option::default();
assert!(opt.is_none());
```

1.30.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2366)[§](#impl-From%3C%26Option%3CT%3E%3E-for-Option%3C%26T%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2387)[§](#method.from-1)

Converts from `&Option<T>` to `Option<&T>`.

##### [§](#examples-53)Examples

Converts an `Option<String>` into an `Option<usize>`, preserving the original. The [`map`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#method.map "method std::option::Option::map") method takes the `self` argument by value, consuming the original, so this technique uses `from` to first take an [`Option`](https://doc.rust-lang.org/stable/std/option/enum.Option.html "enum std::option::Option") to a reference to the value inside the original.

```rust
let s: Option<String> = Some(String::from("Hello, Rustaceans!"));
let o: Option<usize> = Option::from(&s).map(|ss: &String| ss.len());

println!("Can still print s: {s:?}");

assert_eq!(o, Some(18));
```

1.30.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2394)[§](#impl-From%3C%26mut+Option%3CT%3E%3E-for-Option%3C%26mut+T%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2410)[§](#method.from-2)

Converts from `&mut Option<T>` to `Option<&mut T>`

##### [§](#examples-54)Examples

```rust
let mut s = Some(String::from("Hello"));
let o: Option<&mut String> = Option::from(&mut s);

match o {
    Some(t) => *t = String::from("Hello, Rustaceans!"),
    None => (),
}

assert_eq!(s, Some(String::from("Hello, Rustaceans!")));
```

1.12.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2349)[§](#impl-From%3CT%3E-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2359)[§](#method.from)

Moves `val` into a new [`Some`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.Some "variant std::option::Option::Some").

##### [§](#examples-52)Examples

```rust
let o: Option<u8> = Option::from(67);

assert_eq!(Some(67), o);
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2683)[§](#impl-FromIterator%3COption%3CA%3E%3E-for-Option%3CV%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2745)[§](#method.from_iter)

Takes each element in the [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator"): if it is [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), no further elements are taken, and the [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is returned. Should no [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") occur, a container of type `V` containing the values of each [`Option`](https://doc.rust-lang.org/stable/std/option/enum.Option.html "enum std::option::Option") is returned.

##### [§](#examples-58)Examples

Here is an example which increments every integer in a vector. We use the checked variant of `add` that returns `None` when the calculation would result in an overflow.

```rust
let items = vec![0_u16, 1, 2];

let res: Option<Vec<u16>> = items
    .iter()
    .map(|x| x.checked_add(1))
    .collect();

assert_eq!(res, Some(vec![1, 2, 3]));
```

As you can see, this will return the expected, valid items.

Here is another example that tries to subtract one from another list of integers, this time checking for underflow:

```rust
let items = vec![2_u16, 1, 0];

let res: Option<Vec<u16>> = items
    .iter()
    .map(|x| x.checked_sub(1))
    .collect();

assert_eq!(res, None);
```

Since the last element is zero, it would underflow. Thus, the resulting value is `None`.

Here is a variation on the previous example, showing that no further elements are taken from `iter` after the first `None`.

```rust
let items = vec![3_u16, 2, 1, 10];

let mut shared = 0;

let res: Option<Vec<u16>> = items
    .iter()
    .map(|x| { shared += x; x.checked_sub(2) })
    .collect();

assert_eq!(res, None);
assert_eq!(shared, 6);
```

Since the third element caused an underflow, no further elements were taken, so the final value of `shared` is 6 (= `3 + 2 + 1`), not 16.

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2777)[§](#impl-FromResidual%3COption%3CInfallible%3E%3E-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2779)[§](#method.from_residual)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from a compatible `Residual` type. [Read more](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html#tymethod.from_residual)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2789)[§](#impl-FromResidual%3CYeet%3C%28%29%3E%3E-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2791)[§](#method.from_residual-1)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from a compatible `Residual` type. [Read more](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html#tymethod.from_residual)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#594)[§](#impl-Hash-for-Option%3CT%3E)

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2328)[§](#impl-IntoIterator-for-%26Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2329)[§](#associatedtype.Item-1)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2330)[§](#associatedtype.IntoIter-1)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2332)[§](#method.into_iter-1)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2338)[§](#impl-IntoIterator-for-%26mut+Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2339)[§](#associatedtype.Item-2)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2340)[§](#associatedtype.IntoIter-2)

Which kind of iterator are we turning this into?

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2342)[§](#method.into_iter-2)

Creates an iterator from a value. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.IntoIterator.html#tymethod.into_iter)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/92476 "Tracking issue for const_iter")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2304)[§](#impl-IntoIterator-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2322)[§](#method.into_iter)

Returns a consuming iterator over the possibly contained value.

##### [§](#examples-55)Examples

```rust
let x = Some("string");
let v: Vec<&str> = x.into_iter().collect();
assert_eq!(v, ["string"]);

let x = None;
let v: Vec<&str> = x.into_iter().collect();
assert!(v.is_empty());
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2305)[§](#associatedtype.Item)

The type of the elements being iterated over.

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2306)[§](#associatedtype.IntoIter)

Which kind of iterator are we turning this into?

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2455)[§](#impl-Ord-for-Option%3CT%3E)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2422)[§](#impl-PartialEq-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2424)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2441)[§](#impl-PartialOrd-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2443)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.37.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#300-302)[§](#impl-Product%3COption%3CU%3E%3E-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#321-323)[§](#method.product)

Takes each element in the [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator"): if it is a [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), no further elements are taken, and the [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is returned. Should no [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") occur, the product of all elements is returned.

##### [§](#examples-57)Examples

This multiplies each number in a vector of strings, if a string could not be parsed the operation returns `None`:

```rust
let nums = vec!["5", "10", "1", "2"];
let total: Option<usize> = nums.iter().map(|w| w.parse::<usize>().ok()).product();
assert_eq!(total, Some(100));
let nums = vec!["5", "10", "one", "2"];
let total: Option<usize> = nums.iter().map(|w| w.parse::<usize>().ok()).product();
assert_eq!(total, None);
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2798)[§](#impl-Residual%3CT%3E-for-Option%3CInfallible%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2799)[§](#associatedtype.TryType)

🔬This is a nightly-only experimental API. (`try_trait_v2_residual` [#91285](https://github.com/rust-lang/rust/issues/91285))

The “return” type of this meta-function.

1.37.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#270-272)[§](#impl-Sum%3COption%3CU%3E%3E-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/accum.rs.html#291-293)[§](#method.sum)

Takes each element in the [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator"): if it is a [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None"), no further elements are taken, and the [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") is returned. Should no [`None`](https://doc.rust-lang.org/stable/std/option/enum.Option.html#variant.None "variant std::option::Option::None") occur, the sum of all elements is returned.

##### [§](#examples-56)Examples

This sums up the position of the character ‘a’ in a vector of strings, if a word did not have the character ‘a’ the operation returns `None`:

```rust
let words = vec!["have", "a", "great", "day"];
let total: Option<usize> = words.iter().map(|w| w.find('a')).sum();
assert_eq!(total, Some(5));
let words = vec!["have", "a", "good", "day"];
let total: Option<usize> = words.iter().map(|w| w.find('a')).sum();
assert_eq!(total, None);
```

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2755)[§](#impl-Try-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2756)[§](#associatedtype.Output)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

The type of the value produced by `?` when *not* short-circuiting.

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2757)[§](#associatedtype.Residual)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2760)[§](#method.from_output)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from its `Output` type. [Read more](https://doc.rust-lang.org/stable/std/ops/trait.Try.html#tymethod.from_output)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2765)[§](#method.branch)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Used in `?` to decide whether the operator should produce a value (because this returned [`ControlFlow::Continue`](https://doc.rust-lang.org/stable/std/ops/enum.ControlFlow.html#variant.Continue "variant std::ops::ControlFlow::Continue")) or propagate a value back to the caller (because this returned [`ControlFlow::Break`](https://doc.rust-lang.org/stable/std/ops/enum.ControlFlow.html#variant.Break "variant std::ops::ControlFlow::Break")). [Read more](https://doc.rust-lang.org/stable/std/ops/trait.Try.html#tymethod.branch)

[Source](https://doc.rust-lang.org/stable/src/core/cell.rs.html#806)[§](#impl-CloneFromCell-for-Option%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#594)[§](#impl-Copy-for-Option%3CT%3E)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/118304 "Tracking issue for derive_const")) · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#595)[§](#impl-Eq-for-Option%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2419)[§](#impl-StructuralPartialEq-for-Option%3CT%3E)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2278)[§](#impl-UseCloned-for-Option%3CT%3E)