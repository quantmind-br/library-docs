---
title: std::collections::hash_set - Rust
url: https://doc.rust-lang.org/stable/std/collections/hash_set/index.html
source: crawler
fetched_at: 2026-05-06T21:26:36.125398667-03:00
rendered_js: false
word_count: 168
summary: This document provides a technical overview of the HashSet module in Rust, detailing its structure as a hash-based set implementation and listing the available iterators and entry-management types.
tags:
    - rust
    - hash-set
    - collections
    - api-reference
    - data-structures
    - iterators
category: reference
---

## Module hash\_set

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/collections/mod.rs.html#455)

Expand description

A hash set implemented as a `HashMap` where the value is `()`.

[Difference](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.Difference.html "struct std::collections::hash_set::Difference")

A lazy iterator producing elements in the difference of `HashSet`s.

[Drain](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.Drain.html "struct std::collections::hash_set::Drain")

A draining iterator over the items of a `HashSet`.

[ExtractIf](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.ExtractIf.html "struct std::collections::hash_set::ExtractIf")

A draining, filtering iterator over the items of a `HashSet`.

[HashSet](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.HashSet.html "struct std::collections::hash_set::HashSet")

A [hash set](https://doc.rust-lang.org/stable/std/collections/index.html#use-the-set-variant-of-any-of-these-maps-when "mod std::collections") implemented as a `HashMap` where the value is `()`.

[Intersection](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.Intersection.html "struct std::collections::hash_set::Intersection")

A lazy iterator producing elements in the intersection of `HashSet`s.

[IntoIter](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.IntoIter.html "struct std::collections::hash_set::IntoIter")

An owning iterator over the items of a `HashSet`.

[Iter](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.Iter.html "struct std::collections::hash_set::Iter")

An iterator over the items of a `HashSet`.

[SymmetricDifference](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.SymmetricDifference.html "struct std::collections::hash_set::SymmetricDifference")

A lazy iterator producing elements in the symmetric difference of `HashSet`s.

[Union](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.Union.html "struct std::collections::hash_set::Union")

A lazy iterator producing elements in the union of `HashSet`s.

[OccupiedEntry](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.OccupiedEntry.html "struct std::collections::hash_set::OccupiedEntry")Experimental

A view into an occupied entry in a `HashSet`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/hash_set/enum.Entry.html) enum.

[VacantEntry](https://doc.rust-lang.org/stable/std/collections/hash_set/struct.VacantEntry.html "struct std::collections::hash_set::VacantEntry")Experimental

A view into a vacant entry in a `HashSet`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/hash_set/enum.Entry.html) enum.

[Entry](https://doc.rust-lang.org/stable/std/collections/hash_set/enum.Entry.html "enum std::collections::hash_set::Entry")Experimental

A view into a single entry in a set, which may either be vacant or occupied.