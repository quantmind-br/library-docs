---
title: ReverseSearcher in std::str::pattern - Rust
url: https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html
source: crawler
fetched_at: 2026-05-06T21:22:27.152100724-03:00
rendered_js: false
word_count: 241
summary: The ReverseSearcher trait defines the interface for searching string patterns in reverse order, providing non-overlapping match and rejection steps.
tags:
    - rust
    - string-pattern
    - trait
    - reverse-search
    - experimental-api
category: reference
---

## Trait ReverseSearcher

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#288)

```rust
pub unsafe trait ReverseSearcher<'a>: Searcher<'a> {
    // Required method
    fn next_back(&mut self) -> SearchStep;

    // Provided methods
    fn next_match_back(&mut self) -> Option<(usize, usize)> { ... }
    fn next_reject_back(&mut self) -> Option<(usize, usize)> { ... }
}
```

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Expand description

A reverse searcher for a string pattern.

This trait provides methods for searching for non-overlapping matches of a pattern starting from the back (right) of a string.

It will be implemented by associated [`Searcher`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher") types of the [`Pattern`](https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html "trait std::str::pattern::Pattern") trait if the pattern supports searching for it from the back.

The index ranges returned by this trait are not required to exactly match those of the forward search in reverse.

For the reason why this trait is marked unsafe, see the parent trait [`Searcher`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher").

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#310)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Performs the next search step starting from the back.

- Returns [`Match(a, b)`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Match "variant std::str::pattern::SearchStep::Match") if `haystack[a..b]` matches the pattern.
- Returns [`Reject(a, b)`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Reject "variant std::str::pattern::SearchStep::Reject") if `haystack[a..b]` can not match the pattern, even partially.
- Returns [`Done`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Done "variant std::str::pattern::SearchStep::Done") if every byte of the haystack has been visited

The stream of [`Match`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Match "variant std::str::pattern::SearchStep::Match") and [`Reject`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Reject "variant std::str::pattern::SearchStep::Reject") values up to a [`Done`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Done "variant std::str::pattern::SearchStep::Done") will contain index ranges that are adjacent, non-overlapping, covering the whole haystack, and laying on utf8 boundaries.

A [`Match`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Match "variant std::str::pattern::SearchStep::Match") result needs to contain the whole matched pattern, however [`Reject`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Reject "variant std::str::pattern::SearchStep::Reject") results may be split up into arbitrary many adjacent fragments. Both ranges may have zero length.

As an example, the pattern `"aaa"` and the haystack `"cbaaaaab"` might produce the stream `[Reject(7, 8), Match(4, 7), Reject(1, 4), Reject(0, 1)]`.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#315)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#328)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))