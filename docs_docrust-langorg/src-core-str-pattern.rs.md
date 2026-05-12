---
title: pattern.rs - source
url: https://doc.rust-lang.org/src/core/str/pattern.rs.html#1051
source: crawler
fetched_at: 2026-05-06T21:27:40.082621727-03:00
rendered_js: false
word_count: 10069
summary: The Pattern API defines a generic trait mechanism for searching strings using various types, including substrings, characters, character slices, and predicate closures.
tags:
    - rust
    - string-processing
    - pattern-matching
    - search-api
    - traits
    - utf8
category: reference
---

## core/str/ pattern.rs

````rust
1//! The string Pattern API.
2//!
3//! The Pattern API provides a generic mechanism for using different pattern
4//! types when searching through a string.
5//!
6//! For more details, see the traits [`Pattern`], [`Searcher`],
7//! [`ReverseSearcher`], and [`DoubleEndedSearcher`].
8//!
9//! Although this API is unstable, it is exposed via stable APIs on the
10//! [`str`] type.
11//!
12//! # Examples
13//!
14//! [`Pattern`] is [implemented][pattern-impls] in the stable API for
15//! [`&str`][`str`], [`char`], slices of [`char`], and functions and closures
16//! implementing `FnMut(char) -> bool`.
17//!
18//! ```
19//! let s = "Can you find a needle in a haystack?";
20//!
21//! // &str pattern
22//! assert_eq!(s.find("you"), Some(4));
23//! // char pattern
24//! assert_eq!(s.find('n'), Some(2));
25//! // array of chars pattern
26//! assert_eq!(s.find(&['a', 'e', 'i', 'o', 'u']), Some(1));
27//! // slice of chars pattern
28//! assert_eq!(s.find(&['a', 'e', 'i', 'o', 'u'][..]), Some(1));
29//! // closure pattern
30//! assert_eq!(s.find(|c: char| c.is_ascii_punctuation()), Some(35));
31//! ```
32//!
33//! [pattern-impls]: Pattern#implementors
34
35#![unstable(
36    feature = "pattern",
37    reason = "API not fully fleshed out and ready to be stabilized",
38    issue = "27721"
39)]
40
41use crate::cmp::Ordering;
42use crate::convert::TryInto as _;
43use crate::slice::memchr;
44use crate::{cmp, fmt};
45
46// Pattern
47
48/// A string pattern.
49///
50/// A `Pattern` expresses that the implementing type
51/// can be used as a string pattern for searching in a [`&str`][str].
52///
53/// For example, both `'a'` and `"aa"` are patterns that
54/// would match at index `1` in the string `"baaaab"`.
55///
56/// The trait itself acts as a builder for an associated
57/// [`Searcher`] type, which does the actual work of finding
58/// occurrences of the pattern in a string.
59///
60/// Depending on the type of the pattern, the behavior of methods like
61/// [`str::find`] and [`str::contains`] can change. The table below describes
62/// some of those behaviors.
63///
64/// | Pattern type             | Match condition                           |
65/// |--------------------------|-------------------------------------------|
66/// | `&str`                   | is substring                              |
67/// | `char`                   | is contained in string                    |
68/// | `&[char]`                | any char in slice is contained in string  |
69/// | `F: FnMut(char) -> bool` | `F` returns `true` for a char in string   |
70/// | `&&str`                  | is substring                              |
71/// | `&String`                | is substring                              |
72///
73/// # Examples
74///
75/// ```
76/// // &str
77/// assert_eq!("abaaa".find("ba"), Some(1));
78/// assert_eq!("abaaa".find("bac"), None);
79///
80/// // char
81/// assert_eq!("abaaa".find('a'), Some(0));
82/// assert_eq!("abaaa".find('b'), Some(1));
83/// assert_eq!("abaaa".find('c'), None);
84///
85/// // &[char; N]
86/// assert_eq!("ab".find(&['b', 'a']), Some(0));
87/// assert_eq!("abaaa".find(&['a', 'z']), Some(0));
88/// assert_eq!("abaaa".find(&['c', 'd']), None);
89///
90/// // &[char]
91/// assert_eq!("ab".find(&['b', 'a'][..]), Some(0));
92/// assert_eq!("abaaa".find(&['a', 'z'][..]), Some(0));
93/// assert_eq!("abaaa".find(&['c', 'd'][..]), None);
94///
95/// // FnMut(char) -> bool
96/// assert_eq!("abcdef_z".find(|ch| ch > 'd' && ch < 'y'), Some(4));
97/// assert_eq!("abcddd_z".find(|ch| ch > 'd' && ch < 'y'), None);
98/// ```
99pub trait Pattern: Sized {
100    /// Associated searcher for this pattern
101    type Searcher<'a>: Searcher<'a>;
102
103    /// Constructs the associated searcher from
104    /// `self` and the `haystack` to search in.
105    fn into_searcher(self, haystack: &str) -> Self::Searcher<'_>;
106
107    /// Checks whether the pattern matches anywhere in the haystack
108    #[inline]
109    fn is_contained_in(self, haystack: &str) -> bool {
110        self.into_searcher(haystack).next_match().is_some()
111    }
112
113    /// Checks whether the pattern matches at the front of the haystack
114    #[inline]
115    fn is_prefix_of(self, haystack: &str) -> bool {
116        matches!(self.into_searcher(haystack).next(), SearchStep::Match(0, _))
117    }
118
119    /// Checks whether the pattern matches at the back of the haystack
120    #[inline]
121    fn is_suffix_of<'a>(self, haystack: &'a str) -> bool
122    where
123        Self::Searcher<'a>: ReverseSearcher<'a>,
124    {
125        matches!(self.into_searcher(haystack).next_back(), SearchStep::Match(_, j) if haystack.len() == j)
126    }
127
128    /// Removes the pattern from the front of haystack, if it matches.
129    #[inline]
130    fn strip_prefix_of(self, haystack: &str) -> Option<&str> {
131        if let SearchStep::Match(start, len) = self.into_searcher(haystack).next() {
132            debug_assert_eq!(
133                start, 0,
134                "The first search step from Searcher \
135                 must include the first character"
136            );
137            // SAFETY: `Searcher` is known to return valid indices.
138            unsafe { Some(haystack.get_unchecked(len..)) }
139        } else {
140            None
141        }
142    }
143
144    /// Removes the pattern from the back of haystack, if it matches.
145    #[inline]
146    fn strip_suffix_of<'a>(self, haystack: &'a str) -> Option<&'a str>
147    where
148        Self::Searcher<'a>: ReverseSearcher<'a>,
149    {
150        if let SearchStep::Match(start, end) = self.into_searcher(haystack).next_back() {
151            debug_assert_eq!(
152                end,
153                haystack.len(),
154                "The first search step from ReverseSearcher \
155                 must include the last character"
156            );
157            // SAFETY: `Searcher` is known to return valid indices.
158            unsafe { Some(haystack.get_unchecked(..start)) }
159        } else {
160            None
161        }
162    }
163
164    /// Returns the pattern as utf-8 bytes if possible.
165    fn as_utf8_pattern(&self) -> Option<Utf8Pattern<'_>> {
166        None
167    }
168}
169/// Result of calling [`Pattern::as_utf8_pattern()`].
170/// Can be used for inspecting the contents of a [`Pattern`] in cases
171/// where the underlying representation can be represented as UTF-8.
172#[derive(Copy, Clone, Eq, PartialEq, Debug)]
173pub enum Utf8Pattern<'a> {
174    /// Type returned by String and str types.
175    StringPattern(&'a [u8]),
176    /// Type returned by char types.
177    CharPattern(char),
178}
179
180// Searcher
181
182/// Result of calling [`Searcher::next()`] or [`ReverseSearcher::next_back()`].
183#[derive(Copy, Clone, Eq, PartialEq, Debug)]
184pub enum SearchStep {
185    /// Expresses that a match of the pattern has been found at
186    /// `haystack[a..b]`.
187    Match(usize, usize),
188    /// Expresses that `haystack[a..b]` has been rejected as a possible match
189    /// of the pattern.
190    ///
191    /// Note that there might be more than one `Reject` between two `Match`es,
192    /// there is no requirement for them to be combined into one.
193    Reject(usize, usize),
194    /// Expresses that every byte of the haystack has been visited, ending
195    /// the iteration.
196    Done,
197}
198
199/// A searcher for a string pattern.
200///
201/// This trait provides methods for searching for non-overlapping
202/// matches of a pattern starting from the front (left) of a string.
203///
204/// It will be implemented by associated `Searcher`
205/// types of the [`Pattern`] trait.
206///
207/// The trait is marked unsafe because the indices returned by the
208/// [`next()`][Searcher::next] methods are required to lie on valid utf8
209/// boundaries in the haystack. This enables consumers of this trait to
210/// slice the haystack without additional runtime checks.
211pub unsafe trait Searcher<'a> {
212    /// Getter for the underlying string to be searched in
213    ///
214    /// Will always return the same [`&str`][str].
215    fn haystack(&self) -> &'a str;
216
217    /// Performs the next search step starting from the front.
218    ///
219    /// - Returns [`Match(a, b)`][SearchStep::Match] if `haystack[a..b]` matches
220    ///   the pattern.
221    /// - Returns [`Reject(a, b)`][SearchStep::Reject] if `haystack[a..b]` can
222    ///   not match the pattern, even partially.
223    /// - Returns [`Done`][SearchStep::Done] if every byte of the haystack has
224    ///   been visited.
225    ///
226    /// The stream of [`Match`][SearchStep::Match] and
227    /// [`Reject`][SearchStep::Reject] values up to a [`Done`][SearchStep::Done]
228    /// will contain index ranges that are adjacent, non-overlapping,
229    /// covering the whole haystack, and laying on utf8 boundaries.
230    ///
231    /// A [`Match`][SearchStep::Match] result needs to contain the whole matched
232    /// pattern, however [`Reject`][SearchStep::Reject] results may be split up
233    /// into arbitrary many adjacent fragments. Both ranges may have zero length.
234    ///
235    /// As an example, the pattern `"aaa"` and the haystack `"cbaaaaab"`
236    /// might produce the stream
237    /// `[Reject(0, 1), Reject(1, 2), Match(2, 5), Reject(5, 8)]`
238    fn next(&mut self) -> SearchStep;
239
240    /// Finds the next [`Match`][SearchStep::Match] result. See [`next()`][Searcher::next].
241    ///
242    /// Unlike [`next()`][Searcher::next], there is no guarantee that the returned ranges
243    /// of this and [`next_reject`][Searcher::next_reject] will overlap. This will return
244    /// `(start_match, end_match)`, where start_match is the index of where
245    /// the match begins, and end_match is the index after the end of the match.
246    #[inline]
247    fn next_match(&mut self) -> Option<(usize, usize)> {
248        loop {
249            match self.next() {
250                SearchStep::Match(a, b) => return Some((a, b)),
251                SearchStep::Done => return None,
252                _ => continue,
253            }
254        }
255    }
256
257    /// Finds the next [`Reject`][SearchStep::Reject] result. See [`next()`][Searcher::next]
258    /// and [`next_match()`][Searcher::next_match].
259    ///
260    /// Unlike [`next()`][Searcher::next], there is no guarantee that the returned ranges
261    /// of this and [`next_match`][Searcher::next_match] will overlap.
262    #[inline]
263    fn next_reject(&mut self) -> Option<(usize, usize)> {
264        loop {
265            match self.next() {
266                SearchStep::Reject(a, b) => return Some((a, b)),
267                SearchStep::Done => return None,
268                _ => continue,
269            }
270        }
271    }
272}
273
274/// A reverse searcher for a string pattern.
275///
276/// This trait provides methods for searching for non-overlapping
277/// matches of a pattern starting from the back (right) of a string.
278///
279/// It will be implemented by associated [`Searcher`]
280/// types of the [`Pattern`] trait if the pattern supports searching
281/// for it from the back.
282///
283/// The index ranges returned by this trait are not required
284/// to exactly match those of the forward search in reverse.
285///
286/// For the reason why this trait is marked unsafe, see the
287/// parent trait [`Searcher`].
288pub unsafe trait ReverseSearcher<'a>: Searcher<'a> {
289    /// Performs the next search step starting from the back.
290    ///
291    /// - Returns [`Match(a, b)`][SearchStep::Match] if `haystack[a..b]`
292    ///   matches the pattern.
293    /// - Returns [`Reject(a, b)`][SearchStep::Reject] if `haystack[a..b]`
294    ///   can not match the pattern, even partially.
295    /// - Returns [`Done`][SearchStep::Done] if every byte of the haystack
296    ///   has been visited
297    ///
298    /// The stream of [`Match`][SearchStep::Match] and
299    /// [`Reject`][SearchStep::Reject] values up to a [`Done`][SearchStep::Done]
300    /// will contain index ranges that are adjacent, non-overlapping,
301    /// covering the whole haystack, and laying on utf8 boundaries.
302    ///
303    /// A [`Match`][SearchStep::Match] result needs to contain the whole matched
304    /// pattern, however [`Reject`][SearchStep::Reject] results may be split up
305    /// into arbitrary many adjacent fragments. Both ranges may have zero length.
306    ///
307    /// As an example, the pattern `"aaa"` and the haystack `"cbaaaaab"`
308    /// might produce the stream
309    /// `[Reject(7, 8), Match(4, 7), Reject(1, 4), Reject(0, 1)]`.
310    fn next_back(&mut self) -> SearchStep;
311
312    /// Finds the next [`Match`][SearchStep::Match] result.
313    /// See [`next_back()`][ReverseSearcher::next_back].
314    #[inline]
315    fn next_match_back(&mut self) -> Option<(usize, usize)> {
316        loop {
317            match self.next_back() {
318                SearchStep::Match(a, b) => return Some((a, b)),
319                SearchStep::Done => return None,
320                _ => continue,
321            }
322        }
323    }
324
325    /// Finds the next [`Reject`][SearchStep::Reject] result.
326    /// See [`next_back()`][ReverseSearcher::next_back].
327    #[inline]
328    fn next_reject_back(&mut self) -> Option<(usize, usize)> {
329        loop {
330            match self.next_back() {
331                SearchStep::Reject(a, b) => return Some((a, b)),
332                SearchStep::Done => return None,
333                _ => continue,
334            }
335        }
336    }
337}
338
339/// A marker trait to express that a [`ReverseSearcher`]
340/// can be used for a [`DoubleEndedIterator`] implementation.
341///
342/// For this, the impl of [`Searcher`] and [`ReverseSearcher`] need
343/// to follow these conditions:
344///
345/// - All results of `next()` need to be identical
346///   to the results of `next_back()` in reverse order.
347/// - `next()` and `next_back()` need to behave as
348///   the two ends of a range of values, that is they
349///   can not "walk past each other".
350///
351/// # Examples
352///
353/// `char::Searcher` is a `DoubleEndedSearcher` because searching for a
354/// [`char`] only requires looking at one at a time, which behaves the same
355/// from both ends.
356///
357/// `(&str)::Searcher` is not a `DoubleEndedSearcher` because
358/// the pattern `"aa"` in the haystack `"aaa"` matches as either
359/// `"[aa]a"` or `"a[aa]"`, depending on which side it is searched.
360pub trait DoubleEndedSearcher<'a>: ReverseSearcher<'a> {}
361
362/////////////////////////////////////////////////////////////////////////////
363// Impl for char
364/////////////////////////////////////////////////////////////////////////////
365
366/// Associated type for `<char as Pattern>::Searcher<'a>`.
367#[derive(Clone, Debug)]
368pub struct CharSearcher<'a> {
369    haystack: &'a str,
370    // safety invariant: `finger`/`finger_back` must be a valid utf8 byte index of `haystack`
371    // This invariant can be broken *within* next_match and next_match_back, however
372    // they must exit with fingers on valid code point boundaries.
373    /// `finger` is the current byte index of the forward search.
374    /// Imagine that it exists before the byte at its index, i.e.
375    /// `haystack[finger]` is the first byte of the slice we must inspect during
376    /// forward searching
377    finger: usize,
378    /// `finger_back` is the current byte index of the reverse search.
379    /// Imagine that it exists after the byte at its index, i.e.
380    /// haystack[finger_back - 1] is the last byte of the slice we must inspect during
381    /// forward searching (and thus the first byte to be inspected when calling next_back()).
382    finger_back: usize,
383    /// The character being searched for
384    needle: char,
385
386    // safety invariant: `utf8_size` must be less than 5
387    /// The number of bytes `needle` takes up when encoded in utf8.
388    utf8_size: u8,
389    /// A utf8 encoded copy of the `needle`
390    utf8_encoded: [u8; 4],
391}
392
393impl CharSearcher<'_> {
394    fn utf8_size(&self) -> usize {
395        self.utf8_size.into()
396    }
397}
398
399unsafe impl<'a> Searcher<'a> for CharSearcher<'a> {
400    #[inline]
401    fn haystack(&self) -> &'a str {
402        self.haystack
403    }
404    #[inline]
405    fn next(&mut self) -> SearchStep {
406        let old_finger = self.finger;
407        // SAFETY: 1-4 guarantee safety of `get_unchecked`
408        // 1. `self.finger` and `self.finger_back` are kept on unicode boundaries
409        //    (this is invariant)
410        // 2. `self.finger >= 0` since it starts at 0 and only increases
411        // 3. `self.finger < self.finger_back` because otherwise the char `iter`
412        //    would return `SearchStep::Done`
413        // 4. `self.finger` comes before the end of the haystack because `self.finger_back`
414        //    starts at the end and only decreases
415        let slice = unsafe { self.haystack.get_unchecked(old_finger..self.finger_back) };
416        let mut iter = slice.chars();
417        let old_len = iter.iter.len();
418        if let Some(ch) = iter.next() {
419            // add byte offset of current character
420            // without re-encoding as utf-8
421            self.finger += old_len - iter.iter.len();
422            if ch == self.needle {
423                SearchStep::Match(old_finger, self.finger)
424            } else {
425                SearchStep::Reject(old_finger, self.finger)
426            }
427        } else {
428            SearchStep::Done
429        }
430    }
431    #[inline]
432    fn next_match(&mut self) -> Option<(usize, usize)> {
433        loop {
434            // get the haystack after the last character found
435            let bytes = self.haystack.as_bytes().get(self.finger..self.finger_back)?;
436            // the last byte of the utf8 encoded needle
437            // SAFETY: we have an invariant that `utf8_size < 5`
438            let last_byte = unsafe { *self.utf8_encoded.get_unchecked(self.utf8_size() - 1) };
439            if let Some(index) = memchr::memchr(last_byte, bytes) {
440                // The new finger is the index of the byte we found,
441                // plus one, since we memchr'd for the last byte of the character.
442                //
443                // Note that this doesn't always give us a finger on a UTF8 boundary.
444                // If we *didn't* find our character
445                // we may have indexed to the non-last byte of a 3-byte or 4-byte character.
446                // We can't just skip to the next valid starting byte because a character like
447                // ꁁ (U+A041 YI SYLLABLE PA), utf-8 `EA 81 81` will have us always find
448                // the second byte when searching for the third.
449                //
450                // However, this is totally okay. While we have the invariant that
451                // self.finger is on a UTF8 boundary, this invariant is not relied upon
452                // within this method (it is relied upon in CharSearcher::next()).
453                //
454                // We only exit this method when we reach the end of the string, or if we
455                // find something. When we find something the `finger` will be set
456                // to a UTF8 boundary.
457                self.finger += index + 1;
458                if self.finger >= self.utf8_size() {
459                    let found_char = self.finger - self.utf8_size();
460                    if let Some(slice) = self.haystack.as_bytes().get(found_char..self.finger) {
461                        if slice == &self.utf8_encoded[0..self.utf8_size()] {
462                            return Some((found_char, self.finger));
463                        }
464                    }
465                }
466            } else {
467                // found nothing, exit
468                self.finger = self.finger_back;
469                return None;
470            }
471        }
472    }
473
474    // let next_reject use the default implementation from the Searcher trait
475}
476
477unsafe impl<'a> ReverseSearcher<'a> for CharSearcher<'a> {
478    #[inline]
479    fn next_back(&mut self) -> SearchStep {
480        let old_finger = self.finger_back;
481        // SAFETY: see the comment for next() above
482        let slice = unsafe { self.haystack.get_unchecked(self.finger..old_finger) };
483        let mut iter = slice.chars();
484        let old_len = iter.iter.len();
485        if let Some(ch) = iter.next_back() {
486            // subtract byte offset of current character
487            // without re-encoding as utf-8
488            self.finger_back -= old_len - iter.iter.len();
489            if ch == self.needle {
490                SearchStep::Match(self.finger_back, old_finger)
491            } else {
492                SearchStep::Reject(self.finger_back, old_finger)
493            }
494        } else {
495            SearchStep::Done
496        }
497    }
498    #[inline]
499    fn next_match_back(&mut self) -> Option<(usize, usize)> {
500        let haystack = self.haystack.as_bytes();
501        loop {
502            // get the haystack up to but not including the last character searched
503            let bytes = haystack.get(self.finger..self.finger_back)?;
504            // the last byte of the utf8 encoded needle
505            // SAFETY: we have an invariant that `utf8_size < 5`
506            let last_byte = unsafe { *self.utf8_encoded.get_unchecked(self.utf8_size() - 1) };
507            if let Some(index) = memchr::memrchr(last_byte, bytes) {
508                // we searched a slice that was offset by self.finger,
509                // add self.finger to recoup the original index
510                let index = self.finger + index;
511                // memrchr will return the index of the byte we wish to
512                // find. In case of an ASCII character, this is indeed
513                // were we wish our new finger to be ("after" the found
514                // char in the paradigm of reverse iteration). For
515                // multibyte chars we need to skip down by the number of more
516                // bytes they have than ASCII
517                let shift = self.utf8_size() - 1;
518                if index >= shift {
519                    let found_char = index - shift;
520                    if let Some(slice) = haystack.get(found_char..(found_char + self.utf8_size())) {
521                        if slice == &self.utf8_encoded[0..self.utf8_size()] {
522                            // move finger to before the character found (i.e., at its start index)
523                            self.finger_back = found_char;
524                            return Some((self.finger_back, self.finger_back + self.utf8_size()));
525                        }
526                    }
527                }
528                // We can't use finger_back = index - size + 1 here. If we found the last char
529                // of a different-sized character (or the middle byte of a different character)
530                // we need to bump the finger_back down to `index`. This similarly makes
531                // `finger_back` have the potential to no longer be on a boundary,
532                // but this is OK since we only exit this function on a boundary
533                // or when the haystack has been searched completely.
534                //
535                // Unlike next_match this does not
536                // have the problem of repeated bytes in utf-8 because
537                // we're searching for the last byte, and we can only have
538                // found the last byte when searching in reverse.
539                self.finger_back = index;
540            } else {
541                self.finger_back = self.finger;
542                // found nothing, exit
543                return None;
544            }
545        }
546    }
547
548    // let next_reject_back use the default implementation from the Searcher trait
549}
550
551impl<'a> DoubleEndedSearcher<'a> for CharSearcher<'a> {}
552
553/// Searches for chars that are equal to a given [`char`].
554///
555/// # Examples
556///
557/// ```
558/// assert_eq!("Hello world".find('o'), Some(4));
559/// ```
560impl Pattern for char {
561    type Searcher<'a> = CharSearcher<'a>;
562
563    #[inline]
564    fn into_searcher<'a>(self, haystack: &'a str) -> Self::Searcher<'a> {
565        let mut utf8_encoded = [0; char::MAX_LEN_UTF8];
566        let utf8_size = self
567            .encode_utf8(&mut utf8_encoded)
568            .len()
569            .try_into()
570            .expect("char len should be less than 255");
571
572        CharSearcher {
573            haystack,
574            finger: 0,
575            finger_back: haystack.len(),
576            needle: self,
577            utf8_size,
578            utf8_encoded,
579        }
580    }
581
582    #[inline]
583    fn is_contained_in(self, haystack: &str) -> bool {
584        if (self as u32) < 128 {
585            haystack.as_bytes().contains(&(self as u8))
586        } else {
587            let mut buffer = [0u8; 4];
588            self.encode_utf8(&mut buffer).is_contained_in(haystack)
589        }
590    }
591
592    #[inline]
593    fn is_prefix_of(self, haystack: &str) -> bool {
594        self.encode_utf8(&mut [0u8; 4]).is_prefix_of(haystack)
595    }
596
597    #[inline]
598    fn strip_prefix_of(self, haystack: &str) -> Option<&str> {
599        self.encode_utf8(&mut [0u8; 4]).strip_prefix_of(haystack)
600    }
601
602    #[inline]
603    fn is_suffix_of<'a>(self, haystack: &'a str) -> bool
604    where
605        Self::Searcher<'a>: ReverseSearcher<'a>,
606    {
607        self.encode_utf8(&mut [0u8; 4]).is_suffix_of(haystack)
608    }
609
610    #[inline]
611    fn strip_suffix_of<'a>(self, haystack: &'a str) -> Option<&'a str>
612    where
613        Self::Searcher<'a>: ReverseSearcher<'a>,
614    {
615        self.encode_utf8(&mut [0u8; 4]).strip_suffix_of(haystack)
616    }
617
618    #[inline]
619    fn as_utf8_pattern(&self) -> Option<Utf8Pattern<'_>> {
620        Some(Utf8Pattern::CharPattern(*self))
621    }
622}
623
624/////////////////////////////////////////////////////////////////////////////
625// Impl for a MultiCharEq wrapper
626/////////////////////////////////////////////////////////////////////////////
627
628#[doc(hidden)]
629trait MultiCharEq {
630    fn matches(&mut self, c: char) -> bool;
631}
632
633impl<F> MultiCharEq for F
634where
635    F: FnMut(char) -> bool,
636{
637    #[inline]
638    fn matches(&mut self, c: char) -> bool {
639        (*self)(c)
640    }
641}
642
643impl<const N: usize> MultiCharEq for [char; N] {
644    #[inline]
645    fn matches(&mut self, c: char) -> bool {
646        self.contains(&c)
647    }
648}
649
650impl<const N: usize> MultiCharEq for &[char; N] {
651    #[inline]
652    fn matches(&mut self, c: char) -> bool {
653        self.contains(&c)
654    }
655}
656
657impl MultiCharEq for &[char] {
658    #[inline]
659    fn matches(&mut self, c: char) -> bool {
660        self.contains(&c)
661    }
662}
663
664struct MultiCharEqPattern<C: MultiCharEq>(C);
665
666#[derive(Clone, Debug)]
667struct MultiCharEqSearcher<'a, C: MultiCharEq> {
668    char_eq: C,
669    haystack: &'a str,
670    char_indices: super::CharIndices<'a>,
671}
672
673impl<C: MultiCharEq> Pattern for MultiCharEqPattern<C> {
674    type Searcher<'a> = MultiCharEqSearcher<'a, C>;
675
676    #[inline]
677    fn into_searcher(self, haystack: &str) -> MultiCharEqSearcher<'_, C> {
678        MultiCharEqSearcher { haystack, char_eq: self.0, char_indices: haystack.char_indices() }
679    }
680}
681
682unsafe impl<'a, C: MultiCharEq> Searcher<'a> for MultiCharEqSearcher<'a, C> {
683    #[inline]
684    fn haystack(&self) -> &'a str {
685        self.haystack
686    }
687
688    #[inline]
689    fn next(&mut self) -> SearchStep {
690        let s = &mut self.char_indices;
691        // Compare lengths of the internal byte slice iterator
692        // to find length of current char
693        let pre_len = s.iter.iter.len();
694        if let Some((i, c)) = s.next() {
695            let len = s.iter.iter.len();
696            let char_len = pre_len - len;
697            if self.char_eq.matches(c) {
698                return SearchStep::Match(i, i + char_len);
699            } else {
700                return SearchStep::Reject(i, i + char_len);
701            }
702        }
703        SearchStep::Done
704    }
705}
706
707unsafe impl<'a, C: MultiCharEq> ReverseSearcher<'a> for MultiCharEqSearcher<'a, C> {
708    #[inline]
709    fn next_back(&mut self) -> SearchStep {
710        let s = &mut self.char_indices;
711        // Compare lengths of the internal byte slice iterator
712        // to find length of current char
713        let pre_len = s.iter.iter.len();
714        if let Some((i, c)) = s.next_back() {
715            let len = s.iter.iter.len();
716            let char_len = pre_len - len;
717            if self.char_eq.matches(c) {
718                return SearchStep::Match(i, i + char_len);
719            } else {
720                return SearchStep::Reject(i, i + char_len);
721            }
722        }
723        SearchStep::Done
724    }
725}
726
727impl<'a, C: MultiCharEq> DoubleEndedSearcher<'a> for MultiCharEqSearcher<'a, C> {}
728
729/////////////////////////////////////////////////////////////////////////////
730
731macro_rules! pattern_methods {
732    ($a:lifetime, $t:ty, $pmap:expr, $smap:expr) => {
733        type Searcher<$a> = $t;
734
735        #[inline]
736        fn into_searcher<$a>(self, haystack: &$a str) -> $t {
737            ($smap)(($pmap)(self).into_searcher(haystack))
738        }
739
740        #[inline]
741        fn is_contained_in<$a>(self, haystack: &$a str) -> bool {
742            ($pmap)(self).is_contained_in(haystack)
743        }
744
745        #[inline]
746        fn is_prefix_of<$a>(self, haystack: &$a str) -> bool {
747            ($pmap)(self).is_prefix_of(haystack)
748        }
749
750        #[inline]
751        fn strip_prefix_of<$a>(self, haystack: &$a str) -> Option<&$a str> {
752            ($pmap)(self).strip_prefix_of(haystack)
753        }
754
755        #[inline]
756        fn is_suffix_of<$a>(self, haystack: &$a str) -> bool
757        where
758            $t: ReverseSearcher<$a>,
759        {
760            ($pmap)(self).is_suffix_of(haystack)
761        }
762
763        #[inline]
764        fn strip_suffix_of<$a>(self, haystack: &$a str) -> Option<&$a str>
765        where
766            $t: ReverseSearcher<$a>,
767        {
768            ($pmap)(self).strip_suffix_of(haystack)
769        }
770    };
771}
772
773macro_rules! searcher_methods {
774    (forward) => {
775        #[inline]
776        fn haystack(&self) -> &'a str {
777            self.0.haystack()
778        }
779        #[inline]
780        fn next(&mut self) -> SearchStep {
781            self.0.next()
782        }
783        #[inline]
784        fn next_match(&mut self) -> Option<(usize, usize)> {
785            self.0.next_match()
786        }
787        #[inline]
788        fn next_reject(&mut self) -> Option<(usize, usize)> {
789            self.0.next_reject()
790        }
791    };
792    (reverse) => {
793        #[inline]
794        fn next_back(&mut self) -> SearchStep {
795            self.0.next_back()
796        }
797        #[inline]
798        fn next_match_back(&mut self) -> Option<(usize, usize)> {
799            self.0.next_match_back()
800        }
801        #[inline]
802        fn next_reject_back(&mut self) -> Option<(usize, usize)> {
803            self.0.next_reject_back()
804        }
805    };
806}
807
808/// Associated type for `<[char; N] as Pattern>::Searcher<'a>`.
809#[derive(Clone, Debug)]
810pub struct CharArraySearcher<'a, const N: usize>(
811    <MultiCharEqPattern<[char; N]> as Pattern>::Searcher<'a>,
812);
813
814/// Associated type for `<&[char; N] as Pattern>::Searcher<'a>`.
815#[derive(Clone, Debug)]
816pub struct CharArrayRefSearcher<'a, 'b, const N: usize>(
817    <MultiCharEqPattern<&'b [char; N]> as Pattern>::Searcher<'a>,
818);
819
820/// Searches for chars that are equal to any of the [`char`]s in the array.
821///
822/// # Examples
823///
824/// ```
825/// assert_eq!("Hello world".find(['o', 'l']), Some(2));
826/// assert_eq!("Hello world".find(['h', 'w']), Some(6));
827/// ```
828impl<const N: usize> Pattern for [char; N] {
829    pattern_methods!('a, CharArraySearcher<'a, N>, MultiCharEqPattern, CharArraySearcher);
830}
831
832unsafe impl<'a, const N: usize> Searcher<'a> for CharArraySearcher<'a, N> {
833    searcher_methods!(forward);
834}
835
836unsafe impl<'a, const N: usize> ReverseSearcher<'a> for CharArraySearcher<'a, N> {
837    searcher_methods!(reverse);
838}
839
840impl<'a, const N: usize> DoubleEndedSearcher<'a> for CharArraySearcher<'a, N> {}
841
842/// Searches for chars that are equal to any of the [`char`]s in the array.
843///
844/// # Examples
845///
846/// ```
847/// assert_eq!("Hello world".find(&['o', 'l']), Some(2));
848/// assert_eq!("Hello world".find(&['h', 'w']), Some(6));
849/// ```
850impl<'b, const N: usize> Pattern for &'b [char; N] {
851    pattern_methods!('a, CharArrayRefSearcher<'a, 'b, N>, MultiCharEqPattern, CharArrayRefSearcher);
852}
853
854unsafe impl<'a, 'b, const N: usize> Searcher<'a> for CharArrayRefSearcher<'a, 'b, N> {
855    searcher_methods!(forward);
856}
857
858unsafe impl<'a, 'b, const N: usize> ReverseSearcher<'a> for CharArrayRefSearcher<'a, 'b, N> {
859    searcher_methods!(reverse);
860}
861
862impl<'a, 'b, const N: usize> DoubleEndedSearcher<'a> for CharArrayRefSearcher<'a, 'b, N> {}
863
864/////////////////////////////////////////////////////////////////////////////
865// Impl for &[char]
866/////////////////////////////////////////////////////////////////////////////
867
868// Todo: Change / Remove due to ambiguity in meaning.
869
870/// Associated type for `<&[char] as Pattern>::Searcher<'a>`.
871#[derive(Clone, Debug)]
872pub struct CharSliceSearcher<'a, 'b>(<MultiCharEqPattern<&'b [char]> as Pattern>::Searcher<'a>);
873
874unsafe impl<'a, 'b> Searcher<'a> for CharSliceSearcher<'a, 'b> {
875    searcher_methods!(forward);
876}
877
878unsafe impl<'a, 'b> ReverseSearcher<'a> for CharSliceSearcher<'a, 'b> {
879    searcher_methods!(reverse);
880}
881
882impl<'a, 'b> DoubleEndedSearcher<'a> for CharSliceSearcher<'a, 'b> {}
883
884/// Searches for chars that are equal to any of the [`char`]s in the slice.
885///
886/// # Examples
887///
888/// ```
889/// assert_eq!("Hello world".find(&['o', 'l'][..]), Some(2));
890/// assert_eq!("Hello world".find(&['h', 'w'][..]), Some(6));
891/// ```
892impl<'b> Pattern for &'b [char] {
893    pattern_methods!('a, CharSliceSearcher<'a, 'b>, MultiCharEqPattern, CharSliceSearcher);
894}
895
896/////////////////////////////////////////////////////////////////////////////
897// Impl for F: FnMut(char) -> bool
898/////////////////////////////////////////////////////////////////////////////
899
900/// Associated type for `<F as Pattern>::Searcher<'a>`.
901#[derive(Clone)]
902pub struct CharPredicateSearcher<'a, F>(<MultiCharEqPattern<F> as Pattern>::Searcher<'a>)
903where
904    F: FnMut(char) -> bool;
905
906impl<F> fmt::Debug for CharPredicateSearcher<'_, F>
907where
908    F: FnMut(char) -> bool,
909{
910    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
911        f.debug_struct("CharPredicateSearcher")
912            .field("haystack", &self.0.haystack)
913            .field("char_indices", &self.0.char_indices)
914            .finish()
915    }
916}
917unsafe impl<'a, F> Searcher<'a> for CharPredicateSearcher<'a, F>
918where
919    F: FnMut(char) -> bool,
920{
921    searcher_methods!(forward);
922}
923
924unsafe impl<'a, F> ReverseSearcher<'a> for CharPredicateSearcher<'a, F>
925where
926    F: FnMut(char) -> bool,
927{
928    searcher_methods!(reverse);
929}
930
931impl<'a, F> DoubleEndedSearcher<'a> for CharPredicateSearcher<'a, F> where F: FnMut(char) -> bool {}
932
933/// Searches for [`char`]s that match the given predicate.
934///
935/// # Examples
936///
937/// ```
938/// assert_eq!("Hello world".find(char::is_uppercase), Some(0));
939/// assert_eq!("Hello world".find(|c| "aeiou".contains(c)), Some(1));
940/// ```
941impl<F> Pattern for F
942where
943    F: FnMut(char) -> bool,
944{
945    pattern_methods!('a, CharPredicateSearcher<'a, F>, MultiCharEqPattern, CharPredicateSearcher);
946}
947
948/////////////////////////////////////////////////////////////////////////////
949// Impl for &&str
950/////////////////////////////////////////////////////////////////////////////
951
952/// Delegates to the `&str` impl.
953impl<'b, 'c> Pattern for &'c &'b str {
954    pattern_methods!('a, StrSearcher<'a, 'b>, |&s| s, |s| s);
955}
956
957/////////////////////////////////////////////////////////////////////////////
958// Impl for &str
959/////////////////////////////////////////////////////////////////////////////
960
961/// Non-allocating substring search.
962///
963/// Will handle the pattern `""` as returning empty matches at each character
964/// boundary.
965///
966/// # Examples
967///
968/// ```
969/// assert_eq!("Hello world".find("world"), Some(6));
970/// ```
971impl<'b> Pattern for &'b str {
972    type Searcher<'a> = StrSearcher<'a, 'b>;
973
974    #[inline]
975    fn into_searcher(self, haystack: &str) -> StrSearcher<'_, 'b> {
976        StrSearcher::new(haystack, self)
977    }
978
979    /// Checks whether the pattern matches at the front of the haystack.
980    #[inline]
981    fn is_prefix_of(self, haystack: &str) -> bool {
982        haystack.as_bytes().starts_with(self.as_bytes())
983    }
984
985    /// Checks whether the pattern matches anywhere in the haystack
986    #[inline]
987    fn is_contained_in(self, haystack: &str) -> bool {
988        if self.len() == 0 {
989            return true;
990        }
991
992        match self.len().cmp(&haystack.len()) {
993            Ordering::Less => {
994                if self.len() == 1 {
995                    return haystack.as_bytes().contains(&self.as_bytes()[0]);
996                }
997
998                #[cfg(any(
999                    all(target_arch = "x86_64", target_feature = "sse2"),
1000                    all(target_arch = "loongarch64", target_feature = "lsx"),
1001                    all(target_arch = "aarch64", target_feature = "neon")
1002                ))]
1003                if self.len() <= 32 {
1004                    if let Some(result) = simd_contains(self, haystack) {
1005                        return result;
1006                    }
1007                }
1008
1009                self.into_searcher(haystack).next_match().is_some()
1010            }
1011            _ => self == haystack,
1012        }
1013    }
1014
1015    /// Removes the pattern from the front of haystack, if it matches.
1016    #[inline]
1017    fn strip_prefix_of(self, haystack: &str) -> Option<&str> {
1018        if self.is_prefix_of(haystack) {
1019            // SAFETY: prefix was just verified to exist.
1020            unsafe { Some(haystack.get_unchecked(self.as_bytes().len()..)) }
1021        } else {
1022            None
1023        }
1024    }
1025
1026    /// Checks whether the pattern matches at the back of the haystack.
1027    #[inline]
1028    fn is_suffix_of<'a>(self, haystack: &'a str) -> bool
1029    where
1030        Self::Searcher<'a>: ReverseSearcher<'a>,
1031    {
1032        haystack.as_bytes().ends_with(self.as_bytes())
1033    }
1034
1035    /// Removes the pattern from the back of haystack, if it matches.
1036    #[inline]
1037    fn strip_suffix_of<'a>(self, haystack: &'a str) -> Option<&'a str>
1038    where
1039        Self::Searcher<'a>: ReverseSearcher<'a>,
1040    {
1041        if self.is_suffix_of(haystack) {
1042            let i = haystack.len() - self.as_bytes().len();
1043            // SAFETY: suffix was just verified to exist.
1044            unsafe { Some(haystack.get_unchecked(..i)) }
1045        } else {
1046            None
1047        }
1048    }
1049
1050    #[inline]
1051    fn as_utf8_pattern(&self) -> Option<Utf8Pattern<'_>> {
1052        Some(Utf8Pattern::StringPattern(self.as_bytes()))
1053    }
1054}
1055
1056/////////////////////////////////////////////////////////////////////////////
1057// Two Way substring searcher
1058/////////////////////////////////////////////////////////////////////////////
1059
1060#[derive(Clone, Debug)]
1061/// Associated type for `<&str as Pattern>::Searcher<'a>`.
1062pub struct StrSearcher<'a, 'b> {
1063    haystack: &'a str,
1064    needle: &'b str,
1065
1066    searcher: StrSearcherImpl,
1067}
1068
1069#[derive(Clone, Debug)]
1070enum StrSearcherImpl {
1071    Empty(EmptyNeedle),
1072    TwoWay(TwoWaySearcher),
1073}
1074
1075#[derive(Clone, Debug)]
1076struct EmptyNeedle {
1077    position: usize,
1078    end: usize,
1079    is_match_fw: bool,
1080    is_match_bw: bool,
1081    // Needed in case of an empty haystack, see #85462
1082    is_finished: bool,
1083}
1084
1085impl<'a, 'b> StrSearcher<'a, 'b> {
1086    fn new(haystack: &'a str, needle: &'b str) -> StrSearcher<'a, 'b> {
1087        if needle.is_empty() {
1088            StrSearcher {
1089                haystack,
1090                needle,
1091                searcher: StrSearcherImpl::Empty(EmptyNeedle {
1092                    position: 0,
1093                    end: haystack.len(),
1094                    is_match_fw: true,
1095                    is_match_bw: true,
1096                    is_finished: false,
1097                }),
1098            }
1099        } else {
1100            StrSearcher {
1101                haystack,
1102                needle,
1103                searcher: StrSearcherImpl::TwoWay(TwoWaySearcher::new(
1104                    needle.as_bytes(),
1105                    haystack.len(),
1106                )),
1107            }
1108        }
1109    }
1110}
1111
1112unsafe impl<'a, 'b> Searcher<'a> for StrSearcher<'a, 'b> {
1113    #[inline]
1114    fn haystack(&self) -> &'a str {
1115        self.haystack
1116    }
1117
1118    #[inline]
1119    fn next(&mut self) -> SearchStep {
1120        match self.searcher {
1121            StrSearcherImpl::Empty(ref mut searcher) => {
1122                if searcher.is_finished {
1123                    return SearchStep::Done;
1124                }
1125                // empty needle rejects every char and matches every empty string between them
1126                let is_match = searcher.is_match_fw;
1127                searcher.is_match_fw = !searcher.is_match_fw;
1128                let pos = searcher.position;
1129                match self.haystack[pos..].chars().next() {
1130                    _ if is_match => SearchStep::Match(pos, pos),
1131                    None => {
1132                        searcher.is_finished = true;
1133                        SearchStep::Done
1134                    }
1135                    Some(ch) => {
1136                        searcher.position += ch.len_utf8();
1137                        SearchStep::Reject(pos, searcher.position)
1138                    }
1139                }
1140            }
1141            StrSearcherImpl::TwoWay(ref mut searcher) => {
1142                // TwoWaySearcher produces valid *Match* indices that split at char boundaries
1143                // as long as it does correct matching and that haystack and needle are
1144                // valid UTF-8
1145                // *Rejects* from the algorithm can fall on any indices, but we will walk them
1146                // manually to the next character boundary, so that they are utf-8 safe.
1147                if searcher.position == self.haystack.len() {
1148                    return SearchStep::Done;
1149                }
1150                let is_long = searcher.memory == usize::MAX;
1151                match searcher.next::<RejectAndMatch>(
1152                    self.haystack.as_bytes(),
1153                    self.needle.as_bytes(),
1154                    is_long,
1155                ) {
1156                    SearchStep::Reject(a, mut b) => {
1157                        // skip to next char boundary
1158                        while !self.haystack.is_char_boundary(b) {
1159                            b += 1;
1160                        }
1161                        searcher.position = cmp::max(b, searcher.position);
1162                        SearchStep::Reject(a, b)
1163                    }
1164                    otherwise => otherwise,
1165                }
1166            }
1167        }
1168    }
1169
1170    #[inline]
1171    fn next_match(&mut self) -> Option<(usize, usize)> {
1172        match self.searcher {
1173            StrSearcherImpl::Empty(..) => loop {
1174                match self.next() {
1175                    SearchStep::Match(a, b) => return Some((a, b)),
1176                    SearchStep::Done => return None,
1177                    SearchStep::Reject(..) => {}
1178                }
1179            },
1180            StrSearcherImpl::TwoWay(ref mut searcher) => {
1181                let is_long = searcher.memory == usize::MAX;
1182                // write out `true` and `false` cases to encourage the compiler
1183                // to specialize the two cases separately.
1184                if is_long {
1185                    searcher.next::<MatchOnly>(
1186                        self.haystack.as_bytes(),
1187                        self.needle.as_bytes(),
1188                        true,
1189                    )
1190                } else {
1191                    searcher.next::<MatchOnly>(
1192                        self.haystack.as_bytes(),
1193                        self.needle.as_bytes(),
1194                        false,
1195                    )
1196                }
1197            }
1198        }
1199    }
1200}
1201
1202unsafe impl<'a, 'b> ReverseSearcher<'a> for StrSearcher<'a, 'b> {
1203    #[inline]
1204    fn next_back(&mut self) -> SearchStep {
1205        match self.searcher {
1206            StrSearcherImpl::Empty(ref mut searcher) => {
1207                if searcher.is_finished {
1208                    return SearchStep::Done;
1209                }
1210                let is_match = searcher.is_match_bw;
1211                searcher.is_match_bw = !searcher.is_match_bw;
1212                let end = searcher.end;
1213                match self.haystack[..end].chars().next_back() {
1214                    _ if is_match => SearchStep::Match(end, end),
1215                    None => {
1216                        searcher.is_finished = true;
1217                        SearchStep::Done
1218                    }
1219                    Some(ch) => {
1220                        searcher.end -= ch.len_utf8();
1221                        SearchStep::Reject(searcher.end, end)
1222                    }
1223                }
1224            }
1225            StrSearcherImpl::TwoWay(ref mut searcher) => {
1226                if searcher.end == 0 {
1227                    return SearchStep::Done;
1228                }
1229                let is_long = searcher.memory == usize::MAX;
1230                match searcher.next_back::<RejectAndMatch>(
1231                    self.haystack.as_bytes(),
1232                    self.needle.as_bytes(),
1233                    is_long,
1234                ) {
1235                    SearchStep::Reject(mut a, b) => {
1236                        // skip to next char boundary
1237                        while !self.haystack.is_char_boundary(a) {
1238                            a -= 1;
1239                        }
1240                        searcher.end = cmp::min(a, searcher.end);
1241                        SearchStep::Reject(a, b)
1242                    }
1243                    otherwise => otherwise,
1244                }
1245            }
1246        }
1247    }
1248
1249    #[inline]
1250    fn next_match_back(&mut self) -> Option<(usize, usize)> {
1251        match self.searcher {
1252            StrSearcherImpl::Empty(..) => loop {
1253                match self.next_back() {
1254                    SearchStep::Match(a, b) => return Some((a, b)),
1255                    SearchStep::Done => return None,
1256                    SearchStep::Reject(..) => {}
1257                }
1258            },
1259            StrSearcherImpl::TwoWay(ref mut searcher) => {
1260                let is_long = searcher.memory == usize::MAX;
1261                // write out `true` and `false`, like `next_match`
1262                if is_long {
1263                    searcher.next_back::<MatchOnly>(
1264                        self.haystack.as_bytes(),
1265                        self.needle.as_bytes(),
1266                        true,
1267                    )
1268                } else {
1269                    searcher.next_back::<MatchOnly>(
1270                        self.haystack.as_bytes(),
1271                        self.needle.as_bytes(),
1272                        false,
1273                    )
1274                }
1275            }
1276        }
1277    }
1278}
1279
1280/// The internal state of the two-way substring search algorithm.
1281#[derive(Clone, Debug)]
1282struct TwoWaySearcher {
1283    // constants
1284    /// critical factorization index
1285    crit_pos: usize,
1286    /// critical factorization index for reversed needle
1287    crit_pos_back: usize,
1288    period: usize,
1289    /// `byteset` is an extension (not part of the two way algorithm);
1290    /// it's a 64-bit "fingerprint" where each set bit `j` corresponds
1291    /// to a (byte & 63) == j present in the needle.
1292    byteset: u64,
1293
1294    // variables
1295    position: usize,
1296    end: usize,
1297    /// index into needle before which we have already matched
1298    memory: usize,
1299    /// index into needle after which we have already matched
1300    memory_back: usize,
1301}
1302
1303/*
1304    This is the Two-Way search algorithm, which was introduced in the paper:
1305    Crochemore, M., Perrin, D., 1991, Two-way string-matching, Journal of the ACM 38(3):651-675.
1306
1307    Here's some background information.
1308
1309    A *word* is a string of symbols. The *length* of a word should be a familiar
1310    notion, and here we denote it for any word x by |x|.
1311    (We also allow for the possibility of the *empty word*, a word of length zero).
1312
1313    If x is any non-empty word, then an integer p with 0 < p <= |x| is said to be a
1314    *period* for x iff for all i with 0 <= i <= |x| - p - 1, we have x[i] == x[i+p].
1315    For example, both 1 and 2 are periods for the string "aa". As another example,
1316    the only period of the string "abcd" is 4.
1317
1318    We denote by period(x) the *smallest* period of x (provided that x is non-empty).
1319    This is always well-defined since every non-empty word x has at least one period,
1320    |x|. We sometimes call this *the period* of x.
1321
1322    If u, v and x are words such that x = uv, where uv is the concatenation of u and
1323    v, then we say that (u, v) is a *factorization* of x.
1324
1325    Let (u, v) be a factorization for a word x. Then if w is a non-empty word such
1326    that both of the following hold
1327
1328      - either w is a suffix of u or u is a suffix of w
1329      - either w is a prefix of v or v is a prefix of w
1330
1331    then w is said to be a *repetition* for the factorization (u, v).
1332
1333    Just to unpack this, there are four possibilities here. Let w = "abc". Then we
1334    might have:
1335
1336      - w is a suffix of u and w is a prefix of v. ex: ("lolabc", "abcde")
1337      - w is a suffix of u and v is a prefix of w. ex: ("lolabc", "ab")
1338      - u is a suffix of w and w is a prefix of v. ex: ("bc", "abchi")
1339      - u is a suffix of w and v is a prefix of w. ex: ("bc", "a")
1340
1341    Note that the word vu is a repetition for any factorization (u,v) of x = uv,
1342    so every factorization has at least one repetition.
1343
1344    If x is a string and (u, v) is a factorization for x, then a *local period* for
1345    (u, v) is an integer r such that there is some word w such that |w| = r and w is
1346    a repetition for (u, v).
1347
1348    We denote by local_period(u, v) the smallest local period of (u, v). We sometimes
1349    call this *the local period* of (u, v). Provided that x = uv is non-empty, this
1350    is well-defined (because each non-empty word has at least one factorization, as
1351    noted above).
1352
1353    It can be proven that the following is an equivalent definition of a local period
1354    for a factorization (u, v): any positive integer r such that x[i] == x[i+r] for
1355    all i such that |u| - r <= i <= |u| - 1 and such that both x[i] and x[i+r] are
1356    defined. (i.e., i > 0 and i + r < |x|).
1357
1358    Using the above reformulation, it is easy to prove that
1359
1360        1 <= local_period(u, v) <= period(uv)
1361
1362    A factorization (u, v) of x such that local_period(u,v) = period(x) is called a
1363    *critical factorization*.
1364
1365    The algorithm hinges on the following theorem, which is stated without proof:
1366
1367    **Critical Factorization Theorem** Any word x has at least one critical
1368    factorization (u, v) such that |u| < period(x).
1369
1370    The purpose of maximal_suffix is to find such a critical factorization.
1371
1372    If the period is short, compute another factorization x = u' v' to use
1373    for reverse search, chosen instead so that |v'| < period(x).
1374
1375*/
1376impl TwoWaySearcher {
1377    fn new(needle: &[u8], end: usize) -> TwoWaySearcher {
1378        let (crit_pos_false, period_false) = TwoWaySearcher::maximal_suffix(needle, false);
1379        let (crit_pos_true, period_true) = TwoWaySearcher::maximal_suffix(needle, true);
1380
1381        let (crit_pos, period) = if crit_pos_false > crit_pos_true {
1382            (crit_pos_false, period_false)
1383        } else {
1384            (crit_pos_true, period_true)
1385        };
1386
1387        // A particularly readable explanation of what's going on here can be found
1388        // in Crochemore and Rytter's book "Text Algorithms", ch 13. Specifically
1389        // see the code for "Algorithm CP" on p. 323.
1390        //
1391        // What's going on is we have some critical factorization (u, v) of the
1392        // needle, and we want to determine whether u is a suffix of
1393        // &v[..period]. If it is, we use "Algorithm CP1". Otherwise we use
1394        // "Algorithm CP2", which is optimized for when the period of the needle
1395        // is large.
1396        if needle[..crit_pos] == needle[period..period + crit_pos] {
1397            // short period case -- the period is exact
1398            // compute a separate critical factorization for the reversed needle
1399            // x = u' v' where |v'| < period(x).
1400            //
1401            // This is sped up by the period being known already.
1402            // Note that a case like x = "acba" may be factored exactly forwards
1403            // (crit_pos = 1, period = 3) while being factored with approximate
1404            // period in reverse (crit_pos = 2, period = 2). We use the given
1405            // reverse factorization but keep the exact period.
1406            let crit_pos_back = needle.len()
1407                - cmp::max(
1408                    TwoWaySearcher::reverse_maximal_suffix(needle, period, false),
1409                    TwoWaySearcher::reverse_maximal_suffix(needle, period, true),
1410                );
1411
1412            TwoWaySearcher {
1413                crit_pos,
1414                crit_pos_back,
1415                period,
1416                byteset: Self::byteset_create(&needle[..period]),
1417
1418                position: 0,
1419                end,
1420                memory: 0,
1421                memory_back: needle.len(),
1422            }
1423        } else {
1424            // long period case -- we have an approximation to the actual period,
1425            // and don't use memorization.
1426            //
1427            // Approximate the period by lower bound max(|u|, |v|) + 1.
1428            // The critical factorization is efficient to use for both forward and
1429            // reverse search.
1430
1431            TwoWaySearcher {
1432                crit_pos,
1433                crit_pos_back: crit_pos,
1434                period: cmp::max(crit_pos, needle.len() - crit_pos) + 1,
1435                byteset: Self::byteset_create(needle),
1436
1437                position: 0,
1438                end,
1439                memory: usize::MAX, // Dummy value to signify that the period is long
1440                memory_back: usize::MAX,
1441            }
1442        }
1443    }
1444
1445    #[inline]
1446    fn byteset_create(bytes: &[u8]) -> u64 {
1447        bytes.iter().fold(0, |a, &b| (1 << (b & 0x3f)) | a)
1448    }
1449
1450    #[inline]
1451    fn byteset_contains(&self, byte: u8) -> bool {
1452        (self.byteset >> ((byte & 0x3f) as usize)) & 1 != 0
1453    }
1454
1455    // One of the main ideas of Two-Way is that we factorize the needle into
1456    // two halves, (u, v), and begin trying to find v in the haystack by scanning
1457    // left to right. If v matches, we try to match u by scanning right to left.
1458    // How far we can jump when we encounter a mismatch is all based on the fact
1459    // that (u, v) is a critical factorization for the needle.
1460    #[inline]
1461    fn next<S>(&mut self, haystack: &[u8], needle: &[u8], long_period: bool) -> S::Output
1462    where
1463        S: TwoWayStrategy,
1464    {
1465        // `next()` uses `self.position` as its cursor
1466        let old_pos = self.position;
1467        let needle_last = needle.len() - 1;
1468        'search: loop {
1469            // Check that we have room to search in
1470            // position + needle_last can not overflow if we assume slices
1471            // are bounded by isize's range.
1472            let tail_byte = match haystack.get(self.position + needle_last) {
1473                Some(&b) => b,
1474                None => {
1475                    self.position = haystack.len();
1476                    return S::rejecting(old_pos, self.position);
1477                }
1478            };
1479
1480            if S::use_early_reject() && old_pos != self.position {
1481                return S::rejecting(old_pos, self.position);
1482            }
1483
1484            // Quickly skip by large portions unrelated to our substring
1485            if !self.byteset_contains(tail_byte) {
1486                self.position += needle.len();
1487                if !long_period {
1488                    self.memory = 0;
1489                }
1490                continue 'search;
1491            }
1492
1493            // See if the right part of the needle matches
1494            let start =
1495                if long_period { self.crit_pos } else { cmp::max(self.crit_pos, self.memory) };
1496            for i in start..needle.len() {
1497                if needle[i] != haystack[self.position + i] {
1498                    self.position += i - self.crit_pos + 1;
1499                    if !long_period {
1500                        self.memory = 0;
1501                    }
1502                    continue 'search;
1503                }
1504            }
1505
1506            // See if the left part of the needle matches
1507            let start = if long_period { 0 } else { self.memory };
1508            for i in (start..self.crit_pos).rev() {
1509                if needle[i] != haystack[self.position + i] {
1510                    self.position += self.period;
1511                    if !long_period {
1512                        self.memory = needle.len() - self.period;
1513                    }
1514                    continue 'search;
1515                }
1516            }
1517
1518            // We have found a match!
1519            let match_pos = self.position;
1520
1521            // Note: add self.period instead of needle.len() to have overlapping matches
1522            self.position += needle.len();
1523            if !long_period {
1524                self.memory = 0; // set to needle.len() - self.period for overlapping matches
1525            }
1526
1527            return S::matching(match_pos, match_pos + needle.len());
1528        }
1529    }
1530
1531    // Follows the ideas in `next()`.
1532    //
1533    // The definitions are symmetrical, with period(x) = period(reverse(x))
1534    // and local_period(u, v) = local_period(reverse(v), reverse(u)), so if (u, v)
1535    // is a critical factorization, so is (reverse(v), reverse(u)).
1536    //
1537    // For the reverse case we have computed a critical factorization x = u' v'
1538    // (field `crit_pos_back`). We need |u| < period(x) for the forward case and
1539    // thus |v'| < period(x) for the reverse.
1540    //
1541    // To search in reverse through the haystack, we search forward through
1542    // a reversed haystack with a reversed needle, matching first u' and then v'.
1543    #[inline]
1544    fn next_back<S>(&mut self, haystack: &[u8], needle: &[u8], long_period: bool) -> S::Output
1545    where
1546        S: TwoWayStrategy,
1547    {
1548        // `next_back()` uses `self.end` as its cursor -- so that `next()` and `next_back()`
1549        // are independent.
1550        let old_end = self.end;
1551        'search: loop {
1552            // Check that we have room to search in
1553            // end - needle.len() will wrap around when there is no more room,
1554            // but due to slice length limits it can never wrap all the way back
1555            // into the length of haystack.
1556            let front_byte = match haystack.get(self.end.wrapping_sub(needle.len())) {
1557                Some(&b) => b,
1558                None => {
1559                    self.end = 0;
1560                    return S::rejecting(0, old_end);
1561                }
1562            };
1563
1564            if S::use_early_reject() && old_end != self.end {
1565                return S::rejecting(self.end, old_end);
1566            }
1567
1568            // Quickly skip by large portions unrelated to our substring
1569            if !self.byteset_contains(front_byte) {
1570                self.end -= needle.len();
1571                if !long_period {
1572                    self.memory_back = needle.len();
1573                }
1574                continue 'search;
1575            }
1576
1577            // See if the left part of the needle matches
1578            let crit = if long_period {
1579                self.crit_pos_back
1580            } else {
1581                cmp::min(self.crit_pos_back, self.memory_back)
1582            };
1583            for i in (0..crit).rev() {
1584                if needle[i] != haystack[self.end - needle.len() + i] {
1585                    self.end -= self.crit_pos_back - i;
1586                    if !long_period {
1587                        self.memory_back = needle.len();
1588                    }
1589                    continue 'search;
1590                }
1591            }
1592
1593            // See if the right part of the needle matches
1594            let needle_end = if long_period { needle.len() } else { self.memory_back };
1595            for i in self.crit_pos_back..needle_end {
1596                if needle[i] != haystack[self.end - needle.len() + i] {
1597                    self.end -= self.period;
1598                    if !long_period {
1599                        self.memory_back = self.period;
1600                    }
1601                    continue 'search;
1602                }
1603            }
1604
1605            // We have found a match!
1606            let match_pos = self.end - needle.len();
1607            // Note: sub self.period instead of needle.len() to have overlapping matches
1608            self.end -= needle.len();
1609            if !long_period {
1610                self.memory_back = needle.len();
1611            }
1612
1613            return S::matching(match_pos, match_pos + needle.len());
1614        }
1615    }
1616
1617    // Compute the maximal suffix of `arr`.
1618    //
1619    // The maximal suffix is a possible critical factorization (u, v) of `arr`.
1620    //
1621    // Returns (`i`, `p`) where `i` is the starting index of v and `p` is the
1622    // period of v.
1623    //
1624    // `order_greater` determines if lexical order is `<` or `>`. Both
1625    // orders must be computed -- the ordering with the largest `i` gives
1626    // a critical factorization.
1627    //
1628    // For long period cases, the resulting period is not exact (it is too short).
1629    #[inline]
1630    fn maximal_suffix(arr: &[u8], order_greater: bool) -> (usize, usize) {
1631        let mut left = 0; // Corresponds to i in the paper
1632        let mut right = 1; // Corresponds to j in the paper
1633        let mut offset = 0; // Corresponds to k in the paper, but starting at 0
1634        // to match 0-based indexing.
1635        let mut period = 1; // Corresponds to p in the paper
1636
1637        while let Some(&a) = arr.get(right + offset) {
1638            // `left` will be inbounds when `right` is.
1639            let b = arr[left + offset];
1640            if (a < b && !order_greater) || (a > b && order_greater) {
1641                // Suffix is smaller, period is entire prefix so far.
1642                right += offset + 1;
1643                offset = 0;
1644                period = right - left;
1645            } else if a == b {
1646                // Advance through repetition of the current period.
1647                if offset + 1 == period {
1648                    right += offset + 1;
1649                    offset = 0;
1650                } else {
1651                    offset += 1;
1652                }
1653            } else {
1654                // Suffix is larger, start over from current location.
1655                left = right;
1656                right += 1;
1657                offset = 0;
1658                period = 1;
1659            }
1660        }
1661        (left, period)
1662    }
1663
1664    // Compute the maximal suffix of the reverse of `arr`.
1665    //
1666    // The maximal suffix is a possible critical factorization (u', v') of `arr`.
1667    //
1668    // Returns `i` where `i` is the starting index of v', from the back;
1669    // returns immediately when a period of `known_period` is reached.
1670    //
1671    // `order_greater` determines if lexical order is `<` or `>`. Both
1672    // orders must be computed -- the ordering with the largest `i` gives
1673    // a critical factorization.
1674    //
1675    // For long period cases, the resulting period is not exact (it is too short).
1676    fn reverse_maximal_suffix(arr: &[u8], known_period: usize, order_greater: bool) -> usize {
1677        let mut left = 0; // Corresponds to i in the paper
1678        let mut right = 1; // Corresponds to j in the paper
1679        let mut offset = 0; // Corresponds to k in the paper, but starting at 0
1680        // to match 0-based indexing.
1681        let mut period = 1; // Corresponds to p in the paper
1682        let n = arr.len();
1683
1684        while right + offset < n {
1685            let a = arr[n - (1 + right + offset)];
1686            let b = arr[n - (1 + left + offset)];
1687            if (a < b && !order_greater) || (a > b && order_greater) {
1688                // Suffix is smaller, period is entire prefix so far.
1689                right += offset + 1;
1690                offset = 0;
1691                period = right - left;
1692            } else if a == b {
1693                // Advance through repetition of the current period.
1694                if offset + 1 == period {
1695                    right += offset + 1;
1696                    offset = 0;
1697                } else {
1698                    offset += 1;
1699                }
1700            } else {
1701                // Suffix is larger, start over from current location.
1702                left = right;
1703                right += 1;
1704                offset = 0;
1705                period = 1;
1706            }
1707            if period == known_period {
1708                break;
1709            }
1710        }
1711        debug_assert!(period <= known_period);
1712        left
1713    }
1714}
1715
1716// TwoWayStrategy allows the algorithm to either skip non-matches as quickly
1717// as possible, or to work in a mode where it emits Rejects relatively quickly.
1718trait TwoWayStrategy {
1719    type Output;
1720    fn use_early_reject() -> bool;
1721    fn rejecting(a: usize, b: usize) -> Self::Output;
1722    fn matching(a: usize, b: usize) -> Self::Output;
1723}
1724
1725/// Skip to match intervals as quickly as possible
1726enum MatchOnly {}
1727
1728impl TwoWayStrategy for MatchOnly {
1729    type Output = Option<(usize, usize)>;
1730
1731    #[inline]
1732    fn use_early_reject() -> bool {
1733        false
1734    }
1735    #[inline]
1736    fn rejecting(_a: usize, _b: usize) -> Self::Output {
1737        None
1738    }
1739    #[inline]
1740    fn matching(a: usize, b: usize) -> Self::Output {
1741        Some((a, b))
1742    }
1743}
1744
1745/// Emit Rejects regularly
1746enum RejectAndMatch {}
1747
1748impl TwoWayStrategy for RejectAndMatch {
1749    type Output = SearchStep;
1750
1751    #[inline]
1752    fn use_early_reject() -> bool {
1753        true
1754    }
1755    #[inline]
1756    fn rejecting(a: usize, b: usize) -> Self::Output {
1757        SearchStep::Reject(a, b)
1758    }
1759    #[inline]
1760    fn matching(a: usize, b: usize) -> Self::Output {
1761        SearchStep::Match(a, b)
1762    }
1763}
1764
1765/// SIMD search for short needles based on
1766/// Wojciech Muła's "SIMD-friendly algorithms for substring searching"[0]
1767///
1768/// It skips ahead by the vector width on each iteration (rather than the needle length as two-way
1769/// does) by probing the first and last byte of the needle for the whole vector width
1770/// and only doing full needle comparisons when the vectorized probe indicated potential matches.
1771///
1772/// Since the x86_64 baseline only offers SSE2 we only use u8x16 here.
1773/// If we ever ship std with for x86-64-v3 or adapt this for other platforms then wider vectors
1774/// should be evaluated.
1775///
1776/// Similarly, on LoongArch the 128-bit LSX vector extension is the baseline,
1777/// so we also use `u8x16` there. Wider vector widths may be considered
1778/// for future LoongArch extensions (e.g., LASX).
1779///
1780/// For haystacks smaller than vector-size + needle length it falls back to
1781/// a naive O(n*m) search so this implementation should not be called on larger needles.
1782///
1783/// [0]: http://0x80.pl/articles/simd-strfind.html#sse-avx2
1784#[cfg(any(
1785    all(target_arch = "x86_64", target_feature = "sse2"),
1786    all(target_arch = "loongarch64", target_feature = "lsx"),
1787    all(target_arch = "aarch64", target_feature = "neon")
1788))]
1789#[inline]
1790fn simd_contains(needle: &str, haystack: &str) -> Option<bool> {
1791    let needle = needle.as_bytes();
1792    let haystack = haystack.as_bytes();
1793
1794    debug_assert!(needle.len() > 1);
1795
1796    use crate::ops::BitAnd;
1797    use crate::simd::cmp::SimdPartialEq;
1798    use crate::simd::{mask8x16 as Mask, u8x16 as Block};
1799
1800    let first_probe = needle[0];
1801    let last_byte_offset = needle.len() - 1;
1802
1803    // the offset used for the 2nd vector
1804    let second_probe_offset = if needle.len() == 2 {
1805        // never bail out on len=2 needles because the probes will fully cover them and have
1806        // no degenerate cases.
1807        1
1808    } else {
1809        // try a few bytes in case first and last byte of the needle are the same
1810        let Some(second_probe_offset) =
1811            (needle.len().saturating_sub(4)..needle.len()).rfind(|&idx| needle[idx] != first_probe)
1812        else {
1813            // fall back to other search methods if we can't find any different bytes
1814            // since we could otherwise hit some degenerate cases
1815            return None;
1816        };
1817        second_probe_offset
1818    };
1819
1820    // do a naive search if the haystack is too small to fit
1821    if haystack.len() < Block::LEN + last_byte_offset {
1822        return Some(haystack.windows(needle.len()).any(|c| c == needle));
1823    }
1824
1825    let first_probe: Block = Block::splat(first_probe);
1826    let second_probe: Block = Block::splat(needle[second_probe_offset]);
1827    // first byte are already checked by the outer loop. to verify a match only the
1828    // remainder has to be compared.
1829    let trimmed_needle = &needle[1..];
1830
1831    // this #[cold] is load-bearing, benchmark before removing it...
1832    let check_mask = #[cold]
1833    |idx, mask: u16, skip: bool| -> bool {
1834        if skip {
1835            return false;
1836        }
1837
1838        // and so is this. optimizations are weird.
1839        let mut mask = mask;
1840
1841        while mask != 0 {
1842            let trailing = mask.trailing_zeros();
1843            let offset = idx + trailing as usize + 1;
1844            // SAFETY: mask is between 0 and 15 trailing zeroes, we skip one additional byte that was already compared
1845            // and then take trimmed_needle.len() bytes. This is within the bounds defined by the outer loop
1846            unsafe {
1847                let sub = haystack.get_unchecked(offset..).get_unchecked(..trimmed_needle.len());
1848                if small_slice_eq(sub, trimmed_needle) {
1849                    return true;
1850                }
1851            }
1852            mask &= !(1 << trailing);
1853        }
1854        false
1855    };
1856
1857    let test_chunk = |idx| -> u16 {
1858        // SAFETY: this requires at least LANES bytes being readable at idx
1859        // that is ensured by the loop ranges (see comments below)
1860        let a: Block = unsafe { haystack.as_ptr().add(idx).cast::<Block>().read_unaligned() };
1861        // SAFETY: this requires LANES + block_offset bytes being readable at idx
1862        let b: Block = unsafe {
1863            haystack.as_ptr().add(idx).add(second_probe_offset).cast::<Block>().read_unaligned()
1864        };
1865        let eq_first: Mask = a.simd_eq(first_probe);
1866        let eq_last: Mask = b.simd_eq(second_probe);
1867        let both = eq_first.bitand(eq_last);
1868        let mask = both.to_bitmask() as u16;
1869
1870        mask
1871    };
1872
1873    let mut i = 0;
1874    let mut result = false;
1875    // The loop condition must ensure that there's enough headroom to read LANE bytes,
1876    // and not only at the current index but also at the index shifted by block_offset
1877    const UNROLL: usize = 4;
1878    while i + last_byte_offset + UNROLL * Block::LEN < haystack.len() && !result {
1879        let mut masks = [0u16; UNROLL];
1880        for j in 0..UNROLL {
1881            masks[j] = test_chunk(i + j * Block::LEN);
1882        }
1883        for j in 0..UNROLL {
1884            let mask = masks[j];
1885            if mask != 0 {
1886                result |= check_mask(i + j * Block::LEN, mask, result);
1887            }
1888        }
1889        i += UNROLL * Block::LEN;
1890    }
1891    while i + last_byte_offset + Block::LEN < haystack.len() && !result {
1892        let mask = test_chunk(i);
1893        if mask != 0 {
1894            result |= check_mask(i, mask, result);
1895        }
1896        i += Block::LEN;
1897    }
1898
1899    // Process the tail that didn't fit into LANES-sized steps.
1900    // This simply repeats the same procedure but as right-aligned chunk instead
1901    // of a left-aligned one. The last byte must be exactly flush with the string end so
1902    // we don't miss a single byte or read out of bounds.
1903    let i = haystack.len() - last_byte_offset - Block::LEN;
1904    let mask = test_chunk(i);
1905    if mask != 0 {
1906        result |= check_mask(i, mask, result);
1907    }
1908
1909    Some(result)
1910}
1911
1912/// Compares short slices for equality.
1913///
1914/// It avoids a call to libc's memcmp which is faster on long slices
1915/// due to SIMD optimizations but it incurs a function call overhead.
1916///
1917/// # Safety
1918///
1919/// Both slices must have the same length.
1920#[cfg(any(
1921    all(target_arch = "x86_64", target_feature = "sse2"),
1922    all(target_arch = "loongarch64", target_feature = "lsx"),
1923    all(target_arch = "aarch64", target_feature = "neon")
1924))]
1925#[inline]
1926unsafe fn small_slice_eq(x: &[u8], y: &[u8]) -> bool {
1927    debug_assert_eq!(x.len(), y.len());
1928    // This function is adapted from
1929    // https://github.com/BurntSushi/memchr/blob/8037d11b4357b0f07be2bb66dc2659d9cf28ad32/src/memmem/util.rs#L32
1930
1931    // If we don't have enough bytes to do 4-byte at a time loads, then
1932    // fall back to the naive slow version.
1933    //
1934    // Potential alternative: We could do a copy_nonoverlapping combined with a mask instead
1935    // of a loop. Benchmark it.
1936    if x.len() < 4 {
1937        for (&b1, &b2) in x.iter().zip(y) {
1938            if b1 != b2 {
1939                return false;
1940            }
1941        }
1942        return true;
1943    }
1944    // When we have 4 or more bytes to compare, then proceed in chunks of 4 at
1945    // a time using unaligned loads.
1946    //
1947    // Also, why do 4 byte loads instead of, say, 8 byte loads? The reason is
1948    // that this particular version of memcmp is likely to be called with tiny
1949    // needles. That means that if we do 8 byte loads, then a higher proportion
1950    // of memcmp calls will use the slower variant above. With that said, this
1951    // is a hypothesis and is only loosely supported by benchmarks. There's
1952    // likely some improvement that could be made here. The main thing here
1953    // though is to optimize for latency, not throughput.
1954
1955    // SAFETY: Via the conditional above, we know that both `px` and `py`
1956    // have the same length, so `px < pxend` implies that `py < pyend`.
1957    // Thus, dereferencing both `px` and `py` in the loop below is safe.
1958    //
1959    // Moreover, we set `pxend` and `pyend` to be 4 bytes before the actual
1960    // end of `px` and `py`. Thus, the final dereference outside of the
1961    // loop is guaranteed to be valid. (The final comparison will overlap with
1962    // the last comparison done in the loop for lengths that aren't multiples
1963    // of four.)
1964    //
1965    // Finally, we needn't worry about alignment here, since we do unaligned
1966    // loads.
1967    unsafe {
1968        let (mut px, mut py) = (x.as_ptr(), y.as_ptr());
1969        let (pxend, pyend) = (px.add(x.len() - 4), py.add(y.len() - 4));
1970        while px < pxend {
1971            let vx = (px as *const u32).read_unaligned();
1972            let vy = (py as *const u32).read_unaligned();
1973            if vx != vy {
1974                return false;
1975            }
1976            px = px.add(4);
1977            py = py.add(4);
1978        }
1979        let vx = (pxend as *const u32).read_unaligned();
1980        let vy = (pyend as *const u32).read_unaligned();
1981        vx == vy
1982    }
1983}
````