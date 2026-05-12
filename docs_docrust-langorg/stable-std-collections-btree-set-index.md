---
title: std::collections::btree_set - Rust
url: https://doc.rust-lang.org/stable/std/collections/btree_set/index.html
source: crawler
fetched_at: 2026-05-06T21:26:36.143259481-03:00
rendered_js: false
word_count: 211
summary: This document provides a technical reference for the BTreeSet module in Rust, detailing the available data structures, iterators, and experimental entry APIs.
tags:
    - rust
    - btree
    - collections
    - data-structures
    - api-reference
    - set
category: reference
---

## Module btree\_set

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/collections/mod.rs.html#27)

Expand description

An ordered set based on a B-Tree.

[BTreeSet](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.BTreeSet.html "struct std::collections::btree_set::BTreeSet")

An ordered set based on a B-Tree.

[Difference](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.Difference.html "struct std::collections::btree_set::Difference")

A lazy iterator producing elements in the difference of `BTreeSet`s.

[ExtractIf](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.ExtractIf.html "struct std::collections::btree_set::ExtractIf")

An iterator produced by calling `extract_if` on BTreeSet.

[Intersection](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.Intersection.html "struct std::collections::btree_set::Intersection")

A lazy iterator producing elements in the intersection of `BTreeSet`s.

[IntoIter](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.IntoIter.html "struct std::collections::btree_set::IntoIter")

An owning iterator over the items of a `BTreeSet` in ascending order.

[Iter](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.Iter.html "struct std::collections::btree_set::Iter")

An iterator over the items of a `BTreeSet`.

[Range](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.Range.html "struct std::collections::btree_set::Range")

An iterator over a sub-range of items in a `BTreeSet`.

[SymmetricDifference](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.SymmetricDifference.html "struct std::collections::btree_set::SymmetricDifference")

A lazy iterator producing elements in the symmetric difference of `BTreeSet`s.

[Union](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.Union.html "struct std::collections::btree_set::Union")

A lazy iterator producing elements in the union of `BTreeSet`s.

[Cursor](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.Cursor.html "struct std::collections::btree_set::Cursor")Experimental

A cursor over a `BTreeSet`.

[CursorMut](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.CursorMut.html "struct std::collections::btree_set::CursorMut")Experimental

A cursor over a `BTreeSet` with editing operations.

[CursorMutKey](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.CursorMutKey.html "struct std::collections::btree_set::CursorMutKey")Experimental

A cursor over a `BTreeSet` with editing operations, and which allows mutating elements.

[OccupiedEntry](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.OccupiedEntry.html "struct std::collections::btree_set::OccupiedEntry")Experimental

A view into an occupied entry in a `BTreeSet`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/btree_set/enum.Entry.html "enum std::collections::btree_set::Entry") enum.

[UnorderedKeyError](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.UnorderedKeyError.html "struct std::collections::btree_set::UnorderedKeyError")Experimental

Error type returned by [`CursorMut::insert_before`](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.CursorMut.html#method.insert_before "method std::collections::btree_map::CursorMut::insert_before") and [`CursorMut::insert_after`](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.CursorMut.html#method.insert_after "method std::collections::btree_map::CursorMut::insert_after") if the key being inserted is not properly ordered with regards to adjacent keys.

[VacantEntry](https://doc.rust-lang.org/stable/std/collections/btree_set/struct.VacantEntry.html "struct std::collections::btree_set::VacantEntry")Experimental

A view into a vacant entry in a `BTreeSet`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/btree_set/enum.Entry.html "enum std::collections::btree_set::Entry") enum.

[Entry](https://doc.rust-lang.org/stable/std/collections/btree_set/enum.Entry.html "enum std::collections::btree_set::Entry")Experimental

A view into a single entry in a set, which may either be vacant or occupied.