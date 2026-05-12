---
title: CharSearcher in std::str::pattern - Rust
url: https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html
source: crawler
fetched_at: 2026-05-06T21:29:22.555721718-03:00
rendered_js: false
word_count: 570
summary: This document provides the API reference for the CharSearcher struct in Rust, which is an experimental utility used for searching characters within strings.
tags:
    - rust
    - api-reference
    - string-pattern
    - char-searcher
    - nightly-api
category: api
---

[std](https://doc.rust-lang.org/std/index.html)::[str](https://doc.rust-lang.org/std/str/index.html)::[pattern](https://doc.rust-lang.org/std/str/pattern/index.html)

## Struct CharSearcher

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#368)

```rust
pub struct CharSearcher<'a> { /* private fields */ }
```

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Expand description

Associated type for `<char as Pattern>::Searcher<'a>`.

## Trait Implementations[§](#trait-implementations)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#367)[§](#impl-Clone-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [Clone](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#367)[§](#method.clone)

#### fn [clone](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone)(&self) -&gt; [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

Returns a duplicate of the value. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone)

1.0.0 · [Source](https://doc.rust-lang.org/src/core/clone.rs.html#245-247)[§](#method.clone_from)

#### fn [clone\_from](https://doc.rust-lang.org/std/clone/trait.Clone.html#method.clone_from)(&mut self, source: &Self)

Performs copy-assignment from `source`. [Read more](https://doc.rust-lang.org/std/clone/trait.Clone.html#method.clone_from)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#367)[§](#impl-Debug-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [Debug](https://doc.rust-lang.org/std/fmt/trait.Debug.html "trait std::fmt::Debug") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#367)[§](#method.fmt)

#### fn [fmt](https://doc.rust-lang.org/std/fmt/trait.Debug.html#tymethod.fmt)(&self, f: &mut [Formatter](https://doc.rust-lang.org/std/fmt/struct.Formatter.html "struct std::fmt::Formatter")&lt;'\_&gt;) -&gt; [Result](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result")&lt;[()](https://doc.rust-lang.org/std/primitive.unit.html), [Error](https://doc.rust-lang.org/std/fmt/struct.Error.html "struct std::fmt::Error")&gt;

Formats the value using the given formatter. [Read more](https://doc.rust-lang.org/std/fmt/trait.Debug.html#tymethod.fmt)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#477)[§](#impl-ReverseSearcher%3C'a%3E-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [ReverseSearcher](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html "trait std::str::pattern::ReverseSearcher")&lt;'a&gt; for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#479)[§](#method.next_back)

#### fn [next\_back](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html#tymethod.next_back)(&mut self) -&gt; [SearchStep](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html "enum std::str::pattern::SearchStep")

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Performs the next search step starting from the back. [Read more](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html#tymethod.next_back)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#499)[§](#method.next_match_back)

#### fn [next\_match\_back](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html#method.next_match_back)(&mut self) -&gt; [Option](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option")&lt;([usize](https://doc.rust-lang.org/std/primitive.usize.html), [usize](https://doc.rust-lang.org/std/primitive.usize.html))&gt;

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Finds the next [`Match`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Match "variant std::str::pattern::SearchStep::Match") result. See [`next_back()`](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html#tymethod.next_back "method std::str::pattern::ReverseSearcher::next_back").

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#328)[§](#method.next_reject_back)

#### fn [next\_reject\_back](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html#method.next_reject_back)(&mut self) -&gt; [Option](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option")&lt;([usize](https://doc.rust-lang.org/std/primitive.usize.html), [usize](https://doc.rust-lang.org/std/primitive.usize.html))&gt;

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Finds the next [`Reject`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Reject "variant std::str::pattern::SearchStep::Reject") result. See [`next_back()`](https://doc.rust-lang.org/std/str/pattern/trait.ReverseSearcher.html#tymethod.next_back "method std::str::pattern::ReverseSearcher::next_back").

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#399)[§](#impl-Searcher%3C'a%3E-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [Searcher](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html "trait std::str::pattern::Searcher")&lt;'a&gt; for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#401)[§](#method.haystack)

#### fn [haystack](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#tymethod.haystack)(&self) -&gt; &'a [str](https://doc.rust-lang.org/std/primitive.str.html)

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Getter for the underlying string to be searched in [Read more](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#tymethod.haystack)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#405)[§](#method.next)

#### fn [next](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#tymethod.next)(&mut self) -&gt; [SearchStep](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html "enum std::str::pattern::SearchStep")

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Performs the next search step starting from the front. [Read more](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#tymethod.next)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#432)[§](#method.next_match)

#### fn [next\_match](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#method.next_match)(&mut self) -&gt; [Option](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option")&lt;([usize](https://doc.rust-lang.org/std/primitive.usize.html), [usize](https://doc.rust-lang.org/std/primitive.usize.html))&gt;

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Finds the next [`Match`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Match "variant std::str::pattern::SearchStep::Match") result. See [`next()`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#tymethod.next "method std::str::pattern::Searcher::next"). [Read more](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#method.next_match)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#263)[§](#method.next_reject)

#### fn [next\_reject](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#method.next_reject)(&mut self) -&gt; [Option](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option")&lt;([usize](https://doc.rust-lang.org/std/primitive.usize.html), [usize](https://doc.rust-lang.org/std/primitive.usize.html))&gt;

🔬This is a nightly-only experimental API. (`pattern` [#27721](https://github.com/rust-lang/rust/issues/27721))

Finds the next [`Reject`](https://doc.rust-lang.org/std/str/pattern/enum.SearchStep.html#variant.Reject "variant std::str::pattern::SearchStep::Reject") result. See [`next()`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#tymethod.next "method std::str::pattern::Searcher::next") and [`next_match()`](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#method.next_match "method std::str::pattern::Searcher::next_match"). [Read more](https://doc.rust-lang.org/std/str/pattern/trait.Searcher.html#method.next_reject)

[Source](https://doc.rust-lang.org/src/core/str/pattern.rs.html#551)[§](#impl-DoubleEndedSearcher%3C'a%3E-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [DoubleEndedSearcher](https://doc.rust-lang.org/std/str/pattern/trait.DoubleEndedSearcher.html "trait std::str::pattern::DoubleEndedSearcher")&lt;'a&gt; for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

## Auto Trait Implementations[§](#synthetic-implementations)

[§](#impl-Freeze-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [Freeze](https://doc.rust-lang.org/std/marker/trait.Freeze.html "trait std::marker::Freeze") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[§](#impl-RefUnwindSafe-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [RefUnwindSafe](https://doc.rust-lang.org/std/panic/trait.RefUnwindSafe.html "trait std::panic::RefUnwindSafe") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[§](#impl-Send-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [Send](https://doc.rust-lang.org/std/marker/trait.Send.html "trait std::marker::Send") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[§](#impl-Sync-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [Sync](https://doc.rust-lang.org/std/marker/trait.Sync.html "trait std::marker::Sync") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[§](#impl-Unpin-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [Unpin](https://doc.rust-lang.org/std/marker/trait.Unpin.html "trait std::marker::Unpin") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[§](#impl-UnsafeUnpin-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [UnsafeUnpin](https://doc.rust-lang.org/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

[§](#impl-UnwindSafe-for-CharSearcher%3C'a%3E)

### impl&lt;'a&gt; [UnwindSafe](https://doc.rust-lang.org/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe") for [CharSearcher](https://doc.rust-lang.org/std/str/pattern/struct.CharSearcher.html "struct std::str::pattern::CharSearcher")&lt;'a&gt;

## Blanket Implementations[§](#blanket-implementations)

[Source](https://doc.rust-lang.org/src/core/any.rs.html#141)[§](#impl-Any-for-T)

### impl&lt;T&gt; [Any](https://doc.rust-lang.org/std/any/trait.Any.html "trait std::any::Any") for T where T: 'static + ?[Sized](https://doc.rust-lang.org/std/marker/trait.Sized.html "trait std::marker::Sized"),

[Source](https://doc.rust-lang.org/src/core/any.rs.html#142)[§](#method.type_id)

#### fn [type\_id](https://doc.rust-lang.org/std/any/trait.Any.html#tymethod.type_id)(&self) -&gt; [TypeId](https://doc.rust-lang.org/std/any/struct.TypeId.html "struct std::any::TypeId")

Gets the `TypeId` of `self`. [Read more](https://doc.rust-lang.org/std/any/trait.Any.html#tymethod.type_id)

[Source](https://doc.rust-lang.org/src/core/borrow.rs.html#212)[§](#impl-Borrow%3CT%3E-for-T)

### impl&lt;T&gt; [Borrow](https://doc.rust-lang.org/std/borrow/trait.Borrow.html "trait std::borrow::Borrow")&lt;T&gt; for T where T: ?[Sized](https://doc.rust-lang.org/std/marker/trait.Sized.html "trait std::marker::Sized"),

[Source](https://doc.rust-lang.org/src/core/borrow.rs.html#214)[§](#method.borrow)

#### fn [borrow](https://doc.rust-lang.org/std/borrow/trait.Borrow.html#tymethod.borrow)(&self) -&gt; [&T](https://doc.rust-lang.org/std/primitive.reference.html)

Immutably borrows from an owned value. [Read more](https://doc.rust-lang.org/std/borrow/trait.Borrow.html#tymethod.borrow)

[Source](https://doc.rust-lang.org/src/core/borrow.rs.html#221)[§](#impl-BorrowMut%3CT%3E-for-T)

### impl&lt;T&gt; [BorrowMut](https://doc.rust-lang.org/std/borrow/trait.BorrowMut.html "trait std::borrow::BorrowMut")&lt;T&gt; for T where T: ?[Sized](https://doc.rust-lang.org/std/marker/trait.Sized.html "trait std::marker::Sized"),

[Source](https://doc.rust-lang.org/src/core/borrow.rs.html#222)[§](#method.borrow_mut)

#### fn [borrow\_mut](https://doc.rust-lang.org/std/borrow/trait.BorrowMut.html#tymethod.borrow_mut)(&mut self) -&gt; [&mut T](https://doc.rust-lang.org/std/primitive.reference.html)

Mutably borrows from an owned value. [Read more](https://doc.rust-lang.org/std/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#547)[§](#impl-CloneToUninit-for-T)

### impl&lt;T&gt; [CloneToUninit](https://doc.rust-lang.org/std/clone/trait.CloneToUninit.html "trait std::clone::CloneToUninit") for T where T: [Clone](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone"),

[Source](https://doc.rust-lang.org/src/core/clone.rs.html#549)[§](#method.clone_to_uninit)

#### unsafe fn [clone\_to\_uninit](https://doc.rust-lang.org/std/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)(&self, dest: [\*mut](https://doc.rust-lang.org/std/primitive.pointer.html) [u8](https://doc.rust-lang.org/std/primitive.u8.html))

🔬This is a nightly-only experimental API. (`clone_to_uninit` [#126799](https://github.com/rust-lang/rust/issues/126799))

Performs copy-assignment from `self` to `dest`. [Read more](https://doc.rust-lang.org/std/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#785)[§](#impl-From%3CT%3E-for-T)

### impl&lt;T&gt; [From](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From")&lt;T&gt; for T

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#788)[§](#method.from)

#### fn [from](https://doc.rust-lang.org/std/convert/trait.From.html#tymethod.from)(t: T) -&gt; T

Returns the argument unchanged.

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#767-769)[§](#impl-Into%3CU%3E-for-T)

### impl&lt;T, U&gt; [Into](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into")&lt;U&gt; for T where U: [From](https://doc.rust-lang.org/std/convert/trait.From.html "trait std::convert::From")&lt;T&gt;,

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#777)[§](#method.into)

#### fn [into](https://doc.rust-lang.org/std/convert/trait.Into.html#tymethod.into)(self) -&gt; U

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of `From<T> for U` chooses to do.

[Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#72-74)[§](#impl-ToOwned-for-T)

### impl&lt;T&gt; [ToOwned](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html "trait std::borrow::ToOwned") for T where T: [Clone](https://doc.rust-lang.org/std/clone/trait.Clone.html "trait std::clone::Clone"),

[Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#76)[§](#associatedtype.Owned)

#### type [Owned](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#associatedtype.Owned) = T

The resulting type after obtaining ownership.

[Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#77)[§](#method.to_owned)

#### fn [to\_owned](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#tymethod.to_owned)(&self) -&gt; T

Creates owned data from borrowed data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#tymethod.to_owned)

[Source](https://doc.rust-lang.org/src/alloc/borrow.rs.html#81)[§](#method.clone_into)

#### fn [clone\_into](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#method.clone_into)(&self, target: [&mut T](https://doc.rust-lang.org/std/primitive.reference.html))

Uses borrowed data to replace owned data, usually by cloning. [Read more](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#method.clone_into)

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#827-829)[§](#impl-TryFrom%3CU%3E-for-T)

### impl&lt;T, U&gt; [TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;U&gt; for T where U: [Into](https://doc.rust-lang.org/std/convert/trait.Into.html "trait std::convert::Into")&lt;T&gt;,

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#831)[§](#associatedtype.Error-1)

#### type [Error](https://doc.rust-lang.org/std/convert/trait.TryFrom.html#associatedtype.Error) = [Infallible](https://doc.rust-lang.org/std/convert/enum.Infallible.html "enum std::convert::Infallible")

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#834)[§](#method.try_from)

#### fn [try\_from](https://doc.rust-lang.org/std/convert/trait.TryFrom.html#tymethod.try_from)(value: U) -&gt; [Result](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result")&lt;T, &lt;T as [TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;U&gt;&gt;::[Error](https://doc.rust-lang.org/std/convert/trait.TryFrom.html#associatedtype.Error "type std::convert::TryFrom::Error")&gt;

Performs the conversion.

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#811-813)[§](#impl-TryInto%3CU%3E-for-T)

### impl&lt;T, U&gt; [TryInto](https://doc.rust-lang.org/std/convert/trait.TryInto.html "trait std::convert::TryInto")&lt;U&gt; for T where U: [TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;T&gt;,

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#815)[§](#associatedtype.Error)

#### type [Error](https://doc.rust-lang.org/std/convert/trait.TryInto.html#associatedtype.Error) = &lt;U as [TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;T&gt;&gt;::[Error](https://doc.rust-lang.org/std/convert/trait.TryFrom.html#associatedtype.Error "type std::convert::TryFrom::Error")

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/src/core/convert/mod.rs.html#818)[§](#method.try_into)

#### fn [try\_into](https://doc.rust-lang.org/std/convert/trait.TryInto.html#tymethod.try_into)(self) -&gt; [Result](https://doc.rust-lang.org/std/result/enum.Result.html "enum std::result::Result")&lt;U, &lt;U as [TryFrom](https://doc.rust-lang.org/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;T&gt;&gt;::[Error](https://doc.rust-lang.org/std/convert/trait.TryFrom.html#associatedtype.Error "type std::convert::TryFrom::Error")&gt;

Performs the conversion.