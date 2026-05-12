---
title: Ord in std::cmp - Rust
url: https://doc.rust-lang.org/std/cmp/trait.Ord.html#method.max
source: crawler
fetched_at: 2026-05-06T21:23:41.693817297-03:00
rendered_js: false
word_count: 963
summary: The Ord trait defines a total ordering for types in Rust, requiring consistent implementations of comparison methods relative to PartialEq and PartialOrd.
tags:
    - rust
    - trait
    - ordering
    - total-order
    - comparison
    - data-structures
category: reference
---

## Trait Ord

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#981)

```rust
pub trait Ord: Eq + PartialOrd {
    // Required method
    fn cmp(&self, other: &Self) -> Ordering;

    // Provided methods
    fn max(self, other: Self) -> Self
       where Self: Sized { ... }
    fn min(self, other: Self) -> Self
       where Self: Sized { ... }
    fn clamp(self, min: Self, max: Self) -> Self
       where Self: Sized { ... }
}
```

Expand description

Trait for types that form a [total order](https://en.wikipedia.org/wiki/Total_order).

Implementations must be consistent with the [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") implementation, and ensure `max`, `min`, and `clamp` are consistent with `cmp`:

- `partial_cmp(a, b) == Some(cmp(a, b))`.
- `max(a, b) == max_by(a, b, cmp)` (ensured by the default implementation).
- `min(a, b) == min_by(a, b, cmp)` (ensured by the default implementation).
- For `a.clamp(min, max)`, see the [method docs](#method.clamp) (ensured by the default implementation).

Violating these requirements is a logic error. The behavior resulting from a logic error is not specified, but users of the trait must ensure that such logic errors do *not* result in undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these methods.

### [§](#corollaries)Corollaries

From the above and the requirements of `PartialOrd`, it follows that for all `a`, `b` and `c`:

- exactly one of `a < b`, `a == b` or `a > b` is true; and
- `<` is transitive: `a < b` and `b < c` implies `a < c`. The same must hold for both `==` and `>`.

Mathematically speaking, the `<` operator defines a strict [weak order](https://en.wikipedia.org/wiki/Weak_ordering). In cases where `==` conforms to mathematical equality, it also defines a strict [total order](https://en.wikipedia.org/wiki/Total_order).

### [§](#derivable)Derivable

This trait can be used with `#[derive]`.

When `derive`d on structs, it will produce a [lexicographic](https://en.wikipedia.org/wiki/Lexicographic_order) ordering based on the top-to-bottom declaration order of the struct’s members.

When `derive`d on enums, variants are ordered primarily by their discriminants. Secondarily, they are ordered by their fields. By default, the discriminant is smallest for variants at the top, and largest for variants at the bottom. Here’s an example:

```rust
#[derive(PartialEq, Eq, PartialOrd, Ord)]
enum E {
    Top,
    Bottom,
}

assert!(E::Top < E::Bottom);
```

However, manually setting the discriminants can override this default behavior:

```rust
#[derive(PartialEq, Eq, PartialOrd, Ord)]
enum E {
    Top = 2,
    Bottom = 1,
}

assert!(E::Bottom < E::Top);
```

### [§](#lexicographical-comparison)Lexicographical comparison

Lexicographical comparison is an operation with the following properties:

- Two sequences are compared element by element.
- The first mismatching element defines which sequence is lexicographically less or greater than the other.
- If one sequence is a prefix of another, the shorter sequence is lexicographically less than the other.
- If two sequences have equivalent elements and are of the same length, then the sequences are lexicographically equal.
- An empty sequence is lexicographically less than any non-empty sequence.
- Two empty sequences are lexicographically equal.

### [§](#how-can-i-implement-ord)How can I implement `Ord`?

`Ord` requires that the type also be [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd"), [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq"), and [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq").

Because `Ord` implies a stronger ordering relationship than [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd"), and both `Ord` and [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") must agree, you must choose how to implement `Ord` **first**. You can choose to derive it, or implement it manually. If you derive it, you should derive all four traits. If you implement it manually, you should manually implement all four traits, based on the implementation of `Ord`.

Here’s an example where you want to define the `Character` comparison by `health` and `experience` only, disregarding the field `mana`:

```rust
use std::cmp::Ordering;

struct Character {
    health: u32,
    experience: u32,
    mana: f32,
}

impl Ord for Character {
    fn cmp(&self, other: &Self) -> Ordering {
        self.experience
            .cmp(&other.experience)
            .then(self.health.cmp(&other.health))
    }
}

impl PartialOrd for Character {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Character {
    fn eq(&self, other: &Self) -> bool {
        self.health == other.health && self.experience == other.experience
    }
}

impl Eq for Character {}
```

If all you need is to `slice::sort` a type by a field value, it can be simpler to use `slice::sort_by_key`.

### [§](#examples-of-incorrect-ord-implementations)Examples of incorrect `Ord` implementations

```rust
use std::cmp::Ordering;

#[derive(Debug)]
struct Character {
    health: f32,
}

impl Ord for Character {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        if self.health < other.health {
            Ordering::Less
        } else if self.health > other.health {
            Ordering::Greater
        } else {
            Ordering::Equal
        }
    }
}

impl PartialOrd for Character {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Character {
    fn eq(&self, other: &Self) -> bool {
        self.health == other.health
    }
}

impl Eq for Character {}

let a = Character { health: 4.5 };
let b = Character { health: f32::NAN };

// Mistake: floating-point values do not form a total order and using the built-in comparison
// operands to implement `Ord` irregardless of that reality does not change it. Use
// `f32::total_cmp` if you need a total order for floating-point values.

// Reflexivity requirement of `Ord` is not given.
assert!(a == a);
assert!(b != b);

// Antisymmetry requirement of `Ord` is not given. Only one of a < c and c < a is allowed to be
// true, not both or neither.
assert_eq!((a < b) as u8 + (b < a) as u8, 0);
```

```rust
use std::cmp::Ordering;

#[derive(Debug)]
struct Character {
    health: u32,
    experience: u32,
}

impl PartialOrd for Character {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Character {
    fn cmp(&self, other: &Self) -> std::cmp::Ordering {
        if self.health < 50 {
            self.health.cmp(&other.health)
        } else {
            self.experience.cmp(&other.experience)
        }
    }
}

// For performance reasons implementing `PartialEq` this way is not the idiomatic way, but it
// ensures consistent behavior between `PartialEq`, `PartialOrd` and `Ord` in this example.
impl PartialEq for Character {
    fn eq(&self, other: &Self) -> bool {
        self.cmp(other) == Ordering::Equal
    }
}

impl Eq for Character {}

let a = Character {
    health: 3,
    experience: 5,
};
let b = Character {
    health: 10,
    experience: 77,
};
let c = Character {
    health: 143,
    experience: 2,
};

// Mistake: The implementation of `Ord` compares different fields depending on the value of
// `self.health`, the resulting order is not total.

// Transitivity requirement of `Ord` is not given. If a is smaller than b and b is smaller than
// c, by transitive property a must also be smaller than c.
assert!(a < b && b < c && c < a);

// Antisymmetry requirement of `Ord` is not given. Only one of a < c and c < a is allowed to be
// true, not both or neither.
assert_eq!((a < c) as u8 + (c < a) as u8, 2);
```

The documentation of [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") contains further examples, for example it’s wrong for [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") and [`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html "trait std::cmp::PartialEq") to disagree.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#999)

This method returns an [`Ordering`](https://doc.rust-lang.org/std/cmp/enum.Ordering.html "enum std::cmp::Ordering") between `self` and `other`.

By convention, `self.cmp(&other)` returns the ordering matching the expression `self <operator> other` if true.

##### [§](#examples)Examples

```rust
use std::cmp::Ordering;

assert_eq!(5.cmp(&10), Ordering::Less);
assert_eq!(10.cmp(&5), Ordering::Greater);
assert_eq!(5.cmp(&5), Ordering::Equal);
```

1.21.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1033-1035)

Compares and returns the maximum of two values.

Returns the second argument if the comparison determines them to be equal.

##### [§](#examples-1)Examples

```rust
assert_eq!(1.max(2), 2);
assert_eq!(2.max(2), 2);
```

```rust
use std::cmp::Ordering;

#[derive(Eq)]
struct Equal(&'static str);

impl PartialEq for Equal {
    fn eq(&self, other: &Self) -> bool { true }
}
impl PartialOrd for Equal {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(Ordering::Equal) }
}
impl Ord for Equal {
    fn cmp(&self, other: &Self) -> Ordering { Ordering::Equal }
}

assert_eq!(Equal("self").max(Equal("other")).0, "other");
```

1.21.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1072-1074)

Compares and returns the minimum of two values.

Returns the first argument if the comparison determines them to be equal.

##### [§](#examples-2)Examples

```rust
assert_eq!(1.min(2), 1);
assert_eq!(2.min(2), 2);
```

```rust
use std::cmp::Ordering;

#[derive(Eq)]
struct Equal(&'static str);

impl PartialEq for Equal {
    fn eq(&self, other: &Self) -> bool { true }
}
impl PartialOrd for Equal {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> { Some(Ordering::Equal) }
}
impl Ord for Equal {
    fn cmp(&self, other: &Self) -> Ordering { Ordering::Equal }
}

assert_eq!(Equal("self").min(Equal("other")).0, "self");
```

1.50.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#1098-1100)

Restrict a value to a certain interval.

Returns `max` if `self` is greater than `max`, and `min` if `self` is less than `min`. Otherwise this returns `self`.

##### [§](#panics)Panics

Panics if `min > max`.

##### [§](#examples-3)Examples

```rust
assert_eq!((-3).clamp(-2, 1), -2);
assert_eq!(0.clamp(-2, 1), 0);
assert_eq!(2.clamp(-2, 1), 1);
```

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*