---
title: iter.rs - source
url: https://doc.rust-lang.org/src/core/str/iter.rs.html#1493
source: crawler
fetched_at: 2026-05-06T21:36:53.297329489-03:00
rendered_js: false
word_count: 5910
summary: This document defines the Rust iterator structures for traversing string slices by character and by character indices.
tags:
    - rust
    - iterator
    - string-processing
    - utf-8
    - std-library
category: api
---

## core/str/ iter.rs

````rust
1//! Iterators for `str` methods.
2
3use super::pattern::{DoubleEndedSearcher, Pattern, ReverseSearcher, Searcher};
4use super::validations::{next_code_point, next_code_point_reverse};
5use super::{
6    BytesIsNotEmpty, CharEscapeDebugContinue, CharEscapeDefault, CharEscapeUnicode,
7    IsAsciiWhitespace, IsNotEmpty, IsWhitespace, LinesMap, UnsafeBytesToStr, from_utf8_unchecked,
8};
9use crate::fmt::{self, Write};
10use crate::iter::{
11    Chain, Copied, Filter, FlatMap, Flatten, FusedIterator, Map, TrustedLen, TrustedRandomAccess,
12    TrustedRandomAccessNoCoerce,
13};
14use crate::num::NonZero;
15use crate::ops::Try;
16use crate::slice::{self, Split as SliceSplit};
17use crate::{char as char_mod, option};
18
19/// An iterator over the [`char`]s of a string slice.
20///
21///
22/// This struct is created by the [`chars`] method on [`str`].
23/// See its documentation for more.
24///
25/// [`char`]: prim@char
26/// [`chars`]: str::chars
27#[derive(Clone)]
28#[must_use = "iterators are lazy and do nothing unless consumed"]
29#[stable(feature = "rust1", since = "1.0.0")]
30pub struct Chars<'a> {
31    pub(super) iter: slice::Iter<'a, u8>,
32}
33
34#[stable(feature = "rust1", since = "1.0.0")]
35impl<'a> Iterator for Chars<'a> {
36    type Item = char;
37
38    #[inline]
39    fn next(&mut self) -> Option<char> {
40        // SAFETY: `str` invariant says `self.iter` is a valid UTF-8 string and
41        // the resulting `ch` is a valid Unicode Scalar Value.
42        unsafe { next_code_point(&mut self.iter).map(|ch| char::from_u32_unchecked(ch)) }
43    }
44
45    #[inline]
46    fn count(self) -> usize {
47        super::count::count_chars(self.as_str())
48    }
49
50    #[inline]
51    fn advance_by(&mut self, mut remainder: usize) -> Result<(), NonZero<usize>> {
52        const CHUNK_SIZE: usize = 32;
53
54        if remainder >= CHUNK_SIZE {
55            let mut chunks = self.iter.as_slice().as_chunks::<CHUNK_SIZE>().0.iter();
56            let mut bytes_skipped: usize = 0;
57
58            while remainder > CHUNK_SIZE
59                && let Some(chunk) = chunks.next()
60            {
61                bytes_skipped += CHUNK_SIZE;
62
63                let mut start_bytes = [false; CHUNK_SIZE];
64
65                for i in 0..CHUNK_SIZE {
66                    start_bytes[i] = !super::validations::utf8_is_cont_byte(chunk[i]);
67                }
68
69                remainder -= start_bytes.into_iter().map(|i| i as u8).sum::<u8>() as usize;
70            }
71
72            // SAFETY: The amount of bytes exists since we just iterated over them,
73            // so advance_by will succeed.
74            unsafe { self.iter.advance_by(bytes_skipped).unwrap_unchecked() };
75
76            // skip trailing continuation bytes
77            while self.iter.len() > 0 {
78                let b = self.iter.as_slice()[0];
79                if !super::validations::utf8_is_cont_byte(b) {
80                    break;
81                }
82                // SAFETY: We just peeked at the byte, therefore it exists
83                unsafe { self.iter.advance_by(1).unwrap_unchecked() };
84            }
85        }
86
87        while (remainder > 0) && (self.iter.len() > 0) {
88            remainder -= 1;
89            let b = self.iter.as_slice()[0];
90            let slurp = super::validations::utf8_char_width(b);
91            // SAFETY: utf8 validity requires that the string must contain
92            // the continuation bytes (if any)
93            unsafe { self.iter.advance_by(slurp).unwrap_unchecked() };
94        }
95
96        NonZero::new(remainder).map_or(Ok(()), Err)
97    }
98
99    #[inline]
100    fn size_hint(&self) -> (usize, Option<usize>) {
101        let len = self.iter.len();
102        (len.div_ceil(4), Some(len))
103    }
104
105    #[inline]
106    fn last(mut self) -> Option<char> {
107        // No need to go through the entire string.
108        self.next_back()
109    }
110}
111
112#[stable(feature = "chars_debug_impl", since = "1.38.0")]
113impl fmt::Debug for Chars<'_> {
114    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
115        write!(f, "Chars(")?;
116        f.debug_list().entries(self.clone()).finish()?;
117        write!(f, ")")?;
118        Ok(())
119    }
120}
121
122#[stable(feature = "rust1", since = "1.0.0")]
123impl<'a> DoubleEndedIterator for Chars<'a> {
124    #[inline]
125    fn next_back(&mut self) -> Option<char> {
126        // SAFETY: `str` invariant says `self.iter` is a valid UTF-8 string and
127        // the resulting `ch` is a valid Unicode Scalar Value.
128        unsafe { next_code_point_reverse(&mut self.iter).map(|ch| char::from_u32_unchecked(ch)) }
129    }
130}
131
132#[stable(feature = "fused", since = "1.26.0")]
133impl FusedIterator for Chars<'_> {}
134
135impl<'a> Chars<'a> {
136    /// Views the underlying data as a subslice of the original data.
137    ///
138    /// This has the same lifetime as the original slice, and so the
139    /// iterator can continue to be used while this exists.
140    ///
141    /// # Examples
142    ///
143    /// ```
144    /// let mut chars = "abc".chars();
145    ///
146    /// assert_eq!(chars.as_str(), "abc");
147    /// chars.next();
148    /// assert_eq!(chars.as_str(), "bc");
149    /// chars.next();
150    /// chars.next();
151    /// assert_eq!(chars.as_str(), "");
152    /// ```
153    #[stable(feature = "iter_to_slice", since = "1.4.0")]
154    #[must_use]
155    #[inline]
156    pub fn as_str(&self) -> &'a str {
157        // SAFETY: `Chars` is only made from a str, which guarantees the iter is valid UTF-8.
158        unsafe { from_utf8_unchecked(self.iter.as_slice()) }
159    }
160}
161
162/// An iterator over the [`char`]s of a string slice, and their positions.
163///
164/// This struct is created by the [`char_indices`] method on [`str`].
165/// See its documentation for more.
166///
167/// [`char`]: prim@char
168/// [`char_indices`]: str::char_indices
169#[derive(Clone, Debug)]
170#[must_use = "iterators are lazy and do nothing unless consumed"]
171#[stable(feature = "rust1", since = "1.0.0")]
172pub struct CharIndices<'a> {
173    pub(super) front_offset: usize,
174    pub(super) iter: Chars<'a>,
175}
176
177#[stable(feature = "rust1", since = "1.0.0")]
178impl<'a> Iterator for CharIndices<'a> {
179    type Item = (usize, char);
180
181    #[inline]
182    fn next(&mut self) -> Option<(usize, char)> {
183        let pre_len = self.iter.iter.len();
184        match self.iter.next() {
185            None => None,
186            Some(ch) => {
187                let index = self.front_offset;
188                let len = self.iter.iter.len();
189                self.front_offset += pre_len - len;
190                Some((index, ch))
191            }
192        }
193    }
194
195    #[inline]
196    fn count(self) -> usize {
197        self.iter.count()
198    }
199
200    #[inline]
201    fn size_hint(&self) -> (usize, Option<usize>) {
202        self.iter.size_hint()
203    }
204
205    #[inline]
206    fn last(mut self) -> Option<(usize, char)> {
207        // No need to go through the entire string.
208        self.next_back()
209    }
210}
211
212#[stable(feature = "rust1", since = "1.0.0")]
213impl<'a> DoubleEndedIterator for CharIndices<'a> {
214    #[inline]
215    fn next_back(&mut self) -> Option<(usize, char)> {
216        self.iter.next_back().map(|ch| {
217            let index = self.front_offset + self.iter.iter.len();
218            (index, ch)
219        })
220    }
221}
222
223#[stable(feature = "fused", since = "1.26.0")]
224impl FusedIterator for CharIndices<'_> {}
225
226impl<'a> CharIndices<'a> {
227    /// Views the underlying data as a subslice of the original data.
228    ///
229    /// This has the same lifetime as the original slice, and so the
230    /// iterator can continue to be used while this exists.
231    #[stable(feature = "iter_to_slice", since = "1.4.0")]
232    #[must_use]
233    #[inline]
234    pub fn as_str(&self) -> &'a str {
235        self.iter.as_str()
236    }
237
238    /// Returns the byte position of the next character, or the length
239    /// of the underlying string if there are no more characters.
240    ///
241    /// This means that, when the iterator has not been fully consumed,
242    /// the returned value will match the index that will be returned
243    /// by the next call to [`next()`](Self::next).
244    ///
245    /// # Examples
246    ///
247    /// ```
248    /// let mut chars = "a楽".char_indices();
249    ///
250    /// // `next()` has not been called yet, so `offset()` returns the byte
251    /// // index of the first character of the string, which is always 0.
252    /// assert_eq!(chars.offset(), 0);
253    /// // As expected, the first call to `next()` also returns 0 as index.
254    /// assert_eq!(chars.next(), Some((0, 'a')));
255    ///
256    /// // `next()` has been called once, so `offset()` returns the byte index
257    /// // of the second character ...
258    /// assert_eq!(chars.offset(), 1);
259    /// // ... which matches the index returned by the next call to `next()`.
260    /// assert_eq!(chars.next(), Some((1, '楽')));
261    ///
262    /// // Once the iterator has been consumed, `offset()` returns the length
263    /// // in bytes of the string.
264    /// assert_eq!(chars.offset(), 4);
265    /// assert_eq!(chars.next(), None);
266    /// ```
267    #[inline]
268    #[must_use]
269    #[stable(feature = "char_indices_offset", since = "1.82.0")]
270    pub fn offset(&self) -> usize {
271        self.front_offset
272    }
273}
274
275/// An iterator over the bytes of a string slice.
276///
277/// This struct is created by the [`bytes`] method on [`str`].
278/// See its documentation for more.
279///
280/// [`bytes`]: str::bytes
281#[must_use = "iterators are lazy and do nothing unless consumed"]
282#[stable(feature = "rust1", since = "1.0.0")]
283#[derive(Clone, Debug)]
284pub struct Bytes<'a>(pub(super) Copied<slice::Iter<'a, u8>>);
285
286#[stable(feature = "rust1", since = "1.0.0")]
287impl Iterator for Bytes<'_> {
288    type Item = u8;
289
290    #[inline]
291    fn next(&mut self) -> Option<u8> {
292        self.0.next()
293    }
294
295    #[inline]
296    fn size_hint(&self) -> (usize, Option<usize>) {
297        self.0.size_hint()
298    }
299
300    #[inline]
301    fn count(self) -> usize {
302        self.0.count()
303    }
304
305    #[inline]
306    fn last(self) -> Option<Self::Item> {
307        self.0.last()
308    }
309
310    #[inline]
311    fn nth(&mut self, n: usize) -> Option<Self::Item> {
312        self.0.nth(n)
313    }
314
315    #[inline]
316    fn all<F>(&mut self, f: F) -> bool
317    where
318        F: FnMut(Self::Item) -> bool,
319    {
320        self.0.all(f)
321    }
322
323    #[inline]
324    fn any<F>(&mut self, f: F) -> bool
325    where
326        F: FnMut(Self::Item) -> bool,
327    {
328        self.0.any(f)
329    }
330
331    #[inline]
332    fn find<P>(&mut self, predicate: P) -> Option<Self::Item>
333    where
334        P: FnMut(&Self::Item) -> bool,
335    {
336        self.0.find(predicate)
337    }
338
339    #[inline]
340    fn position<P>(&mut self, predicate: P) -> Option<usize>
341    where
342        P: FnMut(Self::Item) -> bool,
343    {
344        self.0.position(predicate)
345    }
346
347    #[inline]
348    fn rposition<P>(&mut self, predicate: P) -> Option<usize>
349    where
350        P: FnMut(Self::Item) -> bool,
351    {
352        self.0.rposition(predicate)
353    }
354
355    #[inline]
356    unsafe fn __iterator_get_unchecked(&mut self, idx: usize) -> u8 {
357        // SAFETY: the caller must uphold the safety contract
358        // for `Iterator::__iterator_get_unchecked`.
359        unsafe { self.0.__iterator_get_unchecked(idx) }
360    }
361}
362
363#[stable(feature = "rust1", since = "1.0.0")]
364impl DoubleEndedIterator for Bytes<'_> {
365    #[inline]
366    fn next_back(&mut self) -> Option<u8> {
367        self.0.next_back()
368    }
369
370    #[inline]
371    fn nth_back(&mut self, n: usize) -> Option<Self::Item> {
372        self.0.nth_back(n)
373    }
374
375    #[inline]
376    fn rfind<P>(&mut self, predicate: P) -> Option<Self::Item>
377    where
378        P: FnMut(&Self::Item) -> bool,
379    {
380        self.0.rfind(predicate)
381    }
382}
383
384#[stable(feature = "rust1", since = "1.0.0")]
385impl ExactSizeIterator for Bytes<'_> {
386    #[inline]
387    fn len(&self) -> usize {
388        self.0.len()
389    }
390
391    #[inline]
392    fn is_empty(&self) -> bool {
393        self.0.is_empty()
394    }
395}
396
397#[stable(feature = "fused", since = "1.26.0")]
398impl FusedIterator for Bytes<'_> {}
399
400#[unstable(feature = "trusted_len", issue = "37572")]
401unsafe impl TrustedLen for Bytes<'_> {}
402
403#[doc(hidden)]
404#[unstable(feature = "trusted_random_access", issue = "none")]
405unsafe impl TrustedRandomAccess for Bytes<'_> {}
406
407#[doc(hidden)]
408#[unstable(feature = "trusted_random_access", issue = "none")]
409unsafe impl TrustedRandomAccessNoCoerce for Bytes<'_> {
410    const MAY_HAVE_SIDE_EFFECT: bool = false;
411}
412
413/// This macro generates a Clone impl for string pattern API
414/// wrapper types of the form X<'a, P>
415macro_rules! derive_pattern_clone {
416    (clone $t:ident with |$s:ident| $e:expr) => {
417        impl<'a, P> Clone for $t<'a, P>
418        where
419            P: Pattern<Searcher<'a>: Clone>,
420        {
421            fn clone(&self) -> Self {
422                let $s = self;
423                $e
424            }
425        }
426    };
427}
428
429/// This macro generates two public iterator structs
430/// wrapping a private internal one that makes use of the `Pattern` API.
431///
432/// For all patterns `P: Pattern` the following items will be
433/// generated (generics omitted):
434///
435/// struct $forward_iterator($internal_iterator);
436/// struct $reverse_iterator($internal_iterator);
437///
438/// impl Iterator for $forward_iterator
439/// { /* internal ends up calling Searcher::next_match() */ }
440///
441/// impl DoubleEndedIterator for $forward_iterator
442///       where P::Searcher: DoubleEndedSearcher
443/// { /* internal ends up calling Searcher::next_match_back() */ }
444///
445/// impl Iterator for $reverse_iterator
446///       where P::Searcher: ReverseSearcher
447/// { /* internal ends up calling Searcher::next_match_back() */ }
448///
449/// impl DoubleEndedIterator for $reverse_iterator
450///       where P::Searcher: DoubleEndedSearcher
451/// { /* internal ends up calling Searcher::next_match() */ }
452///
453/// The internal one is defined outside the macro, and has almost the same
454/// semantic as a DoubleEndedIterator by delegating to `pattern::Searcher` and
455/// `pattern::ReverseSearcher` for both forward and reverse iteration.
456///
457/// "Almost", because a `Searcher` and a `ReverseSearcher` for a given
458/// `Pattern` might not return the same elements, so actually implementing
459/// `DoubleEndedIterator` for it would be incorrect.
460/// (See the docs in `str::pattern` for more details)
461///
462/// However, the internal struct still represents a single ended iterator from
463/// either end, and depending on pattern is also a valid double ended iterator,
464/// so the two wrapper structs implement `Iterator`
465/// and `DoubleEndedIterator` depending on the concrete pattern type, leading
466/// to the complex impls seen above.
467macro_rules! generate_pattern_iterators {
468    {
469        // Forward iterator
470        forward:
471            $(#[$forward_iterator_attribute:meta])*
472            struct $forward_iterator:ident;
473
474        // Reverse iterator
475        reverse:
476            $(#[$reverse_iterator_attribute:meta])*
477            struct $reverse_iterator:ident;
478
479        // Stability of all generated items
480        stability:
481            $(#[$common_stability_attribute:meta])*
482
483        // Internal almost-iterator that is being delegated to
484        internal:
485            $internal_iterator:ident yielding ($iterty:ty);
486
487        // Kind of delegation - either single ended or double ended
488        delegate $($t:tt)*
489    } => {
490        $(#[$forward_iterator_attribute])*
491        $(#[$common_stability_attribute])*
492        pub struct $forward_iterator<'a, P: Pattern>(pub(super) $internal_iterator<'a, P>);
493
494        $(#[$common_stability_attribute])*
495        impl<'a, P> fmt::Debug for $forward_iterator<'a, P>
496        where
497            P: Pattern<Searcher<'a>: fmt::Debug>,
498        {
499            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
500                f.debug_tuple(stringify!($forward_iterator))
501                    .field(&self.0)
502                    .finish()
503            }
504        }
505
506        $(#[$common_stability_attribute])*
507        impl<'a, P: Pattern> Iterator for $forward_iterator<'a, P> {
508            type Item = $iterty;
509
510            #[inline]
511            fn next(&mut self) -> Option<$iterty> {
512                self.0.next()
513            }
514        }
515
516        $(#[$common_stability_attribute])*
517        impl<'a, P> Clone for $forward_iterator<'a, P>
518        where
519            P: Pattern<Searcher<'a>: Clone>,
520        {
521            fn clone(&self) -> Self {
522                $forward_iterator(self.0.clone())
523            }
524        }
525
526        $(#[$reverse_iterator_attribute])*
527        $(#[$common_stability_attribute])*
528        pub struct $reverse_iterator<'a, P: Pattern>(pub(super) $internal_iterator<'a, P>);
529
530        $(#[$common_stability_attribute])*
531        impl<'a, P> fmt::Debug for $reverse_iterator<'a, P>
532        where
533            P: Pattern<Searcher<'a>: fmt::Debug>,
534        {
535            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
536                f.debug_tuple(stringify!($reverse_iterator))
537                    .field(&self.0)
538                    .finish()
539            }
540        }
541
542        $(#[$common_stability_attribute])*
543        impl<'a, P> Iterator for $reverse_iterator<'a, P>
544        where
545            P: Pattern<Searcher<'a>: ReverseSearcher<'a>>,
546        {
547            type Item = $iterty;
548
549            #[inline]
550            fn next(&mut self) -> Option<$iterty> {
551                self.0.next_back()
552            }
553        }
554
555        $(#[$common_stability_attribute])*
556        impl<'a, P> Clone for $reverse_iterator<'a, P>
557        where
558            P: Pattern<Searcher<'a>: Clone>,
559        {
560            fn clone(&self) -> Self {
561                $reverse_iterator(self.0.clone())
562            }
563        }
564
565        #[stable(feature = "fused", since = "1.26.0")]
566        impl<'a, P: Pattern> FusedIterator for $forward_iterator<'a, P> {}
567
568        #[stable(feature = "fused", since = "1.26.0")]
569        impl<'a, P> FusedIterator for $reverse_iterator<'a, P>
570        where
571            P: Pattern<Searcher<'a>: ReverseSearcher<'a>>,
572        {}
573
574        generate_pattern_iterators!($($t)* with $(#[$common_stability_attribute])*,
575                                                $forward_iterator,
576                                                $reverse_iterator, $iterty);
577    };
578    {
579        double ended; with $(#[$common_stability_attribute:meta])*,
580                           $forward_iterator:ident,
581                           $reverse_iterator:ident, $iterty:ty
582    } => {
583        $(#[$common_stability_attribute])*
584        impl<'a, P> DoubleEndedIterator for $forward_iterator<'a, P>
585        where
586            P: Pattern<Searcher<'a>: DoubleEndedSearcher<'a>>,
587        {
588            #[inline]
589            fn next_back(&mut self) -> Option<$iterty> {
590                self.0.next_back()
591            }
592        }
593
594        $(#[$common_stability_attribute])*
595        impl<'a, P> DoubleEndedIterator for $reverse_iterator<'a, P>
596        where
597            P: Pattern<Searcher<'a>: DoubleEndedSearcher<'a>>,
598        {
599            #[inline]
600            fn next_back(&mut self) -> Option<$iterty> {
601                self.0.next()
602            }
603        }
604    };
605    {
606        single ended; with $(#[$common_stability_attribute:meta])*,
607                           $forward_iterator:ident,
608                           $reverse_iterator:ident, $iterty:ty
609    } => {}
610}
611
612derive_pattern_clone! {
613    clone SplitInternal
614    with |s| SplitInternal { matcher: s.matcher.clone(), ..*s }
615}
616
617pub(super) struct SplitInternal<'a, P: Pattern> {
618    pub(super) start: usize,
619    pub(super) end: usize,
620    pub(super) matcher: P::Searcher<'a>,
621    pub(super) allow_trailing_empty: bool,
622    pub(super) finished: bool,
623}
624
625impl<'a, P> fmt::Debug for SplitInternal<'a, P>
626where
627    P: Pattern<Searcher<'a>: fmt::Debug>,
628{
629    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
630        f.debug_struct("SplitInternal")
631            .field("start", &self.start)
632            .field("end", &self.end)
633            .field("matcher", &self.matcher)
634            .field("allow_trailing_empty", &self.allow_trailing_empty)
635            .field("finished", &self.finished)
636            .finish()
637    }
638}
639
640impl<'a, P: Pattern> SplitInternal<'a, P> {
641    #[inline]
642    fn get_end(&mut self) -> Option<&'a str> {
643        if !self.finished {
644            self.finished = true;
645
646            if self.allow_trailing_empty || self.end - self.start > 0 {
647                // SAFETY: `self.start` and `self.end` always lie on unicode boundaries.
648                let string = unsafe { self.matcher.haystack().get_unchecked(self.start..self.end) };
649                return Some(string);
650            }
651        }
652
653        None
654    }
655
656    #[inline]
657    fn next(&mut self) -> Option<&'a str> {
658        if self.finished {
659            return None;
660        }
661
662        let haystack = self.matcher.haystack();
663        match self.matcher.next_match() {
664            // SAFETY: `Searcher` guarantees that `a` and `b` lie on unicode boundaries.
665            Some((a, b)) => unsafe {
666                let elt = haystack.get_unchecked(self.start..a);
667                self.start = b;
668                Some(elt)
669            },
670            None => self.get_end(),
671        }
672    }
673
674    #[inline]
675    fn next_inclusive(&mut self) -> Option<&'a str> {
676        if self.finished {
677            return None;
678        }
679
680        let haystack = self.matcher.haystack();
681        match self.matcher.next_match() {
682            // SAFETY: `Searcher` guarantees that `b` lies on unicode boundary,
683            // and self.start is either the start of the original string,
684            // or `b` was assigned to it, so it also lies on unicode boundary.
685            Some((_, b)) => unsafe {
686                let elt = haystack.get_unchecked(self.start..b);
687                self.start = b;
688                Some(elt)
689            },
690            None => self.get_end(),
691        }
692    }
693
694    #[inline]
695    fn next_back(&mut self) -> Option<&'a str>
696    where
697        P::Searcher<'a>: ReverseSearcher<'a>,
698    {
699        if self.finished {
700            return None;
701        }
702
703        if !self.allow_trailing_empty {
704            self.allow_trailing_empty = true;
705            match self.next_back() {
706                Some(elt) if !elt.is_empty() => return Some(elt),
707                _ => {
708                    if self.finished {
709                        return None;
710                    }
711                }
712            }
713        }
714
715        let haystack = self.matcher.haystack();
716        match self.matcher.next_match_back() {
717            // SAFETY: `Searcher` guarantees that `a` and `b` lie on unicode boundaries.
718            Some((a, b)) => unsafe {
719                let elt = haystack.get_unchecked(b..self.end);
720                self.end = a;
721                Some(elt)
722            },
723            // SAFETY: `self.start` and `self.end` always lie on unicode boundaries.
724            None => unsafe {
725                self.finished = true;
726                Some(haystack.get_unchecked(self.start..self.end))
727            },
728        }
729    }
730
731    #[inline]
732    fn next_back_inclusive(&mut self) -> Option<&'a str>
733    where
734        P::Searcher<'a>: ReverseSearcher<'a>,
735    {
736        if self.finished {
737            return None;
738        }
739
740        if !self.allow_trailing_empty {
741            self.allow_trailing_empty = true;
742            match self.next_back_inclusive() {
743                Some(elt) if !elt.is_empty() => return Some(elt),
744                _ => {
745                    if self.finished {
746                        return None;
747                    }
748                }
749            }
750        }
751
752        let haystack = self.matcher.haystack();
753        match self.matcher.next_match_back() {
754            // SAFETY: `Searcher` guarantees that `b` lies on unicode boundary,
755            // and self.end is either the end of the original string,
756            // or `b` was assigned to it, so it also lies on unicode boundary.
757            Some((_, b)) => unsafe {
758                let elt = haystack.get_unchecked(b..self.end);
759                self.end = b;
760                Some(elt)
761            },
762            // SAFETY: self.start is either the start of the original string,
763            // or start of a substring that represents the part of the string that hasn't
764            // iterated yet. Either way, it is guaranteed to lie on unicode boundary.
765            // self.end is either the end of the original string,
766            // or `b` was assigned to it, so it also lies on unicode boundary.
767            None => unsafe {
768                self.finished = true;
769                Some(haystack.get_unchecked(self.start..self.end))
770            },
771        }
772    }
773
774    #[inline]
775    fn remainder(&self) -> Option<&'a str> {
776        // `Self::get_end` doesn't change `self.start`
777        if self.finished {
778            return None;
779        }
780
781        // SAFETY: `self.start` and `self.end` always lie on unicode boundaries.
782        Some(unsafe { self.matcher.haystack().get_unchecked(self.start..self.end) })
783    }
784}
785
786generate_pattern_iterators! {
787    forward:
788        /// Created with the method [`split`].
789        ///
790        /// [`split`]: str::split
791        struct Split;
792    reverse:
793        /// Created with the method [`rsplit`].
794        ///
795        /// [`rsplit`]: str::rsplit
796        struct RSplit;
797    stability:
798        #[stable(feature = "rust1", since = "1.0.0")]
799    internal:
800        SplitInternal yielding (&'a str);
801    delegate double ended;
802}
803
804impl<'a, P: Pattern> Split<'a, P> {
805    /// Returns remainder of the split string.
806    ///
807    /// If the iterator is empty, returns `None`.
808    ///
809    /// # Examples
810    ///
811    /// ```
812    /// #![feature(str_split_remainder)]
813    /// let mut split = "Mary had a little lamb".split(' ');
814    /// assert_eq!(split.remainder(), Some("Mary had a little lamb"));
815    /// split.next();
816    /// assert_eq!(split.remainder(), Some("had a little lamb"));
817    /// split.by_ref().for_each(drop);
818    /// assert_eq!(split.remainder(), None);
819    /// ```
820    #[inline]
821    #[unstable(feature = "str_split_remainder", issue = "77998")]
822    pub fn remainder(&self) -> Option<&'a str> {
823        self.0.remainder()
824    }
825}
826
827impl<'a, P: Pattern> RSplit<'a, P> {
828    /// Returns remainder of the split string.
829    ///
830    /// If the iterator is empty, returns `None`.
831    ///
832    /// # Examples
833    ///
834    /// ```
835    /// #![feature(str_split_remainder)]
836    /// let mut split = "Mary had a little lamb".rsplit(' ');
837    /// assert_eq!(split.remainder(), Some("Mary had a little lamb"));
838    /// split.next();
839    /// assert_eq!(split.remainder(), Some("Mary had a little"));
840    /// split.by_ref().for_each(drop);
841    /// assert_eq!(split.remainder(), None);
842    /// ```
843    #[inline]
844    #[unstable(feature = "str_split_remainder", issue = "77998")]
845    pub fn remainder(&self) -> Option<&'a str> {
846        self.0.remainder()
847    }
848}
849
850generate_pattern_iterators! {
851    forward:
852        /// Created with the method [`split_terminator`].
853        ///
854        /// [`split_terminator`]: str::split_terminator
855        struct SplitTerminator;
856    reverse:
857        /// Created with the method [`rsplit_terminator`].
858        ///
859        /// [`rsplit_terminator`]: str::rsplit_terminator
860        struct RSplitTerminator;
861    stability:
862        #[stable(feature = "rust1", since = "1.0.0")]
863    internal:
864        SplitInternal yielding (&'a str);
865    delegate double ended;
866}
867
868impl<'a, P: Pattern> SplitTerminator<'a, P> {
869    /// Returns remainder of the split string.
870    ///
871    /// If the iterator is empty, returns `None`.
872    ///
873    /// # Examples
874    ///
875    /// ```
876    /// #![feature(str_split_remainder)]
877    /// let mut split = "A..B..".split_terminator('.');
878    /// assert_eq!(split.remainder(), Some("A..B.."));
879    /// split.next();
880    /// assert_eq!(split.remainder(), Some(".B.."));
881    /// split.by_ref().for_each(drop);
882    /// assert_eq!(split.remainder(), None);
883    /// ```
884    #[inline]
885    #[unstable(feature = "str_split_remainder", issue = "77998")]
886    pub fn remainder(&self) -> Option<&'a str> {
887        self.0.remainder()
888    }
889}
890
891impl<'a, P: Pattern> RSplitTerminator<'a, P> {
892    /// Returns remainder of the split string.
893    ///
894    /// If the iterator is empty, returns `None`.
895    ///
896    /// # Examples
897    ///
898    /// ```
899    /// #![feature(str_split_remainder)]
900    /// let mut split = "A..B..".rsplit_terminator('.');
901    /// assert_eq!(split.remainder(), Some("A..B.."));
902    /// split.next();
903    /// assert_eq!(split.remainder(), Some("A..B"));
904    /// split.by_ref().for_each(drop);
905    /// assert_eq!(split.remainder(), None);
906    /// ```
907    #[inline]
908    #[unstable(feature = "str_split_remainder", issue = "77998")]
909    pub fn remainder(&self) -> Option<&'a str> {
910        self.0.remainder()
911    }
912}
913
914derive_pattern_clone! {
915    clone SplitNInternal
916    with |s| SplitNInternal { iter: s.iter.clone(), ..*s }
917}
918
919pub(super) struct SplitNInternal<'a, P: Pattern> {
920    pub(super) iter: SplitInternal<'a, P>,
921    /// The number of splits remaining
922    pub(super) count: usize,
923}
924
925impl<'a, P> fmt::Debug for SplitNInternal<'a, P>
926where
927    P: Pattern<Searcher<'a>: fmt::Debug>,
928{
929    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
930        f.debug_struct("SplitNInternal")
931            .field("iter", &self.iter)
932            .field("count", &self.count)
933            .finish()
934    }
935}
936
937impl<'a, P: Pattern> SplitNInternal<'a, P> {
938    #[inline]
939    fn next(&mut self) -> Option<&'a str> {
940        match self.count {
941            0 => None,
942            1 => {
943                self.count = 0;
944                self.iter.get_end()
945            }
946            _ => {
947                self.count -= 1;
948                self.iter.next()
949            }
950        }
951    }
952
953    #[inline]
954    fn next_back(&mut self) -> Option<&'a str>
955    where
956        P::Searcher<'a>: ReverseSearcher<'a>,
957    {
958        match self.count {
959            0 => None,
960            1 => {
961                self.count = 0;
962                self.iter.get_end()
963            }
964            _ => {
965                self.count -= 1;
966                self.iter.next_back()
967            }
968        }
969    }
970
971    #[inline]
972    fn remainder(&self) -> Option<&'a str> {
973        self.iter.remainder()
974    }
975}
976
977generate_pattern_iterators! {
978    forward:
979        /// Created with the method [`splitn`].
980        ///
981        /// [`splitn`]: str::splitn
982        struct SplitN;
983    reverse:
984        /// Created with the method [`rsplitn`].
985        ///
986        /// [`rsplitn`]: str::rsplitn
987        struct RSplitN;
988    stability:
989        #[stable(feature = "rust1", since = "1.0.0")]
990    internal:
991        SplitNInternal yielding (&'a str);
992    delegate single ended;
993}
994
995impl<'a, P: Pattern> SplitN<'a, P> {
996    /// Returns remainder of the split string.
997    ///
998    /// If the iterator is empty, returns `None`.
999    ///
1000    /// # Examples
1001    ///
1002    /// ```
1003    /// #![feature(str_split_remainder)]
1004    /// let mut split = "Mary had a little lamb".splitn(3, ' ');
1005    /// assert_eq!(split.remainder(), Some("Mary had a little lamb"));
1006    /// split.next();
1007    /// assert_eq!(split.remainder(), Some("had a little lamb"));
1008    /// split.by_ref().for_each(drop);
1009    /// assert_eq!(split.remainder(), None);
1010    /// ```
1011    #[inline]
1012    #[unstable(feature = "str_split_remainder", issue = "77998")]
1013    pub fn remainder(&self) -> Option<&'a str> {
1014        self.0.remainder()
1015    }
1016}
1017
1018impl<'a, P: Pattern> RSplitN<'a, P> {
1019    /// Returns remainder of the split string.
1020    ///
1021    /// If the iterator is empty, returns `None`.
1022    ///
1023    /// # Examples
1024    ///
1025    /// ```
1026    /// #![feature(str_split_remainder)]
1027    /// let mut split = "Mary had a little lamb".rsplitn(3, ' ');
1028    /// assert_eq!(split.remainder(), Some("Mary had a little lamb"));
1029    /// split.next();
1030    /// assert_eq!(split.remainder(), Some("Mary had a little"));
1031    /// split.by_ref().for_each(drop);
1032    /// assert_eq!(split.remainder(), None);
1033    /// ```
1034    #[inline]
1035    #[unstable(feature = "str_split_remainder", issue = "77998")]
1036    pub fn remainder(&self) -> Option<&'a str> {
1037        self.0.remainder()
1038    }
1039}
1040
1041derive_pattern_clone! {
1042    clone MatchIndicesInternal
1043    with |s| MatchIndicesInternal(s.0.clone())
1044}
1045
1046pub(super) struct MatchIndicesInternal<'a, P: Pattern>(pub(super) P::Searcher<'a>);
1047
1048impl<'a, P> fmt::Debug for MatchIndicesInternal<'a, P>
1049where
1050    P: Pattern<Searcher<'a>: fmt::Debug>,
1051{
1052    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1053        f.debug_tuple("MatchIndicesInternal").field(&self.0).finish()
1054    }
1055}
1056
1057impl<'a, P: Pattern> MatchIndicesInternal<'a, P> {
1058    #[inline]
1059    fn next(&mut self) -> Option<(usize, &'a str)> {
1060        self.0
1061            .next_match()
1062            // SAFETY: `Searcher` guarantees that `start` and `end` lie on unicode boundaries.
1063            .map(|(start, end)| unsafe { (start, self.0.haystack().get_unchecked(start..end)) })
1064    }
1065
1066    #[inline]
1067    fn next_back(&mut self) -> Option<(usize, &'a str)>
1068    where
1069        P::Searcher<'a>: ReverseSearcher<'a>,
1070    {
1071        self.0
1072            .next_match_back()
1073            // SAFETY: `Searcher` guarantees that `start` and `end` lie on unicode boundaries.
1074            .map(|(start, end)| unsafe { (start, self.0.haystack().get_unchecked(start..end)) })
1075    }
1076}
1077
1078generate_pattern_iterators! {
1079    forward:
1080        /// Created with the method [`match_indices`].
1081        ///
1082        /// [`match_indices`]: str::match_indices
1083        struct MatchIndices;
1084    reverse:
1085        /// Created with the method [`rmatch_indices`].
1086        ///
1087        /// [`rmatch_indices`]: str::rmatch_indices
1088        struct RMatchIndices;
1089    stability:
1090        #[stable(feature = "str_match_indices", since = "1.5.0")]
1091    internal:
1092        MatchIndicesInternal yielding ((usize, &'a str));
1093    delegate double ended;
1094}
1095
1096derive_pattern_clone! {
1097    clone MatchesInternal
1098    with |s| MatchesInternal(s.0.clone())
1099}
1100
1101pub(super) struct MatchesInternal<'a, P: Pattern>(pub(super) P::Searcher<'a>);
1102
1103impl<'a, P> fmt::Debug for MatchesInternal<'a, P>
1104where
1105    P: Pattern<Searcher<'a>: fmt::Debug>,
1106{
1107    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1108        f.debug_tuple("MatchesInternal").field(&self.0).finish()
1109    }
1110}
1111
1112impl<'a, P: Pattern> MatchesInternal<'a, P> {
1113    #[inline]
1114    fn next(&mut self) -> Option<&'a str> {
1115        // SAFETY: `Searcher` guarantees that `start` and `end` lie on unicode boundaries.
1116        self.0.next_match().map(|(a, b)| unsafe {
1117            // Indices are known to be on utf8 boundaries
1118            self.0.haystack().get_unchecked(a..b)
1119        })
1120    }
1121
1122    #[inline]
1123    fn next_back(&mut self) -> Option<&'a str>
1124    where
1125        P::Searcher<'a>: ReverseSearcher<'a>,
1126    {
1127        // SAFETY: `Searcher` guarantees that `start` and `end` lie on unicode boundaries.
1128        self.0.next_match_back().map(|(a, b)| unsafe {
1129            // Indices are known to be on utf8 boundaries
1130            self.0.haystack().get_unchecked(a..b)
1131        })
1132    }
1133}
1134
1135generate_pattern_iterators! {
1136    forward:
1137        /// Created with the method [`matches`].
1138        ///
1139        /// [`matches`]: str::matches
1140        struct Matches;
1141    reverse:
1142        /// Created with the method [`rmatches`].
1143        ///
1144        /// [`rmatches`]: str::rmatches
1145        struct RMatches;
1146    stability:
1147        #[stable(feature = "str_matches", since = "1.2.0")]
1148    internal:
1149        MatchesInternal yielding (&'a str);
1150    delegate double ended;
1151}
1152
1153/// An iterator over the lines of a string, as string slices.
1154///
1155/// This struct is created with the [`lines`] method on [`str`].
1156/// See its documentation for more.
1157///
1158/// [`lines`]: str::lines
1159#[stable(feature = "rust1", since = "1.0.0")]
1160#[must_use = "iterators are lazy and do nothing unless consumed"]
1161#[derive(Clone, Debug)]
1162pub struct Lines<'a>(pub(super) Map<SplitInclusive<'a, char>, LinesMap>);
1163
1164#[stable(feature = "rust1", since = "1.0.0")]
1165impl<'a> Iterator for Lines<'a> {
1166    type Item = &'a str;
1167
1168    #[inline]
1169    fn next(&mut self) -> Option<&'a str> {
1170        self.0.next()
1171    }
1172
1173    #[inline]
1174    fn size_hint(&self) -> (usize, Option<usize>) {
1175        self.0.size_hint()
1176    }
1177
1178    #[inline]
1179    fn last(mut self) -> Option<&'a str> {
1180        self.next_back()
1181    }
1182}
1183
1184#[stable(feature = "rust1", since = "1.0.0")]
1185impl<'a> DoubleEndedIterator for Lines<'a> {
1186    #[inline]
1187    fn next_back(&mut self) -> Option<&'a str> {
1188        self.0.next_back()
1189    }
1190}
1191
1192#[stable(feature = "fused", since = "1.26.0")]
1193impl FusedIterator for Lines<'_> {}
1194
1195impl<'a> Lines<'a> {
1196    /// Returns the remaining lines of the split string.
1197    ///
1198    /// # Examples
1199    ///
1200    /// ```
1201    /// #![feature(str_lines_remainder)]
1202    ///
1203    /// let mut lines = "a\nb\nc\nd".lines();
1204    /// assert_eq!(lines.remainder(), Some("a\nb\nc\nd"));
1205    ///
1206    /// lines.next();
1207    /// assert_eq!(lines.remainder(), Some("b\nc\nd"));
1208    ///
1209    /// lines.by_ref().for_each(drop);
1210    /// assert_eq!(lines.remainder(), None);
1211    /// ```
1212    #[inline]
1213    #[must_use]
1214    #[unstable(feature = "str_lines_remainder", issue = "77998")]
1215    pub fn remainder(&self) -> Option<&'a str> {
1216        self.0.iter.remainder()
1217    }
1218}
1219
1220/// Created with the method [`lines_any`].
1221///
1222/// [`lines_any`]: str::lines_any
1223#[stable(feature = "rust1", since = "1.0.0")]
1224#[deprecated(since = "1.4.0", note = "use lines()/Lines instead now")]
1225#[must_use = "iterators are lazy and do nothing unless consumed"]
1226#[derive(Clone, Debug)]
1227#[allow(deprecated)]
1228pub struct LinesAny<'a>(pub(super) Lines<'a>);
1229
1230#[stable(feature = "rust1", since = "1.0.0")]
1231#[allow(deprecated)]
1232impl<'a> Iterator for LinesAny<'a> {
1233    type Item = &'a str;
1234
1235    #[inline]
1236    fn next(&mut self) -> Option<&'a str> {
1237        self.0.next()
1238    }
1239
1240    #[inline]
1241    fn size_hint(&self) -> (usize, Option<usize>) {
1242        self.0.size_hint()
1243    }
1244}
1245
1246#[stable(feature = "rust1", since = "1.0.0")]
1247#[allow(deprecated)]
1248impl<'a> DoubleEndedIterator for LinesAny<'a> {
1249    #[inline]
1250    fn next_back(&mut self) -> Option<&'a str> {
1251        self.0.next_back()
1252    }
1253}
1254
1255#[stable(feature = "fused", since = "1.26.0")]
1256#[allow(deprecated)]
1257impl FusedIterator for LinesAny<'_> {}
1258
1259/// An iterator over the non-whitespace substrings of a string,
1260/// separated by any amount of whitespace.
1261///
1262/// This struct is created by the [`split_whitespace`] method on [`str`].
1263/// See its documentation for more.
1264///
1265/// [`split_whitespace`]: str::split_whitespace
1266#[stable(feature = "split_whitespace", since = "1.1.0")]
1267#[derive(Clone, Debug)]
1268pub struct SplitWhitespace<'a> {
1269    pub(super) inner: Filter<Split<'a, IsWhitespace>, IsNotEmpty>,
1270}
1271
1272/// An iterator over the non-ASCII-whitespace substrings of a string,
1273/// separated by any amount of ASCII whitespace.
1274///
1275/// This struct is created by the [`split_ascii_whitespace`] method on [`str`].
1276/// See its documentation for more.
1277///
1278/// [`split_ascii_whitespace`]: str::split_ascii_whitespace
1279#[stable(feature = "split_ascii_whitespace", since = "1.34.0")]
1280#[derive(Clone, Debug)]
1281pub struct SplitAsciiWhitespace<'a> {
1282    pub(super) inner:
1283        Map<Filter<SliceSplit<'a, u8, IsAsciiWhitespace>, BytesIsNotEmpty>, UnsafeBytesToStr>,
1284}
1285
1286/// An iterator over the substrings of a string,
1287/// terminated by a substring matching to a predicate function
1288/// Unlike `Split`, it contains the matched part as a terminator
1289/// of the subslice.
1290///
1291/// This struct is created by the [`split_inclusive`] method on [`str`].
1292/// See its documentation for more.
1293///
1294/// [`split_inclusive`]: str::split_inclusive
1295#[stable(feature = "split_inclusive", since = "1.51.0")]
1296pub struct SplitInclusive<'a, P: Pattern>(pub(super) SplitInternal<'a, P>);
1297
1298#[stable(feature = "split_whitespace", since = "1.1.0")]
1299impl<'a> Iterator for SplitWhitespace<'a> {
1300    type Item = &'a str;
1301
1302    #[inline]
1303    fn next(&mut self) -> Option<&'a str> {
1304        self.inner.next()
1305    }
1306
1307    #[inline]
1308    fn size_hint(&self) -> (usize, Option<usize>) {
1309        self.inner.size_hint()
1310    }
1311
1312    #[inline]
1313    fn last(mut self) -> Option<&'a str> {
1314        self.next_back()
1315    }
1316}
1317
1318#[stable(feature = "split_whitespace", since = "1.1.0")]
1319impl<'a> DoubleEndedIterator for SplitWhitespace<'a> {
1320    #[inline]
1321    fn next_back(&mut self) -> Option<&'a str> {
1322        self.inner.next_back()
1323    }
1324}
1325
1326#[stable(feature = "fused", since = "1.26.0")]
1327impl FusedIterator for SplitWhitespace<'_> {}
1328
1329impl<'a> SplitWhitespace<'a> {
1330    /// Returns remainder of the split string
1331    ///
1332    /// # Examples
1333    ///
1334    /// ```
1335    /// #![feature(str_split_whitespace_remainder)]
1336    ///
1337    /// let mut split = "Mary had a little lamb".split_whitespace();
1338    /// assert_eq!(split.remainder(), Some("Mary had a little lamb"));
1339    ///
1340    /// split.next();
1341    /// assert_eq!(split.remainder(), Some("had a little lamb"));
1342    ///
1343    /// split.by_ref().for_each(drop);
1344    /// assert_eq!(split.remainder(), None);
1345    /// ```
1346    #[inline]
1347    #[must_use]
1348    #[unstable(feature = "str_split_whitespace_remainder", issue = "77998")]
1349    pub fn remainder(&self) -> Option<&'a str> {
1350        self.inner.iter.remainder()
1351    }
1352}
1353
1354#[stable(feature = "split_ascii_whitespace", since = "1.34.0")]
1355impl<'a> Iterator for SplitAsciiWhitespace<'a> {
1356    type Item = &'a str;
1357
1358    #[inline]
1359    fn next(&mut self) -> Option<&'a str> {
1360        self.inner.next()
1361    }
1362
1363    #[inline]
1364    fn size_hint(&self) -> (usize, Option<usize>) {
1365        self.inner.size_hint()
1366    }
1367
1368    #[inline]
1369    fn last(mut self) -> Option<&'a str> {
1370        self.next_back()
1371    }
1372}
1373
1374#[stable(feature = "split_ascii_whitespace", since = "1.34.0")]
1375impl<'a> DoubleEndedIterator for SplitAsciiWhitespace<'a> {
1376    #[inline]
1377    fn next_back(&mut self) -> Option<&'a str> {
1378        self.inner.next_back()
1379    }
1380}
1381
1382#[stable(feature = "split_ascii_whitespace", since = "1.34.0")]
1383impl FusedIterator for SplitAsciiWhitespace<'_> {}
1384
1385impl<'a> SplitAsciiWhitespace<'a> {
1386    /// Returns remainder of the split string.
1387    ///
1388    /// If the iterator is empty, returns `None`.
1389    ///
1390    /// # Examples
1391    ///
1392    /// ```
1393    /// #![feature(str_split_whitespace_remainder)]
1394    ///
1395    /// let mut split = "Mary had a little lamb".split_ascii_whitespace();
1396    /// assert_eq!(split.remainder(), Some("Mary had a little lamb"));
1397    ///
1398    /// split.next();
1399    /// assert_eq!(split.remainder(), Some("had a little lamb"));
1400    ///
1401    /// split.by_ref().for_each(drop);
1402    /// assert_eq!(split.remainder(), None);
1403    /// ```
1404    #[inline]
1405    #[must_use]
1406    #[unstable(feature = "str_split_whitespace_remainder", issue = "77998")]
1407    pub fn remainder(&self) -> Option<&'a str> {
1408        if self.inner.iter.iter.finished {
1409            return None;
1410        }
1411
1412        // SAFETY: Slice is created from str.
1413        Some(unsafe { crate::str::from_utf8_unchecked(&self.inner.iter.iter.v) })
1414    }
1415}
1416
1417#[stable(feature = "split_inclusive", since = "1.51.0")]
1418impl<'a, P: Pattern> Iterator for SplitInclusive<'a, P> {
1419    type Item = &'a str;
1420
1421    #[inline]
1422    fn next(&mut self) -> Option<&'a str> {
1423        self.0.next_inclusive()
1424    }
1425}
1426
1427#[stable(feature = "split_inclusive", since = "1.51.0")]
1428impl<'a, P: Pattern<Searcher<'a>: fmt::Debug>> fmt::Debug for SplitInclusive<'a, P> {
1429    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1430        f.debug_struct("SplitInclusive").field("0", &self.0).finish()
1431    }
1432}
1433
1434// FIXME(#26925) Remove in favor of `#[derive(Clone)]`
1435#[stable(feature = "split_inclusive", since = "1.51.0")]
1436impl<'a, P: Pattern<Searcher<'a>: Clone>> Clone for SplitInclusive<'a, P> {
1437    fn clone(&self) -> Self {
1438        SplitInclusive(self.0.clone())
1439    }
1440}
1441
1442#[stable(feature = "split_inclusive", since = "1.51.0")]
1443impl<'a, P: Pattern<Searcher<'a>: DoubleEndedSearcher<'a>>> DoubleEndedIterator
1444    for SplitInclusive<'a, P>
1445{
1446    #[inline]
1447    fn next_back(&mut self) -> Option<&'a str> {
1448        self.0.next_back_inclusive()
1449    }
1450}
1451
1452#[stable(feature = "split_inclusive", since = "1.51.0")]
1453impl<'a, P: Pattern> FusedIterator for SplitInclusive<'a, P> {}
1454
1455impl<'a, P: Pattern> SplitInclusive<'a, P> {
1456    /// Returns remainder of the split string.
1457    ///
1458    /// If the iterator is empty, returns `None`.
1459    ///
1460    /// # Examples
1461    ///
1462    /// ```
1463    /// #![feature(str_split_inclusive_remainder)]
1464    /// let mut split = "Mary had a little lamb".split_inclusive(' ');
1465    /// assert_eq!(split.remainder(), Some("Mary had a little lamb"));
1466    /// split.next();
1467    /// assert_eq!(split.remainder(), Some("had a little lamb"));
1468    /// split.by_ref().for_each(drop);
1469    /// assert_eq!(split.remainder(), None);
1470    /// ```
1471    #[inline]
1472    #[unstable(feature = "str_split_inclusive_remainder", issue = "77998")]
1473    pub fn remainder(&self) -> Option<&'a str> {
1474        self.0.remainder()
1475    }
1476}
1477
1478/// An iterator of [`u16`] over the string encoded as UTF-16.
1479///
1480/// This struct is created by the [`encode_utf16`] method on [`str`].
1481/// See its documentation for more.
1482///
1483/// [`encode_utf16`]: str::encode_utf16
1484#[derive(Clone)]
1485#[stable(feature = "encode_utf16", since = "1.8.0")]
1486pub struct EncodeUtf16<'a> {
1487    pub(super) chars: Chars<'a>,
1488    pub(super) extra: u16,
1489}
1490
1491#[stable(feature = "collection_debug", since = "1.17.0")]
1492impl fmt::Debug for EncodeUtf16<'_> {
1493    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1494        f.debug_struct("EncodeUtf16").finish_non_exhaustive()
1495    }
1496}
1497
1498#[stable(feature = "encode_utf16", since = "1.8.0")]
1499impl<'a> Iterator for EncodeUtf16<'a> {
1500    type Item = u16;
1501
1502    #[inline]
1503    fn next(&mut self) -> Option<u16> {
1504        if self.extra != 0 {
1505            let tmp = self.extra;
1506            self.extra = 0;
1507            return Some(tmp);
1508        }
1509
1510        let mut buf = [0; 2];
1511        self.chars.next().map(|ch| {
1512            let n = ch.encode_utf16(&mut buf).len();
1513            if n == 2 {
1514                self.extra = buf[1];
1515            }
1516            buf[0]
1517        })
1518    }
1519
1520    #[inline]
1521    fn size_hint(&self) -> (usize, Option<usize>) {
1522        let len = self.chars.iter.len();
1523        // The highest bytes:code units ratio occurs for 3-byte sequences,
1524        // since a 4-byte sequence results in 2 code units. The lower bound
1525        // is therefore determined by assuming the remaining bytes contain as
1526        // many 3-byte sequences as possible. The highest bytes:code units
1527        // ratio is for 1-byte sequences, so use this for the upper bound.
1528        if self.extra == 0 {
1529            (len.div_ceil(3), Some(len))
1530        } else {
1531            // We're in the middle of a surrogate pair, so add the remaining
1532            // surrogate to the bounds.
1533            (len.div_ceil(3) + 1, Some(len + 1))
1534        }
1535    }
1536}
1537
1538#[stable(feature = "fused", since = "1.26.0")]
1539impl FusedIterator for EncodeUtf16<'_> {}
1540
1541/// The return type of [`str::escape_debug`].
1542#[stable(feature = "str_escape", since = "1.34.0")]
1543#[derive(Clone, Debug)]
1544pub struct EscapeDebug<'a> {
1545    pub(super) inner: Chain<
1546        Flatten<option::IntoIter<char_mod::EscapeDebug>>,
1547        FlatMap<Chars<'a>, char_mod::EscapeDebug, CharEscapeDebugContinue>,
1548    >,
1549}
1550
1551/// The return type of [`str::escape_default`].
1552#[stable(feature = "str_escape", since = "1.34.0")]
1553#[derive(Clone, Debug)]
1554pub struct EscapeDefault<'a> {
1555    pub(super) inner: FlatMap<Chars<'a>, char_mod::EscapeDefault, CharEscapeDefault>,
1556}
1557
1558/// The return type of [`str::escape_unicode`].
1559#[stable(feature = "str_escape", since = "1.34.0")]
1560#[derive(Clone, Debug)]
1561pub struct EscapeUnicode<'a> {
1562    pub(super) inner: FlatMap<Chars<'a>, char_mod::EscapeUnicode, CharEscapeUnicode>,
1563}
1564
1565macro_rules! escape_types_impls {
1566    ($( $Name: ident ),+) => {$(
1567        #[stable(feature = "str_escape", since = "1.34.0")]
1568        impl<'a> fmt::Display for $Name<'a> {
1569            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1570                self.clone().try_for_each(|c| f.write_char(c))
1571            }
1572        }
1573
1574        #[stable(feature = "str_escape", since = "1.34.0")]
1575        impl<'a> Iterator for $Name<'a> {
1576            type Item = char;
1577
1578            #[inline]
1579            fn next(&mut self) -> Option<char> { self.inner.next() }
1580
1581            #[inline]
1582            fn size_hint(&self) -> (usize, Option<usize>) { self.inner.size_hint() }
1583
1584            #[inline]
1585            fn try_fold<Acc, Fold, R>(&mut self, init: Acc, fold: Fold) -> R where
1586                Self: Sized, Fold: FnMut(Acc, Self::Item) -> R, R: Try<Output = Acc>
1587            {
1588                self.inner.try_fold(init, fold)
1589            }
1590
1591            #[inline]
1592            fn fold<Acc, Fold>(self, init: Acc, fold: Fold) -> Acc
1593                where Fold: FnMut(Acc, Self::Item) -> Acc,
1594            {
1595                self.inner.fold(init, fold)
1596            }
1597        }
1598
1599        #[stable(feature = "str_escape", since = "1.34.0")]
1600        impl<'a> FusedIterator for $Name<'a> {}
1601    )+}
1602}
1603
1604escape_types_impls!(EscapeDebug, EscapeDefault, EscapeUnicode);
````