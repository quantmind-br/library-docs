---
title: mod.rs - source
url: https://doc.rust-lang.org/stable/src/std/collections/mod.rs.html#1-459
source: crawler
fetched_at: 2026-05-06T21:26:32.797360456-03:00
rendered_js: false
word_count: 2912
summary: This document provides an overview of the Rust standard library's collection types, offering guidance on choosing the appropriate data structure based on specific use cases and performance characteristics.
tags:
    - rust
    - collections
    - data-structures
    - performance
    - memory-management
category: concept
---

## std/collections/ mod.rs

````rust
1//! Collection types.
2//!
3//! Rust's standard collection library provides efficient implementations of the
4//! most common general purpose programming data structures. By using the
5//! standard implementations, it should be possible for two libraries to
6//! communicate without significant data conversion.
7//!
8//! To get this out of the way: you should probably just use [`Vec`] or [`HashMap`].
9//! These two collections cover most use cases for generic data storage and
10//! processing. They are exceptionally good at doing what they do. All the other
11//! collections in the standard library have specific use cases where they are
12//! the optimal choice, but these cases are borderline *niche* in comparison.
13//! Even when `Vec` and `HashMap` are technically suboptimal, they're probably a
14//! good enough choice to get started.
15//!
16//! Rust's collections can be grouped into four major categories:
17//!
18//! * Sequences: [`Vec`], [`VecDeque`], [`LinkedList`]
19//! * Maps: [`HashMap`], [`BTreeMap`]
20//! * Sets: [`HashSet`], [`BTreeSet`]
21//! * Misc: [`BinaryHeap`]
22//!
23//! # When Should You Use Which Collection?
24//!
25//! These are fairly high-level and quick break-downs of when each collection
26//! should be considered. Detailed discussions of strengths and weaknesses of
27//! individual collections can be found on their own documentation pages.
28//!
29//! ### Use a [`Vec`] when:
30//! * You want to collect items up to be processed or sent elsewhere later, and
31//!   don't care about any properties of the actual values being stored.
32//! * You want a sequence of elements in a particular order, and will only be
33//!   appending to (or near) the end.
34//! * You want a stack.
35//! * You want a resizable array.
36//! * You want a heap-allocated array.
37//!
38//! ### Use a [`VecDeque`] when:
39//! * You want a [`Vec`] that supports efficient insertion at both ends of the
40//!   sequence.
41//! * You want a queue.
42//! * You want a double-ended queue (deque).
43//!
44//! ### Use a [`LinkedList`] when:
45//! * You want a [`Vec`] or [`VecDeque`] of unknown size, and can't tolerate
46//!   amortization.
47//! * You want to efficiently split and append lists.
48//! * You are *absolutely* certain you *really*, *truly*, want a doubly linked
49//!   list.
50//!
51//! ### Use a [`HashMap`] when:
52//! * You want to associate arbitrary keys with an arbitrary value.
53//! * You want a cache.
54//! * You want a map, with no extra functionality.
55//!
56//! ### Use a [`BTreeMap`] when:
57//! * You want a map sorted by its keys.
58//! * You want to be able to get a range of entries on-demand.
59//! * You're interested in what the smallest or largest key-value pair is.
60//! * You want to find the largest or smallest key that is smaller or larger
61//!   than something.
62//!
63//! ### Use the `Set` variant of any of these `Map`s when:
64//! * You just want to remember which keys you've seen.
65//! * There is no meaningful value to associate with your keys.
66//! * You just want a set.
67//!
68//! ### Use a [`BinaryHeap`] when:
69//!
70//! * You want to store a bunch of elements, but only ever want to process the
71//!   "biggest" or "most important" one at any given time.
72//! * You want a priority queue.
73//!
74//! # Performance
75//!
76//! Choosing the right collection for the job requires an understanding of what
77//! each collection is good at. Here we briefly summarize the performance of
78//! different collections for certain important operations. For further details,
79//! see each type's documentation, and note that the names of actual methods may
80//! differ from the tables below on certain collections.
81//!
82//! Throughout the documentation, we will adhere to the following conventions
83//! for operation notation:
84//!
85//! * The collection's size is denoted by `n`.
86//! * If a second collection is involved, its size is denoted by `m`.
87//! * Item indices are denoted by `i`.
88//! * Operations which have an *amortized* cost are suffixed with a `*`.
89//! * Operations with an *expected* cost are suffixed with a `~`.
90//!
91//! Calling operations that add to a collection will occasionally require a
92//! collection to be resized - an extra operation that takes *O*(*n*) time.
93//!
94//! *Amortized* costs are calculated to account for the time cost of such resize
95//! operations *over a sufficiently large series of operations*. An individual
96//! operation may be slower or faster due to the sporadic nature of collection
97//! resizing, however the average cost per operation will approach the amortized
98//! cost.
99//!
100//! Rust's collections never automatically shrink, so removal operations aren't
101//! amortized.
102//!
103//! [`HashMap`] uses *expected* costs. It is theoretically possible, though very
104//! unlikely, for [`HashMap`] to experience significantly worse performance than
105//! the expected cost. This is due to the probabilistic nature of hashing - i.e.
106//! it is possible to generate a duplicate hash given some input key that will
107//! require extra computation to correct.
108//!
109//! ## Cost of Collection Operations
110//!
111//!
112//! |                | get(i)                 | insert(i)               | remove(i)              | append(Vec(m))    | split_off(i)           | range           | append       |
113//! |----------------|------------------------|-------------------------|------------------------|-------------------|------------------------|-----------------|--------------|
114//! | [`Vec`]        | *O*(1)                 | *O*(*n*-*i*)*           | *O*(*n*-*i*)           | *O*(*m*)*         | *O*(*n*-*i*)           | N/A             | N/A          |
115//! | [`VecDeque`]   | *O*(1)                 | *O*(min(*i*, *n*-*i*))* | *O*(min(*i*, *n*-*i*)) | *O*(*m*)*         | *O*(min(*i*, *n*-*i*)) | N/A             | N/A          |
116//! | [`LinkedList`] | *O*(min(*i*, *n*-*i*)) | *O*(min(*i*, *n*-*i*))  | *O*(min(*i*, *n*-*i*)) | *O*(1)            | *O*(min(*i*, *n*-*i*)) | N/A             | N/A          |
117//! | [`HashMap`]    | *O*(1)~                | *O*(1)~*                | *O*(1)~                | N/A               | N/A                    | N/A             | N/A          |
118//! | [`BTreeMap`]   | *O*(log(*n*))          | *O*(log(*n*))           | *O*(log(*n*))          | N/A               | N/A                    | *O*(log(*n*))   | *O*(*n*+*m*) |
119//!
120//! Note that where ties occur, [`Vec`] is generally going to be faster than
121//! [`VecDeque`], and [`VecDeque`] is generally going to be faster than
122//! [`LinkedList`].
123//!
124//! For Sets, all operations have the cost of the equivalent Map operation.
125//!
126//! # Correct and Efficient Usage of Collections
127//!
128//! Of course, knowing which collection is the right one for the job doesn't
129//! instantly permit you to use it correctly. Here are some quick tips for
130//! efficient and correct usage of the standard collections in general. If
131//! you're interested in how to use a specific collection in particular, consult
132//! its documentation for detailed discussion and code examples.
133//!
134//! ## Capacity Management
135//!
136//! Many collections provide several constructors and methods that refer to
137//! "capacity". These collections are generally built on top of an array.
138//! Optimally, this array would be exactly the right size to fit only the
139//! elements stored in the collection, but for the collection to do this would
140//! be very inefficient. If the backing array was exactly the right size at all
141//! times, then every time an element is inserted, the collection would have to
142//! grow the array to fit it. Due to the way memory is allocated and managed on
143//! most computers, this would almost surely require allocating an entirely new
144//! array and copying every single element from the old one into the new one.
145//! Hopefully you can see that this wouldn't be very efficient to do on every
146//! operation.
147//!
148//! Most collections therefore use an *amortized* allocation strategy. They
149//! generally let themselves have a fair amount of unoccupied space so that they
150//! only have to grow on occasion. When they do grow, they allocate a
151//! substantially larger array to move the elements into so that it will take a
152//! while for another grow to be required. While this strategy is great in
153//! general, it would be even better if the collection *never* had to resize its
154//! backing array. Unfortunately, the collection itself doesn't have enough
155//! information to do this itself. Therefore, it is up to us programmers to give
156//! it hints.
157//!
158//! Any `with_capacity` constructor will instruct the collection to allocate
159//! enough space for the specified number of elements. Ideally this will be for
160//! exactly that many elements, but some implementation details may prevent
161//! this. See collection-specific documentation for details. In general, use
162//! `with_capacity` when you know exactly how many elements will be inserted, or
163//! at least have a reasonable upper-bound on that number.
164//!
165//! When anticipating a large influx of elements, the `reserve` family of
166//! methods can be used to hint to the collection how much room it should make
167//! for the coming items. As with `with_capacity`, the precise behavior of
168//! these methods will be specific to the collection of interest.
169//!
170//! For optimal performance, collections will generally avoid shrinking
171//! themselves. If you believe that a collection will not soon contain any more
172//! elements, or just really need the memory, the `shrink_to_fit` method prompts
173//! the collection to shrink the backing array to the minimum size capable of
174//! holding its elements.
175//!
176//! Finally, if ever you're interested in what the actual capacity of the
177//! collection is, most collections provide a `capacity` method to query this
178//! information on demand. This can be useful for debugging purposes, or for
179//! use with the `reserve` methods.
180//!
181//! ## Iterators
182//!
183//! [Iterators][crate::iter]
184//! are a powerful and robust mechanism used throughout Rust's
185//! standard libraries. Iterators provide a sequence of values in a generic,
186//! safe, efficient and convenient way. The contents of an iterator are usually
187//! *lazily* evaluated, so that only the values that are actually needed are
188//! ever actually produced, and no allocation need be done to temporarily store
189//! them. Iterators are primarily consumed using a `for` loop, although many
190//! functions also take iterators where a collection or sequence of values is
191//! desired.
192//!
193//! All of the standard collections provide several iterators for performing
194//! bulk manipulation of their contents. The three primary iterators almost
195//! every collection should provide are `iter`, `iter_mut`, and `into_iter`.
196//! Some of these are not provided on collections where it would be unsound or
197//! unreasonable to provide them.
198//!
199//! `iter` provides an iterator of immutable references to all the contents of a
200//! collection in the most "natural" order. For sequence collections like [`Vec`],
201//! this means the items will be yielded in increasing order of index starting
202//! at 0. For ordered collections like [`BTreeMap`], this means that the items
203//! will be yielded in sorted order. For unordered collections like [`HashMap`],
204//! the items will be yielded in whatever order the internal representation made
205//! most convenient. This is great for reading through all the contents of the
206//! collection.
207//!
208//! ```
209//! let vec = vec![1, 2, 3, 4];
210//! for x in vec.iter() {
211//!    println!("vec contained {x:?}");
212//! }
213//! ```
214//!
215//! `iter_mut` provides an iterator of *mutable* references in the same order as
216//! `iter`. This is great for mutating all the contents of the collection.
217//!
218//! ```
219//! let mut vec = vec![1, 2, 3, 4];
220//! for x in vec.iter_mut() {
221//!    *x += 1;
222//! }
223//! ```
224//!
225//! `into_iter` transforms the actual collection into an iterator over its
226//! contents by-value. This is great when the collection itself is no longer
227//! needed, and the values are needed elsewhere. Using `extend` with `into_iter`
228//! is the main way that contents of one collection are moved into another.
229//! `extend` automatically calls `into_iter`, and takes any <code>T: [IntoIterator]</code>.
230//! Calling `collect` on an iterator itself is also a great way to convert one
231//! collection into another. Both of these methods should internally use the
232//! capacity management tools discussed in the previous section to do this as
233//! efficiently as possible.
234//!
235//! ```
236//! let mut vec1 = vec![1, 2, 3, 4];
237//! let vec2 = vec![10, 20, 30, 40];
238//! vec1.extend(vec2);
239//! ```
240//!
241//! ```
242//! use std::collections::VecDeque;
243//!
244//! let vec = [1, 2, 3, 4];
245//! let buf: VecDeque<_> = vec.into_iter().collect();
246//! ```
247//!
248//! Iterators also provide a series of *adapter* methods for performing common
249//! threads to sequences. Among the adapters are functional favorites like `map`,
250//! `fold`, `skip` and `take`. Of particular interest to collections is the
251//! `rev` adapter, which reverses any iterator that supports this operation. Most
252//! collections provide reversible iterators as the way to iterate over them in
253//! reverse order.
254//!
255//! ```
256//! let vec = vec![1, 2, 3, 4];
257//! for x in vec.iter().rev() {
258//!    println!("vec contained {x:?}");
259//! }
260//! ```
261//!
262//! Several other collection methods also return iterators to yield a sequence
263//! of results but avoid allocating an entire collection to store the result in.
264//! This provides maximum flexibility as
265//! [`collect`][crate::iter::Iterator::collect] or
266//! [`extend`][crate::iter::Extend::extend] can be called to
267//! "pipe" the sequence into any collection if desired. Otherwise, the sequence
268//! can be looped over with a `for` loop. The iterator can also be discarded
269//! after partial use, preventing the computation of the unused items.
270//!
271//! ## Entries
272//!
273//! The `entry` API is intended to provide an efficient mechanism for
274//! manipulating the contents of a map conditionally on the presence of a key or
275//! not. The primary motivating use case for this is to provide efficient
276//! accumulator maps. For instance, if one wishes to maintain a count of the
277//! number of times each key has been seen, they will have to perform some
278//! conditional logic on whether this is the first time the key has been seen or
279//! not. Normally, this would require a `find` followed by an `insert`,
280//! effectively duplicating the search effort on each insertion.
281//!
282//! When a user calls `map.entry(key)`, the map will search for the key and
283//! then yield a variant of the `Entry` enum.
284//!
285//! If a `Vacant(entry)` is yielded, then the key *was not* found. In this case
286//! the only valid operation is to `insert` a value into the entry. When this is
287//! done, the vacant entry is consumed and converted into a mutable reference to
288//! the value that was inserted. This allows for further manipulation of the
289//! value beyond the lifetime of the search itself. This is useful if complex
290//! logic needs to be performed on the value regardless of whether the value was
291//! just inserted.
292//!
293//! If an `Occupied(entry)` is yielded, then the key *was* found. In this case,
294//! the user has several options: they can `get`, `insert` or `remove` the
295//! value of the occupied entry. Additionally, they can convert the occupied
296//! entry into a mutable reference to its value, providing symmetry to the
297//! vacant `insert` case.
298//!
299//! ### Examples
300//!
301//! Here are the two primary ways in which `entry` is used. First, a simple
302//! example where the logic performed on the values is trivial.
303//!
304//! #### Counting the number of times each character in a string occurs
305//!
306//! ```
307//! use std::collections::btree_map::BTreeMap;
308//!
309//! let mut count = BTreeMap::new();
310//! let message = "she sells sea shells by the sea shore";
311//!
312//! for c in message.chars() {
313//!     *count.entry(c).or_insert(0) += 1;
314//! }
315//!
316//! assert_eq!(count.get(&'s'), Some(&8));
317//!
318//! println!("Number of occurrences of each character");
319//! for (char, count) in &count {
320//!     println!("{char}: {count}");
321//! }
322//! ```
323//!
324//! When the logic to be performed on the value is more complex, we may simply
325//! use the `entry` API to ensure that the value is initialized and perform the
326//! logic afterwards.
327//!
328//! #### Tracking the inebriation of customers at a bar
329//!
330//! ```
331//! use std::collections::btree_map::BTreeMap;
332//!
333//! // A client of the bar. They have a blood alcohol level.
334//! struct Person { blood_alcohol: f32 }
335//!
336//! // All the orders made to the bar, by client ID.
337//! let orders = vec![1, 2, 1, 2, 3, 4, 1, 2, 2, 3, 4, 1, 1, 1];
338//!
339//! // Our clients.
340//! let mut blood_alcohol = BTreeMap::new();
341//!
342//! for id in orders {
343//!     // If this is the first time we've seen this customer, initialize them
344//!     // with no blood alcohol. Otherwise, just retrieve them.
345//!     let person = blood_alcohol.entry(id).or_insert(Person { blood_alcohol: 0.0 });
346//!
347//!     // Reduce their blood alcohol level. It takes time to order and drink a beer!
348//!     person.blood_alcohol *= 0.9;
349//!
350//!     // Check if they're sober enough to have another beer.
351//!     if person.blood_alcohol > 0.3 {
352//!         // Too drunk... for now.
353//!         println!("Sorry {id}, I have to cut you off");
354//!     } else {
355//!         // Have another!
356//!         person.blood_alcohol += 0.1;
357//!     }
358//! }
359//! ```
360//!
361//! # Insert and complex keys
362//!
363//! If we have a more complex key, calls to `insert` will
364//! not update the value of the key. For example:
365//!
366//! ```
367//! use std::cmp::Ordering;
368//! use std::collections::BTreeMap;
369//! use std::hash::{Hash, Hasher};
370//!
371//! #[derive(Debug)]
372//! struct Foo {
373//!     a: u32,
374//!     b: &'static str,
375//! }
376//!
377//! // we will compare `Foo`s by their `a` value only.
378//! impl PartialEq for Foo {
379//!     fn eq(&self, other: &Self) -> bool { self.a == other.a }
380//! }
381//!
382//! impl Eq for Foo {}
383//!
384//! // we will hash `Foo`s by their `a` value only.
385//! impl Hash for Foo {
386//!     fn hash<H: Hasher>(&self, h: &mut H) { self.a.hash(h); }
387//! }
388//!
389//! impl PartialOrd for Foo {
390//!     fn partial_cmp(&self, other: &Self) -> Option<Ordering> { self.a.partial_cmp(&other.a) }
391//! }
392//!
393//! impl Ord for Foo {
394//!     fn cmp(&self, other: &Self) -> Ordering { self.a.cmp(&other.a) }
395//! }
396//!
397//! let mut map = BTreeMap::new();
398//! map.insert(Foo { a: 1, b: "baz" }, 99);
399//!
400//! // We already have a Foo with an a of 1, so this will be updating the value.
401//! map.insert(Foo { a: 1, b: "xyz" }, 100);
402//!
403//! // The value has been updated...
404//! assert_eq!(map.values().next().unwrap(), &100);
405//!
406//! // ...but the key hasn't changed. b is still "baz", not "xyz".
407//! assert_eq!(map.keys().next().unwrap().b, "baz");
408//! ```
409
410#![stable(feature = "rust1", since = "1.0.0")]
411
412#[stable(feature = "try_reserve", since = "1.57.0")]
413pub use alloc_crate::collections::TryReserveError;
414#[unstable(
415    feature = "try_reserve_kind",
416    reason = "Uncertain how much info should be exposed",
417    issue = "48043"
418)]
419pub use alloc_crate::collections::TryReserveErrorKind;
420#[stable(feature = "rust1", since = "1.0.0")]
421pub use alloc_crate::collections::{BTreeMap, BTreeSet, BinaryHeap};
422#[stable(feature = "rust1", since = "1.0.0")]
423pub use alloc_crate::collections::{LinkedList, VecDeque};
424#[stable(feature = "rust1", since = "1.0.0")]
425pub use alloc_crate::collections::{binary_heap, btree_map, btree_set};
426#[stable(feature = "rust1", since = "1.0.0")]
427pub use alloc_crate::collections::{linked_list, vec_deque};
428
429#[stable(feature = "rust1", since = "1.0.0")]
430#[doc(inline)]
431pub use self::hash_map::HashMap;
432#[stable(feature = "rust1", since = "1.0.0")]
433#[doc(inline)]
434pub use self::hash_set::HashSet;
435#[stable(feature = "rust1", since = "1.0.0")]
436// FIXME(#82080) The deprecation here is only theoretical, and does not actually produce a warning.
437#[deprecated(note = "moved to `std::ops::Bound`", since = "1.26.0")]
438#[doc(hidden)]
439pub use crate::ops::Bound;
440
441mod hash;
442
443#[stable(feature = "rust1", since = "1.0.0")]
444pub mod hash_map {
445    //! A hash map implemented with quadratic probing and SIMD lookup.
446    #[stable(feature = "rust1", since = "1.0.0")]
447    pub use super::hash::map::*;
448    #[stable(feature = "hashmap_build_hasher", since = "1.7.0")]
449    pub use crate::hash::random::DefaultHasher;
450    #[stable(feature = "hashmap_build_hasher", since = "1.7.0")]
451    pub use crate::hash::random::RandomState;
452}
453
454#[stable(feature = "rust1", since = "1.0.0")]
455pub mod hash_set {
456    //! A hash set implemented as a `HashMap` where the value is `()`.
457    #[stable(feature = "rust1", since = "1.0.0")]
458    pub use super::hash::set::*;
459}
````