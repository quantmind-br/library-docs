---
title: StrSearcher in std::str::pattern - Rust
url: https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html
source: crawler
fetched_at: 2026-05-06T21:27:41.706843288-03:00
rendered_js: false
word_count: 75
summary: Describes the experimental StrSearcher struct in Rust, which serves as the associated searcher type for string pattern matching.
tags:
    - rust
    - api-reference
    - string-pattern
    - experimental-api
    - string-searching
category: api
---

## Struct StrSearcher

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#1062)

```rust
pub struct StrSearcher<'a, 'b> { /* private fields */ }
```

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Expand description

Associated type for `<&str as Pattern>::Searcher<'a>`.

## Trait Implementations[§](#trait-implementations)

## Auto Trait Implementations[§](#synthetic-implementations)

[§](#impl-Freeze-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [Freeze](https://doc.rust-lang.org/std/marker/trait.Freeze.html "trait std::marker::Freeze") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

[§](#impl-RefUnwindSafe-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [RefUnwindSafe](https://doc.rust-lang.org/std/panic/trait.RefUnwindSafe.html "trait std::panic::RefUnwindSafe") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

[§](#impl-Send-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [Send](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

[§](#impl-Sync-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [Sync](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

[§](#impl-Unpin-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [Unpin](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

[§](#impl-UnsafeUnpin-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

[§](#impl-UnwindSafe-for-StrSearcher%3C'a,+'b%3E)

### impl&lt;'a, 'b&gt; [UnwindSafe](https://doc.rust-lang.org/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe") for [StrSearcher](https://doc.rust-lang.org/std/str/pattern/struct.StrSearcher.html "struct std::str::pattern::StrSearcher")&lt;'a, 'b&gt;

## Blanket Implementations[§](#blanket-implementations)