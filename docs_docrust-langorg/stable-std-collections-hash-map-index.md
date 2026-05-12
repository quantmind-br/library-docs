---
title: std::collections::hash_map - Rust
url: https://doc.rust-lang.org/stable/std/collections/hash_map/index.html
source: crawler
fetched_at: 2026-05-06T21:26:35.960565797-03:00
rendered_js: false
word_count: 204
summary: This document provides the API reference for the Rust standard library hash_map module, detailing the HashMap structure, its associated iterators, and entry-handling types.
tags:
    - rust
    - hashmap
    - data-structures
    - api-reference
    - collections
    - hashing
category: reference
---

## Module hash\_map

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/collections/mod.rs.html#444)

Expand description

A hash map implemented with quadratic probing and SIMD lookup.

[DefaultHasher](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.DefaultHasher.html "struct std::collections::hash_map::DefaultHasher")

The default [`Hasher`](https://doc.rust-lang.org/stable/std/hash/trait.Hasher.html "trait std::hash::Hasher") used by [`RandomState`](https://doc.rust-lang.org/stable/std/hash/struct.RandomState.html "struct std::hash::RandomState").

[Drain](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.Drain.html "struct std::collections::hash_map::Drain")

A draining iterator over the entries of a `HashMap`.

[ExtractIf](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.ExtractIf.html "struct std::collections::hash_map::ExtractIf")

A draining, filtering iterator over the entries of a `HashMap`.

[HashMap](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.HashMap.html "struct std::collections::hash_map::HashMap")

A [hash map](https://doc.rust-lang.org/stable/std/collections/index.html#use-a-hashmap-when "mod std::collections") implemented with quadratic probing and SIMD lookup.

[IntoIter](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.IntoIter.html "struct std::collections::hash_map::IntoIter")

An owning iterator over the entries of a `HashMap`.

[IntoKeys](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.IntoKeys.html "struct std::collections::hash_map::IntoKeys")

An owning iterator over the keys of a `HashMap`.

[IntoValues](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.IntoValues.html "struct std::collections::hash_map::IntoValues")

An owning iterator over the values of a `HashMap`.

[Iter](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.Iter.html "struct std::collections::hash_map::Iter")

An iterator over the entries of a `HashMap`.

[IterMut](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.IterMut.html "struct std::collections::hash_map::IterMut")

A mutable iterator over the entries of a `HashMap`.

[Keys](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.Keys.html "struct std::collections::hash_map::Keys")

An iterator over the keys of a `HashMap`.

[OccupiedEntry](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.OccupiedEntry.html "struct std::collections::hash_map::OccupiedEntry")

A view into an occupied entry in a `HashMap`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/hash_map/enum.Entry.html "enum std::collections::hash_map::Entry") enum.

[RandomState](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.RandomState.html "struct std::collections::hash_map::RandomState")

`RandomState` is the default state for [`HashMap`](https://doc.rust-lang.org/stable/std/collections/struct.HashMap.html "struct std::collections::HashMap") types.

[VacantEntry](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.VacantEntry.html "struct std::collections::hash_map::VacantEntry")

A view into a vacant entry in a `HashMap`. It is part of the [`Entry`](https://doc.rust-lang.org/stable/std/collections/hash_map/enum.Entry.html "enum std::collections::hash_map::Entry") enum.

[Values](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.Values.html "struct std::collections::hash_map::Values")

An iterator over the values of a `HashMap`.

[ValuesMut](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.ValuesMut.html "struct std::collections::hash_map::ValuesMut")

A mutable iterator over the values of a `HashMap`.

[OccupiedError](https://doc.rust-lang.org/stable/std/collections/hash_map/struct.OccupiedError.html "struct std::collections::hash_map::OccupiedError")Experimental

The error returned by [`try_insert`](https://doc.rust-lang.org/stable/std/collections/struct.HashMap.html#method.try_insert "method std::collections::HashMap::try_insert") when the key already exists.

[Entry](https://doc.rust-lang.org/stable/std/collections/hash_map/enum.Entry.html "enum std::collections::hash_map::Entry")

A view into a single entry in a map, which may either be vacant or occupied.