---
title: Index in std::ops - Rust
url: https://doc.rust-lang.org/std/ops/trait.Index.html
source: crawler
fetched_at: 2026-05-06T21:22:31.008253238-03:00
rendered_js: false
word_count: 105
summary: This document defines the Index trait in Rust, which allows custom types to support immutable indexing syntax through the square bracket operator.
tags:
    - rust
    - trait
    - indexing
    - operator-overloading
    - standard-library
category: reference
---

## Trait Index

1.0.0 (const: [unstable](https://github.com/rust-lang/rust/issues/143775 "Tracking issue for const_index")) · [Source](https://doc.rust-lang.org/src/core/ops/index.rs.html#59)

```rust
pub trait Index<Idx>
where
    Idx: ?Sized,{
    type Output: ?Sized;

    // Required method
    fn index(&self, index: Idx) -> &Self::Output;
}
```

Expand description

Used for indexing operations (`container[index]`) in immutable contexts.

`container[index]` is actually syntactic sugar for `*container.index(index)`, but only when used as an immutable value. If a mutable value is requested, [`IndexMut`](https://doc.rust-lang.org/std/ops/trait.IndexMut.html "trait std::ops::IndexMut") is used instead. This allows nice things such as `let value = v[index]` if the type of `value` implements [`Copy`](https://doc.rust-lang.org/std/marker/trait.Copy.html "trait std::marker::Copy").

## [§](#examples)Examples

The following example implements `Index` on a read-only `NucleotideCount` container, enabling individual counts to be retrieved with index syntax.

```rust
use std::ops::Index;

enum Nucleotide {
    A,
    C,
    G,
    T,
}

struct NucleotideCount {
    a: usize,
    c: usize,
    g: usize,
    t: usize,
}

impl Index<Nucleotide> for NucleotideCount {
    type Output = usize;

    fn index(&self, nucleotide: Nucleotide) -> &Self::Output {
        match nucleotide {
            Nucleotide::A => &self.a,
            Nucleotide::C => &self.c,
            Nucleotide::G => &self.g,
            Nucleotide::T => &self.t,
        }
    }
}

let nucleotide_count = NucleotideCount {a: 14, c: 9, g: 10, t: 12};
assert_eq!(nucleotide_count[Nucleotide::A], 14);
assert_eq!(nucleotide_count[Nucleotide::C], 9);
assert_eq!(nucleotide_count[Nucleotide::G], 10);
assert_eq!(nucleotide_count[Nucleotide::T], 12);
```

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/index.rs.html#63)

The returned type after indexing.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/ops/index.rs.html#73)

Performs the indexing (`container[index]`) operation.

##### [§](#panics)Panics

May panic if the index is out of bounds.