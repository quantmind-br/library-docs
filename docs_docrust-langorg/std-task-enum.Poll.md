---
title: Poll in std::task - Rust
url: https://doc.rust-lang.org/std/task/enum.Poll.html
source: crawler
fetched_at: 2026-05-06T21:31:45.4910883-03:00
rendered_js: false
word_count: 700
summary: The Poll enum indicates whether a value is immediately available or if a task must wait for further progress in asynchronous Rust programming.
tags:
    - rust
    - asynchronous
    - future
    - poll
    - concurrency
    - task-scheduling
category: reference
---

## Enum Poll

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#14)

```rust
pub enum Poll<T> {
    Ready(T),
    Pending,
}
```

Expand description

Indicates whether a value is available or if the current task has been scheduled to receive a wakeup instead.

This is returned by [`Future::poll`](https://doc.rust-lang.org/std/future/trait.Future.html#tymethod.poll "method std::future::Future::poll").

[§](#variant.Ready)1.36.0

Represents that a value is immediately ready.

[§](#variant.Pending)1.36.0

Represents that a value is not ready yet.

When a function returns `Pending`, the function *must* also ensure that the current task is scheduled to be awoken when progress can be made.

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#30)[§](#impl-Poll%3CT%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#49-51)

Maps a `Poll<T>` to `Poll<U>` by applying a function to a contained value.

##### [§](#examples)Examples

Converts a `Poll<String>` into a `Poll<usize>`, consuming the original:

```rust
let poll_some_string = Poll::Ready(String::from("Hello, World!"));
// `Poll::map` takes self *by value*, consuming `poll_some_string`
let poll_some_len = poll_some_string.map(|s| s.len());

assert_eq!(poll_some_len, Poll::Ready(13));
```

1.36.0 (const: 1.49.0) · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#74)

Returns `true` if the poll is a [`Poll::Ready`](https://doc.rust-lang.org/std/task/enum.Poll.html#variant.Ready "variant std::task::Poll::Ready") value.

##### [§](#examples-1)Examples

```rust
let x: Poll<u32> = Poll::Ready(2);
assert_eq!(x.is_ready(), true);

let x: Poll<u32> = Poll::Pending;
assert_eq!(x.is_ready(), false);
```

1.36.0 (const: 1.49.0) · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#95)

Returns `true` if the poll is a [`Pending`](https://doc.rust-lang.org/std/task/enum.Poll.html#variant.Pending "variant std::task::Poll::Pending") value.

##### [§](#examples-2)Examples

```rust
let x: Poll<u32> = Poll::Ready(2);
assert_eq!(x.is_pending(), false);

let x: Poll<u32> = Poll::Pending;
assert_eq!(x.is_pending(), true);
```

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#100)[§](#impl-Poll%3CResult%3CT,+E%3E%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#117-119)

Maps a `Poll<Result<T, E>>` to `Poll<Result<U, E>>` by applying a function to a contained `Poll::Ready(Ok)` value, leaving all other variants untouched.

This function can be used to compose the results of two functions.

##### [§](#examples-3)Examples

```rust
let res: Poll<Result<u8, _>> = Poll::Ready("12".parse());
let squared = res.map_ok(|n| n * n);
assert_eq!(squared, Poll::Ready(Ok(144)));
```

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#145-147)

Maps a `Poll::Ready<Result<T, E>>` to `Poll::Ready<Result<T, U>>` by applying a function to a contained `Poll::Ready(Err)` value, leaving all other variants untouched.

This function can be used to pass through a successful result while handling an error.

##### [§](#examples-4)Examples

```rust
let res: Poll<Result<u8, _>> = Poll::Ready("oops".parse());
let res = res.map_err(|_| 0_u8);
assert_eq!(res, Poll::Ready(Err(0)));
```

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#157)[§](#impl-Poll%3COption%3CResult%3CT,+E%3E%3E%3E)

1.51.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#174-176)

Maps a `Poll<Option<Result<T, E>>>` to `Poll<Option<Result<U, E>>>` by applying a function to a contained `Poll::Ready(Some(Ok))` value, leaving all other variants untouched.

This function can be used to compose the results of two functions.

##### [§](#examples-5)Examples

```rust
let res: Poll<Option<Result<u8, _>>> = Poll::Ready(Some("12".parse()));
let squared = res.map_ok(|n| n * n);
assert_eq!(squared, Poll::Ready(Some(Ok(144))));
```

1.51.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#204-206)

Maps a `Poll::Ready<Option<Result<T, E>>>` to `Poll::Ready<Option<Result<T, F>>>` by applying a function to a contained `Poll::Ready(Some(Err))` value, leaving all other variants untouched.

This function can be used to pass through a successful result while handling an error.

##### [§](#examples-6)Examples

```rust
let res: Poll<Option<Result<u8, _>>> = Poll::Ready(Some("oops".parse()));
let res = res.map_err(|_| 0_u8);
assert_eq!(res, Poll::Ready(Some(Err(0))));
```

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-Clone-for-Poll%3CT%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-Debug-for-Poll%3CT%3E)

1.36.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143773 "Tracking issue for const_convert")) · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#219)[§](#impl-From%3CT%3E-for-Poll%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#228)[§](#method.from)

Moves the value into a [`Poll::Ready`](https://doc.rust-lang.org/std/task/enum.Poll.html#variant.Ready "variant std::task::Poll::Ready") to make a `Poll<T>`.

##### [§](#example)Example

```rust
assert_eq!(Poll::from(true), Poll::Ready(true));
```

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#285-286)[§](#impl-FromResidual%3CResult%3CInfallible,+E%3E%3E-for-Poll%3COption%3CResult%3CT,+F%3E%3E%3E)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#289)[§](#method.from_residual-1)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from a compatible `Residual` type. [Read more](https://doc.rust-lang.org/std/ops/trait.FromResidual.html#tymethod.from_residual)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#254)[§](#impl-FromResidual%3CResult%3CInfallible,+E%3E%3E-for-Poll%3CResult%3CT,+F%3E%3E)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#256)[§](#method.from_residual)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from a compatible `Residual` type. [Read more](https://doc.rust-lang.org/std/ops/trait.FromResidual.html#tymethod.from_residual)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-Hash-for-Poll%3CT%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-Ord-for-Poll%3CT%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-PartialEq-for-Poll%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-PartialOrd-for-Poll%3CT%3E)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#264)[§](#impl-Try-for-Poll%3COption%3CResult%3CT,+E%3E%3E%3E)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#265)[§](#associatedtype.Output-1)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

The type of the value produced by `?` when *not* short-circuiting.

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#266)[§](#associatedtype.Residual-1)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#269)[§](#method.from_output-1)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from its `Output` type. [Read more](https://doc.rust-lang.org/std/ops/trait.Try.html#tymethod.from_output)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#274)[§](#method.branch-1)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Used in `?` to decide whether the operator should produce a value (because this returned [`ControlFlow::Continue`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Continue "variant std::ops::ControlFlow::Continue")) or propagate a value back to the caller (because this returned [`ControlFlow::Break`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Break "variant std::ops::ControlFlow::Break")). [Read more](https://doc.rust-lang.org/std/ops/trait.Try.html#tymethod.branch)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#234)[§](#impl-Try-for-Poll%3CResult%3CT,+E%3E%3E)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#235)[§](#associatedtype.Output)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

The type of the value produced by `?` when *not* short-circuiting.

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#236)[§](#associatedtype.Residual)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#239)[§](#method.from_output)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from its `Output` type. [Read more](https://doc.rust-lang.org/std/ops/trait.Try.html#tymethod.from_output)

[Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#244)[§](#method.branch)

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Used in `?` to decide whether the operator should produce a value (because this returned [`ControlFlow::Continue`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Continue "variant std::ops::ControlFlow::Continue")) or propagate a value back to the caller (because this returned [`ControlFlow::Break`](https://doc.rust-lang.org/std/ops/enum.ControlFlow.html#variant.Break "variant std::ops::ControlFlow::Break")). [Read more](https://doc.rust-lang.org/std/ops/trait.Try.html#tymethod.branch)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-Copy-for-Poll%3CT%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-Eq-for-Poll%3CT%3E)

1.36.0 · [Source](https://doc.rust-lang.org/src/core/task/poll.rs.html#11)[§](#impl-StructuralPartialEq-for-Poll%3CT%3E)