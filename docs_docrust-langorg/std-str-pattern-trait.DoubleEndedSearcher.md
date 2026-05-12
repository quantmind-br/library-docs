---
title: DoubleEndedSearcher in std::str::pattern - Rust
url: https://doc.rust-lang.org/std/str/pattern/trait.DoubleEndedSearcher.html
source: crawler
fetched_at: 2026-05-06T21:22:51.941037171-03:00
rendered_js: false
word_count: 132
summary: This trait acts as a marker for searchers that can provide bidirectional iteration consistency when used with double-ended iterators.
tags:
    - rust
    - trait
    - iterator
    - pattern-matching
    - bidirectional-search
    - experimental-api
category: reference
---

## Trait DoubleEndedSearcher

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#360)

```rust
pub trait DoubleEndedSearcher<'a>: ReverseSearcher<'a> { }
```

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Expand description

A marker trait to express that a [`ReverseSearcher`](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html "trait std::str::pattern::ReverseSearcher") can be used for a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") implementation.

For this, the impl of [`Searcher`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher") and [`ReverseSearcher`](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html "trait std::str::pattern::ReverseSearcher") need to follow these conditions:

- All results of `next()` need to be identical to the results of `next_back()` in reverse order.
- `next()` and `next_back()` need to behave as the two ends of a range of values, that is they can not “walk past each other”.

## [§](#examples)Examples

`char::Searcher` is a `DoubleEndedSearcher` because searching for a [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char") only requires looking at one at a time, which behaves the same from both ends.

`(&str)::Searcher` is not a `DoubleEndedSearcher` because the pattern `"aa"` in the haystack `"aaa"` matches as either `"[aa]a"` or `"a[aa]"`, depending on which side it is searched.