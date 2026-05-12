---
title: std::prelude - Rust
url: https://doc.rust-lang.org/std/prelude/index.html#other-preludes
source: crawler
fetched_at: 2026-05-06T21:21:48.984923755-03:00
rendered_js: false
word_count: 517
summary: This document explains the purpose and content of the Rust standard library prelude, which automatically imports essential traits and types into every program.
tags:
    - rust
    - standard-library
    - prelude
    - language-features
    - imports
    - programming-concepts
category: concept
---

## Module prelude

1.0.0 · [Source](https://doc.rust-lang.org/src/std/prelude/mod.rs.html#1-192)

Expand description

Rust comes with a variety of things in its standard library. However, if you had to manually import every single thing that you used, it would be very verbose. But importing a lot of things that a program never uses isn’t good either. A balance needs to be struck.

The *prelude* is the list of things that Rust automatically imports into every Rust program. It’s kept as small as possible, and is focused on things, particularly traits, which are used in almost every single Rust program.

## [§](#other-preludes)Other preludes

Preludes can be seen as a pattern to make using multiple types more convenient. As such, you’ll find other preludes in the standard library, such as [`std::io::prelude`](https://doc.rust-lang.org/std/io/prelude/index.html "mod std::io::prelude"). Various libraries in the Rust ecosystem may also define their own preludes.

The difference between ‘the prelude’ and these other preludes is that they are not automatically `use`’d, and must be imported manually. This is still easier than importing all of their constituent components.

## [§](#prelude-contents)Prelude contents

The items included in the prelude depend on the edition of the crate. The first version of the prelude is used in Rust 2015 and Rust 2018, and lives in [`std::prelude::v1`](https://doc.rust-lang.org/std/prelude/v1/index.html "mod std::prelude::v1"). [`std::prelude::rust_2015`](https://doc.rust-lang.org/std/prelude/rust_2015/index.html "mod std::prelude::rust_2015") and [`std::prelude::rust_2018`](https://doc.rust-lang.org/std/prelude/rust_2018/index.html "mod std::prelude::rust_2018") re-export this prelude. It re-exports the following:

- `std::marker::{Copy, Send, Sized, Sync, Unpin}`, marker traits that indicate fundamental properties of types.
- `std::ops::{Fn, FnMut, FnOnce}`, and their analogous async traits, `std::ops::{AsyncFn, AsyncFnMut, AsyncFnOnce}`.
- `std::ops::Drop`, for implementing destructors.
- `std::mem::drop`, a convenience function for explicitly dropping a value.
- `std::mem::{size_of, size_of_val}`, to get the size of a type or value.
- `std::mem::{align_of, align_of_val}`, to get the alignment of a type or value.
- `std::boxed::Box`, a way to allocate values on the heap.
- `std::borrow::ToOwned`, the conversion trait that defines [`to_owned`](https://doc.rust-lang.org/std/borrow/trait.ToOwned.html#tymethod.to_owned "method std::borrow::ToOwned::to_owned"), the generic method for creating an owned type from a borrowed type.
- `std::clone::Clone`, the ubiquitous trait that defines [`clone`](https://doc.rust-lang.org/std/clone/trait.Clone.html#tymethod.clone "method std::clone::Clone::clone"), the method for producing a copy of a value.
- `std::cmp::{PartialEq, PartialOrd, Eq, Ord}`, the comparison traits, which implement the comparison operators and are often seen in trait bounds.
- `std::convert::{AsRef, AsMut, Into, From}`, generic conversions, used by savvy API authors to create overloaded methods.
- `std::default::Default`, types that have default values.
- `std::iter::{Iterator, Extend, IntoIterator, DoubleEndedIterator, ExactSizeIterator}`, iterators of various kinds.
- Most of the standard macros.
- `std::option::Option::{self, Some, None}`, a type which expresses the presence or absence of a value. This type is so commonly used, its variants are also exported.
- `std::result::Result::{self, Ok, Err}`, a type for functions that may succeed or fail. Like [`Option`](https://doc.rust-lang.org/std/option/enum.Option.html "enum std::option::Option"), its variants are exported as well.
- `std::string::{String, ToString}`, heap-allocated strings.
- `std::vec::Vec`, a growable, heap-allocated vector.

The prelude used in Rust 2021, [`std::prelude::rust_2021`](https://doc.rust-lang.org/std/prelude/rust_2021/index.html "mod std::prelude::rust_2021"), includes all of the above, and in addition re-exports:

- `std::convert::{TryFrom, TryInto}`.
- `std::iter::FromIterator`.

The prelude used in Rust 2024, [`std::prelude::rust_2024`](https://doc.rust-lang.org/std/prelude/rust_2024/index.html "mod std::prelude::rust_2024"), includes all of the above, and in addition re-exports:

- `std::future::{Future, IntoFuture}`.

[rust\_2015](https://doc.rust-lang.org/std/prelude/rust_2015/index.html "mod std::prelude::rust_2015")

The 2015 version of the prelude of The Rust Standard Library.

[rust\_2018](https://doc.rust-lang.org/std/prelude/rust_2018/index.html "mod std::prelude::rust_2018")

The 2018 version of the prelude of The Rust Standard Library.

[rust\_2021](https://doc.rust-lang.org/std/prelude/rust_2021/index.html "mod std::prelude::rust_2021")

The 2021 version of the prelude of The Rust Standard Library.

[rust\_2024](https://doc.rust-lang.org/std/prelude/rust_2024/index.html "mod std::prelude::rust_2024")

The 2024 version of the prelude of The Rust Standard Library.

[v1](https://doc.rust-lang.org/std/prelude/v1/index.html "mod std::prelude::v1")

The first version of the prelude of The Rust Standard Library.