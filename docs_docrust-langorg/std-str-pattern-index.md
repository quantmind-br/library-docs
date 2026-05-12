---
title: std::str::pattern - Rust
url: https://doc.rust-lang.org/std/str/pattern/index.html
source: crawler
fetched_at: 2026-05-06T21:22:40.071818259-03:00
rendered_js: false
word_count: 191
summary: The Pattern API provides a generic and flexible mechanism for defining and executing search patterns within string types in Rust.
tags:
    - rust
    - string-pattern
    - api-documentation
    - string-searching
    - generic-traits
category: api
---

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Expand description

The string Pattern API.

The Pattern API provides a generic mechanism for using different pattern types when searching through a string.

For more details, see the traits [`Pattern`](https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html "trait std::str::pattern::Pattern"), [`Searcher`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher"), [`ReverseSearcher`](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html "trait std::str::pattern::ReverseSearcher"), and [`DoubleEndedSearcher`](https://doc.rust-lang.org/std/str/pattern/trait.DoubleEndedSearcher.html "trait std::str::pattern::DoubleEndedSearcher").

Although this API is unstable, it is exposed via stable APIs on the [`str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") type.

## [§](#examples)Examples

[`Pattern`](https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html "trait std::str::pattern::Pattern") is [implemented](https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html#implementors "trait std::str::pattern::Pattern") in the stable API for [`&str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str"), [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), slices of [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char"), and functions and closures implementing `FnMut(char) -> bool`.

```rust
let s = "Can you find a needle in a haystack?";

// &str pattern
assert_eq!(s.find("you"), Some(4));
// char pattern
assert_eq!(s.find('n'), Some(2));
// array of chars pattern
assert_eq!(s.find(&['a', 'e', 'i', 'o', 'u']), Some(1));
// slice of chars pattern
assert_eq!(s.find(&['a', 'e', 'i', 'o', 'u'][..]), Some(1));
// closure pattern
assert_eq!(s.find(|c: char| c.is_ascii_punctuation()), Some(35));
```

[CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")Experimental

Associated type for `<&[char; N] as Pattern>::Searcher<'a>`.

[CharArraySearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArraySearcher.html "struct std::str::pattern::CharArraySearcher")Experimental

Associated type for `<[char; N] as Pattern>::Searcher<'a>`.

[CharPredicateSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharPredicateSearcher.html "struct std::str::pattern::CharPredicateSearcher")Experimental

Associated type for `<F as Pattern>::Searcher<'a>`.

[CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")Experimental

Associated type for `<char as Pattern>::Searcher<'a>`.

[CharSliceSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSliceSearcher.html "struct std::str::pattern::CharSliceSearcher")Experimental

Associated type for `<&[char] as Pattern>::Searcher<'a>`.

[StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")Experimental

Associated type for `<&str as Pattern>::Searcher<'a>`.

[SearchStep](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html "enum std::str::pattern::SearchStep")Experimental

Result of calling [`Searcher::next()`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#tymethod.next "method std::str::pattern::Searcher::next") or [`ReverseSearcher::next_back()`](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html#tymethod.next_back "method std::str::pattern::ReverseSearcher::next_back").

[Utf8Pattern](https://doc.rust-lang.org/std/str/pattern/enum.Utf8Pattern.html "enum std::str::pattern::Utf8Pattern")Experimental

Result of calling [`Pattern::as_utf8_pattern()`](https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html#method.as_utf8_pattern "method std::str::pattern::Pattern::as_utf8_pattern"). Can be used for inspecting the contents of a [`Pattern`](https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html "trait std::str::pattern::Pattern") in cases where the underlying representation can be represented as UTF-8.

[DoubleEndedSearcher](https://doc.rust-lang.org/std/str/pattern/trait.DoubleEndedSearcher.html "trait std::str::pattern::DoubleEndedSearcher")Experimental

A marker trait to express that a [`ReverseSearcher`](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html "trait std::str::pattern::ReverseSearcher") can be used for a [`DoubleEndedIterator`](https://doc.rust-lang.org/std/iter/trait.DoubleEndedIterator.html "trait std::iter::DoubleEndedIterator") implementation.

[Pattern](https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html "trait std::str::pattern::Pattern")Experimental

A string pattern.

[ReverseSearcher](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html "trait std::str::pattern::ReverseSearcher")Experimental

A reverse searcher for a string pattern.

[Searcher](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher")Experimental

A searcher for a string pattern.