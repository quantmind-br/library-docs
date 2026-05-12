---
title: mod.rs - source
url: https://doc.rust-lang.org/src/core/str/mod.rs.html#157
source: crawler
fetched_at: 2026-05-06T21:22:27.907231037-03:00
rendered_js: false
word_count: 13579
summary: This module provides fundamental string manipulation capabilities and UTF-8 validation utilities for the Rust standard library.
tags:
    - rust
    - string-manipulation
    - utf8
    - core-library
    - slice
    - unicode
category: reference
---

## core/str/ mod.rs

````rust
1//! String manipulation.
2//!
3//! For more details, see the [`std::str`] module.
4//!
5//! [`std::str`]: ../../std/str/index.html
6
7#![stable(feature = "rust1", since = "1.0.0")]
8
9mod converts;
10mod count;
11mod error;
12mod iter;
13mod traits;
14mod validations;
15
16use self::pattern::{DoubleEndedSearcher, Pattern, ReverseSearcher, Searcher};
17use crate::char::{self, EscapeDebugExtArgs};
18use crate::ops::Range;
19use crate::slice::{self, SliceIndex};
20use crate::ub_checks::assert_unsafe_precondition;
21use crate::{ascii, mem};
22
23pub mod pattern;
24
25mod lossy;
26#[unstable(feature = "str_from_raw_parts", issue = "119206")]
27pub use converts::{from_raw_parts, from_raw_parts_mut};
28#[stable(feature = "rust1", since = "1.0.0")]
29pub use converts::{from_utf8, from_utf8_unchecked};
30#[stable(feature = "str_mut_extras", since = "1.20.0")]
31pub use converts::{from_utf8_mut, from_utf8_unchecked_mut};
32#[stable(feature = "rust1", since = "1.0.0")]
33pub use error::{ParseBoolError, Utf8Error};
34#[stable(feature = "encode_utf16", since = "1.8.0")]
35pub use iter::EncodeUtf16;
36#[stable(feature = "rust1", since = "1.0.0")]
37#[allow(deprecated)]
38pub use iter::LinesAny;
39#[stable(feature = "split_ascii_whitespace", since = "1.34.0")]
40pub use iter::SplitAsciiWhitespace;
41#[stable(feature = "split_inclusive", since = "1.51.0")]
42pub use iter::SplitInclusive;
43#[stable(feature = "rust1", since = "1.0.0")]
44pub use iter::{Bytes, CharIndices, Chars, Lines, SplitWhitespace};
45#[stable(feature = "str_escape", since = "1.34.0")]
46pub use iter::{EscapeDebug, EscapeDefault, EscapeUnicode};
47#[stable(feature = "str_match_indices", since = "1.5.0")]
48pub use iter::{MatchIndices, RMatchIndices};
49use iter::{MatchIndicesInternal, MatchesInternal, SplitInternal, SplitNInternal};
50#[stable(feature = "str_matches", since = "1.2.0")]
51pub use iter::{Matches, RMatches};
52#[stable(feature = "rust1", since = "1.0.0")]
53pub use iter::{RSplit, RSplitTerminator, Split, SplitTerminator};
54#[stable(feature = "rust1", since = "1.0.0")]
55pub use iter::{RSplitN, SplitN};
56#[stable(feature = "utf8_chunks", since = "1.79.0")]
57pub use lossy::{Utf8Chunk, Utf8Chunks};
58#[stable(feature = "rust1", since = "1.0.0")]
59pub use traits::FromStr;
60#[unstable(feature = "str_internals", issue = "none")]
61pub use validations::{next_code_point, utf8_char_width};
62
63#[inline(never)]
64#[cold]
65#[track_caller]
66#[rustc_allow_const_fn_unstable(const_eval_select)]
67#[cfg(not(panic = "immediate-abort"))]
68const fn slice_error_fail(s: &str, begin: usize, end: usize) -> ! {
69    crate::intrinsics::const_eval_select((s, begin, end), slice_error_fail_ct, slice_error_fail_rt)
70}
71
72#[cfg(panic = "immediate-abort")]
73const fn slice_error_fail(s: &str, begin: usize, end: usize) -> ! {
74    slice_error_fail_ct(s, begin, end)
75}
76
77#[track_caller]
78const fn slice_error_fail_ct(_: &str, _: usize, _: usize) -> ! {
79    panic!("failed to slice string");
80}
81
82#[track_caller]
83fn slice_error_fail_rt(s: &str, begin: usize, end: usize) -> ! {
84    const MAX_DISPLAY_LENGTH: usize = 256;
85    let trunc_len = s.floor_char_boundary(MAX_DISPLAY_LENGTH);
86    let s_trunc = &s[..trunc_len];
87    let ellipsis = if trunc_len < s.len() { "[...]" } else { "" };
88    let len = s.len();
89
90    // 1. begin is OOB.
91    if begin > len {
92        panic!("start byte index {begin} is out of bounds of `{s_trunc}`{ellipsis}");
93    }
94
95    // 2. end is OOB.
96    if end > len {
97        panic!("end byte index {end} is out of bounds of `{s_trunc}`{ellipsis}");
98    }
99
100    // 3. range is backwards.
101    if begin > end {
102        panic!("begin > end ({begin} > {end}) when slicing `{s_trunc}`{ellipsis}")
103    }
104
105    // 4. begin is inside a character.
106    if !s.is_char_boundary(begin) {
107        let floor = s.floor_char_boundary(begin);
108        let ceil = s.ceil_char_boundary(begin);
109        let range = floor..ceil;
110        let ch = s[floor..ceil].chars().next().unwrap();
111        panic!(
112            "start byte index {begin} is not a char boundary; it is inside {ch:?} (bytes {range:?}) of `{s_trunc}`{ellipsis}"
113        )
114    }
115
116    // 5. end is inside a character.
117    if !s.is_char_boundary(end) {
118        let floor = s.floor_char_boundary(end);
119        let ceil = s.ceil_char_boundary(end);
120        let range = floor..ceil;
121        let ch = s[floor..ceil].chars().next().unwrap();
122        panic!(
123            "end byte index {end} is not a char boundary; it is inside {ch:?} (bytes {range:?}) of `{s_trunc}`{ellipsis}"
124        )
125    }
126
127    // 6. end is OOB and range is inclusive (end == len).
128    // This test cannot be combined with 2. above because for cases like
129    // `"abcαβγ"[4..9]` the error is that 4 is inside 'α', not that 9 is OOB.
130    debug_assert_eq!(end, len);
131    panic!("end byte index {end} is out of bounds of `{s_trunc}`{ellipsis}");
132}
133
134impl str {
135    /// Returns the length of `self`.
136    ///
137    /// This length is in bytes, not [`char`]s or graphemes. In other words,
138    /// it might not be what a human considers the length of the string.
139    ///
140    /// [`char`]: prim@char
141    ///
142    /// # Examples
143    ///
144    /// ```
145    /// let len = "foo".len();
146    /// assert_eq!(3, len);
147    ///
148    /// assert_eq!("ƒoo".len(), 4); // fancy f!
149    /// assert_eq!("ƒoo".chars().count(), 3);
150    /// ```
151    #[stable(feature = "rust1", since = "1.0.0")]
152    #[rustc_const_stable(feature = "const_str_len", since = "1.39.0")]
153    #[rustc_diagnostic_item = "str_len"]
154    #[rustc_no_implicit_autorefs]
155    #[must_use]
156    #[inline]
157    pub const fn len(&self) -> usize {
158        self.as_bytes().len()
159    }
160
161    /// Returns `true` if `self` has a length of zero bytes.
162    ///
163    /// # Examples
164    ///
165    /// ```
166    /// let s = "";
167    /// assert!(s.is_empty());
168    ///
169    /// let s = "not empty";
170    /// assert!(!s.is_empty());
171    /// ```
172    #[stable(feature = "rust1", since = "1.0.0")]
173    #[rustc_const_stable(feature = "const_str_is_empty", since = "1.39.0")]
174    #[rustc_no_implicit_autorefs]
175    #[must_use]
176    #[inline]
177    pub const fn is_empty(&self) -> bool {
178        self.len() == 0
179    }
180
181    /// Converts a slice of bytes to a string slice.
182    ///
183    /// A string slice ([`&str`]) is made of bytes ([`u8`]), and a byte slice
184    /// ([`&[u8]`][byteslice]) is made of bytes, so this function converts between
185    /// the two. Not all byte slices are valid string slices, however: [`&str`] requires
186    /// that it is valid UTF-8. `from_utf8()` checks to ensure that the bytes are valid
187    /// UTF-8, and then does the conversion.
188    ///
189    /// [`&str`]: str
190    /// [byteslice]: prim@slice
191    ///
192    /// If you are sure that the byte slice is valid UTF-8, and you don't want to
193    /// incur the overhead of the validity check, there is an unsafe version of
194    /// this function, [`from_utf8_unchecked`], which has the same
195    /// behavior but skips the check.
196    ///
197    /// If you need a `String` instead of a `&str`, consider
198    /// [`String::from_utf8`][string].
199    ///
200    /// [string]: ../std/string/struct.String.html#method.from_utf8
201    ///
202    /// Because you can stack-allocate a `[u8; N]`, and you can take a
203    /// [`&[u8]`][byteslice] of it, this function is one way to have a
204    /// stack-allocated string. There is an example of this in the
205    /// examples section below.
206    ///
207    /// [byteslice]: slice
208    ///
209    /// # Errors
210    ///
211    /// Returns `Err` if the slice is not UTF-8 with a description as to why the
212    /// provided slice is not UTF-8.
213    ///
214    /// # Examples
215    ///
216    /// Basic usage:
217    ///
218    /// ```
219    /// // some bytes, in a vector
220    /// let sparkle_heart = vec![240, 159, 146, 150];
221    ///
222    /// // We can use the ? (try) operator to check if the bytes are valid
223    /// let sparkle_heart = str::from_utf8(&sparkle_heart)?;
224    ///
225    /// assert_eq!("💖", sparkle_heart);
226    /// # Ok::<_, std::str::Utf8Error>(())
227    /// ```
228    ///
229    /// Incorrect bytes:
230    ///
231    /// ```
232    /// // some invalid bytes, in a vector
233    /// let sparkle_heart = vec![0, 159, 146, 150];
234    ///
235    /// assert!(str::from_utf8(&sparkle_heart).is_err());
236    /// ```
237    ///
238    /// See the docs for [`Utf8Error`] for more details on the kinds of
239    /// errors that can be returned.
240    ///
241    /// A "stack allocated string":
242    ///
243    /// ```
244    /// // some bytes, in a stack-allocated array
245    /// let sparkle_heart = [240, 159, 146, 150];
246    ///
247    /// // We know these bytes are valid, so just use `unwrap()`.
248    /// let sparkle_heart: &str = str::from_utf8(&sparkle_heart).unwrap();
249    ///
250    /// assert_eq!("💖", sparkle_heart);
251    /// ```
252    #[stable(feature = "inherent_str_constructors", since = "1.87.0")]
253    #[rustc_const_stable(feature = "inherent_str_constructors", since = "1.87.0")]
254    #[rustc_diagnostic_item = "str_inherent_from_utf8"]
255    pub const fn from_utf8(v: &[u8]) -> Result<&str, Utf8Error> {
256        converts::from_utf8(v)
257    }
258
259    /// Converts a mutable slice of bytes to a mutable string slice.
260    ///
261    /// # Examples
262    ///
263    /// Basic usage:
264    ///
265    /// ```
266    /// // "Hello, Rust!" as a mutable vector
267    /// let mut hellorust = vec![72, 101, 108, 108, 111, 44, 32, 82, 117, 115, 116, 33];
268    ///
269    /// // As we know these bytes are valid, we can use `unwrap()`
270    /// let outstr = str::from_utf8_mut(&mut hellorust).unwrap();
271    ///
272    /// assert_eq!("Hello, Rust!", outstr);
273    /// ```
274    ///
275    /// Incorrect bytes:
276    ///
277    /// ```
278    /// // Some invalid bytes in a mutable vector
279    /// let mut invalid = vec![128, 223];
280    ///
281    /// assert!(str::from_utf8_mut(&mut invalid).is_err());
282    /// ```
283    /// See the docs for [`Utf8Error`] for more details on the kinds of
284    /// errors that can be returned.
285    #[stable(feature = "inherent_str_constructors", since = "1.87.0")]
286    #[rustc_const_stable(feature = "const_str_from_utf8", since = "1.87.0")]
287    #[rustc_diagnostic_item = "str_inherent_from_utf8_mut"]
288    pub const fn from_utf8_mut(v: &mut [u8]) -> Result<&mut str, Utf8Error> {
289        converts::from_utf8_mut(v)
290    }
291
292    /// Converts a slice of bytes to a string slice without checking
293    /// that the string contains valid UTF-8.
294    ///
295    /// See the safe version, [`from_utf8`], for more information.
296    ///
297    /// # Safety
298    ///
299    /// The bytes passed in must be valid UTF-8.
300    ///
301    /// # Examples
302    ///
303    /// Basic usage:
304    ///
305    /// ```
306    /// // some bytes, in a vector
307    /// let sparkle_heart = vec![240, 159, 146, 150];
308    ///
309    /// let sparkle_heart = unsafe {
310    ///     str::from_utf8_unchecked(&sparkle_heart)
311    /// };
312    ///
313    /// assert_eq!("💖", sparkle_heart);
314    /// ```
315    #[inline]
316    #[must_use]
317    #[stable(feature = "inherent_str_constructors", since = "1.87.0")]
318    #[rustc_const_stable(feature = "inherent_str_constructors", since = "1.87.0")]
319    #[rustc_diagnostic_item = "str_inherent_from_utf8_unchecked"]
320    pub const unsafe fn from_utf8_unchecked(v: &[u8]) -> &str {
321        // SAFETY: converts::from_utf8_unchecked has the same safety requirements as this function.
322        unsafe { converts::from_utf8_unchecked(v) }
323    }
324
325    /// Converts a slice of bytes to a string slice without checking
326    /// that the string contains valid UTF-8; mutable version.
327    ///
328    /// See the immutable version, [`from_utf8_unchecked()`] for documentation and safety requirements.
329    ///
330    /// # Examples
331    ///
332    /// Basic usage:
333    ///
334    /// ```
335    /// let mut heart = vec![240, 159, 146, 150];
336    /// let heart = unsafe { str::from_utf8_unchecked_mut(&mut heart) };
337    ///
338    /// assert_eq!("💖", heart);
339    /// ```
340    #[inline]
341    #[must_use]
342    #[stable(feature = "inherent_str_constructors", since = "1.87.0")]
343    #[rustc_const_stable(feature = "inherent_str_constructors", since = "1.87.0")]
344    #[rustc_diagnostic_item = "str_inherent_from_utf8_unchecked_mut"]
345    pub const unsafe fn from_utf8_unchecked_mut(v: &mut [u8]) -> &mut str {
346        // SAFETY: converts::from_utf8_unchecked_mut has the same safety requirements as this function.
347        unsafe { converts::from_utf8_unchecked_mut(v) }
348    }
349
350    /// Checks that `index`-th byte is the first byte in a UTF-8 code point
351    /// sequence or the end of the string.
352    ///
353    /// The start and end of the string (when `index == self.len()`) are
354    /// considered to be boundaries.
355    ///
356    /// Returns `false` if `index` is greater than `self.len()`.
357    ///
358    /// # Examples
359    ///
360    /// ```
361    /// let s = "Löwe 老虎 Léopard";
362    /// assert!(s.is_char_boundary(0));
363    /// // start of `老`
364    /// assert!(s.is_char_boundary(6));
365    /// assert!(s.is_char_boundary(s.len()));
366    ///
367    /// // second byte of `ö`
368    /// assert!(!s.is_char_boundary(2));
369    ///
370    /// // third byte of `老`
371    /// assert!(!s.is_char_boundary(8));
372    /// ```
373    #[must_use]
374    #[stable(feature = "is_char_boundary", since = "1.9.0")]
375    #[rustc_const_stable(feature = "const_is_char_boundary", since = "1.86.0")]
376    #[inline]
377    pub const fn is_char_boundary(&self, index: usize) -> bool {
378        // 0 is always ok.
379        // Test for 0 explicitly so that it can optimize out the check
380        // easily and skip reading string data for that case.
381        // Note that optimizing `self.get(..index)` relies on this.
382        if index == 0 {
383            return true;
384        }
385
386        if index >= self.len() {
387            // For `true` we have two options:
388            //
389            // - index == self.len()
390            //   Empty strings are valid, so return true
391            // - index > self.len()
392            //   In this case return false
393            //
394            // The check is placed exactly here, because it improves generated
395            // code on higher opt-levels. See PR #84751 for more details.
396            index == self.len()
397        } else {
398            self.as_bytes()[index].is_utf8_char_boundary()
399        }
400    }
401
402    /// Finds the closest `x` not exceeding `index` where [`is_char_boundary(x)`] is `true`.
403    ///
404    /// This method can help you truncate a string so that it's still valid UTF-8, but doesn't
405    /// exceed a given number of bytes. Note that this is done purely at the character level
406    /// and can still visually split graphemes, even though the underlying characters aren't
407    /// split. For example, the emoji 🧑‍🔬 (scientist) could be split so that the string only
408    /// includes 🧑 (person) instead.
409    ///
410    /// [`is_char_boundary(x)`]: Self::is_char_boundary
411    ///
412    /// # Examples
413    ///
414    /// ```
415    /// let s = "❤️🧡💛💚💙💜";
416    /// assert_eq!(s.len(), 26);
417    /// assert!(!s.is_char_boundary(13));
418    ///
419    /// let closest = s.floor_char_boundary(13);
420    /// assert_eq!(closest, 10);
421    /// assert_eq!(&s[..closest], "❤️🧡");
422    /// ```
423    #[stable(feature = "round_char_boundary", since = "1.91.0")]
424    #[rustc_const_stable(feature = "round_char_boundary", since = "1.91.0")]
425    #[inline]
426    pub const fn floor_char_boundary(&self, index: usize) -> usize {
427        if index >= self.len() {
428            self.len()
429        } else {
430            let mut i = index;
431            while i > 0 {
432                if self.as_bytes()[i].is_utf8_char_boundary() {
433                    break;
434                }
435                i -= 1;
436            }
437
438            //  The character boundary will be within four bytes of the index
439            debug_assert!(i >= index.saturating_sub(3));
440
441            i
442        }
443    }
444
445    /// Finds the closest `x` not below `index` where [`is_char_boundary(x)`] is `true`.
446    ///
447    /// If `index` is greater than the length of the string, this returns the length of the string.
448    ///
449    /// This method is the natural complement to [`floor_char_boundary`]. See that method
450    /// for more details.
451    ///
452    /// [`floor_char_boundary`]: str::floor_char_boundary
453    /// [`is_char_boundary(x)`]: Self::is_char_boundary
454    ///
455    /// # Examples
456    ///
457    /// ```
458    /// let s = "❤️🧡💛💚💙💜";
459    /// assert_eq!(s.len(), 26);
460    /// assert!(!s.is_char_boundary(13));
461    ///
462    /// let closest = s.ceil_char_boundary(13);
463    /// assert_eq!(closest, 14);
464    /// assert_eq!(&s[..closest], "❤️🧡💛");
465    /// ```
466    #[stable(feature = "round_char_boundary", since = "1.91.0")]
467    #[rustc_const_stable(feature = "round_char_boundary", since = "1.91.0")]
468    #[inline]
469    pub const fn ceil_char_boundary(&self, index: usize) -> usize {
470        if index >= self.len() {
471            self.len()
472        } else {
473            let mut i = index;
474            while i < self.len() {
475                if self.as_bytes()[i].is_utf8_char_boundary() {
476                    break;
477                }
478                i += 1;
479            }
480
481            //  The character boundary will be within four bytes of the index
482            debug_assert!(i <= index + 3);
483
484            i
485        }
486    }
487
488    /// Converts a string slice to a byte slice. To convert the byte slice back
489    /// into a string slice, use the [`from_utf8`] function.
490    ///
491    /// # Examples
492    ///
493    /// ```
494    /// let bytes = "bors".as_bytes();
495    /// assert_eq!(b"bors", bytes);
496    /// ```
497    #[stable(feature = "rust1", since = "1.0.0")]
498    #[rustc_const_stable(feature = "str_as_bytes", since = "1.39.0")]
499    #[must_use]
500    #[inline(always)]
501    #[allow(unused_attributes)]
502    pub const fn as_bytes(&self) -> &[u8] {
503        // SAFETY: const sound because we transmute two types with the same layout
504        unsafe { mem::transmute(self) }
505    }
506
507    /// Converts a mutable string slice to a mutable byte slice.
508    ///
509    /// # Safety
510    ///
511    /// The caller must ensure that the content of the slice is valid UTF-8
512    /// before the borrow ends and the underlying `str` is used.
513    ///
514    /// Use of a `str` whose contents are not valid UTF-8 is undefined behavior.
515    ///
516    /// # Examples
517    ///
518    /// Basic usage:
519    ///
520    /// ```
521    /// let mut s = String::from("Hello");
522    /// let bytes = unsafe { s.as_bytes_mut() };
523    ///
524    /// assert_eq!(b"Hello", bytes);
525    /// ```
526    ///
527    /// Mutability:
528    ///
529    /// ```
530    /// let mut s = String::from("🗻∈🌏");
531    ///
532    /// unsafe {
533    ///     let bytes = s.as_bytes_mut();
534    ///
535    ///     bytes[0] = 0xF0;
536    ///     bytes[1] = 0x9F;
537    ///     bytes[2] = 0x8D;
538    ///     bytes[3] = 0x94;
539    /// }
540    ///
541    /// assert_eq!("🍔∈🌏", s);
542    /// ```
543    #[stable(feature = "str_mut_extras", since = "1.20.0")]
544    #[rustc_const_stable(feature = "const_str_as_mut", since = "1.83.0")]
545    #[must_use]
546    #[inline(always)]
547    pub const unsafe fn as_bytes_mut(&mut self) -> &mut [u8] {
548        // SAFETY: the cast from `&str` to `&[u8]` is safe since `str`
549        // has the same layout as `&[u8]` (only std can make this guarantee).
550        // The pointer dereference is safe since it comes from a mutable reference which
551        // is guaranteed to be valid for writes.
552        unsafe { &mut *(self as *mut str as *mut [u8]) }
553    }
554
555    /// Converts a string slice to a raw pointer.
556    ///
557    /// As string slices are a slice of bytes, the raw pointer points to a
558    /// [`u8`]. This pointer will be pointing to the first byte of the string
559    /// slice.
560    ///
561    /// The caller must ensure that the returned pointer is never written to.
562    /// If you need to mutate the contents of the string slice, use [`as_mut_ptr`].
563    ///
564    /// [`as_mut_ptr`]: str::as_mut_ptr
565    ///
566    /// # Examples
567    ///
568    /// ```
569    /// let s = "Hello";
570    /// let ptr = s.as_ptr();
571    /// ```
572    #[stable(feature = "rust1", since = "1.0.0")]
573    #[rustc_const_stable(feature = "rustc_str_as_ptr", since = "1.32.0")]
574    #[rustc_never_returns_null_ptr]
575    #[rustc_as_ptr]
576    #[must_use]
577    #[inline(always)]
578    pub const fn as_ptr(&self) -> *const u8 {
579        self as *const str as *const u8
580    }
581
582    /// Converts a mutable string slice to a raw pointer.
583    ///
584    /// As string slices are a slice of bytes, the raw pointer points to a
585    /// [`u8`]. This pointer will be pointing to the first byte of the string
586    /// slice.
587    ///
588    /// It is your responsibility to make sure that the string slice only gets
589    /// modified in a way that it remains valid UTF-8.
590    #[stable(feature = "str_as_mut_ptr", since = "1.36.0")]
591    #[rustc_const_stable(feature = "const_str_as_mut", since = "1.83.0")]
592    #[rustc_never_returns_null_ptr]
593    #[rustc_as_ptr]
594    #[must_use]
595    #[inline(always)]
596    pub const fn as_mut_ptr(&mut self) -> *mut u8 {
597        self as *mut str as *mut u8
598    }
599
600    /// Returns a subslice of `str`.
601    ///
602    /// This is the non-panicking alternative to indexing the `str`. Returns
603    /// [`None`] whenever equivalent indexing operation would panic.
604    ///
605    /// # Examples
606    ///
607    /// ```
608    /// let v = String::from("🗻∈🌏");
609    ///
610    /// assert_eq!(Some("🗻"), v.get(0..4));
611    ///
612    /// // indices not on UTF-8 sequence boundaries
613    /// assert!(v.get(1..).is_none());
614    /// assert!(v.get(..8).is_none());
615    ///
616    /// // out of bounds
617    /// assert!(v.get(..42).is_none());
618    /// ```
619    #[stable(feature = "str_checked_slicing", since = "1.20.0")]
620    #[rustc_const_unstable(feature = "const_index", issue = "143775")]
621    #[inline]
622    pub const fn get<I: [const] SliceIndex<str>>(&self, i: I) -> Option<&I::Output> {
623        i.get(self)
624    }
625
626    /// Returns a mutable subslice of `str`.
627    ///
628    /// This is the non-panicking alternative to indexing the `str`. Returns
629    /// [`None`] whenever equivalent indexing operation would panic.
630    ///
631    /// # Examples
632    ///
633    /// ```
634    /// let mut v = String::from("hello");
635    /// // correct length
636    /// assert!(v.get_mut(0..5).is_some());
637    /// // out of bounds
638    /// assert!(v.get_mut(..42).is_none());
639    /// assert_eq!(Some("he"), v.get_mut(0..2).map(|v| &*v));
640    ///
641    /// assert_eq!("hello", v);
642    /// {
643    ///     let s = v.get_mut(0..2);
644    ///     let s = s.map(|s| {
645    ///         s.make_ascii_uppercase();
646    ///         &*s
647    ///     });
648    ///     assert_eq!(Some("HE"), s);
649    /// }
650    /// assert_eq!("HEllo", v);
651    /// ```
652    #[stable(feature = "str_checked_slicing", since = "1.20.0")]
653    #[rustc_const_unstable(feature = "const_index", issue = "143775")]
654    #[inline]
655    pub const fn get_mut<I: [const] SliceIndex<str>>(&mut self, i: I) -> Option<&mut I::Output> {
656        i.get_mut(self)
657    }
658
659    /// Returns an unchecked subslice of `str`.
660    ///
661    /// This is the unchecked alternative to indexing the `str`.
662    ///
663    /// # Safety
664    ///
665    /// Callers of this function are responsible that these preconditions are
666    /// satisfied:
667    ///
668    /// * The starting index must not exceed the ending index;
669    /// * Indexes must be within bounds of the original slice;
670    /// * Indexes must lie on UTF-8 sequence boundaries.
671    ///
672    /// Failing that, the returned string slice may reference invalid memory or
673    /// violate the invariants communicated by the `str` type.
674    ///
675    /// # Examples
676    ///
677    /// ```
678    /// let v = "🗻∈🌏";
679    /// unsafe {
680    ///     assert_eq!("🗻", v.get_unchecked(0..4));
681    ///     assert_eq!("∈", v.get_unchecked(4..7));
682    ///     assert_eq!("🌏", v.get_unchecked(7..11));
683    /// }
684    /// ```
685    #[stable(feature = "str_checked_slicing", since = "1.20.0")]
686    #[inline]
687    pub unsafe fn get_unchecked<I: SliceIndex<str>>(&self, i: I) -> &I::Output {
688        // SAFETY: the caller must uphold the safety contract for `get_unchecked`;
689        // the slice is dereferenceable because `self` is a safe reference.
690        // The returned pointer is safe because impls of `SliceIndex` have to guarantee that it is.
691        unsafe { &*i.get_unchecked(self) }
692    }
693
694    /// Returns a mutable, unchecked subslice of `str`.
695    ///
696    /// This is the unchecked alternative to indexing the `str`.
697    ///
698    /// # Safety
699    ///
700    /// Callers of this function are responsible that these preconditions are
701    /// satisfied:
702    ///
703    /// * The starting index must not exceed the ending index;
704    /// * Indexes must be within bounds of the original slice;
705    /// * Indexes must lie on UTF-8 sequence boundaries.
706    ///
707    /// Failing that, the returned string slice may reference invalid memory or
708    /// violate the invariants communicated by the `str` type.
709    ///
710    /// # Examples
711    ///
712    /// ```
713    /// let mut v = String::from("🗻∈🌏");
714    /// unsafe {
715    ///     assert_eq!("🗻", v.get_unchecked_mut(0..4));
716    ///     assert_eq!("∈", v.get_unchecked_mut(4..7));
717    ///     assert_eq!("🌏", v.get_unchecked_mut(7..11));
718    /// }
719    /// ```
720    #[stable(feature = "str_checked_slicing", since = "1.20.0")]
721    #[inline]
722    pub unsafe fn get_unchecked_mut<I: SliceIndex<str>>(&mut self, i: I) -> &mut I::Output {
723        // SAFETY: the caller must uphold the safety contract for `get_unchecked_mut`;
724        // the slice is dereferenceable because `self` is a safe reference.
725        // The returned pointer is safe because impls of `SliceIndex` have to guarantee that it is.
726        unsafe { &mut *i.get_unchecked_mut(self) }
727    }
728
729    /// Creates a string slice from another string slice, bypassing safety
730    /// checks.
731    ///
732    /// This is generally not recommended, use with caution! For a safe
733    /// alternative see [`str`] and [`Index`].
734    ///
735    /// [`Index`]: crate::ops::Index
736    ///
737    /// This new slice goes from `begin` to `end`, including `begin` but
738    /// excluding `end`.
739    ///
740    /// To get a mutable string slice instead, see the
741    /// [`slice_mut_unchecked`] method.
742    ///
743    /// [`slice_mut_unchecked`]: str::slice_mut_unchecked
744    ///
745    /// # Safety
746    ///
747    /// Callers of this function are responsible that three preconditions are
748    /// satisfied:
749    ///
750    /// * `begin` must not exceed `end`.
751    /// * `begin` and `end` must be byte positions within the string slice.
752    /// * `begin` and `end` must lie on UTF-8 sequence boundaries.
753    ///
754    /// # Examples
755    ///
756    /// ```
757    /// let s = "Löwe 老虎 Léopard";
758    ///
759    /// unsafe {
760    ///     assert_eq!("Löwe 老虎 Léopard", s.slice_unchecked(0, 21));
761    /// }
762    ///
763    /// let s = "Hello, world!";
764    ///
765    /// unsafe {
766    ///     assert_eq!("world", s.slice_unchecked(7, 12));
767    /// }
768    /// ```
769    #[stable(feature = "rust1", since = "1.0.0")]
770    #[deprecated(since = "1.29.0", note = "use `get_unchecked(begin..end)` instead")]
771    #[must_use]
772    #[inline]
773    pub unsafe fn slice_unchecked(&self, begin: usize, end: usize) -> &str {
774        // SAFETY: the caller must uphold the safety contract for `get_unchecked`;
775        // the slice is dereferenceable because `self` is a safe reference.
776        // The returned pointer is safe because impls of `SliceIndex` have to guarantee that it is.
777        unsafe { &*(begin..end).get_unchecked(self) }
778    }
779
780    /// Creates a string slice from another string slice, bypassing safety
781    /// checks.
782    ///
783    /// This is generally not recommended, use with caution! For a safe
784    /// alternative see [`str`] and [`IndexMut`].
785    ///
786    /// [`IndexMut`]: crate::ops::IndexMut
787    ///
788    /// This new slice goes from `begin` to `end`, including `begin` but
789    /// excluding `end`.
790    ///
791    /// To get an immutable string slice instead, see the
792    /// [`slice_unchecked`] method.
793    ///
794    /// [`slice_unchecked`]: str::slice_unchecked
795    ///
796    /// # Safety
797    ///
798    /// Callers of this function are responsible that three preconditions are
799    /// satisfied:
800    ///
801    /// * `begin` must not exceed `end`.
802    /// * `begin` and `end` must be byte positions within the string slice.
803    /// * `begin` and `end` must lie on UTF-8 sequence boundaries.
804    #[stable(feature = "str_slice_mut", since = "1.5.0")]
805    #[deprecated(since = "1.29.0", note = "use `get_unchecked_mut(begin..end)` instead")]
806    #[inline]
807    pub unsafe fn slice_mut_unchecked(&mut self, begin: usize, end: usize) -> &mut str {
808        // SAFETY: the caller must uphold the safety contract for `get_unchecked_mut`;
809        // the slice is dereferenceable because `self` is a safe reference.
810        // The returned pointer is safe because impls of `SliceIndex` have to guarantee that it is.
811        unsafe { &mut *(begin..end).get_unchecked_mut(self) }
812    }
813
814    /// Divides one string slice into two at an index.
815    ///
816    /// The argument, `mid`, should be a byte offset from the start of the
817    /// string. It must also be on the boundary of a UTF-8 code point.
818    ///
819    /// The two slices returned go from the start of the string slice to `mid`,
820    /// and from `mid` to the end of the string slice.
821    ///
822    /// To get mutable string slices instead, see the [`split_at_mut`]
823    /// method.
824    ///
825    /// [`split_at_mut`]: str::split_at_mut
826    ///
827    /// # Panics
828    ///
829    /// Panics if `mid` is not on a UTF-8 code point boundary, or if it is past
830    /// the end of the last code point of the string slice.  For a non-panicking
831    /// alternative see [`split_at_checked`](str::split_at_checked).
832    ///
833    /// # Examples
834    ///
835    /// ```
836    /// let s = "Per Martin-Löf";
837    ///
838    /// let (first, last) = s.split_at(3);
839    ///
840    /// assert_eq!("Per", first);
841    /// assert_eq!(" Martin-Löf", last);
842    /// ```
843    #[inline]
844    #[must_use]
845    #[stable(feature = "str_split_at", since = "1.4.0")]
846    #[rustc_const_stable(feature = "const_str_split_at", since = "1.86.0")]
847    pub const fn split_at(&self, mid: usize) -> (&str, &str) {
848        match self.split_at_checked(mid) {
849            None => slice_error_fail(self, 0, mid),
850            Some(pair) => pair,
851        }
852    }
853
854    /// Divides one mutable string slice into two at an index.
855    ///
856    /// The argument, `mid`, should be a byte offset from the start of the
857    /// string. It must also be on the boundary of a UTF-8 code point.
858    ///
859    /// The two slices returned go from the start of the string slice to `mid`,
860    /// and from `mid` to the end of the string slice.
861    ///
862    /// To get immutable string slices instead, see the [`split_at`] method.
863    ///
864    /// [`split_at`]: str::split_at
865    ///
866    /// # Panics
867    ///
868    /// Panics if `mid` is not on a UTF-8 code point boundary, or if it is past
869    /// the end of the last code point of the string slice.  For a non-panicking
870    /// alternative see [`split_at_mut_checked`](str::split_at_mut_checked).
871    ///
872    /// # Examples
873    ///
874    /// ```
875    /// let mut s = "Per Martin-Löf".to_string();
876    /// {
877    ///     let (first, last) = s.split_at_mut(3);
878    ///     first.make_ascii_uppercase();
879    ///     assert_eq!("PER", first);
880    ///     assert_eq!(" Martin-Löf", last);
881    /// }
882    /// assert_eq!("PER Martin-Löf", s);
883    /// ```
884    #[inline]
885    #[must_use]
886    #[stable(feature = "str_split_at", since = "1.4.0")]
887    #[rustc_const_stable(feature = "const_str_split_at", since = "1.86.0")]
888    pub const fn split_at_mut(&mut self, mid: usize) -> (&mut str, &mut str) {
889        // is_char_boundary checks that the index is in [0, .len()]
890        if self.is_char_boundary(mid) {
891            // SAFETY: just checked that `mid` is on a char boundary.
892            unsafe { self.split_at_mut_unchecked(mid) }
893        } else {
894            slice_error_fail(self, 0, mid)
895        }
896    }
897
898    /// Divides one string slice into two at an index.
899    ///
900    /// The argument, `mid`, should be a valid byte offset from the start of the
901    /// string. It must also be on the boundary of a UTF-8 code point. The
902    /// method returns `None` if that’s not the case.
903    ///
904    /// The two slices returned go from the start of the string slice to `mid`,
905    /// and from `mid` to the end of the string slice.
906    ///
907    /// To get mutable string slices instead, see the [`split_at_mut_checked`]
908    /// method.
909    ///
910    /// [`split_at_mut_checked`]: str::split_at_mut_checked
911    ///
912    /// # Examples
913    ///
914    /// ```
915    /// let s = "Per Martin-Löf";
916    ///
917    /// let (first, last) = s.split_at_checked(3).unwrap();
918    /// assert_eq!("Per", first);
919    /// assert_eq!(" Martin-Löf", last);
920    ///
921    /// assert_eq!(None, s.split_at_checked(13));  // Inside “ö”
922    /// assert_eq!(None, s.split_at_checked(16));  // Beyond the string length
923    /// ```
924    #[inline]
925    #[must_use]
926    #[stable(feature = "split_at_checked", since = "1.80.0")]
927    #[rustc_const_stable(feature = "const_str_split_at", since = "1.86.0")]
928    pub const fn split_at_checked(&self, mid: usize) -> Option<(&str, &str)> {
929        // is_char_boundary checks that the index is in [0, .len()]
930        if self.is_char_boundary(mid) {
931            // SAFETY: just checked that `mid` is on a char boundary.
932            Some(unsafe { self.split_at_unchecked(mid) })
933        } else {
934            None
935        }
936    }
937
938    /// Divides one mutable string slice into two at an index.
939    ///
940    /// The argument, `mid`, should be a valid byte offset from the start of the
941    /// string. It must also be on the boundary of a UTF-8 code point. The
942    /// method returns `None` if that’s not the case.
943    ///
944    /// The two slices returned go from the start of the string slice to `mid`,
945    /// and from `mid` to the end of the string slice.
946    ///
947    /// To get immutable string slices instead, see the [`split_at_checked`] method.
948    ///
949    /// [`split_at_checked`]: str::split_at_checked
950    ///
951    /// # Examples
952    ///
953    /// ```
954    /// let mut s = "Per Martin-Löf".to_string();
955    /// if let Some((first, last)) = s.split_at_mut_checked(3) {
956    ///     first.make_ascii_uppercase();
957    ///     assert_eq!("PER", first);
958    ///     assert_eq!(" Martin-Löf", last);
959    /// }
960    /// assert_eq!("PER Martin-Löf", s);
961    ///
962    /// assert_eq!(None, s.split_at_mut_checked(13));  // Inside “ö”
963    /// assert_eq!(None, s.split_at_mut_checked(16));  // Beyond the string length
964    /// ```
965    #[inline]
966    #[must_use]
967    #[stable(feature = "split_at_checked", since = "1.80.0")]
968    #[rustc_const_stable(feature = "const_str_split_at", since = "1.86.0")]
969    pub const fn split_at_mut_checked(&mut self, mid: usize) -> Option<(&mut str, &mut str)> {
970        // is_char_boundary checks that the index is in [0, .len()]
971        if self.is_char_boundary(mid) {
972            // SAFETY: just checked that `mid` is on a char boundary.
973            Some(unsafe { self.split_at_mut_unchecked(mid) })
974        } else {
975            None
976        }
977    }
978
979    /// Divides one string slice into two at an index.
980    ///
981    /// # Safety
982    ///
983    /// The caller must ensure that `mid` is a valid byte offset from the start
984    /// of the string and falls on the boundary of a UTF-8 code point.
985    #[inline]
986    const unsafe fn split_at_unchecked(&self, mid: usize) -> (&str, &str) {
987        let len = self.len();
988        let ptr = self.as_ptr();
989        // SAFETY: caller guarantees `mid` is on a char boundary.
990        unsafe {
991            (
992                from_utf8_unchecked(slice::from_raw_parts(ptr, mid)),
993                from_utf8_unchecked(slice::from_raw_parts(ptr.add(mid), len - mid)),
994            )
995        }
996    }
997
998    /// Divides one string slice into two at an index.
999    ///
1000    /// # Safety
1001    ///
1002    /// The caller must ensure that `mid` is a valid byte offset from the start
1003    /// of the string and falls on the boundary of a UTF-8 code point.
1004    const unsafe fn split_at_mut_unchecked(&mut self, mid: usize) -> (&mut str, &mut str) {
1005        let len = self.len();
1006        let ptr = self.as_mut_ptr();
1007        // SAFETY: caller guarantees `mid` is on a char boundary.
1008        unsafe {
1009            (
1010                from_utf8_unchecked_mut(slice::from_raw_parts_mut(ptr, mid)),
1011                from_utf8_unchecked_mut(slice::from_raw_parts_mut(ptr.add(mid), len - mid)),
1012            )
1013        }
1014    }
1015
1016    /// Returns an iterator over the [`char`]s of a string slice.
1017    ///
1018    /// As a string slice consists of valid UTF-8, we can iterate through a
1019    /// string slice by [`char`]. This method returns such an iterator.
1020    ///
1021    /// It's important to remember that [`char`] represents a Unicode Scalar
1022    /// Value, and might not match your idea of what a 'character' is. Iteration
1023    /// over grapheme clusters may be what you actually want. This functionality
1024    /// is not provided by Rust's standard library, check crates.io instead.
1025    ///
1026    /// # Examples
1027    ///
1028    /// Basic usage:
1029    ///
1030    /// ```
1031    /// let word = "goodbye";
1032    ///
1033    /// let count = word.chars().count();
1034    /// assert_eq!(7, count);
1035    ///
1036    /// let mut chars = word.chars();
1037    ///
1038    /// assert_eq!(Some('g'), chars.next());
1039    /// assert_eq!(Some('o'), chars.next());
1040    /// assert_eq!(Some('o'), chars.next());
1041    /// assert_eq!(Some('d'), chars.next());
1042    /// assert_eq!(Some('b'), chars.next());
1043    /// assert_eq!(Some('y'), chars.next());
1044    /// assert_eq!(Some('e'), chars.next());
1045    ///
1046    /// assert_eq!(None, chars.next());
1047    /// ```
1048    ///
1049    /// Remember, [`char`]s might not match your intuition about characters:
1050    ///
1051    /// [`char`]: prim@char
1052    ///
1053    /// ```
1054    /// let y = "y̆";
1055    ///
1056    /// let mut chars = y.chars();
1057    ///
1058    /// assert_eq!(Some('y'), chars.next()); // not 'y̆'
1059    /// assert_eq!(Some('\u{0306}'), chars.next());
1060    ///
1061    /// assert_eq!(None, chars.next());
1062    /// ```
1063    #[stable(feature = "rust1", since = "1.0.0")]
1064    #[inline]
1065    #[rustc_diagnostic_item = "str_chars"]
1066    pub fn chars(&self) -> Chars<'_> {
1067        Chars { iter: self.as_bytes().iter() }
1068    }
1069
1070    /// Returns an iterator over the [`char`]s of a string slice, and their
1071    /// positions.
1072    ///
1073    /// As a string slice consists of valid UTF-8, we can iterate through a
1074    /// string slice by [`char`]. This method returns an iterator of both
1075    /// these [`char`]s, as well as their byte positions.
1076    ///
1077    /// The iterator yields tuples. The position is first, the [`char`] is
1078    /// second.
1079    ///
1080    /// # Examples
1081    ///
1082    /// Basic usage:
1083    ///
1084    /// ```
1085    /// let word = "goodbye";
1086    ///
1087    /// let count = word.char_indices().count();
1088    /// assert_eq!(7, count);
1089    ///
1090    /// let mut char_indices = word.char_indices();
1091    ///
1092    /// assert_eq!(Some((0, 'g')), char_indices.next());
1093    /// assert_eq!(Some((1, 'o')), char_indices.next());
1094    /// assert_eq!(Some((2, 'o')), char_indices.next());
1095    /// assert_eq!(Some((3, 'd')), char_indices.next());
1096    /// assert_eq!(Some((4, 'b')), char_indices.next());
1097    /// assert_eq!(Some((5, 'y')), char_indices.next());
1098    /// assert_eq!(Some((6, 'e')), char_indices.next());
1099    ///
1100    /// assert_eq!(None, char_indices.next());
1101    /// ```
1102    ///
1103    /// Remember, [`char`]s might not match your intuition about characters:
1104    ///
1105    /// [`char`]: prim@char
1106    ///
1107    /// ```
1108    /// let yes = "y̆es";
1109    ///
1110    /// let mut char_indices = yes.char_indices();
1111    ///
1112    /// assert_eq!(Some((0, 'y')), char_indices.next()); // not (0, 'y̆')
1113    /// assert_eq!(Some((1, '\u{0306}')), char_indices.next());
1114    ///
1115    /// // note the 3 here - the previous character took up two bytes
1116    /// assert_eq!(Some((3, 'e')), char_indices.next());
1117    /// assert_eq!(Some((4, 's')), char_indices.next());
1118    ///
1119    /// assert_eq!(None, char_indices.next());
1120    /// ```
1121    #[stable(feature = "rust1", since = "1.0.0")]
1122    #[inline]
1123    pub fn char_indices(&self) -> CharIndices<'_> {
1124        CharIndices { front_offset: 0, iter: self.chars() }
1125    }
1126
1127    /// Returns an iterator over the bytes of a string slice.
1128    ///
1129    /// As a string slice consists of a sequence of bytes, we can iterate
1130    /// through a string slice by byte. This method returns such an iterator.
1131    ///
1132    /// # Examples
1133    ///
1134    /// ```
1135    /// let mut bytes = "bors".bytes();
1136    ///
1137    /// assert_eq!(Some(b'b'), bytes.next());
1138    /// assert_eq!(Some(b'o'), bytes.next());
1139    /// assert_eq!(Some(b'r'), bytes.next());
1140    /// assert_eq!(Some(b's'), bytes.next());
1141    ///
1142    /// assert_eq!(None, bytes.next());
1143    /// ```
1144    #[stable(feature = "rust1", since = "1.0.0")]
1145    #[inline]
1146    pub fn bytes(&self) -> Bytes<'_> {
1147        Bytes(self.as_bytes().iter().copied())
1148    }
1149
1150    /// Splits a string slice by whitespace.
1151    ///
1152    /// The iterator returned will return string slices that are sub-slices of
1153    /// the original string slice, separated by any amount of whitespace.
1154    ///
1155    /// 'Whitespace' is defined according to the terms of the Unicode Derived
1156    /// Core Property `White_Space`. If you only want to split on ASCII whitespace
1157    /// instead, use [`split_ascii_whitespace`].
1158    ///
1159    /// [`split_ascii_whitespace`]: str::split_ascii_whitespace
1160    ///
1161    /// # Examples
1162    ///
1163    /// Basic usage:
1164    ///
1165    /// ```
1166    /// let mut iter = "A few words".split_whitespace();
1167    ///
1168    /// assert_eq!(Some("A"), iter.next());
1169    /// assert_eq!(Some("few"), iter.next());
1170    /// assert_eq!(Some("words"), iter.next());
1171    ///
1172    /// assert_eq!(None, iter.next());
1173    /// ```
1174    ///
1175    /// All kinds of whitespace are considered:
1176    ///
1177    /// ```
1178    /// let mut iter = " Mary   had\ta\u{2009}little  \n\t lamb".split_whitespace();
1179    /// assert_eq!(Some("Mary"), iter.next());
1180    /// assert_eq!(Some("had"), iter.next());
1181    /// assert_eq!(Some("a"), iter.next());
1182    /// assert_eq!(Some("little"), iter.next());
1183    /// assert_eq!(Some("lamb"), iter.next());
1184    ///
1185    /// assert_eq!(None, iter.next());
1186    /// ```
1187    ///
1188    /// If the string is empty or all whitespace, the iterator yields no string slices:
1189    /// ```
1190    /// assert_eq!("".split_whitespace().next(), None);
1191    /// assert_eq!("   ".split_whitespace().next(), None);
1192    /// ```
1193    #[must_use = "this returns the split string as an iterator, \
1194                  without modifying the original"]
1195    #[stable(feature = "split_whitespace", since = "1.1.0")]
1196    #[rustc_diagnostic_item = "str_split_whitespace"]
1197    #[inline]
1198    pub fn split_whitespace(&self) -> SplitWhitespace<'_> {
1199        SplitWhitespace { inner: self.split(IsWhitespace).filter(IsNotEmpty) }
1200    }
1201
1202    /// Splits a string slice by ASCII whitespace.
1203    ///
1204    /// The iterator returned will return string slices that are sub-slices of
1205    /// the original string slice, separated by any amount of ASCII whitespace.
1206    ///
1207    /// This uses the same definition as [`char::is_ascii_whitespace`].
1208    /// To split by Unicode `Whitespace` instead, use [`split_whitespace`].
1209    ///
1210    /// [`split_whitespace`]: str::split_whitespace
1211    ///
1212    /// # Examples
1213    ///
1214    /// Basic usage:
1215    ///
1216    /// ```
1217    /// let mut iter = "A few words".split_ascii_whitespace();
1218    ///
1219    /// assert_eq!(Some("A"), iter.next());
1220    /// assert_eq!(Some("few"), iter.next());
1221    /// assert_eq!(Some("words"), iter.next());
1222    ///
1223    /// assert_eq!(None, iter.next());
1224    /// ```
1225    ///
1226    /// Various kinds of ASCII whitespace are considered
1227    /// (see [`char::is_ascii_whitespace`]):
1228    ///
1229    /// ```
1230    /// let mut iter = " Mary   had\ta little  \n\t lamb".split_ascii_whitespace();
1231    /// assert_eq!(Some("Mary"), iter.next());
1232    /// assert_eq!(Some("had"), iter.next());
1233    /// assert_eq!(Some("a"), iter.next());
1234    /// assert_eq!(Some("little"), iter.next());
1235    /// assert_eq!(Some("lamb"), iter.next());
1236    ///
1237    /// assert_eq!(None, iter.next());
1238    /// ```
1239    ///
1240    /// If the string is empty or all ASCII whitespace, the iterator yields no string slices:
1241    /// ```
1242    /// assert_eq!("".split_ascii_whitespace().next(), None);
1243    /// assert_eq!("   ".split_ascii_whitespace().next(), None);
1244    /// ```
1245    #[must_use = "this returns the split string as an iterator, \
1246                  without modifying the original"]
1247    #[stable(feature = "split_ascii_whitespace", since = "1.34.0")]
1248    #[inline]
1249    pub fn split_ascii_whitespace(&self) -> SplitAsciiWhitespace<'_> {
1250        let inner =
1251            self.as_bytes().split(IsAsciiWhitespace).filter(BytesIsNotEmpty).map(UnsafeBytesToStr);
1252        SplitAsciiWhitespace { inner }
1253    }
1254
1255    /// Returns an iterator over the lines of a string, as string slices.
1256    ///
1257    /// Lines are split at line endings that are either newlines (`\n`) or
1258    /// sequences of a carriage return followed by a line feed (`\r\n`).
1259    ///
1260    /// Line terminators are not included in the lines returned by the iterator.
1261    ///
1262    /// Note that any carriage return (`\r`) not immediately followed by a
1263    /// line feed (`\n`) does not split a line. These carriage returns are
1264    /// thereby included in the produced lines.
1265    ///
1266    /// The final line ending is optional. A string that ends with a final line
1267    /// ending will return the same lines as an otherwise identical string
1268    /// without a final line ending.
1269    ///
1270    /// An empty string returns an empty iterator.
1271    ///
1272    /// # Examples
1273    ///
1274    /// Basic usage:
1275    ///
1276    /// ```
1277    /// let text = "foo\r\nbar\n\nbaz\r";
1278    /// let mut lines = text.lines();
1279    ///
1280    /// assert_eq!(Some("foo"), lines.next());
1281    /// assert_eq!(Some("bar"), lines.next());
1282    /// assert_eq!(Some(""), lines.next());
1283    /// // Trailing carriage return is included in the last line
1284    /// assert_eq!(Some("baz\r"), lines.next());
1285    ///
1286    /// assert_eq!(None, lines.next());
1287    /// ```
1288    ///
1289    /// The final line does not require any ending:
1290    ///
1291    /// ```
1292    /// let text = "foo\nbar\n\r\nbaz";
1293    /// let mut lines = text.lines();
1294    ///
1295    /// assert_eq!(Some("foo"), lines.next());
1296    /// assert_eq!(Some("bar"), lines.next());
1297    /// assert_eq!(Some(""), lines.next());
1298    /// assert_eq!(Some("baz"), lines.next());
1299    ///
1300    /// assert_eq!(None, lines.next());
1301    /// ```
1302    ///
1303    /// An empty string returns an empty iterator:
1304    ///
1305    /// ```
1306    /// let text = "";
1307    /// let mut lines = text.lines();
1308    ///
1309    /// assert_eq!(lines.next(), None);
1310    /// ```
1311    #[stable(feature = "rust1", since = "1.0.0")]
1312    #[inline]
1313    pub fn lines(&self) -> Lines<'_> {
1314        Lines(self.split_inclusive('\n').map(LinesMap))
1315    }
1316
1317    /// Returns an iterator over the lines of a string.
1318    #[stable(feature = "rust1", since = "1.0.0")]
1319    #[deprecated(since = "1.4.0", note = "use lines() instead now", suggestion = "lines")]
1320    #[inline]
1321    #[allow(deprecated)]
1322    pub fn lines_any(&self) -> LinesAny<'_> {
1323        LinesAny(self.lines())
1324    }
1325
1326    /// Returns an iterator of `u16` over the string encoded
1327    /// as native endian UTF-16 (without byte-order mark).
1328    ///
1329    /// # Examples
1330    ///
1331    /// ```
1332    /// let text = "Zażółć gęślą jaźń";
1333    ///
1334    /// let utf8_len = text.len();
1335    /// let utf16_len = text.encode_utf16().count();
1336    ///
1337    /// assert!(utf16_len <= utf8_len);
1338    /// ```
1339    #[must_use = "this returns the encoded string as an iterator, \
1340                  without modifying the original"]
1341    #[stable(feature = "encode_utf16", since = "1.8.0")]
1342    pub fn encode_utf16(&self) -> EncodeUtf16<'_> {
1343        EncodeUtf16 { chars: self.chars(), extra: 0 }
1344    }
1345
1346    /// Returns `true` if the given pattern matches a sub-slice of
1347    /// this string slice.
1348    ///
1349    /// Returns `false` if it does not.
1350    ///
1351    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1352    /// function or closure that determines if a character matches.
1353    ///
1354    /// [`char`]: prim@char
1355    /// [pattern]: self::pattern
1356    ///
1357    /// # Examples
1358    ///
1359    /// ```
1360    /// let bananas = "bananas";
1361    ///
1362    /// assert!(bananas.contains("nana"));
1363    /// assert!(!bananas.contains("apples"));
1364    /// ```
1365    #[stable(feature = "rust1", since = "1.0.0")]
1366    #[inline]
1367    pub fn contains<P: Pattern>(&self, pat: P) -> bool {
1368        pat.is_contained_in(self)
1369    }
1370
1371    /// Returns `true` if the given pattern matches a prefix of this
1372    /// string slice.
1373    ///
1374    /// Returns `false` if it does not.
1375    ///
1376    /// The [pattern] can be a `&str`, in which case this function will return true if
1377    /// the `&str` is a prefix of this string slice.
1378    ///
1379    /// The [pattern] can also be a [`char`], a slice of [`char`]s, or a
1380    /// function or closure that determines if a character matches.
1381    /// These will only be checked against the first character of this string slice.
1382    /// Look at the second example below regarding behavior for slices of [`char`]s.
1383    ///
1384    /// [`char`]: prim@char
1385    /// [pattern]: self::pattern
1386    ///
1387    /// # Examples
1388    ///
1389    /// ```
1390    /// let bananas = "bananas";
1391    ///
1392    /// assert!(bananas.starts_with("bana"));
1393    /// assert!(!bananas.starts_with("nana"));
1394    /// ```
1395    ///
1396    /// ```
1397    /// let bananas = "bananas";
1398    ///
1399    /// // Note that both of these assert successfully.
1400    /// assert!(bananas.starts_with(&['b', 'a', 'n', 'a']));
1401    /// assert!(bananas.starts_with(&['a', 'b', 'c', 'd']));
1402    /// ```
1403    #[stable(feature = "rust1", since = "1.0.0")]
1404    #[rustc_diagnostic_item = "str_starts_with"]
1405    pub fn starts_with<P: Pattern>(&self, pat: P) -> bool {
1406        pat.is_prefix_of(self)
1407    }
1408
1409    /// Returns `true` if the given pattern matches a suffix of this
1410    /// string slice.
1411    ///
1412    /// Returns `false` if it does not.
1413    ///
1414    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1415    /// function or closure that determines if a character matches.
1416    ///
1417    /// [`char`]: prim@char
1418    /// [pattern]: self::pattern
1419    ///
1420    /// # Examples
1421    ///
1422    /// ```
1423    /// let bananas = "bananas";
1424    ///
1425    /// assert!(bananas.ends_with("anas"));
1426    /// assert!(!bananas.ends_with("nana"));
1427    /// ```
1428    #[stable(feature = "rust1", since = "1.0.0")]
1429    #[rustc_diagnostic_item = "str_ends_with"]
1430    pub fn ends_with<P: Pattern>(&self, pat: P) -> bool
1431    where
1432        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
1433    {
1434        pat.is_suffix_of(self)
1435    }
1436
1437    /// Returns the byte index of the first character of this string slice that
1438    /// matches the pattern.
1439    ///
1440    /// Returns [`None`] if the pattern doesn't match.
1441    ///
1442    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1443    /// function or closure that determines if a character matches.
1444    ///
1445    /// [`char`]: prim@char
1446    /// [pattern]: self::pattern
1447    ///
1448    /// # Examples
1449    ///
1450    /// Simple patterns:
1451    ///
1452    /// ```
1453    /// let s = "Löwe 老虎 Léopard Gepardi";
1454    ///
1455    /// assert_eq!(s.find('L'), Some(0));
1456    /// assert_eq!(s.find('é'), Some(14));
1457    /// assert_eq!(s.find("pard"), Some(17));
1458    /// ```
1459    ///
1460    /// More complex patterns using point-free style and closures:
1461    ///
1462    /// ```
1463    /// let s = "Löwe 老虎 Léopard";
1464    ///
1465    /// assert_eq!(s.find(char::is_whitespace), Some(5));
1466    /// assert_eq!(s.find(char::is_lowercase), Some(1));
1467    /// assert_eq!(s.find(|c: char| c.is_whitespace() || c.is_lowercase()), Some(1));
1468    /// assert_eq!(s.find(|c: char| (c < 'o') && (c > 'a')), Some(4));
1469    /// ```
1470    ///
1471    /// Not finding the pattern:
1472    ///
1473    /// ```
1474    /// let s = "Löwe 老虎 Léopard";
1475    /// let x: &[_] = &['1', '2'];
1476    ///
1477    /// assert_eq!(s.find(x), None);
1478    /// ```
1479    #[stable(feature = "rust1", since = "1.0.0")]
1480    #[inline]
1481    pub fn find<P: Pattern>(&self, pat: P) -> Option<usize> {
1482        pat.into_searcher(self).next_match().map(|(i, _)| i)
1483    }
1484
1485    /// Returns the byte index for the first character of the last match of the pattern in
1486    /// this string slice.
1487    ///
1488    /// Returns [`None`] if the pattern doesn't match.
1489    ///
1490    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1491    /// function or closure that determines if a character matches.
1492    ///
1493    /// [`char`]: prim@char
1494    /// [pattern]: self::pattern
1495    ///
1496    /// # Examples
1497    ///
1498    /// Simple patterns:
1499    ///
1500    /// ```
1501    /// let s = "Löwe 老虎 Léopard Gepardi";
1502    ///
1503    /// assert_eq!(s.rfind('L'), Some(13));
1504    /// assert_eq!(s.rfind('é'), Some(14));
1505    /// assert_eq!(s.rfind("pard"), Some(24));
1506    /// ```
1507    ///
1508    /// More complex patterns with closures:
1509    ///
1510    /// ```
1511    /// let s = "Löwe 老虎 Léopard";
1512    ///
1513    /// assert_eq!(s.rfind(char::is_whitespace), Some(12));
1514    /// assert_eq!(s.rfind(char::is_lowercase), Some(20));
1515    /// ```
1516    ///
1517    /// Not finding the pattern:
1518    ///
1519    /// ```
1520    /// let s = "Löwe 老虎 Léopard";
1521    /// let x: &[_] = &['1', '2'];
1522    ///
1523    /// assert_eq!(s.rfind(x), None);
1524    /// ```
1525    #[stable(feature = "rust1", since = "1.0.0")]
1526    #[inline]
1527    pub fn rfind<P: Pattern>(&self, pat: P) -> Option<usize>
1528    where
1529        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
1530    {
1531        pat.into_searcher(self).next_match_back().map(|(i, _)| i)
1532    }
1533
1534    /// Returns an iterator over substrings of this string slice, separated by
1535    /// characters matched by a pattern.
1536    ///
1537    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1538    /// function or closure that determines if a character matches.
1539    ///
1540    /// If there are no matches the full string slice is returned as the only
1541    /// item in the iterator.
1542    ///
1543    /// [`char`]: prim@char
1544    /// [pattern]: self::pattern
1545    ///
1546    /// # Iterator behavior
1547    ///
1548    /// The returned iterator will be a [`DoubleEndedIterator`] if the pattern
1549    /// allows a reverse search and forward/reverse search yields the same
1550    /// elements. This is true for, e.g., [`char`], but not for `&str`.
1551    ///
1552    /// If the pattern allows a reverse search but its results might differ
1553    /// from a forward search, the [`rsplit`] method can be used.
1554    ///
1555    /// [`rsplit`]: str::rsplit
1556    ///
1557    /// # Examples
1558    ///
1559    /// Simple patterns:
1560    ///
1561    /// ```
1562    /// let v: Vec<&str> = "Mary had a little lamb".split(' ').collect();
1563    /// assert_eq!(v, ["Mary", "had", "a", "little", "lamb"]);
1564    ///
1565    /// let v: Vec<&str> = "".split('X').collect();
1566    /// assert_eq!(v, [""]);
1567    ///
1568    /// let v: Vec<&str> = "lionXXtigerXleopard".split('X').collect();
1569    /// assert_eq!(v, ["lion", "", "tiger", "leopard"]);
1570    ///
1571    /// let v: Vec<&str> = "lion::tiger::leopard".split("::").collect();
1572    /// assert_eq!(v, ["lion", "tiger", "leopard"]);
1573    ///
1574    /// let v: Vec<&str> = "AABBCC".split("DD").collect();
1575    /// assert_eq!(v, ["AABBCC"]);
1576    ///
1577    /// let v: Vec<&str> = "abc1def2ghi".split(char::is_numeric).collect();
1578    /// assert_eq!(v, ["abc", "def", "ghi"]);
1579    ///
1580    /// let v: Vec<&str> = "lionXtigerXleopard".split(char::is_uppercase).collect();
1581    /// assert_eq!(v, ["lion", "tiger", "leopard"]);
1582    /// ```
1583    ///
1584    /// If the pattern is a slice of chars, split on each occurrence of any of the characters:
1585    ///
1586    /// ```
1587    /// let v: Vec<&str> = "2020-11-03 23:59".split(&['-', ' ', ':', '@'][..]).collect();
1588    /// assert_eq!(v, ["2020", "11", "03", "23", "59"]);
1589    /// ```
1590    ///
1591    /// A more complex pattern, using a closure:
1592    ///
1593    /// ```
1594    /// let v: Vec<&str> = "abc1defXghi".split(|c| c == '1' || c == 'X').collect();
1595    /// assert_eq!(v, ["abc", "def", "ghi"]);
1596    /// ```
1597    ///
1598    /// If a string contains multiple contiguous separators, you will end up
1599    /// with empty strings in the output:
1600    ///
1601    /// ```
1602    /// let x = "||||a||b|c".to_string();
1603    /// let d: Vec<_> = x.split('|').collect();
1604    ///
1605    /// assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
1606    /// ```
1607    ///
1608    /// Contiguous separators are separated by the empty string.
1609    ///
1610    /// ```
1611    /// let x = "(///)".to_string();
1612    /// let d: Vec<_> = x.split('/').collect();
1613    ///
1614    /// assert_eq!(d, &["(", "", "", ")"]);
1615    /// ```
1616    ///
1617    /// Separators at the start or end of a string are neighbored
1618    /// by empty strings.
1619    ///
1620    /// ```
1621    /// let d: Vec<_> = "010".split("0").collect();
1622    /// assert_eq!(d, &["", "1", ""]);
1623    /// ```
1624    ///
1625    /// When the empty string is used as a separator, it separates
1626    /// every character in the string, along with the beginning
1627    /// and end of the string.
1628    ///
1629    /// ```
1630    /// let f: Vec<_> = "rust".split("").collect();
1631    /// assert_eq!(f, &["", "r", "u", "s", "t", ""]);
1632    /// ```
1633    ///
1634    /// Contiguous separators can lead to possibly surprising behavior
1635    /// when whitespace is used as the separator. This code is correct:
1636    ///
1637    /// ```
1638    /// let x = "    a  b c".to_string();
1639    /// let d: Vec<_> = x.split(' ').collect();
1640    ///
1641    /// assert_eq!(d, &["", "", "", "", "a", "", "b", "c"]);
1642    /// ```
1643    ///
1644    /// It does _not_ give you:
1645    ///
1646    /// ```,ignore
1647    /// assert_eq!(d, &["a", "b", "c"]);
1648    /// ```
1649    ///
1650    /// Use [`split_whitespace`] for this behavior.
1651    ///
1652    /// [`split_whitespace`]: str::split_whitespace
1653    #[stable(feature = "rust1", since = "1.0.0")]
1654    #[inline]
1655    pub fn split<P: Pattern>(&self, pat: P) -> Split<'_, P> {
1656        Split(SplitInternal {
1657            start: 0,
1658            end: self.len(),
1659            matcher: pat.into_searcher(self),
1660            allow_trailing_empty: true,
1661            finished: false,
1662        })
1663    }
1664
1665    /// Returns an iterator over substrings of this string slice, separated by
1666    /// characters matched by a pattern.
1667    ///
1668    /// Differs from the iterator produced by `split` in that `split_inclusive`
1669    /// leaves the matched part as the terminator of the substring.
1670    ///
1671    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1672    /// function or closure that determines if a character matches.
1673    ///
1674    /// [`char`]: prim@char
1675    /// [pattern]: self::pattern
1676    ///
1677    /// # Examples
1678    ///
1679    /// ```
1680    /// let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb."
1681    ///     .split_inclusive('\n').collect();
1682    /// assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb."]);
1683    /// ```
1684    ///
1685    /// If the last element of the string is matched,
1686    /// that element will be considered the terminator of the preceding substring.
1687    /// That substring will be the last item returned by the iterator.
1688    ///
1689    /// ```
1690    /// let v: Vec<&str> = "Mary had a little lamb\nlittle lamb\nlittle lamb.\n"
1691    ///     .split_inclusive('\n').collect();
1692    /// assert_eq!(v, ["Mary had a little lamb\n", "little lamb\n", "little lamb.\n"]);
1693    /// ```
1694    #[stable(feature = "split_inclusive", since = "1.51.0")]
1695    #[inline]
1696    pub fn split_inclusive<P: Pattern>(&self, pat: P) -> SplitInclusive<'_, P> {
1697        SplitInclusive(SplitInternal {
1698            start: 0,
1699            end: self.len(),
1700            matcher: pat.into_searcher(self),
1701            allow_trailing_empty: false,
1702            finished: false,
1703        })
1704    }
1705
1706    /// Returns an iterator over substrings of the given string slice, separated
1707    /// by characters matched by a pattern and yielded in reverse order.
1708    ///
1709    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1710    /// function or closure that determines if a character matches.
1711    ///
1712    /// [`char`]: prim@char
1713    /// [pattern]: self::pattern
1714    ///
1715    /// # Iterator behavior
1716    ///
1717    /// The returned iterator requires that the pattern supports a reverse
1718    /// search, and it will be a [`DoubleEndedIterator`] if a forward/reverse
1719    /// search yields the same elements.
1720    ///
1721    /// For iterating from the front, the [`split`] method can be used.
1722    ///
1723    /// [`split`]: str::split
1724    ///
1725    /// # Examples
1726    ///
1727    /// Simple patterns:
1728    ///
1729    /// ```
1730    /// let v: Vec<&str> = "Mary had a little lamb".rsplit(' ').collect();
1731    /// assert_eq!(v, ["lamb", "little", "a", "had", "Mary"]);
1732    ///
1733    /// let v: Vec<&str> = "".rsplit('X').collect();
1734    /// assert_eq!(v, [""]);
1735    ///
1736    /// let v: Vec<&str> = "lionXXtigerXleopard".rsplit('X').collect();
1737    /// assert_eq!(v, ["leopard", "tiger", "", "lion"]);
1738    ///
1739    /// let v: Vec<&str> = "lion::tiger::leopard".rsplit("::").collect();
1740    /// assert_eq!(v, ["leopard", "tiger", "lion"]);
1741    /// ```
1742    ///
1743    /// A more complex pattern, using a closure:
1744    ///
1745    /// ```
1746    /// let v: Vec<&str> = "abc1defXghi".rsplit(|c| c == '1' || c == 'X').collect();
1747    /// assert_eq!(v, ["ghi", "def", "abc"]);
1748    /// ```
1749    #[stable(feature = "rust1", since = "1.0.0")]
1750    #[inline]
1751    pub fn rsplit<P: Pattern>(&self, pat: P) -> RSplit<'_, P>
1752    where
1753        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
1754    {
1755        RSplit(self.split(pat).0)
1756    }
1757
1758    /// Returns an iterator over substrings of the given string slice, separated
1759    /// by characters matched by a pattern.
1760    ///
1761    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1762    /// function or closure that determines if a character matches.
1763    ///
1764    /// [`char`]: prim@char
1765    /// [pattern]: self::pattern
1766    ///
1767    /// Equivalent to [`split`], except that the trailing substring
1768    /// is skipped if empty.
1769    ///
1770    /// [`split`]: str::split
1771    ///
1772    /// This method can be used for string data that is _terminated_,
1773    /// rather than _separated_ by a pattern.
1774    ///
1775    /// # Iterator behavior
1776    ///
1777    /// The returned iterator will be a [`DoubleEndedIterator`] if the pattern
1778    /// allows a reverse search and forward/reverse search yields the same
1779    /// elements. This is true for, e.g., [`char`], but not for `&str`.
1780    ///
1781    /// If the pattern allows a reverse search but its results might differ
1782    /// from a forward search, the [`rsplit_terminator`] method can be used.
1783    ///
1784    /// [`rsplit_terminator`]: str::rsplit_terminator
1785    ///
1786    /// # Examples
1787    ///
1788    /// ```
1789    /// let v: Vec<&str> = "A.B.".split_terminator('.').collect();
1790    /// assert_eq!(v, ["A", "B"]);
1791    ///
1792    /// let v: Vec<&str> = "A..B..".split_terminator(".").collect();
1793    /// assert_eq!(v, ["A", "", "B", ""]);
1794    ///
1795    /// let v: Vec<&str> = "A.B:C.D".split_terminator(&['.', ':'][..]).collect();
1796    /// assert_eq!(v, ["A", "B", "C", "D"]);
1797    /// ```
1798    #[stable(feature = "rust1", since = "1.0.0")]
1799    #[inline]
1800    pub fn split_terminator<P: Pattern>(&self, pat: P) -> SplitTerminator<'_, P> {
1801        SplitTerminator(SplitInternal { allow_trailing_empty: false, ..self.split(pat).0 })
1802    }
1803
1804    /// Returns an iterator over substrings of `self`, separated by characters
1805    /// matched by a pattern and yielded in reverse order.
1806    ///
1807    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1808    /// function or closure that determines if a character matches.
1809    ///
1810    /// [`char`]: prim@char
1811    /// [pattern]: self::pattern
1812    ///
1813    /// Equivalent to [`split`], except that the trailing substring is
1814    /// skipped if empty.
1815    ///
1816    /// [`split`]: str::split
1817    ///
1818    /// This method can be used for string data that is _terminated_,
1819    /// rather than _separated_ by a pattern.
1820    ///
1821    /// # Iterator behavior
1822    ///
1823    /// The returned iterator requires that the pattern supports a
1824    /// reverse search, and it will be double ended if a forward/reverse
1825    /// search yields the same elements.
1826    ///
1827    /// For iterating from the front, the [`split_terminator`] method can be
1828    /// used.
1829    ///
1830    /// [`split_terminator`]: str::split_terminator
1831    ///
1832    /// # Examples
1833    ///
1834    /// ```
1835    /// let v: Vec<&str> = "A.B.".rsplit_terminator('.').collect();
1836    /// assert_eq!(v, ["B", "A"]);
1837    ///
1838    /// let v: Vec<&str> = "A..B..".rsplit_terminator(".").collect();
1839    /// assert_eq!(v, ["", "B", "", "A"]);
1840    ///
1841    /// let v: Vec<&str> = "A.B:C.D".rsplit_terminator(&['.', ':'][..]).collect();
1842    /// assert_eq!(v, ["D", "C", "B", "A"]);
1843    /// ```
1844    #[stable(feature = "rust1", since = "1.0.0")]
1845    #[inline]
1846    pub fn rsplit_terminator<P: Pattern>(&self, pat: P) -> RSplitTerminator<'_, P>
1847    where
1848        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
1849    {
1850        RSplitTerminator(self.split_terminator(pat).0)
1851    }
1852
1853    /// Returns an iterator over substrings of the given string slice, separated
1854    /// by a pattern, restricted to returning at most `n` items.
1855    ///
1856    /// If `n` substrings are returned, the last substring (the `n`th substring)
1857    /// will contain the remainder of the string.
1858    ///
1859    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1860    /// function or closure that determines if a character matches.
1861    ///
1862    /// [`char`]: prim@char
1863    /// [pattern]: self::pattern
1864    ///
1865    /// # Iterator behavior
1866    ///
1867    /// The returned iterator will not be double ended, because it is
1868    /// not efficient to support.
1869    ///
1870    /// If the pattern allows a reverse search, the [`rsplitn`] method can be
1871    /// used.
1872    ///
1873    /// [`rsplitn`]: str::rsplitn
1874    ///
1875    /// # Examples
1876    ///
1877    /// Simple patterns:
1878    ///
1879    /// ```
1880    /// let v: Vec<&str> = "Mary had a little lambda".splitn(3, ' ').collect();
1881    /// assert_eq!(v, ["Mary", "had", "a little lambda"]);
1882    ///
1883    /// let v: Vec<&str> = "lionXXtigerXleopard".splitn(3, "X").collect();
1884    /// assert_eq!(v, ["lion", "", "tigerXleopard"]);
1885    ///
1886    /// let v: Vec<&str> = "abcXdef".splitn(1, 'X').collect();
1887    /// assert_eq!(v, ["abcXdef"]);
1888    ///
1889    /// let v: Vec<&str> = "".splitn(1, 'X').collect();
1890    /// assert_eq!(v, [""]);
1891    /// ```
1892    ///
1893    /// A more complex pattern, using a closure:
1894    ///
1895    /// ```
1896    /// let v: Vec<&str> = "abc1defXghi".splitn(2, |c| c == '1' || c == 'X').collect();
1897    /// assert_eq!(v, ["abc", "defXghi"]);
1898    /// ```
1899    #[stable(feature = "rust1", since = "1.0.0")]
1900    #[inline]
1901    pub fn splitn<P: Pattern>(&self, n: usize, pat: P) -> SplitN<'_, P> {
1902        SplitN(SplitNInternal { iter: self.split(pat).0, count: n })
1903    }
1904
1905    /// Returns an iterator over substrings of this string slice, separated by a
1906    /// pattern, starting from the end of the string, restricted to returning at
1907    /// most `n` items.
1908    ///
1909    /// If `n` substrings are returned, the last substring (the `n`th substring)
1910    /// will contain the remainder of the string.
1911    ///
1912    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
1913    /// function or closure that determines if a character matches.
1914    ///
1915    /// [`char`]: prim@char
1916    /// [pattern]: self::pattern
1917    ///
1918    /// # Iterator behavior
1919    ///
1920    /// The returned iterator will not be double ended, because it is not
1921    /// efficient to support.
1922    ///
1923    /// For splitting from the front, the [`splitn`] method can be used.
1924    ///
1925    /// [`splitn`]: str::splitn
1926    ///
1927    /// # Examples
1928    ///
1929    /// Simple patterns:
1930    ///
1931    /// ```
1932    /// let v: Vec<&str> = "Mary had a little lamb".rsplitn(3, ' ').collect();
1933    /// assert_eq!(v, ["lamb", "little", "Mary had a"]);
1934    ///
1935    /// let v: Vec<&str> = "lionXXtigerXleopard".rsplitn(3, 'X').collect();
1936    /// assert_eq!(v, ["leopard", "tiger", "lionX"]);
1937    ///
1938    /// let v: Vec<&str> = "lion::tiger::leopard".rsplitn(2, "::").collect();
1939    /// assert_eq!(v, ["leopard", "lion::tiger"]);
1940    /// ```
1941    ///
1942    /// A more complex pattern, using a closure:
1943    ///
1944    /// ```
1945    /// let v: Vec<&str> = "abc1defXghi".rsplitn(2, |c| c == '1' || c == 'X').collect();
1946    /// assert_eq!(v, ["ghi", "abc1def"]);
1947    /// ```
1948    #[stable(feature = "rust1", since = "1.0.0")]
1949    #[inline]
1950    pub fn rsplitn<P: Pattern>(&self, n: usize, pat: P) -> RSplitN<'_, P>
1951    where
1952        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
1953    {
1954        RSplitN(self.splitn(n, pat).0)
1955    }
1956
1957    /// Splits the string on the first occurrence of the specified delimiter and
1958    /// returns prefix before delimiter and suffix after delimiter.
1959    ///
1960    /// # Examples
1961    ///
1962    /// ```
1963    /// assert_eq!("cfg".split_once('='), None);
1964    /// assert_eq!("cfg=".split_once('='), Some(("cfg", "")));
1965    /// assert_eq!("cfg=foo".split_once('='), Some(("cfg", "foo")));
1966    /// assert_eq!("cfg=foo=bar".split_once('='), Some(("cfg", "foo=bar")));
1967    /// ```
1968    #[stable(feature = "str_split_once", since = "1.52.0")]
1969    #[inline]
1970    pub fn split_once<P: Pattern>(&self, delimiter: P) -> Option<(&'_ str, &'_ str)> {
1971        let (start, end) = delimiter.into_searcher(self).next_match()?;
1972        // SAFETY: `Searcher` is known to return valid indices.
1973        unsafe { Some((self.get_unchecked(..start), self.get_unchecked(end..))) }
1974    }
1975
1976    /// Splits the string on the last occurrence of the specified delimiter and
1977    /// returns prefix before delimiter and suffix after delimiter.
1978    ///
1979    /// # Examples
1980    ///
1981    /// ```
1982    /// assert_eq!("cfg".rsplit_once('='), None);
1983    /// assert_eq!("cfg=".rsplit_once('='), Some(("cfg", "")));
1984    /// assert_eq!("cfg=foo".rsplit_once('='), Some(("cfg", "foo")));
1985    /// assert_eq!("cfg=foo=bar".rsplit_once('='), Some(("cfg=foo", "bar")));
1986    /// ```
1987    #[stable(feature = "str_split_once", since = "1.52.0")]
1988    #[inline]
1989    pub fn rsplit_once<P: Pattern>(&self, delimiter: P) -> Option<(&'_ str, &'_ str)>
1990    where
1991        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
1992    {
1993        let (start, end) = delimiter.into_searcher(self).next_match_back()?;
1994        // SAFETY: `Searcher` is known to return valid indices.
1995        unsafe { Some((self.get_unchecked(..start), self.get_unchecked(end..))) }
1996    }
1997
1998    /// Returns an iterator over the disjoint matches of a pattern within the
1999    /// given string slice.
2000    ///
2001    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2002    /// function or closure that determines if a character matches.
2003    ///
2004    /// [`char`]: prim@char
2005    /// [pattern]: self::pattern
2006    ///
2007    /// # Iterator behavior
2008    ///
2009    /// The returned iterator will be a [`DoubleEndedIterator`] if the pattern
2010    /// allows a reverse search and forward/reverse search yields the same
2011    /// elements. This is true for, e.g., [`char`], but not for `&str`.
2012    ///
2013    /// If the pattern allows a reverse search but its results might differ
2014    /// from a forward search, the [`rmatches`] method can be used.
2015    ///
2016    /// [`rmatches`]: str::rmatches
2017    ///
2018    /// # Examples
2019    ///
2020    /// ```
2021    /// let v: Vec<&str> = "abcXXXabcYYYabc".matches("abc").collect();
2022    /// assert_eq!(v, ["abc", "abc", "abc"]);
2023    ///
2024    /// let v: Vec<&str> = "1abc2abc3".matches(char::is_numeric).collect();
2025    /// assert_eq!(v, ["1", "2", "3"]);
2026    /// ```
2027    #[stable(feature = "str_matches", since = "1.2.0")]
2028    #[inline]
2029    pub fn matches<P: Pattern>(&self, pat: P) -> Matches<'_, P> {
2030        Matches(MatchesInternal(pat.into_searcher(self)))
2031    }
2032
2033    /// Returns an iterator over the disjoint matches of a pattern within this
2034    /// string slice, yielded in reverse order.
2035    ///
2036    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2037    /// function or closure that determines if a character matches.
2038    ///
2039    /// [`char`]: prim@char
2040    /// [pattern]: self::pattern
2041    ///
2042    /// # Iterator behavior
2043    ///
2044    /// The returned iterator requires that the pattern supports a reverse
2045    /// search, and it will be a [`DoubleEndedIterator`] if a forward/reverse
2046    /// search yields the same elements.
2047    ///
2048    /// For iterating from the front, the [`matches`] method can be used.
2049    ///
2050    /// [`matches`]: str::matches
2051    ///
2052    /// # Examples
2053    ///
2054    /// ```
2055    /// let v: Vec<&str> = "abcXXXabcYYYabc".rmatches("abc").collect();
2056    /// assert_eq!(v, ["abc", "abc", "abc"]);
2057    ///
2058    /// let v: Vec<&str> = "1abc2abc3".rmatches(char::is_numeric).collect();
2059    /// assert_eq!(v, ["3", "2", "1"]);
2060    /// ```
2061    #[stable(feature = "str_matches", since = "1.2.0")]
2062    #[inline]
2063    pub fn rmatches<P: Pattern>(&self, pat: P) -> RMatches<'_, P>
2064    where
2065        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
2066    {
2067        RMatches(self.matches(pat).0)
2068    }
2069
2070    /// Returns an iterator over the disjoint matches of a pattern within this string
2071    /// slice as well as the index that the match starts at.
2072    ///
2073    /// For matches of `pat` within `self` that overlap, only the indices
2074    /// corresponding to the first match are returned.
2075    ///
2076    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2077    /// function or closure that determines if a character matches.
2078    ///
2079    /// [`char`]: prim@char
2080    /// [pattern]: self::pattern
2081    ///
2082    /// # Iterator behavior
2083    ///
2084    /// The returned iterator will be a [`DoubleEndedIterator`] if the pattern
2085    /// allows a reverse search and forward/reverse search yields the same
2086    /// elements. This is true for, e.g., [`char`], but not for `&str`.
2087    ///
2088    /// If the pattern allows a reverse search but its results might differ
2089    /// from a forward search, the [`rmatch_indices`] method can be used.
2090    ///
2091    /// [`rmatch_indices`]: str::rmatch_indices
2092    ///
2093    /// # Examples
2094    ///
2095    /// ```
2096    /// let v: Vec<_> = "abcXXXabcYYYabc".match_indices("abc").collect();
2097    /// assert_eq!(v, [(0, "abc"), (6, "abc"), (12, "abc")]);
2098    ///
2099    /// let v: Vec<_> = "1abcabc2".match_indices("abc").collect();
2100    /// assert_eq!(v, [(1, "abc"), (4, "abc")]);
2101    ///
2102    /// let v: Vec<_> = "ababa".match_indices("aba").collect();
2103    /// assert_eq!(v, [(0, "aba")]); // only the first `aba`
2104    /// ```
2105    #[stable(feature = "str_match_indices", since = "1.5.0")]
2106    #[inline]
2107    pub fn match_indices<P: Pattern>(&self, pat: P) -> MatchIndices<'_, P> {
2108        MatchIndices(MatchIndicesInternal(pat.into_searcher(self)))
2109    }
2110
2111    /// Returns an iterator over the disjoint matches of a pattern within `self`,
2112    /// yielded in reverse order along with the index of the match.
2113    ///
2114    /// For matches of `pat` within `self` that overlap, only the indices
2115    /// corresponding to the last match are returned.
2116    ///
2117    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2118    /// function or closure that determines if a character matches.
2119    ///
2120    /// [`char`]: prim@char
2121    /// [pattern]: self::pattern
2122    ///
2123    /// # Iterator behavior
2124    ///
2125    /// The returned iterator requires that the pattern supports a reverse
2126    /// search, and it will be a [`DoubleEndedIterator`] if a forward/reverse
2127    /// search yields the same elements.
2128    ///
2129    /// For iterating from the front, the [`match_indices`] method can be used.
2130    ///
2131    /// [`match_indices`]: str::match_indices
2132    ///
2133    /// # Examples
2134    ///
2135    /// ```
2136    /// let v: Vec<_> = "abcXXXabcYYYabc".rmatch_indices("abc").collect();
2137    /// assert_eq!(v, [(12, "abc"), (6, "abc"), (0, "abc")]);
2138    ///
2139    /// let v: Vec<_> = "1abcabc2".rmatch_indices("abc").collect();
2140    /// assert_eq!(v, [(4, "abc"), (1, "abc")]);
2141    ///
2142    /// let v: Vec<_> = "ababa".rmatch_indices("aba").collect();
2143    /// assert_eq!(v, [(2, "aba")]); // only the last `aba`
2144    /// ```
2145    #[stable(feature = "str_match_indices", since = "1.5.0")]
2146    #[inline]
2147    pub fn rmatch_indices<P: Pattern>(&self, pat: P) -> RMatchIndices<'_, P>
2148    where
2149        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
2150    {
2151        RMatchIndices(self.match_indices(pat).0)
2152    }
2153
2154    /// Returns a string slice with leading and trailing whitespace removed.
2155    ///
2156    /// 'Whitespace' is defined according to the terms of the Unicode Derived
2157    /// Core Property `White_Space`, which includes newlines.
2158    ///
2159    /// # Examples
2160    ///
2161    /// ```
2162    /// let s = "\n Hello\tworld\t\n";
2163    ///
2164    /// assert_eq!("Hello\tworld", s.trim());
2165    /// ```
2166    #[inline]
2167    #[must_use = "this returns the trimmed string as a slice, \
2168                  without modifying the original"]
2169    #[stable(feature = "rust1", since = "1.0.0")]
2170    #[rustc_diagnostic_item = "str_trim"]
2171    pub fn trim(&self) -> &str {
2172        self.trim_matches(char::is_whitespace)
2173    }
2174
2175    /// Returns a string slice with leading whitespace removed.
2176    ///
2177    /// 'Whitespace' is defined according to the terms of the Unicode Derived
2178    /// Core Property `White_Space`, which includes newlines.
2179    ///
2180    /// # Text directionality
2181    ///
2182    /// A string is a sequence of bytes. `start` in this context means the first
2183    /// position of that byte string; for a left-to-right language like English or
2184    /// Russian, this will be left side, and for right-to-left languages like
2185    /// Arabic or Hebrew, this will be the right side.
2186    ///
2187    /// # Examples
2188    ///
2189    /// Basic usage:
2190    ///
2191    /// ```
2192    /// let s = "\n Hello\tworld\t\n";
2193    /// assert_eq!("Hello\tworld\t\n", s.trim_start());
2194    /// ```
2195    ///
2196    /// Directionality:
2197    ///
2198    /// ```
2199    /// let s = "  English  ";
2200    /// assert!(Some('E') == s.trim_start().chars().next());
2201    ///
2202    /// let s = "  עברית  ";
2203    /// assert!(Some('ע') == s.trim_start().chars().next());
2204    /// ```
2205    #[inline]
2206    #[must_use = "this returns the trimmed string as a new slice, \
2207                  without modifying the original"]
2208    #[stable(feature = "trim_direction", since = "1.30.0")]
2209    #[rustc_diagnostic_item = "str_trim_start"]
2210    pub fn trim_start(&self) -> &str {
2211        self.trim_start_matches(char::is_whitespace)
2212    }
2213
2214    /// Returns a string slice with trailing whitespace removed.
2215    ///
2216    /// 'Whitespace' is defined according to the terms of the Unicode Derived
2217    /// Core Property `White_Space`, which includes newlines.
2218    ///
2219    /// # Text directionality
2220    ///
2221    /// A string is a sequence of bytes. `end` in this context means the last
2222    /// position of that byte string; for a left-to-right language like English or
2223    /// Russian, this will be right side, and for right-to-left languages like
2224    /// Arabic or Hebrew, this will be the left side.
2225    ///
2226    /// # Examples
2227    ///
2228    /// Basic usage:
2229    ///
2230    /// ```
2231    /// let s = "\n Hello\tworld\t\n";
2232    /// assert_eq!("\n Hello\tworld", s.trim_end());
2233    /// ```
2234    ///
2235    /// Directionality:
2236    ///
2237    /// ```
2238    /// let s = "  English  ";
2239    /// assert!(Some('h') == s.trim_end().chars().rev().next());
2240    ///
2241    /// let s = "  עברית  ";
2242    /// assert!(Some('ת') == s.trim_end().chars().rev().next());
2243    /// ```
2244    #[inline]
2245    #[must_use = "this returns the trimmed string as a new slice, \
2246                  without modifying the original"]
2247    #[stable(feature = "trim_direction", since = "1.30.0")]
2248    #[rustc_diagnostic_item = "str_trim_end"]
2249    pub fn trim_end(&self) -> &str {
2250        self.trim_end_matches(char::is_whitespace)
2251    }
2252
2253    /// Returns a string slice with leading whitespace removed.
2254    ///
2255    /// 'Whitespace' is defined according to the terms of the Unicode Derived
2256    /// Core Property `White_Space`.
2257    ///
2258    /// # Text directionality
2259    ///
2260    /// A string is a sequence of bytes. 'Left' in this context means the first
2261    /// position of that byte string; for a language like Arabic or Hebrew
2262    /// which are 'right to left' rather than 'left to right', this will be
2263    /// the _right_ side, not the left.
2264    ///
2265    /// # Examples
2266    ///
2267    /// Basic usage:
2268    ///
2269    /// ```
2270    /// let s = " Hello\tworld\t";
2271    ///
2272    /// assert_eq!("Hello\tworld\t", s.trim_left());
2273    /// ```
2274    ///
2275    /// Directionality:
2276    ///
2277    /// ```
2278    /// let s = "  English";
2279    /// assert!(Some('E') == s.trim_left().chars().next());
2280    ///
2281    /// let s = "  עברית";
2282    /// assert!(Some('ע') == s.trim_left().chars().next());
2283    /// ```
2284    #[must_use = "this returns the trimmed string as a new slice, \
2285                  without modifying the original"]
2286    #[inline]
2287    #[stable(feature = "rust1", since = "1.0.0")]
2288    #[deprecated(since = "1.33.0", note = "superseded by `trim_start`", suggestion = "trim_start")]
2289    pub fn trim_left(&self) -> &str {
2290        self.trim_start()
2291    }
2292
2293    /// Returns a string slice with trailing whitespace removed.
2294    ///
2295    /// 'Whitespace' is defined according to the terms of the Unicode Derived
2296    /// Core Property `White_Space`.
2297    ///
2298    /// # Text directionality
2299    ///
2300    /// A string is a sequence of bytes. 'Right' in this context means the last
2301    /// position of that byte string; for a language like Arabic or Hebrew
2302    /// which are 'right to left' rather than 'left to right', this will be
2303    /// the _left_ side, not the right.
2304    ///
2305    /// # Examples
2306    ///
2307    /// Basic usage:
2308    ///
2309    /// ```
2310    /// let s = " Hello\tworld\t";
2311    ///
2312    /// assert_eq!(" Hello\tworld", s.trim_right());
2313    /// ```
2314    ///
2315    /// Directionality:
2316    ///
2317    /// ```
2318    /// let s = "English  ";
2319    /// assert!(Some('h') == s.trim_right().chars().rev().next());
2320    ///
2321    /// let s = "עברית  ";
2322    /// assert!(Some('ת') == s.trim_right().chars().rev().next());
2323    /// ```
2324    #[must_use = "this returns the trimmed string as a new slice, \
2325                  without modifying the original"]
2326    #[inline]
2327    #[stable(feature = "rust1", since = "1.0.0")]
2328    #[deprecated(since = "1.33.0", note = "superseded by `trim_end`", suggestion = "trim_end")]
2329    pub fn trim_right(&self) -> &str {
2330        self.trim_end()
2331    }
2332
2333    /// Returns a string slice with all prefixes and suffixes that match a
2334    /// pattern repeatedly removed.
2335    ///
2336    /// The [pattern] can be a [`char`], a slice of [`char`]s, or a function
2337    /// or closure that determines if a character matches.
2338    ///
2339    /// [`char`]: prim@char
2340    /// [pattern]: self::pattern
2341    ///
2342    /// # Examples
2343    ///
2344    /// Simple patterns:
2345    ///
2346    /// ```
2347    /// assert_eq!("11foo1bar11".trim_matches('1'), "foo1bar");
2348    /// assert_eq!("123foo1bar123".trim_matches(char::is_numeric), "foo1bar");
2349    ///
2350    /// let x: &[_] = &['1', '2'];
2351    /// assert_eq!("12foo1bar12".trim_matches(x), "foo1bar");
2352    /// ```
2353    ///
2354    /// A more complex pattern, using a closure:
2355    ///
2356    /// ```
2357    /// assert_eq!("1foo1barXX".trim_matches(|c| c == '1' || c == 'X'), "foo1bar");
2358    /// ```
2359    #[must_use = "this returns the trimmed string as a new slice, \
2360                  without modifying the original"]
2361    #[stable(feature = "rust1", since = "1.0.0")]
2362    pub fn trim_matches<P: Pattern>(&self, pat: P) -> &str
2363    where
2364        for<'a> P::Searcher<'a>: DoubleEndedSearcher<'a>,
2365    {
2366        let mut i = 0;
2367        let mut j = 0;
2368        let mut matcher = pat.into_searcher(self);
2369        if let Some((a, b)) = matcher.next_reject() {
2370            i = a;
2371            j = b; // Remember earliest known match, correct it below if
2372            // last match is different
2373        }
2374        if let Some((_, b)) = matcher.next_reject_back() {
2375            j = b;
2376        }
2377        // SAFETY: `Searcher` is known to return valid indices.
2378        unsafe { self.get_unchecked(i..j) }
2379    }
2380
2381    /// Returns a string slice with all prefixes that match a pattern
2382    /// repeatedly removed.
2383    ///
2384    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2385    /// function or closure that determines if a character matches.
2386    ///
2387    /// [`char`]: prim@char
2388    /// [pattern]: self::pattern
2389    ///
2390    /// # Text directionality
2391    ///
2392    /// A string is a sequence of bytes. `start` in this context means the first
2393    /// position of that byte string; for a left-to-right language like English or
2394    /// Russian, this will be left side, and for right-to-left languages like
2395    /// Arabic or Hebrew, this will be the right side.
2396    ///
2397    /// # Examples
2398    ///
2399    /// ```
2400    /// assert_eq!("11foo1bar11".trim_start_matches('1'), "foo1bar11");
2401    /// assert_eq!("123foo1bar123".trim_start_matches(char::is_numeric), "foo1bar123");
2402    ///
2403    /// let x: &[_] = &['1', '2'];
2404    /// assert_eq!("12foo1bar12".trim_start_matches(x), "foo1bar12");
2405    /// ```
2406    #[must_use = "this returns the trimmed string as a new slice, \
2407                  without modifying the original"]
2408    #[stable(feature = "trim_direction", since = "1.30.0")]
2409    pub fn trim_start_matches<P: Pattern>(&self, pat: P) -> &str {
2410        let mut i = self.len();
2411        let mut matcher = pat.into_searcher(self);
2412        if let Some((a, _)) = matcher.next_reject() {
2413            i = a;
2414        }
2415        // SAFETY: `Searcher` is known to return valid indices.
2416        unsafe { self.get_unchecked(i..self.len()) }
2417    }
2418
2419    /// Returns a string slice with the prefix removed.
2420    ///
2421    /// If the string starts with the pattern `prefix`, returns the substring after the prefix,
2422    /// wrapped in `Some`. Unlike [`trim_start_matches`], this method removes the prefix exactly once.
2423    ///
2424    /// If the string does not start with `prefix`, returns `None`.
2425    ///
2426    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2427    /// function or closure that determines if a character matches.
2428    ///
2429    /// [`char`]: prim@char
2430    /// [pattern]: self::pattern
2431    /// [`trim_start_matches`]: Self::trim_start_matches
2432    ///
2433    /// # Examples
2434    ///
2435    /// ```
2436    /// assert_eq!("foo:bar".strip_prefix("foo:"), Some("bar"));
2437    /// assert_eq!("foo:bar".strip_prefix("bar"), None);
2438    /// assert_eq!("foofoo".strip_prefix("foo"), Some("foo"));
2439    /// ```
2440    #[must_use = "this returns the remaining substring as a new slice, \
2441                  without modifying the original"]
2442    #[stable(feature = "str_strip", since = "1.45.0")]
2443    pub fn strip_prefix<P: Pattern>(&self, prefix: P) -> Option<&str> {
2444        prefix.strip_prefix_of(self)
2445    }
2446
2447    /// Returns a string slice with the suffix removed.
2448    ///
2449    /// If the string ends with the pattern `suffix`, returns the substring before the suffix,
2450    /// wrapped in `Some`.  Unlike [`trim_end_matches`], this method removes the suffix exactly once.
2451    ///
2452    /// If the string does not end with `suffix`, returns `None`.
2453    ///
2454    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2455    /// function or closure that determines if a character matches.
2456    ///
2457    /// [`char`]: prim@char
2458    /// [pattern]: self::pattern
2459    /// [`trim_end_matches`]: Self::trim_end_matches
2460    ///
2461    /// # Examples
2462    ///
2463    /// ```
2464    /// assert_eq!("bar:foo".strip_suffix(":foo"), Some("bar"));
2465    /// assert_eq!("bar:foo".strip_suffix("bar"), None);
2466    /// assert_eq!("foofoo".strip_suffix("foo"), Some("foo"));
2467    /// ```
2468    #[must_use = "this returns the remaining substring as a new slice, \
2469                  without modifying the original"]
2470    #[stable(feature = "str_strip", since = "1.45.0")]
2471    pub fn strip_suffix<P: Pattern>(&self, suffix: P) -> Option<&str>
2472    where
2473        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
2474    {
2475        suffix.strip_suffix_of(self)
2476    }
2477
2478    /// Returns a string slice with the prefix and suffix removed.
2479    ///
2480    /// If the string starts with the pattern `prefix` and ends with the pattern `suffix`, returns
2481    /// the substring after the prefix and before the suffix, wrapped in `Some`.
2482    /// Unlike [`trim_start_matches`] and [`trim_end_matches`], this method removes both the prefix
2483    /// and suffix exactly once.
2484    ///
2485    /// If the string does not start with `prefix` or does not end with `suffix`, returns `None`.
2486    ///
2487    /// Each [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2488    /// function or closure that determines if a character matches.
2489    ///
2490    /// [`char`]: prim@char
2491    /// [pattern]: self::pattern
2492    /// [`trim_start_matches`]: Self::trim_start_matches
2493    /// [`trim_end_matches`]: Self::trim_end_matches
2494    ///
2495    /// # Examples
2496    ///
2497    /// ```
2498    /// #![feature(strip_circumfix)]
2499    ///
2500    /// assert_eq!("bar:hello:foo".strip_circumfix("bar:", ":foo"), Some("hello"));
2501    /// assert_eq!("bar:foo".strip_circumfix("foo", "foo"), None);
2502    /// assert_eq!("foo:bar;".strip_circumfix("foo:", ';'), Some("bar"));
2503    /// ```
2504    #[must_use = "this returns the remaining substring as a new slice, \
2505                  without modifying the original"]
2506    #[unstable(feature = "strip_circumfix", issue = "147946")]
2507    pub fn strip_circumfix<P: Pattern, S: Pattern>(&self, prefix: P, suffix: S) -> Option<&str>
2508    where
2509        for<'a> S::Searcher<'a>: ReverseSearcher<'a>,
2510    {
2511        self.strip_prefix(prefix)?.strip_suffix(suffix)
2512    }
2513
2514    /// Returns a string slice with the optional prefix removed.
2515    ///
2516    /// If the string starts with the pattern `prefix`, returns the substring after the prefix.
2517    /// Unlike [`strip_prefix`], this method always returns `&str` for easy method chaining,
2518    /// instead of returning [`Option<&str>`].
2519    ///
2520    /// If the string does not start with `prefix`, returns the original string unchanged.
2521    ///
2522    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2523    /// function or closure that determines if a character matches.
2524    ///
2525    /// [`char`]: prim@char
2526    /// [pattern]: self::pattern
2527    /// [`strip_prefix`]: Self::strip_prefix
2528    ///
2529    /// # Examples
2530    ///
2531    /// ```
2532    /// #![feature(trim_prefix_suffix)]
2533    ///
2534    /// // Prefix present - removes it
2535    /// assert_eq!("foo:bar".trim_prefix("foo:"), "bar");
2536    /// assert_eq!("foofoo".trim_prefix("foo"), "foo");
2537    ///
2538    /// // Prefix absent - returns original string
2539    /// assert_eq!("foo:bar".trim_prefix("bar"), "foo:bar");
2540    ///
2541    /// // Method chaining example
2542    /// assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
2543    /// ```
2544    #[must_use = "this returns the remaining substring as a new slice, \
2545                  without modifying the original"]
2546    #[unstable(feature = "trim_prefix_suffix", issue = "142312")]
2547    pub fn trim_prefix<P: Pattern>(&self, prefix: P) -> &str {
2548        prefix.strip_prefix_of(self).unwrap_or(self)
2549    }
2550
2551    /// Returns a string slice with the optional suffix removed.
2552    ///
2553    /// If the string ends with the pattern `suffix`, returns the substring before the suffix.
2554    /// Unlike [`strip_suffix`], this method always returns `&str` for easy method chaining,
2555    /// instead of returning [`Option<&str>`].
2556    ///
2557    /// If the string does not end with `suffix`, returns the original string unchanged.
2558    ///
2559    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2560    /// function or closure that determines if a character matches.
2561    ///
2562    /// [`char`]: prim@char
2563    /// [pattern]: self::pattern
2564    /// [`strip_suffix`]: Self::strip_suffix
2565    ///
2566    /// # Examples
2567    ///
2568    /// ```
2569    /// #![feature(trim_prefix_suffix)]
2570    ///
2571    /// // Suffix present - removes it
2572    /// assert_eq!("bar:foo".trim_suffix(":foo"), "bar");
2573    /// assert_eq!("foofoo".trim_suffix("foo"), "foo");
2574    ///
2575    /// // Suffix absent - returns original string
2576    /// assert_eq!("bar:foo".trim_suffix("bar"), "bar:foo");
2577    ///
2578    /// // Method chaining example
2579    /// assert_eq!("<https://example.com/>".trim_prefix('<').trim_suffix('>'), "https://example.com/");
2580    /// ```
2581    #[must_use = "this returns the remaining substring as a new slice, \
2582                  without modifying the original"]
2583    #[unstable(feature = "trim_prefix_suffix", issue = "142312")]
2584    pub fn trim_suffix<P: Pattern>(&self, suffix: P) -> &str
2585    where
2586        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
2587    {
2588        suffix.strip_suffix_of(self).unwrap_or(self)
2589    }
2590
2591    /// Returns a string slice with all suffixes that match a pattern
2592    /// repeatedly removed.
2593    ///
2594    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2595    /// function or closure that determines if a character matches.
2596    ///
2597    /// [`char`]: prim@char
2598    /// [pattern]: self::pattern
2599    ///
2600    /// # Text directionality
2601    ///
2602    /// A string is a sequence of bytes. `end` in this context means the last
2603    /// position of that byte string; for a left-to-right language like English or
2604    /// Russian, this will be right side, and for right-to-left languages like
2605    /// Arabic or Hebrew, this will be the left side.
2606    ///
2607    /// # Examples
2608    ///
2609    /// Simple patterns:
2610    ///
2611    /// ```
2612    /// assert_eq!("11foo1bar11".trim_end_matches('1'), "11foo1bar");
2613    /// assert_eq!("123foo1bar123".trim_end_matches(char::is_numeric), "123foo1bar");
2614    ///
2615    /// let x: &[_] = &['1', '2'];
2616    /// assert_eq!("12foo1bar12".trim_end_matches(x), "12foo1bar");
2617    /// ```
2618    ///
2619    /// A more complex pattern, using a closure:
2620    ///
2621    /// ```
2622    /// assert_eq!("1fooX".trim_end_matches(|c| c == '1' || c == 'X'), "1foo");
2623    /// ```
2624    #[must_use = "this returns the trimmed string as a new slice, \
2625                  without modifying the original"]
2626    #[stable(feature = "trim_direction", since = "1.30.0")]
2627    pub fn trim_end_matches<P: Pattern>(&self, pat: P) -> &str
2628    where
2629        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
2630    {
2631        let mut j = 0;
2632        let mut matcher = pat.into_searcher(self);
2633        if let Some((_, b)) = matcher.next_reject_back() {
2634            j = b;
2635        }
2636        // SAFETY: `Searcher` is known to return valid indices.
2637        unsafe { self.get_unchecked(0..j) }
2638    }
2639
2640    /// Returns a string slice with all prefixes that match a pattern
2641    /// repeatedly removed.
2642    ///
2643    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2644    /// function or closure that determines if a character matches.
2645    ///
2646    /// [`char`]: prim@char
2647    /// [pattern]: self::pattern
2648    ///
2649    /// # Text directionality
2650    ///
2651    /// A string is a sequence of bytes. 'Left' in this context means the first
2652    /// position of that byte string; for a language like Arabic or Hebrew
2653    /// which are 'right to left' rather than 'left to right', this will be
2654    /// the _right_ side, not the left.
2655    ///
2656    /// # Examples
2657    ///
2658    /// ```
2659    /// assert_eq!("11foo1bar11".trim_left_matches('1'), "foo1bar11");
2660    /// assert_eq!("123foo1bar123".trim_left_matches(char::is_numeric), "foo1bar123");
2661    ///
2662    /// let x: &[_] = &['1', '2'];
2663    /// assert_eq!("12foo1bar12".trim_left_matches(x), "foo1bar12");
2664    /// ```
2665    #[stable(feature = "rust1", since = "1.0.0")]
2666    #[deprecated(
2667        since = "1.33.0",
2668        note = "superseded by `trim_start_matches`",
2669        suggestion = "trim_start_matches"
2670    )]
2671    pub fn trim_left_matches<P: Pattern>(&self, pat: P) -> &str {
2672        self.trim_start_matches(pat)
2673    }
2674
2675    /// Returns a string slice with all suffixes that match a pattern
2676    /// repeatedly removed.
2677    ///
2678    /// The [pattern] can be a `&str`, [`char`], a slice of [`char`]s, or a
2679    /// function or closure that determines if a character matches.
2680    ///
2681    /// [`char`]: prim@char
2682    /// [pattern]: self::pattern
2683    ///
2684    /// # Text directionality
2685    ///
2686    /// A string is a sequence of bytes. 'Right' in this context means the last
2687    /// position of that byte string; for a language like Arabic or Hebrew
2688    /// which are 'right to left' rather than 'left to right', this will be
2689    /// the _left_ side, not the right.
2690    ///
2691    /// # Examples
2692    ///
2693    /// Simple patterns:
2694    ///
2695    /// ```
2696    /// assert_eq!("11foo1bar11".trim_right_matches('1'), "11foo1bar");
2697    /// assert_eq!("123foo1bar123".trim_right_matches(char::is_numeric), "123foo1bar");
2698    ///
2699    /// let x: &[_] = &['1', '2'];
2700    /// assert_eq!("12foo1bar12".trim_right_matches(x), "12foo1bar");
2701    /// ```
2702    ///
2703    /// A more complex pattern, using a closure:
2704    ///
2705    /// ```
2706    /// assert_eq!("1fooX".trim_right_matches(|c| c == '1' || c == 'X'), "1foo");
2707    /// ```
2708    #[stable(feature = "rust1", since = "1.0.0")]
2709    #[deprecated(
2710        since = "1.33.0",
2711        note = "superseded by `trim_end_matches`",
2712        suggestion = "trim_end_matches"
2713    )]
2714    pub fn trim_right_matches<P: Pattern>(&self, pat: P) -> &str
2715    where
2716        for<'a> P::Searcher<'a>: ReverseSearcher<'a>,
2717    {
2718        self.trim_end_matches(pat)
2719    }
2720
2721    /// Parses this string slice into another type.
2722    ///
2723    /// Because `parse` is so general, it can cause problems with type
2724    /// inference. As such, `parse` is one of the few times you'll see
2725    /// the syntax affectionately known as the 'turbofish': `::<>`. This
2726    /// helps the inference algorithm understand specifically which type
2727    /// you're trying to parse into.
2728    ///
2729    /// `parse` can parse into any type that implements the [`FromStr`] trait.
2730    ///
2731    /// # Errors
2732    ///
2733    /// Will return [`Err`] if it's not possible to parse this string slice into
2734    /// the desired type.
2735    ///
2736    /// [`Err`]: FromStr::Err
2737    ///
2738    /// # Examples
2739    ///
2740    /// Basic usage:
2741    ///
2742    /// ```
2743    /// let four: u32 = "4".parse().unwrap();
2744    ///
2745    /// assert_eq!(4, four);
2746    /// ```
2747    ///
2748    /// Using the 'turbofish' instead of annotating `four`:
2749    ///
2750    /// ```
2751    /// let four = "4".parse::<u32>();
2752    ///
2753    /// assert_eq!(Ok(4), four);
2754    /// ```
2755    ///
2756    /// Failing to parse:
2757    ///
2758    /// ```
2759    /// let nope = "j".parse::<u32>();
2760    ///
2761    /// assert!(nope.is_err());
2762    /// ```
2763    #[inline]
2764    #[stable(feature = "rust1", since = "1.0.0")]
2765    pub fn parse<F: FromStr>(&self) -> Result<F, F::Err> {
2766        FromStr::from_str(self)
2767    }
2768
2769    /// Checks if all characters in this string are within the ASCII range.
2770    ///
2771    /// An empty string returns `true`.
2772    ///
2773    /// # Examples
2774    ///
2775    /// ```
2776    /// let ascii = "hello!\n";
2777    /// let non_ascii = "Grüße, Jürgen ❤";
2778    ///
2779    /// assert!(ascii.is_ascii());
2780    /// assert!(!non_ascii.is_ascii());
2781    /// ```
2782    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
2783    #[rustc_const_stable(feature = "const_slice_is_ascii", since = "1.74.0")]
2784    #[must_use]
2785    #[inline]
2786    pub const fn is_ascii(&self) -> bool {
2787        // We can treat each byte as character here: all multibyte characters
2788        // start with a byte that is not in the ASCII range, so we will stop
2789        // there already.
2790        self.as_bytes().is_ascii()
2791    }
2792
2793    /// If this string slice [`is_ascii`](Self::is_ascii), returns it as a slice
2794    /// of [ASCII characters](`ascii::Char`), otherwise returns `None`.
2795    #[unstable(feature = "ascii_char", issue = "110998")]
2796    #[must_use]
2797    #[inline]
2798    pub const fn as_ascii(&self) -> Option<&[ascii::Char]> {
2799        // Like in `is_ascii`, we can work on the bytes directly.
2800        self.as_bytes().as_ascii()
2801    }
2802
2803    /// Converts this string slice into a slice of [ASCII characters](ascii::Char),
2804    /// without checking whether they are valid.
2805    ///
2806    /// # Safety
2807    ///
2808    /// Every character in this string must be ASCII, or else this is UB.
2809    #[unstable(feature = "ascii_char", issue = "110998")]
2810    #[must_use]
2811    #[inline]
2812    pub const unsafe fn as_ascii_unchecked(&self) -> &[ascii::Char] {
2813        assert_unsafe_precondition!(
2814            check_library_ub,
2815            "as_ascii_unchecked requires that the string is valid ASCII",
2816            (it: &str = self) => it.is_ascii()
2817        );
2818
2819        // SAFETY: the caller promised that every byte of this string slice
2820        // is ASCII.
2821        unsafe { self.as_bytes().as_ascii_unchecked() }
2822    }
2823
2824    /// Checks that two strings are an ASCII case-insensitive match.
2825    ///
2826    /// Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`,
2827    /// but without allocating and copying temporaries.
2828    ///
2829    /// # Examples
2830    ///
2831    /// ```
2832    /// assert!("Ferris".eq_ignore_ascii_case("FERRIS"));
2833    /// assert!("Ferrös".eq_ignore_ascii_case("FERRöS"));
2834    /// assert!(!"Ferrös".eq_ignore_ascii_case("FERRÖS"));
2835    /// ```
2836    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
2837    #[rustc_const_stable(feature = "const_eq_ignore_ascii_case", since = "1.89.0")]
2838    #[must_use]
2839    #[inline]
2840    pub const fn eq_ignore_ascii_case(&self, other: &str) -> bool {
2841        self.as_bytes().eq_ignore_ascii_case(other.as_bytes())
2842    }
2843
2844    /// Converts this string to its ASCII upper case equivalent in-place.
2845    ///
2846    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
2847    /// but non-ASCII letters are unchanged.
2848    ///
2849    /// To return a new uppercased value without modifying the existing one, use
2850    /// [`to_ascii_uppercase()`].
2851    ///
2852    /// [`to_ascii_uppercase()`]: #method.to_ascii_uppercase
2853    ///
2854    /// # Examples
2855    ///
2856    /// ```
2857    /// let mut s = String::from("Grüße, Jürgen ❤");
2858    ///
2859    /// s.make_ascii_uppercase();
2860    ///
2861    /// assert_eq!("GRüßE, JüRGEN ❤", s);
2862    /// ```
2863    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
2864    #[rustc_const_stable(feature = "const_make_ascii", since = "1.84.0")]
2865    #[inline]
2866    pub const fn make_ascii_uppercase(&mut self) {
2867        // SAFETY: changing ASCII letters only does not invalidate UTF-8.
2868        let me = unsafe { self.as_bytes_mut() };
2869        me.make_ascii_uppercase()
2870    }
2871
2872    /// Converts this string to its ASCII lower case equivalent in-place.
2873    ///
2874    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
2875    /// but non-ASCII letters are unchanged.
2876    ///
2877    /// To return a new lowercased value without modifying the existing one, use
2878    /// [`to_ascii_lowercase()`].
2879    ///
2880    /// [`to_ascii_lowercase()`]: #method.to_ascii_lowercase
2881    ///
2882    /// # Examples
2883    ///
2884    /// ```
2885    /// let mut s = String::from("GRÜßE, JÜRGEN ❤");
2886    ///
2887    /// s.make_ascii_lowercase();
2888    ///
2889    /// assert_eq!("grÜße, jÜrgen ❤", s);
2890    /// ```
2891    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
2892    #[rustc_const_stable(feature = "const_make_ascii", since = "1.84.0")]
2893    #[inline]
2894    pub const fn make_ascii_lowercase(&mut self) {
2895        // SAFETY: changing ASCII letters only does not invalidate UTF-8.
2896        let me = unsafe { self.as_bytes_mut() };
2897        me.make_ascii_lowercase()
2898    }
2899
2900    /// Returns a string slice with leading ASCII whitespace removed.
2901    ///
2902    /// 'Whitespace' refers to the definition used by
2903    /// [`u8::is_ascii_whitespace`].
2904    ///
2905    /// [`u8::is_ascii_whitespace`]: u8::is_ascii_whitespace
2906    ///
2907    /// # Examples
2908    ///
2909    /// ```
2910    /// assert_eq!(" \t \u{3000}hello world\n".trim_ascii_start(), "\u{3000}hello world\n");
2911    /// assert_eq!("  ".trim_ascii_start(), "");
2912    /// assert_eq!("".trim_ascii_start(), "");
2913    /// ```
2914    #[must_use = "this returns the trimmed string as a new slice, \
2915                  without modifying the original"]
2916    #[stable(feature = "byte_slice_trim_ascii", since = "1.80.0")]
2917    #[rustc_const_stable(feature = "byte_slice_trim_ascii", since = "1.80.0")]
2918    #[inline]
2919    pub const fn trim_ascii_start(&self) -> &str {
2920        // SAFETY: Removing ASCII characters from a `&str` does not invalidate
2921        // UTF-8.
2922        unsafe { core::str::from_utf8_unchecked(self.as_bytes().trim_ascii_start()) }
2923    }
2924
2925    /// Returns a string slice with trailing ASCII whitespace removed.
2926    ///
2927    /// 'Whitespace' refers to the definition used by
2928    /// [`u8::is_ascii_whitespace`].
2929    ///
2930    /// [`u8::is_ascii_whitespace`]: u8::is_ascii_whitespace
2931    ///
2932    /// # Examples
2933    ///
2934    /// ```
2935    /// assert_eq!("\r hello world\u{3000}\n ".trim_ascii_end(), "\r hello world\u{3000}");
2936    /// assert_eq!("  ".trim_ascii_end(), "");
2937    /// assert_eq!("".trim_ascii_end(), "");
2938    /// ```
2939    #[must_use = "this returns the trimmed string as a new slice, \
2940                  without modifying the original"]
2941    #[stable(feature = "byte_slice_trim_ascii", since = "1.80.0")]
2942    #[rustc_const_stable(feature = "byte_slice_trim_ascii", since = "1.80.0")]
2943    #[inline]
2944    pub const fn trim_ascii_end(&self) -> &str {
2945        // SAFETY: Removing ASCII characters from a `&str` does not invalidate
2946        // UTF-8.
2947        unsafe { core::str::from_utf8_unchecked(self.as_bytes().trim_ascii_end()) }
2948    }
2949
2950    /// Returns a string slice with leading and trailing ASCII whitespace
2951    /// removed.
2952    ///
2953    /// 'Whitespace' refers to the definition used by
2954    /// [`u8::is_ascii_whitespace`].
2955    ///
2956    /// [`u8::is_ascii_whitespace`]: u8::is_ascii_whitespace
2957    ///
2958    /// # Examples
2959    ///
2960    /// ```
2961    /// assert_eq!("\r hello world\n ".trim_ascii(), "hello world");
2962    /// assert_eq!("  ".trim_ascii(), "");
2963    /// assert_eq!("".trim_ascii(), "");
2964    /// ```
2965    #[must_use = "this returns the trimmed string as a new slice, \
2966                  without modifying the original"]
2967    #[stable(feature = "byte_slice_trim_ascii", since = "1.80.0")]
2968    #[rustc_const_stable(feature = "byte_slice_trim_ascii", since = "1.80.0")]
2969    #[inline]
2970    pub const fn trim_ascii(&self) -> &str {
2971        // SAFETY: Removing ASCII characters from a `&str` does not invalidate
2972        // UTF-8.
2973        unsafe { core::str::from_utf8_unchecked(self.as_bytes().trim_ascii()) }
2974    }
2975
2976    /// Returns an iterator that escapes each char in `self` with [`char::escape_debug`].
2977    ///
2978    /// Note: only extended grapheme codepoints that begin the string will be
2979    /// escaped.
2980    ///
2981    /// # Examples
2982    ///
2983    /// As an iterator:
2984    ///
2985    /// ```
2986    /// for c in "❤\n!".escape_debug() {
2987    ///     print!("{c}");
2988    /// }
2989    /// println!();
2990    /// ```
2991    ///
2992    /// Using `println!` directly:
2993    ///
2994    /// ```
2995    /// println!("{}", "❤\n!".escape_debug());
2996    /// ```
2997    ///
2998    ///
2999    /// Both are equivalent to:
3000    ///
3001    /// ```
3002    /// println!("❤\\n!");
3003    /// ```
3004    ///
3005    /// Using `to_string`:
3006    ///
3007    /// ```
3008    /// assert_eq!("❤\n!".escape_debug().to_string(), "❤\\n!");
3009    /// ```
3010    #[must_use = "this returns the escaped string as an iterator, \
3011                  without modifying the original"]
3012    #[stable(feature = "str_escape", since = "1.34.0")]
3013    pub fn escape_debug(&self) -> EscapeDebug<'_> {
3014        let mut chars = self.chars();
3015        EscapeDebug {
3016            inner: chars
3017                .next()
3018                .map(|first| first.escape_debug_ext(EscapeDebugExtArgs::ESCAPE_ALL))
3019                .into_iter()
3020                .flatten()
3021                .chain(chars.flat_map(CharEscapeDebugContinue)),
3022        }
3023    }
3024
3025    /// Returns an iterator that escapes each char in `self` with [`char::escape_default`].
3026    ///
3027    /// # Examples
3028    ///
3029    /// As an iterator:
3030    ///
3031    /// ```
3032    /// for c in "❤\n!".escape_default() {
3033    ///     print!("{c}");
3034    /// }
3035    /// println!();
3036    /// ```
3037    ///
3038    /// Using `println!` directly:
3039    ///
3040    /// ```
3041    /// println!("{}", "❤\n!".escape_default());
3042    /// ```
3043    ///
3044    ///
3045    /// Both are equivalent to:
3046    ///
3047    /// ```
3048    /// println!("\\u{{2764}}\\n!");
3049    /// ```
3050    ///
3051    /// Using `to_string`:
3052    ///
3053    /// ```
3054    /// assert_eq!("❤\n!".escape_default().to_string(), "\\u{2764}\\n!");
3055    /// ```
3056    #[must_use = "this returns the escaped string as an iterator, \
3057                  without modifying the original"]
3058    #[stable(feature = "str_escape", since = "1.34.0")]
3059    pub fn escape_default(&self) -> EscapeDefault<'_> {
3060        EscapeDefault { inner: self.chars().flat_map(CharEscapeDefault) }
3061    }
3062
3063    /// Returns an iterator that escapes each char in `self` with [`char::escape_unicode`].
3064    ///
3065    /// # Examples
3066    ///
3067    /// As an iterator:
3068    ///
3069    /// ```
3070    /// for c in "❤\n!".escape_unicode() {
3071    ///     print!("{c}");
3072    /// }
3073    /// println!();
3074    /// ```
3075    ///
3076    /// Using `println!` directly:
3077    ///
3078    /// ```
3079    /// println!("{}", "❤\n!".escape_unicode());
3080    /// ```
3081    ///
3082    ///
3083    /// Both are equivalent to:
3084    ///
3085    /// ```
3086    /// println!("\\u{{2764}}\\u{{a}}\\u{{21}}");
3087    /// ```
3088    ///
3089    /// Using `to_string`:
3090    ///
3091    /// ```
3092    /// assert_eq!("❤\n!".escape_unicode().to_string(), "\\u{2764}\\u{a}\\u{21}");
3093    /// ```
3094    #[must_use = "this returns the escaped string as an iterator, \
3095                  without modifying the original"]
3096    #[stable(feature = "str_escape", since = "1.34.0")]
3097    pub fn escape_unicode(&self) -> EscapeUnicode<'_> {
3098        EscapeUnicode { inner: self.chars().flat_map(CharEscapeUnicode) }
3099    }
3100
3101    /// Returns the range that a substring points to.
3102    ///
3103    /// Returns `None` if `substr` does not point within `self`.
3104    ///
3105    /// Unlike [`str::find`], **this does not search through the string**.
3106    /// Instead, it uses pointer arithmetic to find where in the string
3107    /// `substr` is derived from.
3108    ///
3109    /// This is useful for extending [`str::split`] and similar methods.
3110    ///
3111    /// Note that this method may return false positives (typically either
3112    /// `Some(0..0)` or `Some(self.len()..self.len())`) if `substr` is a
3113    /// zero-length `str` that points at the beginning or end of another,
3114    /// independent, `str`.
3115    ///
3116    /// # Examples
3117    /// ```
3118    /// #![feature(substr_range)]
3119    ///
3120    /// let data = "a, b, b, a";
3121    /// let mut iter = data.split(", ").map(|s| data.substr_range(s).unwrap());
3122    ///
3123    /// assert_eq!(iter.next(), Some(0..1));
3124    /// assert_eq!(iter.next(), Some(3..4));
3125    /// assert_eq!(iter.next(), Some(6..7));
3126    /// assert_eq!(iter.next(), Some(9..10));
3127    /// ```
3128    #[must_use]
3129    #[unstable(feature = "substr_range", issue = "126769")]
3130    pub fn substr_range(&self, substr: &str) -> Option<Range<usize>> {
3131        self.as_bytes().subslice_range(substr.as_bytes())
3132    }
3133
3134    /// Returns the same string as a string slice `&str`.
3135    ///
3136    /// This method is redundant when used directly on `&str`, but
3137    /// it helps dereferencing other string-like types to string slices,
3138    /// for example references to `Box<str>` or `Arc<str>`.
3139    #[inline]
3140    #[unstable(feature = "str_as_str", issue = "130366")]
3141    pub const fn as_str(&self) -> &str {
3142        self
3143    }
3144}
3145
3146#[stable(feature = "rust1", since = "1.0.0")]
3147#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
3148impl const AsRef<[u8]> for str {
3149    #[inline]
3150    fn as_ref(&self) -> &[u8] {
3151        self.as_bytes()
3152    }
3153}
3154
3155#[stable(feature = "rust1", since = "1.0.0")]
3156#[rustc_const_unstable(feature = "const_default", issue = "143894")]
3157impl const Default for &str {
3158    /// Creates an empty str
3159    #[inline]
3160    fn default() -> Self {
3161        ""
3162    }
3163}
3164
3165#[stable(feature = "default_mut_str", since = "1.28.0")]
3166#[rustc_const_unstable(feature = "const_default", issue = "143894")]
3167impl const Default for &mut str {
3168    /// Creates an empty mutable str
3169    #[inline]
3170    fn default() -> Self {
3171        // SAFETY: The empty string is valid UTF-8.
3172        unsafe { from_utf8_unchecked_mut(&mut []) }
3173    }
3174}
3175
3176impl_fn_for_zst! {
3177    /// A nameable, cloneable fn type
3178    #[derive(Clone)]
3179    struct LinesMap impl<'a> Fn = |line: &'a str| -> &'a str {
3180        let Some(line) = line.strip_suffix('\n') else { return line };
3181        let Some(line) = line.strip_suffix('\r') else { return line };
3182        line
3183    };
3184
3185    #[derive(Clone)]
3186    struct CharEscapeDebugContinue impl Fn = |c: char| -> char::EscapeDebug {
3187        c.escape_debug_ext(EscapeDebugExtArgs {
3188            escape_grapheme_extended: false,
3189            escape_single_quote: true,
3190            escape_double_quote: true
3191        })
3192    };
3193
3194    #[derive(Clone)]
3195    struct CharEscapeUnicode impl Fn = |c: char| -> char::EscapeUnicode {
3196        c.escape_unicode()
3197    };
3198    #[derive(Clone)]
3199    struct CharEscapeDefault impl Fn = |c: char| -> char::EscapeDefault {
3200        c.escape_default()
3201    };
3202
3203    #[derive(Clone)]
3204    struct IsWhitespace impl Fn = |c: char| -> bool {
3205        c.is_whitespace()
3206    };
3207
3208    #[derive(Clone)]
3209    struct IsAsciiWhitespace impl Fn = |byte: &u8| -> bool {
3210        byte.is_ascii_whitespace()
3211    };
3212
3213    #[derive(Clone)]
3214    struct IsNotEmpty impl<'a, 'b> Fn = |s: &'a &'b str| -> bool {
3215        !s.is_empty()
3216    };
3217
3218    #[derive(Clone)]
3219    struct BytesIsNotEmpty impl<'a, 'b> Fn = |s: &'a &'b [u8]| -> bool {
3220        !s.is_empty()
3221    };
3222
3223    #[derive(Clone)]
3224    struct UnsafeBytesToStr impl<'a> Fn = |bytes: &'a [u8]| -> &'a str {
3225        // SAFETY: not safe
3226        unsafe { from_utf8_unchecked(bytes) }
3227    };
3228}
3229
3230// This is required to make `impl From<&str> for Box<dyn Error>` and `impl<E> From<E> for Box<dyn Error>` not overlap.
3231#[stable(feature = "error_in_core_neg_impl", since = "1.65.0")]
3232impl !crate::error::Error for &str {}
````