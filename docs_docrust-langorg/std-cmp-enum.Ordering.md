---
title: Ordering in std::cmp - Rust
url: https://doc.rust-lang.org/std/cmp/enum.Ordering.html
source: crawler
fetched_at: 2026-05-06T21:23:41.367676925-03:00
rendered_js: false
word_count: 230
summary: This document describes the Rust Ordering enum, which represents the result of value comparisons, and details its associated methods for checking states, reversing, and chaining comparisons.
tags:
    - rust
    - enum
    - ordering
    - comparison
    - std-cmp
category: reference
---

## Enum Ordering

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#404)

```rust
#[repr(i8)]pub enum Ordering {
    Less = -1,
    Equal = 0,
    Greater = 1,
}
```

Expand description

An `Ordering` is the result of a comparison between two values.

## [§](#examples)Examples

```rust
use std::cmp::Ordering;

assert_eq!(1.cmp(&2), Ordering::Less);

assert_eq!(1.cmp(&1), Ordering::Equal);

assert_eq!(2.cmp(&1), Ordering::Greater);
```

[§](#variant.Less)1.0.0

An ordering where a compared value is less than another.

[§](#variant.Equal)1.0.0

An ordering where a compared value is equal to another.

[§](#variant.Greater)1.0.0

An ordering where a compared value is greater than another.

[Source](https://doc.rust-lang.org/src/core/cmp.rs.html#416)[§](#impl-Ordering)

1.53.0 (const: 1.53.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#438)

Returns `true` if the ordering is the `Equal` variant.

##### [§](#examples-1)Examples

```rust
use std::cmp::Ordering;

assert_eq!(Ordering::Less.is_eq(), false);
assert_eq!(Ordering::Equal.is_eq(), true);
assert_eq!(Ordering::Greater.is_eq(), false);
```

1.53.0 (const: 1.53.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#461)

Returns `true` if the ordering is not the `Equal` variant.

##### [§](#examples-2)Examples

```rust
use std::cmp::Ordering;

assert_eq!(Ordering::Less.is_ne(), true);
assert_eq!(Ordering::Equal.is_ne(), false);
assert_eq!(Ordering::Greater.is_ne(), true);
```

1.53.0 (const: 1.53.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#480)

Returns `true` if the ordering is the `Less` variant.

##### [§](#examples-3)Examples

```rust
use std::cmp::Ordering;

assert_eq!(Ordering::Less.is_lt(), true);
assert_eq!(Ordering::Equal.is_lt(), false);
assert_eq!(Ordering::Greater.is_lt(), false);
```

1.53.0 (const: 1.53.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#499)

Returns `true` if the ordering is the `Greater` variant.

##### [§](#examples-4)Examples

```rust
use std::cmp::Ordering;

assert_eq!(Ordering::Less.is_gt(), false);
assert_eq!(Ordering::Equal.is_gt(), false);
assert_eq!(Ordering::Greater.is_gt(), true);
```

1.53.0 (const: 1.53.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#518)

Returns `true` if the ordering is either the `Less` or `Equal` variant.

##### [§](#examples-5)Examples

```rust
use std::cmp::Ordering;

assert_eq!(Ordering::Less.is_le(), true);
assert_eq!(Ordering::Equal.is_le(), true);
assert_eq!(Ordering::Greater.is_le(), false);
```

1.53.0 (const: 1.53.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#537)

Returns `true` if the ordering is either the `Greater` or `Equal` variant.

##### [§](#examples-6)Examples

```rust
use std::cmp::Ordering;

assert_eq!(Ordering::Less.is_ge(), false);
assert_eq!(Ordering::Equal.is_ge(), true);
assert_eq!(Ordering::Greater.is_ge(), true);
```

1.0.0 (const: 1.48.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#574)

Reverses the `Ordering`.

- `Less` becomes `Greater`.
- `Greater` becomes `Less`.
- `Equal` becomes `Equal`.

##### [§](#examples-7)Examples

Basic behavior:

```rust
use std::cmp::Ordering;

assert_eq!(Ordering::Less.reverse(), Ordering::Greater);
assert_eq!(Ordering::Equal.reverse(), Ordering::Equal);
assert_eq!(Ordering::Greater.reverse(), Ordering::Less);
```

This method can be used to reverse a comparison:

```rust
let data: &mut [_] = &mut [2, 10, 5, 8];

// sort the array from largest to smallest.
data.sort_by(|a, b| a.cmp(b).reverse());

let b: &mut [_] = &mut [10, 8, 5, 2];
assert!(data == b);
```

1.17.0 (const: 1.48.0) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#613)

Chains two orderings.

Returns `self` when it’s not `Equal`. Otherwise returns `other`.

##### [§](#examples-8)Examples

```rust
use std::cmp::Ordering;

let result = Ordering::Equal.then(Ordering::Less);
assert_eq!(result, Ordering::Less);

let result = Ordering::Less.then(Ordering::Equal);
assert_eq!(result, Ordering::Less);

let result = Ordering::Less.then(Ordering::Greater);
assert_eq!(result, Ordering::Less);

let result = Ordering::Equal.then(Ordering::Equal);
assert_eq!(result, Ordering::Equal);

let x: (i64, i64, i64) = (1, 2, 7);
let y: (i64, i64, i64) = (1, 5, 3);
let result = x.0.cmp(&y.0).then(x.1.cmp(&y.1)).then(x.2.cmp(&y.2));

assert_eq!(result, Ordering::Less);
```

1.17.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#652-654)

Chains the ordering with the given function.

Returns `self` when it’s not `Equal`. Otherwise calls `f` and returns the result.

##### [§](#examples-9)Examples

```rust
use std::cmp::Ordering;

let result = Ordering::Equal.then_with(|| Ordering::Less);
assert_eq!(result, Ordering::Less);

let result = Ordering::Less.then_with(|| Ordering::Equal);
assert_eq!(result, Ordering::Less);

let result = Ordering::Less.then_with(|| Ordering::Greater);
assert_eq!(result, Ordering::Less);

let result = Ordering::Equal.then_with(|| Ordering::Equal);
assert_eq!(result, Ordering::Equal);

let x: (i64, i64, i64) = (1, 2, 7);
let y: (i64, i64, i64) = (1, 5, 3);
let result = x.0.cmp(&y.0).then_with(|| x.1.cmp(&y.1)).then_with(|| x.2.cmp(&y.2));

assert_eq!(result, Ordering::Less);
```

[§](#impl-Freeze-for-Ordering)

[§](#impl-RefUnwindSafe-for-Ordering)

[§](#impl-Send-for-Ordering)

[§](#impl-Sync-for-Ordering)

[§](#impl-Unpin-for-Ordering)

[§](#impl-UnsafeUnpin-for-Ordering)

[§](#impl-UnwindSafe-for-Ordering)