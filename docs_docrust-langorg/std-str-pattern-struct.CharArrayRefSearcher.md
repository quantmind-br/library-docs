---
title: CharArrayRefSearcher in std::str::pattern - Rust
url: https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html
source: crawler
fetched_at: 2026-05-06T21:34:57.964563232-03:00
rendered_js: false
word_count: 159
summary: The CharArrayRefSearcher struct acts as the associated searcher for character array references implementing the Pattern trait in Rust's core library.
tags:
    - rust
    - api-reference
    - pattern-matching
    - string-processing
    - nightly-api
category: reference
---

## Struct CharArrayRefSearcher

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#816)

```rust
pub struct CharArrayRefSearcher<'a, 'b, const N: usize>(/* private fields */);
```

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Expand description

Associated type for `<&[char; N] as Pattern>::Searcher<'a>`.

## Trait Implementations[§](#trait-implementations)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#815)[§](#impl-Clone-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [Clone](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#815)[§](#impl-Debug-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [Debug](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#858)[§](#impl-ReverseSearcher%3C'a%3E-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [ReverseSearcher](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html "trait std::str::pattern::ReverseSearcher")&lt;'a&gt; for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#854)[§](#impl-Searcher%3C'a%3E-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [Searcher](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher")&lt;'a&gt; for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#862)[§](#impl-DoubleEndedSearcher%3C'a%3E-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [DoubleEndedSearcher](https://doc.rust-lang.org/std/str/pattern/trait.DoubleEndedSearcher.html "trait std::str::pattern::DoubleEndedSearcher")&lt;'a&gt; for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

## Auto Trait Implementations[§](#synthetic-implementations)

[§](#impl-Freeze-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [Freeze](https://doc.rust-lang.org/std/marker/trait.Freeze.html "trait std::marker::Freeze") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[§](#impl-RefUnwindSafe-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [RefUnwindSafe](https://doc.rust-lang.org/std/panic/trait.RefUnwindSafe.html "trait std::panic::RefUnwindSafe") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[§](#impl-Send-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [Send](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[§](#impl-Sync-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [Sync](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[§](#impl-Unpin-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [Unpin](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[§](#impl-UnsafeUnpin-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

[§](#impl-UnwindSafe-for-CharArrayRefSearcher%3C'a,+'b,+N%3E)

### impl&lt;'a, 'b, const N: [usize](https://doc.rust-lang.org/std/primitive.usize.html)&gt; [UnwindSafe](https://doc.rust-lang.org/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe") for [CharArrayRefSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharArrayRefSearcher.html "struct std::str::pattern::CharArrayRefSearcher")&lt;'a, 'b, N&gt;

## Blanket Implementations[§](#blanket-implementations)