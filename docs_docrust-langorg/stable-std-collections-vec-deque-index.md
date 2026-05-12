---
title: std::collections::vec_deque - Rust
url: https://doc.rust-lang.org/stable/std/collections/vec_deque/index.html
source: crawler
fetched_at: 2026-05-06T21:26:36.480946662-03:00
rendered_js: false
word_count: 130
summary: This document provides an API overview of the VecDeque collection in Rust, which functions as a double-ended queue implemented via a growable ring buffer.
tags:
    - rust
    - data-structures
    - vec-deque
    - collection
    - ring-buffer
    - api-reference
category: reference
---

## Module vec\_deque

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/alloc/collections/mod.rs.html#15)

Expand description

A double-ended queue (deque) implemented with a growable ring buffer.

This queue has *O*(1) amortized inserts and removals from both ends of the container. It also has *O*(1) indexing like a vector. The contained elements are not required to be copyable, and the queue will be sendable if the contained type is sendable.

[Drain](https://doc.rust-lang.org/stable/std/collections/vec_deque/struct.Drain.html "struct std::collections::vec_deque::Drain")

A draining iterator over the elements of a `VecDeque`.

[IntoIter](https://doc.rust-lang.org/stable/std/collections/vec_deque/struct.IntoIter.html "struct std::collections::vec_deque::IntoIter")

An owning iterator over the elements of a `VecDeque`.

[Iter](https://doc.rust-lang.org/stable/std/collections/vec_deque/struct.Iter.html "struct std::collections::vec_deque::Iter")

An iterator over the elements of a `VecDeque`.

[IterMut](https://doc.rust-lang.org/stable/std/collections/vec_deque/struct.IterMut.html "struct std::collections::vec_deque::IterMut")

A mutable iterator over the elements of a `VecDeque`.

[VecDeque](https://doc.rust-lang.org/stable/std/collections/vec_deque/struct.VecDeque.html "struct std::collections::vec_deque::VecDeque")

A double-ended queue implemented with a growable ring buffer.

[ExtractIf](https://doc.rust-lang.org/stable/std/collections/vec_deque/struct.ExtractIf.html "struct std::collections::vec_deque::ExtractIf")Experimental

An iterator which uses a closure to determine if an element should be removed.

[Splice](https://doc.rust-lang.org/stable/std/collections/vec_deque/struct.Splice.html "struct std::collections::vec_deque::Splice")Experimental

A splicing iterator for `VecDeque`.