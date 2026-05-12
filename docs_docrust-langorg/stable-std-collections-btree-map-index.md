---
title: std::collections::btree_map - Rust
url: https://doc.rust-lang.org/stable/std/collections/btree_map/index.html
source: crawler
fetched_at: 2026-05-06T21:26:36.829865192-03:00
rendered_js: false
word_count: 250
summary: This document provides the API reference documentation for the Rust btree_map module, detailing the BTreeMap data structure and its associated iterators, entry types, and cursor operations.
tags:
    - rust
    - btree-map
    - data-structures
    - api-reference
    - collections
category: api
---

## Module btree\_map

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/collections/mod.rs.html#19)

Expand description

An ordered map based on a B-Tree.

[BTreeMap](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.BTreeMap.html "struct std::collections::btree_map::BTreeMap")

An ordered map based on a [B-Tree](https://en.wikipedia.org/wiki/B-tree).

[ExtractIf](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.ExtractIf.html "struct std::collections::btree_map::ExtractIf")

An iterator produced by calling `extract_if` on BTreeMap.

[IntoIter](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.IntoIter.html "struct std::collections::btree_map::IntoIter")

An owning iterator over the entries of a `BTreeMap`, sorted by key.

[IntoKeys](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.IntoKeys.html "struct std::collections::btree_map::IntoKeys")

An owning iterator over the keys of a `BTreeMap`.

[IntoValues](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.IntoValues.html "struct std::collections::btree_map::IntoValues")

An owning iterator over the values of a `BTreeMap`.

[Iter](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.Iter.html "struct std::collections::btree_map::Iter")

An iterator over the entries of a `BTreeMap`.

[IterMut](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.IterMut.html "struct std::collections::btree_map::IterMut")

A mutable iterator over the entries of a `BTreeMap`.

[Keys](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.Keys.html "struct std::collections::btree_map::Keys")

An iterator over the keys of a `BTreeMap`.

[OccupiedEntry](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.OccupiedEntry.html "struct std::collections::btree_map::OccupiedEntry")

A view into an occupied entry in a `BTreeMap`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/btree_map/enum.Entry.html "enum std::collections::btree_map::Entry") enum.

[Range](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.Range.html "struct std::collections::btree_map::Range")

An iterator over a sub-range of entries in a `BTreeMap`.

[RangeMut](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.RangeMut.html "struct std::collections::btree_map::RangeMut")

A mutable iterator over a sub-range of entries in a `BTreeMap`.

[VacantEntry](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.VacantEntry.html "struct std::collections::btree_map::VacantEntry")

A view into a vacant entry in a `BTreeMap`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/btree_map/enum.Entry.html "enum std::collections::btree_map::Entry") enum.

[Values](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.Values.html "struct std::collections::btree_map::Values")

An iterator over the values of a `BTreeMap`.

[ValuesMut](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.ValuesMut.html "struct std::collections::btree_map::ValuesMut")

A mutable iterator over the values of a `BTreeMap`.

[Cursor](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.Cursor.html "struct std::collections::btree_map::Cursor")Experimental

A cursor over a `BTreeMap`.

[CursorMut](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.CursorMut.html "struct std::collections::btree_map::CursorMut")Experimental

A cursor over a `BTreeMap` with editing operations.

[CursorMutKey](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.CursorMutKey.html "struct std::collections::btree_map::CursorMutKey")Experimental

A cursor over a `BTreeMap` with editing operations, and which allows mutating the key of elements.

[OccupiedError](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.OccupiedError.html "struct std::collections::btree_map::OccupiedError")Experimental

The error returned by [`try_insert`](https://doc.rust-lang.org/stable/std/collections/struct.BTreeMap.html#method.try_insert "method std::collections::BTreeMap::try_insert") when the key already exists.

[UnorderedKeyError](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.UnorderedKeyError.html "struct std::collections::btree_map::UnorderedKeyError")Experimental

Error type returned by [`CursorMut::insert_before`](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.CursorMut.html#method.insert_before "method std::collections::btree_map::CursorMut::insert_before") and [`CursorMut::insert_after`](https://doc.rust-lang.org/stable/std/collections/btree_map/struct.CursorMut.html#method.insert_after "method std::collections::btree_map::CursorMut::insert_after") if the key being inserted is not properly ordered with regards to adjacent keys.

[Entry](https://doc.rust-lang.org/stable/std/collections/btree_map/enum.Entry.html "enum std::collections::btree_map::Entry")

A view into a single entry in a map, which may either be vacant or occupied.