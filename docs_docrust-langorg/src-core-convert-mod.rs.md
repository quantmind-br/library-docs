---
title: mod.rs - source
url: https://doc.rust-lang.org/src/core/convert/mod.rs.html#811-813
source: crawler
fetched_at: 2026-05-06T21:24:13.705982975-03:00
rendered_js: false
word_count: 4627
summary: This module provides essential Rust traits for type conversions, including standard traits like AsRef, AsMut, From, Into, TryFrom, and TryInto, alongside the identity function for generic programming.
tags:
    - rust
    - type-conversion
    - traits
    - generic-programming
    - language-features
category: reference
---

## core/convert/ mod.rs

````rust
1//! Traits for conversions between types.
2//!
3//! The traits in this module provide a way to convert from one type to another type.
4//! Each trait serves a different purpose:
5//!
6//! - Implement the [`AsRef`] trait for cheap reference-to-reference conversions
7//! - Implement the [`AsMut`] trait for cheap mutable-to-mutable conversions
8//! - Implement the [`From`] trait for consuming value-to-value conversions
9//! - Implement the [`Into`] trait for consuming value-to-value conversions to types
10//!   outside the current crate
11//! - The [`TryFrom`] and [`TryInto`] traits behave like [`From`] and [`Into`],
12//!   but should be implemented when the conversion can fail.
13//!
14//! The traits in this module are often used as trait bounds for generic functions such that to
15//! arguments of multiple types are supported. See the documentation of each trait for examples.
16//!
17//! As a library author, you should always prefer implementing [`From<T>`][`From`] or
18//! [`TryFrom<T>`][`TryFrom`] rather than [`Into<U>`][`Into`] or [`TryInto<U>`][`TryInto`],
19//! as [`From`] and [`TryFrom`] provide greater flexibility and offer
20//! equivalent [`Into`] or [`TryInto`] implementations for free, thanks to a
21//! blanket implementation in the standard library. When targeting a version prior to Rust 1.41, it
22//! may be necessary to implement [`Into`] or [`TryInto`] directly when converting to a type
23//! outside the current crate.
24//!
25//! # Generic Implementations
26//!
27//! - [`AsRef`] and [`AsMut`] auto-dereference if the inner type is a reference
28//!   (but not generally for all [dereferenceable types][core::ops::Deref])
29//! - [`From`]`<U> for T` implies [`Into`]`<T> for U`
30//! - [`TryFrom`]`<U> for T` implies [`TryInto`]`<T> for U`
31//! - [`From`] and [`Into`] are reflexive, which means that all types can
32//!   `into` themselves and `from` themselves
33//!
34//! See each trait for usage examples.
35
36#![stable(feature = "rust1", since = "1.0.0")]
37
38use crate::error::Error;
39use crate::fmt;
40use crate::hash::{Hash, Hasher};
41use crate::marker::PointeeSized;
42
43mod num;
44
45#[unstable(feature = "convert_float_to_int", issue = "67057")]
46pub use num::FloatToInt;
47
48/// The identity function.
49///
50/// Two things are important to note about this function:
51///
52/// - It is not always equivalent to a closure like `|x| x`, since the
53///   closure may coerce `x` into a different type.
54///
55/// - It moves the input `x` passed to the function.
56///
57/// While it might seem strange to have a function that just returns back the
58/// input, there are some interesting uses.
59///
60/// # Examples
61///
62/// Using `identity` to do nothing in a sequence of other, interesting,
63/// functions:
64///
65/// ```rust
66/// use std::convert::identity;
67///
68/// fn manipulation(x: u32) -> u32 {
69///     // Let's pretend that adding one is an interesting function.
70///     x + 1
71/// }
72///
73/// let _arr = &[identity, manipulation];
74/// ```
75///
76/// Using `identity` as a "do nothing" base case in a conditional:
77///
78/// ```rust
79/// use std::convert::identity;
80///
81/// # let condition = true;
82/// #
83/// # fn manipulation(x: u32) -> u32 { x + 1 }
84/// #
85/// let do_stuff = if condition { manipulation } else { identity };
86///
87/// // Do more interesting stuff...
88///
89/// let _results = do_stuff(42);
90/// ```
91///
92/// Using `identity` to keep the `Some` variants of an iterator of `Option<T>`:
93///
94/// ```rust
95/// use std::convert::identity;
96///
97/// let iter = [Some(1), None, Some(3)].into_iter();
98/// let filtered = iter.filter_map(identity).collect::<Vec<_>>();
99/// assert_eq!(vec![1, 3], filtered);
100/// ```
101#[stable(feature = "convert_id", since = "1.33.0")]
102#[rustc_const_stable(feature = "const_identity", since = "1.33.0")]
103#[inline(always)]
104#[rustc_diagnostic_item = "convert_identity"]
105pub const fn identity<T>(x: T) -> T {
106    x
107}
108
109/// Used to do a cheap reference-to-reference conversion.
110///
111/// This trait is similar to [`AsMut`] which is used for converting between mutable references.
112/// If you need to do a costly conversion it is better to implement [`From`] with type
113/// `&T` or write a custom function.
114///
115/// # Relation to `Borrow`
116///
117/// `AsRef` has the same signature as [`Borrow`], but [`Borrow`] is different in a few aspects:
118///
119/// - Unlike `AsRef`, [`Borrow`] has a blanket impl for any `T`, and can be used to accept either
120///   a reference or a value. (See also note on `AsRef`'s reflexibility below.)
121/// - [`Borrow`] also requires that [`Hash`], [`Eq`] and [`Ord`] for a borrowed value are
122///   equivalent to those of the owned value. For this reason, if you want to
123///   borrow only a single field of a struct you can implement `AsRef`, but not [`Borrow`].
124///
125/// **Note: This trait must not fail**. If the conversion can fail, use a
126/// dedicated method which returns an [`Option<T>`] or a [`Result<T, E>`].
127///
128/// # Generic Implementations
129///
130/// `AsRef` auto-dereferences if the inner type is a reference or a mutable reference
131/// (e.g.: `foo.as_ref()` will work the same if `foo` has type `&mut Foo` or `&&mut Foo`).
132///
133/// Note that due to historic reasons, the above currently does not hold generally for all
134/// [dereferenceable types], e.g. `foo.as_ref()` will *not* work the same as
135/// `Box::new(foo).as_ref()`. Instead, many smart pointers provide an `as_ref` implementation which
136/// simply returns a reference to the [pointed-to value] (but do not perform a cheap
137/// reference-to-reference conversion for that value). However, [`AsRef::as_ref`] should not be
138/// used for the sole purpose of dereferencing; instead ['`Deref` coercion'] can be used:
139///
140/// [dereferenceable types]: core::ops::Deref
141/// [pointed-to value]: core::ops::Deref::Target
142/// ['`Deref` coercion']: core::ops::Deref#deref-coercion
143///
144/// ```
145/// let x = Box::new(5i32);
146/// // Avoid this:
147/// // let y: &i32 = x.as_ref();
148/// // Better just write:
149/// let y: &i32 = &x;
150/// ```
151///
152/// Types which implement [`Deref`] should consider implementing `AsRef<T>` as follows:
153///
154/// [`Deref`]: core::ops::Deref
155///
156/// ```
157/// # use core::ops::Deref;
158/// # struct SomeType;
159/// # impl Deref for SomeType {
160/// #     type Target = [u8];
161/// #     fn deref(&self) -> &[u8] {
162/// #         &[]
163/// #     }
164/// # }
165/// impl<T> AsRef<T> for SomeType
166/// where
167///     T: ?Sized,
168///     <SomeType as Deref>::Target: AsRef<T>,
169/// {
170///     fn as_ref(&self) -> &T {
171///         self.deref().as_ref()
172///     }
173/// }
174/// ```
175///
176/// # Reflexivity
177///
178/// Ideally, `AsRef` would be reflexive, i.e. there would be an `impl<T: ?Sized> AsRef<T> for T`
179/// with [`as_ref`] simply returning its argument unchanged.
180/// Such a blanket implementation is currently *not* provided due to technical restrictions of
181/// Rust's type system (it would be overlapping with another existing blanket implementation for
182/// `&T where T: AsRef<U>` which allows `AsRef` to auto-dereference, see "Generic Implementations"
183/// above).
184///
185/// [`as_ref`]: AsRef::as_ref
186///
187/// A trivial implementation of `AsRef<T> for T` must be added explicitly for a particular type `T`
188/// where needed or desired. Note, however, that not all types from `std` contain such an
189/// implementation, and those cannot be added by external code due to orphan rules.
190///
191/// # Examples
192///
193/// By using trait bounds we can accept arguments of different types as long as they can be
194/// converted to the specified type `T`.
195///
196/// For example: By creating a generic function that takes an `AsRef<str>` we express that we
197/// want to accept all references that can be converted to [`&str`] as an argument.
198/// Since both [`String`] and [`&str`] implement `AsRef<str>` we can accept both as input argument.
199///
200/// [`&str`]: primitive@str
201/// [`Borrow`]: crate::borrow::Borrow
202/// [`Eq`]: crate::cmp::Eq
203/// [`Ord`]: crate::cmp::Ord
204/// [`String`]: ../../std/string/struct.String.html
205///
206/// ```
207/// fn is_hello<T: AsRef<str>>(s: T) {
208///    assert_eq!("hello", s.as_ref());
209/// }
210///
211/// let s = "hello";
212/// is_hello(s);
213///
214/// let s = "hello".to_string();
215/// is_hello(s);
216/// ```
217#[stable(feature = "rust1", since = "1.0.0")]
218#[rustc_diagnostic_item = "AsRef"]
219#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
220pub const trait AsRef<T: PointeeSized>: PointeeSized {
221    /// Converts this type into a shared reference of the (usually inferred) input type.
222    #[stable(feature = "rust1", since = "1.0.0")]
223    fn as_ref(&self) -> &T;
224}
225
226/// Used to do a cheap mutable-to-mutable reference conversion.
227///
228/// This trait is similar to [`AsRef`] but used for converting between mutable
229/// references. If you need to do a costly conversion it is better to
230/// implement [`From`] with type `&mut T` or write a custom function.
231///
232/// **Note: This trait must not fail**. If the conversion can fail, use a
233/// dedicated method which returns an [`Option<T>`] or a [`Result<T, E>`].
234///
235/// # Generic Implementations
236///
237/// `AsMut` auto-dereferences if the inner type is a mutable reference
238/// (e.g.: `foo.as_mut()` will work the same if `foo` has type `&mut Foo` or `&mut &mut Foo`).
239///
240/// Note that due to historic reasons, the above currently does not hold generally for all
241/// [mutably dereferenceable types], e.g. `foo.as_mut()` will *not* work the same as
242/// `Box::new(foo).as_mut()`. Instead, many smart pointers provide an `as_mut` implementation which
243/// simply returns a reference to the [pointed-to value] (but do not perform a cheap
244/// reference-to-reference conversion for that value). However, [`AsMut::as_mut`] should not be
245/// used for the sole purpose of mutable dereferencing; instead ['`Deref` coercion'] can be used:
246///
247/// [mutably dereferenceable types]: core::ops::DerefMut
248/// [pointed-to value]: core::ops::Deref::Target
249/// ['`Deref` coercion']: core::ops::DerefMut#mutable-deref-coercion
250///
251/// ```
252/// let mut x = Box::new(5i32);
253/// // Avoid this:
254/// // let y: &mut i32 = x.as_mut();
255/// // Better just write:
256/// let y: &mut i32 = &mut x;
257/// ```
258///
259/// Types which implement [`DerefMut`] should consider to add an implementation of `AsMut<T>` as
260/// follows:
261///
262/// [`DerefMut`]: core::ops::DerefMut
263///
264/// ```
265/// # use core::ops::{Deref, DerefMut};
266/// # struct SomeType;
267/// # impl Deref for SomeType {
268/// #     type Target = [u8];
269/// #     fn deref(&self) -> &[u8] {
270/// #         &[]
271/// #     }
272/// # }
273/// # impl DerefMut for SomeType {
274/// #     fn deref_mut(&mut self) -> &mut [u8] {
275/// #         &mut []
276/// #     }
277/// # }
278/// impl<T> AsMut<T> for SomeType
279/// where
280///     <SomeType as Deref>::Target: AsMut<T>,
281/// {
282///     fn as_mut(&mut self) -> &mut T {
283///         self.deref_mut().as_mut()
284///     }
285/// }
286/// ```
287///
288/// # Reflexivity
289///
290/// Ideally, `AsMut` would be reflexive, i.e. there would be an `impl<T: ?Sized> AsMut<T> for T`
291/// with [`as_mut`] simply returning its argument unchanged.
292/// Such a blanket implementation is currently *not* provided due to technical restrictions of
293/// Rust's type system (it would be overlapping with another existing blanket implementation for
294/// `&mut T where T: AsMut<U>` which allows `AsMut` to auto-dereference, see "Generic
295/// Implementations" above).
296///
297/// [`as_mut`]: AsMut::as_mut
298///
299/// A trivial implementation of `AsMut<T> for T` must be added explicitly for a particular type `T`
300/// where needed or desired. Note, however, that not all types from `std` contain such an
301/// implementation, and those cannot be added by external code due to orphan rules.
302///
303/// # Examples
304///
305/// Using `AsMut` as trait bound for a generic function, we can accept all mutable references that
306/// can be converted to type `&mut T`. Unlike [dereference], which has a single [target type],
307/// there can be multiple implementations of `AsMut` for a type. In particular, `Vec<T>` implements
308/// both `AsMut<Vec<T>>` and `AsMut<[T]>`.
309///
310/// In the following, the example functions `caesar` and `null_terminate` provide a generic
311/// interface which works with any type that can be converted by cheap mutable-to-mutable conversion
312/// into a byte slice (`[u8]`) or a byte vector (`Vec<u8>`), respectively.
313///
314/// [dereference]: core::ops::DerefMut
315/// [target type]: core::ops::Deref::Target
316///
317/// ```
318/// struct Document {
319///     info: String,
320///     content: Vec<u8>,
321/// }
322///
323/// impl<T: ?Sized> AsMut<T> for Document
324/// where
325///     Vec<u8>: AsMut<T>,
326/// {
327///     fn as_mut(&mut self) -> &mut T {
328///         self.content.as_mut()
329///     }
330/// }
331///
332/// fn caesar<T: AsMut<[u8]>>(data: &mut T, key: u8) {
333///     for byte in data.as_mut() {
334///         *byte = byte.wrapping_add(key);
335///     }
336/// }
337///
338/// fn null_terminate<T: AsMut<Vec<u8>>>(data: &mut T) {
339///     // Using a non-generic inner function, which contains most of the
340///     // functionality, helps to minimize monomorphization overhead.
341///     fn doit(data: &mut Vec<u8>) {
342///         let len = data.len();
343///         if len == 0 || data[len-1] != 0 {
344///             data.push(0);
345///         }
346///     }
347///     doit(data.as_mut());
348/// }
349///
350/// fn main() {
351///     let mut v: Vec<u8> = vec![1, 2, 3];
352///     caesar(&mut v, 5);
353///     assert_eq!(v, [6, 7, 8]);
354///     null_terminate(&mut v);
355///     assert_eq!(v, [6, 7, 8, 0]);
356///     let mut doc = Document {
357///         info: String::from("Example"),
358///         content: vec![17, 19, 8],
359///     };
360///     caesar(&mut doc, 1);
361///     assert_eq!(doc.content, [18, 20, 9]);
362///     null_terminate(&mut doc);
363///     assert_eq!(doc.content, [18, 20, 9, 0]);
364/// }
365/// ```
366///
367/// Note, however, that APIs don't need to be generic. In many cases taking a `&mut [u8]` or
368/// `&mut Vec<u8>`, for example, is the better choice (callers need to pass the correct type then).
369#[stable(feature = "rust1", since = "1.0.0")]
370#[rustc_diagnostic_item = "AsMut"]
371#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
372pub const trait AsMut<T: PointeeSized>: PointeeSized {
373    /// Converts this type into a mutable reference of the (usually inferred) input type.
374    #[stable(feature = "rust1", since = "1.0.0")]
375    fn as_mut(&mut self) -> &mut T;
376}
377
378/// A value-to-value conversion that consumes the input value. The
379/// opposite of [`From`].
380///
381/// One should avoid implementing [`Into`] and implement [`From`] instead.
382/// Implementing [`From`] automatically provides one with an implementation of [`Into`]
383/// thanks to the blanket implementation in the standard library.
384///
385/// Prefer using [`Into`] over [`From`] when specifying trait bounds on a generic function
386/// to ensure that types that only implement [`Into`] can be used as well.
387///
388/// **Note: This trait must not fail**. If the conversion can fail, use [`TryInto`].
389///
390/// # Generic Implementations
391///
392/// - [`From`]`<T> for U` implies `Into<U> for T`
393/// - [`Into`] is reflexive, which means that `Into<T> for T` is implemented
394///
395/// # Implementing [`Into`] for conversions to external types in old versions of Rust
396///
397/// Prior to Rust 1.41, if the destination type was not part of the current crate
398/// then you couldn't implement [`From`] directly.
399/// For example, take this code:
400///
401/// ```
402/// # #![allow(non_local_definitions)]
403/// struct Wrapper<T>(Vec<T>);
404/// impl<T> From<Wrapper<T>> for Vec<T> {
405///     fn from(w: Wrapper<T>) -> Vec<T> {
406///         w.0
407///     }
408/// }
409/// ```
410/// This will fail to compile in older versions of the language because Rust's orphaning rules
411/// used to be a little bit more strict. To bypass this, you could implement [`Into`] directly:
412///
413/// ```
414/// struct Wrapper<T>(Vec<T>);
415/// impl<T> Into<Vec<T>> for Wrapper<T> {
416///     fn into(self) -> Vec<T> {
417///         self.0
418///     }
419/// }
420/// ```
421///
422/// It is important to understand that [`Into`] does not provide a [`From`] implementation
423/// (as [`From`] does with [`Into`]). Therefore, you should always try to implement [`From`]
424/// and then fall back to [`Into`] if [`From`] can't be implemented.
425///
426/// # Examples
427///
428/// [`String`] implements [`Into`]`<`[`Vec`]`<`[`u8`]`>>`:
429///
430/// In order to express that we want a generic function to take all arguments that can be
431/// converted to a specified type `T`, we can use a trait bound of [`Into`]`<T>`.
432/// For example: The function `is_hello` takes all arguments that can be converted into a
433/// [`Vec`]`<`[`u8`]`>`.
434///
435/// ```
436/// fn is_hello<T: Into<Vec<u8>>>(s: T) {
437///    let bytes = b"hello".to_vec();
438///    assert_eq!(bytes, s.into());
439/// }
440///
441/// let s = "hello".to_string();
442/// is_hello(s);
443/// ```
444///
445/// [`String`]: ../../std/string/struct.String.html
446/// [`Vec`]: ../../std/vec/struct.Vec.html
447#[rustc_diagnostic_item = "Into"]
448#[stable(feature = "rust1", since = "1.0.0")]
449#[doc(search_unbox)]
450#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
451pub const trait Into<T>: Sized {
452    /// Converts this type into the (usually inferred) input type.
453    #[must_use]
454    #[stable(feature = "rust1", since = "1.0.0")]
455    fn into(self) -> T;
456}
457
458/// Used to do value-to-value conversions while consuming the input value. It is the reciprocal of
459/// [`Into`].
460///
461/// One should always prefer implementing `From` over [`Into`]
462/// because implementing `From` automatically provides one with an implementation of [`Into`]
463/// thanks to the blanket implementation in the standard library.
464///
465/// Only implement [`Into`] when targeting a version prior to Rust 1.41 and converting to a type
466/// outside the current crate.
467/// `From` was not able to do these types of conversions in earlier versions because of Rust's
468/// orphaning rules.
469/// See [`Into`] for more details.
470///
471/// Prefer using [`Into`] over [`From`] when specifying trait bounds on a generic function
472/// to ensure that types that only implement [`Into`] can be used as well.
473///
474/// The `From` trait is also very useful when performing error handling. When constructing a function
475/// that is capable of failing, the return type will generally be of the form `Result<T, E>`.
476/// `From` simplifies error handling by allowing a function to return a single error type
477/// that encapsulates multiple error types. See the "Examples" section and [the book][book] for more
478/// details.
479///
480/// **Note: This trait must not fail**. The `From` trait is intended for perfect conversions.
481/// If the conversion can fail or is not perfect, use [`TryFrom`].
482///
483/// # Generic Implementations
484///
485/// - `From<T> for U` implies [`Into`]`<U> for T`
486/// - `From` is reflexive, which means that `From<T> for T` is implemented
487///
488/// # When to implement `From`
489///
490/// While there's no technical restrictions on which conversions can be done using
491/// a `From` implementation, the general expectation is that the conversions
492/// should typically be restricted as follows:
493///
494/// * The conversion is *infallible*: if the conversion can fail, use [`TryFrom`]
495///   instead; don't provide a `From` impl that panics.
496///
497/// * The conversion is *lossless*: semantically, it should not lose or discard
498///   information. For example, `i32: From<u16>` exists, where the original
499///   value can be recovered using `u16: TryFrom<i32>`.  And `String: From<&str>`
500///   exists, where you can get something equivalent to the original value via
501///   `Deref`.  But `From` cannot be used to convert from `u32` to `u16`, since
502///   that cannot succeed in a lossless way.  (There's some wiggle room here for
503///   information not considered semantically relevant.  For example,
504///   `Box<[T]>: From<Vec<T>>` exists even though it might not preserve capacity,
505///   like how two vectors can be equal despite differing capacities.)
506///
507/// * The conversion is *value-preserving*: the conceptual kind and meaning of
508///   the resulting value is the same, even though the Rust type and technical
509///   representation might be different.  For example `-1_i8 as u8` is *lossless*,
510///   since `as` casting back can recover the original value, but that conversion
511///   is *not* available via `From` because `-1` and `255` are different conceptual
512///   values (despite being identical bit patterns technically).  But
513///   `f32: From<i16>` *is* available because `1_i16` and `1.0_f32` are conceptually
514///   the same real number (despite having very different bit patterns technically).
515///   `String: From<char>` is available because they're both *text*, but
516///   `String: From<u32>` is *not* available, since `1` (a number) and `"1"`
517///   (text) are too different.  (Converting values to text is instead covered
518///   by the [`Display`](crate::fmt::Display) trait.)
519///
520/// * The conversion is *obvious*: it's the only reasonable conversion between
521///   the two types.  Otherwise it's better to have it be a named method or
522///   constructor, like how [`str::as_bytes`] is a method and how integers have
523///   methods like [`u32::from_ne_bytes`], [`u32::from_le_bytes`], and
524///   [`u32::from_be_bytes`], none of which are `From` implementations.  Whereas
525///   there's only one reasonable way to wrap an [`Ipv6Addr`](crate::net::Ipv6Addr)
526///   into an [`IpAddr`](crate::net::IpAddr), thus `IpAddr: From<Ipv6Addr>` exists.
527///
528/// # Examples
529///
530/// [`String`] implements `From<&str>`:
531///
532/// An explicit conversion from a `&str` to a String is done as follows:
533///
534/// ```
535/// let string = "hello".to_string();
536/// let other_string = String::from("hello");
537///
538/// assert_eq!(string, other_string);
539/// ```
540///
541/// While performing error handling it is often useful to implement `From` for your own error type.
542/// By converting underlying error types to our own custom error type that encapsulates the
543/// underlying error type, we can return a single error type without losing information on the
544/// underlying cause. The '?' operator automatically converts the underlying error type to our
545/// custom error type with `From::from`.
546///
547/// ```
548/// use std::fs;
549/// use std::io;
550/// use std::num;
551///
552/// enum CliError {
553///     IoError(io::Error),
554///     ParseError(num::ParseIntError),
555/// }
556///
557/// impl From<io::Error> for CliError {
558///     fn from(error: io::Error) -> Self {
559///         CliError::IoError(error)
560///     }
561/// }
562///
563/// impl From<num::ParseIntError> for CliError {
564///     fn from(error: num::ParseIntError) -> Self {
565///         CliError::ParseError(error)
566///     }
567/// }
568///
569/// fn open_and_parse_file(file_name: &str) -> Result<i32, CliError> {
570///     let mut contents = fs::read_to_string(&file_name)?;
571///     let num: i32 = contents.trim().parse()?;
572///     Ok(num)
573/// }
574/// ```
575///
576/// [`String`]: ../../std/string/struct.String.html
577/// [`from`]: From::from
578/// [book]: ../../book/ch09-00-error-handling.html
579#[rustc_diagnostic_item = "From"]
580#[stable(feature = "rust1", since = "1.0.0")]
581#[rustc_on_unimplemented(on(
582    all(Self = "&str", T = "alloc::string::String"),
583    note = "to coerce a `{T}` into a `{Self}`, use `&*` as a prefix",
584))]
585#[doc(search_unbox)]
586#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
587pub const trait From<T>: Sized {
588    /// Converts to this type from the input type.
589    #[rustc_diagnostic_item = "from_fn"]
590    #[must_use]
591    #[stable(feature = "rust1", since = "1.0.0")]
592    fn from(value: T) -> Self;
593}
594
595/// An attempted conversion that consumes `self`, which may or may not be
596/// expensive.
597///
598/// Library authors should usually not directly implement this trait,
599/// but should prefer implementing the [`TryFrom`] trait, which offers
600/// greater flexibility and provides an equivalent `TryInto`
601/// implementation for free, thanks to a blanket implementation in the
602/// standard library. For more information on this, see the
603/// documentation for [`Into`].
604///
605/// Prefer using [`TryInto`] over [`TryFrom`] when specifying trait bounds on a generic function
606/// to ensure that types that only implement [`TryInto`] can be used as well.
607///
608/// # Implementing `TryInto`
609///
610/// This suffers the same restrictions and reasoning as implementing
611/// [`Into`], see there for details.
612#[rustc_diagnostic_item = "TryInto"]
613#[stable(feature = "try_from", since = "1.34.0")]
614#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
615pub const trait TryInto<T>: Sized {
616    /// The type returned in the event of a conversion error.
617    #[stable(feature = "try_from", since = "1.34.0")]
618    type Error;
619
620    /// Performs the conversion.
621    #[stable(feature = "try_from", since = "1.34.0")]
622    fn try_into(self) -> Result<T, Self::Error>;
623}
624
625/// Simple and safe type conversions that may fail in a controlled
626/// way under some circumstances. It is the reciprocal of [`TryInto`].
627///
628/// This is useful when you are doing a type conversion that may
629/// trivially succeed but may also need special handling.
630/// For example, there is no way to convert an [`i64`] into an [`i32`]
631/// using the [`From`] trait, because an [`i64`] may contain a value
632/// that an [`i32`] cannot represent and so the conversion would lose data.
633/// This might be handled by truncating the [`i64`] to an [`i32`] or by
634/// simply returning [`i32::MAX`], or by some other method.  The [`From`]
635/// trait is intended for perfect conversions, so the `TryFrom` trait
636/// informs the programmer when a type conversion could go bad and lets
637/// them decide how to handle it.
638///
639/// # Generic Implementations
640///
641/// - `TryFrom<T> for U` implies [`TryInto`]`<U> for T`
642/// - [`try_from`] is reflexive, which means that `TryFrom<T> for T`
643/// is implemented and cannot fail -- the associated `Error` type for
644/// calling `T::try_from()` on a value of type `T` is [`Infallible`].
645/// When the [`!`] type is stabilized [`Infallible`] and [`!`] will be
646/// equivalent.
647///
648/// Prefer using [`TryInto`] over [`TryFrom`] when specifying trait bounds on a generic function
649/// to ensure that types that only implement [`TryInto`] can be used as well.
650///
651/// `TryFrom<T>` can be implemented as follows:
652///
653/// ```
654/// struct GreaterThanZero(i32);
655///
656/// impl TryFrom<i32> for GreaterThanZero {
657///     type Error = &'static str;
658///
659///     fn try_from(value: i32) -> Result<Self, Self::Error> {
660///         if value <= 0 {
661///             Err("GreaterThanZero only accepts values greater than zero!")
662///         } else {
663///             Ok(GreaterThanZero(value))
664///         }
665///     }
666/// }
667/// ```
668///
669/// # Examples
670///
671/// As described, [`i32`] implements `TryFrom<`[`i64`]`>`:
672///
673/// ```
674/// let big_number = 1_000_000_000_000i64;
675/// // Silently truncates `big_number`, requires detecting
676/// // and handling the truncation after the fact.
677/// let smaller_number = big_number as i32;
678/// assert_eq!(smaller_number, -727379968);
679///
680/// // Returns an error because `big_number` is too big to
681/// // fit in an `i32`.
682/// let try_smaller_number = i32::try_from(big_number);
683/// assert!(try_smaller_number.is_err());
684///
685/// // Returns `Ok(3)`.
686/// let try_successful_smaller_number = i32::try_from(3);
687/// assert!(try_successful_smaller_number.is_ok());
688/// ```
689///
690/// [`try_from`]: TryFrom::try_from
691#[rustc_diagnostic_item = "TryFrom"]
692#[stable(feature = "try_from", since = "1.34.0")]
693#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
694pub const trait TryFrom<T>: Sized {
695    /// The type returned in the event of a conversion error.
696    #[stable(feature = "try_from", since = "1.34.0")]
697    type Error;
698
699    /// Performs the conversion.
700    #[stable(feature = "try_from", since = "1.34.0")]
701    #[rustc_diagnostic_item = "try_from_fn"]
702    fn try_from(value: T) -> Result<Self, Self::Error>;
703}
704
705////////////////////////////////////////////////////////////////////////////////
706// GENERIC IMPLS
707////////////////////////////////////////////////////////////////////////////////
708
709// As lifts over &
710#[stable(feature = "rust1", since = "1.0.0")]
711#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
712impl<T: PointeeSized, U: PointeeSized> const AsRef<U> for &T
713where
714    T: [const] AsRef<U>,
715{
716    #[inline]
717    fn as_ref(&self) -> &U {
718        <T as AsRef<U>>::as_ref(*self)
719    }
720}
721
722// As lifts over &mut
723#[stable(feature = "rust1", since = "1.0.0")]
724#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
725impl<T: PointeeSized, U: PointeeSized> const AsRef<U> for &mut T
726where
727    T: [const] AsRef<U>,
728{
729    #[inline]
730    fn as_ref(&self) -> &U {
731        <T as AsRef<U>>::as_ref(*self)
732    }
733}
734
735// FIXME (#45742): replace the above impls for &/&mut with the following more general one:
736// // As lifts over Deref
737// impl<D: ?Sized + Deref<Target: AsRef<U>>, U: ?Sized> AsRef<U> for D {
738//     fn as_ref(&self) -> &U {
739//         self.deref().as_ref()
740//     }
741// }
742
743// AsMut lifts over &mut
744#[stable(feature = "rust1", since = "1.0.0")]
745#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
746impl<T: PointeeSized, U: PointeeSized> const AsMut<U> for &mut T
747where
748    T: [const] AsMut<U>,
749{
750    #[inline]
751    fn as_mut(&mut self) -> &mut U {
752        (*self).as_mut()
753    }
754}
755
756// FIXME (#45742): replace the above impl for &mut with the following more general one:
757// // AsMut lifts over DerefMut
758// impl<D: ?Sized + Deref<Target: AsMut<U>>, U: ?Sized> AsMut<U> for D {
759//     fn as_mut(&mut self) -> &mut U {
760//         self.deref_mut().as_mut()
761//     }
762// }
763
764// From implies Into
765#[stable(feature = "rust1", since = "1.0.0")]
766#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
767impl<T, U> const Into<U> for T
768where
769    U: [const] From<T>,
770{
771    /// Calls `U::from(self)`.
772    ///
773    /// That is, this conversion is whatever the implementation of
774    /// <code>[From]&lt;T&gt; for U</code> chooses to do.
775    #[inline]
776    #[track_caller]
777    fn into(self) -> U {
778        U::from(self)
779    }
780}
781
782// From (and thus Into) is reflexive
783#[stable(feature = "rust1", since = "1.0.0")]
784#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
785impl<T> const From<T> for T {
786    /// Returns the argument unchanged.
787    #[inline(always)]
788    fn from(t: T) -> T {
789        t
790    }
791}
792
793/// **Stability note:** This impl does not yet exist, but we are
794/// "reserving space" to add it in the future. See
795/// [rust-lang/rust#64715][#64715] for details.
796///
797/// [#64715]: https://github.com/rust-lang/rust/issues/64715
798#[stable(feature = "convert_infallible", since = "1.34.0")]
799#[rustc_reservation_impl = "permitting this impl would forbid us from adding \
800                            `impl<T> From<!> for T` later; see rust-lang/rust#64715 for details"]
801#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
802impl<T> const From<!> for T {
803    fn from(t: !) -> T {
804        t
805    }
806}
807
808// TryFrom implies TryInto
809#[stable(feature = "try_from", since = "1.34.0")]
810#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
811impl<T, U> const TryInto<U> for T
812where
813    U: [const] TryFrom<T>,
814{
815    type Error = U::Error;
816
817    #[inline]
818    fn try_into(self) -> Result<U, U::Error> {
819        U::try_from(self)
820    }
821}
822
823// Infallible conversions are semantically equivalent to fallible conversions
824// with an uninhabited error type.
825#[stable(feature = "try_from", since = "1.34.0")]
826#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
827impl<T, U> const TryFrom<U> for T
828where
829    U: [const] Into<T>,
830{
831    type Error = Infallible;
832
833    #[inline]
834    fn try_from(value: U) -> Result<Self, Self::Error> {
835        Ok(U::into(value))
836    }
837}
838
839////////////////////////////////////////////////////////////////////////////////
840// CONCRETE IMPLS
841////////////////////////////////////////////////////////////////////////////////
842
843#[stable(feature = "rust1", since = "1.0.0")]
844#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
845impl<T> const AsRef<[T]> for [T] {
846    #[inline(always)]
847    fn as_ref(&self) -> &[T] {
848        self
849    }
850}
851
852#[stable(feature = "rust1", since = "1.0.0")]
853#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
854impl<T> const AsMut<[T]> for [T] {
855    #[inline(always)]
856    fn as_mut(&mut self) -> &mut [T] {
857        self
858    }
859}
860
861#[stable(feature = "rust1", since = "1.0.0")]
862#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
863impl const AsRef<str> for str {
864    #[inline(always)]
865    fn as_ref(&self) -> &str {
866        self
867    }
868}
869
870#[stable(feature = "as_mut_str_for_str", since = "1.51.0")]
871#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
872impl const AsMut<str> for str {
873    #[inline(always)]
874    fn as_mut(&mut self) -> &mut str {
875        self
876    }
877}
878
879////////////////////////////////////////////////////////////////////////////////
880// THE NO-ERROR ERROR TYPE
881////////////////////////////////////////////////////////////////////////////////
882
883/// The error type for errors that can never happen.
884///
885/// Since this enum has no variant, a value of this type can never actually exist.
886/// This can be useful for generic APIs that use [`Result`] and parameterize the error type,
887/// to indicate that the result is always [`Ok`].
888///
889/// For example, the [`TryFrom`] trait (conversion that returns a [`Result`])
890/// has a blanket implementation for all types where a reverse [`Into`] implementation exists.
891///
892/// ```ignore (illustrates std code, duplicating the impl in a doctest would be an error)
893/// impl<T, U> TryFrom<U> for T where U: Into<T> {
894///     type Error = Infallible;
895///
896///     fn try_from(value: U) -> Result<Self, Infallible> {
897///         Ok(U::into(value))  // Never returns `Err`
898///     }
899/// }
900/// ```
901///
902/// # Future compatibility
903///
904/// This enum has the same role as [the `!` “never” type][never],
905/// which is unstable in this version of Rust.
906/// When `!` is stabilized, we plan to make `Infallible` a type alias to it:
907///
908/// ```ignore (illustrates future std change)
909/// pub type Infallible = !;
910/// ```
911///
912/// … and eventually deprecate `Infallible`.
913///
914/// However there is one case where `!` syntax can be used
915/// before `!` is stabilized as a full-fledged type: in the position of a function’s return type.
916/// Specifically, it is possible to have implementations for two different function pointer types:
917///
918/// ```
919/// trait MyTrait {}
920/// impl MyTrait for fn() -> ! {}
921/// impl MyTrait for fn() -> std::convert::Infallible {}
922/// ```
923///
924/// With `Infallible` being an enum, this code is valid.
925/// However when `Infallible` becomes an alias for the never type,
926/// the two `impl`s will start to overlap
927/// and therefore will be disallowed by the language’s trait coherence rules.
928#[stable(feature = "convert_infallible", since = "1.34.0")]
929#[derive(Copy)]
930pub enum Infallible {}
931
932#[stable(feature = "convert_infallible", since = "1.34.0")]
933#[rustc_const_unstable(feature = "const_clone", issue = "142757")]
934impl const Clone for Infallible {
935    fn clone(&self) -> Infallible {
936        match *self {}
937    }
938}
939
940#[stable(feature = "convert_infallible", since = "1.34.0")]
941impl fmt::Debug for Infallible {
942    fn fmt(&self, _: &mut fmt::Formatter<'_>) -> fmt::Result {
943        match *self {}
944    }
945}
946
947#[stable(feature = "convert_infallible", since = "1.34.0")]
948impl fmt::Display for Infallible {
949    fn fmt(&self, _: &mut fmt::Formatter<'_>) -> fmt::Result {
950        match *self {}
951    }
952}
953
954#[stable(feature = "str_parse_error2", since = "1.8.0")]
955impl Error for Infallible {}
956
957#[stable(feature = "convert_infallible", since = "1.34.0")]
958#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
959impl const PartialEq for Infallible {
960    fn eq(&self, _: &Infallible) -> bool {
961        match *self {}
962    }
963}
964
965#[stable(feature = "convert_infallible", since = "1.34.0")]
966#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
967impl const Eq for Infallible {}
968
969#[stable(feature = "convert_infallible", since = "1.34.0")]
970#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
971impl const PartialOrd for Infallible {
972    fn partial_cmp(&self, _other: &Self) -> Option<crate::cmp::Ordering> {
973        match *self {}
974    }
975}
976
977#[stable(feature = "convert_infallible", since = "1.34.0")]
978#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
979impl const Ord for Infallible {
980    fn cmp(&self, _other: &Self) -> crate::cmp::Ordering {
981        match *self {}
982    }
983}
984
985#[stable(feature = "convert_infallible", since = "1.34.0")]
986#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
987impl const From<!> for Infallible {
988    #[inline]
989    fn from(x: !) -> Self {
990        x
991    }
992}
993
994#[stable(feature = "convert_infallible_hash", since = "1.44.0")]
995impl Hash for Infallible {
996    fn hash<H: Hasher>(&self, _: &mut H) {
997        match *self {}
998    }
999}
````