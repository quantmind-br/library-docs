---
title: unit - Rust
url: https://doc.rust-lang.org/stable/std/primitive.unit.html
source: crawler
fetched_at: 2026-05-06T21:25:59.536625016-03:00
rendered_js: false
word_count: 378
summary: This document describes the unit type '()' in Rust, which is used to represent the absence of a meaningful value, particularly as a default function return type.
tags:
    - rust
    - primitive-types
    - unit-type
    - language-features
    - type-system
category: reference
---

## Primitive Type unit

1.0.0

Expand description

The `()` type, also called “unit”.

The `()` type has exactly one value `()`, and is used when there is no other meaningful value that could be returned. `()` is most commonly seen implicitly: functions without a `-> ...` implicitly have return type `()`, that is, these are equivalent:

```rust
fn long() -> () {}

fn short() {}
```

The semicolon `;` can be used to discard the result of an expression at the end of a block, making the expression (and thus the block) evaluate to `()`. For example,

```rust
fn returns_i64() -> i64 {
    1i64
}
fn returns_unit() {
    1i64;
}

let is_i64 = {
    returns_i64()
};
let is_unit = {
    returns_i64();
};
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/fmt/mod.rs.html#3121)[§](#impl-Debug-for-%28%29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143894 "Tracking issue for const_default")) · [Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#164)[§](#impl-Default-for-%28%29)

[Source](https://doc.rust-lang.org/stable/src/core/default.rs.html#164)[§](#method.default)

Returns the default value of `()`

1.28.0 · [Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#454)[§](#impl-Extend%3C%28%29%3E-for-%28%29)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#455)[§](#method.extend)

Extends a collection with the contents of an iterator. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#tymethod.extend)

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#458)[§](#method.extend_one)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Extends a collection with exactly one element.

[Source](https://doc.rust-lang.org/stable/src/core/iter/traits/collect.rs.html#428)[§](#method.extend_reserve)

🔬This is a nightly-only experimental API. (`extend_one` [#72631](https://github.com/rust-lang/rust/issues/72631))

Reserves capacity in a collection for the given number of additional elements. [Read more](https://doc.rust-lang.org/stable/std/iter/trait.Extend.html#method.extend_reserve)

1.23.0 · [Source](https://doc.rust-lang.org/stable/src/core/unit.rs.html#15)[§](#impl-FromIterator%3C%28%29%3E-for-%28%29)

Collapses all unit items from an iterator into one.

This is more useful when combined with higher-level abstractions, like collecting to a `Result<(), E>` where you only care about errors:

```rust
use std::io::*;
let data = vec![1, 2, 3, 4, 5];
let res: Result<()> = data.iter()
    .map(|x| writeln!(stdout(), "{x}"))
    .collect();
assert!(res.is_ok());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/hash/mod.rs.html#916)[§](#impl-Hash-for-%28%29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#2039)[§](#impl-Ord-for-%28%29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1887)[§](#impl-PartialEq-for-%28%29)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1889)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1893)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1973)[§](#impl-PartialOrd-for-%28%29)

[Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1975)[§](#method.partial_cmp)

This method returns an ordering between `self` and `other` values if one exists. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1410)[§](#method.lt)

Tests less than (for `self` and `other`) and is used by the `<` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.lt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1428)[§](#method.le)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.le)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1446)[§](#method.gt)

Tests greater than (for `self` and `other`) and is used by the `>` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.gt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1464)[§](#method.ge)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator. [Read more](https://doc.rust-lang.org/stable/std/cmp/trait.PartialOrd.html#method.ge)

1.61.0 · [Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#2579-2584)[§](#impl-Termination-for-%28%29)

[Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#2581-2583)[§](#method.report)

Is called to get the representation of the value as status code. This status code is returned to the operating system.

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#1100-1109)[§](#impl-ConstParamTy_-for-%28%29)

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/stable/src/core/cmp.rs.html#1910)[§](#impl-Eq-for-%28%29)

[Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#264-276)[§](#impl-StructuralPartialEq-for-%28%29)

[§](#impl-Freeze-for-%28%29)

[§](#impl-RefUnwindSafe-for-%28%29)

[§](#impl-Send-for-%28%29)

[§](#impl-Sync-for-%28%29)

[§](#impl-Unpin-for-%28%29)

[§](#impl-UnsafeUnpin-for-%28%29)

[§](#impl-UnwindSafe-for-%28%29)