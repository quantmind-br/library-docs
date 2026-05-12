---
title: Pattern in std::str::pattern - Rust
url: https://doc.rust-lang.org/std/str/pattern/trait.Pattern.html
source: crawler
fetched_at: 2026-05-06T21:22:20.106339729-03:00
rendered_js: false
word_count: 422
summary: The Pattern trait defines an interface for types that can be used to perform searches within a Rust string slice, providing a unified mechanism for methods like find and contains.
tags:
    - rust
    - string-processing
    - pattern-matching
    - trait
    - experimental-api
    - searcher
category: reference
---

```rust
pub trait Pattern: Sized {
    type Searcher<'a>: Searcher<'a>;

    // Required method
    fn into_searcher(self, haystack: &str) -> Self::Searcher<'_>;

    // Provided methods
    fn is_contained_in(self, haystack: &str) -> bool { ... }
    fn is_prefix_of(self, haystack: &str) -> bool { ... }
    fn is_suffix_of<'a>(self, haystack: &'a str) -> bool
       where Self::Searcher<'a>: ReverseSearcher<'a> { ... }
    fn strip_prefix_of(self, haystack: &str) -> Option<&str> { ... }
    fn strip_suffix_of<'a>(self, haystack: &'a str) -> Option<&'a str>
       where Self::Searcher<'a>: ReverseSearcher<'a> { ... }
    fn as_utf8_pattern(&self) -> Option<Utf8Pattern<'_>> { ... }
}
```

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Expand description

A string pattern.

A `Pattern` expresses that the implementing type can be used as a string pattern for searching in a [`&str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str").

For example, both `'a'` and `"aa"` are patterns that would match at index `1` in the string `"baaaab"`.

The trait itself acts as a builder for an associated [`Searcher`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher") type, which does the actual work of finding occurrences of the pattern in a string.

Depending on the type of the pattern, the behavior of methods like [`str::find`](https://doc.rust-lang.org/std/primitive.str.html#method.find "method str::find") and [`str::contains`](https://doc.rust-lang.org/std/primitive.str.html#method.contains "method str::contains") can change. The table below describes some of those behaviors.

Pattern typeMatch condition `&str`is substring `char`is contained in string `&[char]`any char in slice is contained in string `F: FnMut(char) -> bool``F` returns `true` for a char in string `&&str`is substring `&String`is substring

## [§](#examples)Examples

```rust
// &str
assert_eq!("abaaa".find("ba"), Some(1));
assert_eq!("abaaa".find("bac"), None);

// char
assert_eq!("abaaa".find('a'), Some(0));
assert_eq!("abaaa".find('b'), Some(1));
assert_eq!("abaaa".find('c'), None);

// &[char; N]
assert_eq!("ab".find(&['b', 'a']), Some(0));
assert_eq!("abaaa".find(&['a', 'z']), Some(0));
assert_eq!("abaaa".find(&['c', 'd']), None);

// &[char]
assert_eq!("ab".find(&['b', 'a'][..]), Some(0));
assert_eq!("abaaa".find(&['a', 'z'][..]), Some(0));
assert_eq!("abaaa".find(&['c', 'd'][..]), None);

// FnMut(char) -> bool
assert_eq!("abcdef_z".find(|ch| ch > 'd' && ch < 'y'), Some(4));
assert_eq!("abcddd_z".find(|ch| ch > 'd' && ch < 'y'), None);
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#101)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Associated searcher for this pattern

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#105)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Constructs the associated searcher from `self` and the `haystack` to search in.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#109)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches anywhere in the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#115)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the front of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#121-123)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Checks whether the pattern matches at the back of the haystack

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#130)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the front of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#146-148)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Removes the pattern from the back of haystack, if it matches.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#165)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Returns the pattern as utf-8 bytes if possible.

This trait is **not** [dyn compatible](https://doc.rust-lang.org/1.95.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object safety", so this trait is not object safe.*

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#560)[§](#impl-Pattern-for-char)

Searches for chars that are equal to a given [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char").

#### [§](#examples-1)Examples

```rust
assert_eq!("Hello world".find('o'), Some(4));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#561)[§](#associatedtype.Searcher-1)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#971)[§](#impl-Pattern-for-%26str)

Non-allocating substring search.

Will handle the pattern `""` as returning empty matches at each character boundary.

#### [§](#examples-2)Examples

```rust
assert_eq!("Hello world".find("world"), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#972)[§](#associatedtype.Searcher-2)

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2617)[§](#impl-Pattern-for-%26String)

A convenience impl that delegates to the impl for `&str`.

#### [§](#examples-3)Examples

```rust
assert_eq!(String::from("Hello world").find("world"), Some(6));
```

[Source](https://doc.rust-lang.org/src/alloc/string.rs.html#2618)[§](#associatedtype.Searcher-3)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#892)[§](#impl-Pattern-for-%26%5Bchar%5D)

Searches for chars that are equal to any of the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s in the slice.

#### [§](#examples-4)Examples

```rust
assert_eq!("Hello world".find(&['o', 'l'][..]), Some(2));
assert_eq!("Hello world".find(&['h', 'w'][..]), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#893)[§](#associatedtype.Searcher-4)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#953)[§](#impl-Pattern-for-%26%26str)

Delegates to the `&str` impl.

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#954)[§](#associatedtype.Searcher-5)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#850)[§](#impl-Pattern-for-%26%5Bchar;+N%5D)

Searches for chars that are equal to any of the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s in the array.

#### [§](#examples-5)Examples

```rust
assert_eq!("Hello world".find(&['o', 'l']), Some(2));
assert_eq!("Hello world".find(&['h', 'w']), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#851)[§](#associatedtype.Searcher-6)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#941-943)[§](#impl-Pattern-for-F)

Searches for [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s that match the given predicate.

#### [§](#examples-6)Examples

```rust
assert_eq!("Hello world".find(char::is_uppercase), Some(0));
assert_eq!("Hello world".find(|c| "aeiou".contains(c)), Some(1));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#945)[§](#associatedtype.Searcher-7)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#828)[§](#impl-Pattern-for-%5Bchar;+N%5D)

Searches for chars that are equal to any of the [`char`](https://doc.rust-lang.org/std/primitive.char.html "primitive char")s in the array.

#### [§](#examples-7)Examples

```rust
assert_eq!("Hello world".find(['o', 'l']), Some(2));
assert_eq!("Hello world".find(['h', 'w']), Some(6));
```

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#829)[§](#associatedtype.Searcher-8)