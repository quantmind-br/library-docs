---
title: mod.rs - source
url: https://doc.rust-lang.org/src/std/prelude/mod.rs.html#1-192
source: crawler
fetched_at: 2026-05-06T21:24:39.405072741-03:00
rendered_js: false
word_count: 1051
summary: This document explains the Rust prelude, which is a collection of essential traits and types that are automatically imported into every Rust program to streamline development.
tags:
    - rust
    - prelude
    - standard-library
    - imports
    - language-features
category: concept
---

## std/prelude/ mod.rs

```rust
1//! # The Rust Prelude
2//!
3//! Rust comes with a variety of things in its standard library. However, if
4//! you had to manually import every single thing that you used, it would be
5//! very verbose. But importing a lot of things that a program never uses isn't
6//! good either. A balance needs to be struck.
7//!
8//! The *prelude* is the list of things that Rust automatically imports into
9//! every Rust program. It's kept as small as possible, and is focused on
10//! things, particularly traits, which are used in almost every single Rust
11//! program.
12//!
13//! # Other preludes
14//!
15//! Preludes can be seen as a pattern to make using multiple types more
16//! convenient. As such, you'll find other preludes in the standard library,
17//! such as [`std::io::prelude`]. Various libraries in the Rust ecosystem may
18//! also define their own preludes.
19//!
20//! [`std::io::prelude`]: crate::io::prelude
21//!
22//! The difference between 'the prelude' and these other preludes is that they
23//! are not automatically `use`'d, and must be imported manually. This is still
24//! easier than importing all of their constituent components.
25//!
26//! # Prelude contents
27//!
28//! The items included in the prelude depend on the edition of the crate.
29//! The first version of the prelude is used in Rust 2015 and Rust 2018,
30//! and lives in [`std::prelude::v1`].
31//! [`std::prelude::rust_2015`] and [`std::prelude::rust_2018`] re-export this prelude.
32//! It re-exports the following:
33//!
34//! * <code>[std::marker]::{[Copy], [Send], [Sized], [Sync], [Unpin]}</code>,
35//!   marker traits that indicate fundamental properties of types.
36//! * <code>[std::ops]::{[Fn], [FnMut], [FnOnce]}</code>, and their analogous
37//!   async traits, <code>[std::ops]::{[AsyncFn], [AsyncFnMut], [AsyncFnOnce]}</code>.
38//! * <code>[std::ops]::[Drop]</code>, for implementing destructors.
39//! * <code>[std::mem]::[drop]</code>, a convenience function for explicitly
40//!   dropping a value.
41//! * <code>[std::mem]::{[size_of], [size_of_val]}</code>, to get the size of
42//!   a type or value.
43//! * <code>[std::mem]::{[align_of], [align_of_val]}</code>, to get the
44//!   alignment of a type or value.
45//! * <code>[std::boxed]::[Box]</code>, a way to allocate values on the heap.
46//! * <code>[std::borrow]::[ToOwned]</code>, the conversion trait that defines
47//!   [`to_owned`], the generic method for creating an owned type from a
48//!   borrowed type.
49//! * <code>[std::clone]::[Clone]</code>, the ubiquitous trait that defines
50//!   [`clone`][Clone::clone], the method for producing a copy of a value.
51//! * <code>[std::cmp]::{[PartialEq], [PartialOrd], [Eq], [Ord]}</code>, the
52//!   comparison traits, which implement the comparison operators and are often
53//!   seen in trait bounds.
54//! * <code>[std::convert]::{[AsRef], [AsMut], [Into], [From]}</code>, generic
55//!   conversions, used by savvy API authors to create overloaded methods.
56//! * <code>[std::default]::[Default]</code>, types that have default values.
57//! * <code>[std::iter]::{[Iterator], [Extend], [IntoIterator], [DoubleEndedIterator],
58//!   [ExactSizeIterator]}</code>, iterators of various kinds.
59//! * Most of the standard macros.
60//! * <code>[std::option]::[Option]::{[self][Option], [Some], [None]}</code>, a
61//!   type which expresses the presence or absence of a value. This type is so
62//!   commonly used, its variants are also exported.
63//! * <code>[std::result]::[Result]::{[self][Result], [Ok], [Err]}</code>, a type
64//!   for functions that may succeed or fail. Like [`Option`], its variants are
65//!   exported as well.
66//! * <code>[std::string]::{[String], [ToString]}</code>, heap-allocated strings.
67//! * <code>[std::vec]::[Vec]</code>, a growable, heap-allocated vector.
68//!
69//! The prelude used in Rust 2021, [`std::prelude::rust_2021`], includes all of the above,
70//! and in addition re-exports:
71//!
72//! * <code>[std::convert]::{[TryFrom], [TryInto]}</code>.
73//! * <code>[std::iter]::[FromIterator]</code>.
74//!
75//! The prelude used in Rust 2024, [`std::prelude::rust_2024`], includes all of the above,
76//! and in addition re-exports:
77//!
78//! * <code>[std::future]::{[Future], [IntoFuture]}</code>.
79//!
80//! [std::borrow]: crate::borrow
81//! [std::boxed]: crate::boxed
82//! [std::clone]: crate::clone
83//! [std::cmp]: crate::cmp
84//! [std::convert]: crate::convert
85//! [std::default]: crate::default
86//! [std::future]: crate::future
87//! [std::iter]: crate::iter
88//! [std::marker]: crate::marker
89//! [std::mem]: crate::mem
90//! [std::ops]: crate::ops
91//! [std::option]: crate::option
92//! [`std::prelude::v1`]: v1
93//! [`std::prelude::rust_2015`]: rust_2015
94//! [`std::prelude::rust_2018`]: rust_2018
95//! [`std::prelude::rust_2021`]: rust_2021
96//! [`std::prelude::rust_2024`]: rust_2024
97//! [std::result]: crate::result
98//! [std::slice]: crate::slice
99//! [std::string]: crate::string
100//! [std::vec]: mod@crate::vec
101//! [`to_owned`]: crate::borrow::ToOwned::to_owned
102//! [book-closures]: ../../book/ch13-01-closures.html
103//! [book-dtor]: ../../book/ch15-03-drop.html
104//! [book-enums]: ../../book/ch06-01-defining-an-enum.html
105//! [book-iter]: ../../book/ch13-02-iterators.html
106//! [Future]: crate::future::Future
107//! [IntoFuture]: crate::future::IntoFuture
108
109// No formatting: this file is nothing but re-exports, and their order is worth preserving.
110#![cfg_attr(rustfmt, rustfmt::skip)]
111
112#![stable(feature = "rust1", since = "1.0.0")]
113
114pub mod v1;
115
116/// The 2015 version of the prelude of The Rust Standard Library.
117///
118/// See the [module-level documentation](self) for more.
119#[stable(feature = "prelude_2015", since = "1.55.0")]
120pub mod rust_2015 {
121    #[stable(feature = "prelude_2015", since = "1.55.0")]
122    #[doc(no_inline)]
123    pub use super::v1::*;
124}
125
126/// The 2018 version of the prelude of The Rust Standard Library.
127///
128/// See the [module-level documentation](self) for more.
129#[stable(feature = "prelude_2018", since = "1.55.0")]
130pub mod rust_2018 {
131    #[stable(feature = "prelude_2018", since = "1.55.0")]
132    #[doc(no_inline)]
133    pub use super::v1::*;
134}
135
136/// The 2021 version of the prelude of The Rust Standard Library.
137///
138/// See the [module-level documentation](self) for more.
139#[stable(feature = "prelude_2021", since = "1.55.0")]
140pub mod rust_2021 {
141    #[stable(feature = "prelude_2021", since = "1.55.0")]
142    #[doc(no_inline)]
143    pub use super::v1::*;
144
145    #[stable(feature = "prelude_2021", since = "1.55.0")]
146    #[doc(no_inline)]
147    pub use core::prelude::rust_2021::*;
148
149    // There are two different panic macros, one in `core` and one in `std`. They are slightly
150    // different. For `std` we explicitly want the one defined in `std`.
151    #[stable(feature = "prelude_2021", since = "1.55.0")]
152    pub use super::v1::panic;
153}
154
155/// The 2024 version of the prelude of The Rust Standard Library.
156///
157/// See the [module-level documentation](self) for more.
158#[stable(feature = "prelude_2024", since = "1.85.0")]
159pub mod rust_2024 {
160    #[stable(feature = "rust1", since = "1.0.0")]
161    #[doc(no_inline)]
162    pub use super::v1::*;
163
164    #[stable(feature = "prelude_2024", since = "1.85.0")]
165    #[doc(no_inline)]
166    pub use core::prelude::rust_2024::*;
167
168    // There are two different panic macros, one in `core` and one in `std`. They are slightly
169    // different. For `std` we explicitly want the one defined in `std`.
170    #[stable(feature = "prelude_2024", since = "1.85.0")]
171    pub use super::v1::panic;
172}
173
174/// The Future version of the prelude of The Rust Standard Library.
175///
176/// See the [module-level documentation](self) for more.
177#[doc(hidden)]
178#[unstable(feature = "prelude_future", issue = "none")]
179pub mod rust_future {
180    #[stable(feature = "rust1", since = "1.0.0")]
181    #[doc(no_inline)]
182    pub use super::v1::*;
183
184    #[unstable(feature = "prelude_next", issue = "none")]
185    #[doc(no_inline)]
186    pub use core::prelude::rust_future::*;
187
188    // There are two different panic macros, one in `core` and one in `std`. They are slightly
189    // different. For `std` we explicitly want the one defined in `std`.
190    #[unstable(feature = "prelude_next", issue = "none")]
191    pub use super::v1::panic;
192}
```