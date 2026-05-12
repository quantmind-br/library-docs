---
title: PartialEq in std::cmp - Rust
url: https://doc.rust-lang.org/std/cmp/trait.PartialEq.html#method.ne
source: crawler
fetched_at: 2026-05-06T21:23:44.144543999-03:00
rendered_js: false
word_count: 783
summary: The PartialEq trait provides a mechanism for defining equality comparisons using the == and != operators for custom types in Rust.
tags:
    - rust
    - traits
    - equality
    - operators
    - partial-eq
    - programming-language
category: reference
---

## Trait PartialEq

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143800 "Tracking issue for const_cmp")) · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#251)

```rust
pub trait PartialEq<Rhs = Self>
where
    Rhs: ?Sized,{
    // Required method
    fn eq(&self, other: &Rhs) -> bool;

    // Provided method
    fn ne(&self, other: &Rhs) -> bool { ... }
}
```

Expand description

Trait for comparisons using the equality operator.

Implementing this trait for types provides the `==` and `!=` operators for those types.

`x.eq(y)` can also be written `x == y`, and `x.ne(y)` can be written `x != y`. We use the easier-to-read infix notation in the remainder of this documentation.

This trait allows for comparisons using the equality operator, for types that do not have a full equivalence relation. For example, in floating point numbers `NaN != NaN`, so floating point types implement `PartialEq` but not [`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html "trait std::cmp::Eq"). Formally speaking, when `Rhs == Self`, this trait corresponds to a [partial equivalence relation](https://en.wikipedia.org/wiki/Partial_equivalence_relation).

Implementations must ensure that `eq` and `ne` are consistent with each other:

- `a != b` if and only if `!(a == b)`.

The default implementation of `ne` provides this consistency and is almost always sufficient. It should not be overridden without very good reason.

If [`PartialOrd`](https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html "trait std::cmp::PartialOrd") or [`Ord`](https://doc.rust-lang.org/std/cmp/trait.Ord.html "trait std::cmp::Ord") are also implemented for `Self` and `Rhs`, their methods must also be consistent with `PartialEq` (see the documentation of those traits for the exact requirements). It’s easy to accidentally make them disagree by deriving some of the traits and manually implementing others.

The equality relation `==` must satisfy the following conditions (for all `a`, `b`, `c` of type `A`, `B`, `C`):

- **Symmetry**: if `A: PartialEq<B>` and `B: PartialEq<A>`, then **`a == b` implies `b == a`** ; and
- **Transitivity**: if `A: PartialEq<B>` and `B: PartialEq<C>` and `A: PartialEq<C>`, then **`a == b` and `b == c` implies `a == c`** . This must also work for longer chains, such as when `A: PartialEq<B>`, `B: PartialEq<C>`, `C: PartialEq<D>`, and `A: PartialEq<D>` all exist.

Note that the `B: PartialEq<A>` (symmetric) and `A: PartialEq<C>` (transitive) impls are not forced to exist, but these requirements apply whenever they do exist.

Violating these requirements is a logic error. The behavior resulting from a logic error is not specified, but users of the trait must ensure that such logic errors do *not* result in undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these methods.

### [§](#cross-crate-considerations)Cross-crate considerations

Upholding the requirements stated above can become tricky when one crate implements `PartialEq` for a type of another crate (i.e., to allow comparing one of its own types with a type from the standard library). The recommendation is to never implement this trait for a foreign type. In other words, such a crate should do `impl PartialEq<ForeignType> for LocalType`, but it should *not* do `impl PartialEq<LocalType> for ForeignType`.

This avoids the problem of transitive chains that criss-cross crate boundaries: for all local types `T`, you may assume that no other crate will add `impl`s that allow comparing `T == U`. In other words, if other crates add `impl`s that allow building longer transitive chains `U1 == ... == T == V1 == ...`, then all the types that appear to the right of `T` must be types that the crate defining `T` already knows about. This rules out transitive chains where downstream crates can add new `impl`s that “stitch together” comparisons of foreign types in ways that violate transitivity.

Not having such foreign `impl`s also avoids forward compatibility issues where one crate adding more `PartialEq` implementations can cause build failures in downstream crates.

### [§](#derivable)Derivable

This trait can be used with `#[derive]`. When `derive`d on structs, two instances are equal if all fields are equal, and not equal if any fields are not equal. When `derive`d on enums, two instances are equal if they are the same variant and all fields are equal.

### [§](#how-can-i-implement-partialeq)How can I implement `PartialEq`?

An example implementation for a domain in which two books are considered the same book if their ISBN matches, even if the formats differ:

```rust
enum BookFormat {
    Paperback,
    Hardback,
    Ebook,
}

struct Book {
    isbn: i32,
    format: BookFormat,
}

impl PartialEq for Book {
    fn eq(&self, other: &Self) -> bool {
        self.isbn == other.isbn
    }
}

let b1 = Book { isbn: 3, format: BookFormat::Paperback };
let b2 = Book { isbn: 3, format: BookFormat::Ebook };
let b3 = Book { isbn: 10, format: BookFormat::Paperback };

assert!(b1 == b2);
assert!(b1 != b3);
```

### [§](#how-can-i-compare-two-different-types)How can I compare two different types?

The type you can compare with is controlled by `PartialEq`’s type parameter. For example, let’s tweak our previous code a bit:

```rust
// The derive implements <BookFormat> == <BookFormat> comparisons
#[derive(PartialEq)]
enum BookFormat {
    Paperback,
    Hardback,
    Ebook,
}

struct Book {
    isbn: i32,
    format: BookFormat,
}

// Implement <Book> == <BookFormat> comparisons
impl PartialEq<BookFormat> for Book {
    fn eq(&self, other: &BookFormat) -> bool {
        self.format == *other
    }
}

// Implement <BookFormat> == <Book> comparisons
impl PartialEq<Book> for BookFormat {
    fn eq(&self, other: &Book) -> bool {
        *self == other.format
    }
}

let b1 = Book { isbn: 3, format: BookFormat::Paperback };

assert!(b1 == BookFormat::Paperback);
assert!(BookFormat::Ebook != b1);
```

By changing `impl PartialEq for Book` to `impl PartialEq<BookFormat> for Book`, we allow `BookFormat`s to be compared with `Book`s.

A comparison like the one above, which ignores some fields of the struct, can be dangerous. It can easily lead to an unintended violation of the requirements for a partial equivalence relation. For example, if we kept the above implementation of `PartialEq<Book>` for `BookFormat` and added an implementation of `PartialEq<Book>` for `Book` (either via a `#[derive]` or via the manual implementation from the first example) then the result would violate transitivity:

[ⓘ](# "This example panics")

```rust
#[derive(PartialEq)]
enum BookFormat {
    Paperback,
    Hardback,
    Ebook,
}

#[derive(PartialEq)]
struct Book {
    isbn: i32,
    format: BookFormat,
}

impl PartialEq<BookFormat> for Book {
    fn eq(&self, other: &BookFormat) -> bool {
        self.format == *other
    }
}

impl PartialEq<Book> for BookFormat {
    fn eq(&self, other: &Book) -> bool {
        *self == other.format
    }
}

fn main() {
    let b1 = Book { isbn: 1, format: BookFormat::Paperback };
    let b2 = Book { isbn: 2, format: BookFormat::Paperback };

    assert!(b1 == BookFormat::Paperback);
    assert!(BookFormat::Paperback == b2);

    // The following should hold by transitivity but doesn't.
    assert!(b1 == b2); // <-- PANICS
}
```

## [§](#examples)Examples

```rust
let x: u32 = 0;
let y: u32 = 1;

assert_eq!(x == y, false);
assert_eq!(x.eq(&y), false);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#256)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.