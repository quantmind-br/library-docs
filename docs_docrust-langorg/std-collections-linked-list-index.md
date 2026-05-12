---
title: std::collections::linked_list - Rust
url: https://doc.rust-lang.org/std/collections/linked_list/index.html
source: crawler
fetched_at: 2026-05-06T21:24:53.349866664-03:00
rendered_js: false
word_count: 113
summary: This document provides the API documentation for the Rust standard library's doubly-linked list implementation, including its associated iterators and cursor types.
tags:
    - rust-standard-library
    - linked-list
    - data-structures
    - collection-types
    - api-documentation
category: reference
---

## Module linked\_list

1.0.0 · [Source](https://doc.rust-lang.org/src/alloc/collections/mod.rs.html#13)

Expand description

A doubly-linked list with owned nodes.

The `LinkedList` allows pushing and popping elements at either end in constant time.

NOTE: It is almost always better to use [`Vec`](https://doc.rust-lang.org/std/vec/struct.Vec.html "struct std::vec::Vec") or [`VecDeque`](https://doc.rust-lang.org/std/collections/struct.VecDeque.html "struct std::collections::VecDeque") because array-based containers are generally faster, more memory efficient, and make better use of CPU cache.

[ExtractIf](https://doc.rust-lang.org/std/collections/linked_list/struct.ExtractIf.html "struct std::collections::linked_list::ExtractIf")

An iterator produced by calling `extract_if` on LinkedList.

[IntoIter](https://doc.rust-lang.org/std/collections/linked_list/struct.IntoIter.html "struct std::collections::linked_list::IntoIter")

An owning iterator over the elements of a `LinkedList`.

[Iter](https://doc.rust-lang.org/std/collections/linked_list/struct.Iter.html "struct std::collections::linked_list::Iter")

An iterator over the elements of a `LinkedList`.

[IterMut](https://doc.rust-lang.org/std/collections/linked_list/struct.IterMut.html "struct std::collections::linked_list::IterMut")

A mutable iterator over the elements of a `LinkedList`.

[LinkedList](https://doc.rust-lang.org/std/collections/linked_list/struct.LinkedList.html "struct std::collections::linked_list::LinkedList")

A doubly-linked list with owned nodes.

[Cursor](https://doc.rust-lang.org/std/collections/linked_list/struct.Cursor.html "struct std::collections::linked_list::Cursor")Experimental

A cursor over a `LinkedList`.

[CursorMut](https://doc.rust-lang.org/std/collections/linked_list/struct.CursorMut.html "struct std::collections::linked_list::CursorMut")Experimental

A cursor over a `LinkedList` with editing operations.