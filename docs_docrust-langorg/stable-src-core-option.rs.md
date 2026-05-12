---
title: option.rs - source
url: https://doc.rust-lang.org/stable/src/core/option.rs.html#600
source: crawler
fetched_at: 2026-05-06T21:35:30.426757609-03:00
rendered_js: false
word_count: 11356
summary: This document explains the usage and memory representation of the Option type in Rust, including pattern matching, the question mark operator, and null pointer optimization.
tags:
    - rust
    - option
    - pattern-matching
    - null-pointer-optimization
    - data-types
category: concept
---

## core/ option.rs

````rust
1//! Optional values.
2//!
3//! Type [`Option`] represents an optional value: every [`Option`]
4//! is either [`Some`] and contains a value, or [`None`], and
5//! does not. [`Option`] types are very common in Rust code, as
6//! they have a number of uses:
7//!
8//! * Initial values
9//! * Return values for functions that are not defined
10//!   over their entire input range (partial functions)
11//! * Return value for otherwise reporting simple errors, where [`None`] is
12//!   returned on error
13//! * Optional struct fields
14//! * Struct fields that can be loaned or "taken"
15//! * Optional function arguments
16//! * Nullable pointers
17//! * Swapping things out of difficult situations
18//!
19//! [`Option`]s are commonly paired with pattern matching to query the presence
20//! of a value and take action, always accounting for the [`None`] case.
21//!
22//! ```
23//! fn divide(numerator: f64, denominator: f64) -> Option<f64> {
24//!     if denominator == 0.0 {
25//!         None
26//!     } else {
27//!         Some(numerator / denominator)
28//!     }
29//! }
30//!
31//! // The return value of the function is an option
32//! let result = divide(2.0, 3.0);
33//!
34//! // Pattern match to retrieve the value
35//! match result {
36//!     // The division was valid
37//!     Some(x) => println!("Result: {x}"),
38//!     // The division was invalid
39//!     None    => println!("Cannot divide by 0"),
40//! }
41//! ```
42//!
43//
44// FIXME: Show how `Option` is used in practice, with lots of methods
45//
46//! # Options and pointers ("nullable" pointers)
47//!
48//! Rust's pointer types must always point to a valid location; there are
49//! no "null" references. Instead, Rust has *optional* pointers, like
50//! the optional owned box, <code>[Option]<[Box\<T>]></code>.
51//!
52//! [Box\<T>]: ../../std/boxed/struct.Box.html
53//!
54//! The following example uses [`Option`] to create an optional box of
55//! [`i32`]. Notice that in order to use the inner [`i32`] value, the
56//! `check_optional` function first needs to use pattern matching to
57//! determine whether the box has a value (i.e., it is [`Some(...)`][`Some`]) or
58//! not ([`None`]).
59//!
60//! ```
61//! let optional = None;
62//! check_optional(optional);
63//!
64//! let optional = Some(Box::new(9000));
65//! check_optional(optional);
66//!
67//! fn check_optional(optional: Option<Box<i32>>) {
68//!     match optional {
69//!         Some(p) => println!("has value {p}"),
70//!         None => println!("has no value"),
71//!     }
72//! }
73//! ```
74//!
75//! # The question mark operator, `?`
76//!
77//! Similar to the [`Result`] type, when writing code that calls many functions that return the
78//! [`Option`] type, handling `Some`/`None` can be tedious. The question mark
79//! operator, [`?`], hides some of the boilerplate of propagating values
80//! up the call stack.
81//!
82//! It replaces this:
83//!
84//! ```
85//! # #![allow(dead_code)]
86//! fn add_last_numbers(stack: &mut Vec<i32>) -> Option<i32> {
87//!     let a = stack.pop();
88//!     let b = stack.pop();
89//!
90//!     match (a, b) {
91//!         (Some(x), Some(y)) => Some(x + y),
92//!         _ => None,
93//!     }
94//! }
95//!
96//! ```
97//!
98//! With this:
99//!
100//! ```
101//! # #![allow(dead_code)]
102//! fn add_last_numbers(stack: &mut Vec<i32>) -> Option<i32> {
103//!     Some(stack.pop()? + stack.pop()?)
104//! }
105//! ```
106//!
107//! *It's much nicer!*
108//!
109//! Ending the expression with [`?`] will result in the [`Some`]'s unwrapped value, unless the
110//! result is [`None`], in which case [`None`] is returned early from the enclosing function.
111//!
112//! [`?`] can be used in functions that return [`Option`] because of the
113//! early return of [`None`] that it provides.
114//!
115//! [`?`]: crate::ops::Try
116//! [`Some`]: Some
117//! [`None`]: None
118//!
119//! # Representation
120//!
121//! Rust guarantees to optimize the following types `T` such that [`Option<T>`]
122//! has the same size, alignment, and [function call ABI] as `T`. It is
123//! therefore sound, when `T` is one of these types, to transmute a value `t` of
124//! type `T` to type `Option<T>` (producing the value `Some(t)`) and to
125//! transmute a value `Some(t)` of type `Option<T>` to type `T` (producing the
126//! value `t`).
127//!
128//! In some of these cases, Rust further guarantees the following:
129//! - `transmute::<_, Option<T>>([0u8; size_of::<T>()])` is sound and produces
130//!   `Option::<T>::None`
131//! - `transmute::<_, [u8; size_of::<T>()]>(Option::<T>::None)` is sound and produces
132//!   `[0u8; size_of::<T>()]`
133//!
134//! These cases are identified by the second column:
135//!
136//! | `T`                                                                 | Transmuting between `[0u8; size_of::<T>()]` and `Option::<T>::None` sound? |
137//! |---------------------------------------------------------------------|----------------------------------------------------------------------------|
138//! | [`Box<U>`] (specifically, only `Box<U, Global>`)                    | when `U: Sized`                                                            |
139//! | `&U`                                                                | when `U: Sized`                                                            |
140//! | `&mut U`                                                            | when `U: Sized`                                                            |
141//! | `fn`, `extern "C" fn`[^extern_fn]                                   | always                                                                     |
142//! | [`num::NonZero*`]                                                   | always                                                                     |
143//! | [`ptr::NonNull<U>`]                                                 | when `U: Sized`                                                            |
144//! | `#[repr(transparent)]` struct around one of the types in this list. | when it holds for the inner type                                           |
145//!
146//! [^extern_fn]: this remains true for `unsafe` variants, any argument/return types, and any other ABI: `[unsafe] extern "abi" fn` (_e.g._, `extern "system" fn`)
147//!
148//! Under some conditions the above types `T` are also null pointer optimized when wrapped in a [`Result`][result_repr].
149//!
150//! [`Box<U>`]: ../../std/boxed/struct.Box.html
151//! [`num::NonZero*`]: crate::num
152//! [`ptr::NonNull<U>`]: crate::ptr::NonNull
153//! [function call ABI]: ../primitive.fn.html#abi-compatibility
154//! [result_repr]: crate::result#representation
155//!
156//! This is called the "null pointer optimization" or NPO.
157//!
158//! It is further guaranteed that, for the cases above, one can
159//! [`mem::transmute`] from all valid values of `T` to `Option<T>` and
160//! from `Some::<T>(_)` to `T` (but transmuting `None::<T>` to `T`
161//! is undefined behavior).
162//!
163//! # Method overview
164//!
165//! In addition to working with pattern matching, [`Option`] provides a wide
166//! variety of different methods.
167//!
168//! ## Querying the variant
169//!
170//! The [`is_some`] and [`is_none`] methods return [`true`] if the [`Option`]
171//! is [`Some`] or [`None`], respectively.
172//!
173//! The [`is_some_and`] and [`is_none_or`] methods apply the provided function
174//! to the contents of the [`Option`] to produce a boolean value.
175//! If this is [`None`] then a default result is returned instead without executing the function.
176//!
177//! [`is_none`]: Option::is_none
178//! [`is_some`]: Option::is_some
179//! [`is_some_and`]: Option::is_some_and
180//! [`is_none_or`]: Option::is_none_or
181//!
182//! ## Adapters for working with references
183//!
184//! * [`as_ref`] converts from <code>[&][][Option]\<T></code> to <code>[Option]<[&]T></code>
185//! * [`as_mut`] converts from <code>[&mut] [Option]\<T></code> to <code>[Option]<[&mut] T></code>
186//! * [`as_deref`] converts from <code>[&][][Option]\<T></code> to
187//!   <code>[Option]<[&]T::[Target]></code>
188//! * [`as_deref_mut`] converts from <code>[&mut] [Option]\<T></code> to
189//!   <code>[Option]<[&mut] T::[Target]></code>
190//! * [`as_pin_ref`] converts from <code>[Pin]<[&][][Option]\<T>></code> to
191//!   <code>[Option]<[Pin]<[&]T>></code>
192//! * [`as_pin_mut`] converts from <code>[Pin]<[&mut] [Option]\<T>></code> to
193//!   <code>[Option]<[Pin]<[&mut] T>></code>
194//! * [`as_slice`] returns a one-element slice of the contained value, if any.
195//!   If this is [`None`], an empty slice is returned.
196//! * [`as_mut_slice`] returns a mutable one-element slice of the contained value, if any.
197//!   If this is [`None`], an empty slice is returned.
198//!
199//! [&]: reference "shared reference"
200//! [&mut]: reference "mutable reference"
201//! [Target]: Deref::Target "ops::Deref::Target"
202//! [`as_deref`]: Option::as_deref
203//! [`as_deref_mut`]: Option::as_deref_mut
204//! [`as_mut`]: Option::as_mut
205//! [`as_pin_mut`]: Option::as_pin_mut
206//! [`as_pin_ref`]: Option::as_pin_ref
207//! [`as_ref`]: Option::as_ref
208//! [`as_slice`]: Option::as_slice
209//! [`as_mut_slice`]: Option::as_mut_slice
210//!
211//! ## Extracting the contained value
212//!
213//! These methods extract the contained value in an [`Option<T>`] when it
214//! is the [`Some`] variant. If the [`Option`] is [`None`]:
215//!
216//! * [`expect`] panics with a provided custom message
217//! * [`unwrap`] panics with a generic message
218//! * [`unwrap_or`] returns the provided default value
219//! * [`unwrap_or_default`] returns the default value of the type `T`
220//!   (which must implement the [`Default`] trait)
221//! * [`unwrap_or_else`] returns the result of evaluating the provided
222//!   function
223//! * [`unwrap_unchecked`] produces *[undefined behavior]*
224//!
225//! [`expect`]: Option::expect
226//! [`unwrap`]: Option::unwrap
227//! [`unwrap_or`]: Option::unwrap_or
228//! [`unwrap_or_default`]: Option::unwrap_or_default
229//! [`unwrap_or_else`]: Option::unwrap_or_else
230//! [`unwrap_unchecked`]: Option::unwrap_unchecked
231//! [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
232//!
233//! ## Transforming contained values
234//!
235//! These methods transform [`Option`] to [`Result`]:
236//!
237//! * [`ok_or`] transforms [`Some(v)`] to [`Ok(v)`], and [`None`] to
238//!   [`Err(err)`] using the provided default `err` value
239//! * [`ok_or_else`] transforms [`Some(v)`] to [`Ok(v)`], and [`None`] to
240//!   a value of [`Err`] using the provided function
241//! * [`transpose`] transposes an [`Option`] of a [`Result`] into a
242//!   [`Result`] of an [`Option`]
243//!
244//! [`Err(err)`]: Err
245//! [`Ok(v)`]: Ok
246//! [`Some(v)`]: Some
247//! [`ok_or`]: Option::ok_or
248//! [`ok_or_else`]: Option::ok_or_else
249//! [`transpose`]: Option::transpose
250//!
251//! These methods transform the [`Some`] variant:
252//!
253//! * [`filter`] calls the provided predicate function on the contained
254//!   value `t` if the [`Option`] is [`Some(t)`], and returns [`Some(t)`]
255//!   if the function returns `true`; otherwise, returns [`None`]
256//! * [`flatten`] removes one level of nesting from an [`Option<Option<T>>`]
257//! * [`inspect`] method takes ownership of the [`Option`] and applies
258//!   the provided function to the contained value by reference if [`Some`]
259//! * [`map`] transforms [`Option<T>`] to [`Option<U>`] by applying the
260//!   provided function to the contained value of [`Some`] and leaving
261//!   [`None`] values unchanged
262//!
263//! [`Some(t)`]: Some
264//! [`filter`]: Option::filter
265//! [`flatten`]: Option::flatten
266//! [`inspect`]: Option::inspect
267//! [`map`]: Option::map
268//!
269//! These methods transform [`Option<T>`] to a value of a possibly
270//! different type `U`:
271//!
272//! * [`map_or`] applies the provided function to the contained value of
273//!   [`Some`], or returns the provided default value if the [`Option`] is
274//!   [`None`]
275//! * [`map_or_else`] applies the provided function to the contained value
276//!   of [`Some`], or returns the result of evaluating the provided
277//!   fallback function if the [`Option`] is [`None`]
278//!
279//! [`map_or`]: Option::map_or
280//! [`map_or_else`]: Option::map_or_else
281//!
282//! These methods combine the [`Some`] variants of two [`Option`] values:
283//!
284//! * [`zip`] returns [`Some((s, o))`] if `self` is [`Some(s)`] and the
285//!   provided [`Option`] value is [`Some(o)`]; otherwise, returns [`None`]
286//! * [`zip_with`] calls the provided function `f` and returns
287//!   [`Some(f(s, o))`] if `self` is [`Some(s)`] and the provided
288//!   [`Option`] value is [`Some(o)`]; otherwise, returns [`None`]
289//!
290//! [`Some(f(s, o))`]: Some
291//! [`Some(o)`]: Some
292//! [`Some(s)`]: Some
293//! [`Some((s, o))`]: Some
294//! [`zip`]: Option::zip
295//! [`zip_with`]: Option::zip_with
296//!
297//! ## Boolean operators
298//!
299//! These methods treat the [`Option`] as a boolean value, where [`Some`]
300//! acts like [`true`] and [`None`] acts like [`false`]. There are two
301//! categories of these methods: ones that take an [`Option`] as input, and
302//! ones that take a function as input (to be lazily evaluated).
303//!
304//! The [`and`], [`or`], and [`xor`] methods take another [`Option`] as
305//! input, and produce an [`Option`] as output. Only the [`and`] method can
306//! produce an [`Option<U>`] value having a different inner type `U` than
307//! [`Option<T>`].
308//!
309//! | method  | self      | input     | output    |
310//! |---------|-----------|-----------|-----------|
311//! | [`and`] | `None`    | (ignored) | `None`    |
312//! | [`and`] | `Some(x)` | `None`    | `None`    |
313//! | [`and`] | `Some(x)` | `Some(y)` | `Some(y)` |
314//! | [`or`]  | `None`    | `None`    | `None`    |
315//! | [`or`]  | `None`    | `Some(y)` | `Some(y)` |
316//! | [`or`]  | `Some(x)` | (ignored) | `Some(x)` |
317//! | [`xor`] | `None`    | `None`    | `None`    |
318//! | [`xor`] | `None`    | `Some(y)` | `Some(y)` |
319//! | [`xor`] | `Some(x)` | `None`    | `Some(x)` |
320//! | [`xor`] | `Some(x)` | `Some(y)` | `None`    |
321//!
322//! [`and`]: Option::and
323//! [`or`]: Option::or
324//! [`xor`]: Option::xor
325//!
326//! The [`and_then`] and [`or_else`] methods take a function as input, and
327//! only evaluate the function when they need to produce a new value. Only
328//! the [`and_then`] method can produce an [`Option<U>`] value having a
329//! different inner type `U` than [`Option<T>`].
330//!
331//! | method       | self      | function input | function result | output    |
332//! |--------------|-----------|----------------|-----------------|-----------|
333//! | [`and_then`] | `None`    | (not provided) | (not evaluated) | `None`    |
334//! | [`and_then`] | `Some(x)` | `x`            | `None`          | `None`    |
335//! | [`and_then`] | `Some(x)` | `x`            | `Some(y)`       | `Some(y)` |
336//! | [`or_else`]  | `None`    | (not provided) | `None`          | `None`    |
337//! | [`or_else`]  | `None`    | (not provided) | `Some(y)`       | `Some(y)` |
338//! | [`or_else`]  | `Some(x)` | (not provided) | (not evaluated) | `Some(x)` |
339//!
340//! [`and_then`]: Option::and_then
341//! [`or_else`]: Option::or_else
342//!
343//! This is an example of using methods like [`and_then`] and [`or`] in a
344//! pipeline of method calls. Early stages of the pipeline pass failure
345//! values ([`None`]) through unchanged, and continue processing on
346//! success values ([`Some`]). Toward the end, [`or`] substitutes an error
347//! message if it receives [`None`].
348//!
349//! ```
350//! # use std::collections::BTreeMap;
351//! let mut bt = BTreeMap::new();
352//! bt.insert(20u8, "foo");
353//! bt.insert(42u8, "bar");
354//! let res = [0u8, 1, 11, 200, 22]
355//!     .into_iter()
356//!     .map(|x| {
357//!         // `checked_sub()` returns `None` on error
358//!         x.checked_sub(1)
359//!             // same with `checked_mul()`
360//!             .and_then(|x| x.checked_mul(2))
361//!             // `BTreeMap::get` returns `None` on error
362//!             .and_then(|x| bt.get(&x))
363//!             // Substitute an error message if we have `None` so far
364//!             .or(Some(&"error!"))
365//!             .copied()
366//!             // Won't panic because we unconditionally used `Some` above
367//!             .unwrap()
368//!     })
369//!     .collect::<Vec<_>>();
370//! assert_eq!(res, ["error!", "error!", "foo", "error!", "bar"]);
371//! ```
372//!
373//! ## Comparison operators
374//!
375//! If `T` implements [`PartialOrd`] then [`Option<T>`] will derive its
376//! [`PartialOrd`] implementation.  With this order, [`None`] compares as
377//! less than any [`Some`], and two [`Some`] compare the same way as their
378//! contained values would in `T`.  If `T` also implements
379//! [`Ord`], then so does [`Option<T>`].
380//!
381//! ```
382//! assert!(None < Some(0));
383//! assert!(Some(0) < Some(1));
384//! ```
385//!
386//! ## Iterating over `Option`
387//!
388//! An [`Option`] can be iterated over. This can be helpful if you need an
389//! iterator that is conditionally empty. The iterator will either produce
390//! a single value (when the [`Option`] is [`Some`]), or produce no values
391//! (when the [`Option`] is [`None`]). For example, [`into_iter`] acts like
392//! [`once(v)`] if the [`Option`] is [`Some(v)`], and like [`empty()`] if
393//! the [`Option`] is [`None`].
394//!
395//! [`Some(v)`]: Some
396//! [`empty()`]: crate::iter::empty
397//! [`once(v)`]: crate::iter::once
398//!
399//! Iterators over [`Option<T>`] come in three types:
400//!
401//! * [`into_iter`] consumes the [`Option`] and produces the contained
402//!   value
403//! * [`iter`] produces an immutable reference of type `&T` to the
404//!   contained value
405//! * [`iter_mut`] produces a mutable reference of type `&mut T` to the
406//!   contained value
407//!
408//! [`into_iter`]: Option::into_iter
409//! [`iter`]: Option::iter
410//! [`iter_mut`]: Option::iter_mut
411//!
412//! An iterator over [`Option`] can be useful when chaining iterators, for
413//! example, to conditionally insert items. (It's not always necessary to
414//! explicitly call an iterator constructor: many [`Iterator`] methods that
415//! accept other iterators will also accept iterable types that implement
416//! [`IntoIterator`], which includes [`Option`].)
417//!
418//! ```
419//! let yep = Some(42);
420//! let nope = None;
421//! // chain() already calls into_iter(), so we don't have to do so
422//! let nums: Vec<i32> = (0..4).chain(yep).chain(4..8).collect();
423//! assert_eq!(nums, [0, 1, 2, 3, 42, 4, 5, 6, 7]);
424//! let nums: Vec<i32> = (0..4).chain(nope).chain(4..8).collect();
425//! assert_eq!(nums, [0, 1, 2, 3, 4, 5, 6, 7]);
426//! ```
427//!
428//! One reason to chain iterators in this way is that a function returning
429//! `impl Iterator` must have all possible return values be of the same
430//! concrete type. Chaining an iterated [`Option`] can help with that.
431//!
432//! ```
433//! fn make_iter(do_insert: bool) -> impl Iterator<Item = i32> {
434//!     // Explicit returns to illustrate return types matching
435//!     match do_insert {
436//!         true => return (0..4).chain(Some(42)).chain(4..8),
437//!         false => return (0..4).chain(None).chain(4..8),
438//!     }
439//! }
440//! println!("{:?}", make_iter(true).collect::<Vec<_>>());
441//! println!("{:?}", make_iter(false).collect::<Vec<_>>());
442//! ```
443//!
444//! If we try to do the same thing, but using [`once()`] and [`empty()`],
445//! we can't return `impl Iterator` anymore because the concrete types of
446//! the return values differ.
447//!
448//! [`empty()`]: crate::iter::empty
449//! [`once()`]: crate::iter::once
450//!
451//! ```compile_fail,E0308
452//! # use std::iter::{empty, once};
453//! // This won't compile because all possible returns from the function
454//! // must have the same concrete type.
455//! fn make_iter(do_insert: bool) -> impl Iterator<Item = i32> {
456//!     // Explicit returns to illustrate return types not matching
457//!     match do_insert {
458//!         true => return (0..4).chain(once(42)).chain(4..8),
459//!         false => return (0..4).chain(empty()).chain(4..8),
460//!     }
461//! }
462//! ```
463//!
464//! ## Collecting into `Option`
465//!
466//! [`Option`] implements the [`FromIterator`][impl-FromIterator] trait,
467//! which allows an iterator over [`Option`] values to be collected into an
468//! [`Option`] of a collection of each contained value of the original
469//! [`Option`] values, or [`None`] if any of the elements was [`None`].
470//!
471//! [impl-FromIterator]: Option#impl-FromIterator%3COption%3CA%3E%3E-for-Option%3CV%3E
472//!
473//! ```
474//! let v = [Some(2), Some(4), None, Some(8)];
475//! let res: Option<Vec<_>> = v.into_iter().collect();
476//! assert_eq!(res, None);
477//! let v = [Some(2), Some(4), Some(8)];
478//! let res: Option<Vec<_>> = v.into_iter().collect();
479//! assert_eq!(res, Some(vec![2, 4, 8]));
480//! ```
481//!
482//! [`Option`] also implements the [`Product`][impl-Product] and
483//! [`Sum`][impl-Sum] traits, allowing an iterator over [`Option`] values
484//! to provide the [`product`][Iterator::product] and
485//! [`sum`][Iterator::sum] methods.
486//!
487//! [impl-Product]: Option#impl-Product%3COption%3CU%3E%3E-for-Option%3CT%3E
488//! [impl-Sum]: Option#impl-Sum%3COption%3CU%3E%3E-for-Option%3CT%3E
489//!
490//! ```
491//! let v = [None, Some(1), Some(2), Some(3)];
492//! let res: Option<i32> = v.into_iter().sum();
493//! assert_eq!(res, None);
494//! let v = [Some(1), Some(2), Some(21)];
495//! let res: Option<i32> = v.into_iter().product();
496//! assert_eq!(res, Some(42));
497//! ```
498//!
499//! ## Modifying an [`Option`] in-place
500//!
501//! These methods return a mutable reference to the contained value of an
502//! [`Option<T>`]:
503//!
504//! * [`insert`] inserts a value, dropping any old contents
505//! * [`get_or_insert`] gets the current value, inserting a provided
506//!   default value if it is [`None`]
507//! * [`get_or_insert_default`] gets the current value, inserting the
508//!   default value of type `T` (which must implement [`Default`]) if it is
509//!   [`None`]
510//! * [`get_or_insert_with`] gets the current value, inserting a default
511//!   computed by the provided function if it is [`None`]
512//!
513//! [`get_or_insert`]: Option::get_or_insert
514//! [`get_or_insert_default`]: Option::get_or_insert_default
515//! [`get_or_insert_with`]: Option::get_or_insert_with
516//! [`insert`]: Option::insert
517//!
518//! These methods transfer ownership of the contained value of an
519//! [`Option`]:
520//!
521//! * [`take`] takes ownership of the contained value of an [`Option`], if
522//!   any, replacing the [`Option`] with [`None`]
523//! * [`replace`] takes ownership of the contained value of an [`Option`],
524//!   if any, replacing the [`Option`] with a [`Some`] containing the
525//!   provided value
526//!
527//! [`replace`]: Option::replace
528//! [`take`]: Option::take
529//!
530//! # Examples
531//!
532//! Basic pattern matching on [`Option`]:
533//!
534//! ```
535//! let msg = Some("howdy");
536//!
537//! // Take a reference to the contained string
538//! if let Some(m) = &msg {
539//!     println!("{}", *m);
540//! }
541//!
542//! // Remove the contained string, destroying the Option
543//! let unwrapped_msg = msg.unwrap_or("default message");
544//! ```
545//!
546//! Initialize a result to [`None`] before a loop:
547//!
548//! ```
549//! enum Kingdom { Plant(u32, &'static str), Animal(u32, &'static str) }
550//!
551//! // A list of data to search through.
552//! let all_the_big_things = [
553//!     Kingdom::Plant(250, "redwood"),
554//!     Kingdom::Plant(230, "noble fir"),
555//!     Kingdom::Plant(229, "sugar pine"),
556//!     Kingdom::Animal(25, "blue whale"),
557//!     Kingdom::Animal(19, "fin whale"),
558//!     Kingdom::Animal(15, "north pacific right whale"),
559//! ];
560//!
561//! // We're going to search for the name of the biggest animal,
562//! // but to start with we've just got `None`.
563//! let mut name_of_biggest_animal = None;
564//! let mut size_of_biggest_animal = 0;
565//! for big_thing in &all_the_big_things {
566//!     match *big_thing {
567//!         Kingdom::Animal(size, name) if size > size_of_biggest_animal => {
568//!             // Now we've found the name of some big animal
569//!             size_of_biggest_animal = size;
570//!             name_of_biggest_animal = Some(name);
571//!         }
572//!         Kingdom::Animal(..) | Kingdom::Plant(..) => ()
573//!     }
574//! }
575//!
576//! match name_of_biggest_animal {
577//!     Some(name) => println!("the biggest animal is {name}"),
578//!     None => println!("there are no animals :("),
579//! }
580//! ```
581
582#![stable(feature = "rust1", since = "1.0.0")]
583
584use crate::clone::TrivialClone;
585use crate::iter::{self, FusedIterator, TrustedLen};
586use crate::marker::Destruct;
587use crate::ops::{self, ControlFlow, Deref, DerefMut, Residual, Try};
588use crate::panicking::{panic, panic_display};
589use crate::pin::Pin;
590use crate::{cmp, convert, hint, mem, slice};
591
592/// The `Option` type. See [the module level documentation](self) for more.
593#[doc(search_unbox)]
594#[derive(Copy, Debug, Hash)]
595#[derive_const(Eq)]
596#[rustc_diagnostic_item = "Option"]
597#[lang = "Option"]
598#[stable(feature = "rust1", since = "1.0.0")]
599#[allow(clippy::derived_hash_with_manual_eq)] // PartialEq is manually implemented equivalently
600pub enum Option<T> {
601    /// No value.
602    #[lang = "None"]
603    #[stable(feature = "rust1", since = "1.0.0")]
604    None,
605    /// Some value of type `T`.
606    #[lang = "Some"]
607    #[stable(feature = "rust1", since = "1.0.0")]
608    Some(#[stable(feature = "rust1", since = "1.0.0")] T),
609}
610
611/////////////////////////////////////////////////////////////////////////////
612// Type implementation
613/////////////////////////////////////////////////////////////////////////////
614
615impl<T> Option<T> {
616    /////////////////////////////////////////////////////////////////////////
617    // Querying the contained values
618    /////////////////////////////////////////////////////////////////////////
619
620    /// Returns `true` if the option is a [`Some`] value.
621    ///
622    /// # Examples
623    ///
624    /// ```
625    /// let x: Option<u32> = Some(2);
626    /// assert_eq!(x.is_some(), true);
627    ///
628    /// let x: Option<u32> = None;
629    /// assert_eq!(x.is_some(), false);
630    /// ```
631    #[must_use = "if you intended to assert that this has a value, consider `.unwrap()` instead"]
632    #[inline]
633    #[stable(feature = "rust1", since = "1.0.0")]
634    #[rustc_const_stable(feature = "const_option_basics", since = "1.48.0")]
635    pub const fn is_some(&self) -> bool {
636        matches!(*self, Some(_))
637    }
638
639    /// Returns `true` if the option is a [`Some`] and the value inside of it matches a predicate.
640    ///
641    /// # Examples
642    ///
643    /// ```
644    /// let x: Option<u32> = Some(2);
645    /// assert_eq!(x.is_some_and(|x| x > 1), true);
646    ///
647    /// let x: Option<u32> = Some(0);
648    /// assert_eq!(x.is_some_and(|x| x > 1), false);
649    ///
650    /// let x: Option<u32> = None;
651    /// assert_eq!(x.is_some_and(|x| x > 1), false);
652    ///
653    /// let x: Option<String> = Some("ownership".to_string());
654    /// assert_eq!(x.as_ref().is_some_and(|x| x.len() > 1), true);
655    /// println!("still alive {:?}", x);
656    /// ```
657    #[must_use]
658    #[inline]
659    #[stable(feature = "is_some_and", since = "1.70.0")]
660    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
661    pub const fn is_some_and(self, f: impl [const] FnOnce(T) -> bool + [const] Destruct) -> bool {
662        match self {
663            None => false,
664            Some(x) => f(x),
665        }
666    }
667
668    /// Returns `true` if the option is a [`None`] value.
669    ///
670    /// # Examples
671    ///
672    /// ```
673    /// let x: Option<u32> = Some(2);
674    /// assert_eq!(x.is_none(), false);
675    ///
676    /// let x: Option<u32> = None;
677    /// assert_eq!(x.is_none(), true);
678    /// ```
679    #[must_use = "if you intended to assert that this doesn't have a value, consider \
680                  wrapping this in an `assert!()` instead"]
681    #[inline]
682    #[stable(feature = "rust1", since = "1.0.0")]
683    #[rustc_const_stable(feature = "const_option_basics", since = "1.48.0")]
684    pub const fn is_none(&self) -> bool {
685        !self.is_some()
686    }
687
688    /// Returns `true` if the option is a [`None`] or the value inside of it matches a predicate.
689    ///
690    /// # Examples
691    ///
692    /// ```
693    /// let x: Option<u32> = Some(2);
694    /// assert_eq!(x.is_none_or(|x| x > 1), true);
695    ///
696    /// let x: Option<u32> = Some(0);
697    /// assert_eq!(x.is_none_or(|x| x > 1), false);
698    ///
699    /// let x: Option<u32> = None;
700    /// assert_eq!(x.is_none_or(|x| x > 1), true);
701    ///
702    /// let x: Option<String> = Some("ownership".to_string());
703    /// assert_eq!(x.as_ref().is_none_or(|x| x.len() > 1), true);
704    /// println!("still alive {:?}", x);
705    /// ```
706    #[must_use]
707    #[inline]
708    #[stable(feature = "is_none_or", since = "1.82.0")]
709    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
710    pub const fn is_none_or(self, f: impl [const] FnOnce(T) -> bool + [const] Destruct) -> bool {
711        match self {
712            None => true,
713            Some(x) => f(x),
714        }
715    }
716
717    /////////////////////////////////////////////////////////////////////////
718    // Adapter for working with references
719    /////////////////////////////////////////////////////////////////////////
720
721    /// Converts from `&Option<T>` to `Option<&T>`.
722    ///
723    /// # Examples
724    ///
725    /// Calculates the length of an <code>Option<[String]></code> as an <code>Option<[usize]></code>
726    /// without moving the [`String`]. The [`map`] method takes the `self` argument by value,
727    /// consuming the original, so this technique uses `as_ref` to first take an `Option` to a
728    /// reference to the value inside the original.
729    ///
730    /// [`map`]: Option::map
731    /// [String]: ../../std/string/struct.String.html "String"
732    /// [`String`]: ../../std/string/struct.String.html "String"
733    ///
734    /// ```
735    /// let text: Option<String> = Some("Hello, world!".to_string());
736    /// // First, cast `Option<String>` to `Option<&String>` with `as_ref`,
737    /// // then consume *that* with `map`, leaving `text` on the stack.
738    /// let text_length: Option<usize> = text.as_ref().map(|s| s.len());
739    /// println!("still can print text: {text:?}");
740    /// ```
741    #[inline]
742    #[rustc_const_stable(feature = "const_option_basics", since = "1.48.0")]
743    #[stable(feature = "rust1", since = "1.0.0")]
744    pub const fn as_ref(&self) -> Option<&T> {
745        match *self {
746            Some(ref x) => Some(x),
747            None => None,
748        }
749    }
750
751    /// Converts from `&mut Option<T>` to `Option<&mut T>`.
752    ///
753    /// # Examples
754    ///
755    /// ```
756    /// let mut x = Some(2);
757    /// match x.as_mut() {
758    ///     Some(v) => *v = 42,
759    ///     None => {},
760    /// }
761    /// assert_eq!(x, Some(42));
762    /// ```
763    #[inline]
764    #[stable(feature = "rust1", since = "1.0.0")]
765    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
766    pub const fn as_mut(&mut self) -> Option<&mut T> {
767        match *self {
768            Some(ref mut x) => Some(x),
769            None => None,
770        }
771    }
772
773    /// Converts from <code>[Pin]<[&]Option\<T>></code> to <code>Option<[Pin]<[&]T>></code>.
774    ///
775    /// [&]: reference "shared reference"
776    #[inline]
777    #[must_use]
778    #[stable(feature = "pin", since = "1.33.0")]
779    #[rustc_const_stable(feature = "const_option_ext", since = "1.84.0")]
780    pub const fn as_pin_ref(self: Pin<&Self>) -> Option<Pin<&T>> {
781        // FIXME(const-hack): use `map` once that is possible
782        match Pin::get_ref(self).as_ref() {
783            // SAFETY: `x` is guaranteed to be pinned because it comes from `self`
784            // which is pinned.
785            Some(x) => unsafe { Some(Pin::new_unchecked(x)) },
786            None => None,
787        }
788    }
789
790    /// Converts from <code>[Pin]<[&mut] Option\<T>></code> to <code>Option<[Pin]<[&mut] T>></code>.
791    ///
792    /// [&mut]: reference "mutable reference"
793    #[inline]
794    #[must_use]
795    #[stable(feature = "pin", since = "1.33.0")]
796    #[rustc_const_stable(feature = "const_option_ext", since = "1.84.0")]
797    pub const fn as_pin_mut(self: Pin<&mut Self>) -> Option<Pin<&mut T>> {
798        // SAFETY: `get_unchecked_mut` is never used to move the `Option` inside `self`.
799        // `x` is guaranteed to be pinned because it comes from `self` which is pinned.
800        unsafe {
801            // FIXME(const-hack): use `map` once that is possible
802            match Pin::get_unchecked_mut(self).as_mut() {
803                Some(x) => Some(Pin::new_unchecked(x)),
804                None => None,
805            }
806        }
807    }
808
809    #[inline]
810    const fn len(&self) -> usize {
811        // Using the intrinsic avoids emitting a branch to get the 0 or 1.
812        let discriminant: isize = crate::intrinsics::discriminant_value(self);
813        discriminant as usize
814    }
815
816    /// Returns a slice of the contained value, if any. If this is `None`, an
817    /// empty slice is returned. This can be useful to have a single type of
818    /// iterator over an `Option` or slice.
819    ///
820    /// Note: Should you have an `Option<&T>` and wish to get a slice of `T`,
821    /// you can unpack it via `opt.map_or(&[], std::slice::from_ref)`.
822    ///
823    /// # Examples
824    ///
825    /// ```rust
826    /// assert_eq!(
827    ///     [Some(1234).as_slice(), None.as_slice()],
828    ///     [&[1234][..], &[][..]],
829    /// );
830    /// ```
831    ///
832    /// The inverse of this function is (discounting
833    /// borrowing) [`[_]::first`](slice::first):
834    ///
835    /// ```rust
836    /// for i in [Some(1234_u16), None] {
837    ///     assert_eq!(i.as_ref(), i.as_slice().first());
838    /// }
839    /// ```
840    #[inline]
841    #[must_use]
842    #[stable(feature = "option_as_slice", since = "1.75.0")]
843    #[rustc_const_stable(feature = "const_option_ext", since = "1.84.0")]
844    pub const fn as_slice(&self) -> &[T] {
845        // SAFETY: When the `Option` is `Some`, we're using the actual pointer
846        // to the payload, with a length of 1, so this is equivalent to
847        // `slice::from_ref`, and thus is safe.
848        // When the `Option` is `None`, the length used is 0, so to be safe it
849        // just needs to be aligned, which it is because `&self` is aligned and
850        // the offset used is a multiple of alignment.
851        //
852        // Here we assume that `offset_of!` always returns an offset to an
853        // in-bounds and correctly aligned position for a `T` (even if in the
854        // `None` case it's just padding).
855        unsafe {
856            slice::from_raw_parts(
857                (self as *const Self).byte_add(core::mem::offset_of!(Self, Some.0)).cast(),
858                self.len(),
859            )
860        }
861    }
862
863    /// Returns a mutable slice of the contained value, if any. If this is
864    /// `None`, an empty slice is returned. This can be useful to have a
865    /// single type of iterator over an `Option` or slice.
866    ///
867    /// Note: Should you have an `Option<&mut T>` instead of a
868    /// `&mut Option<T>`, which this method takes, you can obtain a mutable
869    /// slice via `opt.map_or(&mut [], std::slice::from_mut)`.
870    ///
871    /// # Examples
872    ///
873    /// ```rust
874    /// assert_eq!(
875    ///     [Some(1234).as_mut_slice(), None.as_mut_slice()],
876    ///     [&mut [1234][..], &mut [][..]],
877    /// );
878    /// ```
879    ///
880    /// The result is a mutable slice of zero or one items that points into
881    /// our original `Option`:
882    ///
883    /// ```rust
884    /// let mut x = Some(1234);
885    /// x.as_mut_slice()[0] += 1;
886    /// assert_eq!(x, Some(1235));
887    /// ```
888    ///
889    /// The inverse of this method (discounting borrowing)
890    /// is [`[_]::first_mut`](slice::first_mut):
891    ///
892    /// ```rust
893    /// assert_eq!(Some(123).as_mut_slice().first_mut(), Some(&mut 123))
894    /// ```
895    #[inline]
896    #[must_use]
897    #[stable(feature = "option_as_slice", since = "1.75.0")]
898    #[rustc_const_stable(feature = "const_option_ext", since = "1.84.0")]
899    pub const fn as_mut_slice(&mut self) -> &mut [T] {
900        // SAFETY: When the `Option` is `Some`, we're using the actual pointer
901        // to the payload, with a length of 1, so this is equivalent to
902        // `slice::from_mut`, and thus is safe.
903        // When the `Option` is `None`, the length used is 0, so to be safe it
904        // just needs to be aligned, which it is because `&self` is aligned and
905        // the offset used is a multiple of alignment.
906        //
907        // In the new version, the intrinsic creates a `*const T` from a
908        // mutable reference  so it is safe to cast back to a mutable pointer
909        // here. As with `as_slice`, the intrinsic always returns a pointer to
910        // an in-bounds and correctly aligned position for a `T` (even if in
911        // the `None` case it's just padding).
912        unsafe {
913            slice::from_raw_parts_mut(
914                (self as *mut Self).byte_add(core::mem::offset_of!(Self, Some.0)).cast(),
915                self.len(),
916            )
917        }
918    }
919
920    /////////////////////////////////////////////////////////////////////////
921    // Getting to contained values
922    /////////////////////////////////////////////////////////////////////////
923
924    /// Returns the contained [`Some`] value, consuming the `self` value.
925    ///
926    /// # Panics
927    ///
928    /// Panics if the value is a [`None`] with a custom panic message provided by
929    /// `msg`.
930    ///
931    /// # Examples
932    ///
933    /// ```
934    /// let x = Some("value");
935    /// assert_eq!(x.expect("fruits are healthy"), "value");
936    /// ```
937    ///
938    /// ```should_panic
939    /// let x: Option<&str> = None;
940    /// x.expect("fruits are healthy"); // panics with `fruits are healthy`
941    /// ```
942    ///
943    /// # Recommended Message Style
944    ///
945    /// We recommend that `expect` messages are used to describe the reason you
946    /// _expect_ the `Option` should be `Some`.
947    ///
948    /// ```should_panic
949    /// # let slice: &[u8] = &[];
950    /// let item = slice.get(0)
951    ///     .expect("slice should not be empty");
952    /// ```
953    ///
954    /// **Hint**: If you're having trouble remembering how to phrase expect
955    /// error messages remember to focus on the word "should" as in "env
956    /// variable should be set by blah" or "the given binary should be available
957    /// and executable by the current user".
958    ///
959    /// For more detail on expect message styles and the reasoning behind our
960    /// recommendation please refer to the section on ["Common Message
961    /// Styles"](../../std/error/index.html#common-message-styles) in the [`std::error`](../../std/error/index.html) module docs.
962    #[inline]
963    #[track_caller]
964    #[stable(feature = "rust1", since = "1.0.0")]
965    #[rustc_diagnostic_item = "option_expect"]
966    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
967    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
968    pub const fn expect(self, msg: &str) -> T {
969        match self {
970            Some(val) => val,
971            None => expect_failed(msg),
972        }
973    }
974
975    /// Returns the contained [`Some`] value, consuming the `self` value.
976    ///
977    /// Because this function may panic, its use is generally discouraged.
978    /// Panics are meant for unrecoverable errors, and
979    /// [may abort the entire program][panic-abort].
980    ///
981    /// Instead, prefer to use pattern matching and handle the [`None`]
982    /// case explicitly, or call [`unwrap_or`], [`unwrap_or_else`], or
983    /// [`unwrap_or_default`]. In functions returning `Option`, you can use
984    /// [the `?` (try) operator][try-option].
985    ///
986    /// [panic-abort]: https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic.html
987    /// [try-option]: https://doc.rust-lang.org/book/ch09-02-recoverable-errors-with-result.html#where-the--operator-can-be-used
988    /// [`unwrap_or`]: Option::unwrap_or
989    /// [`unwrap_or_else`]: Option::unwrap_or_else
990    /// [`unwrap_or_default`]: Option::unwrap_or_default
991    ///
992    /// # Panics
993    ///
994    /// Panics if the self value equals [`None`].
995    ///
996    /// # Examples
997    ///
998    /// ```
999    /// let x = Some("air");
1000    /// assert_eq!(x.unwrap(), "air");
1001    /// ```
1002    ///
1003    /// ```should_panic
1004    /// let x: Option<&str> = None;
1005    /// assert_eq!(x.unwrap(), "air"); // fails
1006    /// ```
1007    #[inline(always)]
1008    #[track_caller]
1009    #[stable(feature = "rust1", since = "1.0.0")]
1010    #[rustc_diagnostic_item = "option_unwrap"]
1011    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1012    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
1013    pub const fn unwrap(self) -> T {
1014        match self {
1015            Some(val) => val,
1016            None => unwrap_failed(),
1017        }
1018    }
1019
1020    /// Returns the contained [`Some`] value or a provided default.
1021    ///
1022    /// Arguments passed to `unwrap_or` are eagerly evaluated; if you are passing
1023    /// the result of a function call, it is recommended to use [`unwrap_or_else`],
1024    /// which is lazily evaluated.
1025    ///
1026    /// [`unwrap_or_else`]: Option::unwrap_or_else
1027    ///
1028    /// # Examples
1029    ///
1030    /// ```
1031    /// assert_eq!(Some("car").unwrap_or("bike"), "car");
1032    /// assert_eq!(None.unwrap_or("bike"), "bike");
1033    /// ```
1034    #[inline]
1035    #[stable(feature = "rust1", since = "1.0.0")]
1036    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1037    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1038    pub const fn unwrap_or(self, default: T) -> T
1039    where
1040        T: [const] Destruct,
1041    {
1042        match self {
1043            Some(x) => x,
1044            None => default,
1045        }
1046    }
1047
1048    /// Returns the contained [`Some`] value or computes it from a closure.
1049    ///
1050    /// # Examples
1051    ///
1052    /// ```
1053    /// let k = 10;
1054    /// assert_eq!(Some(4).unwrap_or_else(|| 2 * k), 4);
1055    /// assert_eq!(None.unwrap_or_else(|| 2 * k), 20);
1056    /// ```
1057    #[inline]
1058    #[track_caller]
1059    #[stable(feature = "rust1", since = "1.0.0")]
1060    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1061    pub const fn unwrap_or_else<F>(self, f: F) -> T
1062    where
1063        F: [const] FnOnce() -> T + [const] Destruct,
1064    {
1065        match self {
1066            Some(x) => x,
1067            None => f(),
1068        }
1069    }
1070
1071    /// Returns the contained [`Some`] value or a default.
1072    ///
1073    /// Consumes the `self` argument then, if [`Some`], returns the contained
1074    /// value, otherwise if [`None`], returns the [default value] for that
1075    /// type.
1076    ///
1077    /// # Examples
1078    ///
1079    /// ```
1080    /// let x: Option<u32> = None;
1081    /// let y: Option<u32> = Some(12);
1082    ///
1083    /// assert_eq!(x.unwrap_or_default(), 0);
1084    /// assert_eq!(y.unwrap_or_default(), 12);
1085    /// ```
1086    ///
1087    /// [default value]: Default::default
1088    /// [`parse`]: str::parse
1089    /// [`FromStr`]: crate::str::FromStr
1090    #[inline]
1091    #[stable(feature = "rust1", since = "1.0.0")]
1092    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1093    pub const fn unwrap_or_default(self) -> T
1094    where
1095        T: [const] Default,
1096    {
1097        match self {
1098            Some(x) => x,
1099            None => T::default(),
1100        }
1101    }
1102
1103    /// Returns the contained [`Some`] value, consuming the `self` value,
1104    /// without checking that the value is not [`None`].
1105    ///
1106    /// # Safety
1107    ///
1108    /// Calling this method on [`None`] is *[undefined behavior]*.
1109    ///
1110    /// [undefined behavior]: https://doc.rust-lang.org/reference/behavior-considered-undefined.html
1111    ///
1112    /// # Examples
1113    ///
1114    /// ```
1115    /// let x = Some("air");
1116    /// assert_eq!(unsafe { x.unwrap_unchecked() }, "air");
1117    /// ```
1118    ///
1119    /// ```no_run
1120    /// let x: Option<&str> = None;
1121    /// assert_eq!(unsafe { x.unwrap_unchecked() }, "air"); // Undefined behavior!
1122    /// ```
1123    #[inline]
1124    #[track_caller]
1125    #[stable(feature = "option_result_unwrap_unchecked", since = "1.58.0")]
1126    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1127    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
1128    pub const unsafe fn unwrap_unchecked(self) -> T {
1129        match self {
1130            Some(val) => val,
1131            // SAFETY: the safety contract must be upheld by the caller.
1132            None => unsafe { hint::unreachable_unchecked() },
1133        }
1134    }
1135
1136    /////////////////////////////////////////////////////////////////////////
1137    // Transforming contained values
1138    /////////////////////////////////////////////////////////////////////////
1139
1140    /// Maps an `Option<T>` to `Option<U>` by applying a function to a contained value (if `Some`) or returns `None` (if `None`).
1141    ///
1142    /// # Examples
1143    ///
1144    /// Calculates the length of an <code>Option<[String]></code> as an
1145    /// <code>Option<[usize]></code>, consuming the original:
1146    ///
1147    /// [String]: ../../std/string/struct.String.html "String"
1148    /// ```
1149    /// let maybe_some_string = Some(String::from("Hello, World!"));
1150    /// // `Option::map` takes self *by value*, consuming `maybe_some_string`
1151    /// let maybe_some_len = maybe_some_string.map(|s| s.len());
1152    /// assert_eq!(maybe_some_len, Some(13));
1153    ///
1154    /// let x: Option<&str> = None;
1155    /// assert_eq!(x.map(|s| s.len()), None);
1156    /// ```
1157    #[inline]
1158    #[stable(feature = "rust1", since = "1.0.0")]
1159    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1160    pub const fn map<U, F>(self, f: F) -> Option<U>
1161    where
1162        F: [const] FnOnce(T) -> U + [const] Destruct,
1163    {
1164        match self {
1165            Some(x) => Some(f(x)),
1166            None => None,
1167        }
1168    }
1169
1170    /// Calls a function with a reference to the contained value if [`Some`].
1171    ///
1172    /// Returns the original option.
1173    ///
1174    /// # Examples
1175    ///
1176    /// ```
1177    /// let list = vec![1, 2, 3];
1178    ///
1179    /// // prints "got: 2"
1180    /// let x = list
1181    ///     .get(1)
1182    ///     .inspect(|x| println!("got: {x}"))
1183    ///     .expect("list should be long enough");
1184    ///
1185    /// // prints nothing
1186    /// list.get(5).inspect(|x| println!("got: {x}"));
1187    /// ```
1188    #[inline]
1189    #[stable(feature = "result_option_inspect", since = "1.76.0")]
1190    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1191    pub const fn inspect<F>(self, f: F) -> Self
1192    where
1193        F: [const] FnOnce(&T) + [const] Destruct,
1194    {
1195        if let Some(ref x) = self {
1196            f(x);
1197        }
1198
1199        self
1200    }
1201
1202    /// Returns the provided default result (if none),
1203    /// or applies a function to the contained value (if any).
1204    ///
1205    /// Arguments passed to `map_or` are eagerly evaluated; if you are passing
1206    /// the result of a function call, it is recommended to use [`map_or_else`],
1207    /// which is lazily evaluated.
1208    ///
1209    /// [`map_or_else`]: Option::map_or_else
1210    ///
1211    /// # Examples
1212    ///
1213    /// ```
1214    /// let x = Some("foo");
1215    /// assert_eq!(x.map_or(42, |v| v.len()), 3);
1216    ///
1217    /// let x: Option<&str> = None;
1218    /// assert_eq!(x.map_or(42, |v| v.len()), 42);
1219    /// ```
1220    #[inline]
1221    #[stable(feature = "rust1", since = "1.0.0")]
1222    #[must_use = "if you don't need the returned value, use `if let` instead"]
1223    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1224    pub const fn map_or<U, F>(self, default: U, f: F) -> U
1225    where
1226        F: [const] FnOnce(T) -> U + [const] Destruct,
1227        U: [const] Destruct,
1228    {
1229        match self {
1230            Some(t) => f(t),
1231            None => default,
1232        }
1233    }
1234
1235    /// Computes a default function result (if none), or
1236    /// applies a different function to the contained value (if any).
1237    ///
1238    /// # Basic examples
1239    ///
1240    /// ```
1241    /// let k = 21;
1242    ///
1243    /// let x = Some("foo");
1244    /// assert_eq!(x.map_or_else(|| 2 * k, |v| v.len()), 3);
1245    ///
1246    /// let x: Option<&str> = None;
1247    /// assert_eq!(x.map_or_else(|| 2 * k, |v| v.len()), 42);
1248    /// ```
1249    ///
1250    /// # Handling a Result-based fallback
1251    ///
1252    /// A somewhat common occurrence when dealing with optional values
1253    /// in combination with [`Result<T, E>`] is the case where one wants to invoke
1254    /// a fallible fallback if the option is not present.  This example
1255    /// parses a command line argument (if present), or the contents of a file to
1256    /// an integer.  However, unlike accessing the command line argument, reading
1257    /// the file is fallible, so it must be wrapped with `Ok`.
1258    ///
1259    /// ```no_run
1260    /// # fn main() -> Result<(), Box<dyn std::error::Error>> {
1261    /// let v: u64 = std::env::args()
1262    ///    .nth(1)
1263    ///    .map_or_else(|| std::fs::read_to_string("/etc/someconfig.conf"), Ok)?
1264    ///    .parse()?;
1265    /// #   Ok(())
1266    /// # }
1267    /// ```
1268    #[inline]
1269    #[stable(feature = "rust1", since = "1.0.0")]
1270    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1271    pub const fn map_or_else<U, D, F>(self, default: D, f: F) -> U
1272    where
1273        D: [const] FnOnce() -> U + [const] Destruct,
1274        F: [const] FnOnce(T) -> U + [const] Destruct,
1275    {
1276        match self {
1277            Some(t) => f(t),
1278            None => default(),
1279        }
1280    }
1281
1282    /// Maps an `Option<T>` to a `U` by applying function `f` to the contained
1283    /// value if the option is [`Some`], otherwise if [`None`], returns the
1284    /// [default value] for the type `U`.
1285    ///
1286    /// # Examples
1287    ///
1288    /// ```
1289    /// #![feature(result_option_map_or_default)]
1290    ///
1291    /// let x: Option<&str> = Some("hi");
1292    /// let y: Option<&str> = None;
1293    ///
1294    /// assert_eq!(x.map_or_default(|x| x.len()), 2);
1295    /// assert_eq!(y.map_or_default(|y| y.len()), 0);
1296    /// ```
1297    ///
1298    /// [default value]: Default::default
1299    #[inline]
1300    #[unstable(feature = "result_option_map_or_default", issue = "138099")]
1301    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1302    pub const fn map_or_default<U, F>(self, f: F) -> U
1303    where
1304        U: [const] Default,
1305        F: [const] FnOnce(T) -> U + [const] Destruct,
1306    {
1307        match self {
1308            Some(t) => f(t),
1309            None => U::default(),
1310        }
1311    }
1312
1313    /// Transforms the `Option<T>` into a [`Result<T, E>`], mapping [`Some(v)`] to
1314    /// [`Ok(v)`] and [`None`] to [`Err(err)`].
1315    ///
1316    /// Arguments passed to `ok_or` are eagerly evaluated; if you are passing the
1317    /// result of a function call, it is recommended to use [`ok_or_else`], which is
1318    /// lazily evaluated.
1319    ///
1320    /// [`Ok(v)`]: Ok
1321    /// [`Err(err)`]: Err
1322    /// [`Some(v)`]: Some
1323    /// [`ok_or_else`]: Option::ok_or_else
1324    ///
1325    /// # Examples
1326    ///
1327    /// ```
1328    /// let x = Some("foo");
1329    /// assert_eq!(x.ok_or(0), Ok("foo"));
1330    ///
1331    /// let x: Option<&str> = None;
1332    /// assert_eq!(x.ok_or(0), Err(0));
1333    /// ```
1334    #[inline]
1335    #[stable(feature = "rust1", since = "1.0.0")]
1336    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1337    pub const fn ok_or<E: [const] Destruct>(self, err: E) -> Result<T, E> {
1338        match self {
1339            Some(v) => Ok(v),
1340            None => Err(err),
1341        }
1342    }
1343
1344    /// Transforms the `Option<T>` into a [`Result<T, E>`], mapping [`Some(v)`] to
1345    /// [`Ok(v)`] and [`None`] to [`Err(err())`].
1346    ///
1347    /// [`Ok(v)`]: Ok
1348    /// [`Err(err())`]: Err
1349    /// [`Some(v)`]: Some
1350    ///
1351    /// # Examples
1352    ///
1353    /// ```
1354    /// let x = Some("foo");
1355    /// assert_eq!(x.ok_or_else(|| 0), Ok("foo"));
1356    ///
1357    /// let x: Option<&str> = None;
1358    /// assert_eq!(x.ok_or_else(|| 0), Err(0));
1359    /// ```
1360    #[inline]
1361    #[stable(feature = "rust1", since = "1.0.0")]
1362    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1363    pub const fn ok_or_else<E, F>(self, err: F) -> Result<T, E>
1364    where
1365        F: [const] FnOnce() -> E + [const] Destruct,
1366    {
1367        match self {
1368            Some(v) => Ok(v),
1369            None => Err(err()),
1370        }
1371    }
1372
1373    /// Converts from `Option<T>` (or `&Option<T>`) to `Option<&T::Target>`.
1374    ///
1375    /// Leaves the original Option in-place, creating a new one with a reference
1376    /// to the original one, additionally coercing the contents via [`Deref`].
1377    ///
1378    /// # Examples
1379    ///
1380    /// ```
1381    /// let x: Option<String> = Some("hey".to_owned());
1382    /// assert_eq!(x.as_deref(), Some("hey"));
1383    ///
1384    /// let x: Option<String> = None;
1385    /// assert_eq!(x.as_deref(), None);
1386    /// ```
1387    #[inline]
1388    #[stable(feature = "option_deref", since = "1.40.0")]
1389    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1390    pub const fn as_deref(&self) -> Option<&T::Target>
1391    where
1392        T: [const] Deref,
1393    {
1394        self.as_ref().map(Deref::deref)
1395    }
1396
1397    /// Converts from `Option<T>` (or `&mut Option<T>`) to `Option<&mut T::Target>`.
1398    ///
1399    /// Leaves the original `Option` in-place, creating a new one containing a mutable reference to
1400    /// the inner type's [`Deref::Target`] type.
1401    ///
1402    /// # Examples
1403    ///
1404    /// ```
1405    /// let mut x: Option<String> = Some("hey".to_owned());
1406    /// assert_eq!(x.as_deref_mut().map(|x| {
1407    ///     x.make_ascii_uppercase();
1408    ///     x
1409    /// }), Some("HEY".to_owned().as_mut_str()));
1410    /// ```
1411    #[inline]
1412    #[stable(feature = "option_deref", since = "1.40.0")]
1413    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1414    pub const fn as_deref_mut(&mut self) -> Option<&mut T::Target>
1415    where
1416        T: [const] DerefMut,
1417    {
1418        self.as_mut().map(DerefMut::deref_mut)
1419    }
1420
1421    /////////////////////////////////////////////////////////////////////////
1422    // Iterator constructors
1423    /////////////////////////////////////////////////////////////////////////
1424
1425    /// Returns an iterator over the possibly contained value.
1426    ///
1427    /// # Examples
1428    ///
1429    /// ```
1430    /// let x = Some(4);
1431    /// assert_eq!(x.iter().next(), Some(&4));
1432    ///
1433    /// let x: Option<u32> = None;
1434    /// assert_eq!(x.iter().next(), None);
1435    /// ```
1436    #[inline]
1437    #[stable(feature = "rust1", since = "1.0.0")]
1438    pub fn iter(&self) -> Iter<'_, T> {
1439        Iter { inner: Item { opt: self.as_ref() } }
1440    }
1441
1442    /// Returns a mutable iterator over the possibly contained value.
1443    ///
1444    /// # Examples
1445    ///
1446    /// ```
1447    /// let mut x = Some(4);
1448    /// match x.iter_mut().next() {
1449    ///     Some(v) => *v = 42,
1450    ///     None => {},
1451    /// }
1452    /// assert_eq!(x, Some(42));
1453    ///
1454    /// let mut x: Option<u32> = None;
1455    /// assert_eq!(x.iter_mut().next(), None);
1456    /// ```
1457    #[inline]
1458    #[stable(feature = "rust1", since = "1.0.0")]
1459    pub fn iter_mut(&mut self) -> IterMut<'_, T> {
1460        IterMut { inner: Item { opt: self.as_mut() } }
1461    }
1462
1463    /////////////////////////////////////////////////////////////////////////
1464    // Boolean operations on the values, eager and lazy
1465    /////////////////////////////////////////////////////////////////////////
1466
1467    /// Returns [`None`] if the option is [`None`], otherwise returns `optb`.
1468    ///
1469    /// Arguments passed to `and` are eagerly evaluated; if you are passing the
1470    /// result of a function call, it is recommended to use [`and_then`], which is
1471    /// lazily evaluated.
1472    ///
1473    /// [`and_then`]: Option::and_then
1474    ///
1475    /// # Examples
1476    ///
1477    /// ```
1478    /// let x = Some(2);
1479    /// let y: Option<&str> = None;
1480    /// assert_eq!(x.and(y), None);
1481    ///
1482    /// let x: Option<u32> = None;
1483    /// let y = Some("foo");
1484    /// assert_eq!(x.and(y), None);
1485    ///
1486    /// let x = Some(2);
1487    /// let y = Some("foo");
1488    /// assert_eq!(x.and(y), Some("foo"));
1489    ///
1490    /// let x: Option<u32> = None;
1491    /// let y: Option<&str> = None;
1492    /// assert_eq!(x.and(y), None);
1493    /// ```
1494    #[inline]
1495    #[stable(feature = "rust1", since = "1.0.0")]
1496    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1497    pub const fn and<U>(self, optb: Option<U>) -> Option<U>
1498    where
1499        T: [const] Destruct,
1500        U: [const] Destruct,
1501    {
1502        match self {
1503            Some(_) => optb,
1504            None => None,
1505        }
1506    }
1507
1508    /// Returns [`None`] if the option is [`None`], otherwise calls `f` with the
1509    /// wrapped value and returns the result.
1510    ///
1511    /// Some languages call this operation flatmap.
1512    ///
1513    /// # Examples
1514    ///
1515    /// ```
1516    /// fn sq_then_to_string(x: u32) -> Option<String> {
1517    ///     x.checked_mul(x).map(|sq| sq.to_string())
1518    /// }
1519    ///
1520    /// assert_eq!(Some(2).and_then(sq_then_to_string), Some(4.to_string()));
1521    /// assert_eq!(Some(1_000_000).and_then(sq_then_to_string), None); // overflowed!
1522    /// assert_eq!(None.and_then(sq_then_to_string), None);
1523    /// ```
1524    ///
1525    /// Often used to chain fallible operations that may return [`None`].
1526    ///
1527    /// ```
1528    /// let arr_2d = [["A0", "A1"], ["B0", "B1"]];
1529    ///
1530    /// let item_0_1 = arr_2d.get(0).and_then(|row| row.get(1));
1531    /// assert_eq!(item_0_1, Some(&"A1"));
1532    ///
1533    /// let item_2_0 = arr_2d.get(2).and_then(|row| row.get(0));
1534    /// assert_eq!(item_2_0, None);
1535    /// ```
1536    #[doc(alias = "flatmap")]
1537    #[inline]
1538    #[stable(feature = "rust1", since = "1.0.0")]
1539    #[rustc_confusables("flat_map", "flatmap")]
1540    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1541    pub const fn and_then<U, F>(self, f: F) -> Option<U>
1542    where
1543        F: [const] FnOnce(T) -> Option<U> + [const] Destruct,
1544    {
1545        match self {
1546            Some(x) => f(x),
1547            None => None,
1548        }
1549    }
1550
1551    /// Returns [`None`] if the option is [`None`], otherwise calls `predicate`
1552    /// with the wrapped value and returns:
1553    ///
1554    /// - [`Some(t)`] if `predicate` returns `true` (where `t` is the wrapped
1555    ///   value), and
1556    /// - [`None`] if `predicate` returns `false`.
1557    ///
1558    /// This function works similar to [`Iterator::filter()`]. You can imagine
1559    /// the `Option<T>` being an iterator over one or zero elements. `filter()`
1560    /// lets you decide which elements to keep.
1561    ///
1562    /// # Examples
1563    ///
1564    /// ```rust
1565    /// fn is_even(n: &i32) -> bool {
1566    ///     n % 2 == 0
1567    /// }
1568    ///
1569    /// assert_eq!(None.filter(is_even), None);
1570    /// assert_eq!(Some(3).filter(is_even), None);
1571    /// assert_eq!(Some(4).filter(is_even), Some(4));
1572    /// ```
1573    ///
1574    /// [`Some(t)`]: Some
1575    #[inline]
1576    #[stable(feature = "option_filter", since = "1.27.0")]
1577    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1578    pub const fn filter<P>(self, predicate: P) -> Self
1579    where
1580        P: [const] FnOnce(&T) -> bool + [const] Destruct,
1581        T: [const] Destruct,
1582    {
1583        if let Some(x) = self {
1584            if predicate(&x) {
1585                return Some(x);
1586            }
1587        }
1588        None
1589    }
1590
1591    /// Returns the option if it contains a value, otherwise returns `optb`.
1592    ///
1593    /// Arguments passed to `or` are eagerly evaluated; if you are passing the
1594    /// result of a function call, it is recommended to use [`or_else`], which is
1595    /// lazily evaluated.
1596    ///
1597    /// [`or_else`]: Option::or_else
1598    ///
1599    /// # Examples
1600    ///
1601    /// ```
1602    /// let x = Some(2);
1603    /// let y = None;
1604    /// assert_eq!(x.or(y), Some(2));
1605    ///
1606    /// let x = None;
1607    /// let y = Some(100);
1608    /// assert_eq!(x.or(y), Some(100));
1609    ///
1610    /// let x = Some(2);
1611    /// let y = Some(100);
1612    /// assert_eq!(x.or(y), Some(2));
1613    ///
1614    /// let x: Option<u32> = None;
1615    /// let y = None;
1616    /// assert_eq!(x.or(y), None);
1617    /// ```
1618    #[inline]
1619    #[stable(feature = "rust1", since = "1.0.0")]
1620    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1621    pub const fn or(self, optb: Option<T>) -> Option<T>
1622    where
1623        T: [const] Destruct,
1624    {
1625        match self {
1626            x @ Some(_) => x,
1627            None => optb,
1628        }
1629    }
1630
1631    /// Returns the option if it contains a value, otherwise calls `f` and
1632    /// returns the result.
1633    ///
1634    /// # Examples
1635    ///
1636    /// ```
1637    /// fn nobody() -> Option<&'static str> { None }
1638    /// fn vikings() -> Option<&'static str> { Some("vikings") }
1639    ///
1640    /// assert_eq!(Some("barbarians").or_else(vikings), Some("barbarians"));
1641    /// assert_eq!(None.or_else(vikings), Some("vikings"));
1642    /// assert_eq!(None.or_else(nobody), None);
1643    /// ```
1644    #[inline]
1645    #[stable(feature = "rust1", since = "1.0.0")]
1646    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1647    pub const fn or_else<F>(self, f: F) -> Option<T>
1648    where
1649        F: [const] FnOnce() -> Option<T> + [const] Destruct,
1650        //FIXME(const_hack): this `T: [const] Destruct` is unnecessary, but even precise live drops can't tell
1651        // no value of type `T` gets dropped here
1652        T: [const] Destruct,
1653    {
1654        match self {
1655            x @ Some(_) => x,
1656            None => f(),
1657        }
1658    }
1659
1660    /// Returns [`Some`] if exactly one of `self`, `optb` is [`Some`], otherwise returns [`None`].
1661    ///
1662    /// # Examples
1663    ///
1664    /// ```
1665    /// let x = Some(2);
1666    /// let y: Option<u32> = None;
1667    /// assert_eq!(x.xor(y), Some(2));
1668    ///
1669    /// let x: Option<u32> = None;
1670    /// let y = Some(2);
1671    /// assert_eq!(x.xor(y), Some(2));
1672    ///
1673    /// let x = Some(2);
1674    /// let y = Some(2);
1675    /// assert_eq!(x.xor(y), None);
1676    ///
1677    /// let x: Option<u32> = None;
1678    /// let y: Option<u32> = None;
1679    /// assert_eq!(x.xor(y), None);
1680    /// ```
1681    #[inline]
1682    #[stable(feature = "option_xor", since = "1.37.0")]
1683    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1684    pub const fn xor(self, optb: Option<T>) -> Option<T>
1685    where
1686        T: [const] Destruct,
1687    {
1688        match (self, optb) {
1689            (a @ Some(_), None) => a,
1690            (None, b @ Some(_)) => b,
1691            _ => None,
1692        }
1693    }
1694
1695    /////////////////////////////////////////////////////////////////////////
1696    // Entry-like operations to insert a value and return a reference
1697    /////////////////////////////////////////////////////////////////////////
1698
1699    /// Inserts `value` into the option, then returns a mutable reference to it.
1700    ///
1701    /// If the option already contains a value, the old value is dropped.
1702    ///
1703    /// See also [`Option::get_or_insert`], which doesn't update the value if
1704    /// the option already contains [`Some`].
1705    ///
1706    /// # Example
1707    ///
1708    /// ```
1709    /// let mut opt = None;
1710    /// let val = opt.insert(1);
1711    /// assert_eq!(*val, 1);
1712    /// assert_eq!(opt.unwrap(), 1);
1713    /// let val = opt.insert(2);
1714    /// assert_eq!(*val, 2);
1715    /// *val = 3;
1716    /// assert_eq!(opt.unwrap(), 3);
1717    /// ```
1718    #[must_use = "if you intended to set a value, consider assignment instead"]
1719    #[inline]
1720    #[stable(feature = "option_insert", since = "1.53.0")]
1721    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1722    pub const fn insert(&mut self, value: T) -> &mut T
1723    where
1724        T: [const] Destruct,
1725    {
1726        *self = Some(value);
1727
1728        // SAFETY: the code above just filled the option
1729        unsafe { self.as_mut().unwrap_unchecked() }
1730    }
1731
1732    /// Inserts `value` into the option if it is [`None`], then
1733    /// returns a mutable reference to the contained value.
1734    ///
1735    /// See also [`Option::insert`], which updates the value even if
1736    /// the option already contains [`Some`].
1737    ///
1738    /// # Examples
1739    ///
1740    /// ```
1741    /// let mut x = None;
1742    ///
1743    /// {
1744    ///     let y: &mut u32 = x.get_or_insert(5);
1745    ///     assert_eq!(y, &5);
1746    ///
1747    ///     *y = 7;
1748    /// }
1749    ///
1750    /// assert_eq!(x, Some(7));
1751    /// ```
1752    #[inline]
1753    #[stable(feature = "option_entry", since = "1.20.0")]
1754    pub fn get_or_insert(&mut self, value: T) -> &mut T {
1755        self.get_or_insert_with(|| value)
1756    }
1757
1758    /// Inserts the default value into the option if it is [`None`], then
1759    /// returns a mutable reference to the contained value.
1760    ///
1761    /// # Examples
1762    ///
1763    /// ```
1764    /// let mut x = None;
1765    ///
1766    /// {
1767    ///     let y: &mut u32 = x.get_or_insert_default();
1768    ///     assert_eq!(y, &0);
1769    ///
1770    ///     *y = 7;
1771    /// }
1772    ///
1773    /// assert_eq!(x, Some(7));
1774    /// ```
1775    #[inline]
1776    #[stable(feature = "option_get_or_insert_default", since = "1.83.0")]
1777    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1778    pub const fn get_or_insert_default(&mut self) -> &mut T
1779    where
1780        T: [const] Default + [const] Destruct,
1781    {
1782        self.get_or_insert_with(T::default)
1783    }
1784
1785    /// Inserts a value computed from `f` into the option if it is [`None`],
1786    /// then returns a mutable reference to the contained value.
1787    ///
1788    /// # Examples
1789    ///
1790    /// ```
1791    /// let mut x = None;
1792    ///
1793    /// {
1794    ///     let y: &mut u32 = x.get_or_insert_with(|| 5);
1795    ///     assert_eq!(y, &5);
1796    ///
1797    ///     *y = 7;
1798    /// }
1799    ///
1800    /// assert_eq!(x, Some(7));
1801    /// ```
1802    #[inline]
1803    #[stable(feature = "option_entry", since = "1.20.0")]
1804    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1805    pub const fn get_or_insert_with<F>(&mut self, f: F) -> &mut T
1806    where
1807        F: [const] FnOnce() -> T + [const] Destruct,
1808        T: [const] Destruct,
1809    {
1810        if let None = self {
1811            *self = Some(f());
1812        }
1813
1814        // SAFETY: a `None` variant for `self` would have been replaced by a `Some`
1815        // variant in the code above.
1816        unsafe { self.as_mut().unwrap_unchecked() }
1817    }
1818
1819    /// If the option is `None`, calls the closure and inserts its output if successful.
1820    ///
1821    /// If the closure returns a residual value such as `Err` or `None`,
1822    /// that residual value is returned and nothing is inserted.
1823    ///
1824    /// If the option is `Some`, nothing is inserted.
1825    ///
1826    /// Unless a residual is returned, a mutable reference to the value
1827    /// of the option will be output.
1828    ///
1829    /// # Examples
1830    ///
1831    /// ```
1832    /// #![feature(option_get_or_try_insert_with)]
1833    /// let mut o1: Option<u32> = None;
1834    /// let mut o2: Option<u8> = None;
1835    ///
1836    /// let number = "12345";
1837    ///
1838    /// assert_eq!(o1.get_or_try_insert_with(|| number.parse()).copied(), Ok(12345));
1839    /// assert!(o2.get_or_try_insert_with(|| number.parse()).is_err());
1840    /// assert_eq!(o1, Some(12345));
1841    /// assert_eq!(o2, None);
1842    /// ```
1843    #[inline]
1844    #[unstable(feature = "option_get_or_try_insert_with", issue = "143648")]
1845    pub fn get_or_try_insert_with<'a, R, F>(
1846        &'a mut self,
1847        f: F,
1848    ) -> <R::Residual as Residual<&'a mut T>>::TryType
1849    where
1850        F: FnOnce() -> R,
1851        R: Try<Output = T, Residual: Residual<&'a mut T>>,
1852    {
1853        if let None = self {
1854            *self = Some(f()?);
1855        }
1856        // SAFETY: a `None` variant for `self` would have been replaced by a `Some`
1857        // variant in the code above.
1858
1859        Try::from_output(unsafe { self.as_mut().unwrap_unchecked() })
1860    }
1861
1862    /////////////////////////////////////////////////////////////////////////
1863    // Misc
1864    /////////////////////////////////////////////////////////////////////////
1865
1866    /// Takes the value out of the option, leaving a [`None`] in its place.
1867    ///
1868    /// # Examples
1869    ///
1870    /// ```
1871    /// let mut x = Some(2);
1872    /// let y = x.take();
1873    /// assert_eq!(x, None);
1874    /// assert_eq!(y, Some(2));
1875    ///
1876    /// let mut x: Option<u32> = None;
1877    /// let y = x.take();
1878    /// assert_eq!(x, None);
1879    /// assert_eq!(y, None);
1880    /// ```
1881    #[inline]
1882    #[stable(feature = "rust1", since = "1.0.0")]
1883    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
1884    pub const fn take(&mut self) -> Option<T> {
1885        // FIXME(const-hack) replace `mem::replace` by `mem::take` when the latter is const ready
1886        mem::replace(self, None)
1887    }
1888
1889    /// Takes the value out of the option, but only if the predicate evaluates to
1890    /// `true` on a mutable reference to the value.
1891    ///
1892    /// In other words, replaces `self` with `None` if the predicate returns `true`.
1893    /// This method operates similar to [`Option::take`] but conditional.
1894    ///
1895    /// # Examples
1896    ///
1897    /// ```
1898    /// let mut x = Some(42);
1899    ///
1900    /// let prev = x.take_if(|v| if *v == 42 {
1901    ///     *v += 1;
1902    ///     false
1903    /// } else {
1904    ///     false
1905    /// });
1906    /// assert_eq!(x, Some(43));
1907    /// assert_eq!(prev, None);
1908    ///
1909    /// let prev = x.take_if(|v| *v == 43);
1910    /// assert_eq!(x, None);
1911    /// assert_eq!(prev, Some(43));
1912    /// ```
1913    #[inline]
1914    #[stable(feature = "option_take_if", since = "1.80.0")]
1915    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1916    pub const fn take_if<P>(&mut self, predicate: P) -> Option<T>
1917    where
1918        P: [const] FnOnce(&mut T) -> bool + [const] Destruct,
1919    {
1920        if self.as_mut().map_or(false, predicate) { self.take() } else { None }
1921    }
1922
1923    /// Replaces the actual value in the option by the value given in parameter,
1924    /// returning the old value if present,
1925    /// leaving a [`Some`] in its place without deinitializing either one.
1926    ///
1927    /// # Examples
1928    ///
1929    /// ```
1930    /// let mut x = Some(2);
1931    /// let old = x.replace(5);
1932    /// assert_eq!(x, Some(5));
1933    /// assert_eq!(old, Some(2));
1934    ///
1935    /// let mut x = None;
1936    /// let old = x.replace(3);
1937    /// assert_eq!(x, Some(3));
1938    /// assert_eq!(old, None);
1939    /// ```
1940    #[inline]
1941    #[stable(feature = "option_replace", since = "1.31.0")]
1942    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
1943    pub const fn replace(&mut self, value: T) -> Option<T> {
1944        mem::replace(self, Some(value))
1945    }
1946
1947    /// Zips `self` with another `Option`.
1948    ///
1949    /// If `self` is `Some(s)` and `other` is `Some(o)`, this method returns `Some((s, o))`.
1950    /// Otherwise, `None` is returned.
1951    ///
1952    /// # Examples
1953    ///
1954    /// ```
1955    /// let x = Some(1);
1956    /// let y = Some("hi");
1957    /// let z = None::<u8>;
1958    ///
1959    /// assert_eq!(x.zip(y), Some((1, "hi")));
1960    /// assert_eq!(x.zip(z), None);
1961    /// ```
1962    #[stable(feature = "option_zip_option", since = "1.46.0")]
1963    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
1964    pub const fn zip<U>(self, other: Option<U>) -> Option<(T, U)>
1965    where
1966        T: [const] Destruct,
1967        U: [const] Destruct,
1968    {
1969        match (self, other) {
1970            (Some(a), Some(b)) => Some((a, b)),
1971            _ => None,
1972        }
1973    }
1974
1975    /// Zips `self` and another `Option` with function `f`.
1976    ///
1977    /// If `self` is `Some(s)` and `other` is `Some(o)`, this method returns `Some(f(s, o))`.
1978    /// Otherwise, `None` is returned.
1979    ///
1980    /// # Examples
1981    ///
1982    /// ```
1983    /// #![feature(option_zip)]
1984    ///
1985    /// #[derive(Debug, PartialEq)]
1986    /// struct Point {
1987    ///     x: f64,
1988    ///     y: f64,
1989    /// }
1990    ///
1991    /// impl Point {
1992    ///     fn new(x: f64, y: f64) -> Self {
1993    ///         Self { x, y }
1994    ///     }
1995    /// }
1996    ///
1997    /// let x = Some(17.5);
1998    /// let y = Some(42.7);
1999    ///
2000    /// assert_eq!(x.zip_with(y, Point::new), Some(Point { x: 17.5, y: 42.7 }));
2001    /// assert_eq!(x.zip_with(None, Point::new), None);
2002    /// ```
2003    #[unstable(feature = "option_zip", issue = "70086")]
2004    #[rustc_const_unstable(feature = "const_option_ops", issue = "143956")]
2005    pub const fn zip_with<U, F, R>(self, other: Option<U>, f: F) -> Option<R>
2006    where
2007        F: [const] FnOnce(T, U) -> R + [const] Destruct,
2008        T: [const] Destruct,
2009        U: [const] Destruct,
2010    {
2011        match (self, other) {
2012            (Some(a), Some(b)) => Some(f(a, b)),
2013            _ => None,
2014        }
2015    }
2016
2017    /// Reduces two options into one, using the provided function if both are `Some`.
2018    ///
2019    /// If `self` is `Some(s)` and `other` is `Some(o)`, this method returns `Some(f(s, o))`.
2020    /// Otherwise, if only one of `self` and `other` is `Some`, that one is returned.
2021    /// If both `self` and `other` are `None`, `None` is returned.
2022    ///
2023    /// # Examples
2024    ///
2025    /// ```
2026    /// #![feature(option_reduce)]
2027    ///
2028    /// let s12 = Some(12);
2029    /// let s17 = Some(17);
2030    /// let n = None;
2031    /// let f = |a, b| a + b;
2032    ///
2033    /// assert_eq!(s12.reduce(s17, f), Some(29));
2034    /// assert_eq!(s12.reduce(n, f), Some(12));
2035    /// assert_eq!(n.reduce(s17, f), Some(17));
2036    /// assert_eq!(n.reduce(n, f), None);
2037    /// ```
2038    #[unstable(feature = "option_reduce", issue = "144273")]
2039    pub fn reduce<U, R, F>(self, other: Option<U>, f: F) -> Option<R>
2040    where
2041        T: Into<R>,
2042        U: Into<R>,
2043        F: FnOnce(T, U) -> R,
2044    {
2045        match (self, other) {
2046            (Some(a), Some(b)) => Some(f(a, b)),
2047            (Some(a), _) => Some(a.into()),
2048            (_, Some(b)) => Some(b.into()),
2049            _ => None,
2050        }
2051    }
2052}
2053
2054impl<T: IntoIterator> Option<T> {
2055    /// Transforms an optional iterator into an iterator.
2056    ///
2057    /// If `self` is `None`, the resulting iterator is empty.
2058    /// Otherwise, an iterator is made from the `Some` value and returned.
2059    /// # Examples
2060    /// ```
2061    /// #![feature(option_into_flat_iter)]
2062    ///
2063    /// let o1 = Some([1, 2]);
2064    /// let o2 = None::<&[usize]>;
2065    ///
2066    /// assert_eq!(o1.into_flat_iter().collect::<Vec<_>>(), [1, 2]);
2067    /// assert_eq!(o2.into_flat_iter().collect::<Vec<_>>(), Vec::<&usize>::new());
2068    /// ```
2069    #[unstable(feature = "option_into_flat_iter", issue = "148441")]
2070    pub fn into_flat_iter<A>(self) -> OptionFlatten<A>
2071    where
2072        T: IntoIterator<IntoIter = A>,
2073    {
2074        OptionFlatten { iter: self.map(IntoIterator::into_iter) }
2075    }
2076}
2077
2078impl<T, U> Option<(T, U)> {
2079    /// Unzips an option containing a tuple of two options.
2080    ///
2081    /// If `self` is `Some((a, b))` this method returns `(Some(a), Some(b))`.
2082    /// Otherwise, `(None, None)` is returned.
2083    ///
2084    /// # Examples
2085    ///
2086    /// ```
2087    /// let x = Some((1, "hi"));
2088    /// let y = None::<(u8, u32)>;
2089    ///
2090    /// assert_eq!(x.unzip(), (Some(1), Some("hi")));
2091    /// assert_eq!(y.unzip(), (None, None));
2092    /// ```
2093    #[inline]
2094    #[stable(feature = "unzip_option", since = "1.66.0")]
2095    pub fn unzip(self) -> (Option<T>, Option<U>) {
2096        match self {
2097            Some((a, b)) => (Some(a), Some(b)),
2098            None => (None, None),
2099        }
2100    }
2101}
2102
2103impl<T> Option<&T> {
2104    /// Maps an `Option<&T>` to an `Option<T>` by copying the contents of the
2105    /// option.
2106    ///
2107    /// # Examples
2108    ///
2109    /// ```
2110    /// let x = 12;
2111    /// let opt_x = Some(&x);
2112    /// assert_eq!(opt_x, Some(&12));
2113    /// let copied = opt_x.copied();
2114    /// assert_eq!(copied, Some(12));
2115    /// ```
2116    #[must_use = "`self` will be dropped if the result is not used"]
2117    #[stable(feature = "copied", since = "1.35.0")]
2118    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
2119    pub const fn copied(self) -> Option<T>
2120    where
2121        T: Copy,
2122    {
2123        // FIXME(const-hack): this implementation, which sidesteps using `Option::map` since it's not const
2124        // ready yet, should be reverted when possible to avoid code repetition
2125        match self {
2126            Some(&v) => Some(v),
2127            None => None,
2128        }
2129    }
2130
2131    /// Maps an `Option<&T>` to an `Option<T>` by cloning the contents of the
2132    /// option.
2133    ///
2134    /// # Examples
2135    ///
2136    /// ```
2137    /// let x = 12;
2138    /// let opt_x = Some(&x);
2139    /// assert_eq!(opt_x, Some(&12));
2140    /// let cloned = opt_x.cloned();
2141    /// assert_eq!(cloned, Some(12));
2142    /// ```
2143    #[must_use = "`self` will be dropped if the result is not used"]
2144    #[stable(feature = "rust1", since = "1.0.0")]
2145    pub fn cloned(self) -> Option<T>
2146    where
2147        T: Clone,
2148    {
2149        self.map(T::clone)
2150    }
2151}
2152
2153impl<T> Option<&mut T> {
2154    /// Maps an `Option<&mut T>` to an `Option<T>` by copying the contents of the
2155    /// option.
2156    ///
2157    /// # Examples
2158    ///
2159    /// ```
2160    /// let mut x = 12;
2161    /// let opt_x = Some(&mut x);
2162    /// assert_eq!(opt_x, Some(&mut 12));
2163    /// let copied = opt_x.copied();
2164    /// assert_eq!(copied, Some(12));
2165    /// ```
2166    #[must_use = "`self` will be dropped if the result is not used"]
2167    #[stable(feature = "copied", since = "1.35.0")]
2168    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
2169    pub const fn copied(self) -> Option<T>
2170    where
2171        T: Copy,
2172    {
2173        match self {
2174            Some(&mut t) => Some(t),
2175            None => None,
2176        }
2177    }
2178
2179    /// Maps an `Option<&mut T>` to an `Option<T>` by cloning the contents of the
2180    /// option.
2181    ///
2182    /// # Examples
2183    ///
2184    /// ```
2185    /// let mut x = 12;
2186    /// let opt_x = Some(&mut x);
2187    /// assert_eq!(opt_x, Some(&mut 12));
2188    /// let cloned = opt_x.cloned();
2189    /// assert_eq!(cloned, Some(12));
2190    /// ```
2191    #[must_use = "`self` will be dropped if the result is not used"]
2192    #[stable(since = "1.26.0", feature = "option_ref_mut_cloned")]
2193    pub fn cloned(self) -> Option<T>
2194    where
2195        T: Clone,
2196    {
2197        self.as_deref().map(T::clone)
2198    }
2199}
2200
2201impl<T, E> Option<Result<T, E>> {
2202    /// Transposes an `Option` of a [`Result`] into a [`Result`] of an `Option`.
2203    ///
2204    /// <code>[Some]\([Ok]\(\_))</code> is mapped to <code>[Ok]\([Some]\(\_))</code>,
2205    /// <code>[Some]\([Err]\(\_))</code> is mapped to <code>[Err]\(\_)</code>,
2206    /// and [`None`] will be mapped to <code>[Ok]\([None])</code>.
2207    ///
2208    /// # Examples
2209    ///
2210    /// ```
2211    /// #[derive(Debug, Eq, PartialEq)]
2212    /// struct SomeErr;
2213    ///
2214    /// let x: Option<Result<i32, SomeErr>> = Some(Ok(5));
2215    /// let y: Result<Option<i32>, SomeErr> = Ok(Some(5));
2216    /// assert_eq!(x.transpose(), y);
2217    /// ```
2218    #[inline]
2219    #[stable(feature = "transpose_result", since = "1.33.0")]
2220    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
2221    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
2222    pub const fn transpose(self) -> Result<Option<T>, E> {
2223        match self {
2224            Some(Ok(x)) => Ok(Some(x)),
2225            Some(Err(e)) => Err(e),
2226            None => Ok(None),
2227        }
2228    }
2229}
2230
2231#[cfg_attr(not(panic = "immediate-abort"), inline(never))]
2232#[cfg_attr(panic = "immediate-abort", inline)]
2233#[cold]
2234#[track_caller]
2235const fn unwrap_failed() -> ! {
2236    panic("called `Option::unwrap()` on a `None` value")
2237}
2238
2239// This is a separate function to reduce the code size of .expect() itself.
2240#[cfg_attr(not(panic = "immediate-abort"), inline(never))]
2241#[cfg_attr(panic = "immediate-abort", inline)]
2242#[cold]
2243#[track_caller]
2244const fn expect_failed(msg: &str) -> ! {
2245    panic_display(&msg)
2246}
2247
2248/////////////////////////////////////////////////////////////////////////////
2249// Trait implementations
2250/////////////////////////////////////////////////////////////////////////////
2251
2252#[stable(feature = "rust1", since = "1.0.0")]
2253#[rustc_const_unstable(feature = "const_clone", issue = "142757")]
2254impl<T> const Clone for Option<T>
2255where
2256    // FIXME(const_hack): the T: [const] Destruct should be inferred from the Self: [const] Destruct in clone_from.
2257    // See https://github.com/rust-lang/rust/issues/144207
2258    T: [const] Clone + [const] Destruct,
2259{
2260    #[inline]
2261    fn clone(&self) -> Self {
2262        match self {
2263            Some(x) => Some(x.clone()),
2264            None => None,
2265        }
2266    }
2267
2268    #[inline]
2269    fn clone_from(&mut self, source: &Self) {
2270        match (self, source) {
2271            (Some(to), Some(from)) => to.clone_from(from),
2272            (to, from) => *to = from.clone(),
2273        }
2274    }
2275}
2276
2277#[unstable(feature = "ergonomic_clones", issue = "132290")]
2278impl<T> crate::clone::UseCloned for Option<T> where T: crate::clone::UseCloned {}
2279
2280#[doc(hidden)]
2281#[unstable(feature = "trivial_clone", issue = "none")]
2282#[rustc_const_unstable(feature = "const_clone", issue = "142757")]
2283unsafe impl<T> const TrivialClone for Option<T> where T: [const] TrivialClone + [const] Destruct {}
2284
2285#[stable(feature = "rust1", since = "1.0.0")]
2286#[rustc_const_unstable(feature = "const_default", issue = "143894")]
2287impl<T> const Default for Option<T> {
2288    /// Returns [`None`][Option::None].
2289    ///
2290    /// # Examples
2291    ///
2292    /// ```
2293    /// let opt: Option<u32> = Option::default();
2294    /// assert!(opt.is_none());
2295    /// ```
2296    #[inline]
2297    fn default() -> Option<T> {
2298        None
2299    }
2300}
2301
2302#[stable(feature = "rust1", since = "1.0.0")]
2303#[rustc_const_unstable(feature = "const_iter", issue = "92476")]
2304impl<T> const IntoIterator for Option<T> {
2305    type Item = T;
2306    type IntoIter = IntoIter<T>;
2307
2308    /// Returns a consuming iterator over the possibly contained value.
2309    ///
2310    /// # Examples
2311    ///
2312    /// ```
2313    /// let x = Some("string");
2314    /// let v: Vec<&str> = x.into_iter().collect();
2315    /// assert_eq!(v, ["string"]);
2316    ///
2317    /// let x = None;
2318    /// let v: Vec<&str> = x.into_iter().collect();
2319    /// assert!(v.is_empty());
2320    /// ```
2321    #[inline]
2322    fn into_iter(self) -> IntoIter<T> {
2323        IntoIter { inner: Item { opt: self } }
2324    }
2325}
2326
2327#[stable(since = "1.4.0", feature = "option_iter")]
2328impl<'a, T> IntoIterator for &'a Option<T> {
2329    type Item = &'a T;
2330    type IntoIter = Iter<'a, T>;
2331
2332    fn into_iter(self) -> Iter<'a, T> {
2333        self.iter()
2334    }
2335}
2336
2337#[stable(since = "1.4.0", feature = "option_iter")]
2338impl<'a, T> IntoIterator for &'a mut Option<T> {
2339    type Item = &'a mut T;
2340    type IntoIter = IterMut<'a, T>;
2341
2342    fn into_iter(self) -> IterMut<'a, T> {
2343        self.iter_mut()
2344    }
2345}
2346
2347#[stable(since = "1.12.0", feature = "option_from")]
2348#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2349impl<T> const From<T> for Option<T> {
2350    /// Moves `val` into a new [`Some`].
2351    ///
2352    /// # Examples
2353    ///
2354    /// ```
2355    /// let o: Option<u8> = Option::from(67);
2356    ///
2357    /// assert_eq!(Some(67), o);
2358    /// ```
2359    fn from(val: T) -> Option<T> {
2360        Some(val)
2361    }
2362}
2363
2364#[stable(feature = "option_ref_from_ref_option", since = "1.30.0")]
2365#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2366impl<'a, T> const From<&'a Option<T>> for Option<&'a T> {
2367    /// Converts from `&Option<T>` to `Option<&T>`.
2368    ///
2369    /// # Examples
2370    ///
2371    /// Converts an <code>[Option]<[String]></code> into an <code>[Option]<[usize]></code>, preserving
2372    /// the original. The [`map`] method takes the `self` argument by value, consuming the original,
2373    /// so this technique uses `from` to first take an [`Option`] to a reference
2374    /// to the value inside the original.
2375    ///
2376    /// [`map`]: Option::map
2377    /// [String]: ../../std/string/struct.String.html "String"
2378    ///
2379    /// ```
2380    /// let s: Option<String> = Some(String::from("Hello, Rustaceans!"));
2381    /// let o: Option<usize> = Option::from(&s).map(|ss: &String| ss.len());
2382    ///
2383    /// println!("Can still print s: {s:?}");
2384    ///
2385    /// assert_eq!(o, Some(18));
2386    /// ```
2387    fn from(o: &'a Option<T>) -> Option<&'a T> {
2388        o.as_ref()
2389    }
2390}
2391
2392#[stable(feature = "option_ref_from_ref_option", since = "1.30.0")]
2393#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
2394impl<'a, T> const From<&'a mut Option<T>> for Option<&'a mut T> {
2395    /// Converts from `&mut Option<T>` to `Option<&mut T>`
2396    ///
2397    /// # Examples
2398    ///
2399    /// ```
2400    /// let mut s = Some(String::from("Hello"));
2401    /// let o: Option<&mut String> = Option::from(&mut s);
2402    ///
2403    /// match o {
2404    ///     Some(t) => *t = String::from("Hello, Rustaceans!"),
2405    ///     None => (),
2406    /// }
2407    ///
2408    /// assert_eq!(s, Some(String::from("Hello, Rustaceans!")));
2409    /// ```
2410    fn from(o: &'a mut Option<T>) -> Option<&'a mut T> {
2411        o.as_mut()
2412    }
2413}
2414
2415// Ideally, LLVM should be able to optimize our derive code to this.
2416// Once https://github.com/llvm/llvm-project/issues/52622 is fixed, we can
2417// go back to deriving `PartialEq`.
2418#[stable(feature = "rust1", since = "1.0.0")]
2419impl<T> crate::marker::StructuralPartialEq for Option<T> {}
2420#[stable(feature = "rust1", since = "1.0.0")]
2421#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2422impl<T: [const] PartialEq> const PartialEq for Option<T> {
2423    #[inline]
2424    fn eq(&self, other: &Self) -> bool {
2425        // Spelling out the cases explicitly optimizes better than
2426        // `_ => false`
2427        match (self, other) {
2428            (Some(l), Some(r)) => *l == *r,
2429            (Some(_), None) => false,
2430            (None, Some(_)) => false,
2431            (None, None) => true,
2432        }
2433    }
2434}
2435
2436// Manually implementing here somewhat improves codegen for
2437// https://github.com/rust-lang/rust/issues/49892, although still
2438// not optimal.
2439#[stable(feature = "rust1", since = "1.0.0")]
2440#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2441impl<T: [const] PartialOrd> const PartialOrd for Option<T> {
2442    #[inline]
2443    fn partial_cmp(&self, other: &Self) -> Option<cmp::Ordering> {
2444        match (self, other) {
2445            (Some(l), Some(r)) => l.partial_cmp(r),
2446            (Some(_), None) => Some(cmp::Ordering::Greater),
2447            (None, Some(_)) => Some(cmp::Ordering::Less),
2448            (None, None) => Some(cmp::Ordering::Equal),
2449        }
2450    }
2451}
2452
2453#[stable(feature = "rust1", since = "1.0.0")]
2454#[rustc_const_unstable(feature = "const_cmp", issue = "143800")]
2455impl<T: [const] Ord> const Ord for Option<T> {
2456    #[inline]
2457    fn cmp(&self, other: &Self) -> cmp::Ordering {
2458        match (self, other) {
2459            (Some(l), Some(r)) => l.cmp(r),
2460            (Some(_), None) => cmp::Ordering::Greater,
2461            (None, Some(_)) => cmp::Ordering::Less,
2462            (None, None) => cmp::Ordering::Equal,
2463        }
2464    }
2465}
2466
2467/////////////////////////////////////////////////////////////////////////////
2468// The Option Iterators
2469/////////////////////////////////////////////////////////////////////////////
2470
2471#[derive(Clone, Debug)]
2472struct Item<A> {
2473    opt: Option<A>,
2474}
2475
2476#[rustc_const_unstable(feature = "const_iter", issue = "92476")]
2477impl<A> const Iterator for Item<A> {
2478    type Item = A;
2479
2480    #[inline]
2481    fn next(&mut self) -> Option<A> {
2482        self.opt.take()
2483    }
2484
2485    #[inline]
2486    fn size_hint(&self) -> (usize, Option<usize>) {
2487        let len = self.opt.len();
2488        (len, Some(len))
2489    }
2490}
2491
2492impl<A> DoubleEndedIterator for Item<A> {
2493    #[inline]
2494    fn next_back(&mut self) -> Option<A> {
2495        self.opt.take()
2496    }
2497}
2498
2499impl<A> ExactSizeIterator for Item<A> {
2500    #[inline]
2501    fn len(&self) -> usize {
2502        self.opt.len()
2503    }
2504}
2505impl<A> FusedIterator for Item<A> {}
2506unsafe impl<A> TrustedLen for Item<A> {}
2507
2508/// An iterator over a reference to the [`Some`] variant of an [`Option`].
2509///
2510/// The iterator yields one value if the [`Option`] is a [`Some`], otherwise none.
2511///
2512/// This `struct` is created by the [`Option::iter`] function.
2513#[stable(feature = "rust1", since = "1.0.0")]
2514#[derive(Debug)]
2515pub struct Iter<'a, A: 'a> {
2516    inner: Item<&'a A>,
2517}
2518
2519#[stable(feature = "rust1", since = "1.0.0")]
2520impl<'a, A> Iterator for Iter<'a, A> {
2521    type Item = &'a A;
2522
2523    #[inline]
2524    fn next(&mut self) -> Option<&'a A> {
2525        self.inner.next()
2526    }
2527    #[inline]
2528    fn size_hint(&self) -> (usize, Option<usize>) {
2529        self.inner.size_hint()
2530    }
2531}
2532
2533#[stable(feature = "rust1", since = "1.0.0")]
2534impl<'a, A> DoubleEndedIterator for Iter<'a, A> {
2535    #[inline]
2536    fn next_back(&mut self) -> Option<&'a A> {
2537        self.inner.next_back()
2538    }
2539}
2540
2541#[stable(feature = "rust1", since = "1.0.0")]
2542impl<A> ExactSizeIterator for Iter<'_, A> {}
2543
2544#[stable(feature = "fused", since = "1.26.0")]
2545impl<A> FusedIterator for Iter<'_, A> {}
2546
2547#[unstable(feature = "trusted_len", issue = "37572")]
2548unsafe impl<A> TrustedLen for Iter<'_, A> {}
2549
2550#[stable(feature = "rust1", since = "1.0.0")]
2551impl<A> Clone for Iter<'_, A> {
2552    #[inline]
2553    fn clone(&self) -> Self {
2554        Iter { inner: self.inner.clone() }
2555    }
2556}
2557
2558/// An iterator over a mutable reference to the [`Some`] variant of an [`Option`].
2559///
2560/// The iterator yields one value if the [`Option`] is a [`Some`], otherwise none.
2561///
2562/// This `struct` is created by the [`Option::iter_mut`] function.
2563#[stable(feature = "rust1", since = "1.0.0")]
2564#[derive(Debug)]
2565pub struct IterMut<'a, A: 'a> {
2566    inner: Item<&'a mut A>,
2567}
2568
2569#[stable(feature = "rust1", since = "1.0.0")]
2570impl<'a, A> Iterator for IterMut<'a, A> {
2571    type Item = &'a mut A;
2572
2573    #[inline]
2574    fn next(&mut self) -> Option<&'a mut A> {
2575        self.inner.next()
2576    }
2577    #[inline]
2578    fn size_hint(&self) -> (usize, Option<usize>) {
2579        self.inner.size_hint()
2580    }
2581}
2582
2583#[stable(feature = "rust1", since = "1.0.0")]
2584impl<'a, A> DoubleEndedIterator for IterMut<'a, A> {
2585    #[inline]
2586    fn next_back(&mut self) -> Option<&'a mut A> {
2587        self.inner.next_back()
2588    }
2589}
2590
2591#[stable(feature = "rust1", since = "1.0.0")]
2592impl<A> ExactSizeIterator for IterMut<'_, A> {}
2593
2594#[stable(feature = "fused", since = "1.26.0")]
2595impl<A> FusedIterator for IterMut<'_, A> {}
2596#[unstable(feature = "trusted_len", issue = "37572")]
2597unsafe impl<A> TrustedLen for IterMut<'_, A> {}
2598
2599/// An iterator over the value in [`Some`] variant of an [`Option`].
2600///
2601/// The iterator yields one value if the [`Option`] is a [`Some`], otherwise none.
2602///
2603/// This `struct` is created by the [`Option::into_iter`] function.
2604#[derive(Clone, Debug)]
2605#[stable(feature = "rust1", since = "1.0.0")]
2606pub struct IntoIter<A> {
2607    inner: Item<A>,
2608}
2609
2610#[stable(feature = "rust1", since = "1.0.0")]
2611#[rustc_const_unstable(feature = "const_iter", issue = "92476")]
2612impl<A> const Iterator for IntoIter<A> {
2613    type Item = A;
2614
2615    #[inline]
2616    fn next(&mut self) -> Option<A> {
2617        self.inner.next()
2618    }
2619    #[inline]
2620    fn size_hint(&self) -> (usize, Option<usize>) {
2621        self.inner.size_hint()
2622    }
2623}
2624
2625#[stable(feature = "rust1", since = "1.0.0")]
2626impl<A> DoubleEndedIterator for IntoIter<A> {
2627    #[inline]
2628    fn next_back(&mut self) -> Option<A> {
2629        self.inner.next_back()
2630    }
2631}
2632
2633#[stable(feature = "rust1", since = "1.0.0")]
2634impl<A> ExactSizeIterator for IntoIter<A> {}
2635
2636#[stable(feature = "fused", since = "1.26.0")]
2637impl<A> FusedIterator for IntoIter<A> {}
2638
2639#[unstable(feature = "trusted_len", issue = "37572")]
2640unsafe impl<A> TrustedLen for IntoIter<A> {}
2641
2642/// The iterator produced by [`Option::into_flat_iter`]. See its documentation for more.
2643#[derive(Clone, Debug)]
2644#[unstable(feature = "option_into_flat_iter", issue = "148441")]
2645pub struct OptionFlatten<A> {
2646    iter: Option<A>,
2647}
2648
2649#[unstable(feature = "option_into_flat_iter", issue = "148441")]
2650impl<A: Iterator> Iterator for OptionFlatten<A> {
2651    type Item = A::Item;
2652
2653    fn next(&mut self) -> Option<Self::Item> {
2654        self.iter.as_mut()?.next()
2655    }
2656
2657    fn size_hint(&self) -> (usize, Option<usize>) {
2658        self.iter.as_ref().map(|i| i.size_hint()).unwrap_or((0, Some(0)))
2659    }
2660}
2661
2662#[unstable(feature = "option_into_flat_iter", issue = "148441")]
2663impl<A: DoubleEndedIterator> DoubleEndedIterator for OptionFlatten<A> {
2664    fn next_back(&mut self) -> Option<Self::Item> {
2665        self.iter.as_mut()?.next_back()
2666    }
2667}
2668
2669#[unstable(feature = "option_into_flat_iter", issue = "148441")]
2670impl<A: ExactSizeIterator> ExactSizeIterator for OptionFlatten<A> {}
2671
2672#[unstable(feature = "option_into_flat_iter", issue = "148441")]
2673impl<A: FusedIterator> FusedIterator for OptionFlatten<A> {}
2674
2675#[unstable(feature = "option_into_flat_iter", issue = "148441")]
2676unsafe impl<A: TrustedLen> TrustedLen for OptionFlatten<A> {}
2677
2678/////////////////////////////////////////////////////////////////////////////
2679// FromIterator
2680/////////////////////////////////////////////////////////////////////////////
2681
2682#[stable(feature = "rust1", since = "1.0.0")]
2683impl<A, V: FromIterator<A>> FromIterator<Option<A>> for Option<V> {
2684    /// Takes each element in the [`Iterator`]: if it is [`None`][Option::None],
2685    /// no further elements are taken, and the [`None`][Option::None] is
2686    /// returned. Should no [`None`][Option::None] occur, a container of type
2687    /// `V` containing the values of each [`Option`] is returned.
2688    ///
2689    /// # Examples
2690    ///
2691    /// Here is an example which increments every integer in a vector.
2692    /// We use the checked variant of `add` that returns `None` when the
2693    /// calculation would result in an overflow.
2694    ///
2695    /// ```
2696    /// let items = vec![0_u16, 1, 2];
2697    ///
2698    /// let res: Option<Vec<u16>> = items
2699    ///     .iter()
2700    ///     .map(|x| x.checked_add(1))
2701    ///     .collect();
2702    ///
2703    /// assert_eq!(res, Some(vec![1, 2, 3]));
2704    /// ```
2705    ///
2706    /// As you can see, this will return the expected, valid items.
2707    ///
2708    /// Here is another example that tries to subtract one from another list
2709    /// of integers, this time checking for underflow:
2710    ///
2711    /// ```
2712    /// let items = vec![2_u16, 1, 0];
2713    ///
2714    /// let res: Option<Vec<u16>> = items
2715    ///     .iter()
2716    ///     .map(|x| x.checked_sub(1))
2717    ///     .collect();
2718    ///
2719    /// assert_eq!(res, None);
2720    /// ```
2721    ///
2722    /// Since the last element is zero, it would underflow. Thus, the resulting
2723    /// value is `None`.
2724    ///
2725    /// Here is a variation on the previous example, showing that no
2726    /// further elements are taken from `iter` after the first `None`.
2727    ///
2728    /// ```
2729    /// let items = vec![3_u16, 2, 1, 10];
2730    ///
2731    /// let mut shared = 0;
2732    ///
2733    /// let res: Option<Vec<u16>> = items
2734    ///     .iter()
2735    ///     .map(|x| { shared += x; x.checked_sub(2) })
2736    ///     .collect();
2737    ///
2738    /// assert_eq!(res, None);
2739    /// assert_eq!(shared, 6);
2740    /// ```
2741    ///
2742    /// Since the third element caused an underflow, no further elements were taken,
2743    /// so the final value of `shared` is 6 (= `3 + 2 + 1`), not 16.
2744    #[inline]
2745    fn from_iter<I: IntoIterator<Item = Option<A>>>(iter: I) -> Option<V> {
2746        // FIXME(#11084): This could be replaced with Iterator::scan when this
2747        // performance bug is closed.
2748
2749        iter::try_process(iter.into_iter(), |i| i.collect())
2750    }
2751}
2752
2753#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
2754#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2755impl<T> const ops::Try for Option<T> {
2756    type Output = T;
2757    type Residual = Option<convert::Infallible>;
2758
2759    #[inline]
2760    fn from_output(output: Self::Output) -> Self {
2761        Some(output)
2762    }
2763
2764    #[inline]
2765    fn branch(self) -> ControlFlow<Self::Residual, Self::Output> {
2766        match self {
2767            Some(v) => ControlFlow::Continue(v),
2768            None => ControlFlow::Break(None),
2769        }
2770    }
2771}
2772
2773#[unstable(feature = "try_trait_v2", issue = "84277", old_name = "try_trait")]
2774#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2775// Note: manually specifying the residual type instead of using the default to work around
2776// https://github.com/rust-lang/rust/issues/99940
2777impl<T> const ops::FromResidual<Option<convert::Infallible>> for Option<T> {
2778    #[inline]
2779    fn from_residual(residual: Option<convert::Infallible>) -> Self {
2780        match residual {
2781            None => None,
2782        }
2783    }
2784}
2785
2786#[diagnostic::do_not_recommend]
2787#[unstable(feature = "try_trait_v2_yeet", issue = "96374")]
2788#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2789impl<T> const ops::FromResidual<ops::Yeet<()>> for Option<T> {
2790    #[inline]
2791    fn from_residual(ops::Yeet(()): ops::Yeet<()>) -> Self {
2792        None
2793    }
2794}
2795
2796#[unstable(feature = "try_trait_v2_residual", issue = "91285")]
2797#[rustc_const_unstable(feature = "const_try", issue = "74935")]
2798impl<T> const ops::Residual<T> for Option<convert::Infallible> {
2799    type TryType = Option<T>;
2800}
2801
2802impl<T> Option<Option<T>> {
2803    /// Converts from `Option<Option<T>>` to `Option<T>`.
2804    ///
2805    /// # Examples
2806    ///
2807    /// Basic usage:
2808    ///
2809    /// ```
2810    /// let x: Option<Option<u32>> = Some(Some(6));
2811    /// assert_eq!(Some(6), x.flatten());
2812    ///
2813    /// let x: Option<Option<u32>> = Some(None);
2814    /// assert_eq!(None, x.flatten());
2815    ///
2816    /// let x: Option<Option<u32>> = None;
2817    /// assert_eq!(None, x.flatten());
2818    /// ```
2819    ///
2820    /// Flattening only removes one level of nesting at a time:
2821    ///
2822    /// ```
2823    /// let x: Option<Option<Option<u32>>> = Some(Some(Some(6)));
2824    /// assert_eq!(Some(Some(6)), x.flatten());
2825    /// assert_eq!(Some(6), x.flatten().flatten());
2826    /// ```
2827    #[inline]
2828    #[stable(feature = "option_flattening", since = "1.40.0")]
2829    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
2830    #[rustc_const_stable(feature = "const_option", since = "1.83.0")]
2831    pub const fn flatten(self) -> Option<T> {
2832        // FIXME(const-hack): could be written with `and_then`
2833        match self {
2834            Some(inner) => inner,
2835            None => None,
2836        }
2837    }
2838}
2839
2840impl<'a, T> Option<&'a Option<T>> {
2841    /// Converts from `Option<&Option<T>>` to `Option<&T>`.
2842    ///
2843    /// # Examples
2844    ///
2845    /// Basic usage:
2846    ///
2847    /// ```
2848    /// #![feature(option_reference_flattening)]
2849    ///
2850    /// let x: Option<&Option<u32>> = Some(&Some(6));
2851    /// assert_eq!(Some(&6), x.flatten_ref());
2852    ///
2853    /// let x: Option<&Option<u32>> = Some(&None);
2854    /// assert_eq!(None, x.flatten_ref());
2855    ///
2856    /// let x: Option<&Option<u32>> = None;
2857    /// assert_eq!(None, x.flatten_ref());
2858    /// ```
2859    #[inline]
2860    #[unstable(feature = "option_reference_flattening", issue = "149221")]
2861    pub const fn flatten_ref(self) -> Option<&'a T> {
2862        match self {
2863            Some(inner) => inner.as_ref(),
2864            None => None,
2865        }
2866    }
2867}
2868
2869impl<'a, T> Option<&'a mut Option<T>> {
2870    /// Converts from `Option<&mut Option<T>>` to `&Option<T>`.
2871    ///
2872    /// # Examples
2873    ///
2874    /// Basic usage:
2875    ///
2876    /// ```
2877    /// #![feature(option_reference_flattening)]
2878    ///
2879    /// let y = &mut Some(6);
2880    /// let x: Option<&mut Option<u32>> = Some(y);
2881    /// assert_eq!(Some(&6), x.flatten_ref());
2882    ///
2883    /// let y: &mut Option<u32> = &mut None;
2884    /// let x: Option<&mut Option<u32>> = Some(y);
2885    /// assert_eq!(None, x.flatten_ref());
2886    ///
2887    /// let x: Option<&mut Option<u32>> = None;
2888    /// assert_eq!(None, x.flatten_ref());
2889    /// ```
2890    #[inline]
2891    #[unstable(feature = "option_reference_flattening", issue = "149221")]
2892    pub const fn flatten_ref(self) -> Option<&'a T> {
2893        match self {
2894            Some(inner) => inner.as_ref(),
2895            None => None,
2896        }
2897    }
2898
2899    /// Converts from `Option<&mut Option<T>>` to `Option<&mut T>`.
2900    ///
2901    /// # Examples
2902    ///
2903    /// Basic usage:
2904    ///
2905    /// ```
2906    /// #![feature(option_reference_flattening)]
2907    ///
2908    /// let y: &mut Option<u32> = &mut Some(6);
2909    /// let x: Option<&mut Option<u32>> = Some(y);
2910    /// assert_eq!(Some(&mut 6), x.flatten_mut());
2911    ///
2912    /// let y: &mut Option<u32> = &mut None;
2913    /// let x: Option<&mut Option<u32>> = Some(y);
2914    /// assert_eq!(None, x.flatten_mut());
2915    ///
2916    /// let x: Option<&mut Option<u32>> = None;
2917    /// assert_eq!(None, x.flatten_mut());
2918    /// ```
2919    #[inline]
2920    #[unstable(feature = "option_reference_flattening", issue = "149221")]
2921    pub const fn flatten_mut(self) -> Option<&'a mut T> {
2922        match self {
2923            Some(inner) => inner.as_mut(),
2924            None => None,
2925        }
2926    }
2927}
2928
2929impl<T, const N: usize> [Option<T>; N] {
2930    /// Transposes a `[Option<T>; N]` into a `Option<[T; N]>`.
2931    ///
2932    /// # Examples
2933    ///
2934    /// ```
2935    /// #![feature(option_array_transpose)]
2936    /// # use std::option::Option;
2937    ///
2938    /// let data = [Some(0); 1000];
2939    /// let data: Option<[u8; 1000]> = data.transpose();
2940    /// assert_eq!(data, Some([0; 1000]));
2941    ///
2942    /// let data = [Some(0), None];
2943    /// let data: Option<[u8; 2]> = data.transpose();
2944    /// assert_eq!(data, None);
2945    /// ```
2946    #[inline]
2947    #[unstable(feature = "option_array_transpose", issue = "130828")]
2948    pub fn transpose(self) -> Option<[T; N]> {
2949        self.try_map(core::convert::identity)
2950    }
2951}
````