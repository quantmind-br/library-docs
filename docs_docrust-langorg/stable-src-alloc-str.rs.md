---
title: str.rs - source
url: https://doc.rust-lang.org/stable/src/alloc/str.rs.html#191
source: crawler
fetched_at: 2026-05-06T21:33:44.85067144-03:00
rendered_js: false
word_count: 3125
summary: This document defines utilities and trait implementations for the Rust string primitive, providing optimized methods for joining slices and integrating with standard library collections.
tags:
    - rust
    - string-manipulation
    - memory-allocation
    - standard-library
    - utf8
    - slice-operations
category: reference
---

## alloc/ str.rs

````rust
1//! Utilities for the `str` primitive type.
2//!
3//! *[See also the `str` primitive type](str).*
4
5#![stable(feature = "rust1", since = "1.0.0")]
6// Many of the usings in this module are only used in the test configuration.
7// It's cleaner to just turn off the unused_imports warning than to fix them.
8#![allow(unused_imports)]
9
10use core::borrow::{Borrow, BorrowMut};
11use core::iter::FusedIterator;
12use core::mem::MaybeUninit;
13#[stable(feature = "encode_utf16", since = "1.8.0")]
14pub use core::str::EncodeUtf16;
15#[stable(feature = "split_ascii_whitespace", since = "1.34.0")]
16pub use core::str::SplitAsciiWhitespace;
17#[stable(feature = "split_inclusive", since = "1.51.0")]
18pub use core::str::SplitInclusive;
19#[stable(feature = "rust1", since = "1.0.0")]
20pub use core::str::SplitWhitespace;
21#[stable(feature = "rust1", since = "1.0.0")]
22pub use core::str::pattern;
23use core::str::pattern::{DoubleEndedSearcher, Pattern, ReverseSearcher, Searcher, Utf8Pattern};
24#[stable(feature = "rust1", since = "1.0.0")]
25pub use core::str::{Bytes, CharIndices, Chars, from_utf8, from_utf8_mut};
26#[stable(feature = "str_escape", since = "1.34.0")]
27pub use core::str::{EscapeDebug, EscapeDefault, EscapeUnicode};
28#[stable(feature = "rust1", since = "1.0.0")]
29pub use core::str::{FromStr, Utf8Error};
30#[allow(deprecated)]
31#[stable(feature = "rust1", since = "1.0.0")]
32pub use core::str::{Lines, LinesAny};
33#[stable(feature = "rust1", since = "1.0.0")]
34pub use core::str::{MatchIndices, RMatchIndices};
35#[stable(feature = "rust1", since = "1.0.0")]
36pub use core::str::{Matches, RMatches};
37#[stable(feature = "rust1", since = "1.0.0")]
38pub use core::str::{ParseBoolError, from_utf8_unchecked, from_utf8_unchecked_mut};
39#[stable(feature = "rust1", since = "1.0.0")]
40pub use core::str::{RSplit, Split};
41#[stable(feature = "rust1", since = "1.0.0")]
42pub use core::str::{RSplitN, SplitN};
43#[stable(feature = "rust1", since = "1.0.0")]
44pub use core::str::{RSplitTerminator, SplitTerminator};
45#[stable(feature = "utf8_chunks", since = "1.79.0")]
46pub use core::str::{Utf8Chunk, Utf8Chunks};
47#[unstable(feature = "str_from_raw_parts", issue = "119206")]
48pub use core::str::{from_raw_parts, from_raw_parts_mut};
49use core::unicode::conversions;
50use core::{mem, ptr};
51
52use crate::borrow::ToOwned;
53use crate::boxed::Box;
54use crate::slice::{Concat, Join, SliceIndex};
55use crate::string::String;
56use crate::vec::Vec;
57
58/// Note: `str` in `Concat<str>` is not meaningful here.
59/// This type parameter of the trait only exists to enable another impl.
60#[cfg(not(no_global_oom_handling))]
61#[unstable(feature = "slice_concat_ext", issue = "27747")]
62impl<S: Borrow<str>> Concat<str> for [S] {
63    type Output = String;
64
65    fn concat(slice: &Self) -> String {
66        Join::join(slice, "")
67    }
68}
69
70#[cfg(not(no_global_oom_handling))]
71#[unstable(feature = "slice_concat_ext", issue = "27747")]
72impl<S: Borrow<str>> Join<&str> for [S] {
73    type Output = String;
74
75    fn join(slice: &Self, sep: &str) -> String {
76        unsafe { String::from_utf8_unchecked(join_generic_copy(slice, sep.as_bytes())) }
77    }
78}
79
80#[cfg(not(no_global_oom_handling))]
81macro_rules! specialize_for_lengths {
82    ($separator:expr, $target:expr, $iter:expr; $($num:expr),*) => {{
83        let mut target = $target;
84        let iter = $iter;
85        let sep_bytes = $separator;
86        match $separator.len() {
87            $(
88                // loops with hardcoded sizes run much faster
89                // specialize the cases with small separator lengths
90                $num => {
91                    for s in iter {
92                        copy_slice_and_advance!(target, sep_bytes);
93                        let content_bytes = s.borrow().as_ref();
94                        copy_slice_and_advance!(target, content_bytes);
95                    }
96                },
97            )*
98            _ => {
99                // arbitrary non-zero size fallback
100                for s in iter {
101                    copy_slice_and_advance!(target, sep_bytes);
102                    let content_bytes = s.borrow().as_ref();
103                    copy_slice_and_advance!(target, content_bytes);
104                }
105            }
106        }
107        target
108    }}
109}
110
111#[cfg(not(no_global_oom_handling))]
112macro_rules! copy_slice_and_advance {
113    ($target:expr, $bytes:expr) => {
114        let len = $bytes.len();
115        let (head, tail) = { $target }.split_at_mut(len);
116        head.copy_from_slice($bytes);
117        $target = tail;
118    };
119}
120
121// Optimized join implementation that works for both Vec<T> (T: Copy) and String's inner vec
122// Currently (2018-05-13) there is a bug with type inference and specialization (see issue #36262)
123// For this reason SliceConcat<T> is not specialized for T: Copy and SliceConcat<str> is the
124// only user of this function. It is left in place for the time when that is fixed.
125//
126// the bounds for String-join are S: Borrow<str> and for Vec-join Borrow<[T]>
127// [T] and str both impl AsRef<[T]> for some T
128// => s.borrow().as_ref() and we always have slices
129#[cfg(not(no_global_oom_handling))]
130fn join_generic_copy<B, T, S>(slice: &[S], sep: &[T]) -> Vec<T>
131where
132    T: Copy,
133    B: AsRef<[T]> + ?Sized,
134    S: Borrow<B>,
135{
136    let sep_len = sep.len();
137    let mut iter = slice.iter();
138
139    // the first slice is the only one without a separator preceding it
140    let first = match iter.next() {
141        Some(first) => first,
142        None => return vec![],
143    };
144
145    // compute the exact total length of the joined Vec
146    // if the `len` calculation overflows, we'll panic
147    // we would have run out of memory anyway and the rest of the function requires
148    // the entire Vec pre-allocated for safety
149    let reserved_len = sep_len
150        .checked_mul(iter.len())
151        .and_then(|n| {
152            slice.iter().map(|s| s.borrow().as_ref().len()).try_fold(n, usize::checked_add)
153        })
154        .expect("attempt to join into collection with len > usize::MAX");
155
156    // prepare an uninitialized buffer
157    let mut result = Vec::with_capacity(reserved_len);
158    debug_assert!(result.capacity() >= reserved_len);
159
160    result.extend_from_slice(first.borrow().as_ref());
161
162    unsafe {
163        let pos = result.len();
164        let target = result.spare_capacity_mut().get_unchecked_mut(..reserved_len - pos);
165
166        // Convert the separator and slices to slices of MaybeUninit
167        // to simplify implementation in specialize_for_lengths
168        let sep_uninit = core::slice::from_raw_parts(sep.as_ptr().cast(), sep.len());
169        let iter_uninit = iter.map(|it| {
170            let it = it.borrow().as_ref();
171            core::slice::from_raw_parts(it.as_ptr().cast(), it.len())
172        });
173
174        // copy separator and slices over without bounds checks
175        // generate loops with hardcoded offsets for small separators
176        // massive improvements possible (~ x2)
177        let remain = specialize_for_lengths!(sep_uninit, target, iter_uninit; 0, 1, 2, 3, 4);
178
179        // A weird borrow implementation may return different
180        // slices for the length calculation and the actual copy.
181        // Make sure we don't expose uninitialized bytes to the caller.
182        let result_len = reserved_len - remain.len();
183        result.set_len(result_len);
184    }
185    result
186}
187
188#[stable(feature = "rust1", since = "1.0.0")]
189impl Borrow<str> for String {
190    #[inline]
191    fn borrow(&self) -> &str {
192        &self[..]
193    }
194}
195
196#[stable(feature = "string_borrow_mut", since = "1.36.0")]
197impl BorrowMut<str> for String {
198    #[inline]
199    fn borrow_mut(&mut self) -> &mut str {
200        &mut self[..]
201    }
202}
203
204#[cfg(not(no_global_oom_handling))]
205#[stable(feature = "rust1", since = "1.0.0")]
206impl ToOwned for str {
207    type Owned = String;
208
209    #[inline]
210    fn to_owned(&self) -> String {
211        unsafe { String::from_utf8_unchecked(self.as_bytes().to_owned()) }
212    }
213
214    #[inline]
215    fn clone_into(&self, target: &mut String) {
216        target.clear();
217        target.push_str(self);
218    }
219}
220
221/// Methods for string slices.
222impl str {
223    /// Converts a `Box<str>` into a `Box<[u8]>` without copying or allocating.
224    ///
225    /// # Examples
226    ///
227    /// ```
228    /// let s = "this is a string";
229    /// let boxed_str = s.to_owned().into_boxed_str();
230    /// let boxed_bytes = boxed_str.into_boxed_bytes();
231    /// assert_eq!(*boxed_bytes, *s.as_bytes());
232    /// ```
233    #[rustc_allow_incoherent_impl]
234    #[stable(feature = "str_box_extras", since = "1.20.0")]
235    #[must_use = "`self` will be dropped if the result is not used"]
236    #[inline]
237    pub fn into_boxed_bytes(self: Box<Self>) -> Box<[u8]> {
238        self.into()
239    }
240
241    /// Replaces all matches of a pattern with another string.
242    ///
243    /// `replace` creates a new [`String`], and copies the data from this string slice into it.
244    /// While doing so, it attempts to find matches of a pattern. If it finds any, it
245    /// replaces them with the replacement string slice.
246    ///
247    /// # Examples
248    ///
249    /// ```
250    /// let s = "this is old";
251    ///
252    /// assert_eq!("this is new", s.replace("old", "new"));
253    /// assert_eq!("than an old", s.replace("is", "an"));
254    /// ```
255    ///
256    /// When the pattern doesn't match, it returns this string slice as [`String`]:
257    ///
258    /// ```
259    /// let s = "this is old";
260    /// assert_eq!(s, s.replace("cookie monster", "little lamb"));
261    /// ```
262    #[cfg(not(no_global_oom_handling))]
263    #[rustc_allow_incoherent_impl]
264    #[must_use = "this returns the replaced string as a new allocation, \
265                  without modifying the original"]
266    #[stable(feature = "rust1", since = "1.0.0")]
267    #[inline]
268    pub fn replace<P: Pattern>(&self, from: P, to: &str) -> String {
269        // Fast path for replacing a single ASCII character with another.
270        if let Some(from_byte) = match from.as_utf8_pattern() {
271            Some(Utf8Pattern::StringPattern([from_byte])) => Some(*from_byte),
272            Some(Utf8Pattern::CharPattern(c)) => c.as_ascii().map(|ascii_char| ascii_char.to_u8()),
273            _ => None,
274        } {
275            if let [to_byte] = to.as_bytes() {
276                return unsafe { replace_ascii(self.as_bytes(), from_byte, *to_byte) };
277            }
278        }
279        // Set result capacity to self.len() when from.len() <= to.len()
280        let default_capacity = match from.as_utf8_pattern() {
281            Some(Utf8Pattern::StringPattern(s)) if s.len() <= to.len() => self.len(),
282            Some(Utf8Pattern::CharPattern(c)) if c.len_utf8() <= to.len() => self.len(),
283            _ => 0,
284        };
285        let mut result = String::with_capacity(default_capacity);
286        let mut last_end = 0;
287        for (start, part) in self.match_indices(from) {
288            result.push_str(unsafe { self.get_unchecked(last_end..start) });
289            result.push_str(to);
290            last_end = start + part.len();
291        }
292        result.push_str(unsafe { self.get_unchecked(last_end..self.len()) });
293        result
294    }
295
296    /// Replaces first N matches of a pattern with another string.
297    ///
298    /// `replacen` creates a new [`String`], and copies the data from this string slice into it.
299    /// While doing so, it attempts to find matches of a pattern. If it finds any, it
300    /// replaces them with the replacement string slice at most `count` times.
301    ///
302    /// # Examples
303    ///
304    /// ```
305    /// let s = "foo foo 123 foo";
306    /// assert_eq!("new new 123 foo", s.replacen("foo", "new", 2));
307    /// assert_eq!("faa fao 123 foo", s.replacen('o', "a", 3));
308    /// assert_eq!("foo foo new23 foo", s.replacen(char::is_numeric, "new", 1));
309    /// ```
310    ///
311    /// When the pattern doesn't match, it returns this string slice as [`String`]:
312    ///
313    /// ```
314    /// let s = "this is old";
315    /// assert_eq!(s, s.replacen("cookie monster", "little lamb", 10));
316    /// ```
317    #[cfg(not(no_global_oom_handling))]
318    #[rustc_allow_incoherent_impl]
319    #[doc(alias = "replace_first")]
320    #[must_use = "this returns the replaced string as a new allocation, \
321                  without modifying the original"]
322    #[stable(feature = "str_replacen", since = "1.16.0")]
323    pub fn replacen<P: Pattern>(&self, pat: P, to: &str, count: usize) -> String {
324        // Hope to reduce the times of re-allocation
325        let mut result = String::with_capacity(32);
326        let mut last_end = 0;
327        for (start, part) in self.match_indices(pat).take(count) {
328            result.push_str(unsafe { self.get_unchecked(last_end..start) });
329            result.push_str(to);
330            last_end = start + part.len();
331        }
332        result.push_str(unsafe { self.get_unchecked(last_end..self.len()) });
333        result
334    }
335
336    /// Returns the lowercase equivalent of this string slice, as a new [`String`].
337    ///
338    /// 'Lowercase' is defined according to the terms of the Unicode Derived Core Property
339    /// `Lowercase`.
340    ///
341    /// Since some characters can expand into multiple characters when changing
342    /// the case, this function returns a [`String`] instead of modifying the
343    /// parameter in-place.
344    ///
345    /// # Examples
346    ///
347    /// Basic usage:
348    ///
349    /// ```
350    /// let s = "HELLO";
351    ///
352    /// assert_eq!("hello", s.to_lowercase());
353    /// ```
354    ///
355    /// A tricky example, with sigma:
356    ///
357    /// ```
358    /// let sigma = "Σ";
359    ///
360    /// assert_eq!("σ", sigma.to_lowercase());
361    ///
362    /// // but at the end of a word, it's ς, not σ:
363    /// let odysseus = "ὈΔΥΣΣΕΎΣ";
364    ///
365    /// assert_eq!("ὀδυσσεύς", odysseus.to_lowercase());
366    /// ```
367    ///
368    /// Languages without case are not changed:
369    ///
370    /// ```
371    /// let new_year = "农历新年";
372    ///
373    /// assert_eq!(new_year, new_year.to_lowercase());
374    /// ```
375    #[cfg(not(no_global_oom_handling))]
376    #[rustc_allow_incoherent_impl]
377    #[must_use = "this returns the lowercase string as a new String, \
378                  without modifying the original"]
379    #[stable(feature = "unicode_case_mapping", since = "1.2.0")]
380    pub fn to_lowercase(&self) -> String {
381        let (mut s, rest) = convert_while_ascii(self, u8::to_ascii_lowercase);
382
383        let prefix_len = s.len();
384
385        for (i, c) in rest.char_indices() {
386            if c == 'Σ' {
387                // Σ maps to σ, except at the end of a word where it maps to ς.
388                // This is the only conditional (contextual) but language-independent mapping
389                // in `SpecialCasing.txt`,
390                // so hard-code it rather than have a generic "condition" mechanism.
391                // See https://github.com/rust-lang/rust/issues/26035
392                let sigma_lowercase = map_uppercase_sigma(self, prefix_len + i);
393                s.push(sigma_lowercase);
394            } else {
395                match conversions::to_lower(c) {
396                    [a, '\0', _] => s.push(a),
397                    [a, b, '\0'] => {
398                        s.push(a);
399                        s.push(b);
400                    }
401                    [a, b, c] => {
402                        s.push(a);
403                        s.push(b);
404                        s.push(c);
405                    }
406                }
407            }
408        }
409        return s;
410
411        fn map_uppercase_sigma(from: &str, i: usize) -> char {
412            // See https://www.unicode.org/versions/Unicode7.0.0/ch03.pdf#G33992
413            // for the definition of `Final_Sigma`.
414            let is_word_final = case_ignorable_then_cased(from[..i].chars().rev())
415                && !case_ignorable_then_cased(from[i + const { 'Σ'.len_utf8() }..].chars());
416            if is_word_final { 'ς' } else { 'σ' }
417        }
418
419        fn case_ignorable_then_cased<I: Iterator<Item = char>>(iter: I) -> bool {
420            match iter.skip_while(|&c| c.is_case_ignorable()).next() {
421                Some(c) => c.is_cased(),
422                None => false,
423            }
424        }
425    }
426
427    /// Returns the uppercase equivalent of this string slice, as a new [`String`].
428    ///
429    /// 'Uppercase' is defined according to the terms of the Unicode Derived Core Property
430    /// `Uppercase`.
431    ///
432    /// Since some characters can expand into multiple characters when changing
433    /// the case, this function returns a [`String`] instead of modifying the
434    /// parameter in-place.
435    ///
436    /// # Examples
437    ///
438    /// Basic usage:
439    ///
440    /// ```
441    /// let s = "hello";
442    ///
443    /// assert_eq!("HELLO", s.to_uppercase());
444    /// ```
445    ///
446    /// Scripts without case are not changed:
447    ///
448    /// ```
449    /// let new_year = "农历新年";
450    ///
451    /// assert_eq!(new_year, new_year.to_uppercase());
452    /// ```
453    ///
454    /// One character can become multiple:
455    /// ```
456    /// let s = "tschüß";
457    ///
458    /// assert_eq!("TSCHÜSS", s.to_uppercase());
459    /// ```
460    #[cfg(not(no_global_oom_handling))]
461    #[rustc_allow_incoherent_impl]
462    #[must_use = "this returns the uppercase string as a new String, \
463                  without modifying the original"]
464    #[stable(feature = "unicode_case_mapping", since = "1.2.0")]
465    pub fn to_uppercase(&self) -> String {
466        let (mut s, rest) = convert_while_ascii(self, u8::to_ascii_uppercase);
467
468        for c in rest.chars() {
469            match conversions::to_upper(c) {
470                [a, '\0', _] => s.push(a),
471                [a, b, '\0'] => {
472                    s.push(a);
473                    s.push(b);
474                }
475                [a, b, c] => {
476                    s.push(a);
477                    s.push(b);
478                    s.push(c);
479                }
480            }
481        }
482        s
483    }
484
485    /// Converts a [`Box<str>`] into a [`String`] without copying or allocating.
486    ///
487    /// # Examples
488    ///
489    /// ```
490    /// let string = String::from("birthday gift");
491    /// let boxed_str = string.clone().into_boxed_str();
492    ///
493    /// assert_eq!(boxed_str.into_string(), string);
494    /// ```
495    #[stable(feature = "box_str", since = "1.4.0")]
496    #[rustc_allow_incoherent_impl]
497    #[must_use = "`self` will be dropped if the result is not used"]
498    #[inline]
499    pub fn into_string(self: Box<Self>) -> String {
500        let slice = Box::<[u8]>::from(self);
501        unsafe { String::from_utf8_unchecked(slice.into_vec()) }
502    }
503
504    /// Creates a new [`String`] by repeating a string `n` times.
505    ///
506    /// # Panics
507    ///
508    /// This function will panic if the capacity would overflow.
509    ///
510    /// # Examples
511    ///
512    /// Basic usage:
513    ///
514    /// ```
515    /// assert_eq!("abc".repeat(4), String::from("abcabcabcabc"));
516    /// ```
517    ///
518    /// A panic upon overflow:
519    ///
520    /// ```should_panic
521    /// // this will panic at runtime
522    /// let huge = "0123456789abcdef".repeat(usize::MAX);
523    /// ```
524    #[cfg(not(no_global_oom_handling))]
525    #[rustc_allow_incoherent_impl]
526    #[must_use]
527    #[stable(feature = "repeat_str", since = "1.16.0")]
528    #[inline]
529    pub fn repeat(&self, n: usize) -> String {
530        unsafe { String::from_utf8_unchecked(self.as_bytes().repeat(n)) }
531    }
532
533    /// Returns a copy of this string where each character is mapped to its
534    /// ASCII upper case equivalent.
535    ///
536    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
537    /// but non-ASCII letters are unchanged.
538    ///
539    /// To uppercase the value in-place, use [`make_ascii_uppercase`].
540    ///
541    /// To uppercase ASCII characters in addition to non-ASCII characters, use
542    /// [`to_uppercase`].
543    ///
544    /// # Examples
545    ///
546    /// ```
547    /// let s = "Grüße, Jürgen ❤";
548    ///
549    /// assert_eq!("GRüßE, JüRGEN ❤", s.to_ascii_uppercase());
550    /// ```
551    ///
552    /// [`make_ascii_uppercase`]: str::make_ascii_uppercase
553    /// [`to_uppercase`]: #method.to_uppercase
554    #[cfg(not(no_global_oom_handling))]
555    #[rustc_allow_incoherent_impl]
556    #[must_use = "to uppercase the value in-place, use `make_ascii_uppercase()`"]
557    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
558    #[inline]
559    pub fn to_ascii_uppercase(&self) -> String {
560        let mut s = self.to_owned();
561        s.make_ascii_uppercase();
562        s
563    }
564
565    /// Returns a copy of this string where each character is mapped to its
566    /// ASCII lower case equivalent.
567    ///
568    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
569    /// but non-ASCII letters are unchanged.
570    ///
571    /// To lowercase the value in-place, use [`make_ascii_lowercase`].
572    ///
573    /// To lowercase ASCII characters in addition to non-ASCII characters, use
574    /// [`to_lowercase`].
575    ///
576    /// # Examples
577    ///
578    /// ```
579    /// let s = "Grüße, Jürgen ❤";
580    ///
581    /// assert_eq!("grüße, jürgen ❤", s.to_ascii_lowercase());
582    /// ```
583    ///
584    /// [`make_ascii_lowercase`]: str::make_ascii_lowercase
585    /// [`to_lowercase`]: #method.to_lowercase
586    #[cfg(not(no_global_oom_handling))]
587    #[rustc_allow_incoherent_impl]
588    #[must_use = "to lowercase the value in-place, use `make_ascii_lowercase()`"]
589    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
590    #[inline]
591    pub fn to_ascii_lowercase(&self) -> String {
592        let mut s = self.to_owned();
593        s.make_ascii_lowercase();
594        s
595    }
596}
597
598/// Converts a boxed slice of bytes to a boxed string slice without checking
599/// that the string contains valid UTF-8.
600///
601/// # Safety
602///
603/// * The provided bytes must contain a valid UTF-8 sequence.
604///
605/// # Examples
606///
607/// ```
608/// let smile_utf8 = Box::new([226, 152, 186]);
609/// let smile = unsafe { std::str::from_boxed_utf8_unchecked(smile_utf8) };
610///
611/// assert_eq!("☺", &*smile);
612/// ```
613#[stable(feature = "str_box_extras", since = "1.20.0")]
614#[must_use]
615#[inline]
616pub unsafe fn from_boxed_utf8_unchecked(v: Box<[u8]>) -> Box<str> {
617    unsafe { Box::from_raw(Box::into_raw(v) as *mut str) }
618}
619
620/// Converts leading ascii bytes in `s` by calling the `convert` function.
621///
622/// For better average performance, this happens in chunks of `2*size_of::<usize>()`.
623///
624/// Returns a tuple of the converted prefix and the remainder starting from
625/// the first non-ascii character.
626///
627/// This function is only public so that it can be verified in a codegen test,
628/// see `issue-123712-str-to-lower-autovectorization.rs`.
629#[unstable(feature = "str_internals", issue = "none")]
630#[doc(hidden)]
631#[inline]
632#[cfg(not(no_global_oom_handling))]
633pub fn convert_while_ascii(s: &str, convert: fn(&u8) -> u8) -> (String, &str) {
634    // Process the input in chunks of 16 bytes to enable auto-vectorization.
635    // Previously the chunk size depended on the size of `usize`,
636    // but on 32-bit platforms with sse or neon is also the better choice.
637    // The only downside on other platforms would be a bit more loop-unrolling.
638    const N: usize = 16;
639
640    let mut slice = s.as_bytes();
641    let mut out = Vec::with_capacity(slice.len());
642    let mut out_slice = out.spare_capacity_mut();
643
644    let mut ascii_prefix_len = 0_usize;
645    let mut is_ascii = [false; N];
646
647    while slice.len() >= N {
648        // SAFETY: checked in loop condition
649        let chunk = unsafe { slice.get_unchecked(..N) };
650        // SAFETY: out_slice has at least same length as input slice and gets sliced with the same offsets
651        let out_chunk = unsafe { out_slice.get_unchecked_mut(..N) };
652
653        for j in 0..N {
654            is_ascii[j] = chunk[j] <= 127;
655        }
656
657        // Auto-vectorization for this check is a bit fragile, sum and comparing against the chunk
658        // size gives the best result, specifically a pmovmsk instruction on x86.
659        // See https://github.com/llvm/llvm-project/issues/96395 for why llvm currently does not
660        // currently recognize other similar idioms.
661        if is_ascii.iter().map(|x| *x as u8).sum::<u8>() as usize != N {
662            break;
663        }
664
665        for j in 0..N {
666            out_chunk[j] = MaybeUninit::new(convert(&chunk[j]));
667        }
668
669        ascii_prefix_len += N;
670        slice = unsafe { slice.get_unchecked(N..) };
671        out_slice = unsafe { out_slice.get_unchecked_mut(N..) };
672    }
673
674    // handle the remainder as individual bytes
675    while slice.len() > 0 {
676        let byte = slice[0];
677        if byte > 127 {
678            break;
679        }
680        // SAFETY: out_slice has at least same length as input slice
681        unsafe {
682            *out_slice.get_unchecked_mut(0) = MaybeUninit::new(convert(&byte));
683        }
684        ascii_prefix_len += 1;
685        slice = unsafe { slice.get_unchecked(1..) };
686        out_slice = unsafe { out_slice.get_unchecked_mut(1..) };
687    }
688
689    unsafe {
690        // SAFETY: ascii_prefix_len bytes have been initialized above
691        out.set_len(ascii_prefix_len);
692
693        // SAFETY: We have written only valid ascii to the output vec
694        let ascii_string = String::from_utf8_unchecked(out);
695
696        // SAFETY: we know this is a valid char boundary
697        // since we only skipped over leading ascii bytes
698        let rest = core::str::from_utf8_unchecked(slice);
699
700        (ascii_string, rest)
701    }
702}
703#[inline]
704#[cfg(not(no_global_oom_handling))]
705#[allow(dead_code)]
706/// Faster implementation of string replacement for ASCII to ASCII cases.
707/// Should produce fast vectorized code.
708unsafe fn replace_ascii(utf8_bytes: &[u8], from: u8, to: u8) -> String {
709    let result: Vec<u8> = utf8_bytes.iter().map(|b| if *b == from { to } else { *b }).collect();
710    // SAFETY: We replaced ascii with ascii on valid utf8 strings.
711    unsafe { String::from_utf8_unchecked(result) }
712}
````