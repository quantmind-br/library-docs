---
title: result.rs - source
url: https://doc.rust-lang.org/stable/src/core/result.rs.html#557
source: crawler
fetched_at: 2026-05-06T21:25:42.703231957-03:00
rendered_js: false
word_count: 8478
summary: This document explains the usage of the Result type in Rust for error handling, covering pattern matching, convenience methods, the importance of explicit error management, and the use of the question mark operator for propagation.
tags:
    - rust
    - error-handling
    - result-type
    - pattern-matching
    - question-mark-operator
    - programming-concepts
category: concept
---

## core/ result.rs

````rust
1//! Error handling with the `Result` type.
2//!
3//! [`Result<T, E>`][`Result`] is the type used for returning and propagating
4//! errors. It is an enum with the variants, [`Ok(T)`], representing
5//! success and containing a value, and [`Err(E)`], representing error
6//! and containing an error value.
7//!
8//! ```
9//! # #[allow(dead_code)]
10//! enum Result<T, E> {
11//!    Ok(T),
12//!    Err(E),
13//! }
14//! ```
15//!
16//! Functions return [`Result`] whenever errors are expected and
17//! recoverable. In the `std` crate, [`Result`] is most prominently used
18//! for [I/O](../../std/io/index.html).
19//!
20//! A simple function returning [`Result`] might be
21//! defined and used like so:
22//!
23//! ```
24//! #[derive(Debug)]
25//! enum Version { Version1, Version2 }
26//!
27//! fn parse_version(header: &[u8]) -> Result<Version, &'static str> {
28//!     match header.get(0) {
29//!         None => Err("invalid header length"),
30//!         Some(&1) => Ok(Version::Version1),
31//!         Some(&2) => Ok(Version::Version2),
32//!         Some(_) => Err("invalid version"),
33//!     }
34//! }
35//!
36//! let version = parse_version(&[1, 2, 3, 4]);
37//! match version {
38//!     Ok(v) => println!("working with version: {v:?}"),
39//!     Err(e) => println!("error parsing header: {e:?}"),
40//! }
41//! ```
42//!
43//! Pattern matching on [`Result`]s is clear and straightforward for
44//! simple cases, but [`Result`] comes with some convenience methods
45//! that make working with it more succinct.
46//!
47//! ```
48//! // The `is_ok` and `is_err` methods do what they say.
49//! let good_result: Result<i32, i32> = Ok(10);
50//! let bad_result: Result<i32, i32> = Err(10);
51//! assert!(good_result.is_ok() && !good_result.is_err());
52//! assert!(bad_result.is_err() && !bad_result.is_ok());
53//!
54//! // `map` and `map_err` consume the `Result` and produce another.
55//! let good_result: Result<i32, i32> = good_result.map(|i| i + 1);
56//! let bad_result: Result<i32, i32> = bad_result.map_err(|i| i - 1);
57//! assert_eq!(good_result, Ok(11));
58//! assert_eq!(bad_result, Err(9));
59//!
60//! // Use `and_then` to continue the computation.
61//! let good_result: Result<bool, i32> = good_result.and_then(|i| Ok(i == 11));
62//! assert_eq!(good_result, Ok(true));
63//!
64//! // Use `or_else` to handle the error.
65//! let bad_result: Result<i32, i32> = bad_result.or_else(|i| Ok(i + 20));
66//! assert_eq!(bad_result, Ok(29));
67//!
68//! // Consume the result and return the contents with `unwrap`.
69//! let final_awesome_result = good_result.unwrap();
70//! assert!(final_awesome_result)
71//! ```
72//!
73//! # Results must be used
74//!
75//! A common problem with using return values to indicate errors is
76//! that it is easy to ignore the return value, thus failing to handle
77//! the error. [`Result`] is annotated with the `#[must_use]` attribute,
78//! which will cause the compiler to issue a warning when a Result
79//! value is ignored. This makes [`Result`] especially useful with
80//! functions that may encounter errors but don't otherwise return a
81//! useful value.
82//!
83//! Consider the [`write_all`] method defined for I/O types
84//! by the [`Write`] trait:
85//!
86//! ```
87//! use std::io;
88//!
89//! trait Write {
90//!     fn write_all(&mut self, bytes: &[u8]) -> Result<(), io::Error>;
91//! }
92//! ```
93//!
94//! *Note: The actual definition of [`Write`] uses [`io::Result`], which
95//! is just a synonym for <code>[Result]<T, [io::Error]></code>.*
96//!
97//! This method doesn't produce a value, but the write may
98//! fail. It's crucial to handle the error case, and *not* write
99//! something like this:
100//!
101//! ```no_run
102//! # #![allow(unused_must_use)] // \o/
103//! use std::fs::File;
104//! use std::io::prelude::*;
105//!
106//! let mut file = File::create("valuable_data.txt").unwrap();
107//! // If `write_all` errors, then we'll never know, because the return
108//! // value is ignored.
109//! file.write_all(b"important message");
110//! ```
111//!
112//! If you *do* write that in Rust, the compiler will give you a
113//! warning (by default, controlled by the `unused_must_use` lint).
114//!
115//! You might instead, if you don't want to handle the error, simply
116//! assert success with [`expect`]. This will panic if the
117//! write fails, providing a marginally useful message indicating why:
118//!
119//! ```no_run
120//! use std::fs::File;
121//! use std::io::prelude::*;
122//!
123//! let mut file = File::create("valuable_data.txt").unwrap();
124//! file.write_all(b"important message").expect("failed to write message");
125//! ```
126//!
127//! You might also simply assert success:
128//!
129//! ```no_run
130//! # use std::fs::File;
131//! # use std::io::prelude::*;
132//! # let mut file = File::create("valuable_data.txt").unwrap();
133//! assert!(file.write_all(b"important message").is_ok());
134//! ```
135//!
136//! Or propagate the error up the call stack with [`?`]:
137//!
138//! ```
139//! # use std::fs::File;
140//! # use std::io::prelude::*;
141//! # use std::io;
142//! # #[allow(dead_code)]
143//! fn write_message() -> io::Result<()> {
144//!     let mut file = File::create("valuable_data.txt")?;
145//!     file.write_all(b"important message")?;
146//!     Ok(())
147//! }
148//! ```
149//!
150//! # The question mark operator, `?`
151//!
152//! When writing code that calls many functions that return the
153//! [`Result`] type, the error handling can be tedious. The question mark
154//! operator, [`?`], hides some of the boilerplate of propagating errors
155//! up the call stack.
156//!
157//! It replaces this:
158//!
159//! ```
160//! # #![allow(dead_code)]
161//! use std::fs::File;
162//! use std::io::prelude::*;
163//! use std::io;
164//!
165//! struct Info {
166//!     name: String,
167//!     age: i32,
168//!     rating: i32,
169//! }
170//!
171//! fn write_info(info: &Info) -> io::Result<()> {
172//!     // Early return on error
173//!     let mut file = match File::create("my_best_friends.txt") {
174//!            Err(e) => return Err(e),
175//!            Ok(f) => f,
176//!     };
177//!     if let Err(e) = file.write_all(format!("name: {}\n", info.name).as_bytes()) {
178//!         return Err(e)
179//!     }
180//!     if let Err(e) = file.write_all(format!("age: {}\n", info.age).as_bytes()) {
181//!         return Err(e)
182//!     }
183//!     if let Err(e) = file.write_all(format!("rating: {}\n", info.rating).as_bytes()) {
184//!         return Err(e)
185//!     }
186//!     Ok(())
187//! }
188//! ```
189//!
190//! With this:
191//!
192//! ```
193//! # #![allow(dead_code)]
194//! use std::fs::File;
195//! use std::io::prelude::*;
196//! use std::io;
197//!
198//! struct Info {
199//!     name: String,
200//!     age: i32,
201//!     rating: i32,
202//! }
203//!
204//! fn write_info(info: &Info) -> io::Result<()> {
205//!     let mut file = File::create("my_best_friends.txt")?;
206//!     // Early return on error
207//!     file.write_all(format!("name: {}\n", info.name).as_bytes())?;
208//!     file.write_all(format!("age: {}\n", info.age).as_bytes())?;
209//!     file.write_all(format!("rating: {}\n", info.rating).as_bytes())?;
210//!     Ok(())
211//! }
212//! ```
213//!
214//! *It's much nicer!*
215//!
216//! Ending the expression with [`?`] will result in the [`Ok`]'s unwrapped value, unless the result
217//! is [`Err`], in which case [`Err`] is returned early from the enclosing function.
218//!
219//! [`?`] can be used in functions that return [`Result`] because of the
220//! early return of [`Err`] that it provides.
221//!
222//! [`expect`]: Result::expect
223//! [`Write`]: ../../std/io/trait.Write.html "io::Write"
224//! [`write_all`]: ../../std/io/trait.Write.html#method.write_all "io::Write::write_all"
225//! [`io::Result`]: ../../std/io/type.Result.html "io::Result"
226//! [`?`]: crate::ops::Try
227//! [`Ok(T)`]: Ok
228//! [`Err(E)`]: Err
229//! [io::Error]: ../../std/io/struct.Error.html "io::Error"
230//!
231//! # Representation
232//!
233//! In some cases, [`Result<T, E>`] comes with size, alignment, and ABI
234//! guarantees. Specifically, one of either the `T` or `E` type must be a type
235//! that qualifies for the `Option` [representation guarantees][opt-rep] (let's
236//! call that type `I`), and the *other* type is a zero-sized type with
237//! alignment 1 (a "1-ZST").
238//!
239//! If that is the case, then `Result<T, E>` has the same size, alignment, and
240//! [function call ABI] as `I` (and therefore, as `Option<I>`). If `I` is `T`,
241//! it is therefore sound to transmute a value `t` of type `I` to type
242//! `Result<T, E>` (producing the value `Ok(t)`) and to transmute a value
243//! `Ok(t)` of type `Result<T, E>` to type `I` (producing the value `t`). If `I`
244//! is `E`, the same applies with `Ok` replaced by `Err`.
245//!
246//! For example, `NonZeroI32` qualifies for the `Option` representation
247//! guarantees and `()` is a zero-sized type with alignment 1. This means that
248//! both `Result<NonZeroI32, ()>` and `Result<(), NonZeroI32>` have the same
249//! size, alignment, and ABI as `NonZeroI32` (and `Option<NonZeroI32>`). The
250//! only difference between these is in the implied semantics:
251//!
252//! * `Option<NonZeroI32>` is "a non-zero i32 might be present"
253//! * `Result<NonZeroI32, ()>` is "a non-zero i32 success result, if any"
254//! * `Result<(), NonZeroI32>` is "a non-zero i32 error result, if any"
255//!
256//! [opt-rep]: ../option/index.html#representation "Option Representation"
257//! [function call ABI]: ../primitive.fn.html#abi-compatibility
258//!
259//! # Method overview
260//!
261//! In addition to working with pattern matching, [`Result`] provides a
262//! wide variety of different methods.
263//!
264//! ## Querying the variant
265//!
266//! The [`is_ok`] and [`is_err`] methods return [`true`] if the [`Result`]
267//! is [`Ok`] or [`Err`], respectively.
268//!
269//! The [`is_ok_and`] and [`is_err_and`] methods apply the provided function
270//! to the contents of the [`Result`] to produce a boolean value. If the [`Result`] does not have the expected variant
271//! then [`false`] is returned instead without executing the function.
272//!
273//! [`is_err`]: Result::is_err
274//! [`is_ok`]: Result::is_ok
275//! [`is_ok_and`]: Result::is_ok_and
276//! [`is_err_and`]: Result::is_err_and
277//!
278//! ## Adapters for working with references
279//!
280//! * [`as_ref`] converts from `&Result<T, E>` to `Result<&T, &E>`
281//! * [`as_mut`] converts from `&mut Result<T, E>` to `Result<&mut T, &mut E>`
282//! * [`as_deref`] converts from `&Result<T, E>` to `Result<&T::Target, &E>`
283//! * [`as_deref_mut`] converts from `&mut Result<T, E>` to
284//!   `Result<&mut T::Target, &mut E>`
285//!
286//! [`as_deref`]: Result::as_deref
287//! [`as_deref_mut`]: Result::as_deref_mut
288//! [`as_mut`]: Result::as_mut
289//! [`as_ref`]: Result::as_ref
290//!
291//! ## Extracting contained values
292//!
293//! These methods extract the contained value in a [`Result<T, E>`] when it
294//! is the [`Ok`] variant. If the [`Result`] is [`Err`]:
295//!
296//! * [`expect`] panics with a provided custom message
297//! * [`unwrap`] panics with a generic message
298//! * [`unwrap_or`] returns the provided default value
299//! * [`unwrap_or_default`] returns the default value of the type `T`
300//!   (which must implement the [`Default`] trait)
301//! * [`unwrap_or_else`] returns the result of evaluating the provided
302//!   function
303//! * [`unwrap_unchecked`] produces *[undefined behavior]*
304//!
305//! The panicking methods [`expect`] and [`unwrap`] require `E` to
306//! implement the [`Debug`] trait.
307//!
308//! [`Debug`]: crate::fmt::Debug
309//! [`expect`]: Result::expect
310//! [`unwrap`]: Result::unwrap
311//! [`unwrap_or`]: Result::unwrap_or
312//! [`unwrap_or_default`]: Result::unwrap_or_default
313//! [`unwrap_or_else`]: Result::unwrap_or_else
314//! [`unwrap_unchecked`]: Result::unwrap_unchecked
315//! [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
316//!
317//! These methods extract the contained value in a [`Result<T, E>`] when it
318//! is the [`Err`] variant. They require `T` to implement the [`Debug`]
319//! trait. If the [`Result`] is [`Ok`]:
320//!
321//! * [`expect_err`] panics with a provided custom message
322//! * [`unwrap_err`] panics with a generic message
323//! * [`unwrap_err_unchecked`] produces *[undefined behavior]*
324//!
325//! [`Debug`]: crate::fmt::Debug
326//! [`expect_err`]: Result::expect_err
327//! [`unwrap_err`]: Result::unwrap_err
328//! [`unwrap_err_unchecked`]: Result::unwrap_err_unchecked
329//! [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
330//!
331//! ## Transforming contained values
332//!
333//! These methods transform [`Result`] to [`Option`]:
334//!
335//! * [`err`][Result::err] transforms [`Result<T, E>`] into [`Option<E>`],
336//!   mapping [`Err(e)`] to [`Some(e)`] and [`Ok(v)`] to [`None`]
337//! * [`ok`][Result::ok] transforms [`Result<T, E>`] into [`Option<T>`],
338//!   mapping [`Ok(v)`] to [`Some(v)`] and [`Err(e)`] to [`None`]
339//! * [`transpose`] transposes a [`Result`] of an [`Option`] into an
340//!   [`Option`] of a [`Result`]
341//!
342// Do NOT add link reference definitions for `err` or `ok`, because they
343// will generate numerous incorrect URLs for `Err` and `Ok` elsewhere, due
344// to case folding.
345//!
346//! [`Err(e)`]: Err
347//! [`Ok(v)`]: Ok
348//! [`Some(e)`]: Option::Some
349//! [`Some(v)`]: Option::Some
350//! [`transpose`]: Result::transpose
351//!
352//! These methods transform the contained value of the [`Ok`] variant:
353//!
354//! * [`map`] transforms [`Result<T, E>`] into [`Result<U, E>`] by applying
355//!   the provided function to the contained value of [`Ok`] and leaving
356//!   [`Err`] values unchanged
357//! * [`inspect`] takes ownership of the [`Result`], applies the
358//!   provided function to the contained value by reference,
359//!   and then returns the [`Result`]
360//!
361//! [`map`]: Result::map
362//! [`inspect`]: Result::inspect
363//!
364//! These methods transform the contained value of the [`Err`] variant:
365//!
366//! * [`map_err`] transforms [`Result<T, E>`] into [`Result<T, F>`] by
367//!   applying the provided function to the contained value of [`Err`] and
368//!   leaving [`Ok`] values unchanged
369//! * [`inspect_err`] takes ownership of the [`Result`], applies the
370//!   provided function to the contained value of [`Err`] by reference,
371//!   and then returns the [`Result`]
372//!
373//! [`map_err`]: Result::map_err
374//! [`inspect_err`]: Result::inspect_err
375//!
376//! These methods transform a [`Result<T, E>`] into a value of a possibly
377//! different type `U`:
378//!
379//! * [`map_or`] applies the provided function to the contained value of
380//!   [`Ok`], or returns the provided default value if the [`Result`] is
381//!   [`Err`]
382//! * [`map_or_else`] applies the provided function to the contained value
383//!   of [`Ok`], or applies the provided default fallback function to the
384//!   contained value of [`Err`]
385//!
386//! [`map_or`]: Result::map_or
387//! [`map_or_else`]: Result::map_or_else
388//!
389//! ## Boolean operators
390//!
391//! These methods treat the [`Result`] as a boolean value, where [`Ok`]
392//! acts like [`true`] and [`Err`] acts like [`false`]. There are two
393//! categories of these methods: ones that take a [`Result`] as input, and
394//! ones that take a function as input (to be lazily evaluated).
395//!
396//! The [`and`] and [`or`] methods take another [`Result`] as input, and
397//! produce a [`Result`] as output. The [`and`] method can produce a
398//! [`Result<U, E>`] value having a different inner type `U` than
399//! [`Result<T, E>`]. The [`or`] method can produce a [`Result<T, F>`]
400//! value having a different error type `F` than [`Result<T, E>`].
401//!
402//! | method  | self     | input     | output   |
403//! |---------|----------|-----------|----------|
404//! | [`and`] | `Err(e)` | (ignored) | `Err(e)` |
405//! | [`and`] | `Ok(x)`  | `Err(d)`  | `Err(d)` |
406//! | [`and`] | `Ok(x)`  | `Ok(y)`   | `Ok(y)`  |
407//! | [`or`]  | `Err(e)` | `Err(d)`  | `Err(d)` |
408//! | [`or`]  | `Err(e)` | `Ok(y)`   | `Ok(y)`  |
409//! | [`or`]  | `Ok(x)`  | (ignored) | `Ok(x)`  |
410//!
411//! [`and`]: Result::and
412//! [`or`]: Result::or
413//!
414//! The [`and_then`] and [`or_else`] methods take a function as input, and
415//! only evaluate the function when they need to produce a new value. The
416//! [`and_then`] method can produce a [`Result<U, E>`] value having a
417//! different inner type `U` than [`Result<T, E>`]. The [`or_else`] method
418//! can produce a [`Result<T, F>`] value having a different error type `F`
419//! than [`Result<T, E>`].
420//!
421//! | method       | self     | function input | function result | output   |
422//! |--------------|----------|----------------|-----------------|----------|
423//! | [`and_then`] | `Err(e)` | (not provided) | (not evaluated) | `Err(e)` |
424//! | [`and_then`] | `Ok(x)`  | `x`            | `Err(d)`        | `Err(d)` |
425//! | [`and_then`] | `Ok(x)`  | `x`            | `Ok(y)`         | `Ok(y)`  |
426//! | [`or_else`]  | `Err(e)` | `e`            | `Err(d)`        | `Err(d)` |
427//! | [`or_else`]  | `Err(e)` | `e`            | `Ok(y)`         | `Ok(y)`  |
428//! | [`or_else`]  | `Ok(x)`  | (not provided) | (not evaluated) | `Ok(x)`  |
429//!
430//! [`and_then`]: Result::and_then
431//! [`or_else`]: Result::or_else
432//!
433//! ## Comparison operators
434//!
435//! If `T` and `E` both implement [`PartialOrd`] then [`Result<T, E>`] will
436//! derive its [`PartialOrd`] implementation.  With this order, an [`Ok`]
437//! compares as less than any [`Err`], while two [`Ok`] or two [`Err`]
438//! compare as their contained values would in `T` or `E` respectively.  If `T`
439//! and `E` both also implement [`Ord`], then so does [`Result<T, E>`].
440//!
441//! ```
442//! assert!(Ok(1) < Err(0));
443//! let x: Result<i32, ()> = Ok(0);
444//! let y = Ok(1);
445//! assert!(x < y);
446//! let x: Result<(), i32> = Err(0);
447//! let y = Err(1);
448//! assert!(x < y);
449//! ```
450//!
451//! ## Iterating over `Result`
452//!
453//! A [`Result`] can be iterated over. This can be helpful if you need an
454//! iterator that is conditionally empty. The iterator will either produce
455//! a single value (when the [`Result`] is [`Ok`]), or produce no values
456//! (when the [`Result`] is [`Err`]). For example, [`into_iter`] acts like
457//! [`once(v)`] if the [`Result`] is [`Ok(v)`], and like [`empty()`] if the
458//! [`Result`] is [`Err`].
459//!
460//! [`Ok(v)`]: Ok
461//! [`empty()`]: crate::iter::empty
462//! [`once(v)`]: crate::iter::once
463//!
464//! Iterators over [`Result<T, E>`] come in three types:
465//!
466//! * [`into_iter`] consumes the [`Result`] and produces the contained
467//!   value
468//! * [`iter`] produces an immutable reference of type `&T` to the
469//!   contained value
470//! * [`iter_mut`] produces a mutable reference of type `&mut T` to the
471//!   contained value
472//!
473//! See [Iterating over `Option`] for examples of how this can be useful.
474//!
475//! [Iterating over `Option`]: crate::option#iterating-over-option
476//! [`into_iter`]: Result::into_iter
477//! [`iter`]: Result::iter
478//! [`iter_mut`]: Result::iter_mut
479//!
480//! You might want to use an iterator chain to do multiple instances of an
481//! operation that can fail, but would like to ignore failures while
482//! continuing to process the successful results. In this example, we take
483//! advantage of the iterable nature of [`Result`] to select only the
484//! [`Ok`] values using [`flatten`][Iterator::flatten].
485//!
486//! ```
487//! # use std::str::FromStr;
488//! let mut results = vec![];
489//! let mut errs = vec![];
490//! let nums: Vec<_> = ["17", "not a number", "99", "-27", "768"]
491//!    .into_iter()
492//!    .map(u8::from_str)
493//!    // Save clones of the raw `Result` values to inspect
494//!    .inspect(|x| results.push(x.clone()))
495//!    // Challenge: explain how this captures only the `Err` values
496//!    .inspect(|x| errs.extend(x.clone().err()))
497//!    .flatten()
498//!    .collect();
499//! assert_eq!(errs.len(), 3);
500//! assert_eq!(nums, [17, 99]);
501//! println!("results {results:?}");
502//! println!("errs {errs:?}");
503//! println!("nums {nums:?}");
504//! ```
505//!
506//! ## Collecting into `Result`
507//!
508//! [`Result`] implements the [`FromIterator`][impl-FromIterator] trait,
509//! which allows an iterator over [`Result`] values to be collected into a
510//! [`Result`] of a collection of each contained value of the original
511//! [`Result`] values, or [`Err`] if any of the elements was [`Err`].
512//!
513//! [impl-FromIterator]: Result#impl-FromIterator%3CResult%3CA,+E%3E%3E-for-Result%3CV,+E%3E
514//!
515//! ```
516//! let v = [Ok(2), Ok(4), Err("err!"), Ok(8)];
517//! let res: Result<Vec<_>, &str> = v.into_iter().collect();
518//! assert_eq!(res, Err("err!"));
519//! let v = [Ok(2), Ok(4), Ok(8)];
520//! let res: Result<Vec<_>, &str> = v.into_iter().collect();
521//! assert_eq!(res, Ok(vec![2, 4, 8]));
522//! ```
523//!
524//! [`Result`] also implements the [`Product`][impl-Product] and
525//! [`Sum`][impl-Sum] traits, allowing an iterator over [`Result`] values
526//! to provide the [`product`][Iterator::product] and
527//! [`sum`][Iterator::sum] methods.
528//!
529//! [impl-Product]: Result#impl-Product%3CResult%3CU,+E%3E%3E-for-Result%3CT,+E%3E
530//! [impl-Sum]: Result#impl-Sum%3CResult%3CU,+E%3E%3E-for-Result%3CT,+E%3E
531//!
532//! ```
533//! let v = [Err("error!"), Ok(1), Ok(2), Ok(3), Err("foo")];
534//! let res: Result<i32, &str> = v.into_iter().sum();
535//! assert_eq!(res, Err("error!"));
536//! let v = [Ok(1), Ok(2), Ok(21)];
537//! let res: Result<i32, &str> = v.into_iter().product();
538//! assert_eq!(res, Ok(42));
539//! ```
540
541#![stable(feature = "rust1", since = "1.0.0")]
542
543use crate::iter::{self, FusedIterator, TrustedLen};
544use crate::marker::Destruct;
545use crate::ops::{self, ControlFlow, Deref, DerefMut};
546use crate::{convert, fmt, hint};
547
548/// `Result` is a type that represents either success ([`Ok`]) or failure ([`Err`]).
549///
550/// See the [module documentation](self) for details.
551#[doc(search_unbox)]
552#[derive(Copy, Debug, Hash)]
553#[derive_const(PartialEq, PartialOrd, Eq, Ord)]
554#[must_use = "this `Result` may be an `Err` variant, which should be handled"]
555#[rustc_diagnostic_item = "Result"]
556#[stable(feature = "rust1", since = "1.0.0")]
557pub enum Result<T, E> {
558    /// Contains the success value
559    #[lang = "Ok"]
560    #[stable(feature = "rust1", since = "1.0.0")]
561    Ok(#[stable(feature = "rust1", since = "1.0.0")] T),
562
563    /// Contains the error value
564    #[lang = "Err"]
565    #[stable(feature = "rust1", since = "1.0.0")]
566    Err(#[stable(feature = "rust1", since = "1.0.0")] E),
567}
568
569/////////////////////////////////////////////////////////////////////////////
570// Type implementation
571/////////////////////////////////////////////////////////////////////////////
572
573impl<T, E> Result<T, E> {
574    /////////////////////////////////////////////////////////////////////////
575    // Querying the contained values
576    /////////////////////////////////////////////////////////////////////////
577
578    /// Returns `true` if the result is [`Ok`].
579    ///
580    /// # Examples
581    ///
582    /// ```
583    /// let x: Result<i32, &str> = Ok(-3);
584    /// assert_eq!(x.is_ok(), true);
585    ///
586    /// let x: Result<i32, &str> = Err("Some error message");
587    /// assert_eq!(x.is_ok(), false);
588    /// ```
589    #[must_use = "if you intended to assert that this is ok, consider `.unwrap()` instead"]
590    #[rustc_const_stable(feature = "const_result_basics", since = "1.48.0")]
591    #[inline]
592    #[stable(feature = "rust1", since = "1.0.0")]
593    pub const fn is_ok(&self) -> bool {
594        matches!(*self, Ok(_))
595    }
596
597    /// Returns `true` if the result is [`Ok`] and the value inside of it matches a predicate.
598    ///
599    /// # Examples
600    ///
601    /// ```
602    /// let x: Result<u32, &str> = Ok(2);
603    /// assert_eq!(x.is_ok_and(|x| x > 1), true);
604    ///
605    /// let x: Result<u32, &str> = Ok(0);
606    /// assert_eq!(x.is_ok_and(|x| x > 1), false);
607    ///
608    /// let x: Result<u32, &str> = Err("hey");
609    /// assert_eq!(x.is_ok_and(|x| x > 1), false);
610    ///
611    /// let x: Result<String, &str> = Ok("ownership".to_string());
612    /// assert_eq!(x.as_ref().is_ok_and(|x| x.len() > 1), true);
613    /// println!("still alive {:?}", x);
614    /// ```
615    #[must_use]
616    #[inline]
617    #[stable(feature = "is_some_and", since = "1.70.0")]
618    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
619    pub const fn is_ok_and<F>(self, f: F) -> bool
620    where
621        F: [const] FnOnce(T) -> bool + [const] Destruct,
622        T: [const] Destruct,
623        E: [const] Destruct,
624    {
625        match self {
626            Err(_) => false,
627            Ok(x) => f(x),
628        }
629    }
630
631    /// Returns `true` if the result is [`Err`].
632    ///
633    /// # Examples
634    ///
635    /// ```
636    /// let x: Result<i32, &str> = Ok(-3);
637    /// assert_eq!(x.is_err(), false);
638    ///
639    /// let x: Result<i32, &str> = Err("Some error message");
640    /// assert_eq!(x.is_err(), true);
641    /// ```
642    #[must_use = "if you intended to assert that this is err, consider `.unwrap_err()` instead"]
643    #[rustc_const_stable(feature = "const_result_basics", since = "1.48.0")]
644    #[inline]
645    #[stable(feature = "rust1", since = "1.0.0")]
646    pub const fn is_err(&self) -> bool {
647        !self.is_ok()
648    }
649
650    /// Returns `true` if the result is [`Err`] and the value inside of it matches a predicate.
651    ///
652    /// # Examples
653    ///
654    /// ```
655    /// use std::io::{Error, ErrorKind};
656    ///
657    /// let x: Result<u32, Error> = Err(Error::new(ErrorKind::NotFound, "!"));
658    /// assert_eq!(x.is_err_and(|x| x.kind() == ErrorKind::NotFound), true);
659    ///
660    /// let x: Result<u32, Error> = Err(Error::new(ErrorKind::PermissionDenied, "!"));
661    /// assert_eq!(x.is_err_and(|x| x.kind() == ErrorKind::NotFound), false);
662    ///
663    /// let x: Result<u32, Error> = Ok(123);
664    /// assert_eq!(x.is_err_and(|x| x.kind() == ErrorKind::NotFound), false);
665    ///
666    /// let x: Result<u32, String> = Err("ownership".to_string());
667    /// assert_eq!(x.as_ref().is_err_and(|x| x.len() > 1), true);
668    /// println!("still alive {:?}", x);
669    /// ```
670    #[must_use]
671    #[inline]
672    #[stable(feature = "is_some_and", since = "1.70.0")]
673    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
674    pub const fn is_err_and<F>(self, f: F) -> bool
675    where
676        F: [const] FnOnce(E) -> bool + [const] Destruct,
677        E: [const] Destruct,
678        T: [const] Destruct,
679    {
680        match self {
681            Ok(_) => false,
682            Err(e) => f(e),
683        }
684    }
685
686    /////////////////////////////////////////////////////////////////////////
687    // Adapter for each variant
688    /////////////////////////////////////////////////////////////////////////
689
690    /// Converts from `Result<T, E>` to [`Option<T>`].
691    ///
692    /// Converts `self` into an [`Option<T>`], consuming `self`,
693    /// and converting the error to `None`, if any.
694    ///
695    /// # Examples
696    ///
697    /// ```
698    /// let x: Result<u32, &str> = Ok(2);
699    /// assert_eq!(x.ok(), Some(2));
700    ///
701    /// let x: Result<u32, &str> = Err("Nothing here");
702    /// assert_eq!(x.ok(), None);
703    /// ```
704    #[inline]
705    #[stable(feature = "rust1", since = "1.0.0")]
706    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
707    #[rustc_diagnostic_item = "result_ok_method"]
708    pub const fn ok(self) -> Option<T>
709    where
710        T: [const] Destruct,
711        E: [const] Destruct,
712    {
713        match self {
714            Ok(x) => Some(x),
715            Err(_) => None,
716        }
717    }
718
719    /// Converts from `Result<T, E>` to [`Option<E>`].
720    ///
721    /// Converts `self` into an [`Option<E>`], consuming `self`,
722    /// and discarding the success value, if any.
723    ///
724    /// # Examples
725    ///
726    /// ```
727    /// let x: Result<u32, &str> = Ok(2);
728    /// assert_eq!(x.err(), None);
729    ///
730    /// let x: Result<u32, &str> = Err("Nothing here");
731    /// assert_eq!(x.err(), Some("Nothing here"));
732    /// ```
733    #[inline]
734    #[stable(feature = "rust1", since = "1.0.0")]
735    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
736    pub const fn err(self) -> Option<E>
737    where
738        T: [const] Destruct,
739        E: [const] Destruct,
740    {
741        match self {
742            Ok(_) => None,
743            Err(x) => Some(x),
744        }
745    }
746
747    /////////////////////////////////////////////////////////////////////////
748    // Adapter for working with references
749    /////////////////////////////////////////////////////////////////////////
750
751    /// Converts from `&Result<T, E>` to `Result<&T, &E>`.
752    ///
753    /// Produces a new `Result`, containing a reference
754    /// into the original, leaving the original in place.
755    ///
756    /// # Examples
757    ///
758    /// ```
759    /// let x: Result<u32, &str> = Ok(2);
760    /// assert_eq!(x.as_ref(), Ok(&2));
761    ///
762    /// let x: Result<u32, &str> = Err("Error");
763    /// assert_eq!(x.as_ref(), Err(&"Error"));
764    /// ```
765    #[inline]
766    #[rustc_const_stable(feature = "const_result_basics", since = "1.48.0")]
767    #[stable(feature = "rust1", since = "1.0.0")]
768    pub const fn as_ref(&self) -> Result<&T, &E> {
769        match *self {
770            Ok(ref x) => Ok(x),
771            Err(ref x) => Err(x),
772        }
773    }
774
775    /// Converts from `&mut Result<T, E>` to `Result<&mut T, &mut E>`.
776    ///
777    /// # Examples
778    ///
779    /// ```
780    /// fn mutate(r: &mut Result<i32, i32>) {
781    ///     match r.as_mut() {
782    ///         Ok(v) => *v = 42,
783    ///         Err(e) => *e = 0,
784    ///     }
785    /// }
786    ///
787    /// let mut x: Result<i32, i32> = Ok(2);
788    /// mutate(&mut x);
789    /// assert_eq!(x.unwrap(), 42);
790    ///
791    /// let mut x: Result<i32, i32> = Err(13);
792    /// mutate(&mut x);
793    /// assert_eq!(x.unwrap_err(), 0);
794    /// ```
795    #[inline]
796    #[stable(feature = "rust1", since = "1.0.0")]
797    #[rustc_const_stable(feature = "const_result", since = "1.83.0")]
798    pub const fn as_mut(&mut self) -> Result<&mut T, &mut E> {
799        match *self {
800            Ok(ref mut x) => Ok(x),
801            Err(ref mut x) => Err(x),
802        }
803    }
804
805    /////////////////////////////////////////////////////////////////////////
806    // Transforming contained values
807    /////////////////////////////////////////////////////////////////////////
808
809    /// Maps a `Result<T, E>` to `Result<U, E>` by applying a function to a
810    /// contained [`Ok`] value, leaving an [`Err`] value untouched.
811    ///
812    /// This function can be used to compose the results of two functions.
813    ///
814    /// # Examples
815    ///
816    /// Print the numbers on each line of a string multiplied by two.
817    ///
818    /// ```
819    /// let line = "1\n2\n3\n4\n";
820    ///
821    /// for num in line.lines() {
822    ///     match num.parse::<i32>().map(|i| i * 2) {
823    ///         Ok(n) => println!("{n}"),
824    ///         Err(..) => {}
825    ///     }
826    /// }
827    /// ```
828    #[inline]
829    #[stable(feature = "rust1", since = "1.0.0")]
830    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
831    pub const fn map<U, F>(self, op: F) -> Result<U, E>
832    where
833        F: [const] FnOnce(T) -> U + [const] Destruct,
834    {
835        match self {
836            Ok(t) => Ok(op(t)),
837            Err(e) => Err(e),
838        }
839    }
840
841    /// Returns the provided default (if [`Err`]), or
842    /// applies a function to the contained value (if [`Ok`]).
843    ///
844    /// Arguments passed to `map_or` are eagerly evaluated; if you are passing
845    /// the result of a function call, it is recommended to use [`map_or_else`],
846    /// which is lazily evaluated.
847    ///
848    /// [`map_or_else`]: Result::map_or_else
849    ///
850    /// # Examples
851    ///
852    /// ```
853    /// let x: Result<_, &str> = Ok("foo");
854    /// assert_eq!(x.map_or(42, |v| v.len()), 3);
855    ///
856    /// let x: Result<&str, _> = Err("bar");
857    /// assert_eq!(x.map_or(42, |v| v.len()), 42);
858    /// ```
859    #[inline]
860    #[stable(feature = "result_map_or", since = "1.41.0")]
861    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
862    #[must_use = "if you don't need the returned value, use `if let` instead"]
863    pub const fn map_or<U, F>(self, default: U, f: F) -> U
864    where
865        F: [const] FnOnce(T) -> U + [const] Destruct,
866        T: [const] Destruct,
867        E: [const] Destruct,
868        U: [const] Destruct,
869    {
870        match self {
871            Ok(t) => f(t),
872            Err(_) => default,
873        }
874    }
875
876    /// Maps a `Result<T, E>` to `U` by applying fallback function `default` to
877    /// a contained [`Err`] value, or function `f` to a contained [`Ok`] value.
878    ///
879    /// This function can be used to unpack a successful result
880    /// while handling an error.
881    ///
882    ///
883    /// # Examples
884    ///
885    /// ```
886    /// let k = 21;
887    ///
888    /// let x : Result<_, &str> = Ok("foo");
889    /// assert_eq!(x.map_or_else(|e| k * 2, |v| v.len()), 3);
890    ///
891    /// let x : Result<&str, _> = Err("bar");
892    /// assert_eq!(x.map_or_else(|e| k * 2, |v| v.len()), 42);
893    /// ```
894    #[inline]
895    #[stable(feature = "result_map_or_else", since = "1.41.0")]
896    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
897    pub const fn map_or_else<U, D, F>(self, default: D, f: F) -> U
898    where
899        D: [const] FnOnce(E) -> U + [const] Destruct,
900        F: [const] FnOnce(T) -> U + [const] Destruct,
901    {
902        match self {
903            Ok(t) => f(t),
904            Err(e) => default(e),
905        }
906    }
907
908    /// Maps a `Result<T, E>` to a `U` by applying function `f` to the contained
909    /// value if the result is [`Ok`], otherwise if [`Err`], returns the
910    /// [default value] for the type `U`.
911    ///
912    /// # Examples
913    ///
914    /// ```
915    /// #![feature(result_option_map_or_default)]
916    ///
917    /// let x: Result<_, &str> = Ok("foo");
918    /// let y: Result<&str, _> = Err("bar");
919    ///
920    /// assert_eq!(x.map_or_default(|x| x.len()), 3);
921    /// assert_eq!(y.map_or_default(|y| y.len()), 0);
922    /// ```
923    ///
924    /// [default value]: Default::default
925    #[inline]
926    #[unstable(feature = "result_option_map_or_default", issue = "138099")]
927    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
928    pub const fn map_or_default<U, F>(self, f: F) -> U
929    where
930        F: [const] FnOnce(T) -> U + [const] Destruct,
931        U: [const] Default,
932        T: [const] Destruct,
933        E: [const] Destruct,
934    {
935        match self {
936            Ok(t) => f(t),
937            Err(_) => U::default(),
938        }
939    }
940
941    /// Maps a `Result<T, E>` to `Result<T, F>` by applying a function to a
942    /// contained [`Err`] value, leaving an [`Ok`] value untouched.
943    ///
944    /// This function can be used to pass through a successful result while handling
945    /// an error.
946    ///
947    ///
948    /// # Examples
949    ///
950    /// ```
951    /// fn stringify(x: u32) -> String { format!("error code: {x}") }
952    ///
953    /// let x: Result<u32, u32> = Ok(2);
954    /// assert_eq!(x.map_err(stringify), Ok(2));
955    ///
956    /// let x: Result<u32, u32> = Err(13);
957    /// assert_eq!(x.map_err(stringify), Err("error code: 13".to_string()));
958    /// ```
959    #[inline]
960    #[stable(feature = "rust1", since = "1.0.0")]
961    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
962    pub const fn map_err<F, O>(self, op: O) -> Result<T, F>
963    where
964        O: [const] FnOnce(E) -> F + [const] Destruct,
965    {
966        match self {
967            Ok(t) => Ok(t),
968            Err(e) => Err(op(e)),
969        }
970    }
971
972    /// Calls a function with a reference to the contained value if [`Ok`].
973    ///
974    /// Returns the original result.
975    ///
976    /// # Examples
977    ///
978    /// ```
979    /// let x: u8 = "4"
980    ///     .parse::<u8>()
981    ///     .inspect(|x| println!("original: {x}"))
982    ///     .map(|x| x.pow(3))
983    ///     .expect("failed to parse number");
984    /// ```
985    #[inline]
986    #[stable(feature = "result_option_inspect", since = "1.76.0")]
987    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
988    pub const fn inspect<F>(self, f: F) -> Self
989    where
990        F: [const] FnOnce(&T) + [const] Destruct,
991    {
992        if let Ok(ref t) = self {
993            f(t);
994        }
995
996        self
997    }
998
999    /// Calls a function with a reference to the contained value if [`Err`].
1000    ///
1001    /// Returns the original result.
1002    ///
1003    /// # Examples
1004    ///
1005    /// ```
1006    /// use std::{fs, io};
1007    ///
1008    /// fn read() -> io::Result<String> {
1009    ///     fs::read_to_string("address.txt")
1010    ///         .inspect_err(|e| eprintln!("failed to read file: {e}"))
1011    /// }
1012    /// ```
1013    #[inline]
1014    #[stable(feature = "result_option_inspect", since = "1.76.0")]
1015    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1016    pub const fn inspect_err<F>(self, f: F) -> Self
1017    where
1018        F: [const] FnOnce(&E) + [const] Destruct,
1019    {
1020        if let Err(ref e) = self {
1021            f(e);
1022        }
1023
1024        self
1025    }
1026
1027    /// Converts from `Result<T, E>` (or `&Result<T, E>`) to `Result<&<T as Deref>::Target, &E>`.
1028    ///
1029    /// Coerces the [`Ok`] variant of the original [`Result`] via [`Deref`](crate::ops::Deref)
1030    /// and returns the new [`Result`].
1031    ///
1032    /// # Examples
1033    ///
1034    /// ```
1035    /// let x: Result<String, u32> = Ok("hello".to_string());
1036    /// let y: Result<&str, &u32> = Ok("hello");
1037    /// assert_eq!(x.as_deref(), y);
1038    ///
1039    /// let x: Result<String, u32> = Err(42);
1040    /// let y: Result<&str, &u32> = Err(&42);
1041    /// assert_eq!(x.as_deref(), y);
1042    /// ```
1043    #[inline]
1044    #[stable(feature = "inner_deref", since = "1.47.0")]
1045    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1046    pub const fn as_deref(&self) -> Result<&T::Target, &E>
1047    where
1048        T: [const] Deref,
1049    {
1050        self.as_ref().map(Deref::deref)
1051    }
1052
1053    /// Converts from `Result<T, E>` (or `&mut Result<T, E>`) to `Result<&mut <T as DerefMut>::Target, &mut E>`.
1054    ///
1055    /// Coerces the [`Ok`] variant of the original [`Result`] via [`DerefMut`](crate::ops::DerefMut)
1056    /// and returns the new [`Result`].
1057    ///
1058    /// # Examples
1059    ///
1060    /// ```
1061    /// let mut s = "HELLO".to_string();
1062    /// let mut x: Result<String, u32> = Ok("hello".to_string());
1063    /// let y: Result<&mut str, &mut u32> = Ok(&mut s);
1064    /// assert_eq!(x.as_deref_mut().map(|x| { x.make_ascii_uppercase(); x }), y);
1065    ///
1066    /// let mut i = 42;
1067    /// let mut x: Result<String, u32> = Err(42);
1068    /// let y: Result<&mut str, &mut u32> = Err(&mut i);
1069    /// assert_eq!(x.as_deref_mut().map(|x| { x.make_ascii_uppercase(); x }), y);
1070    /// ```
1071    #[inline]
1072    #[stable(feature = "inner_deref", since = "1.47.0")]
1073    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1074    pub const fn as_deref_mut(&mut self) -> Result<&mut T::Target, &mut E>
1075    where
1076        T: [const] DerefMut,
1077    {
1078        self.as_mut().map(DerefMut::deref_mut)
1079    }
1080
1081    /////////////////////////////////////////////////////////////////////////
1082    // Iterator constructors
1083    /////////////////////////////////////////////////////////////////////////
1084
1085    /// Returns an iterator over the possibly contained value.
1086    ///
1087    /// The iterator yields one value if the result is [`Result::Ok`], otherwise none.
1088    ///
1089    /// # Examples
1090    ///
1091    /// ```
1092    /// let x: Result<u32, &str> = Ok(7);
1093    /// assert_eq!(x.iter().next(), Some(&7));
1094    ///
1095    /// let x: Result<u32, &str> = Err("nothing!");
1096    /// assert_eq!(x.iter().next(), None);
1097    /// ```
1098    #[inline]
1099    #[stable(feature = "rust1", since = "1.0.0")]
1100    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1101    pub const fn iter(&self) -> Iter<'_, T> {
1102        Iter { inner: self.as_ref().ok() }
1103    }
1104
1105    /// Returns a mutable iterator over the possibly contained value.
1106    ///
1107    /// The iterator yields one value if the result is [`Result::Ok`], otherwise none.
1108    ///
1109    /// # Examples
1110    ///
1111    /// ```
1112    /// let mut x: Result<u32, &str> = Ok(7);
1113    /// match x.iter_mut().next() {
1114    ///     Some(v) => *v = 40,
1115    ///     None => {},
1116    /// }
1117    /// assert_eq!(x, Ok(40));
1118    ///
1119    /// let mut x: Result<u32, &str> = Err("nothing!");
1120    /// assert_eq!(x.iter_mut().next(), None);
1121    /// ```
1122    #[inline]
1123    #[stable(feature = "rust1", since = "1.0.0")]
1124    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1125    pub const fn iter_mut(&mut self) -> IterMut<'_, T> {
1126        IterMut { inner: self.as_mut().ok() }
1127    }
1128
1129    /////////////////////////////////////////////////////////////////////////
1130    // Extract a value
1131    /////////////////////////////////////////////////////////////////////////
1132
1133    /// Returns the contained [`Ok`] value, consuming the `self` value.
1134    ///
1135    /// Because this function may panic, its use is generally discouraged.
1136    /// Instead, prefer to use pattern matching and handle the [`Err`]
1137    /// case explicitly, or call [`unwrap_or`], [`unwrap_or_else`], or
1138    /// [`unwrap_or_default`].
1139    ///
1140    /// [`unwrap_or`]: Result::unwrap_or
1141    /// [`unwrap_or_else`]: Result::unwrap_or_else
1142    /// [`unwrap_or_default`]: Result::unwrap_or_default
1143    ///
1144    /// # Panics
1145    ///
1146    /// Panics if the value is an [`Err`], with a panic message including the
1147    /// passed message, and the content of the [`Err`].
1148    ///
1149    ///
1150    /// # Examples
1151    ///
1152    /// ```should_panic
1153    /// let x: Result<u32, &str> = Err("emergency failure");
1154    /// x.expect("Testing expect"); // panics with `Testing expect: emergency failure`
1155    /// ```
1156    ///
1157    /// # Recommended Message Style
1158    ///
1159    /// We recommend that `expect` messages are used to describe the reason you
1160    /// _expect_ the `Result` should be `Ok`.
1161    ///
1162    /// ```should_panic
1163    /// let path = std::env::var("IMPORTANT_PATH")
1164    ///     .expect("env variable `IMPORTANT_PATH` should be set by `wrapper_script.sh`");
1165    /// ```
1166    ///
1167    /// **Hint**: If you're having trouble remembering how to phrase expect
1168    /// error messages remember to focus on the word "should" as in "env
1169    /// variable should be set by blah" or "the given binary should be available
1170    /// and executable by the current user".
1171    ///
1172    /// For more detail on expect message styles and the reasoning behind our recommendation please
1173    /// refer to the section on ["Common Message
1174    /// Styles"](../../std/error/index.html#common-message-styles) in the
1175    /// [`std::error`](../../std/error/index.html) module docs.
1176    #[inline]
1177    #[track_caller]
1178    #[stable(feature = "result_expect", since = "1.4.0")]
1179    pub fn expect(self, msg: &str) -> T
1180    where
1181        E: fmt::Debug,
1182    {
1183        match self {
1184            Ok(t) => t,
1185            Err(e) => unwrap_failed(msg, &e),
1186        }
1187    }
1188
1189    /// Returns the contained [`Ok`] value, consuming the `self` value.
1190    ///
1191    /// Because this function may panic, its use is generally discouraged.
1192    /// Panics are meant for unrecoverable errors, and
1193    /// [may abort the entire program][panic-abort].
1194    ///
1195    /// Instead, prefer to use [the `?` (try) operator][try-operator], or pattern matching
1196    /// to handle the [`Err`] case explicitly, or call [`unwrap_or`],
1197    /// [`unwrap_or_else`], or [`unwrap_or_default`].
1198    ///
1199    /// [panic-abort]: https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic.html
1200    /// [try-operator]: https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#a-shortcut-for-propagating-errors-the--operator
1201    /// [`unwrap_or`]: Result::unwrap_or
1202    /// [`unwrap_or_else`]: Result::unwrap_or_else
1203    /// [`unwrap_or_default`]: Result::unwrap_or_default
1204    ///
1205    /// # Panics
1206    ///
1207    /// Panics if the value is an [`Err`], with a panic message provided by the
1208    /// [`Err`]'s value.
1209    ///
1210    ///
1211    /// # Examples
1212    ///
1213    /// Basic usage:
1214    ///
1215    /// ```
1216    /// let x: Result<u32, &str> = Ok(2);
1217    /// assert_eq!(x.unwrap(), 2);
1218    /// ```
1219    ///
1220    /// ```should_panic
1221    /// let x: Result<u32, &str> = Err("emergency failure");
1222    /// x.unwrap(); // panics with `emergency failure`
1223    /// ```
1224    #[inline(always)]
1225    #[track_caller]
1226    #[stable(feature = "rust1", since = "1.0.0")]
1227    pub fn unwrap(self) -> T
1228    where
1229        E: fmt::Debug,
1230    {
1231        match self {
1232            Ok(t) => t,
1233            Err(e) => unwrap_failed("called `Result::unwrap()` on an `Err` value", &e),
1234        }
1235    }
1236
1237    /// Returns the contained [`Ok`] value or a default
1238    ///
1239    /// Consumes the `self` argument then, if [`Ok`], returns the contained
1240    /// value, otherwise if [`Err`], returns the default value for that
1241    /// type.
1242    ///
1243    /// # Examples
1244    ///
1245    /// Converts a string to an integer, turning poorly-formed strings
1246    /// into 0 (the default value for integers). [`parse`] converts
1247    /// a string to any other type that implements [`FromStr`], returning an
1248    /// [`Err`] on error.
1249    ///
1250    /// ```
1251    /// let good_year_from_input = "1909";
1252    /// let bad_year_from_input = "190blarg";
1253    /// let good_year = good_year_from_input.parse().unwrap_or_default();
1254    /// let bad_year = bad_year_from_input.parse().unwrap_or_default();
1255    ///
1256    /// assert_eq!(1909, good_year);
1257    /// assert_eq!(0, bad_year);
1258    /// ```
1259    ///
1260    /// [`parse`]: str::parse
1261    /// [`FromStr`]: crate::str::FromStr
1262    #[inline]
1263    #[stable(feature = "result_unwrap_or_default", since = "1.16.0")]
1264    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1265    pub const fn unwrap_or_default(self) -> T
1266    where
1267        T: [const] Default + [const] Destruct,
1268        E: [const] Destruct,
1269    {
1270        match self {
1271            Ok(x) => x,
1272            Err(_) => Default::default(),
1273        }
1274    }
1275
1276    /// Returns the contained [`Err`] value, consuming the `self` value.
1277    ///
1278    /// # Panics
1279    ///
1280    /// Panics if the value is an [`Ok`], with a panic message including the
1281    /// passed message, and the content of the [`Ok`].
1282    ///
1283    ///
1284    /// # Examples
1285    ///
1286    /// ```should_panic
1287    /// let x: Result<u32, &str> = Ok(10);
1288    /// x.expect_err("Testing expect_err"); // panics with `Testing expect_err: 10`
1289    /// ```
1290    #[inline]
1291    #[track_caller]
1292    #[stable(feature = "result_expect_err", since = "1.17.0")]
1293    pub fn expect_err(self, msg: &str) -> E
1294    where
1295        T: fmt::Debug,
1296    {
1297        match self {
1298            Ok(t) => unwrap_failed(msg, &t),
1299            Err(e) => e,
1300        }
1301    }
1302
1303    /// Returns the contained [`Err`] value, consuming the `self` value.
1304    ///
1305    /// # Panics
1306    ///
1307    /// Panics if the value is an [`Ok`], with a custom panic message provided
1308    /// by the [`Ok`]'s value.
1309    ///
1310    /// # Examples
1311    ///
1312    /// ```should_panic
1313    /// let x: Result<u32, &str> = Ok(2);
1314    /// x.unwrap_err(); // panics with `2`
1315    /// ```
1316    ///
1317    /// ```
1318    /// let x: Result<u32, &str> = Err("emergency failure");
1319    /// assert_eq!(x.unwrap_err(), "emergency failure");
1320    /// ```
1321    #[inline]
1322    #[track_caller]
1323    #[stable(feature = "rust1", since = "1.0.0")]
1324    pub fn unwrap_err(self) -> E
1325    where
1326        T: fmt::Debug,
1327    {
1328        match self {
1329            Ok(t) => unwrap_failed("called `Result::unwrap_err()` on an `Ok` value", &t),
1330            Err(e) => e,
1331        }
1332    }
1333
1334    /// Returns the contained [`Ok`] value, but never panics.
1335    ///
1336    /// Unlike [`unwrap`], this method is known to never panic on the
1337    /// result types it is implemented for. Therefore, it can be used
1338    /// instead of `unwrap` as a maintainability safeguard that will fail
1339    /// to compile if the error type of the `Result` is later changed
1340    /// to an error that can actually occur.
1341    ///
1342    /// [`unwrap`]: Result::unwrap
1343    ///
1344    /// # Examples
1345    ///
1346    /// ```
1347    /// # #![feature(never_type)]
1348    /// # #![feature(unwrap_infallible)]
1349    ///
1350    /// fn only_good_news() -> Result<String, !> {
1351    ///     Ok("this is fine".into())
1352    /// }
1353    ///
1354    /// let s: String = only_good_news().into_ok();
1355    /// println!("{s}");
1356    /// ```
1357    #[unstable(feature = "unwrap_infallible", issue = "61695")]
1358    #[inline]
1359    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1360    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1361    pub const fn into_ok(self) -> T
1362    where
1363        E: [const] Into<!>,
1364    {
1365        match self {
1366            Ok(x) => x,
1367            Err(e) => e.into(),
1368        }
1369    }
1370
1371    /// Returns the contained [`Err`] value, but never panics.
1372    ///
1373    /// Unlike [`unwrap_err`], this method is known to never panic on the
1374    /// result types it is implemented for. Therefore, it can be used
1375    /// instead of `unwrap_err` as a maintainability safeguard that will fail
1376    /// to compile if the ok type of the `Result` is later changed
1377    /// to a type that can actually occur.
1378    ///
1379    /// [`unwrap_err`]: Result::unwrap_err
1380    ///
1381    /// # Examples
1382    ///
1383    /// ```
1384    /// # #![feature(never_type)]
1385    /// # #![feature(unwrap_infallible)]
1386    ///
1387    /// fn only_bad_news() -> Result<!, String> {
1388    ///     Err("Oops, it failed".into())
1389    /// }
1390    ///
1391    /// let error: String = only_bad_news().into_err();
1392    /// println!("{error}");
1393    /// ```
1394    #[unstable(feature = "unwrap_infallible", issue = "61695")]
1395    #[inline]
1396    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1397    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1398    pub const fn into_err(self) -> E
1399    where
1400        T: [const] Into<!>,
1401    {
1402        match self {
1403            Ok(x) => x.into(),
1404            Err(e) => e,
1405        }
1406    }
1407
1408    ////////////////////////////////////////////////////////////////////////
1409    // Boolean operations on the values, eager and lazy
1410    /////////////////////////////////////////////////////////////////////////
1411
1412    /// Returns `res` if the result is [`Ok`], otherwise returns the [`Err`] value of `self`.
1413    ///
1414    /// Arguments passed to `and` are eagerly evaluated; if you are passing the
1415    /// result of a function call, it is recommended to use [`and_then`], which is
1416    /// lazily evaluated.
1417    ///
1418    /// [`and_then`]: Result::and_then
1419    ///
1420    /// # Examples
1421    ///
1422    /// ```
1423    /// let x: Result<u32, &str> = Ok(2);
1424    /// let y: Result<&str, &str> = Err("late error");
1425    /// assert_eq!(x.and(y), Err("late error"));
1426    ///
1427    /// let x: Result<u32, &str> = Err("early error");
1428    /// let y: Result<&str, &str> = Ok("foo");
1429    /// assert_eq!(x.and(y), Err("early error"));
1430    ///
1431    /// let x: Result<u32, &str> = Err("not a 2");
1432    /// let y: Result<&str, &str> = Err("late error");
1433    /// assert_eq!(x.and(y), Err("not a 2"));
1434    ///
1435    /// let x: Result<u32, &str> = Ok(2);
1436    /// let y: Result<&str, &str> = Ok("different result type");
1437    /// assert_eq!(x.and(y), Ok("different result type"));
1438    /// ```
1439    #[inline]
1440    #[stable(feature = "rust1", since = "1.0.0")]
1441    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1442    pub const fn and<U>(self, res: Result<U, E>) -> Result<U, E>
1443    where
1444        T: [const] Destruct,
1445        E: [const] Destruct,
1446        U: [const] Destruct,
1447    {
1448        match self {
1449            Ok(_) => res,
1450            Err(e) => Err(e),
1451        }
1452    }
1453
1454    /// Calls `op` if the result is [`Ok`], otherwise returns the [`Err`] value of `self`.
1455    ///
1456    ///
1457    /// This function can be used for control flow based on `Result` values.
1458    ///
1459    /// # Examples
1460    ///
1461    /// ```
1462    /// fn sq_then_to_string(x: u32) -> Result<String, &'static str> {
1463    ///     x.checked_mul(x).map(|sq| sq.to_string()).ok_or("overflowed")
1464    /// }
1465    ///
1466    /// assert_eq!(Ok(2).and_then(sq_then_to_string), Ok(4.to_string()));
1467    /// assert_eq!(Ok(1_000_000).and_then(sq_then_to_string), Err("overflowed"));
1468    /// assert_eq!(Err("not a number").and_then(sq_then_to_string), Err("not a number"));
1469    /// ```
1470    ///
1471    /// Often used to chain fallible operations that may return [`Err`].
1472    ///
1473    /// ```
1474    /// use std::{io::ErrorKind, path::Path};
1475    ///
1476    /// // Note: on Windows "/" maps to "C:\"
1477    /// let root_modified_time = Path::new("/").metadata().and_then(|md| md.modified());
1478    /// assert!(root_modified_time.is_ok());
1479    ///
1480    /// let should_fail = Path::new("/bad/path").metadata().and_then(|md| md.modified());
1481    /// assert!(should_fail.is_err());
1482    /// assert_eq!(should_fail.unwrap_err().kind(), ErrorKind::NotFound);
1483    /// ```
1484    #[inline]
1485    #[stable(feature = "rust1", since = "1.0.0")]
1486    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1487    #[rustc_confusables("flat_map", "flatmap")]
1488    pub const fn and_then<U, F>(self, op: F) -> Result<U, E>
1489    where
1490        F: [const] FnOnce(T) -> Result<U, E> + [const] Destruct,
1491    {
1492        match self {
1493            Ok(t) => op(t),
1494            Err(e) => Err(e),
1495        }
1496    }
1497
1498    /// Returns `res` if the result is [`Err`], otherwise returns the [`Ok`] value of `self`.
1499    ///
1500    /// Arguments passed to `or` are eagerly evaluated; if you are passing the
1501    /// result of a function call, it is recommended to use [`or_else`], which is
1502    /// lazily evaluated.
1503    ///
1504    /// [`or_else`]: Result::or_else
1505    ///
1506    /// # Examples
1507    ///
1508    /// ```
1509    /// let x: Result<u32, &str> = Ok(2);
1510    /// let y: Result<u32, &str> = Err("late error");
1511    /// assert_eq!(x.or(y), Ok(2));
1512    ///
1513    /// let x: Result<u32, &str> = Err("early error");
1514    /// let y: Result<u32, &str> = Ok(2);
1515    /// assert_eq!(x.or(y), Ok(2));
1516    ///
1517    /// let x: Result<u32, &str> = Err("not a 2");
1518    /// let y: Result<u32, &str> = Err("late error");
1519    /// assert_eq!(x.or(y), Err("late error"));
1520    ///
1521    /// let x: Result<u32, &str> = Ok(2);
1522    /// let y: Result<u32, &str> = Ok(100);
1523    /// assert_eq!(x.or(y), Ok(2));
1524    /// ```
1525    #[inline]
1526    #[stable(feature = "rust1", since = "1.0.0")]
1527    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1528    pub const fn or<F>(self, res: Result<T, F>) -> Result<T, F>
1529    where
1530        T: [const] Destruct,
1531        E: [const] Destruct,
1532        F: [const] Destruct,
1533    {
1534        match self {
1535            Ok(v) => Ok(v),
1536            Err(_) => res,
1537        }
1538    }
1539
1540    /// Calls `op` if the result is [`Err`], otherwise returns the [`Ok`] value of `self`.
1541    ///
1542    /// This function can be used for control flow based on result values.
1543    ///
1544    ///
1545    /// # Examples
1546    ///
1547    /// ```
1548    /// fn sq(x: u32) -> Result<u32, u32> { Ok(x * x) }
1549    /// fn err(x: u32) -> Result<u32, u32> { Err(x) }
1550    ///
1551    /// assert_eq!(Ok(2).or_else(sq).or_else(sq), Ok(2));
1552    /// assert_eq!(Ok(2).or_else(err).or_else(sq), Ok(2));
1553    /// assert_eq!(Err(3).or_else(sq).or_else(err), Ok(9));
1554    /// assert_eq!(Err(3).or_else(err).or_else(err), Err(3));
1555    /// ```
1556    #[inline]
1557    #[stable(feature = "rust1", since = "1.0.0")]
1558    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1559    pub const fn or_else<F, O>(self, op: O) -> Result<T, F>
1560    where
1561        O: [const] FnOnce(E) -> Result<T, F> + [const] Destruct,
1562    {
1563        match self {
1564            Ok(t) => Ok(t),
1565            Err(e) => op(e),
1566        }
1567    }
1568
1569    /// Returns the contained [`Ok`] value or a provided default.
1570    ///
1571    /// Arguments passed to `unwrap_or` are eagerly evaluated; if you are passing
1572    /// the result of a function call, it is recommended to use [`unwrap_or_else`],
1573    /// which is lazily evaluated.
1574    ///
1575    /// [`unwrap_or_else`]: Result::unwrap_or_else
1576    ///
1577    /// # Examples
1578    ///
1579    /// ```
1580    /// let default = 2;
1581    /// let x: Result<u32, &str> = Ok(9);
1582    /// assert_eq!(x.unwrap_or(default), 9);
1583    ///
1584    /// let x: Result<u32, &str> = Err("error");
1585    /// assert_eq!(x.unwrap_or(default), default);
1586    /// ```
1587    #[inline]
1588    #[stable(feature = "rust1", since = "1.0.0")]
1589    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1590    pub const fn unwrap_or(self, default: T) -> T
1591    where
1592        T: [const] Destruct,
1593        E: [const] Destruct,
1594    {
1595        match self {
1596            Ok(t) => t,
1597            Err(_) => default,
1598        }
1599    }
1600
1601    /// Returns the contained [`Ok`] value or computes it from a closure.
1602    ///
1603    ///
1604    /// # Examples
1605    ///
1606    /// ```
1607    /// fn count(x: &str) -> usize { x.len() }
1608    ///
1609    /// assert_eq!(Ok(2).unwrap_or_else(count), 2);
1610    /// assert_eq!(Err("foo").unwrap_or_else(count), 3);
1611    /// ```
1612    #[inline]
1613    #[track_caller]
1614    #[stable(feature = "rust1", since = "1.0.0")]
1615    #[rustc_const_unstable(feature = "const_result_trait_fn", issue = "144211")]
1616    pub const fn unwrap_or_else<F>(self, op: F) -> T
1617    where
1618        F: [const] FnOnce(E) -> T + [const] Destruct,
1619    {
1620        match self {
1621            Ok(t) => t,
1622            Err(e) => op(e),
1623        }
1624    }
1625
1626    /// Returns the contained [`Ok`] value, consuming the `self` value,
1627    /// without checking that the value is not an [`Err`].
1628    ///
1629    /// # Safety
1630    ///
1631    /// Calling this method on an [`Err`] is *[undefined behavior]*.
1632    ///
1633    /// [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
1634    ///
1635    /// # Examples
1636    ///
1637    /// ```
1638    /// let x: Result<u32, &str> = Ok(2);
1639    /// assert_eq!(unsafe { x.unwrap_unchecked() }, 2);
1640    /// ```
1641    ///
1642    /// ```no_run
1643    /// let x: Result<u32, &str> = Err("emergency failure");
1644    /// unsafe { x.unwrap_unchecked() }; // Undefined behavior!
1645    /// ```
1646    #[inline]
1647    #[track_caller]
1648    #[stable(feature = "option_result_unwrap_unchecked", since = "1.58.0")]
1649    #[rustc_const_unstable(feature = "const_result_unwrap_unchecked", issue = "148714")]
1650    pub const unsafe fn unwrap_unchecked(self) -> T {
1651        match self {
1652            Ok(t) => t,
1653            Err(e) => {
1654                // FIXME(const-hack): to avoid E: const Destruct bound
1655                super::mem::forget(e);
1656                // SAFETY: the safety contract must be upheld by the caller.
1657                unsafe { hint::unreachable_unchecked() }
1658            }
1659        }
1660    }
1661
1662    /// Returns the contained [`Err`] value, consuming the `self` value,
1663    /// without checking that the value is not an [`Ok`].
1664    ///
1665    /// # Safety
1666    ///
1667    /// Calling this method on an [`Ok`] is *[undefined behavior]*.
1668    ///
1669    /// [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
1670    ///
1671    /// # Examples
1672    ///
1673    /// ```no_run
1674    /// let x: Result<u32, &str> = Ok(2);
1675    /// unsafe { x.unwrap_err_unchecked() }; // Undefined behavior!
1676    /// ```
1677    ///
1678    /// ```
1679    /// let x: Result<u32, &str> = Err("emergency failure");
1680    /// assert_eq!(unsafe { x.unwrap_err_unchecked() }, "emergency failure");
1681    /// ```
1682    #[inline]
1683    #[track_caller]
1684    #[stable(feature = "option_result_unwrap_unchecked", since = "1.58.0")]
1685    pub unsafe fn unwrap_err_unchecked(self) -> E {
1686        match self {
1687            // SAFETY: the safety contract must be upheld by the caller.
1688            Ok(_) => unsafe { hint::unreachable_unchecked() },
1689            Err(e) => e,
1690        }
1691    }
1692}
1693
1694impl<T, E> Result<&T, E> {
1695    /// Maps a `Result<&T, E>` to a `Result<T, E>` by copying the contents of the
1696    /// `Ok` part.
1697    ///
1698    /// # Examples
1699    ///
1700    /// ```
1701    /// let val = 12;
1702    /// let x: Result<&i32, i32> = Ok(&val);
1703    /// assert_eq!(x, Ok(&12));
1704    /// let copied = x.copied();
1705    /// assert_eq!(copied, Ok(12));
1706    /// ```
1707    #[inline]
1708    #[stable(feature = "result_copied", since = "1.59.0")]
1709    #[rustc_const_stable(feature = "const_result", since = "1.83.0")]
1710    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1711    pub const fn copied(self) -> Result<T, E>
1712    where
1713        T: Copy,
1714    {
1715        // FIXME(const-hack): this implementation, which sidesteps using `Result::map` since it's not const
1716        // ready yet, should be reverted when possible to avoid code repetition
1717        match self {
1718            Ok(&v) => Ok(v),
1719            Err(e) => Err(e),
1720        }
1721    }
1722
1723    /// Maps a `Result<&T, E>` to a `Result<T, E>` by cloning the contents of the
1724    /// `Ok` part.
1725    ///
1726    /// # Examples
1727    ///
1728    /// ```
1729    /// let val = 12;
1730    /// let x: Result<&i32, i32> = Ok(&val);
1731    /// assert_eq!(x, Ok(&12));
1732    /// let cloned = x.cloned();
1733    /// assert_eq!(cloned, Ok(12));
1734    /// ```
1735    #[inline]
1736    #[stable(feature = "result_cloned", since = "1.59.0")]
1737    pub fn cloned(self) -> Result<T, E>
1738    where
1739        T: Clone,
1740    {
1741        self.map(|t| t.clone())
1742    }
1743}
1744
1745impl<T, E> Result<&mut T, E> {
1746    /// Maps a `Result<&mut T, E>` to a `Result<T, E>` by copying the contents of the
1747    /// `Ok` part.
1748    ///
1749    /// # Examples
1750    ///
1751    /// ```
1752    /// let mut val = 12;
1753    /// let x: Result<&mut i32, i32> = Ok(&mut val);
1754    /// assert_eq!(x, Ok(&mut 12));
1755    /// let copied = x.copied();
1756    /// assert_eq!(copied, Ok(12));
1757    /// ```
1758    #[inline]
1759    #[stable(feature = "result_copied", since = "1.59.0")]
1760    #[rustc_const_stable(feature = "const_result", since = "1.83.0")]
1761    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1762    pub const fn copied(self) -> Result<T, E>
1763    where
1764        T: Copy,
1765    {
1766        // FIXME(const-hack): this implementation, which sidesteps using `Result::map` since it's not const
1767        // ready yet, should be reverted when possible to avoid code repetition
1768        match self {
1769            Ok(&mut v) => Ok(v),
1770            Err(e) => Err(e),
1771        }
1772    }
1773
1774    /// Maps a `Result<&mut T, E>` to a `Result<T, E>` by cloning the contents of the
1775    /// `Ok` part.
1776    ///
1777    /// # Examples
1778    ///
1779    /// ```
1780    /// let mut val = 12;
1781    /// let x: Result<&mut i32, i32> = Ok(&mut val);
1782    /// assert_eq!(x, Ok(&mut 12));
1783    /// let cloned = x.cloned();
1784    /// assert_eq!(cloned, Ok(12));
1785    /// ```
1786    #[inline]
1787    #[stable(feature = "result_cloned", since = "1.59.0")]
1788    pub fn cloned(self) -> Result<T, E>
1789    where
1790        T: Clone,
1791    {
1792        self.map(|t| t.clone())
1793    }
1794}
1795
1796impl<T, E> Result<Option<T>, E> {
1797    /// Transposes a `Result` of an `Option` into an `Option` of a `Result`.
1798    ///
1799    /// `Ok(None)` will be mapped to `None`.
1800    /// `Ok(Some(_))` and `Err(_)` will be mapped to `Some(Ok(_))` and `Some(Err(_))`.
1801    ///
1802    /// # Examples
1803    ///
1804    /// ```
1805    /// #[derive(Debug, Eq, PartialEq)]
1806    /// struct SomeErr;
1807    ///
1808    /// let x: Result<Option<i32>, SomeErr> = Ok(Some(5));
1809    /// let y: Option<Result<i32, SomeErr>> = Some(Ok(5));
1810    /// assert_eq!(x.transpose(), y);
1811    /// ```
1812    #[inline]
1813    #[stable(feature = "transpose_result", since = "1.33.0")]
1814    #[rustc_const_stable(feature = "const_result", since = "1.83.0")]
1815    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1816    pub const fn transpose(self) -> Option<Result<T, E>> {
1817        match self {
1818            Ok(Some(x)) => Some(Ok(x)),
1819            Ok(None) => None,
1820            Err(e) => Some(Err(e)),
1821        }
1822    }
1823}
1824
1825impl<T, E> Result<Result<T, E>, E> {
1826    /// Converts from `Result<Result<T, E>, E>` to `Result<T, E>`
1827    ///
1828    /// # Examples
1829    ///
1830    /// ```
1831    /// let x: Result<Result<&'static str, u32>, u32> = Ok(Ok("hello"));
1832    /// assert_eq!(Ok("hello"), x.flatten());
1833    ///
1834    /// let x: Result<Result<&'static str, u32>, u32> = Ok(Err(6));
1835    /// assert_eq!(Err(6), x.flatten());
1836    ///
1837    /// let x: Result<Result<&'static str, u32>, u32> = Err(6);
1838    /// assert_eq!(Err(6), x.flatten());
1839    /// ```
1840    ///
1841    /// Flattening only removes one level of nesting at a time:
1842    ///
1843    /// ```
1844    /// let x: Result<Result<Result<&'static str, u32>, u32>, u32> = Ok(Ok(Ok("hello")));
1845    /// assert_eq!(Ok(Ok("hello")), x.flatten());
1846    /// assert_eq!(Ok("hello"), x.flatten().flatten());
1847    /// ```
1848    #[inline]
1849    #[stable(feature = "result_flattening", since = "1.89.0")]
1850    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1851    #[rustc_const_stable(feature = "result_flattening", since = "1.89.0")]
1852    pub const fn flatten(self) -> Result<T, E> {
1853        // FIXME(const-hack): could be written with `and_then`
1854        match self {
1855            Ok(inner) => inner,
1856            Err(e) => Err(e),
1857        }
1858    }
1859}
1860
1861// This is a separate function to reduce the code size of the methods
1862#[cfg(not(panic = "immediate-abort"))]
1863#[inline(never)]
1864#[cold]
1865#[track_caller]
1866fn unwrap_failed(msg: &str, error: &dyn fmt::Debug) -> ! {
1867    panic!("{msg}: {error:?}");
1868}
1869
1870// This is a separate function to avoid constructing a `dyn Debug`
1871// that gets immediately thrown away, since vtables don't get cleaned up
1872// by dead code elimination if a trait object is constructed even if it goes
1873// unused
1874#[cfg(panic = "immediate-abort")]
1875#[inline]
1876#[cold]
1877#[track_caller]
1878const fn unwrap_failed<T>(_msg: &str, _error: &T) -> ! {
1879    panic!()
1880}
1881
1882/////////////////////////////////////////////////////////////////////////////
1883// Trait implementations
1884/////////////////////////////////////////////////////////////////////////////
1885
1886#[stable(feature = "rust1", since = "1.0.0")]
1887impl<T, E> Clone for Result<T, E>
1888where
1889    T: Clone,
1890    E: Clone,
1891{
1892    #[inline]
1893    fn clone(&self) -> Self {
1894        match self {
1895            Ok(x) => Ok(x.clone()),
1896            Err(x) => Err(x.clone()),
1897        }
1898    }
1899
1900    #[inline]
1901    fn clone_from(&mut self, source: &Self) {
1902        match (self, source) {
1903            (Ok(to), Ok(from)) => to.clone_from(from),
1904            (Err(to), Err(from)) => to.clone_from(from),
1905            (to, from) => *to = from.clone(),
1906        }
1907    }
1908}
1909
1910#[unstable(feature = "ergonomic_clones", issue = "132290")]
1911impl<T, E> crate::clone::UseCloned for Result<T, E>
1912where
1913    T: crate::clone::UseCloned,
1914    E: crate::clone::UseCloned,
1915{
1916}
1917
1918#[stable(feature = "rust1", since = "1.0.0")]
1919impl<T, E> IntoIterator for Result<T, E> {
1920    type Item = T;
1921    type IntoIter = IntoIter<T>;
1922
1923    /// Returns a consuming iterator over the possibly contained value.
1924    ///
1925    /// The iterator yields one value if the result is [`Result::Ok`], otherwise none.
1926    ///
1927    /// # Examples
1928    ///
1929    /// ```
1930    /// let x: Result<u32, &str> = Ok(5);
1931    /// let v: Vec<u32> = x.into_iter().collect();
1932    /// assert_eq!(v, [5]);
1933    ///
1934    /// let x: Result<u32, &str> = Err("nothing!");
1935    /// let v: Vec<u32> = x.into_iter().collect();
1936    /// assert_eq!(v, []);
1937    /// ```
1938    #[inline]
1939    fn into_iter(self) -> IntoIter<T> {
1940        IntoIter { inner: self.ok() }
1941    }
1942}
1943
1944#[stable(since = "1.4.0", feature = "result_iter")]
1945impl<'a, T, E> IntoIterator for &'a Result<T, E> {
1946    type Item = &'a T;
1947    type IntoIter = Iter<'a, T>;
1948
1949    fn into_iter(self) -> Iter<'a, T> {
1950        self.iter()
1951    }
1952}
1953
1954#[stable(since = "1.4.0", feature = "result_iter")]
1955impl<'a, T, E> IntoIterator for &'a mut Result<T, E> {
1956    type Item = &'a mut T;
1957    type IntoIter = IterMut<'a, T>;
1958
1959    fn into_iter(self) -> IterMut<'a, T> {
1960        self.iter_mut()
1961    }
1962}
1963
1964/////////////////////////////////////////////////////////////////////////////
1965// The Result Iterators
1966/////////////////////////////////////////////////////////////////////////////
1967
1968/// An iterator over a reference to the [`Ok`] variant of a [`Result`].
1969///
1970/// The iterator yields one value if the result is [`Ok`], otherwise none.
1971///
1972/// Created by [`Result::iter`].
1973#[derive(Debug)]
1974#[stable(feature = "rust1", since = "1.0.0")]
1975pub struct Iter<'a, T: 'a> {
1976    inner: Option<&'a T>,
1977}
1978
1979#[stable(feature = "rust1", since = "1.0.0")]
1980impl<'a, T> Iterator for Iter<'a, T> {
1981    type Item = &'a T;
1982
1983    #[inline]
1984    fn next(&mut self) -> Option<&'a T> {
1985        self.inner.take()
1986    }
1987    #[inline]
1988    fn size_hint(&self) -> (usize, Option<usize>) {
1989        let n = if self.inner.is_some() { 1 } else { 0 };
1990        (n, Some(n))
1991    }
1992}
1993
1994#[stable(feature = "rust1", since = "1.0.0")]
1995impl<'a, T> DoubleEndedIterator for Iter<'a, T> {
1996    #[inline]
1997    fn next_back(&mut self) -> Option<&'a T> {
1998        self.inner.take()
1999    }
2000}
2001
2002#[stable(feature = "rust1", since = "1.0.0")]
2003impl<T> ExactSizeIterator for Iter<'_, T> {}
2004
2005#[stable(feature = "fused", since = "1.26.0")]
2006impl<T> FusedIterator for Iter<'_, T> {}
2007
2008#[unstable(feature = "trusted_len", issue = "37572")]
2009unsafe impl<A> TrustedLen for Iter<'_, A> {}
2010
2011#[stable(feature = "rust1", since = "1.0.0")]
2012impl<T> Clone for Iter<'_, T> {
2013    #[inline]
2014    fn clone(&self) -> Self {
2015        Iter { inner: self.inner }
2016    }
2017}
2018
2019/// An iterator over a mutable reference to the [`Ok`] variant of a [`Result`].
2020///
2021/// Created by [`Result::iter_mut`].
2022#[derive(Debug)]
2023#[stable(feature = "rust1", since = "1.0.0")]
2024pub struct IterMut<'a, T: 'a> {
2025    inner: Option<&'a mut T>,
2026}
2027
2028#[stable(feature = "rust1", since = "1.0.0")]
2029impl<'a, T> Iterator for IterMut<'a, T> {
2030    type Item = &'a mut T;
2031
2032    #[inline]
2033    fn next(&mut self) -> Option<&'a mut T> {
2034        self.inner.take()
2035    }
2036    #[inline]
2037    fn size_hint(&self) -> (usize, Option<usize>) {
2038        let n = if self.inner.is_some() { 1 } else { 0 };
2039        (n, Some(n))
2040    }
2041}
2042
2043#[stable(feature = "rust1", since = "1.0.0")]
2044impl<'a, T> DoubleEndedIterator for IterMut<'a, T> {
2045    #[inline]
2046    fn next_back(&mut self) -> Option<&'a mut T> {
2047        self.inner.take()
2048    }
2049}
2050
2051#[stable(feature = "rust1", since = "1.0.0")]
2052impl<T> ExactSizeIterator for IterMut<'_, T> {}
2053
2054#[stable(feature = "fused", since = "1.26.0")]
2055impl<T> FusedIterator for IterMut<'_, T> {}
2056
2057#[unstable(feature = "trusted_len", issue = "37572")]
2058unsafe impl<A> TrustedLen for IterMut<'_, A> {}
2059
2060/// An iterator over the value in a [`Ok`] variant of a [`Result`].
2061///
2062/// The iterator yields one value if the result is [`Ok`], otherwise none.
2063///
2064/// This struct is created by the [`into_iter`] method on
2065/// [`Result`] (provided by the [`IntoIterator`] trait).
2066///
2067/// [`into_iter`]: IntoIterator::into_iter
2068#[derive(Clone, Debug)]
2069#[stable(feature = "rust1", since = "1.0.0")]
2070pub struct IntoIter<T> {
2071    inner: Option<T>,
2072}
2073
2074#[stable(feature = "rust1", since = "1.0.0")]
2075impl<T> Iterator for IntoIter<T> {
2076    type Item = T;
2077
2078    #[inline]
2079    fn next(&mut self) -> Option<T> {
2080        self.inner.take()
2081    }
2082    #[inline]
2083    fn size_hint(&self) -> (usize, Option<usize>) {
2084        let n = if self.inner.is_some() { 1 } else { 0 };
2085        (n, Some(n))
2086    }
2087}
2088
2089#[stable(feature = "rust1", since = "1.0.0")]
2090impl<T> DoubleEndedIterator for IntoIter<T> {
2091    #[inline]
2092    fn next_back(&mut self) -> Option<T> {
2093        self.inner.take()
2094    }
2095}
2096
2097#[stable(feature = "rust1", since = "1.0.0")]
2098impl<T> ExactSizeIterator for IntoIter<T> {}
2099
2100#[stable(feature = "fused", since = "1.26.0")]
2101impl<T> FusedIterator for IntoIter<T> {}
2102
2103#[unstable(feature = "trusted_len", issue = "37572")]
2104unsafe impl<A> TrustedLen for IntoIter<A> {}
2105
2106/////////////////////////////////////////////////////////////////////////////
2107// FromIterator
2108/////////////////////////////////////////////////////////////////////////////
2109
2110#[stable(feature = "rust1", since = "1.0.0")]
2111impl<A, E, V: FromIterator<A>> FromIterator<Result<A, E>> for Result<V, E> {
2112    /// Takes each element in the `Iterator`: if it is an `Err`, no further
2113    /// elements are taken, and the `Err` is returned. Should no `Err` occur, a
2114    /// container with the values of each `Result` is returned.
2115    ///
2116    /// Here is an example which increments every integer in a vector,
2117    /// checking for overflow:
2118    ///
2119    /// ```
2120    /// let v = vec![1, 2];
2121    /// let res: Result<Vec<u32>, &'static str> = v.iter().map(|x: &u32|
2122    ///     x.checked_add(1).ok_or("Overflow!")
2123    /// ).collect();
2124    /// assert_eq!(res, Ok(vec![2, 3]));
2125    /// ```
2126    ///
2127    /// Here is another example that tries to subtract one from another list
2128    /// of integers, this time checking for underflow:
2129    ///
2130    /// ```
2131    /// let v = vec![1, 2, 0];
2132    /// let res: Result<Vec<u32>, &'static str> = v.iter().map(|x: &u32|
2133    ///     x.checked_sub(1).ok_or("Underflow!")
2134    /// ).collect();
2135    /// assert_eq!(res, Err("Underflow!"));
2136    /// ```
2137    ///
2138    /// Here is a variation on the previous example, showing that no
2139    /// further elements are taken from `iter` after the first `Err`.
2140    ///
2141    /// ```
2142    /// let v = vec![3, 2, 1, 10];
2143    /// let mut shared = 0;
2144    /// let res: Result<Vec<u32>, &'static str> = v.iter().map(|x: &u32| {
2145    ///     shared += x;
2146    ///     x.checked_sub(2).ok_or("Underflow!")
2147    /// }).collect();
2148    /// assert_eq!(res, Err("Underflow!"));
2149    /// assert_eq!(shared, 6);
2150    /// ```
2151    ///
2152    /// Since the third element caused an underflow, no further elements were taken,
2153    /// so the final value of `shared` is 6 (= `3 + 2 + 1`), not 16.
2154    #[inline]
2155    fn from_iter<I: IntoIterator<Item = Result<A, E>>>(iter: I) -> Result<V, E> {
2156        iter::try_process(iter.into_iter(), |i| i.collect())
2157    }
2158}
2159
2160#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
2161#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2162impl<T, E> const ops::Try for Result<T, E> {
2163    type Output = T;
2164    type Residual = Result<convert::Infallible, E>;
2165
2166    #[inline]
2167    fn from_output(output: Self::Output) -> Self {
2168        Ok(output)
2169    }
2170
2171    #[inline]
2172    fn branch(self) -> ControlFlow<Self::Residual, Self::Output> {
2173        match self {
2174            Ok(v) => ControlFlow::Continue(v),
2175            Err(e) => ControlFlow::Break(Err(e)),
2176        }
2177    }
2178}
2179
2180#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
2181#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2182impl<T, E, F: [const] From<E>> const ops::FromResidual<Result<convert::Infallible, E>>
2183    for Result<T, F>
2184{
2185    #[inline]
2186    #[track_caller]
2187    fn from_residual(residual: Result<convert::Infallible, E>) -> Self {
2188        match residual {
2189            Err(e) => Err(From::from(e)),
2190        }
2191    }
2192}
2193#[diagnostic::do_not_recommend]
2194#[unstable(feature = "try_trait_v2_yeet", issue = "96374")]
2195#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2196impl<T, E, F: [const] From<E>> const ops::FromResidual<ops::Yeet<E>> for Result<T, F> {
2197    #[inline]
2198    fn from_residual(ops::Yeet(e): ops::Yeet<E>) -> Self {
2199        Err(From::from(e))
2200    }
2201}
2202
2203#[unstable(feature = "try_trait_v2_residual", issue = "91285")]
2204#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2205impl<T, E> const ops::Residual<T> for Result<convert::Infallible, E> {
2206    type TryType = Result<T, E>;
2207}
````