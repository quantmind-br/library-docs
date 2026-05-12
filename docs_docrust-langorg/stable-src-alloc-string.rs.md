---
title: string.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/string.rs.html#2386
source: crawler
fetched_at: 2026-05-06T21:34:00.786995987-03:00
rendered_js: false
word_count: 13821
summary: This document describes the String type in Rust, which is a growable, heap-allocated, UTF-8 encoded string, and explains its core characteristics, ownership model, and methods for manipulation.
tags:
    - rust
    - string
    - utf-8
    - memory-management
    - heap-allocation
    - type-reference
category: reference
---

## alloc/ string.rs

````rust
1//! A UTF-8–encoded, growable string.
2//!
3//! This module contains the [`String`] type, the [`ToString`] trait for
4//! converting to strings, and several error types that may result from
5//! working with [`String`]s.
6//!
7//! # Examples
8//!
9//! There are multiple ways to create a new [`String`] from a string literal:
10//!
11//! ```
12//! let s = "Hello".to_string();
13//!
14//! let s = String::from("world");
15//! let s: String = "also this".into();
16//! ```
17//!
18//! You can create a new [`String`] from an existing one by concatenating with
19//! `+`:
20//!
21//! ```
22//! let s = "Hello".to_string();
23//!
24//! let message = s + " world!";
25//! ```
26//!
27//! If you have a vector of valid UTF-8 bytes, you can make a [`String`] out of
28//! it. You can do the reverse too.
29//!
30//! ```
31//! let sparkle_heart = vec![240, 159, 146, 150];
32//!
33//! // We know these bytes are valid, so we'll use `unwrap()`.
34//! let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();
35//!
36//! assert_eq!("💖", sparkle_heart);
37//!
38//! let bytes = sparkle_heart.into_bytes();
39//!
40//! assert_eq!(bytes, [240, 159, 146, 150]);
41//! ```
42
43#![stable(feature = "rust1", since = "1.0.0")]
44
45use core::error::Error;
46use core::iter::FusedIterator;
47#[cfg(not(no_global_oom_handling))]
48use core::iter::from_fn;
49#[cfg(not(no_global_oom_handling))]
50use core::num::Saturating;
51#[cfg(not(no_global_oom_handling))]
52use core::ops::Add;
53#[cfg(not(no_global_oom_handling))]
54use core::ops::AddAssign;
55use core::ops::{self, Range, RangeBounds};
56use core::str::pattern::{Pattern, Utf8Pattern};
57use core::{fmt, hash, ptr, slice};
58
59#[cfg(not(no_global_oom_handling))]
60use crate::alloc::Allocator;
61#[cfg(not(no_global_oom_handling))]
62use crate::borrow::{Cow, ToOwned};
63use crate::boxed::Box;
64use crate::collections::TryReserveError;
65use crate::str::{self, CharIndices, Chars, Utf8Error, from_utf8_unchecked_mut};
66#[cfg(not(no_global_oom_handling))]
67use crate::str::{FromStr, from_boxed_utf8_unchecked};
68use crate::vec::{self, Vec};
69
70/// A UTF-8–encoded, growable string.
71///
72/// `String` is the most common string type. It has ownership over the contents
73/// of the string, stored in a heap-allocated buffer (see [Representation](#representation)).
74/// It is closely related to its borrowed counterpart, the primitive [`str`].
75///
76/// # Examples
77///
78/// You can create a `String` from [a literal string][`&str`] with [`String::from`]:
79///
80/// [`String::from`]: From::from
81///
82/// ```
83/// let hello = String::from("Hello, world!");
84/// ```
85///
86/// You can append a [`char`] to a `String` with the [`push`] method, and
87/// append a [`&str`] with the [`push_str`] method:
88///
89/// ```
90/// let mut hello = String::from("Hello, ");
91///
92/// hello.push('w');
93/// hello.push_str("orld!");
94/// ```
95///
96/// [`push`]: String::push
97/// [`push_str`]: String::push_str
98///
99/// If you have a vector of UTF-8 bytes, you can create a `String` from it with
100/// the [`from_utf8`] method:
101///
102/// ```
103/// // some bytes, in a vector
104/// let sparkle_heart = vec![240, 159, 146, 150];
105///
106/// // We know these bytes are valid, so we'll use `unwrap()`.
107/// let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();
108///
109/// assert_eq!("💖", sparkle_heart);
110/// ```
111///
112/// [`from_utf8`]: String::from_utf8
113///
114/// # UTF-8
115///
116/// `String`s are always valid UTF-8. If you need a non-UTF-8 string, consider
117/// [`OsString`]. It is similar, but without the UTF-8 constraint. Because UTF-8
118/// is a variable width encoding, `String`s are typically smaller than an array of
119/// the same `char`s:
120///
121/// ```
122/// // `s` is ASCII which represents each `char` as one byte
123/// let s = "hello";
124/// assert_eq!(s.len(), 5);
125///
126/// // A `char` array with the same contents would be longer because
127/// // every `char` is four bytes
128/// let s = ['h', 'e', 'l', 'l', 'o'];
129/// let size: usize = s.into_iter().map(|c| size_of_val(&c)).sum();
130/// assert_eq!(size, 20);
131///
132/// // However, for non-ASCII strings, the difference will be smaller
133/// // and sometimes they are the same
134/// let s = "💖💖💖💖💖";
135/// assert_eq!(s.len(), 20);
136///
137/// let s = ['💖', '💖', '💖', '💖', '💖'];
138/// let size: usize = s.into_iter().map(|c| size_of_val(&c)).sum();
139/// assert_eq!(size, 20);
140/// ```
141///
142/// This raises interesting questions as to how `s[i]` should work.
143/// What should `i` be here? Several options include byte indices and
144/// `char` indices but, because of UTF-8 encoding, only byte indices
145/// would provide constant time indexing. Getting the `i`th `char`, for
146/// example, is available using [`chars`]:
147///
148/// ```
149/// let s = "hello";
150/// let third_character = s.chars().nth(2);
151/// assert_eq!(third_character, Some('l'));
152///
153/// let s = "💖💖💖💖💖";
154/// let third_character = s.chars().nth(2);
155/// assert_eq!(third_character, Some('💖'));
156/// ```
157///
158/// Next, what should `s[i]` return? Because indexing returns a reference
159/// to underlying data it could be `&u8`, `&[u8]`, or something similar.
160/// Since we're only providing one index, `&u8` makes the most sense but that
161/// might not be what the user expects and can be explicitly achieved with
162/// [`as_bytes()`]:
163///
164/// ```
165/// // The first byte is 104 - the byte value of `'h'`
166/// let s = "hello";
167/// assert_eq!(s.as_bytes()[0], 104);
168/// // or
169/// assert_eq!(s.as_bytes()[0], b'h');
170///
171/// // The first byte is 240 which isn't obviously useful
172/// let s = "💖💖💖💖💖";
173/// assert_eq!(s.as_bytes()[0], 240);
174/// ```
175///
176/// Due to these ambiguities/restrictions, indexing with a `usize` is simply
177/// forbidden:
178///
179/// ```compile_fail,E0277
180/// let s = "hello";
181///
182/// // The following will not compile!
183/// println!("The first letter of s is {}", s[0]);
184/// ```
185///
186/// It is more clear, however, how `&s[i..j]` should work (that is,
187/// indexing with a range). It should accept byte indices (to be constant-time)
188/// and return a `&str` which is UTF-8 encoded. This is also called "string slicing".
189/// Note this will panic if the byte indices provided are not character
190/// boundaries - see [`is_char_boundary`] for more details. See the implementations
191/// for [`SliceIndex<str>`] for more details on string slicing. For a non-panicking
192/// version of string slicing, see [`get`].
193///
194/// [`OsString`]: ../../std/ffi/struct.OsString.html "ffi::OsString"
195/// [`SliceIndex<str>`]: core::slice::SliceIndex
196/// [`as_bytes()`]: str::as_bytes
197/// [`get`]: str::get
198/// [`is_char_boundary`]: str::is_char_boundary
199///
200/// The [`bytes`] and [`chars`] methods return iterators over the bytes and
201/// codepoints of the string, respectively. To iterate over codepoints along
202/// with byte indices, use [`char_indices`].
203///
204/// [`bytes`]: str::bytes
205/// [`chars`]: str::chars
206/// [`char_indices`]: str::char_indices
207///
208/// # Deref
209///
210/// `String` implements <code>[Deref]<Target = [str]></code>, and so inherits all of [`str`]'s
211/// methods. In addition, this means that you can pass a `String` to a
212/// function which takes a [`&str`] by using an ampersand (`&`):
213///
214/// ```
215/// fn takes_str(s: &str) { }
216///
217/// let s = String::from("Hello");
218///
219/// takes_str(&s);
220/// ```
221///
222/// This will create a [`&str`] from the `String` and pass it in. This
223/// conversion is very inexpensive, and so generally, functions will accept
224/// [`&str`]s as arguments unless they need a `String` for some specific
225/// reason.
226///
227/// In certain cases Rust doesn't have enough information to make this
228/// conversion, known as [`Deref`] coercion. In the following example a string
229/// slice [`&'a str`][`&str`] implements the trait `TraitExample`, and the function
230/// `example_func` takes anything that implements the trait. In this case Rust
231/// would need to make two implicit conversions, which Rust doesn't have the
232/// means to do. For that reason, the following example will not compile.
233///
234/// ```compile_fail,E0277
235/// trait TraitExample {}
236///
237/// impl<'a> TraitExample for &'a str {}
238///
239/// fn example_func<A: TraitExample>(example_arg: A) {}
240///
241/// let example_string = String::from("example_string");
242/// example_func(&example_string);
243/// ```
244///
245/// There are two options that would work instead. The first would be to
246/// change the line `example_func(&example_string);` to
247/// `example_func(example_string.as_str());`, using the method [`as_str()`]
248/// to explicitly extract the string slice containing the string. The second
249/// way changes `example_func(&example_string);` to
250/// `example_func(&*example_string);`. In this case we are dereferencing a
251/// `String` to a [`str`], then referencing the [`str`] back to
252/// [`&str`]. The second way is more idiomatic, however both work to do the
253/// conversion explicitly rather than relying on the implicit conversion.
254///
255/// # Representation
256///
257/// A `String` is made up of three components: a pointer to some bytes, a
258/// length, and a capacity. The pointer points to the internal buffer which `String`
259/// uses to store its data. The length is the number of bytes currently stored
260/// in the buffer, and the capacity is the size of the buffer in bytes. As such,
261/// the length will always be less than or equal to the capacity.
262///
263/// This buffer is always stored on the heap.
264///
265/// You can look at these with the [`as_ptr`], [`len`], and [`capacity`]
266/// methods:
267///
268/// ```
269/// let story = String::from("Once upon a time...");
270///
271/// // Deconstruct the String into parts.
272/// let (ptr, len, capacity) = story.into_raw_parts();
273///
274/// // story has nineteen bytes
275/// assert_eq!(19, len);
276///
277/// // We can re-build a String out of ptr, len, and capacity. This is all
278/// // unsafe because we are responsible for making sure the components are
279/// // valid:
280/// let s = unsafe { String::from_raw_parts(ptr, len, capacity) } ;
281///
282/// assert_eq!(String::from("Once upon a time..."), s);
283/// ```
284///
285/// [`as_ptr`]: str::as_ptr
286/// [`len`]: String::len
287/// [`capacity`]: String::capacity
288///
289/// If a `String` has enough capacity, adding elements to it will not
290/// re-allocate. For example, consider this program:
291///
292/// ```
293/// let mut s = String::new();
294///
295/// println!("{}", s.capacity());
296///
297/// for _ in 0..5 {
298///     s.push_str("hello");
299///     println!("{}", s.capacity());
300/// }
301/// ```
302///
303/// This will output the following:
304///
305/// ```text
306/// 0
307/// 8
308/// 16
309/// 16
310/// 32
311/// 32
312/// ```
313///
314/// At first, we have no memory allocated at all, but as we append to the
315/// string, it increases its capacity appropriately. If we instead use the
316/// [`with_capacity`] method to allocate the correct capacity initially:
317///
318/// ```
319/// let mut s = String::with_capacity(25);
320///
321/// println!("{}", s.capacity());
322///
323/// for _ in 0..5 {
324///     s.push_str("hello");
325///     println!("{}", s.capacity());
326/// }
327/// ```
328///
329/// [`with_capacity`]: String::with_capacity
330///
331/// We end up with a different output:
332///
333/// ```text
334/// 25
335/// 25
336/// 25
337/// 25
338/// 25
339/// 25
340/// ```
341///
342/// Here, there's no need to allocate more memory inside the loop.
343///
344/// [str]: prim@str "str"
345/// [`str`]: prim@str "str"
346/// [`&str`]: prim@str "&str"
347/// [Deref]: core::ops::Deref "ops::Deref"
348/// [`Deref`]: core::ops::Deref "ops::Deref"
349/// [`as_str()`]: String::as_str
350#[derive(PartialEq, PartialOrd, Eq, Ord)]
351#[stable(feature = "rust1", since = "1.0.0")]
352#[lang = "String"]
353pub struct String {
354    vec: Vec<u8>,
355}
356
357/// A possible error value when converting a `String` from a UTF-8 byte vector.
358///
359/// This type is the error type for the [`from_utf8`] method on [`String`]. It
360/// is designed in such a way to carefully avoid reallocations: the
361/// [`into_bytes`] method will give back the byte vector that was used in the
362/// conversion attempt.
363///
364/// [`from_utf8`]: String::from_utf8
365/// [`into_bytes`]: FromUtf8Error::into_bytes
366///
367/// The [`Utf8Error`] type provided by [`std::str`] represents an error that may
368/// occur when converting a slice of [`u8`]s to a [`&str`]. In this sense, it's
369/// an analogue to `FromUtf8Error`, and you can get one from a `FromUtf8Error`
370/// through the [`utf8_error`] method.
371///
372/// [`Utf8Error`]: str::Utf8Error "std::str::Utf8Error"
373/// [`std::str`]: core::str "std::str"
374/// [`&str`]: prim@str "&str"
375/// [`utf8_error`]: FromUtf8Error::utf8_error
376///
377/// # Examples
378///
379/// ```
380/// // some invalid bytes, in a vector
381/// let bytes = vec![0, 159];
382///
383/// let value = String::from_utf8(bytes);
384///
385/// assert!(value.is_err());
386/// assert_eq!(vec![0, 159], value.unwrap_err().into_bytes());
387/// ```
388#[stable(feature = "rust1", since = "1.0.0")]
389#[cfg_attr(not(no_global_oom_handling), derive(Clone))]
390#[derive(Debug, PartialEq, Eq)]
391pub struct FromUtf8Error {
392    bytes: Vec<u8>,
393    error: Utf8Error,
394}
395
396/// A possible error value when converting a `String` from a UTF-16 byte slice.
397///
398/// This type is the error type for the [`from_utf16`] method on [`String`].
399///
400/// [`from_utf16`]: String::from_utf16
401///
402/// # Examples
403///
404/// ```
405/// // 𝄞mu<invalid>ic
406/// let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
407///           0xD800, 0x0069, 0x0063];
408///
409/// assert!(String::from_utf16(v).is_err());
410/// ```
411#[stable(feature = "rust1", since = "1.0.0")]
412#[derive(Debug)]
413pub struct FromUtf16Error(());
414
415impl String {
416    /// Creates a new empty `String`.
417    ///
418    /// Given that the `String` is empty, this will not allocate any initial
419    /// buffer. While that means that this initial operation is very
420    /// inexpensive, it may cause excessive allocation later when you add
421    /// data. If you have an idea of how much data the `String` will hold,
422    /// consider the [`with_capacity`] method to prevent excessive
423    /// re-allocation.
424    ///
425    /// [`with_capacity`]: String::with_capacity
426    ///
427    /// # Examples
428    ///
429    /// ```
430    /// let s = String::new();
431    /// ```
432    #[inline]
433    #[rustc_const_stable(feature = "const_string_new", since = "1.39.0")]
434    #[rustc_diagnostic_item = "string_new"]
435    #[stable(feature = "rust1", since = "1.0.0")]
436    #[must_use]
437    pub const fn new() -> String {
438        String { vec: Vec::new() }
439    }
440
441    /// Creates a new empty `String` with at least the specified capacity.
442    ///
443    /// `String`s have an internal buffer to hold their data. The capacity is
444    /// the length of that buffer, and can be queried with the [`capacity`]
445    /// method. This method creates an empty `String`, but one with an initial
446    /// buffer that can hold at least `capacity` bytes. This is useful when you
447    /// may be appending a bunch of data to the `String`, reducing the number of
448    /// reallocations it needs to do.
449    ///
450    /// [`capacity`]: String::capacity
451    ///
452    /// If the given capacity is `0`, no allocation will occur, and this method
453    /// is identical to the [`new`] method.
454    ///
455    /// [`new`]: String::new
456    ///
457    /// # Panics
458    ///
459    /// Panics if the capacity exceeds `isize::MAX` _bytes_.
460    ///
461    /// # Examples
462    ///
463    /// ```
464    /// let mut s = String::with_capacity(10);
465    ///
466    /// // The String contains no chars, even though it has capacity for more
467    /// assert_eq!(s.len(), 0);
468    ///
469    /// // These are all done without reallocating...
470    /// let cap = s.capacity();
471    /// for _ in 0..10 {
472    ///     s.push('a');
473    /// }
474    ///
475    /// assert_eq!(s.capacity(), cap);
476    ///
477    /// // ...but this may make the string reallocate
478    /// s.push('a');
479    /// ```
480    #[cfg(not(no_global_oom_handling))]
481    #[inline]
482    #[stable(feature = "rust1", since = "1.0.0")]
483    #[must_use]
484    pub fn with_capacity(capacity: usize) -> String {
485        String { vec: Vec::with_capacity(capacity) }
486    }
487
488    /// Creates a new empty `String` with at least the specified capacity.
489    ///
490    /// # Errors
491    ///
492    /// Returns [`Err`] if the capacity exceeds `isize::MAX` bytes,
493    /// or if the memory allocator reports failure.
494    ///
495    #[inline]
496    #[unstable(feature = "try_with_capacity", issue = "91913")]
497    pub fn try_with_capacity(capacity: usize) -> Result<String, TryReserveError> {
498        Ok(String { vec: Vec::try_with_capacity(capacity)? })
499    }
500
501    /// Converts a vector of bytes to a `String`.
502    ///
503    /// A string ([`String`]) is made of bytes ([`u8`]), and a vector of bytes
504    /// ([`Vec<u8>`]) is made of bytes, so this function converts between the
505    /// two. Not all byte slices are valid `String`s, however: `String`
506    /// requires that it is valid UTF-8. `from_utf8()` checks to ensure that
507    /// the bytes are valid UTF-8, and then does the conversion.
508    ///
509    /// If you are sure that the byte slice is valid UTF-8, and you don't want
510    /// to incur the overhead of the validity check, there is an unsafe version
511    /// of this function, [`from_utf8_unchecked`], which has the same behavior
512    /// but skips the check.
513    ///
514    /// This method will take care to not copy the vector, for efficiency's
515    /// sake.
516    ///
517    /// If you need a [`&str`] instead of a `String`, consider
518    /// [`str::from_utf8`].
519    ///
520    /// The inverse of this method is [`into_bytes`].
521    ///
522    /// # Errors
523    ///
524    /// Returns [`Err`] if the slice is not UTF-8 with a description as to why the
525    /// provided bytes are not UTF-8. The vector you moved in is also included.
526    ///
527    /// # Examples
528    ///
529    /// Basic usage:
530    ///
531    /// ```
532    /// // some bytes, in a vector
533    /// let sparkle_heart = vec![240, 159, 146, 150];
534    ///
535    /// // We know these bytes are valid, so we'll use `unwrap()`.
536    /// let sparkle_heart = String::from_utf8(sparkle_heart).unwrap();
537    ///
538    /// assert_eq!("💖", sparkle_heart);
539    /// ```
540    ///
541    /// Incorrect bytes:
542    ///
543    /// ```
544    /// // some invalid bytes, in a vector
545    /// let sparkle_heart = vec![0, 159, 146, 150];
546    ///
547    /// assert!(String::from_utf8(sparkle_heart).is_err());
548    /// ```
549    ///
550    /// See the docs for [`FromUtf8Error`] for more details on what you can do
551    /// with this error.
552    ///
553    /// [`from_utf8_unchecked`]: String::from_utf8_unchecked
554    /// [`Vec<u8>`]: crate::vec::Vec "Vec"
555    /// [`&str`]: prim@str "&str"
556    /// [`into_bytes`]: String::into_bytes
557    #[inline]
558    #[stable(feature = "rust1", since = "1.0.0")]
559    #[rustc_diagnostic_item = "string_from_utf8"]
560    pub fn from_utf8(vec: Vec<u8>) -> Result<String, FromUtf8Error> {
561        match str::from_utf8(&vec) {
562            Ok(..) => Ok(String { vec }),
563            Err(e) => Err(FromUtf8Error { bytes: vec, error: e }),
564        }
565    }
566
567    /// Converts a slice of bytes to a string, including invalid characters.
568    ///
569    /// Strings are made of bytes ([`u8`]), and a slice of bytes
570    /// ([`&[u8]`][byteslice]) is made of bytes, so this function converts
571    /// between the two. Not all byte slices are valid strings, however: strings
572    /// are required to be valid UTF-8. During this conversion,
573    /// `from_utf8_lossy()` will replace any invalid UTF-8 sequences with
574    /// [`U+FFFD REPLACEMENT CHARACTER`][U+FFFD], which looks like this: �
575    ///
576    /// [byteslice]: prim@slice
577    /// [U+FFFD]: core::char::REPLACEMENT_CHARACTER
578    ///
579    /// If you are sure that the byte slice is valid UTF-8, and you don't want
580    /// to incur the overhead of the conversion, there is an unsafe version
581    /// of this function, [`from_utf8_unchecked`], which has the same behavior
582    /// but skips the checks.
583    ///
584    /// [`from_utf8_unchecked`]: String::from_utf8_unchecked
585    ///
586    /// This function returns a [`Cow<'a, str>`]. If our byte slice is invalid
587    /// UTF-8, then we need to insert the replacement characters, which will
588    /// change the size of the string, and hence, require a `String`. But if
589    /// it's already valid UTF-8, we don't need a new allocation. This return
590    /// type allows us to handle both cases.
591    ///
592    /// [`Cow<'a, str>`]: crate::borrow::Cow "borrow::Cow"
593    ///
594    /// # Examples
595    ///
596    /// Basic usage:
597    ///
598    /// ```
599    /// // some bytes, in a vector
600    /// let sparkle_heart = vec![240, 159, 146, 150];
601    ///
602    /// let sparkle_heart = String::from_utf8_lossy(&sparkle_heart);
603    ///
604    /// assert_eq!("💖", sparkle_heart);
605    /// ```
606    ///
607    /// Incorrect bytes:
608    ///
609    /// ```
610    /// // some invalid bytes
611    /// let input = b"Hello \xF0\x90\x80World";
612    /// let output = String::from_utf8_lossy(input);
613    ///
614    /// assert_eq!("Hello �World", output);
615    /// ```
616    #[must_use]
617    #[cfg(not(no_global_oom_handling))]
618    #[stable(feature = "rust1", since = "1.0.0")]
619    pub fn from_utf8_lossy(v: &[u8]) -> Cow<'_, str> {
620        let mut iter = v.utf8_chunks();
621
622        let Some(chunk) = iter.next() else {
623            return Cow::Borrowed("");
624        };
625        let first_valid = chunk.valid();
626        if chunk.invalid().is_empty() {
627            debug_assert_eq!(first_valid.len(), v.len());
628            return Cow::Borrowed(first_valid);
629        }
630
631        const REPLACEMENT: &str = "\u{FFFD}";
632
633        let mut res = String::with_capacity(v.len());
634        res.push_str(first_valid);
635        res.push_str(REPLACEMENT);
636
637        for chunk in iter {
638            res.push_str(chunk.valid());
639            if !chunk.invalid().is_empty() {
640                res.push_str(REPLACEMENT);
641            }
642        }
643
644        Cow::Owned(res)
645    }
646
647    /// Converts a [`Vec<u8>`] to a `String`, substituting invalid UTF-8
648    /// sequences with replacement characters.
649    ///
650    /// See [`from_utf8_lossy`] for more details.
651    ///
652    /// [`from_utf8_lossy`]: String::from_utf8_lossy
653    ///
654    /// Note that this function does not guarantee reuse of the original `Vec`
655    /// allocation.
656    ///
657    /// # Examples
658    ///
659    /// Basic usage:
660    ///
661    /// ```
662    /// #![feature(string_from_utf8_lossy_owned)]
663    /// // some bytes, in a vector
664    /// let sparkle_heart = vec![240, 159, 146, 150];
665    ///
666    /// let sparkle_heart = String::from_utf8_lossy_owned(sparkle_heart);
667    ///
668    /// assert_eq!(String::from("💖"), sparkle_heart);
669    /// ```
670    ///
671    /// Incorrect bytes:
672    ///
673    /// ```
674    /// #![feature(string_from_utf8_lossy_owned)]
675    /// // some invalid bytes
676    /// let input: Vec<u8> = b"Hello \xF0\x90\x80World".into();
677    /// let output = String::from_utf8_lossy_owned(input);
678    ///
679    /// assert_eq!(String::from("Hello �World"), output);
680    /// ```
681    #[must_use]
682    #[cfg(not(no_global_oom_handling))]
683    #[unstable(feature = "string_from_utf8_lossy_owned", issue = "129436")]
684    pub fn from_utf8_lossy_owned(v: Vec<u8>) -> String {
685        if let Cow::Owned(string) = String::from_utf8_lossy(&v) {
686            string
687        } else {
688            // SAFETY: `String::from_utf8_lossy`'s contract ensures that if
689            // it returns a `Cow::Borrowed`, it is a valid UTF-8 string.
690            // Otherwise, it returns a new allocation of an owned `String`, with
691            // replacement characters for invalid sequences, which is returned
692            // above.
693            unsafe { String::from_utf8_unchecked(v) }
694        }
695    }
696
697    /// Decode a native endian UTF-16–encoded vector `v` into a `String`,
698    /// returning [`Err`] if `v` contains any invalid data.
699    ///
700    /// # Examples
701    ///
702    /// ```
703    /// // 𝄞music
704    /// let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
705    ///           0x0073, 0x0069, 0x0063];
706    /// assert_eq!(String::from("𝄞music"),
707    ///            String::from_utf16(v).unwrap());
708    ///
709    /// // 𝄞mu<invalid>ic
710    /// let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
711    ///           0xD800, 0x0069, 0x0063];
712    /// assert!(String::from_utf16(v).is_err());
713    /// ```
714    #[cfg(not(no_global_oom_handling))]
715    #[stable(feature = "rust1", since = "1.0.0")]
716    pub fn from_utf16(v: &[u16]) -> Result<String, FromUtf16Error> {
717        // This isn't done via collect::<Result<_, _>>() for performance reasons.
718        // FIXME: the function can be simplified again when #48994 is closed.
719        let mut ret = String::with_capacity(v.len());
720        for c in char::decode_utf16(v.iter().cloned()) {
721            let Ok(c) = c else {
722                return Err(FromUtf16Error(()));
723            };
724            ret.push(c);
725        }
726        Ok(ret)
727    }
728
729    /// Decode a native endian UTF-16–encoded slice `v` into a `String`,
730    /// replacing invalid data with [the replacement character (`U+FFFD`)][U+FFFD].
731    ///
732    /// Unlike [`from_utf8_lossy`] which returns a [`Cow<'a, str>`],
733    /// `from_utf16_lossy` returns a `String` since the UTF-16 to UTF-8
734    /// conversion requires a memory allocation.
735    ///
736    /// [`from_utf8_lossy`]: String::from_utf8_lossy
737    /// [`Cow<'a, str>`]: crate::borrow::Cow "borrow::Cow"
738    /// [U+FFFD]: core::char::REPLACEMENT_CHARACTER
739    ///
740    /// # Examples
741    ///
742    /// ```
743    /// // 𝄞mus<invalid>ic<invalid>
744    /// let v = &[0xD834, 0xDD1E, 0x006d, 0x0075,
745    ///           0x0073, 0xDD1E, 0x0069, 0x0063,
746    ///           0xD834];
747    ///
748    /// assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
749    ///            String::from_utf16_lossy(v));
750    /// ```
751    #[cfg(not(no_global_oom_handling))]
752    #[must_use]
753    #[inline]
754    #[stable(feature = "rust1", since = "1.0.0")]
755    pub fn from_utf16_lossy(v: &[u16]) -> String {
756        char::decode_utf16(v.iter().cloned())
757            .map(|r| r.unwrap_or(char::REPLACEMENT_CHARACTER))
758            .collect()
759    }
760
761    /// Decode a UTF-16LE–encoded vector `v` into a `String`,
762    /// returning [`Err`] if `v` contains any invalid data.
763    ///
764    /// # Examples
765    ///
766    /// Basic usage:
767    ///
768    /// ```
769    /// #![feature(str_from_utf16_endian)]
770    /// // 𝄞music
771    /// let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
772    ///           0x73, 0x00, 0x69, 0x00, 0x63, 0x00];
773    /// assert_eq!(String::from("𝄞music"),
774    ///            String::from_utf16le(v).unwrap());
775    ///
776    /// // 𝄞mu<invalid>ic
777    /// let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
778    ///           0x00, 0xD8, 0x69, 0x00, 0x63, 0x00];
779    /// assert!(String::from_utf16le(v).is_err());
780    /// ```
781    #[cfg(not(no_global_oom_handling))]
782    #[unstable(feature = "str_from_utf16_endian", issue = "116258")]
783    pub fn from_utf16le(v: &[u8]) -> Result<String, FromUtf16Error> {
784        let (chunks, []) = v.as_chunks::<2>() else {
785            return Err(FromUtf16Error(()));
786        };
787        match (cfg!(target_endian = "little"), unsafe { v.align_to::<u16>() }) {
788            (true, ([], v, [])) => Self::from_utf16(v),
789            _ => char::decode_utf16(chunks.iter().copied().map(u16::from_le_bytes))
790                .collect::<Result<_, _>>()
791                .map_err(|_| FromUtf16Error(())),
792        }
793    }
794
795    /// Decode a UTF-16LE–encoded slice `v` into a `String`, replacing
796    /// invalid data with [the replacement character (`U+FFFD`)][U+FFFD].
797    ///
798    /// Unlike [`from_utf8_lossy`] which returns a [`Cow<'a, str>`],
799    /// `from_utf16le_lossy` returns a `String` since the UTF-16 to UTF-8
800    /// conversion requires a memory allocation.
801    ///
802    /// [`from_utf8_lossy`]: String::from_utf8_lossy
803    /// [`Cow<'a, str>`]: crate::borrow::Cow "borrow::Cow"
804    /// [U+FFFD]: core::char::REPLACEMENT_CHARACTER
805    ///
806    /// # Examples
807    ///
808    /// Basic usage:
809    ///
810    /// ```
811    /// #![feature(str_from_utf16_endian)]
812    /// // 𝄞mus<invalid>ic<invalid>
813    /// let v = &[0x34, 0xD8, 0x1E, 0xDD, 0x6d, 0x00, 0x75, 0x00,
814    ///           0x73, 0x00, 0x1E, 0xDD, 0x69, 0x00, 0x63, 0x00,
815    ///           0x34, 0xD8];
816    ///
817    /// assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
818    ///            String::from_utf16le_lossy(v));
819    /// ```
820    #[cfg(not(no_global_oom_handling))]
821    #[unstable(feature = "str_from_utf16_endian", issue = "116258")]
822    pub fn from_utf16le_lossy(v: &[u8]) -> String {
823        match (cfg!(target_endian = "little"), unsafe { v.align_to::<u16>() }) {
824            (true, ([], v, [])) => Self::from_utf16_lossy(v),
825            (true, ([], v, [_remainder])) => Self::from_utf16_lossy(v) + "\u{FFFD}",
826            _ => {
827                let (chunks, remainder) = v.as_chunks::<2>();
828                let string = char::decode_utf16(chunks.iter().copied().map(u16::from_le_bytes))
829                    .map(|r| r.unwrap_or(char::REPLACEMENT_CHARACTER))
830                    .collect();
831                if remainder.is_empty() { string } else { string + "\u{FFFD}" }
832            }
833        }
834    }
835
836    /// Decode a UTF-16BE–encoded vector `v` into a `String`,
837    /// returning [`Err`] if `v` contains any invalid data.
838    ///
839    /// # Examples
840    ///
841    /// Basic usage:
842    ///
843    /// ```
844    /// #![feature(str_from_utf16_endian)]
845    /// // 𝄞music
846    /// let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
847    ///           0x00, 0x73, 0x00, 0x69, 0x00, 0x63];
848    /// assert_eq!(String::from("𝄞music"),
849    ///            String::from_utf16be(v).unwrap());
850    ///
851    /// // 𝄞mu<invalid>ic
852    /// let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
853    ///           0xD8, 0x00, 0x00, 0x69, 0x00, 0x63];
854    /// assert!(String::from_utf16be(v).is_err());
855    /// ```
856    #[cfg(not(no_global_oom_handling))]
857    #[unstable(feature = "str_from_utf16_endian", issue = "116258")]
858    pub fn from_utf16be(v: &[u8]) -> Result<String, FromUtf16Error> {
859        let (chunks, []) = v.as_chunks::<2>() else {
860            return Err(FromUtf16Error(()));
861        };
862        match (cfg!(target_endian = "big"), unsafe { v.align_to::<u16>() }) {
863            (true, ([], v, [])) => Self::from_utf16(v),
864            _ => char::decode_utf16(chunks.iter().copied().map(u16::from_be_bytes))
865                .collect::<Result<_, _>>()
866                .map_err(|_| FromUtf16Error(())),
867        }
868    }
869
870    /// Decode a UTF-16BE–encoded slice `v` into a `String`, replacing
871    /// invalid data with [the replacement character (`U+FFFD`)][U+FFFD].
872    ///
873    /// Unlike [`from_utf8_lossy`] which returns a [`Cow<'a, str>`],
874    /// `from_utf16le_lossy` returns a `String` since the UTF-16 to UTF-8
875    /// conversion requires a memory allocation.
876    ///
877    /// [`from_utf8_lossy`]: String::from_utf8_lossy
878    /// [`Cow<'a, str>`]: crate::borrow::Cow "borrow::Cow"
879    /// [U+FFFD]: core::char::REPLACEMENT_CHARACTER
880    ///
881    /// # Examples
882    ///
883    /// Basic usage:
884    ///
885    /// ```
886    /// #![feature(str_from_utf16_endian)]
887    /// // 𝄞mus<invalid>ic<invalid>
888    /// let v = &[0xD8, 0x34, 0xDD, 0x1E, 0x00, 0x6d, 0x00, 0x75,
889    ///           0x00, 0x73, 0xDD, 0x1E, 0x00, 0x69, 0x00, 0x63,
890    ///           0xD8, 0x34];
891    ///
892    /// assert_eq!(String::from("𝄞mus\u{FFFD}ic\u{FFFD}"),
893    ///            String::from_utf16be_lossy(v));
894    /// ```
895    #[cfg(not(no_global_oom_handling))]
896    #[unstable(feature = "str_from_utf16_endian", issue = "116258")]
897    pub fn from_utf16be_lossy(v: &[u8]) -> String {
898        match (cfg!(target_endian = "big"), unsafe { v.align_to::<u16>() }) {
899            (true, ([], v, [])) => Self::from_utf16_lossy(v),
900            (true, ([], v, [_remainder])) => Self::from_utf16_lossy(v) + "\u{FFFD}",
901            _ => {
902                let (chunks, remainder) = v.as_chunks::<2>();
903                let string = char::decode_utf16(chunks.iter().copied().map(u16::from_be_bytes))
904                    .map(|r| r.unwrap_or(char::REPLACEMENT_CHARACTER))
905                    .collect();
906                if remainder.is_empty() { string } else { string + "\u{FFFD}" }
907            }
908        }
909    }
910
911    /// Decomposes a `String` into its raw components: `(pointer, length, capacity)`.
912    ///
913    /// Returns the raw pointer to the underlying data, the length of
914    /// the string (in bytes), and the allocated capacity of the data
915    /// (in bytes). These are the same arguments in the same order as
916    /// the arguments to [`from_raw_parts`].
917    ///
918    /// After calling this function, the caller is responsible for the
919    /// memory previously managed by the `String`. The only way to do
920    /// this is to convert the raw pointer, length, and capacity back
921    /// into a `String` with the [`from_raw_parts`] function, allowing
922    /// the destructor to perform the cleanup.
923    ///
924    /// [`from_raw_parts`]: String::from_raw_parts
925    ///
926    /// # Examples
927    ///
928    /// ```
929    /// let s = String::from("hello");
930    ///
931    /// let (ptr, len, cap) = s.into_raw_parts();
932    ///
933    /// let rebuilt = unsafe { String::from_raw_parts(ptr, len, cap) };
934    /// assert_eq!(rebuilt, "hello");
935    /// ```
936    #[must_use = "losing the pointer will leak memory"]
937    #[stable(feature = "vec_into_raw_parts", since = "1.93.0")]
938    pub fn into_raw_parts(self) -> (*mut u8, usize, usize) {
939        self.vec.into_raw_parts()
940    }
941
942    /// Creates a new `String` from a pointer, a length and a capacity.
943    ///
944    /// # Safety
945    ///
946    /// This is highly unsafe, due to the number of invariants that aren't
947    /// checked:
948    ///
949    /// * all safety requirements for [`Vec::<u8>::from_raw_parts`].
950    /// * all safety requirements for [`String::from_utf8_unchecked`].
951    ///
952    /// Violating these may cause problems like corrupting the allocator's
953    /// internal data structures. For example, it is normally **not** safe to
954    /// build a `String` from a pointer to a C `char` array containing UTF-8
955    /// _unless_ you are certain that array was originally allocated by the
956    /// Rust standard library's allocator.
957    ///
958    /// The ownership of `buf` is effectively transferred to the
959    /// `String` which may then deallocate, reallocate or change the
960    /// contents of memory pointed to by the pointer at will. Ensure
961    /// that nothing else uses the pointer after calling this
962    /// function.
963    ///
964    /// # Examples
965    ///
966    /// ```
967    /// unsafe {
968    ///     let s = String::from("hello");
969    ///
970    ///     // Deconstruct the String into parts.
971    ///     let (ptr, len, capacity) = s.into_raw_parts();
972    ///
973    ///     let s = String::from_raw_parts(ptr, len, capacity);
974    ///
975    ///     assert_eq!(String::from("hello"), s);
976    /// }
977    /// ```
978    #[inline]
979    #[stable(feature = "rust1", since = "1.0.0")]
980    pub unsafe fn from_raw_parts(buf: *mut u8, length: usize, capacity: usize) -> String {
981        unsafe { String { vec: Vec::from_raw_parts(buf, length, capacity) } }
982    }
983
984    /// Converts a vector of bytes to a `String` without checking that the
985    /// string contains valid UTF-8.
986    ///
987    /// See the safe version, [`from_utf8`], for more details.
988    ///
989    /// [`from_utf8`]: String::from_utf8
990    ///
991    /// # Safety
992    ///
993    /// This function is unsafe because it does not check that the bytes passed
994    /// to it are valid UTF-8. If this constraint is violated, it may cause
995    /// memory unsafety issues with future users of the `String`, as the rest of
996    /// the standard library assumes that `String`s are valid UTF-8.
997    ///
998    /// # Examples
999    ///
1000    /// ```
1001    /// // some bytes, in a vector
1002    /// let sparkle_heart = vec![240, 159, 146, 150];
1003    ///
1004    /// let sparkle_heart = unsafe {
1005    ///     String::from_utf8_unchecked(sparkle_heart)
1006    /// };
1007    ///
1008    /// assert_eq!("💖", sparkle_heart);
1009    /// ```
1010    #[inline]
1011    #[must_use]
1012    #[stable(feature = "rust1", since = "1.0.0")]
1013    pub unsafe fn from_utf8_unchecked(bytes: Vec<u8>) -> String {
1014        String { vec: bytes }
1015    }
1016
1017    /// Converts a `String` into a byte vector.
1018    ///
1019    /// This consumes the `String`, so we do not need to copy its contents.
1020    ///
1021    /// # Examples
1022    ///
1023    /// ```
1024    /// let s = String::from("hello");
1025    /// let bytes = s.into_bytes();
1026    ///
1027    /// assert_eq!(&[104, 101, 108, 108, 111][..], &bytes[..]);
1028    /// ```
1029    #[inline]
1030    #[must_use = "`self` will be dropped if the result is not used"]
1031    #[stable(feature = "rust1", since = "1.0.0")]
1032    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1033    #[rustc_allow_const_fn_unstable(const_precise_live_drops)]
1034    pub const fn into_bytes(self) -> Vec<u8> {
1035        self.vec
1036    }
1037
1038    /// Extracts a string slice containing the entire `String`.
1039    ///
1040    /// # Examples
1041    ///
1042    /// ```
1043    /// let s = String::from("foo");
1044    ///
1045    /// assert_eq!("foo", s.as_str());
1046    /// ```
1047    #[inline]
1048    #[must_use]
1049    #[stable(feature = "string_as_str", since = "1.7.0")]
1050    #[rustc_diagnostic_item = "string_as_str"]
1051    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1052    pub const fn as_str(&self) -> &str {
1053        // SAFETY: String contents are stipulated to be valid UTF-8, invalid contents are an error
1054        // at construction.
1055        unsafe { str::from_utf8_unchecked(self.vec.as_slice()) }
1056    }
1057
1058    /// Converts a `String` into a mutable string slice.
1059    ///
1060    /// # Examples
1061    ///
1062    /// ```
1063    /// let mut s = String::from("foobar");
1064    /// let s_mut_str = s.as_mut_str();
1065    ///
1066    /// s_mut_str.make_ascii_uppercase();
1067    ///
1068    /// assert_eq!("FOOBAR", s_mut_str);
1069    /// ```
1070    #[inline]
1071    #[must_use]
1072    #[stable(feature = "string_as_str", since = "1.7.0")]
1073    #[rustc_diagnostic_item = "string_as_mut_str"]
1074    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1075    pub const fn as_mut_str(&mut self) -> &mut str {
1076        // SAFETY: String contents are stipulated to be valid UTF-8, invalid contents are an error
1077        // at construction.
1078        unsafe { str::from_utf8_unchecked_mut(self.vec.as_mut_slice()) }
1079    }
1080
1081    /// Appends a given string slice onto the end of this `String`.
1082    ///
1083    /// # Panics
1084    ///
1085    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
1086    ///
1087    /// # Examples
1088    ///
1089    /// ```
1090    /// let mut s = String::from("foo");
1091    ///
1092    /// s.push_str("bar");
1093    ///
1094    /// assert_eq!("foobar", s);
1095    /// ```
1096    #[cfg(not(no_global_oom_handling))]
1097    #[inline]
1098    #[stable(feature = "rust1", since = "1.0.0")]
1099    #[rustc_confusables("append", "push")]
1100    #[rustc_diagnostic_item = "string_push_str"]
1101    pub fn push_str(&mut self, string: &str) {
1102        self.vec.extend_from_slice(string.as_bytes())
1103    }
1104
1105    #[cfg(not(no_global_oom_handling))]
1106    #[inline]
1107    fn push_str_slice(&mut self, slice: &[&str]) {
1108        // use saturating arithmetic to ensure that in the case of an overflow, reserve() throws OOM
1109        let additional: Saturating<usize> = slice.iter().map(|x| Saturating(x.len())).sum();
1110        self.reserve(additional.0);
1111        let (ptr, len, cap) = core::mem::take(self).into_raw_parts();
1112        unsafe {
1113            let mut dst = ptr.add(len);
1114            for new in slice {
1115                core::ptr::copy_nonoverlapping(new.as_ptr(), dst, new.len());
1116                dst = dst.add(new.len());
1117            }
1118            *self = String::from_raw_parts(ptr, len + additional.0, cap);
1119        }
1120    }
1121
1122    /// Copies elements from `src` range to the end of the string.
1123    ///
1124    /// # Panics
1125    ///
1126    /// Panics if the range has `start_bound > end_bound`, if the range is
1127    /// bounded on either end and does not lie on a [`char`] boundary, or if the
1128    /// new capacity exceeds `isize::MAX` bytes.
1129    ///
1130    /// # Examples
1131    ///
1132    /// ```
1133    /// let mut string = String::from("abcde");
1134    ///
1135    /// string.extend_from_within(2..);
1136    /// assert_eq!(string, "abcdecde");
1137    ///
1138    /// string.extend_from_within(..2);
1139    /// assert_eq!(string, "abcdecdeab");
1140    ///
1141    /// string.extend_from_within(4..8);
1142    /// assert_eq!(string, "abcdecdeabecde");
1143    /// ```
1144    #[cfg(not(no_global_oom_handling))]
1145    #[stable(feature = "string_extend_from_within", since = "1.87.0")]
1146    #[track_caller]
1147    pub fn extend_from_within<R>(&mut self, src: R)
1148    where
1149        R: RangeBounds<usize>,
1150    {
1151        let src @ Range { start, end } = slice::range(src, ..self.len());
1152
1153        assert!(self.is_char_boundary(start));
1154        assert!(self.is_char_boundary(end));
1155
1156        self.vec.extend_from_within(src);
1157    }
1158
1159    /// Returns this `String`'s capacity, in bytes.
1160    ///
1161    /// # Examples
1162    ///
1163    /// ```
1164    /// let s = String::with_capacity(10);
1165    ///
1166    /// assert!(s.capacity() >= 10);
1167    /// ```
1168    #[inline]
1169    #[must_use]
1170    #[stable(feature = "rust1", since = "1.0.0")]
1171    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1172    pub const fn capacity(&self) -> usize {
1173        self.vec.capacity()
1174    }
1175
1176    /// Reserves capacity for at least `additional` bytes more than the
1177    /// current length. The allocator may reserve more space to speculatively
1178    /// avoid frequent allocations. After calling `reserve`,
1179    /// capacity will be greater than or equal to `self.len() + additional`.
1180    /// Does nothing if capacity is already sufficient.
1181    ///
1182    /// # Panics
1183    ///
1184    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
1185    ///
1186    /// # Examples
1187    ///
1188    /// Basic usage:
1189    ///
1190    /// ```
1191    /// let mut s = String::new();
1192    ///
1193    /// s.reserve(10);
1194    ///
1195    /// assert!(s.capacity() >= 10);
1196    /// ```
1197    ///
1198    /// This might not actually increase the capacity:
1199    ///
1200    /// ```
1201    /// let mut s = String::with_capacity(10);
1202    /// s.push('a');
1203    /// s.push('b');
1204    ///
1205    /// // s now has a length of 2 and a capacity of at least 10
1206    /// let capacity = s.capacity();
1207    /// assert_eq!(2, s.len());
1208    /// assert!(capacity >= 10);
1209    ///
1210    /// // Since we already have at least an extra 8 capacity, calling this...
1211    /// s.reserve(8);
1212    ///
1213    /// // ... doesn't actually increase.
1214    /// assert_eq!(capacity, s.capacity());
1215    /// ```
1216    #[cfg(not(no_global_oom_handling))]
1217    #[inline]
1218    #[stable(feature = "rust1", since = "1.0.0")]
1219    pub fn reserve(&mut self, additional: usize) {
1220        self.vec.reserve(additional)
1221    }
1222
1223    /// Reserves the minimum capacity for at least `additional` bytes more than
1224    /// the current length. Unlike [`reserve`], this will not
1225    /// deliberately over-allocate to speculatively avoid frequent allocations.
1226    /// After calling `reserve_exact`, capacity will be greater than or equal to
1227    /// `self.len() + additional`. Does nothing if the capacity is already
1228    /// sufficient.
1229    ///
1230    /// [`reserve`]: String::reserve
1231    ///
1232    /// # Panics
1233    ///
1234    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
1235    ///
1236    /// # Examples
1237    ///
1238    /// Basic usage:
1239    ///
1240    /// ```
1241    /// let mut s = String::new();
1242    ///
1243    /// s.reserve_exact(10);
1244    ///
1245    /// assert!(s.capacity() >= 10);
1246    /// ```
1247    ///
1248    /// This might not actually increase the capacity:
1249    ///
1250    /// ```
1251    /// let mut s = String::with_capacity(10);
1252    /// s.push('a');
1253    /// s.push('b');
1254    ///
1255    /// // s now has a length of 2 and a capacity of at least 10
1256    /// let capacity = s.capacity();
1257    /// assert_eq!(2, s.len());
1258    /// assert!(capacity >= 10);
1259    ///
1260    /// // Since we already have at least an extra 8 capacity, calling this...
1261    /// s.reserve_exact(8);
1262    ///
1263    /// // ... doesn't actually increase.
1264    /// assert_eq!(capacity, s.capacity());
1265    /// ```
1266    #[cfg(not(no_global_oom_handling))]
1267    #[inline]
1268    #[stable(feature = "rust1", since = "1.0.0")]
1269    pub fn reserve_exact(&mut self, additional: usize) {
1270        self.vec.reserve_exact(additional)
1271    }
1272
1273    /// Tries to reserve capacity for at least `additional` bytes more than the
1274    /// current length. The allocator may reserve more space to speculatively
1275    /// avoid frequent allocations. After calling `try_reserve`, capacity will be
1276    /// greater than or equal to `self.len() + additional` if it returns
1277    /// `Ok(())`. Does nothing if capacity is already sufficient. This method
1278    /// preserves the contents even if an error occurs.
1279    ///
1280    /// # Errors
1281    ///
1282    /// If the capacity overflows, or the allocator reports a failure, then an error
1283    /// is returned.
1284    ///
1285    /// # Examples
1286    ///
1287    /// ```
1288    /// use std::collections::TryReserveError;
1289    ///
1290    /// fn process_data(data: &str) -> Result<String, TryReserveError> {
1291    ///     let mut output = String::new();
1292    ///
1293    ///     // Pre-reserve the memory, exiting if we can't
1294    ///     output.try_reserve(data.len())?;
1295    ///
1296    ///     // Now we know this can't OOM in the middle of our complex work
1297    ///     output.push_str(data);
1298    ///
1299    ///     Ok(output)
1300    /// }
1301    /// # process_data("rust").expect("why is the test harness OOMing on 4 bytes?");
1302    /// ```
1303    #[stable(feature = "try_reserve", since = "1.57.0")]
1304    pub fn try_reserve(&mut self, additional: usize) -> Result<(), TryReserveError> {
1305        self.vec.try_reserve(additional)
1306    }
1307
1308    /// Tries to reserve the minimum capacity for at least `additional` bytes
1309    /// more than the current length. Unlike [`try_reserve`], this will not
1310    /// deliberately over-allocate to speculatively avoid frequent allocations.
1311    /// After calling `try_reserve_exact`, capacity will be greater than or
1312    /// equal to `self.len() + additional` if it returns `Ok(())`.
1313    /// Does nothing if the capacity is already sufficient.
1314    ///
1315    /// Note that the allocator may give the collection more space than it
1316    /// requests. Therefore, capacity can not be relied upon to be precisely
1317    /// minimal. Prefer [`try_reserve`] if future insertions are expected.
1318    ///
1319    /// [`try_reserve`]: String::try_reserve
1320    ///
1321    /// # Errors
1322    ///
1323    /// If the capacity overflows, or the allocator reports a failure, then an error
1324    /// is returned.
1325    ///
1326    /// # Examples
1327    ///
1328    /// ```
1329    /// use std::collections::TryReserveError;
1330    ///
1331    /// fn process_data(data: &str) -> Result<String, TryReserveError> {
1332    ///     let mut output = String::new();
1333    ///
1334    ///     // Pre-reserve the memory, exiting if we can't
1335    ///     output.try_reserve_exact(data.len())?;
1336    ///
1337    ///     // Now we know this can't OOM in the middle of our complex work
1338    ///     output.push_str(data);
1339    ///
1340    ///     Ok(output)
1341    /// }
1342    /// # process_data("rust").expect("why is the test harness OOMing on 4 bytes?");
1343    /// ```
1344    #[stable(feature = "try_reserve", since = "1.57.0")]
1345    pub fn try_reserve_exact(&mut self, additional: usize) -> Result<(), TryReserveError> {
1346        self.vec.try_reserve_exact(additional)
1347    }
1348
1349    /// Shrinks the capacity of this `String` to match its length.
1350    ///
1351    /// # Examples
1352    ///
1353    /// ```
1354    /// let mut s = String::from("foo");
1355    ///
1356    /// s.reserve(100);
1357    /// assert!(s.capacity() >= 100);
1358    ///
1359    /// s.shrink_to_fit();
1360    /// assert_eq!(3, s.capacity());
1361    /// ```
1362    #[cfg(not(no_global_oom_handling))]
1363    #[inline]
1364    #[stable(feature = "rust1", since = "1.0.0")]
1365    pub fn shrink_to_fit(&mut self) {
1366        self.vec.shrink_to_fit()
1367    }
1368
1369    /// Shrinks the capacity of this `String` with a lower bound.
1370    ///
1371    /// The capacity will remain at least as large as both the length
1372    /// and the supplied value.
1373    ///
1374    /// If the current capacity is less than the lower limit, this is a no-op.
1375    ///
1376    /// # Examples
1377    ///
1378    /// ```
1379    /// let mut s = String::from("foo");
1380    ///
1381    /// s.reserve(100);
1382    /// assert!(s.capacity() >= 100);
1383    ///
1384    /// s.shrink_to(10);
1385    /// assert!(s.capacity() >= 10);
1386    /// s.shrink_to(0);
1387    /// assert!(s.capacity() >= 3);
1388    /// ```
1389    #[cfg(not(no_global_oom_handling))]
1390    #[inline]
1391    #[stable(feature = "shrink_to", since = "1.56.0")]
1392    pub fn shrink_to(&mut self, min_capacity: usize) {
1393        self.vec.shrink_to(min_capacity)
1394    }
1395
1396    /// Appends the given [`char`] to the end of this `String`.
1397    ///
1398    /// # Panics
1399    ///
1400    /// Panics if the new capacity exceeds `isize::MAX` _bytes_.
1401    ///
1402    /// # Examples
1403    ///
1404    /// ```
1405    /// let mut s = String::from("abc");
1406    ///
1407    /// s.push('1');
1408    /// s.push('2');
1409    /// s.push('3');
1410    ///
1411    /// assert_eq!("abc123", s);
1412    /// ```
1413    #[cfg(not(no_global_oom_handling))]
1414    #[inline]
1415    #[stable(feature = "rust1", since = "1.0.0")]
1416    pub fn push(&mut self, ch: char) {
1417        let len = self.len();
1418        let ch_len = ch.len_utf8();
1419        self.reserve(ch_len);
1420
1421        // SAFETY: Just reserved capacity for at least the length needed to encode `ch`.
1422        unsafe {
1423            core::char::encode_utf8_raw_unchecked(ch as u32, self.vec.as_mut_ptr().add(self.len()));
1424            self.vec.set_len(len + ch_len);
1425        }
1426    }
1427
1428    /// Returns a byte slice of this `String`'s contents.
1429    ///
1430    /// The inverse of this method is [`from_utf8`].
1431    ///
1432    /// [`from_utf8`]: String::from_utf8
1433    ///
1434    /// # Examples
1435    ///
1436    /// ```
1437    /// let s = String::from("hello");
1438    ///
1439    /// assert_eq!(&[104, 101, 108, 108, 111], s.as_bytes());
1440    /// ```
1441    #[inline]
1442    #[must_use]
1443    #[stable(feature = "rust1", since = "1.0.0")]
1444    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1445    pub const fn as_bytes(&self) -> &[u8] {
1446        self.vec.as_slice()
1447    }
1448
1449    /// Shortens this `String` to the specified length.
1450    ///
1451    /// If `new_len` is greater than or equal to the string's current length, this has no
1452    /// effect.
1453    ///
1454    /// Note that this method has no effect on the allocated capacity
1455    /// of the string
1456    ///
1457    /// # Panics
1458    ///
1459    /// Panics if `new_len` does not lie on a [`char`] boundary.
1460    ///
1461    /// # Examples
1462    ///
1463    /// ```
1464    /// let mut s = String::from("hello");
1465    ///
1466    /// s.truncate(2);
1467    ///
1468    /// assert_eq!("he", s);
1469    /// ```
1470    #[inline]
1471    #[stable(feature = "rust1", since = "1.0.0")]
1472    #[track_caller]
1473    pub fn truncate(&mut self, new_len: usize) {
1474        if new_len <= self.len() {
1475            assert!(self.is_char_boundary(new_len));
1476            self.vec.truncate(new_len)
1477        }
1478    }
1479
1480    /// Removes the last character from the string buffer and returns it.
1481    ///
1482    /// Returns [`None`] if this `String` is empty.
1483    ///
1484    /// # Examples
1485    ///
1486    /// ```
1487    /// let mut s = String::from("abč");
1488    ///
1489    /// assert_eq!(s.pop(), Some('č'));
1490    /// assert_eq!(s.pop(), Some('b'));
1491    /// assert_eq!(s.pop(), Some('a'));
1492    ///
1493    /// assert_eq!(s.pop(), None);
1494    /// ```
1495    #[inline]
1496    #[stable(feature = "rust1", since = "1.0.0")]
1497    pub fn pop(&mut self) -> Option<char> {
1498        let ch = self.chars().rev().next()?;
1499        let newlen = self.len() - ch.len_utf8();
1500        unsafe {
1501            self.vec.set_len(newlen);
1502        }
1503        Some(ch)
1504    }
1505
1506    /// Removes a [`char`] from this `String` at byte position `idx` and returns it.
1507    ///
1508    /// Copies all bytes after the removed char to new positions.
1509    ///
1510    /// Note that calling this in a loop can result in quadratic behavior.
1511    ///
1512    /// # Panics
1513    ///
1514    /// Panics if `idx` is larger than or equal to the `String`'s length,
1515    /// or if it does not lie on a [`char`] boundary.
1516    ///
1517    /// # Examples
1518    ///
1519    /// ```
1520    /// let mut s = String::from("abç");
1521    ///
1522    /// assert_eq!(s.remove(0), 'a');
1523    /// assert_eq!(s.remove(1), 'ç');
1524    /// assert_eq!(s.remove(0), 'b');
1525    /// ```
1526    #[inline]
1527    #[stable(feature = "rust1", since = "1.0.0")]
1528    #[track_caller]
1529    #[rustc_confusables("delete", "take")]
1530    pub fn remove(&mut self, idx: usize) -> char {
1531        let ch = match self[idx..].chars().next() {
1532            Some(ch) => ch,
1533            None => panic!("cannot remove a char from the end of a string"),
1534        };
1535
1536        let next = idx + ch.len_utf8();
1537        let len = self.len();
1538        unsafe {
1539            ptr::copy(self.vec.as_ptr().add(next), self.vec.as_mut_ptr().add(idx), len - next);
1540            self.vec.set_len(len - (next - idx));
1541        }
1542        ch
1543    }
1544
1545    /// Remove all matches of pattern `pat` in the `String`.
1546    ///
1547    /// # Examples
1548    ///
1549    /// ```
1550    /// #![feature(string_remove_matches)]
1551    /// let mut s = String::from("Trees are not green, the sky is not blue.");
1552    /// s.remove_matches("not ");
1553    /// assert_eq!("Trees are green, the sky is blue.", s);
1554    /// ```
1555    ///
1556    /// Matches will be detected and removed iteratively, so in cases where
1557    /// patterns overlap, only the first pattern will be removed:
1558    ///
1559    /// ```
1560    /// #![feature(string_remove_matches)]
1561    /// let mut s = String::from("banana");
1562    /// s.remove_matches("ana");
1563    /// assert_eq!("bna", s);
1564    /// ```
1565    #[cfg(not(no_global_oom_handling))]
1566    #[unstable(feature = "string_remove_matches", issue = "72826")]
1567    pub fn remove_matches<P: Pattern>(&mut self, pat: P) {
1568        use core::str::pattern::Searcher;
1569
1570        let rejections = {
1571            let mut searcher = pat.into_searcher(self);
1572            // Per Searcher::next:
1573            //
1574            // A Match result needs to contain the whole matched pattern,
1575            // however Reject results may be split up into arbitrary many
1576            // adjacent fragments. Both ranges may have zero length.
1577            //
1578            // In practice the implementation of Searcher::next_match tends to
1579            // be more efficient, so we use it here and do some work to invert
1580            // matches into rejections since that's what we want to copy below.
1581            let mut front = 0;
1582            let rejections: Vec<_> = from_fn(|| {
1583                let (start, end) = searcher.next_match()?;
1584                let prev_front = front;
1585                front = end;
1586                Some((prev_front, start))
1587            })
1588            .collect();
1589            rejections.into_iter().chain(core::iter::once((front, self.len())))
1590        };
1591
1592        let mut len = 0;
1593        let ptr = self.vec.as_mut_ptr();
1594
1595        for (start, end) in rejections {
1596            let count = end - start;
1597            if start != len {
1598                // SAFETY: per Searcher::next:
1599                //
1600                // The stream of Match and Reject values up to a Done will
1601                // contain index ranges that are adjacent, non-overlapping,
1602                // covering the whole haystack, and laying on utf8
1603                // boundaries.
1604                unsafe {
1605                    ptr::copy(ptr.add(start), ptr.add(len), count);
1606                }
1607            }
1608            len += count;
1609        }
1610
1611        unsafe {
1612            self.vec.set_len(len);
1613        }
1614    }
1615
1616    /// Retains only the characters specified by the predicate.
1617    ///
1618    /// In other words, remove all characters `c` such that `f(c)` returns `false`.
1619    /// This method operates in place, visiting each character exactly once in the
1620    /// original order, and preserves the order of the retained characters.
1621    ///
1622    /// # Examples
1623    ///
1624    /// ```
1625    /// let mut s = String::from("f_o_ob_ar");
1626    ///
1627    /// s.retain(|c| c != '_');
1628    ///
1629    /// assert_eq!(s, "foobar");
1630    /// ```
1631    ///
1632    /// Because the elements are visited exactly once in the original order,
1633    /// external state may be used to decide which elements to keep.
1634    ///
1635    /// ```
1636    /// let mut s = String::from("abcde");
1637    /// let keep = [false, true, true, false, true];
1638    /// let mut iter = keep.iter();
1639    /// s.retain(|_| *iter.next().unwrap());
1640    /// assert_eq!(s, "bce");
1641    /// ```
1642    #[inline]
1643    #[stable(feature = "string_retain", since = "1.26.0")]
1644    pub fn retain<F>(&mut self, mut f: F)
1645    where
1646        F: FnMut(char) -> bool,
1647    {
1648        struct SetLenOnDrop<'a> {
1649            s: &'a mut String,
1650            idx: usize,
1651            del_bytes: usize,
1652        }
1653
1654        impl<'a> Drop for SetLenOnDrop<'a> {
1655            fn drop(&mut self) {
1656                let new_len = self.idx - self.del_bytes;
1657                debug_assert!(new_len <= self.s.len());
1658                unsafe { self.s.vec.set_len(new_len) };
1659            }
1660        }
1661
1662        let len = self.len();
1663        let mut guard = SetLenOnDrop { s: self, idx: 0, del_bytes: 0 };
1664
1665        while guard.idx < len {
1666            let ch =
1667                // SAFETY: `guard.idx` is positive-or-zero and less that len so the `get_unchecked`
1668                // is in bound. `self` is valid UTF-8 like string and the returned slice starts at
1669                // a unicode code point so the `Chars` always return one character.
1670                unsafe { guard.s.get_unchecked(guard.idx..len).chars().next().unwrap_unchecked() };
1671            let ch_len = ch.len_utf8();
1672
1673            if !f(ch) {
1674                guard.del_bytes += ch_len;
1675            } else if guard.del_bytes > 0 {
1676                // SAFETY: `guard.idx` is in bound and `guard.del_bytes` represent the number of
1677                // bytes that are erased from the string so the resulting `guard.idx -
1678                // guard.del_bytes` always represent a valid unicode code point.
1679                //
1680                // `guard.del_bytes` >= `ch.len_utf8()`, so taking a slice with `ch.len_utf8()` len
1681                // is safe.
1682                ch.encode_utf8(unsafe {
1683                    crate::slice::from_raw_parts_mut(
1684                        guard.s.as_mut_ptr().add(guard.idx - guard.del_bytes),
1685                        ch.len_utf8(),
1686                    )
1687                });
1688            }
1689
1690            // Point idx to the next char
1691            guard.idx += ch_len;
1692        }
1693
1694        drop(guard);
1695    }
1696
1697    /// Inserts a character into this `String` at byte position `idx`.
1698    ///
1699    /// Reallocates if `self.capacity()` is insufficient, which may involve copying all
1700    /// `self.capacity()` bytes. Makes space for the insertion by copying all bytes of
1701    /// `&self[idx..]` to new positions.
1702    ///
1703    /// Note that calling this in a loop can result in quadratic behavior.
1704    ///
1705    /// # Panics
1706    ///
1707    /// Panics if `idx` is larger than the `String`'s length, or if it does not
1708    /// lie on a [`char`] boundary.
1709    ///
1710    /// # Examples
1711    ///
1712    /// ```
1713    /// let mut s = String::with_capacity(3);
1714    ///
1715    /// s.insert(0, 'f');
1716    /// s.insert(1, 'o');
1717    /// s.insert(2, 'o');
1718    ///
1719    /// assert_eq!("foo", s);
1720    /// ```
1721    #[cfg(not(no_global_oom_handling))]
1722    #[inline]
1723    #[track_caller]
1724    #[stable(feature = "rust1", since = "1.0.0")]
1725    #[rustc_confusables("set")]
1726    pub fn insert(&mut self, idx: usize, ch: char) {
1727        assert!(self.is_char_boundary(idx));
1728
1729        let len = self.len();
1730        let ch_len = ch.len_utf8();
1731        self.reserve(ch_len);
1732
1733        // SAFETY: Move the bytes starting from `idx` to their new location `ch_len`
1734        // bytes ahead. This is safe because sufficient capacity was reserved, and `idx`
1735        // is a char boundary.
1736        unsafe {
1737            ptr::copy(
1738                self.vec.as_ptr().add(idx),
1739                self.vec.as_mut_ptr().add(idx + ch_len),
1740                len - idx,
1741            );
1742        }
1743
1744        // SAFETY: Encode the character into the vacated region if `idx != len`,
1745        // or into the uninitialized spare capacity otherwise.
1746        unsafe {
1747            core::char::encode_utf8_raw_unchecked(ch as u32, self.vec.as_mut_ptr().add(idx));
1748        }
1749
1750        // SAFETY: Update the length to include the newly added bytes.
1751        unsafe {
1752            self.vec.set_len(len + ch_len);
1753        }
1754    }
1755
1756    /// Inserts a string slice into this `String` at byte position `idx`.
1757    ///
1758    /// Reallocates if `self.capacity()` is insufficient, which may involve copying all
1759    /// `self.capacity()` bytes. Makes space for the insertion by copying all bytes of
1760    /// `&self[idx..]` to new positions.
1761    ///
1762    /// Note that calling this in a loop can result in quadratic behavior.
1763    ///
1764    /// # Panics
1765    ///
1766    /// Panics if `idx` is larger than the `String`'s length, or if it does not
1767    /// lie on a [`char`] boundary.
1768    ///
1769    /// # Examples
1770    ///
1771    /// ```
1772    /// let mut s = String::from("bar");
1773    ///
1774    /// s.insert_str(0, "foo");
1775    ///
1776    /// assert_eq!("foobar", s);
1777    /// ```
1778    #[cfg(not(no_global_oom_handling))]
1779    #[inline]
1780    #[track_caller]
1781    #[stable(feature = "insert_str", since = "1.16.0")]
1782    #[rustc_diagnostic_item = "string_insert_str"]
1783    pub fn insert_str(&mut self, idx: usize, string: &str) {
1784        assert!(self.is_char_boundary(idx));
1785
1786        let len = self.len();
1787        let amt = string.len();
1788        self.reserve(amt);
1789
1790        // SAFETY: Move the bytes starting from `idx` to their new location `amt` bytes
1791        // ahead. This is safe because sufficient capacity was just reserved, and `idx`
1792        // is a char boundary.
1793        unsafe {
1794            ptr::copy(self.vec.as_ptr().add(idx), self.vec.as_mut_ptr().add(idx + amt), len - idx);
1795        }
1796
1797        // SAFETY: Copy the new string slice into the vacated region if `idx != len`,
1798        // or into the uninitialized spare capacity otherwise. The borrow checker
1799        // ensures that the source and destination do not overlap.
1800        unsafe {
1801            ptr::copy_nonoverlapping(string.as_ptr(), self.vec.as_mut_ptr().add(idx), amt);
1802        }
1803
1804        // SAFETY: Update the length to include the newly added bytes.
1805        unsafe {
1806            self.vec.set_len(len + amt);
1807        }
1808    }
1809
1810    /// Returns a mutable reference to the contents of this `String`.
1811    ///
1812    /// # Safety
1813    ///
1814    /// This function is unsafe because the returned `&mut Vec` allows writing
1815    /// bytes which are not valid UTF-8. If this constraint is violated, using
1816    /// the original `String` after dropping the `&mut Vec` may violate memory
1817    /// safety, as the rest of the standard library assumes that `String`s are
1818    /// valid UTF-8.
1819    ///
1820    /// # Examples
1821    ///
1822    /// ```
1823    /// let mut s = String::from("hello");
1824    ///
1825    /// unsafe {
1826    ///     let vec = s.as_mut_vec();
1827    ///     assert_eq!(&[104, 101, 108, 108, 111][..], &vec[..]);
1828    ///
1829    ///     vec.reverse();
1830    /// }
1831    /// assert_eq!(s, "olleh");
1832    /// ```
1833    #[inline]
1834    #[stable(feature = "rust1", since = "1.0.0")]
1835    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1836    pub const unsafe fn as_mut_vec(&mut self) -> &mut Vec<u8> {
1837        &mut self.vec
1838    }
1839
1840    /// Returns the length of this `String`, in bytes, not [`char`]s or
1841    /// graphemes. In other words, it might not be what a human considers the
1842    /// length of the string.
1843    ///
1844    /// # Examples
1845    ///
1846    /// ```
1847    /// let a = String::from("foo");
1848    /// assert_eq!(a.len(), 3);
1849    ///
1850    /// let fancy_f = String::from("ƒoo");
1851    /// assert_eq!(fancy_f.len(), 4);
1852    /// assert_eq!(fancy_f.chars().count(), 3);
1853    /// ```
1854    #[inline]
1855    #[must_use]
1856    #[stable(feature = "rust1", since = "1.0.0")]
1857    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1858    #[rustc_confusables("length", "size")]
1859    #[rustc_no_implicit_autorefs]
1860    pub const fn len(&self) -> usize {
1861        self.vec.len()
1862    }
1863
1864    /// Returns `true` if this `String` has a length of zero, and `false` otherwise.
1865    ///
1866    /// # Examples
1867    ///
1868    /// ```
1869    /// let mut v = String::new();
1870    /// assert!(v.is_empty());
1871    ///
1872    /// v.push('a');
1873    /// assert!(!v.is_empty());
1874    /// ```
1875    #[inline]
1876    #[must_use]
1877    #[stable(feature = "rust1", since = "1.0.0")]
1878    #[rustc_const_stable(feature = "const_vec_string_slice", since = "1.87.0")]
1879    #[rustc_no_implicit_autorefs]
1880    pub const fn is_empty(&self) -> bool {
1881        self.len() == 0
1882    }
1883
1884    /// Splits the string into two at the given byte index.
1885    ///
1886    /// Returns a newly allocated `String`. `self` contains bytes `[0, at)`, and
1887    /// the returned `String` contains bytes `[at, len)`. `at` must be on the
1888    /// boundary of a UTF-8 code point.
1889    ///
1890    /// Note that the capacity of `self` does not change.
1891    ///
1892    /// # Panics
1893    ///
1894    /// Panics if `at` is not on a `UTF-8` code point boundary, or if it is beyond the last
1895    /// code point of the string.
1896    ///
1897    /// # Examples
1898    ///
1899    /// ```
1900    /// # fn main() {
1901    /// let mut hello = String::from("Hello, World!");
1902    /// let world = hello.split_off(7);
1903    /// assert_eq!(hello, "Hello, ");
1904    /// assert_eq!(world, "World!");
1905    /// # }
1906    /// ```
1907    #[cfg(not(no_global_oom_handling))]
1908    #[inline]
1909    #[track_caller]
1910    #[stable(feature = "string_split_off", since = "1.16.0")]
1911    #[must_use = "use `.truncate()` if you don't need the other half"]
1912    pub fn split_off(&mut self, at: usize) -> String {
1913        assert!(self.is_char_boundary(at));
1914        let other = self.vec.split_off(at);
1915        unsafe { String::from_utf8_unchecked(other) }
1916    }
1917
1918    /// Truncates this `String`, removing all contents.
1919    ///
1920    /// While this means the `String` will have a length of zero, it does not
1921    /// touch its capacity.
1922    ///
1923    /// # Examples
1924    ///
1925    /// ```
1926    /// let mut s = String::from("foo");
1927    ///
1928    /// s.clear();
1929    ///
1930    /// assert!(s.is_empty());
1931    /// assert_eq!(0, s.len());
1932    /// assert_eq!(3, s.capacity());
1933    /// ```
1934    #[inline]
1935    #[stable(feature = "rust1", since = "1.0.0")]
1936    pub fn clear(&mut self) {
1937        self.vec.clear()
1938    }
1939
1940    /// Removes the specified range from the string in bulk, returning all
1941    /// removed characters as an iterator.
1942    ///
1943    /// The returned iterator keeps a mutable borrow on the string to optimize
1944    /// its implementation.
1945    ///
1946    /// # Panics
1947    ///
1948    /// Panics if the range has `start_bound > end_bound`, or, if the range is
1949    /// bounded on either end and does not lie on a [`char`] boundary.
1950    ///
1951    /// # Leaking
1952    ///
1953    /// If the returned iterator goes out of scope without being dropped (due to
1954    /// [`core::mem::forget`], for example), the string may still contain a copy
1955    /// of any drained characters, or may have lost characters arbitrarily,
1956    /// including characters outside the range.
1957    ///
1958    /// # Examples
1959    ///
1960    /// ```
1961    /// let mut s = String::from("α is alpha, β is beta");
1962    /// let beta_offset = s.find('β').unwrap_or(s.len());
1963    ///
1964    /// // Remove the range up until the β from the string
1965    /// let t: String = s.drain(..beta_offset).collect();
1966    /// assert_eq!(t, "α is alpha, ");
1967    /// assert_eq!(s, "β is beta");
1968    ///
1969    /// // A full range clears the string, like `clear()` does
1970    /// s.drain(..);
1971    /// assert_eq!(s, "");
1972    /// ```
1973    #[stable(feature = "drain", since = "1.6.0")]
1974    #[track_caller]
1975    pub fn drain<R>(&mut self, range: R) -> Drain<'_>
1976    where
1977        R: RangeBounds<usize>,
1978    {
1979        // Memory safety
1980        //
1981        // The String version of Drain does not have the memory safety issues
1982        // of the vector version. The data is just plain bytes.
1983        // Because the range removal happens in Drop, if the Drain iterator is leaked,
1984        // the removal will not happen.
1985        let Range { start, end } = slice::range(range, ..self.len());
1986        assert!(self.is_char_boundary(start));
1987        assert!(self.is_char_boundary(end));
1988
1989        // Take out two simultaneous borrows. The &mut String won't be accessed
1990        // until iteration is over, in Drop.
1991        let self_ptr = self as *mut _;
1992        // SAFETY: `slice::range` and `is_char_boundary` do the appropriate bounds checks.
1993        let chars_iter = unsafe { self.get_unchecked(start..end) }.chars();
1994
1995        Drain { start, end, iter: chars_iter, string: self_ptr }
1996    }
1997
1998    /// Converts a `String` into an iterator over the [`char`]s of the string.
1999    ///
2000    /// As a string consists of valid UTF-8, we can iterate through a string
2001    /// by [`char`]. This method returns such an iterator.
2002    ///
2003    /// It's important to remember that [`char`] represents a Unicode Scalar
2004    /// Value, and might not match your idea of what a 'character' is. Iteration
2005    /// over grapheme clusters may be what you actually want. That functionality
2006    /// is not provided by Rust's standard library, check crates.io instead.
2007    ///
2008    /// # Examples
2009    ///
2010    /// Basic usage:
2011    ///
2012    /// ```
2013    /// #![feature(string_into_chars)]
2014    ///
2015    /// let word = String::from("goodbye");
2016    ///
2017    /// let mut chars = word.into_chars();
2018    ///
2019    /// assert_eq!(Some('g'), chars.next());
2020    /// assert_eq!(Some('o'), chars.next());
2021    /// assert_eq!(Some('o'), chars.next());
2022    /// assert_eq!(Some('d'), chars.next());
2023    /// assert_eq!(Some('b'), chars.next());
2024    /// assert_eq!(Some('y'), chars.next());
2025    /// assert_eq!(Some('e'), chars.next());
2026    ///
2027    /// assert_eq!(None, chars.next());
2028    /// ```
2029    ///
2030    /// Remember, [`char`]s might not match your intuition about characters:
2031    ///
2032    /// ```
2033    /// #![feature(string_into_chars)]
2034    ///
2035    /// let y = String::from("y̆");
2036    ///
2037    /// let mut chars = y.into_chars();
2038    ///
2039    /// assert_eq!(Some('y'), chars.next()); // not 'y̆'
2040    /// assert_eq!(Some('\u{0306}'), chars.next());
2041    ///
2042    /// assert_eq!(None, chars.next());
2043    /// ```
2044    ///
2045    /// [`char`]: prim@char
2046    #[inline]
2047    #[must_use = "`self` will be dropped if the result is not used"]
2048    #[unstable(feature = "string_into_chars", issue = "133125")]
2049    pub fn into_chars(self) -> IntoChars {
2050        IntoChars { bytes: self.into_bytes().into_iter() }
2051    }
2052
2053    /// Removes the specified range in the string,
2054    /// and replaces it with the given string.
2055    /// The given string doesn't need to be the same length as the range.
2056    ///
2057    /// # Panics
2058    ///
2059    /// Panics if the range has `start_bound > end_bound`, or, if the range is
2060    /// bounded on either end and does not lie on a [`char`] boundary.
2061    ///
2062    /// # Examples
2063    ///
2064    /// ```
2065    /// let mut s = String::from("α is alpha, β is beta");
2066    /// let beta_offset = s.find('β').unwrap_or(s.len());
2067    ///
2068    /// // Replace the range up until the β from the string
2069    /// s.replace_range(..beta_offset, "Α is capital alpha; ");
2070    /// assert_eq!(s, "Α is capital alpha; β is beta");
2071    /// ```
2072    #[cfg(not(no_global_oom_handling))]
2073    #[stable(feature = "splice", since = "1.27.0")]
2074    #[track_caller]
2075    pub fn replace_range<R>(&mut self, range: R, replace_with: &str)
2076    where
2077        R: RangeBounds<usize>,
2078    {
2079        // We avoid #81138 (nondeterministic RangeBounds impls) because we only use `range` once, here.
2080        let checked_range = slice::range(range, ..self.len());
2081
2082        assert!(
2083            self.is_char_boundary(checked_range.start),
2084            "start of range should be a character boundary"
2085        );
2086        assert!(
2087            self.is_char_boundary(checked_range.end),
2088            "end of range should be a character boundary"
2089        );
2090
2091        unsafe { self.as_mut_vec() }.splice(checked_range, replace_with.bytes());
2092    }
2093
2094    /// Replaces the leftmost occurrence of a pattern with another string, in-place.
2095    ///
2096    /// This method can be preferred over [`string = string.replacen(..., 1);`][replacen],
2097    /// as it can use the `String`'s existing capacity to prevent a reallocation if
2098    /// sufficient space is available.
2099    ///
2100    /// # Examples
2101    ///
2102    /// Basic usage:
2103    ///
2104    /// ```
2105    /// #![feature(string_replace_in_place)]
2106    ///
2107    /// let mut s = String::from("Test Results: ❌❌❌");
2108    ///
2109    /// // Replace the leftmost ❌ with a ✅
2110    /// s.replace_first('❌', "✅");
2111    /// assert_eq!(s, "Test Results: ✅❌❌");
2112    /// ```
2113    ///
2114    /// [replacen]: ../../std/primitive.str.html#method.replacen
2115    #[cfg(not(no_global_oom_handling))]
2116    #[unstable(feature = "string_replace_in_place", issue = "147949")]
2117    pub fn replace_first<P: Pattern>(&mut self, from: P, to: &str) {
2118        let range = match self.match_indices(from).next() {
2119            Some((start, match_str)) => start..start + match_str.len(),
2120            None => return,
2121        };
2122
2123        self.replace_range(range, to);
2124    }
2125
2126    /// Replaces the rightmost occurrence of a pattern with another string, in-place.
2127    ///
2128    /// # Examples
2129    ///
2130    /// Basic usage:
2131    ///
2132    /// ```
2133    /// #![feature(string_replace_in_place)]
2134    ///
2135    /// let mut s = String::from("Test Results: ❌❌❌");
2136    ///
2137    /// // Replace the rightmost ❌ with a ✅
2138    /// s.replace_last('❌', "✅");
2139    /// assert_eq!(s, "Test Results: ❌❌✅");
2140    /// ```
2141    #[cfg(not(no_global_oom_handling))]
2142    #[unstable(feature = "string_replace_in_place", issue = "147949")]
2143    pub fn replace_last<P: Pattern>(&mut self, from: P, to: &str)
2144    where
2145        for<'a> P::Searcher<'a>: core::str::pattern::ReverseSearcher<'a>,
2146    {
2147        let range = match self.rmatch_indices(from).next() {
2148            Some((start, match_str)) => start..start + match_str.len(),
2149            None => return,
2150        };
2151
2152        self.replace_range(range, to);
2153    }
2154
2155    /// Converts this `String` into a <code>[Box]<[str]></code>.
2156    ///
2157    /// Before doing the conversion, this method discards excess capacity like [`shrink_to_fit`].
2158    /// Note that this call may reallocate and copy the bytes of the string.
2159    ///
2160    /// [`shrink_to_fit`]: String::shrink_to_fit
2161    /// [str]: prim@str "str"
2162    ///
2163    /// # Examples
2164    ///
2165    /// ```
2166    /// let s = String::from("hello");
2167    ///
2168    /// let b = s.into_boxed_str();
2169    /// ```
2170    #[cfg(not(no_global_oom_handling))]
2171    #[stable(feature = "box_str", since = "1.4.0")]
2172    #[must_use = "`self` will be dropped if the result is not used"]
2173    #[inline]
2174    pub fn into_boxed_str(self) -> Box<str> {
2175        let slice = self.vec.into_boxed_slice();
2176        unsafe { from_boxed_utf8_unchecked(slice) }
2177    }
2178
2179    /// Consumes and leaks the `String`, returning a mutable reference to the contents,
2180    /// `&'a mut str`.
2181    ///
2182    /// The caller has free choice over the returned lifetime, including `'static`. Indeed,
2183    /// this function is ideally used for data that lives for the remainder of the program's life,
2184    /// as dropping the returned reference will cause a memory leak.
2185    ///
2186    /// It does not reallocate or shrink the `String`, so the leaked allocation may include unused
2187    /// capacity that is not part of the returned slice. If you want to discard excess capacity,
2188    /// call [`into_boxed_str`], and then [`Box::leak`] instead. However, keep in mind that
2189    /// trimming the capacity may result in a reallocation and copy.
2190    ///
2191    /// [`into_boxed_str`]: Self::into_boxed_str
2192    ///
2193    /// # Examples
2194    ///
2195    /// ```
2196    /// let x = String::from("bucket");
2197    /// let static_ref: &'static mut str = x.leak();
2198    /// assert_eq!(static_ref, "bucket");
2199    /// # // FIXME(https://github.com/rust-lang/miri/issues/3670):
2200    /// # // use -Zmiri-disable-leak-check instead of unleaking in tests meant to leak.
2201    /// # drop(unsafe { Box::from_raw(static_ref) });
2202    /// ```
2203    #[stable(feature = "string_leak", since = "1.72.0")]
2204    #[inline]
2205    pub fn leak<'a>(self) -> &'a mut str {
2206        let slice = self.vec.leak();
2207        unsafe { from_utf8_unchecked_mut(slice) }
2208    }
2209}
2210
2211impl FromUtf8Error {
2212    /// Returns a slice of [`u8`]s bytes that were attempted to convert to a `String`.
2213    ///
2214    /// # Examples
2215    ///
2216    /// ```
2217    /// // some invalid bytes, in a vector
2218    /// let bytes = vec![0, 159];
2219    ///
2220    /// let value = String::from_utf8(bytes);
2221    ///
2222    /// assert_eq!(&[0, 159], value.unwrap_err().as_bytes());
2223    /// ```
2224    #[must_use]
2225    #[stable(feature = "from_utf8_error_as_bytes", since = "1.26.0")]
2226    pub fn as_bytes(&self) -> &[u8] {
2227        &self.bytes[..]
2228    }
2229
2230    /// Converts the bytes into a `String` lossily, substituting invalid UTF-8
2231    /// sequences with replacement characters.
2232    ///
2233    /// See [`String::from_utf8_lossy`] for more details on replacement of
2234    /// invalid sequences, and [`String::from_utf8_lossy_owned`] for the
2235    /// `String` function which corresponds to this function.
2236    ///
2237    /// # Examples
2238    ///
2239    /// ```
2240    /// #![feature(string_from_utf8_lossy_owned)]
2241    /// // some invalid bytes
2242    /// let input: Vec<u8> = b"Hello \xF0\x90\x80World".into();
2243    /// let output = String::from_utf8(input).unwrap_or_else(|e| e.into_utf8_lossy());
2244    ///
2245    /// assert_eq!(String::from("Hello �World"), output);
2246    /// ```
2247    #[must_use]
2248    #[cfg(not(no_global_oom_handling))]
2249    #[unstable(feature = "string_from_utf8_lossy_owned", issue = "129436")]
2250    pub fn into_utf8_lossy(self) -> String {
2251        const REPLACEMENT: &str = "\u{FFFD}";
2252
2253        let mut res = {
2254            let mut v = Vec::with_capacity(self.bytes.len());
2255
2256            // `Utf8Error::valid_up_to` returns the maximum index of validated
2257            // UTF-8 bytes. Copy the valid bytes into the output buffer.
2258            v.extend_from_slice(&self.bytes[..self.error.valid_up_to()]);
2259
2260            // SAFETY: This is safe because the only bytes present in the buffer
2261            // were validated as UTF-8 by the call to `String::from_utf8` which
2262            // produced this `FromUtf8Error`.
2263            unsafe { String::from_utf8_unchecked(v) }
2264        };
2265
2266        let iter = self.bytes[self.error.valid_up_to()..].utf8_chunks();
2267
2268        for chunk in iter {
2269            res.push_str(chunk.valid());
2270            if !chunk.invalid().is_empty() {
2271                res.push_str(REPLACEMENT);
2272            }
2273        }
2274
2275        res
2276    }
2277
2278    /// Returns the bytes that were attempted to convert to a `String`.
2279    ///
2280    /// This method is carefully constructed to avoid allocation. It will
2281    /// consume the error, moving out the bytes, so that a copy of the bytes
2282    /// does not need to be made.
2283    ///
2284    /// # Examples
2285    ///
2286    /// ```
2287    /// // some invalid bytes, in a vector
2288    /// let bytes = vec![0, 159];
2289    ///
2290    /// let value = String::from_utf8(bytes);
2291    ///
2292    /// assert_eq!(vec![0, 159], value.unwrap_err().into_bytes());
2293    /// ```
2294    #[must_use = "`self` will be dropped if the result is not used"]
2295    #[stable(feature = "rust1", since = "1.0.0")]
2296    pub fn into_bytes(self) -> Vec<u8> {
2297        self.bytes
2298    }
2299
2300    /// Fetch a `Utf8Error` to get more details about the conversion failure.
2301    ///
2302    /// The [`Utf8Error`] type provided by [`std::str`] represents an error that may
2303    /// occur when converting a slice of [`u8`]s to a [`&str`]. In this sense, it's
2304    /// an analogue to `FromUtf8Error`. See its documentation for more details
2305    /// on using it.
2306    ///
2307    /// [`std::str`]: core::str "std::str"
2308    /// [`&str`]: prim@str "&str"
2309    ///
2310    /// # Examples
2311    ///
2312    /// ```
2313    /// // some invalid bytes, in a vector
2314    /// let bytes = vec![0, 159];
2315    ///
2316    /// let error = String::from_utf8(bytes).unwrap_err().utf8_error();
2317    ///
2318    /// // the first byte is invalid here
2319    /// assert_eq!(1, error.valid_up_to());
2320    /// ```
2321    #[must_use]
2322    #[stable(feature = "rust1", since = "1.0.0")]
2323    pub fn utf8_error(&self) -> Utf8Error {
2324        self.error
2325    }
2326}
2327
2328#[stable(feature = "rust1", since = "1.0.0")]
2329impl fmt::Display for FromUtf8Error {
2330    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2331        fmt::Display::fmt(&self.error, f)
2332    }
2333}
2334
2335#[stable(feature = "rust1", since = "1.0.0")]
2336impl fmt::Display for FromUtf16Error {
2337    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2338        fmt::Display::fmt("invalid utf-16: lone surrogate found", f)
2339    }
2340}
2341
2342#[stable(feature = "rust1", since = "1.0.0")]
2343impl Error for FromUtf8Error {}
2344
2345#[stable(feature = "rust1", since = "1.0.0")]
2346impl Error for FromUtf16Error {}
2347
2348#[cfg(not(no_global_oom_handling))]
2349#[stable(feature = "rust1", since = "1.0.0")]
2350impl Clone for String {
2351    fn clone(&self) -> Self {
2352        String { vec: self.vec.clone() }
2353    }
2354
2355    /// Clones the contents of `source` into `self`.
2356    ///
2357    /// This method is preferred over simply assigning `source.clone()` to `self`,
2358    /// as it avoids reallocation if possible.
2359    fn clone_from(&mut self, source: &Self) {
2360        self.vec.clone_from(&source.vec);
2361    }
2362}
2363
2364#[cfg(not(no_global_oom_handling))]
2365#[stable(feature = "rust1", since = "1.0.0")]
2366impl FromIterator<char> for String {
2367    fn from_iter<I: IntoIterator<Item = char>>(iter: I) -> String {
2368        let mut buf = String::new();
2369        buf.extend(iter);
2370        buf
2371    }
2372}
2373
2374#[cfg(not(no_global_oom_handling))]
2375#[stable(feature = "string_from_iter_by_ref", since = "1.17.0")]
2376impl<'a> FromIterator<&'a char> for String {
2377    fn from_iter<I: IntoIterator<Item = &'a char>>(iter: I) -> String {
2378        let mut buf = String::new();
2379        buf.extend(iter);
2380        buf
2381    }
2382}
2383
2384#[cfg(not(no_global_oom_handling))]
2385#[stable(feature = "rust1", since = "1.0.0")]
2386impl<'a> FromIterator<&'a str> for String {
2387    fn from_iter<I: IntoIterator<Item = &'a str>>(iter: I) -> String {
2388        let mut buf = String::new();
2389        buf.extend(iter);
2390        buf
2391    }
2392}
2393
2394#[cfg(not(no_global_oom_handling))]
2395#[stable(feature = "extend_string", since = "1.4.0")]
2396impl FromIterator<String> for String {
2397    fn from_iter<I: IntoIterator<Item = String>>(iter: I) -> String {
2398        let mut iterator = iter.into_iter();
2399
2400        // Because we're iterating over `String`s, we can avoid at least
2401        // one allocation by getting the first string from the iterator
2402        // and appending to it all the subsequent strings.
2403        match iterator.next() {
2404            None => String::new(),
2405            Some(mut buf) => {
2406                buf.extend(iterator);
2407                buf
2408            }
2409        }
2410    }
2411}
2412
2413#[cfg(not(no_global_oom_handling))]
2414#[stable(feature = "box_str2", since = "1.45.0")]
2415impl<A: Allocator> FromIterator<Box<str, A>> for String {
2416    fn from_iter<I: IntoIterator<Item = Box<str, A>>>(iter: I) -> String {
2417        let mut buf = String::new();
2418        buf.extend(iter);
2419        buf
2420    }
2421}
2422
2423#[cfg(not(no_global_oom_handling))]
2424#[stable(feature = "herd_cows", since = "1.19.0")]
2425impl<'a> FromIterator<Cow<'a, str>> for String {
2426    fn from_iter<I: IntoIterator<Item = Cow<'a, str>>>(iter: I) -> String {
2427        let mut iterator = iter.into_iter();
2428
2429        // Because we're iterating over CoWs, we can (potentially) avoid at least
2430        // one allocation by getting the first item and appending to it all the
2431        // subsequent items.
2432        match iterator.next() {
2433            None => String::new(),
2434            Some(cow) => {
2435                let mut buf = cow.into_owned();
2436                buf.extend(iterator);
2437                buf
2438            }
2439        }
2440    }
2441}
2442
2443#[cfg(not(no_global_oom_handling))]
2444#[unstable(feature = "ascii_char", issue = "110998")]
2445impl FromIterator<core::ascii::Char> for String {
2446    fn from_iter<T: IntoIterator<Item = core::ascii::Char>>(iter: T) -> Self {
2447        let buf = iter.into_iter().map(core::ascii::Char::to_u8).collect();
2448        // SAFETY: `buf` is guaranteed to be valid UTF-8 because the `core::ascii::Char` type
2449        // only contains ASCII values (0x00-0x7F), which are valid UTF-8.
2450        unsafe { String::from_utf8_unchecked(buf) }
2451    }
2452}
2453
2454#[cfg(not(no_global_oom_handling))]
2455#[unstable(feature = "ascii_char", issue = "110998")]
2456impl<'a> FromIterator<&'a core::ascii::Char> for String {
2457    fn from_iter<T: IntoIterator<Item = &'a core::ascii::Char>>(iter: T) -> Self {
2458        let buf = iter.into_iter().copied().map(core::ascii::Char::to_u8).collect();
2459        // SAFETY: `buf` is guaranteed to be valid UTF-8 because the `core::ascii::Char` type
2460        // only contains ASCII values (0x00-0x7F), which are valid UTF-8.
2461        unsafe { String::from_utf8_unchecked(buf) }
2462    }
2463}
2464
2465#[cfg(not(no_global_oom_handling))]
2466#[stable(feature = "rust1", since = "1.0.0")]
2467impl Extend<char> for String {
2468    fn extend<I: IntoIterator<Item = char>>(&mut self, iter: I) {
2469        let iterator = iter.into_iter();
2470        let (lower_bound, _) = iterator.size_hint();
2471        self.reserve(lower_bound);
2472        iterator.for_each(move |c| self.push(c));
2473    }
2474
2475    #[inline]
2476    fn extend_one(&mut self, c: char) {
2477        self.push(c);
2478    }
2479
2480    #[inline]
2481    fn extend_reserve(&mut self, additional: usize) {
2482        self.reserve(additional);
2483    }
2484}
2485
2486#[cfg(not(no_global_oom_handling))]
2487#[stable(feature = "extend_ref", since = "1.2.0")]
2488impl<'a> Extend<&'a char> for String {
2489    fn extend<I: IntoIterator<Item = &'a char>>(&mut self, iter: I) {
2490        self.extend(iter.into_iter().cloned());
2491    }
2492
2493    #[inline]
2494    fn extend_one(&mut self, &c: &'a char) {
2495        self.push(c);
2496    }
2497
2498    #[inline]
2499    fn extend_reserve(&mut self, additional: usize) {
2500        self.reserve(additional);
2501    }
2502}
2503
2504#[cfg(not(no_global_oom_handling))]
2505#[stable(feature = "rust1", since = "1.0.0")]
2506impl<'a> Extend<&'a str> for String {
2507    fn extend<I: IntoIterator<Item = &'a str>>(&mut self, iter: I) {
2508        <I as SpecExtendStr>::spec_extend_into(iter, self)
2509    }
2510
2511    #[inline]
2512    fn extend_one(&mut self, s: &'a str) {
2513        self.push_str(s);
2514    }
2515}
2516
2517#[cfg(not(no_global_oom_handling))]
2518trait SpecExtendStr {
2519    fn spec_extend_into(self, s: &mut String);
2520}
2521
2522#[cfg(not(no_global_oom_handling))]
2523impl<'a, T: IntoIterator<Item = &'a str>> SpecExtendStr for T {
2524    default fn spec_extend_into(self, target: &mut String) {
2525        self.into_iter().for_each(move |s| target.push_str(s));
2526    }
2527}
2528
2529#[cfg(not(no_global_oom_handling))]
2530impl SpecExtendStr for [&str] {
2531    fn spec_extend_into(self, target: &mut String) {
2532        target.push_str_slice(&self);
2533    }
2534}
2535
2536#[cfg(not(no_global_oom_handling))]
2537impl<const N: usize> SpecExtendStr for [&str; N] {
2538    fn spec_extend_into(self, target: &mut String) {
2539        target.push_str_slice(&self[..]);
2540    }
2541}
2542
2543#[cfg(not(no_global_oom_handling))]
2544#[stable(feature = "box_str2", since = "1.45.0")]
2545impl<A: Allocator> Extend<Box<str, A>> for String {
2546    fn extend<I: IntoIterator<Item = Box<str, A>>>(&mut self, iter: I) {
2547        iter.into_iter().for_each(move |s| self.push_str(&s));
2548    }
2549}
2550
2551#[cfg(not(no_global_oom_handling))]
2552#[stable(feature = "extend_string", since = "1.4.0")]
2553impl Extend<String> for String {
2554    fn extend<I: IntoIterator<Item = String>>(&mut self, iter: I) {
2555        iter.into_iter().for_each(move |s| self.push_str(&s));
2556    }
2557
2558    #[inline]
2559    fn extend_one(&mut self, s: String) {
2560        self.push_str(&s);
2561    }
2562}
2563
2564#[cfg(not(no_global_oom_handling))]
2565#[stable(feature = "herd_cows", since = "1.19.0")]
2566impl<'a> Extend<Cow<'a, str>> for String {
2567    fn extend<I: IntoIterator<Item = Cow<'a, str>>>(&mut self, iter: I) {
2568        iter.into_iter().for_each(move |s| self.push_str(&s));
2569    }
2570
2571    #[inline]
2572    fn extend_one(&mut self, s: Cow<'a, str>) {
2573        self.push_str(&s);
2574    }
2575}
2576
2577#[cfg(not(no_global_oom_handling))]
2578#[unstable(feature = "ascii_char", issue = "110998")]
2579impl Extend<core::ascii::Char> for String {
2580    #[inline]
2581    fn extend<I: IntoIterator<Item = core::ascii::Char>>(&mut self, iter: I) {
2582        self.vec.extend(iter.into_iter().map(|c| c.to_u8()));
2583    }
2584
2585    #[inline]
2586    fn extend_one(&mut self, c: core::ascii::Char) {
2587        self.vec.push(c.to_u8());
2588    }
2589}
2590
2591#[cfg(not(no_global_oom_handling))]
2592#[unstable(feature = "ascii_char", issue = "110998")]
2593impl<'a> Extend<&'a core::ascii::Char> for String {
2594    #[inline]
2595    fn extend<I: IntoIterator<Item = &'a core::ascii::Char>>(&mut self, iter: I) {
2596        self.extend(iter.into_iter().cloned());
2597    }
2598
2599    #[inline]
2600    fn extend_one(&mut self, c: &'a core::ascii::Char) {
2601        self.vec.push(c.to_u8());
2602    }
2603}
2604
2605/// A convenience impl that delegates to the impl for `&str`.
2606///
2607/// # Examples
2608///
2609/// ```
2610/// assert_eq!(String::from("Hello world").find("world"), Some(6));
2611/// ```
2612#[unstable(
2613    feature = "pattern",
2614    reason = "API not fully fleshed out and ready to be stabilized",
2615    issue = "27721"
2616)]
2617impl<'b> Pattern for &'b String {
2618    type Searcher<'a> = <&'b str as Pattern>::Searcher<'a>;
2619
2620    fn into_searcher(self, haystack: &str) -> <&'b str as Pattern>::Searcher<'_> {
2621        self[..].into_searcher(haystack)
2622    }
2623
2624    #[inline]
2625    fn is_contained_in(self, haystack: &str) -> bool {
2626        self[..].is_contained_in(haystack)
2627    }
2628
2629    #[inline]
2630    fn is_prefix_of(self, haystack: &str) -> bool {
2631        self[..].is_prefix_of(haystack)
2632    }
2633
2634    #[inline]
2635    fn strip_prefix_of(self, haystack: &str) -> Option<&str> {
2636        self[..].strip_prefix_of(haystack)
2637    }
2638
2639    #[inline]
2640    fn is_suffix_of<'a>(self, haystack: &'a str) -> bool
2641    where
2642        Self::Searcher<'a>: core::str::pattern::ReverseSearcher<'a>,
2643    {
2644        self[..].is_suffix_of(haystack)
2645    }
2646
2647    #[inline]
2648    fn strip_suffix_of<'a>(self, haystack: &'a str) -> Option<&'a str>
2649    where
2650        Self::Searcher<'a>: core::str::pattern::ReverseSearcher<'a>,
2651    {
2652        self[..].strip_suffix_of(haystack)
2653    }
2654
2655    #[inline]
2656    fn as_utf8_pattern(&self) -> Option<Utf8Pattern<'_>> {
2657        Some(Utf8Pattern::StringPattern(self.as_bytes()))
2658    }
2659}
2660
2661macro_rules! impl_eq {
2662    ($lhs:ty, $rhs: ty) => {
2663        #[stable(feature = "rust1", since = "1.0.0")]
2664        impl PartialEq<$rhs> for $lhs {
2665            #[inline]
2666            fn eq(&self, other: &$rhs) -> bool {
2667                PartialEq::eq(&self[..], &other[..])
2668            }
2669            #[inline]
2670            fn ne(&self, other: &$rhs) -> bool {
2671                PartialEq::ne(&self[..], &other[..])
2672            }
2673        }
2674
2675        #[stable(feature = "rust1", since = "1.0.0")]
2676        impl PartialEq<$lhs> for $rhs {
2677            #[inline]
2678            fn eq(&self, other: &$lhs) -> bool {
2679                PartialEq::eq(&self[..], &other[..])
2680            }
2681            #[inline]
2682            fn ne(&self, other: &$lhs) -> bool {
2683                PartialEq::ne(&self[..], &other[..])
2684            }
2685        }
2686    };
2687}
2688
2689impl_eq! { String, str }
2690impl_eq! { String, &str }
2691#[cfg(not(no_global_oom_handling))]
2692impl_eq! { Cow<'_, str>, str }
2693#[cfg(not(no_global_oom_handling))]
2694impl_eq! { Cow<'_, str>, &'_ str }
2695#[cfg(not(no_global_oom_handling))]
2696impl_eq! { Cow<'_, str>, String }
2697
2698#[stable(feature = "rust1", since = "1.0.0")]
2699#[rustc_const_unstable(feature = "const_default", issue = "143894")]
2700impl const Default for String {
2701    /// Creates an empty `String`.
2702    #[inline]
2703    fn default() -> String {
2704        String::new()
2705    }
2706}
2707
2708#[stable(feature = "rust1", since = "1.0.0")]
2709impl fmt::Display for String {
2710    #[inline]
2711    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2712        fmt::Display::fmt(&**self, f)
2713    }
2714}
2715
2716#[stable(feature = "rust1", since = "1.0.0")]
2717impl fmt::Debug for String {
2718    #[inline]
2719    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2720        fmt::Debug::fmt(&**self, f)
2721    }
2722}
2723
2724#[stable(feature = "rust1", since = "1.0.0")]
2725impl hash::Hash for String {
2726    #[inline]
2727    fn hash<H: hash::Hasher>(&self, hasher: &mut H) {
2728        (**self).hash(hasher)
2729    }
2730}
2731
2732/// Implements the `+` operator for concatenating two strings.
2733///
2734/// This consumes the `String` on the left-hand side and re-uses its buffer (growing it if
2735/// necessary). This is done to avoid allocating a new `String` and copying the entire contents on
2736/// every operation, which would lead to *O*(*n*^2) running time when building an *n*-byte string by
2737/// repeated concatenation.
2738///
2739/// The string on the right-hand side is only borrowed; its contents are copied into the returned
2740/// `String`.
2741///
2742/// # Examples
2743///
2744/// Concatenating two `String`s takes the first by value and borrows the second:
2745///
2746/// ```
2747/// let a = String::from("hello");
2748/// let b = String::from(" world");
2749/// let c = a + &b;
2750/// // `a` is moved and can no longer be used here.
2751/// ```
2752///
2753/// If you want to keep using the first `String`, you can clone it and append to the clone instead:
2754///
2755/// ```
2756/// let a = String::from("hello");
2757/// let b = String::from(" world");
2758/// let c = a.clone() + &b;
2759/// // `a` is still valid here.
2760/// ```
2761///
2762/// Concatenating `&str` slices can be done by converting the first to a `String`:
2763///
2764/// ```
2765/// let a = "hello";
2766/// let b = " world";
2767/// let c = a.to_string() + b;
2768/// ```
2769#[cfg(not(no_global_oom_handling))]
2770#[stable(feature = "rust1", since = "1.0.0")]
2771impl Add<&str> for String {
2772    type Output = String;
2773
2774    #[inline]
2775    fn add(mut self, other: &str) -> String {
2776        self.push_str(other);
2777        self
2778    }
2779}
2780
2781/// Implements the `+=` operator for appending to a `String`.
2782///
2783/// This has the same behavior as the [`push_str`][String::push_str] method.
2784#[cfg(not(no_global_oom_handling))]
2785#[stable(feature = "stringaddassign", since = "1.12.0")]
2786impl AddAssign<&str> for String {
2787    #[inline]
2788    fn add_assign(&mut self, other: &str) {
2789        self.push_str(other);
2790    }
2791}
2792
2793#[stable(feature = "rust1", since = "1.0.0")]
2794impl<I> ops::Index<I> for String
2795where
2796    I: slice::SliceIndex<str>,
2797{
2798    type Output = I::Output;
2799
2800    #[inline]
2801    fn index(&self, index: I) -> &I::Output {
2802        index.index(self.as_str())
2803    }
2804}
2805
2806#[stable(feature = "rust1", since = "1.0.0")]
2807impl<I> ops::IndexMut<I> for String
2808where
2809    I: slice::SliceIndex<str>,
2810{
2811    #[inline]
2812    fn index_mut(&mut self, index: I) -> &mut I::Output {
2813        index.index_mut(self.as_mut_str())
2814    }
2815}
2816
2817#[stable(feature = "rust1", since = "1.0.0")]
2818impl ops::Deref for String {
2819    type Target = str;
2820
2821    #[inline]
2822    fn deref(&self) -> &str {
2823        self.as_str()
2824    }
2825}
2826
2827#[unstable(feature = "deref_pure_trait", issue = "87121")]
2828unsafe impl ops::DerefPure for String {}
2829
2830#[stable(feature = "derefmut_for_string", since = "1.3.0")]
2831impl ops::DerefMut for String {
2832    #[inline]
2833    fn deref_mut(&mut self) -> &mut str {
2834        self.as_mut_str()
2835    }
2836}
2837
2838/// A type alias for [`Infallible`].
2839///
2840/// This alias exists for backwards compatibility, and may be eventually deprecated.
2841///
2842/// [`Infallible`]: core::convert::Infallible "convert::Infallible"
2843#[stable(feature = "str_parse_error", since = "1.5.0")]
2844pub type ParseError = core::convert::Infallible;
2845
2846#[cfg(not(no_global_oom_handling))]
2847#[stable(feature = "rust1", since = "1.0.0")]
2848impl FromStr for String {
2849    type Err = core::convert::Infallible;
2850    #[inline]
2851    fn from_str(s: &str) -> Result<String, Self::Err> {
2852        Ok(String::from(s))
2853    }
2854}
2855
2856/// A trait for converting a value to a `String`.
2857///
2858/// This trait is automatically implemented for any type which implements the
2859/// [`Display`] trait. As such, `ToString` shouldn't be implemented directly:
2860/// [`Display`] should be implemented instead, and you get the `ToString`
2861/// implementation for free.
2862///
2863/// [`Display`]: fmt::Display
2864#[rustc_diagnostic_item = "ToString"]
2865#[stable(feature = "rust1", since = "1.0.0")]
2866pub trait ToString {
2867    /// Converts the given value to a `String`.
2868    ///
2869    /// # Examples
2870    ///
2871    /// ```
2872    /// let i = 5;
2873    /// let five = String::from("5");
2874    ///
2875    /// assert_eq!(five, i.to_string());
2876    /// ```
2877    #[rustc_conversion_suggestion]
2878    #[stable(feature = "rust1", since = "1.0.0")]
2879    #[rustc_diagnostic_item = "to_string_method"]
2880    fn to_string(&self) -> String;
2881}
2882
2883/// # Panics
2884///
2885/// In this implementation, the `to_string` method panics
2886/// if the `Display` implementation returns an error.
2887/// This indicates an incorrect `Display` implementation
2888/// since `fmt::Write for String` never returns an error itself.
2889#[cfg(not(no_global_oom_handling))]
2890#[stable(feature = "rust1", since = "1.0.0")]
2891impl<T: fmt::Display + ?Sized> ToString for T {
2892    #[inline]
2893    fn to_string(&self) -> String {
2894        <Self as SpecToString>::spec_to_string(self)
2895    }
2896}
2897
2898#[cfg(not(no_global_oom_handling))]
2899trait SpecToString {
2900    fn spec_to_string(&self) -> String;
2901}
2902
2903#[cfg(not(no_global_oom_handling))]
2904impl<T: fmt::Display + ?Sized> SpecToString for T {
2905    // A common guideline is to not inline generic functions. However,
2906    // removing `#[inline]` from this method causes non-negligible regressions.
2907    // See <https://github.com/rust-lang/rust/pull/74852>, the last attempt
2908    // to try to remove it.
2909    #[inline]
2910    default fn spec_to_string(&self) -> String {
2911        let mut buf = String::new();
2912        let mut formatter =
2913            core::fmt::Formatter::new(&mut buf, core::fmt::FormattingOptions::new());
2914        // Bypass format_args!() to avoid write_str with zero-length strs
2915        fmt::Display::fmt(self, &mut formatter)
2916            .expect("a Display implementation returned an error unexpectedly");
2917        buf
2918    }
2919}
2920
2921#[cfg(not(no_global_oom_handling))]
2922impl SpecToString for core::ascii::Char {
2923    #[inline]
2924    fn spec_to_string(&self) -> String {
2925        self.as_str().to_owned()
2926    }
2927}
2928
2929#[cfg(not(no_global_oom_handling))]
2930impl SpecToString for char {
2931    #[inline]
2932    fn spec_to_string(&self) -> String {
2933        String::from(self.encode_utf8(&mut [0; char::MAX_LEN_UTF8]))
2934    }
2935}
2936
2937#[cfg(not(no_global_oom_handling))]
2938impl SpecToString for bool {
2939    #[inline]
2940    fn spec_to_string(&self) -> String {
2941        String::from(if *self { "true" } else { "false" })
2942    }
2943}
2944
2945macro_rules! impl_to_string {
2946    ($($signed:ident, $unsigned:ident,)*) => {
2947        $(
2948        #[cfg(not(no_global_oom_handling))]
2949        #[cfg(not(feature = "optimize_for_size"))]
2950        impl SpecToString for $signed {
2951            #[inline]
2952            fn spec_to_string(&self) -> String {
2953                const SIZE: usize = $signed::MAX.ilog10() as usize + 1;
2954                let mut buf = [core::mem::MaybeUninit::<u8>::uninit(); SIZE];
2955                // Only difference between signed and unsigned are these 8 lines.
2956                let mut out;
2957                if *self < 0 {
2958                    out = String::with_capacity(SIZE + 1);
2959                    out.push('-');
2960                } else {
2961                    out = String::with_capacity(SIZE);
2962                }
2963
2964                // SAFETY: `buf` is always big enough to contain all the digits.
2965                unsafe { out.push_str(self.unsigned_abs()._fmt(&mut buf)); }
2966                out
2967            }
2968        }
2969        #[cfg(not(no_global_oom_handling))]
2970        #[cfg(not(feature = "optimize_for_size"))]
2971        impl SpecToString for $unsigned {
2972            #[inline]
2973            fn spec_to_string(&self) -> String {
2974                const SIZE: usize = $unsigned::MAX.ilog10() as usize + 1;
2975                let mut buf = [core::mem::MaybeUninit::<u8>::uninit(); SIZE];
2976
2977                // SAFETY: `buf` is always big enough to contain all the digits.
2978                unsafe { self._fmt(&mut buf).to_string() }
2979            }
2980        }
2981        )*
2982    }
2983}
2984
2985impl_to_string! {
2986    i8, u8,
2987    i16, u16,
2988    i32, u32,
2989    i64, u64,
2990    isize, usize,
2991    i128, u128,
2992}
2993
2994#[cfg(not(no_global_oom_handling))]
2995#[cfg(feature = "optimize_for_size")]
2996impl SpecToString for u8 {
2997    #[inline]
2998    fn spec_to_string(&self) -> String {
2999        let mut buf = String::with_capacity(3);
3000        let mut n = *self;
3001        if n >= 10 {
3002            if n >= 100 {
3003                buf.push((b'0' + n / 100) as char);
3004                n %= 100;
3005            }
3006            buf.push((b'0' + n / 10) as char);
3007            n %= 10;
3008        }
3009        buf.push((b'0' + n) as char);
3010        buf
3011    }
3012}
3013
3014#[cfg(not(no_global_oom_handling))]
3015#[cfg(feature = "optimize_for_size")]
3016impl SpecToString for i8 {
3017    #[inline]
3018    fn spec_to_string(&self) -> String {
3019        let mut buf = String::with_capacity(4);
3020        if self.is_negative() {
3021            buf.push('-');
3022        }
3023        let mut n = self.unsigned_abs();
3024        if n >= 10 {
3025            if n >= 100 {
3026                buf.push('1');
3027                n -= 100;
3028            }
3029            buf.push((b'0' + n / 10) as char);
3030            n %= 10;
3031        }
3032        buf.push((b'0' + n) as char);
3033        buf
3034    }
3035}
3036
3037#[cfg(not(no_global_oom_handling))]
3038macro_rules! to_string_str {
3039    {$($type:ty,)*} => {
3040        $(
3041            impl SpecToString for $type {
3042                #[inline]
3043                fn spec_to_string(&self) -> String {
3044                    let s: &str = self;
3045                    String::from(s)
3046                }
3047            }
3048        )*
3049    };
3050}
3051
3052#[cfg(not(no_global_oom_handling))]
3053to_string_str! {
3054    Cow<'_, str>,
3055    String,
3056    // Generic/generated code can sometimes have multiple, nested references
3057    // for strings, including `&&&str`s that would never be written
3058    // by hand.
3059    &&&&&&&&&&&&str,
3060    &&&&&&&&&&&str,
3061    &&&&&&&&&&str,
3062    &&&&&&&&&str,
3063    &&&&&&&&str,
3064    &&&&&&&str,
3065    &&&&&&str,
3066    &&&&&str,
3067    &&&&str,
3068    &&&str,
3069    &&str,
3070    &str,
3071    str,
3072}
3073
3074#[cfg(not(no_global_oom_handling))]
3075impl SpecToString for fmt::Arguments<'_> {
3076    #[inline]
3077    fn spec_to_string(&self) -> String {
3078        crate::fmt::format(*self)
3079    }
3080}
3081
3082#[stable(feature = "rust1", since = "1.0.0")]
3083impl AsRef<str> for String {
3084    #[inline]
3085    fn as_ref(&self) -> &str {
3086        self
3087    }
3088}
3089
3090#[stable(feature = "string_as_mut", since = "1.43.0")]
3091impl AsMut<str> for String {
3092    #[inline]
3093    fn as_mut(&mut self) -> &mut str {
3094        self
3095    }
3096}
3097
3098#[stable(feature = "rust1", since = "1.0.0")]
3099impl AsRef<[u8]> for String {
3100    #[inline]
3101    fn as_ref(&self) -> &[u8] {
3102        self.as_bytes()
3103    }
3104}
3105
3106#[cfg(not(no_global_oom_handling))]
3107#[stable(feature = "rust1", since = "1.0.0")]
3108impl From<&str> for String {
3109    /// Converts a `&str` into a [`String`].
3110    ///
3111    /// The result is allocated on the heap.
3112    #[inline]
3113    fn from(s: &str) -> String {
3114        s.to_owned()
3115    }
3116}
3117
3118#[cfg(not(no_global_oom_handling))]
3119#[stable(feature = "from_mut_str_for_string", since = "1.44.0")]
3120impl From<&mut str> for String {
3121    /// Converts a `&mut str` into a [`String`].
3122    ///
3123    /// The result is allocated on the heap.
3124    #[inline]
3125    fn from(s: &mut str) -> String {
3126        s.to_owned()
3127    }
3128}
3129
3130#[cfg(not(no_global_oom_handling))]
3131#[stable(feature = "from_ref_string", since = "1.35.0")]
3132impl From<&String> for String {
3133    /// Converts a `&String` into a [`String`].
3134    ///
3135    /// This clones `s` and returns the clone.
3136    #[inline]
3137    fn from(s: &String) -> String {
3138        s.clone()
3139    }
3140}
3141
3142// note: test pulls in std, which causes errors here
3143#[stable(feature = "string_from_box", since = "1.18.0")]
3144impl From<Box<str>> for String {
3145    /// Converts the given boxed `str` slice to a [`String`].
3146    /// It is notable that the `str` slice is owned.
3147    ///
3148    /// # Examples
3149    ///
3150    /// ```
3151    /// let s1: String = String::from("hello world");
3152    /// let s2: Box<str> = s1.into_boxed_str();
3153    /// let s3: String = String::from(s2);
3154    ///
3155    /// assert_eq!("hello world", s3)
3156    /// ```
3157    fn from(s: Box<str>) -> String {
3158        s.into_string()
3159    }
3160}
3161
3162#[cfg(not(no_global_oom_handling))]
3163#[stable(feature = "box_from_str", since = "1.20.0")]
3164impl From<String> for Box<str> {
3165    /// Converts the given [`String`] to a boxed `str` slice that is owned.
3166    ///
3167    /// # Examples
3168    ///
3169    /// ```
3170    /// let s1: String = String::from("hello world");
3171    /// let s2: Box<str> = Box::from(s1);
3172    /// let s3: String = String::from(s2);
3173    ///
3174    /// assert_eq!("hello world", s3)
3175    /// ```
3176    fn from(s: String) -> Box<str> {
3177        s.into_boxed_str()
3178    }
3179}
3180
3181#[cfg(not(no_global_oom_handling))]
3182#[stable(feature = "string_from_cow_str", since = "1.14.0")]
3183impl<'a> From<Cow<'a, str>> for String {
3184    /// Converts a clone-on-write string to an owned
3185    /// instance of [`String`].
3186    ///
3187    /// This extracts the owned string,
3188    /// clones the string if it is not already owned.
3189    ///
3190    /// # Example
3191    ///
3192    /// ```
3193    /// # use std::borrow::Cow;
3194    /// // If the string is not owned...
3195    /// let cow: Cow<'_, str> = Cow::Borrowed("eggplant");
3196    /// // It will allocate on the heap and copy the string.
3197    /// let owned: String = String::from(cow);
3198    /// assert_eq!(&owned[..], "eggplant");
3199    /// ```
3200    fn from(s: Cow<'a, str>) -> String {
3201        s.into_owned()
3202    }
3203}
3204
3205#[cfg(not(no_global_oom_handling))]
3206#[stable(feature = "rust1", since = "1.0.0")]
3207impl<'a> From<&'a str> for Cow<'a, str> {
3208    /// Converts a string slice into a [`Borrowed`] variant.
3209    /// No heap allocation is performed, and the string
3210    /// is not copied.
3211    ///
3212    /// # Example
3213    ///
3214    /// ```
3215    /// # use std::borrow::Cow;
3216    /// assert_eq!(Cow::from("eggplant"), Cow::Borrowed("eggplant"));
3217    /// ```
3218    ///
3219    /// [`Borrowed`]: crate::borrow::Cow::Borrowed "borrow::Cow::Borrowed"
3220    #[inline]
3221    fn from(s: &'a str) -> Cow<'a, str> {
3222        Cow::Borrowed(s)
3223    }
3224}
3225
3226#[cfg(not(no_global_oom_handling))]
3227#[stable(feature = "rust1", since = "1.0.0")]
3228impl<'a> From<String> for Cow<'a, str> {
3229    /// Converts a [`String`] into an [`Owned`] variant.
3230    /// No heap allocation is performed, and the string
3231    /// is not copied.
3232    ///
3233    /// # Example
3234    ///
3235    /// ```
3236    /// # use std::borrow::Cow;
3237    /// let s = "eggplant".to_string();
3238    /// let s2 = "eggplant".to_string();
3239    /// assert_eq!(Cow::from(s), Cow::<'static, str>::Owned(s2));
3240    /// ```
3241    ///
3242    /// [`Owned`]: crate::borrow::Cow::Owned "borrow::Cow::Owned"
3243    #[inline]
3244    fn from(s: String) -> Cow<'a, str> {
3245        Cow::Owned(s)
3246    }
3247}
3248
3249#[cfg(not(no_global_oom_handling))]
3250#[stable(feature = "cow_from_string_ref", since = "1.28.0")]
3251impl<'a> From<&'a String> for Cow<'a, str> {
3252    /// Converts a [`String`] reference into a [`Borrowed`] variant.
3253    /// No heap allocation is performed, and the string
3254    /// is not copied.
3255    ///
3256    /// # Example
3257    ///
3258    /// ```
3259    /// # use std::borrow::Cow;
3260    /// let s = "eggplant".to_string();
3261    /// assert_eq!(Cow::from(&s), Cow::Borrowed("eggplant"));
3262    /// ```
3263    ///
3264    /// [`Borrowed`]: crate::borrow::Cow::Borrowed "borrow::Cow::Borrowed"
3265    #[inline]
3266    fn from(s: &'a String) -> Cow<'a, str> {
3267        Cow::Borrowed(s.as_str())
3268    }
3269}
3270
3271#[cfg(not(no_global_oom_handling))]
3272#[stable(feature = "cow_str_from_iter", since = "1.12.0")]
3273impl<'a> FromIterator<char> for Cow<'a, str> {
3274    fn from_iter<I: IntoIterator<Item = char>>(it: I) -> Cow<'a, str> {
3275        Cow::Owned(FromIterator::from_iter(it))
3276    }
3277}
3278
3279#[cfg(not(no_global_oom_handling))]
3280#[stable(feature = "cow_str_from_iter", since = "1.12.0")]
3281impl<'a, 'b> FromIterator<&'b str> for Cow<'a, str> {
3282    fn from_iter<I: IntoIterator<Item = &'b str>>(it: I) -> Cow<'a, str> {
3283        Cow::Owned(FromIterator::from_iter(it))
3284    }
3285}
3286
3287#[cfg(not(no_global_oom_handling))]
3288#[stable(feature = "cow_str_from_iter", since = "1.12.0")]
3289impl<'a> FromIterator<String> for Cow<'a, str> {
3290    fn from_iter<I: IntoIterator<Item = String>>(it: I) -> Cow<'a, str> {
3291        Cow::Owned(FromIterator::from_iter(it))
3292    }
3293}
3294
3295#[cfg(not(no_global_oom_handling))]
3296#[unstable(feature = "ascii_char", issue = "110998")]
3297impl<'a> FromIterator<core::ascii::Char> for Cow<'a, str> {
3298    fn from_iter<T: IntoIterator<Item = core::ascii::Char>>(it: T) -> Self {
3299        Cow::Owned(FromIterator::from_iter(it))
3300    }
3301}
3302
3303#[stable(feature = "from_string_for_vec_u8", since = "1.14.0")]
3304impl From<String> for Vec<u8> {
3305    /// Converts the given [`String`] to a vector [`Vec`] that holds values of type [`u8`].
3306    ///
3307    /// # Examples
3308    ///
3309    /// ```
3310    /// let s1 = String::from("hello world");
3311    /// let v1 = Vec::from(s1);
3312    ///
3313    /// for b in v1 {
3314    ///     println!("{b}");
3315    /// }
3316    /// ```
3317    fn from(string: String) -> Vec<u8> {
3318        string.into_bytes()
3319    }
3320}
3321
3322#[stable(feature = "try_from_vec_u8_for_string", since = "1.87.0")]
3323impl TryFrom<Vec<u8>> for String {
3324    type Error = FromUtf8Error;
3325    /// Converts the given [`Vec<u8>`] into a  [`String`] if it contains valid UTF-8 data.
3326    ///
3327    /// # Examples
3328    ///
3329    /// ```
3330    /// let s1 = b"hello world".to_vec();
3331    /// let v1 = String::try_from(s1).unwrap();
3332    /// assert_eq!(v1, "hello world");
3333    ///
3334    /// ```
3335    fn try_from(bytes: Vec<u8>) -> Result<Self, Self::Error> {
3336        Self::from_utf8(bytes)
3337    }
3338}
3339
3340#[cfg(not(no_global_oom_handling))]
3341#[stable(feature = "rust1", since = "1.0.0")]
3342impl fmt::Write for String {
3343    #[inline]
3344    fn write_str(&mut self, s: &str) -> fmt::Result {
3345        self.push_str(s);
3346        Ok(())
3347    }
3348
3349    #[inline]
3350    fn write_char(&mut self, c: char) -> fmt::Result {
3351        self.push(c);
3352        Ok(())
3353    }
3354}
3355
3356/// An iterator over the [`char`]s of a string.
3357///
3358/// This struct is created by the [`into_chars`] method on [`String`].
3359/// See its documentation for more.
3360///
3361/// [`char`]: prim@char
3362/// [`into_chars`]: String::into_chars
3363#[cfg_attr(not(no_global_oom_handling), derive(Clone))]
3364#[must_use = "iterators are lazy and do nothing unless consumed"]
3365#[unstable(feature = "string_into_chars", issue = "133125")]
3366pub struct IntoChars {
3367    bytes: vec::IntoIter<u8>,
3368}
3369
3370#[unstable(feature = "string_into_chars", issue = "133125")]
3371impl fmt::Debug for IntoChars {
3372    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3373        f.debug_tuple("IntoChars").field(&self.as_str()).finish()
3374    }
3375}
3376
3377impl IntoChars {
3378    /// Views the underlying data as a subslice of the original data.
3379    ///
3380    /// # Examples
3381    ///
3382    /// ```
3383    /// #![feature(string_into_chars)]
3384    ///
3385    /// let mut chars = String::from("abc").into_chars();
3386    ///
3387    /// assert_eq!(chars.as_str(), "abc");
3388    /// chars.next();
3389    /// assert_eq!(chars.as_str(), "bc");
3390    /// chars.next();
3391    /// chars.next();
3392    /// assert_eq!(chars.as_str(), "");
3393    /// ```
3394    #[unstable(feature = "string_into_chars", issue = "133125")]
3395    #[must_use]
3396    #[inline]
3397    pub fn as_str(&self) -> &str {
3398        // SAFETY: `bytes` is a valid UTF-8 string.
3399        unsafe { str::from_utf8_unchecked(self.bytes.as_slice()) }
3400    }
3401
3402    /// Consumes the `IntoChars`, returning the remaining string.
3403    ///
3404    /// # Examples
3405    ///
3406    /// ```
3407    /// #![feature(string_into_chars)]
3408    ///
3409    /// let chars = String::from("abc").into_chars();
3410    /// assert_eq!(chars.into_string(), "abc");
3411    ///
3412    /// let mut chars = String::from("def").into_chars();
3413    /// chars.next();
3414    /// assert_eq!(chars.into_string(), "ef");
3415    /// ```
3416    #[cfg(not(no_global_oom_handling))]
3417    #[unstable(feature = "string_into_chars", issue = "133125")]
3418    #[inline]
3419    pub fn into_string(self) -> String {
3420        // Safety: `bytes` are kept in UTF-8 form, only removing whole `char`s at a time.
3421        unsafe { String::from_utf8_unchecked(self.bytes.collect()) }
3422    }
3423
3424    #[inline]
3425    fn iter(&self) -> CharIndices<'_> {
3426        self.as_str().char_indices()
3427    }
3428}
3429
3430#[unstable(feature = "string_into_chars", issue = "133125")]
3431impl Iterator for IntoChars {
3432    type Item = char;
3433
3434    #[inline]
3435    fn next(&mut self) -> Option<char> {
3436        let mut iter = self.iter();
3437        match iter.next() {
3438            None => None,
3439            Some((_, ch)) => {
3440                let offset = iter.offset();
3441                // `offset` is a valid index.
3442                let _ = self.bytes.advance_by(offset);
3443                Some(ch)
3444            }
3445        }
3446    }
3447
3448    #[inline]
3449    fn count(self) -> usize {
3450        self.iter().count()
3451    }
3452
3453    #[inline]
3454    fn size_hint(&self) -> (usize, Option<usize>) {
3455        self.iter().size_hint()
3456    }
3457
3458    #[inline]
3459    fn last(mut self) -> Option<char> {
3460        self.next_back()
3461    }
3462}
3463
3464#[unstable(feature = "string_into_chars", issue = "133125")]
3465impl DoubleEndedIterator for IntoChars {
3466    #[inline]
3467    fn next_back(&mut self) -> Option<char> {
3468        let len = self.as_str().len();
3469        let mut iter = self.iter();
3470        match iter.next_back() {
3471            None => None,
3472            Some((idx, ch)) => {
3473                // `idx` is a valid index.
3474                let _ = self.bytes.advance_back_by(len - idx);
3475                Some(ch)
3476            }
3477        }
3478    }
3479}
3480
3481#[unstable(feature = "string_into_chars", issue = "133125")]
3482impl FusedIterator for IntoChars {}
3483
3484/// A draining iterator for `String`.
3485///
3486/// This struct is created by the [`drain`] method on [`String`]. See its
3487/// documentation for more.
3488///
3489/// [`drain`]: String::drain
3490#[stable(feature = "drain", since = "1.6.0")]
3491pub struct Drain<'a> {
3492    /// Will be used as &'a mut String in the destructor
3493    string: *mut String,
3494    /// Start of part to remove
3495    start: usize,
3496    /// End of part to remove
3497    end: usize,
3498    /// Current remaining range to remove
3499    iter: Chars<'a>,
3500}
3501
3502#[stable(feature = "collection_debug", since = "1.17.0")]
3503impl fmt::Debug for Drain<'_> {
3504    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
3505        f.debug_tuple("Drain").field(&self.as_str()).finish()
3506    }
3507}
3508
3509#[stable(feature = "drain", since = "1.6.0")]
3510unsafe impl Sync for Drain<'_> {}
3511#[stable(feature = "drain", since = "1.6.0")]
3512unsafe impl Send for Drain<'_> {}
3513
3514#[stable(feature = "drain", since = "1.6.0")]
3515impl Drop for Drain<'_> {
3516    fn drop(&mut self) {
3517        unsafe {
3518            // Use Vec::drain. "Reaffirm" the bounds checks to avoid
3519            // panic code being inserted again.
3520            let self_vec = (*self.string).as_mut_vec();
3521            if self.start <= self.end && self.end <= self_vec.len() {
3522                self_vec.drain(self.start..self.end);
3523            }
3524        }
3525    }
3526}
3527
3528impl<'a> Drain<'a> {
3529    /// Returns the remaining (sub)string of this iterator as a slice.
3530    ///
3531    /// # Examples
3532    ///
3533    /// ```
3534    /// let mut s = String::from("abc");
3535    /// let mut drain = s.drain(..);
3536    /// assert_eq!(drain.as_str(), "abc");
3537    /// let _ = drain.next().unwrap();
3538    /// assert_eq!(drain.as_str(), "bc");
3539    /// ```
3540    #[must_use]
3541    #[stable(feature = "string_drain_as_str", since = "1.55.0")]
3542    pub fn as_str(&self) -> &str {
3543        self.iter.as_str()
3544    }
3545}
3546
3547#[stable(feature = "string_drain_as_str", since = "1.55.0")]
3548impl<'a> AsRef<str> for Drain<'a> {
3549    fn as_ref(&self) -> &str {
3550        self.as_str()
3551    }
3552}
3553
3554#[stable(feature = "string_drain_as_str", since = "1.55.0")]
3555impl<'a> AsRef<[u8]> for Drain<'a> {
3556    fn as_ref(&self) -> &[u8] {
3557        self.as_str().as_bytes()
3558    }
3559}
3560
3561#[stable(feature = "drain", since = "1.6.0")]
3562impl Iterator for Drain<'_> {
3563    type Item = char;
3564
3565    #[inline]
3566    fn next(&mut self) -> Option<char> {
3567        self.iter.next()
3568    }
3569
3570    fn size_hint(&self) -> (usize, Option<usize>) {
3571        self.iter.size_hint()
3572    }
3573
3574    #[inline]
3575    fn last(mut self) -> Option<char> {
3576        self.next_back()
3577    }
3578}
3579
3580#[stable(feature = "drain", since = "1.6.0")]
3581impl DoubleEndedIterator for Drain<'_> {
3582    #[inline]
3583    fn next_back(&mut self) -> Option<char> {
3584        self.iter.next_back()
3585    }
3586}
3587
3588#[stable(feature = "fused", since = "1.26.0")]
3589impl FusedIterator for Drain<'_> {}
3590
3591#[cfg(not(no_global_oom_handling))]
3592#[stable(feature = "from_char_for_string", since = "1.46.0")]
3593impl From<char> for String {
3594    /// Allocates an owned [`String`] from a single character.
3595    ///
3596    /// # Example
3597    /// ```rust
3598    /// let c: char = 'a';
3599    /// let s: String = String::from(c);
3600    /// assert_eq!("a", &s[..]);
3601    /// ```
3602    #[inline]
3603    fn from(c: char) -> Self {
3604        c.to_string()
3605    }
3606}
````