---
title: PartialOrd in std::cmp - Rust
url: https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#method.ge
source: crawler
fetched_at: 2026-05-06T21:23:49.767131458-03:00
rendered_js: false
word_count: 1056
summary: The PartialOrd trait provides a mechanism for comparing values that form a partial order, supporting the implementation of comparison operators in Rust.
tags:
    - rust
    - trait
    - partial-order
    - comparison
    - operators
    - programming-language
category: reference
---

## Trait PartialOrd

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1366-1367)

```rust
pub trait PartialOrd<Rhs = Self>: PartialEq<Rhs>
where
    Rhs: ?Sized,{
    // Required method
    fn partial_cmp(&self, other: &Rhs) -> Option<Ordering>;

    // Provided methods
    fn lt(&self, other: &Rhs) -> bool { ... }
    fn le(&self, other: &Rhs) -> bool { ... }
    fn gt(&self, other: &Rhs) -> bool { ... }
    fn ge(&self, other: &Rhs) -> bool { ... }
}
```

Expand description

Trait for types that form a [partial order](https://en.wikipedia.org/wiki/Partial_order).

The `lt`, `le`, `gt`, and `ge` methods of this trait can be called using the `<`, `<=`, `>`, and `>=` operators, respectively.

This trait should **only** contain the comparison logic for a type **if one plans on only implementing `PartialOrd` but not [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord")**. Otherwise the comparison logic should be in [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") and this trait implemented with `Some(self.cmp(other))`.

The methods of this trait must be consistent with each other and with those of [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq"). The following conditions must hold:

1. `a == b` if and only if `partial_cmp(a, b) == Some(Equal)`.
2. `a < b` if and only if `partial_cmp(a, b) == Some(Less)`
3. `a > b` if and only if `partial_cmp(a, b) == Some(Greater)`
4. `a <= b` if and only if `a < b || a == b`
5. `a >= b` if and only if `a > b || a == b`
6. `a != b` if and only if `!(a == b)`.

Conditions 2–5 above are ensured by the default implementation. Condition 6 is already ensured by [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq").

If [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") is also implemented for `Self` and `Rhs`, it must also be consistent with `partial_cmp` (see the documentation of that trait for the exact requirements). It’s easy to accidentally make them disagree by deriving some of the traits and manually implementing others.

The comparison relations must satisfy the following conditions (for all `a`, `b`, `c` of type `A`, `B`, `C`):

- **Transitivity**: if `A: PartialOrd<B>` and `B: PartialOrd<C>` and `A: PartialOrd<C>`, then `a < b` and `b < c` implies `a < c`. The same must hold for both `==` and `>`. This must also work for longer chains, such as when `A: PartialOrd<B>`, `B: PartialOrd<C>`, `C: PartialOrd<D>`, and `A: PartialOrd<D>` all exist.
- **Duality**: if `A: PartialOrd<B>` and `B: PartialOrd<A>`, then `a < b` if and only if `b > a`.

Note that the `B: PartialOrd<A>` (dual) and `A: PartialOrd<C>` (transitive) impls are not forced to exist, but these requirements apply whenever they do exist.

Violating these requirements is a logic error. The behavior resulting from a logic error is not specified, but users of the trait must ensure that such logic errors do *not* result in undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these methods.

### [§](#cross-crate-considerations)Cross-crate considerations

Upholding the requirements stated above can become tricky when one crate implements `PartialOrd` for a type of another crate (i.e., to allow comparing one of its own types with a type from the standard library). The recommendation is to never implement this trait for a foreign type. In other words, such a crate should do `impl PartialOrd<ForeignType> for LocalType`, but it should *not* do `impl PartialOrd<LocalType> for ForeignType`.

This avoids the problem of transitive chains that criss-cross crate boundaries: for all local types `T`, you may assume that no other crate will add `impl`s that allow comparing `T < U`. In other words, if other crates add `impl`s that allow building longer transitive chains `U1 < ... < T < V1 < ...`, then all the types that appear to the right of `T` must be types that the crate defining `T` already knows about. This rules out transitive chains where downstream crates can add new `impl`s that “stitch together” comparisons of foreign types in ways that violate transitivity.

Not having such foreign `impl`s also avoids forward compatibility issues where one crate adding more `PartialOrd` implementations can cause build failures in downstream crates.

### [§](#corollaries)Corollaries

The following corollaries follow from the above requirements:

- irreflexivity of `<` and `>`: `!(a < a)`, `!(a > a)`
- transitivity of `>`: if `a > b` and `b > c` then `a > c`
- duality of `partial_cmp`: `partial_cmp(a, b) == partial_cmp(b, a).map(Ordering::reverse)`

### [§](#strict-and-non-strict-partial-orders)Strict and non-strict partial orders

The `<` and `>` operators behave according to a *strict* partial order. However, `<=` and `>=` do **not** behave according to a *non-strict* partial order. That is because mathematically, a non-strict partial order would require reflexivity, i.e. `a <= a` would need to be true for every `a`. This isn’t always the case for types that implement `PartialOrd`, for example:

```rust
let a = f64::NAN;
assert_eq!(a <= a, false);
```

### [§](#derivable)Derivable

This trait can be used with `#[derive]`.

When `derive`d on structs, it will produce a [lexicographic](https://en.wikipedia.org/wiki/Lexicographic_order) ordering based on the top-to-bottom declaration order of the struct’s members.

When `derive`d on enums, variants are primarily ordered by their discriminants. Secondarily, they are ordered by their fields. By default, the discriminant is smallest for variants at the top, and largest for variants at the bottom. Here’s an example:

```rust
#[derive(PartialEq, PartialOrd)]
enum E {
    Top,
    Bottom,
}

assert!(E::Top < E::Bottom);
```

However, manually setting the discriminants can override this default behavior:

```rust
#[derive(PartialEq, PartialOrd)]
enum E {
    Top = 2,
    Bottom = 1,
}

assert!(E::Bottom < E::Top);
```

### [§](#how-can-i-implement-partialord)How can I implement `PartialOrd`?

`PartialOrd` only requires implementation of the [`partial_cmp`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp "method std::cmp::PartialOrd::partial_cmp") method, with the others generated from default implementations.

However it remains possible to implement the others separately for types which do not have a total order. For example, for floating point numbers, `NaN < 0 == false` and `NaN >= 0 == false` (cf. IEEE 754-2008 section 5.11).

`PartialOrd` requires your type to be [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq").

If your type is [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord"), you can implement [`partial_cmp`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp "method std::cmp::PartialOrd::partial_cmp") by using [`cmp`](https://doc.rust-lang.org/std/cmp/trait.Ord.html#tymethod.cmp "method std::cmp::Ord::cmp"):

```rust
use std::cmp::Ordering;

struct Person {
    id: u32,
    name: String,
    height: u32,
}

impl PartialOrd for Person {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Person {
    fn cmp(&self, other: &Self) -> Ordering {
        self.height.cmp(&other.height)
    }
}

impl PartialEq for Person {
    fn eq(&self, other: &Self) -> bool {
        self.height == other.height
    }
}

impl Eq for Person {}
```

You may also find it useful to use [`partial_cmp`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html#tymethod.partial_cmp "method std::cmp::PartialOrd::partial_cmp") on your type’s fields. Here is an example of `Person` types who have a floating-point `height` field that is the only field to be used for sorting:

```rust
use std::cmp::Ordering;

struct Person {
    id: u32,
    name: String,
    height: f64,
}

impl PartialOrd for Person {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        self.height.partial_cmp(&other.height)
    }
}

impl PartialEq for Person {
    fn eq(&self, other: &Self) -> bool {
        self.height == other.height
    }
}
```

### [§](#examples-of-incorrect-partialord-implementations)Examples of incorrect `PartialOrd` implementations

```rust
use std::cmp::Ordering;

#[derive(PartialEq, Debug)]
struct Character {
    health: u32,
    experience: u32,
}

impl PartialOrd for Character {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.health.cmp(&other.health))
    }
}

let a = Character {
    health: 10,
    experience: 5,
};
let b = Character {
    health: 10,
    experience: 77,
};

// Mistake: `PartialEq` and `PartialOrd` disagree with each other.

assert_eq!(a.partial_cmp(&b).unwrap(), Ordering::Equal); // a == b according to `PartialOrd`.
assert_ne!(a, b); // a != b according to `PartialEq`.
```

## [§](#examples)Examples

```rust
let x: u32 = 0;
let y: u32 = 1;

assert_eq!(x < y, true);
assert_eq!(x.lt(&y), true);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1395)

This method returns an ordering between `self` and `other` values if one exists.

##### [§](#examples-1)Examples

```rust
use std::cmp::Ordering;

let result = 1.0.partial_cmp(&2.0);
assert_eq!(result, Some(Ordering::Less));

let result = 1.0.partial_cmp(&1.0);
assert_eq!(result, Some(Ordering::Equal));

let result = 2.0.partial_cmp(&1.0);
assert_eq!(result, Some(Ordering::Greater));
```

When comparison is impossible:

```rust
let result = f64::NAN.partial_cmp(&1.0);
assert_eq!(result, None);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1410)

Tests less than (for `self` and `other`) and is used by the `<` operator.

##### [§](#examples-2)Examples

```rust
assert_eq!(1.0 < 1.0, false);
assert_eq!(1.0 < 2.0, true);
assert_eq!(2.0 < 1.0, false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1428)

Tests less than or equal to (for `self` and `other`) and is used by the `<=` operator.

##### [§](#examples-3)Examples

```rust
assert_eq!(1.0 <= 1.0, true);
assert_eq!(1.0 <= 2.0, true);
assert_eq!(2.0 <= 1.0, false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1446)

Tests greater than (for `self` and `other`) and is used by the `>` operator.

##### [§](#examples-4)Examples

```rust
assert_eq!(1.0 > 1.0, false);
assert_eq!(1.0 > 2.0, false);
assert_eq!(2.0 > 1.0, true);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1464)

Tests greater than or equal to (for `self` and `other`) and is used by the `>=` operator.

##### [§](#examples-5)Examples

```rust
assert_eq!(1.0 >= 1.0, true);
assert_eq!(1.0 >= 2.0, false);
assert_eq!(2.0 >= 1.0, true);
```