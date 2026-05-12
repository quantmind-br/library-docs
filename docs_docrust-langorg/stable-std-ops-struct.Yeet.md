---
title: Yeet in std::ops - Rust
url: https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html
source: crawler
fetched_at: 2026-05-06T21:26:04.255150534-03:00
rendered_js: false
word_count: 381
summary: The Yeet struct is an experimental Rust API that facilitates early returns in functions by implementing the FromResidual trait to support the do yeet syntax.
tags:
    - rust
    - nightly-api
    - error-handling
    - try-trait
    - yeet
    - control-flow
category: api
---

[std](https://doc.rust-lang.org/stable/std/index.html)::[ops](https://doc.rust-lang.org/stable/std/ops/index.html)

## Struct Yeet

[Source](https://doc.rust-lang.org/stable/src/core/ops/try_trait.rs.html#473)

```rust
pub struct Yeet<T>(pub T);
```

🔬This is a nightly-only experimental API. (`try_trait_v2_yeet` [#96374](https://github.com/rust-lang/rust/issues/96374))

Expand description

Implement `FromResidual<Yeet<T>>` on your type to enable `do yeet expr` syntax in functions returning your type.

## Tuple Fields[§](#fields)

[§](#structfield.0)`0: T`

🔬This is a nightly-only experimental API. (`try_trait_v2_yeet` [#96374](https://github.com/rust-lang/rust/issues/96374))

## Trait Implementations[§](#trait-implementations)

[Source](https://doc.rust-lang.org/stable/src/core/ops/try_trait.rs.html#472)[§](#impl-Debug-for-Yeet%3CT%3E)

### impl&lt;T&gt; [Debug](https://doc.rust-lang.org/stable/std/fmt/trait.Debug.html "trait std::fmt::Debug") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [Debug](https://doc.rust-lang.org/stable/std/fmt/trait.Debug.html "trait std::fmt::Debug"),

[Source](https://doc.rust-lang.org/stable/src/core/ops/try_trait.rs.html#472)[§](#method.fmt)

#### fn [fmt](https://doc.rust-lang.org/stable/std/fmt/trait.Debug.html#tymethod.fmt)(&self, f: &mut [Formatter](https://doc.rust-lang.org/stable/std/fmt/struct.Formatter.html "struct std::fmt::Formatter")&lt;'\_&gt;) -&gt; [Result](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result")&lt;[()](https://doc.rust-lang.org/stable/std/primitive.unit.html), [Error](https://doc.rust-lang.org/stable/std/fmt/struct.Error.html "struct std::fmt::Error")&gt;

Formats the value using the given formatter. [Read more](https://doc.rust-lang.org/stable/std/fmt/trait.Debug.html#tymethod.fmt)

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2789)[§](#impl-FromResidual%3CYeet%3C%28%29%3E%3E-for-Option%3CT%3E)

### impl&lt;T&gt; [FromResidual](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html "trait std::ops::FromResidual")&lt;[Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;[()](https://doc.rust-lang.org/stable/std/primitive.unit.html)&gt;&gt; for [Option](https://doc.rust-lang.org/stable/std/option/enum.Option.html "enum std::option::Option")&lt;T&gt;

[Source](https://doc.rust-lang.org/stable/src/core/option.rs.html#2791)[§](#method.from_residual)

#### fn [from\_residual](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html#tymethod.from_residual)(\_: [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;[()](https://doc.rust-lang.org/stable/std/primitive.unit.html)&gt;) -&gt; [Option](https://doc.rust-lang.org/stable/std/option/enum.Option.html "enum std::option::Option")&lt;T&gt;

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from a compatible `Residual` type. [Read more](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html#tymethod.from_residual)

[Source](https://doc.rust-lang.org/stable/src/core/result.rs.html#2196)[§](#impl-FromResidual%3CYeet%3CE%3E%3E-for-Result%3CT,+F%3E)

### impl&lt;T, E, F&gt; [FromResidual](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html "trait std::ops::FromResidual")&lt;[Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;E&gt;&gt; for [Result](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result")&lt;T, F&gt; where F: [From](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From")&lt;E&gt;,

[Source](https://doc.rust-lang.org/stable/src/core/result.rs.html#2198)[§](#method.from_residual-1)

#### fn [from\_residual](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html#tymethod.from_residual)(\_: [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;E&gt;) -&gt; [Result](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result")&lt;T, F&gt;

🔬This is a nightly-only experimental API. (`try_trait_v2` [#84277](https://github.com/rust-lang/rust/issues/84277))

Constructs the type from a compatible `Residual` type. [Read more](https://doc.rust-lang.org/stable/std/ops/trait.FromResidual.html#tymethod.from_residual)

## Auto Trait Implementations[§](#synthetic-implementations)

[§](#impl-Freeze-for-Yeet%3CT%3E)

### impl&lt;T&gt; [Freeze](https://doc.rust-lang.org/stable/std/marker/trait.Freeze.html "trait std::marker::Freeze") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [Freeze](https://doc.rust-lang.org/stable/std/marker/trait.Freeze.html "trait std::marker::Freeze"),

[§](#impl-RefUnwindSafe-for-Yeet%3CT%3E)

### impl&lt;T&gt; [RefUnwindSafe](https://doc.rust-lang.org/stable/std/panic/trait.RefUnwindSafe.html "trait std::panic::RefUnwindSafe") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [RefUnwindSafe](https://doc.rust-lang.org/stable/std/panic/trait.RefUnwindSafe.html "trait std::panic::RefUnwindSafe"),

[§](#impl-Send-for-Yeet%3CT%3E)

### impl&lt;T&gt; [Send](https://doc.rust-lang.org/stable/std/marker/trait.Send.html "trait std::marker::Send") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [Send](https://doc.rust-lang.org/stable/std/marker/trait.Send.html "trait std::marker::Send"),

[§](#impl-Sync-for-Yeet%3CT%3E)

### impl&lt;T&gt; [Sync](https://doc.rust-lang.org/stable/std/marker/trait.Sync.html "trait std::marker::Sync") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [Sync](https://doc.rust-lang.org/stable/std/marker/trait.Sync.html "trait std::marker::Sync"),

[§](#impl-Unpin-for-Yeet%3CT%3E)

### impl&lt;T&gt; [Unpin](https://doc.rust-lang.org/stable/std/marker/trait.Unpin.html "trait std::marker::Unpin") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [Unpin](https://doc.rust-lang.org/stable/std/marker/trait.Unpin.html "trait std::marker::Unpin"),

[§](#impl-UnsafeUnpin-for-Yeet%3CT%3E)

### impl&lt;T&gt; [UnsafeUnpin](https://doc.rust-lang.org/stable/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [UnsafeUnpin](https://doc.rust-lang.org/stable/std/marker/trait.UnsafeUnpin.html "trait std::marker::UnsafeUnpin"),

[§](#impl-UnwindSafe-for-Yeet%3CT%3E)

### impl&lt;T&gt; [UnwindSafe](https://doc.rust-lang.org/stable/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe") for [Yeet](https://doc.rust-lang.org/stable/std/ops/struct.Yeet.html "struct std::ops::Yeet")&lt;T&gt; where T: [UnwindSafe](https://doc.rust-lang.org/stable/std/panic/trait.UnwindSafe.html "trait std::panic::UnwindSafe"),

## Blanket Implementations[§](#blanket-implementations)

[Source](https://doc.rust-lang.org/stable/src/core/any.rs.html#141)[§](#impl-Any-for-T)

### impl&lt;T&gt; [Any](https://doc.rust-lang.org/stable/std/any/trait.Any.html "trait std::any::Any") for T where T: 'static + ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized"),

[Source](https://doc.rust-lang.org/stable/src/core/any.rs.html#142)[§](#method.type_id)

#### fn [type\_id](https://doc.rust-lang.org/stable/std/any/trait.Any.html#tymethod.type_id)(&self) -&gt; [TypeId](https://doc.rust-lang.org/stable/std/any/struct.TypeId.html "struct std::any::TypeId")

Gets the `TypeId` of `self`. [Read more](https://doc.rust-lang.org/stable/std/any/trait.Any.html#tymethod.type_id)

[Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#212)[§](#impl-Borrow%3CT%3E-for-T)

### impl&lt;T&gt; [Borrow](https://doc.rust-lang.org/stable/std/borrow/trait.Borrow.html "trait std::borrow::Borrow")&lt;T&gt; for T where T: ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized"),

[Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#214)[§](#method.borrow)

#### fn [borrow](https://doc.rust-lang.org/stable/std/borrow/trait.Borrow.html#tymethod.borrow)(&self) -&gt; [&T](https://doc.rust-lang.org/stable/std/primitive.reference.html)

Immutably borrows from an owned value. [Read more](https://doc.rust-lang.org/stable/std/borrow/trait.Borrow.html#tymethod.borrow)

[Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#221)[§](#impl-BorrowMut%3CT%3E-for-T)

### impl&lt;T&gt; [BorrowMut](https://doc.rust-lang.org/stable/std/borrow/trait.BorrowMut.html "trait std::borrow::BorrowMut")&lt;T&gt; for T where T: ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized"),

[Source](https://doc.rust-lang.org/stable/src/core/borrow.rs.html#222)[§](#method.borrow_mut)

#### fn [borrow\_mut](https://doc.rust-lang.org/stable/std/borrow/trait.BorrowMut.html#tymethod.borrow_mut)(&mut self) -&gt; [&mut T](https://doc.rust-lang.org/stable/std/primitive.reference.html)

Mutably borrows from an owned value. [Read more](https://doc.rust-lang.org/stable/std/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#785)[§](#impl-From%3CT%3E-for-T)

### impl&lt;T&gt; [From](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From")&lt;T&gt; for T

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#788)[§](#method.from)

#### fn [from](https://doc.rust-lang.org/stable/std/convert/trait.From.html#tymethod.from)(t: T) -&gt; T

Returns the argument unchanged.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#767-769)[§](#impl-Into%3CU%3E-for-T)

### impl&lt;T, U&gt; [Into](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into")&lt;U&gt; for T where U: [From](https://doc.rust-lang.org/stable/std/convert/trait.From.html "trait std::convert::From")&lt;T&gt;,

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#777)[§](#method.into)

#### fn [into](https://doc.rust-lang.org/stable/std/convert/trait.Into.html#tymethod.into)(self) -&gt; U

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of `From<T> for U` chooses to do.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#827-829)[§](#impl-TryFrom%3CU%3E-for-T)

### impl&lt;T, U&gt; [TryFrom](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;U&gt; for T where U: [Into](https://doc.rust-lang.org/stable/std/convert/trait.Into.html "trait std::convert::Into")&lt;T&gt;,

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#831)[§](#associatedtype.Error-1)

#### type [Error](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html#associatedtype.Error) = [Infallible](https://doc.rust-lang.org/stable/std/convert/enum.Infallible.html "enum std::convert::Infallible")

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#834)[§](#method.try_from)

#### fn [try\_from](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html#tymethod.try_from)(value: U) -&gt; [Result](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result")&lt;T, &lt;T as [TryFrom](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;U&gt;&gt;::[Error](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html#associatedtype.Error "type std::convert::TryFrom::Error")&gt;

Performs the conversion.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#811-813)[§](#impl-TryInto%3CU%3E-for-T)

### impl&lt;T, U&gt; [TryInto](https://doc.rust-lang.org/stable/std/convert/trait.TryInto.html "trait std::convert::TryInto")&lt;U&gt; for T where U: [TryFrom](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;T&gt;,

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#815)[§](#associatedtype.Error)

#### type [Error](https://doc.rust-lang.org/stable/std/convert/trait.TryInto.html#associatedtype.Error) = &lt;U as [TryFrom](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;T&gt;&gt;::[Error](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html#associatedtype.Error "type std::convert::TryFrom::Error")

The type returned in the event of a conversion error.

[Source](https://doc.rust-lang.org/stable/src/core/convert/mod.rs.html#818)[§](#method.try_into)

#### fn [try\_into](https://doc.rust-lang.org/stable/std/convert/trait.TryInto.html#tymethod.try_into)(self) -&gt; [Result](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result")&lt;U, &lt;U as [TryFrom](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html "trait std::convert::TryFrom")&lt;T&gt;&gt;::[Error](https://doc.rust-lang.org/stable/std/convert/trait.TryFrom.html#associatedtype.Error "type std::convert::TryFrom::Error")&gt;

Performs the conversion.