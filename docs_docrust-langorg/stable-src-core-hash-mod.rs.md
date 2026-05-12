---
title: mod.rs - source
url: https://doc.rust-lang.org/stable/src/core/hash/mod.rs.html#234-236
source: crawler
fetched_at: 2026-05-06T21:26:05.985567162-03:00
rendered_js: false
word_count: 4006
summary: This document defines the Hash trait in Rust, providing a standard interface for types to be hashed for use in collections like HashMap and HashSet.
tags:
    - rust
    - hash
    - trait
    - hashing
    - data-structures
    - generic-programming
category: reference
---

## core/hash/ mod.rs

````rust
1//! Generic hashing support.
2//!
3//! This module provides a generic way to compute the [hash] of a value.
4//! Hashes are most commonly used with [`HashMap`] and [`HashSet`].
5//!
6//! [hash]: https://en.wikipedia.org/wiki/Hash_function
7//! [`HashMap`]: ../../std/collections/struct.HashMap.html
8//! [`HashSet`]: ../../std/collections/struct.HashSet.html
9//!
10//! The simplest way to make a type hashable is to use `#[derive(Hash)]`:
11//!
12//! # Examples
13//!
14//! ```rust
15//! use std::hash::{DefaultHasher, Hash, Hasher};
16//!
17//! #[derive(Hash)]
18//! struct Person {
19//!     id: u32,
20//!     name: String,
21//!     phone: u64,
22//! }
23//!
24//! let person1 = Person {
25//!     id: 5,
26//!     name: "Janet".to_string(),
27//!     phone: 555_666_7777,
28//! };
29//! let person2 = Person {
30//!     id: 5,
31//!     name: "Bob".to_string(),
32//!     phone: 555_666_7777,
33//! };
34//!
35//! assert!(calculate_hash(&person1) != calculate_hash(&person2));
36//!
37//! fn calculate_hash<T: Hash>(t: &T) -> u64 {
38//!     let mut s = DefaultHasher::new();
39//!     t.hash(&mut s);
40//!     s.finish()
41//! }
42//! ```
43//!
44//! If you need more control over how a value is hashed, you need to implement
45//! the [`Hash`] trait:
46//!
47//! ```rust
48//! use std::hash::{DefaultHasher, Hash, Hasher};
49//!
50//! struct Person {
51//!     id: u32,
52//!     # #[allow(dead_code)]
53//!     name: String,
54//!     phone: u64,
55//! }
56//!
57//! impl Hash for Person {
58//!     fn hash<H: Hasher>(&self, state: &mut H) {
59//!         self.id.hash(state);
60//!         self.phone.hash(state);
61//!     }
62//! }
63//!
64//! let person1 = Person {
65//!     id: 5,
66//!     name: "Janet".to_string(),
67//!     phone: 555_666_7777,
68//! };
69//! let person2 = Person {
70//!     id: 5,
71//!     name: "Bob".to_string(),
72//!     phone: 555_666_7777,
73//! };
74//!
75//! assert_eq!(calculate_hash(&person1), calculate_hash(&person2));
76//!
77//! fn calculate_hash<T: Hash>(t: &T) -> u64 {
78//!     let mut s = DefaultHasher::new();
79//!     t.hash(&mut s);
80//!     s.finish()
81//! }
82//! ```
83
84#![stable(feature = "rust1", since = "1.0.0")]
85
86#[stable(feature = "rust1", since = "1.0.0")]
87#[allow(deprecated)]
88pub use self::sip::SipHasher;
89#[unstable(feature = "hashmap_internals", issue = "none")]
90#[doc(hidden)]
91pub use self::sip::SipHasher13;
92use crate::{fmt, marker};
93
94mod sip;
95
96/// A hashable type.
97///
98/// Types implementing `Hash` are able to be [`hash`]ed with an instance of
99/// [`Hasher`].
100///
101/// ## Implementing `Hash`
102///
103/// You can derive `Hash` with `#[derive(Hash)]` if all fields implement `Hash`.
104/// The resulting hash will be the combination of the values from calling
105/// [`hash`] on each field.
106///
107/// ```
108/// #[derive(Hash)]
109/// struct Rustacean {
110///     name: String,
111///     country: String,
112/// }
113/// ```
114///
115/// If you need more control over how a value is hashed, you can of course
116/// implement the `Hash` trait yourself:
117///
118/// ```
119/// use std::hash::{Hash, Hasher};
120///
121/// struct Person {
122///     id: u32,
123///     name: String,
124///     phone: u64,
125/// }
126///
127/// impl Hash for Person {
128///     fn hash<H: Hasher>(&self, state: &mut H) {
129///         self.id.hash(state);
130///         self.phone.hash(state);
131///     }
132/// }
133/// ```
134///
135/// ## `Hash` and `Eq`
136///
137/// When implementing both `Hash` and [`Eq`], it is important that the following
138/// property holds:
139///
140/// ```text
141/// k1 == k2 -> hash(k1) == hash(k2)
142/// ```
143///
144/// In other words, if two keys are equal, their hashes must also be equal.
145/// [`HashMap`] and [`HashSet`] both rely on this behavior.
146///
147/// Thankfully, you won't need to worry about upholding this property when
148/// deriving both [`Eq`] and `Hash` with `#[derive(PartialEq, Eq, Hash)]`.
149///
150/// Violating this property is a logic error. The behavior resulting from a logic error is not
151/// specified, but users of the trait must ensure that such logic errors do *not* result in
152/// undefined behavior. This means that `unsafe` code **must not** rely on the correctness of these
153/// methods.
154///
155/// ## Prefix collisions
156///
157/// Implementations of `hash` should ensure that the data they
158/// pass to the `Hasher` are prefix-free. That is,
159/// values which are not equal should cause two different sequences of values to be written,
160/// and neither of the two sequences should be a prefix of the other.
161///
162/// For example, the standard implementation of [`Hash` for `&str`][impl] passes an extra
163/// `0xFF` byte to the `Hasher` so that the values `("ab", "c")` and `("a",
164/// "bc")` hash differently.
165///
166/// ## Portability
167///
168/// Due to differences in endianness and type sizes, data fed by `Hash` to a `Hasher`
169/// should not be considered portable across platforms. Additionally the data passed by most
170/// standard library types should not be considered stable between compiler versions.
171///
172/// This means tests shouldn't probe hard-coded hash values or data fed to a `Hasher` and
173/// instead should check consistency with `Eq`.
174///
175/// Serialization formats intended to be portable between platforms or compiler versions should
176/// either avoid encoding hashes or only rely on `Hash` and `Hasher` implementations that
177/// provide additional guarantees.
178///
179/// [`HashMap`]: ../../std/collections/struct.HashMap.html
180/// [`HashSet`]: ../../std/collections/struct.HashSet.html
181/// [`hash`]: Hash::hash
182/// [impl]: ../../std/primitive.str.html#impl-Hash-for-str
183#[stable(feature = "rust1", since = "1.0.0")]
184#[rustc_diagnostic_item = "Hash"]
185pub trait Hash: marker::PointeeSized {
186    /// Feeds this value into the given [`Hasher`].
187    ///
188    /// # Examples
189    ///
190    /// ```
191    /// use std::hash::{DefaultHasher, Hash, Hasher};
192    ///
193    /// let mut hasher = DefaultHasher::new();
194    /// 7920.hash(&mut hasher);
195    /// println!("Hash is {:x}!", hasher.finish());
196    /// ```
197    #[stable(feature = "rust1", since = "1.0.0")]
198    fn hash<H: Hasher>(&self, state: &mut H);
199
200    /// Feeds a slice of this type into the given [`Hasher`].
201    ///
202    /// This method is meant as a convenience, but its implementation is
203    /// also explicitly left unspecified. It isn't guaranteed to be
204    /// equivalent to repeated calls of [`hash`] and implementations of
205    /// [`Hash`] should keep that in mind and call [`hash`] themselves
206    /// if the slice isn't treated as a whole unit in the [`PartialEq`]
207    /// implementation.
208    ///
209    /// For example, a [`VecDeque`] implementation might naïvely call
210    /// [`as_slices`] and then [`hash_slice`] on each slice, but this
211    /// is wrong since the two slices can change with a call to
212    /// [`make_contiguous`] without affecting the [`PartialEq`]
213    /// result. Since these slices aren't treated as singular
214    /// units, and instead part of a larger deque, this method cannot
215    /// be used.
216    ///
217    /// # Examples
218    ///
219    /// ```
220    /// use std::hash::{DefaultHasher, Hash, Hasher};
221    ///
222    /// let mut hasher = DefaultHasher::new();
223    /// let numbers = [6, 28, 496, 8128];
224    /// Hash::hash_slice(&numbers, &mut hasher);
225    /// println!("Hash is {:x}!", hasher.finish());
226    /// ```
227    ///
228    /// [`VecDeque`]: ../../std/collections/struct.VecDeque.html
229    /// [`as_slices`]: ../../std/collections/struct.VecDeque.html#method.as_slices
230    /// [`make_contiguous`]: ../../std/collections/struct.VecDeque.html#method.make_contiguous
231    /// [`hash`]: Hash::hash
232    /// [`hash_slice`]: Hash::hash_slice
233    #[stable(feature = "hash_slice", since = "1.3.0")]
234    fn hash_slice<H: Hasher>(data: &[Self], state: &mut H)
235    where
236        Self: Sized,
237    {
238        for piece in data {
239            piece.hash(state)
240        }
241    }
242}
243
244// Separate module to reexport the macro `Hash` from prelude without the trait `Hash`.
245pub(crate) mod macros {
246    /// Derive macro generating an impl of the trait `Hash`.
247    #[rustc_builtin_macro]
248    #[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
249    #[allow_internal_unstable(core_intrinsics)]
250    pub macro Hash($item:item) {
251        /* compiler built-in */
252    }
253}
254#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
255#[doc(inline)]
256pub use macros::Hash;
257
258/// A trait for hashing an arbitrary stream of bytes.
259///
260/// Instances of `Hasher` usually represent state that is changed while hashing
261/// data.
262///
263/// `Hasher` provides a fairly basic interface for retrieving the generated hash
264/// (with [`finish`]), and writing integers as well as slices of bytes into an
265/// instance (with [`write`] and [`write_u8`] etc.). Most of the time, `Hasher`
266/// instances are used in conjunction with the [`Hash`] trait.
267///
268/// This trait provides no guarantees about how the various `write_*` methods are
269/// defined and implementations of [`Hash`] should not assume that they work one
270/// way or another. You cannot assume, for example, that a [`write_u32`] call is
271/// equivalent to four calls of [`write_u8`].  Nor can you assume that adjacent
272/// `write` calls are merged, so it's possible, for example, that
273/// ```
274/// # fn foo(hasher: &mut impl std::hash::Hasher) {
275/// hasher.write(&[1, 2]);
276/// hasher.write(&[3, 4, 5, 6]);
277/// # }
278/// ```
279/// and
280/// ```
281/// # fn foo(hasher: &mut impl std::hash::Hasher) {
282/// hasher.write(&[1, 2, 3, 4]);
283/// hasher.write(&[5, 6]);
284/// # }
285/// ```
286/// end up producing different hashes.
287///
288/// Thus to produce the same hash value, [`Hash`] implementations must ensure
289/// for equivalent items that exactly the same sequence of calls is made -- the
290/// same methods with the same parameters in the same order.
291///
292/// # Examples
293///
294/// ```
295/// use std::hash::{DefaultHasher, Hasher};
296///
297/// let mut hasher = DefaultHasher::new();
298///
299/// hasher.write_u32(1989);
300/// hasher.write_u8(11);
301/// hasher.write_u8(9);
302/// hasher.write(b"Huh?");
303///
304/// println!("Hash is {:x}!", hasher.finish());
305/// ```
306///
307/// [`finish`]: Hasher::finish
308/// [`write`]: Hasher::write
309/// [`write_u8`]: Hasher::write_u8
310/// [`write_u32`]: Hasher::write_u32
311#[stable(feature = "rust1", since = "1.0.0")]
312pub trait Hasher {
313    /// Returns the hash value for the values written so far.
314    ///
315    /// Despite its name, the method does not reset the hasher’s internal
316    /// state. Additional [`write`]s will continue from the current value.
317    /// If you need to start a fresh hash value, you will have to create
318    /// a new hasher.
319    ///
320    /// # Examples
321    ///
322    /// ```
323    /// use std::hash::{DefaultHasher, Hasher};
324    ///
325    /// let mut hasher = DefaultHasher::new();
326    /// hasher.write(b"Cool!");
327    ///
328    /// println!("Hash is {:x}!", hasher.finish());
329    /// ```
330    ///
331    /// [`write`]: Hasher::write
332    #[stable(feature = "rust1", since = "1.0.0")]
333    #[must_use]
334    fn finish(&self) -> u64;
335
336    /// Writes some data into this `Hasher`.
337    ///
338    /// # Examples
339    ///
340    /// ```
341    /// use std::hash::{DefaultHasher, Hasher};
342    ///
343    /// let mut hasher = DefaultHasher::new();
344    /// let data = [0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef];
345    ///
346    /// hasher.write(&data);
347    ///
348    /// println!("Hash is {:x}!", hasher.finish());
349    /// ```
350    ///
351    /// # Note to Implementers
352    ///
353    /// You generally should not do length-prefixing as part of implementing
354    /// this method.  It's up to the [`Hash`] implementation to call
355    /// [`Hasher::write_length_prefix`] before sequences that need it.
356    #[stable(feature = "rust1", since = "1.0.0")]
357    fn write(&mut self, bytes: &[u8]);
358
359    /// Writes a single `u8` into this hasher.
360    #[inline]
361    #[stable(feature = "hasher_write", since = "1.3.0")]
362    fn write_u8(&mut self, i: u8) {
363        self.write(&[i])
364    }
365    /// Writes a single `u16` into this hasher.
366    #[inline]
367    #[stable(feature = "hasher_write", since = "1.3.0")]
368    fn write_u16(&mut self, i: u16) {
369        self.write(&i.to_ne_bytes())
370    }
371    /// Writes a single `u32` into this hasher.
372    #[inline]
373    #[stable(feature = "hasher_write", since = "1.3.0")]
374    fn write_u32(&mut self, i: u32) {
375        self.write(&i.to_ne_bytes())
376    }
377    /// Writes a single `u64` into this hasher.
378    #[inline]
379    #[stable(feature = "hasher_write", since = "1.3.0")]
380    fn write_u64(&mut self, i: u64) {
381        self.write(&i.to_ne_bytes())
382    }
383    /// Writes a single `u128` into this hasher.
384    #[inline]
385    #[stable(feature = "i128", since = "1.26.0")]
386    fn write_u128(&mut self, i: u128) {
387        self.write(&i.to_ne_bytes())
388    }
389    /// Writes a single `usize` into this hasher.
390    #[inline]
391    #[stable(feature = "hasher_write", since = "1.3.0")]
392    fn write_usize(&mut self, i: usize) {
393        self.write(&i.to_ne_bytes())
394    }
395
396    /// Writes a single `i8` into this hasher.
397    #[inline]
398    #[stable(feature = "hasher_write", since = "1.3.0")]
399    fn write_i8(&mut self, i: i8) {
400        self.write_u8(i as u8)
401    }
402    /// Writes a single `i16` into this hasher.
403    #[inline]
404    #[stable(feature = "hasher_write", since = "1.3.0")]
405    fn write_i16(&mut self, i: i16) {
406        self.write_u16(i as u16)
407    }
408    /// Writes a single `i32` into this hasher.
409    #[inline]
410    #[stable(feature = "hasher_write", since = "1.3.0")]
411    fn write_i32(&mut self, i: i32) {
412        self.write_u32(i as u32)
413    }
414    /// Writes a single `i64` into this hasher.
415    #[inline]
416    #[stable(feature = "hasher_write", since = "1.3.0")]
417    fn write_i64(&mut self, i: i64) {
418        self.write_u64(i as u64)
419    }
420    /// Writes a single `i128` into this hasher.
421    #[inline]
422    #[stable(feature = "i128", since = "1.26.0")]
423    fn write_i128(&mut self, i: i128) {
424        self.write_u128(i as u128)
425    }
426    /// Writes a single `isize` into this hasher.
427    #[inline]
428    #[stable(feature = "hasher_write", since = "1.3.0")]
429    fn write_isize(&mut self, i: isize) {
430        self.write_usize(i as usize)
431    }
432
433    /// Writes a length prefix into this hasher, as part of being prefix-free.
434    ///
435    /// If you're implementing [`Hash`] for a custom collection, call this before
436    /// writing its contents to this `Hasher`.  That way
437    /// `(collection![1, 2, 3], collection![4, 5])` and
438    /// `(collection![1, 2], collection![3, 4, 5])` will provide different
439    /// sequences of values to the `Hasher`
440    ///
441    /// The `impl<T> Hash for [T]` includes a call to this method, so if you're
442    /// hashing a slice (or array or vector) via its `Hash::hash` method,
443    /// you should **not** call this yourself.
444    ///
445    /// This method is only for providing domain separation.  If you want to
446    /// hash a `usize` that represents part of the *data*, then it's important
447    /// that you pass it to [`Hasher::write_usize`] instead of to this method.
448    ///
449    /// # Examples
450    ///
451    /// ```
452    /// #![feature(hasher_prefixfree_extras)]
453    /// # // Stubs to make the `impl` below pass the compiler
454    /// # #![allow(non_local_definitions)]
455    /// # struct MyCollection<T>(Option<T>);
456    /// # impl<T> MyCollection<T> {
457    /// #     fn len(&self) -> usize { todo!() }
458    /// # }
459    /// # impl<'a, T> IntoIterator for &'a MyCollection<T> {
460    /// #     type Item = T;
461    /// #     type IntoIter = std::iter::Empty<T>;
462    /// #     fn into_iter(self) -> Self::IntoIter { todo!() }
463    /// # }
464    ///
465    /// use std::hash::{Hash, Hasher};
466    /// impl<T: Hash> Hash for MyCollection<T> {
467    ///     fn hash<H: Hasher>(&self, state: &mut H) {
468    ///         state.write_length_prefix(self.len());
469    ///         for elt in self {
470    ///             elt.hash(state);
471    ///         }
472    ///     }
473    /// }
474    /// ```
475    ///
476    /// # Note to Implementers
477    ///
478    /// If you've decided that your `Hasher` is willing to be susceptible to
479    /// Hash-DoS attacks, then you might consider skipping hashing some or all
480    /// of the `len` provided in the name of increased performance.
481    #[inline]
482    #[unstable(feature = "hasher_prefixfree_extras", issue = "96762")]
483    fn write_length_prefix(&mut self, len: usize) {
484        self.write_usize(len);
485    }
486
487    /// Writes a single `str` into this hasher.
488    ///
489    /// If you're implementing [`Hash`], you generally do not need to call this,
490    /// as the `impl Hash for str` does, so you should prefer that instead.
491    ///
492    /// This includes the domain separator for prefix-freedom, so you should
493    /// **not** call `Self::write_length_prefix` before calling this.
494    ///
495    /// # Note to Implementers
496    ///
497    /// There are at least two reasonable default ways to implement this.
498    /// Which one will be the default is not yet decided, so for now
499    /// you probably want to override it specifically.
500    ///
501    /// ## The general answer
502    ///
503    /// It's always correct to implement this with a length prefix:
504    ///
505    /// ```
506    /// # #![feature(hasher_prefixfree_extras)]
507    /// # struct Foo;
508    /// # impl std::hash::Hasher for Foo {
509    /// # fn finish(&self) -> u64 { unimplemented!() }
510    /// # fn write(&mut self, _bytes: &[u8]) { unimplemented!() }
511    /// fn write_str(&mut self, s: &str) {
512    ///     self.write_length_prefix(s.len());
513    ///     self.write(s.as_bytes());
514    /// }
515    /// # }
516    /// ```
517    ///
518    /// And, if your `Hasher` works in `usize` chunks, this is likely a very
519    /// efficient way to do it, as anything more complicated may well end up
520    /// slower than just running the round with the length.
521    ///
522    /// ## If your `Hasher` works byte-wise
523    ///
524    /// One nice thing about `str` being UTF-8 is that the `b'\xFF'` byte
525    /// never happens.  That means that you can append that to the byte stream
526    /// being hashed and maintain prefix-freedom:
527    ///
528    /// ```
529    /// # #![feature(hasher_prefixfree_extras)]
530    /// # struct Foo;
531    /// # impl std::hash::Hasher for Foo {
532    /// # fn finish(&self) -> u64 { unimplemented!() }
533    /// # fn write(&mut self, _bytes: &[u8]) { unimplemented!() }
534    /// fn write_str(&mut self, s: &str) {
535    ///     self.write(s.as_bytes());
536    ///     self.write_u8(0xff);
537    /// }
538    /// # }
539    /// ```
540    ///
541    /// This does require that your implementation not add extra padding, and
542    /// thus generally requires that you maintain a buffer, running a round
543    /// only once that buffer is full (or `finish` is called).
544    ///
545    /// That's because if `write` pads data out to a fixed chunk size, it's
546    /// likely that it does it in such a way that `"a"` and `"a\x00"` would
547    /// end up hashing the same sequence of things, introducing conflicts.
548    #[inline]
549    #[unstable(feature = "hasher_prefixfree_extras", issue = "96762")]
550    fn write_str(&mut self, s: &str) {
551        self.write(s.as_bytes());
552        self.write_u8(0xff);
553    }
554}
555
556#[stable(feature = "indirect_hasher_impl", since = "1.22.0")]
557impl<H: Hasher + ?Sized> Hasher for &mut H {
558    fn finish(&self) -> u64 {
559        (**self).finish()
560    }
561    fn write(&mut self, bytes: &[u8]) {
562        (**self).write(bytes)
563    }
564    fn write_u8(&mut self, i: u8) {
565        (**self).write_u8(i)
566    }
567    fn write_u16(&mut self, i: u16) {
568        (**self).write_u16(i)
569    }
570    fn write_u32(&mut self, i: u32) {
571        (**self).write_u32(i)
572    }
573    fn write_u64(&mut self, i: u64) {
574        (**self).write_u64(i)
575    }
576    fn write_u128(&mut self, i: u128) {
577        (**self).write_u128(i)
578    }
579    fn write_usize(&mut self, i: usize) {
580        (**self).write_usize(i)
581    }
582    fn write_i8(&mut self, i: i8) {
583        (**self).write_i8(i)
584    }
585    fn write_i16(&mut self, i: i16) {
586        (**self).write_i16(i)
587    }
588    fn write_i32(&mut self, i: i32) {
589        (**self).write_i32(i)
590    }
591    fn write_i64(&mut self, i: i64) {
592        (**self).write_i64(i)
593    }
594    fn write_i128(&mut self, i: i128) {
595        (**self).write_i128(i)
596    }
597    fn write_isize(&mut self, i: isize) {
598        (**self).write_isize(i)
599    }
600    fn write_length_prefix(&mut self, len: usize) {
601        (**self).write_length_prefix(len)
602    }
603    fn write_str(&mut self, s: &str) {
604        (**self).write_str(s)
605    }
606}
607
608/// A trait for creating instances of [`Hasher`].
609///
610/// A `BuildHasher` is typically used (e.g., by [`HashMap`]) to create
611/// [`Hasher`]s for each key such that they are hashed independently of one
612/// another, since [`Hasher`]s contain state.
613///
614/// For each instance of `BuildHasher`, the [`Hasher`]s created by
615/// [`build_hasher`] should be identical. That is, if the same stream of bytes
616/// is fed into each hasher, the same output will also be generated.
617///
618/// # Examples
619///
620/// ```
621/// use std::hash::{BuildHasher, Hasher, RandomState};
622///
623/// let s = RandomState::new();
624/// let mut hasher_1 = s.build_hasher();
625/// let mut hasher_2 = s.build_hasher();
626///
627/// hasher_1.write_u32(8128);
628/// hasher_2.write_u32(8128);
629///
630/// assert_eq!(hasher_1.finish(), hasher_2.finish());
631/// ```
632///
633/// [`build_hasher`]: BuildHasher::build_hasher
634/// [`HashMap`]: ../../std/collections/struct.HashMap.html
635#[cfg_attr(not(test), rustc_diagnostic_item = "BuildHasher")]
636#[stable(since = "1.7.0", feature = "build_hasher")]
637pub trait BuildHasher {
638    /// Type of the hasher that will be created.
639    #[stable(since = "1.7.0", feature = "build_hasher")]
640    type Hasher: Hasher;
641
642    /// Creates a new hasher.
643    ///
644    /// Each call to `build_hasher` on the same instance should produce identical
645    /// [`Hasher`]s.
646    ///
647    /// # Examples
648    ///
649    /// ```
650    /// use std::hash::{BuildHasher, RandomState};
651    ///
652    /// let s = RandomState::new();
653    /// let new_s = s.build_hasher();
654    /// ```
655    #[stable(since = "1.7.0", feature = "build_hasher")]
656    fn build_hasher(&self) -> Self::Hasher;
657
658    /// Calculates the hash of a single value.
659    ///
660    /// This is intended as a convenience for code which *consumes* hashes, such
661    /// as the implementation of a hash table or in unit tests that check
662    /// whether a custom [`Hash`] implementation behaves as expected.
663    ///
664    /// This must not be used in any code which *creates* hashes, such as in an
665    /// implementation of [`Hash`].  The way to create a combined hash of
666    /// multiple values is to call [`Hash::hash`] multiple times using the same
667    /// [`Hasher`], not to call this method repeatedly and combine the results.
668    ///
669    /// # Example
670    ///
671    /// ```
672    /// use std::cmp::{max, min};
673    /// use std::hash::{BuildHasher, Hash, Hasher};
674    /// struct OrderAmbivalentPair<T: Ord>(T, T);
675    /// impl<T: Ord + Hash> Hash for OrderAmbivalentPair<T> {
676    ///     fn hash<H: Hasher>(&self, hasher: &mut H) {
677    ///         min(&self.0, &self.1).hash(hasher);
678    ///         max(&self.0, &self.1).hash(hasher);
679    ///     }
680    /// }
681    ///
682    /// // Then later, in a `#[test]` for the type...
683    /// let bh = std::hash::RandomState::new();
684    /// assert_eq!(
685    ///     bh.hash_one(OrderAmbivalentPair(1, 2)),
686    ///     bh.hash_one(OrderAmbivalentPair(2, 1))
687    /// );
688    /// assert_eq!(
689    ///     bh.hash_one(OrderAmbivalentPair(10, 2)),
690    ///     bh.hash_one(&OrderAmbivalentPair(2, 10))
691    /// );
692    /// ```
693    #[stable(feature = "build_hasher_simple_hash_one", since = "1.71.0")]
694    fn hash_one<T: Hash>(&self, x: T) -> u64
695    where
696        Self: Sized,
697        Self::Hasher: Hasher,
698    {
699        let mut hasher = self.build_hasher();
700        x.hash(&mut hasher);
701        hasher.finish()
702    }
703}
704
705/// Used to create a default [`BuildHasher`] instance for types that implement
706/// [`Hasher`] and [`Default`].
707///
708/// `BuildHasherDefault<H>` can be used when a type `H` implements [`Hasher`] and
709/// [`Default`], and you need a corresponding [`BuildHasher`] instance, but none is
710/// defined.
711///
712/// Any `BuildHasherDefault` is [zero-sized]. It can be created with
713/// [`default`][method.default]. When using `BuildHasherDefault` with [`HashMap`] or
714/// [`HashSet`], this doesn't need to be done, since they implement appropriate
715/// [`Default`] instances themselves.
716///
717/// # Examples
718///
719/// Using `BuildHasherDefault` to specify a custom [`BuildHasher`] for
720/// [`HashMap`]:
721///
722/// ```
723/// use std::collections::HashMap;
724/// use std::hash::{BuildHasherDefault, Hasher};
725///
726/// #[derive(Default)]
727/// struct MyHasher;
728///
729/// impl Hasher for MyHasher {
730///     fn write(&mut self, bytes: &[u8]) {
731///         // Your hashing algorithm goes here!
732///        unimplemented!()
733///     }
734///
735///     fn finish(&self) -> u64 {
736///         // Your hashing algorithm goes here!
737///         unimplemented!()
738///     }
739/// }
740///
741/// type MyBuildHasher = BuildHasherDefault<MyHasher>;
742///
743/// let hash_map = HashMap::<u32, u32, MyBuildHasher>::default();
744/// ```
745///
746/// [method.default]: BuildHasherDefault::default
747/// [`HashMap`]: ../../std/collections/struct.HashMap.html
748/// [`HashSet`]: ../../std/collections/struct.HashSet.html
749/// [zero-sized]: https://doc.rust-lang.org/nomicon/exotic-sizes.html#zero-sized-types-zsts
750#[stable(since = "1.7.0", feature = "build_hasher")]
751pub struct BuildHasherDefault<H>(marker::PhantomData<fn() -> H>);
752
753impl<H> BuildHasherDefault<H> {
754    /// Creates a new BuildHasherDefault for Hasher `H`.
755    #[stable(feature = "build_hasher_default_const_new", since = "1.85.0")]
756    #[rustc_const_stable(feature = "build_hasher_default_const_new", since = "1.85.0")]
757    pub const fn new() -> Self {
758        BuildHasherDefault(marker::PhantomData)
759    }
760}
761
762#[stable(since = "1.9.0", feature = "core_impl_debug")]
763impl<H> fmt::Debug for BuildHasherDefault<H> {
764    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
765        f.debug_struct("BuildHasherDefault").finish()
766    }
767}
768
769#[stable(since = "1.7.0", feature = "build_hasher")]
770impl<H: Default + Hasher> BuildHasher for BuildHasherDefault<H> {
771    type Hasher = H;
772
773    fn build_hasher(&self) -> H {
774        H::default()
775    }
776}
777
778#[stable(since = "1.7.0", feature = "build_hasher")]
779impl<H> Clone for BuildHasherDefault<H> {
780    fn clone(&self) -> BuildHasherDefault<H> {
781        BuildHasherDefault(marker::PhantomData)
782    }
783}
784
785#[stable(since = "1.7.0", feature = "build_hasher")]
786#[rustc_const_unstable(feature = "const_default", issue = "143894")]
787impl<H> const Default for BuildHasherDefault<H> {
788    fn default() -> BuildHasherDefault<H> {
789        Self::new()
790    }
791}
792
793#[stable(since = "1.29.0", feature = "build_hasher_eq")]
794impl<H> PartialEq for BuildHasherDefault<H> {
795    fn eq(&self, _other: &BuildHasherDefault<H>) -> bool {
796        true
797    }
798}
799
800#[stable(since = "1.29.0", feature = "build_hasher_eq")]
801impl<H> Eq for BuildHasherDefault<H> {}
802
803mod impls {
804    use super::*;
805    use crate::slice;
806
807    macro_rules! impl_write {
808        ($(($ty:ident, $meth:ident),)*) => {$(
809            #[stable(feature = "rust1", since = "1.0.0")]
810            impl Hash for $ty {
811                #[inline]
812                fn hash<H: Hasher>(&self, state: &mut H) {
813                    state.$meth(*self)
814                }
815
816                #[inline]
817                fn hash_slice<H: Hasher>(data: &[$ty], state: &mut H) {
818                    let newlen = size_of_val(data);
819                    let ptr = data.as_ptr() as *const u8;
820                    // SAFETY: `ptr` is valid and aligned, as this macro is only used
821                    // for numeric primitives which have no padding. The new slice only
822                    // spans across `data` and is never mutated, and its total size is the
823                    // same as the original `data` so it can't be over `isize::MAX`.
824                    state.write(unsafe { slice::from_raw_parts(ptr, newlen) })
825                }
826            }
827        )*}
828    }
829
830    impl_write! {
831        (u8, write_u8),
832        (u16, write_u16),
833        (u32, write_u32),
834        (u64, write_u64),
835        (usize, write_usize),
836        (i8, write_i8),
837        (i16, write_i16),
838        (i32, write_i32),
839        (i64, write_i64),
840        (isize, write_isize),
841        (u128, write_u128),
842        (i128, write_i128),
843    }
844
845    #[stable(feature = "rust1", since = "1.0.0")]
846    impl Hash for bool {
847        #[inline]
848        fn hash<H: Hasher>(&self, state: &mut H) {
849            state.write_u8(*self as u8)
850        }
851    }
852
853    #[stable(feature = "rust1", since = "1.0.0")]
854    impl Hash for char {
855        #[inline]
856        fn hash<H: Hasher>(&self, state: &mut H) {
857            state.write_u32(*self as u32)
858        }
859    }
860
861    #[stable(feature = "rust1", since = "1.0.0")]
862    impl Hash for str {
863        #[inline]
864        fn hash<H: Hasher>(&self, state: &mut H) {
865            state.write_str(self);
866        }
867    }
868
869    #[stable(feature = "never_hash", since = "1.29.0")]
870    impl Hash for ! {
871        #[inline]
872        fn hash<H: Hasher>(&self, _: &mut H) {
873            *self
874        }
875    }
876
877    macro_rules! impl_hash_tuple {
878        () => (
879            #[stable(feature = "rust1", since = "1.0.0")]
880            impl Hash for () {
881                #[inline]
882                fn hash<H: Hasher>(&self, _state: &mut H) {}
883            }
884        );
885
886        ( $($name:ident)+) => (
887            maybe_tuple_doc! {
888                $($name)+ @
889                #[stable(feature = "rust1", since = "1.0.0")]
890                impl<$($name: Hash),+> Hash for ($($name,)+) {
891                    #[allow(non_snake_case)]
892                    #[inline]
893                    fn hash<S: Hasher>(&self, state: &mut S) {
894                        let ($(ref $name,)+) = *self;
895                        $($name.hash(state);)+
896                    }
897                }
898            }
899        );
900    }
901
902    macro_rules! maybe_tuple_doc {
903        ($a:ident @ #[$meta:meta] $item:item) => {
904            #[doc(fake_variadic)]
905            #[doc = "This trait is implemented for tuples up to twelve items long."]
906            #[$meta]
907            $item
908        };
909        ($a:ident $($rest_a:ident)+ @ #[$meta:meta] $item:item) => {
910            #[doc(hidden)]
911            #[$meta]
912            $item
913        };
914    }
915
916    impl_hash_tuple! {}
917    impl_hash_tuple! { T }
918    impl_hash_tuple! { T B }
919    impl_hash_tuple! { T B C }
920    impl_hash_tuple! { T B C D }
921    impl_hash_tuple! { T B C D E }
922    impl_hash_tuple! { T B C D E F }
923    impl_hash_tuple! { T B C D E F G }
924    impl_hash_tuple! { T B C D E F G H }
925    impl_hash_tuple! { T B C D E F G H I }
926    impl_hash_tuple! { T B C D E F G H I J }
927    impl_hash_tuple! { T B C D E F G H I J K }
928    impl_hash_tuple! { T B C D E F G H I J K L }
929
930    #[stable(feature = "rust1", since = "1.0.0")]
931    impl<T: Hash> Hash for [T] {
932        #[inline]
933        fn hash<H: Hasher>(&self, state: &mut H) {
934            state.write_length_prefix(self.len());
935            Hash::hash_slice(self, state)
936        }
937    }
938
939    #[stable(feature = "rust1", since = "1.0.0")]
940    impl<T: ?Sized + marker::PointeeSized + Hash> Hash for &T {
941        #[inline]
942        fn hash<H: Hasher>(&self, state: &mut H) {
943            (**self).hash(state);
944        }
945    }
946
947    #[stable(feature = "rust1", since = "1.0.0")]
948    impl<T: ?Sized + marker::PointeeSized + Hash> Hash for &mut T {
949        #[inline]
950        fn hash<H: Hasher>(&self, state: &mut H) {
951            (**self).hash(state);
952        }
953    }
954
955    #[stable(feature = "rust1", since = "1.0.0")]
956    impl<T: ?Sized + marker::PointeeSized> Hash for *const T {
957        #[inline]
958        fn hash<H: Hasher>(&self, state: &mut H) {
959            let (address, metadata) = self.to_raw_parts();
960            state.write_usize(address.addr());
961            metadata.hash(state);
962        }
963    }
964
965    #[stable(feature = "rust1", since = "1.0.0")]
966    impl<T: ?Sized + marker::PointeeSized> Hash for *mut T {
967        #[inline]
968        fn hash<H: Hasher>(&self, state: &mut H) {
969            let (address, metadata) = self.to_raw_parts();
970            state.write_usize(address.addr());
971            metadata.hash(state);
972        }
973    }
974}
````