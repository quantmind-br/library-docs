---
title: methods.rs - source
url: https://doc.rust-lang.org/src/core/char/methods.rs.html#778
source: crawler
fetched_at: 2026-05-06T21:29:07.986737923-03:00
rendered_js: false
word_count: 7378
summary: This document defines the core Rust implementation for the char primitive type, including associated constants for bounds and character properties, as well as utility functions for Unicode decoding and type conversion.
tags:
    - rust
    - char
    - unicode
    - primitive-types
    - utf-8
    - utf-16
    - api-reference
category: reference
---

## core/char/ methods.rs

````rust
1//! impl char {}
2
3use super::*;
4use crate::panic::const_panic;
5use crate::slice;
6use crate::str::from_utf8_unchecked_mut;
7use crate::ub_checks::assert_unsafe_precondition;
8use crate::unicode::printable::is_printable;
9use crate::unicode::{self, conversions};
10
11impl char {
12    /// The lowest valid code point a `char` can have, `'\0'`.
13    ///
14    /// Unlike integer types, `char` actually has a gap in the middle,
15    /// meaning that the range of possible `char`s is smaller than you
16    /// might expect. Ranges of `char` will automatically hop this gap
17    /// for you:
18    ///
19    /// ```
20    /// let dist = u32::from(char::MAX) - u32::from(char::MIN);
21    /// let size = (char::MIN..=char::MAX).count() as u32;
22    /// assert!(size < dist);
23    /// ```
24    ///
25    /// Despite this gap, the `MIN` and [`MAX`] values can be used as bounds for
26    /// all `char` values.
27    ///
28    /// [`MAX`]: char::MAX
29    ///
30    /// # Examples
31    ///
32    /// ```
33    /// # fn something_which_returns_char() -> char { 'a' }
34    /// let c: char = something_which_returns_char();
35    /// assert!(char::MIN <= c);
36    ///
37    /// let value_at_min = u32::from(char::MIN);
38    /// assert_eq!(char::from_u32(value_at_min), Some('\0'));
39    /// ```
40    #[stable(feature = "char_min", since = "1.83.0")]
41    pub const MIN: char = '\0';
42
43    /// The highest valid code point a `char` can have, `'\u{10FFFF}'`.
44    ///
45    /// Unlike integer types, `char` actually has a gap in the middle,
46    /// meaning that the range of possible `char`s is smaller than you
47    /// might expect. Ranges of `char` will automatically hop this gap
48    /// for you:
49    ///
50    /// ```
51    /// let dist = u32::from(char::MAX) - u32::from(char::MIN);
52    /// let size = (char::MIN..=char::MAX).count() as u32;
53    /// assert!(size < dist);
54    /// ```
55    ///
56    /// Despite this gap, the [`MIN`] and `MAX` values can be used as bounds for
57    /// all `char` values.
58    ///
59    /// [`MIN`]: char::MIN
60    ///
61    /// # Examples
62    ///
63    /// ```
64    /// # fn something_which_returns_char() -> char { 'a' }
65    /// let c: char = something_which_returns_char();
66    /// assert!(c <= char::MAX);
67    ///
68    /// let value_at_max = u32::from(char::MAX);
69    /// assert_eq!(char::from_u32(value_at_max), Some('\u{10FFFF}'));
70    /// assert_eq!(char::from_u32(value_at_max + 1), None);
71    /// ```
72    #[stable(feature = "assoc_char_consts", since = "1.52.0")]
73    pub const MAX: char = '\u{10FFFF}';
74
75    /// The maximum number of bytes required to [encode](char::encode_utf8) a `char` to
76    /// UTF-8 encoding.
77    #[stable(feature = "char_max_len_assoc", since = "1.93.0")]
78    pub const MAX_LEN_UTF8: usize = 4;
79
80    /// The maximum number of two-byte units required to [encode](char::encode_utf16) a `char`
81    /// to UTF-16 encoding.
82    #[stable(feature = "char_max_len_assoc", since = "1.93.0")]
83    pub const MAX_LEN_UTF16: usize = 2;
84
85    /// `U+FFFD REPLACEMENT CHARACTER` (�) is used in Unicode to represent a
86    /// decoding error.
87    ///
88    /// It can occur, for example, when giving ill-formed UTF-8 bytes to
89    /// [`String::from_utf8_lossy`](../std/string/struct.String.html#method.from_utf8_lossy).
90    #[stable(feature = "assoc_char_consts", since = "1.52.0")]
91    pub const REPLACEMENT_CHARACTER: char = '\u{FFFD}';
92
93    /// The version of [Unicode](https://www.unicode.org/) that the Unicode parts of
94    /// `char` and `str` methods are based on.
95    ///
96    /// New versions of Unicode are released regularly and subsequently all methods
97    /// in the standard library depending on Unicode are updated. Therefore the
98    /// behavior of some `char` and `str` methods and the value of this constant
99    /// changes over time. This is *not* considered to be a breaking change.
100    ///
101    /// The version numbering scheme is explained in
102    /// [Unicode 11.0 or later, Section 3.1 Versions of the Unicode Standard](https://www.unicode.org/versions/Unicode11.0.0/ch03.pdf#page=4).
103    #[stable(feature = "assoc_char_consts", since = "1.52.0")]
104    pub const UNICODE_VERSION: (u8, u8, u8) = crate::unicode::UNICODE_VERSION;
105
106    /// Creates an iterator over the native endian UTF-16 encoded code points in `iter`,
107    /// returning unpaired surrogates as `Err`s.
108    ///
109    /// # Examples
110    ///
111    /// Basic usage:
112    ///
113    /// ```
114    /// // 𝄞mus<invalid>ic<invalid>
115    /// let v = [
116    ///     0xD834, 0xDD1E, 0x006d, 0x0075, 0x0073, 0xDD1E, 0x0069, 0x0063, 0xD834,
117    /// ];
118    ///
119    /// assert_eq!(
120    ///     char::decode_utf16(v)
121    ///         .map(|r| r.map_err(|e| e.unpaired_surrogate()))
122    ///         .collect::<Vec<_>>(),
123    ///     vec![
124    ///         Ok('𝄞'),
125    ///         Ok('m'), Ok('u'), Ok('s'),
126    ///         Err(0xDD1E),
127    ///         Ok('i'), Ok('c'),
128    ///         Err(0xD834)
129    ///     ]
130    /// );
131    /// ```
132    ///
133    /// A lossy decoder can be obtained by replacing `Err` results with the replacement character:
134    ///
135    /// ```
136    /// // 𝄞mus<invalid>ic<invalid>
137    /// let v = [
138    ///     0xD834, 0xDD1E, 0x006d, 0x0075, 0x0073, 0xDD1E, 0x0069, 0x0063, 0xD834,
139    /// ];
140    ///
141    /// assert_eq!(
142    ///     char::decode_utf16(v)
143    ///        .map(|r| r.unwrap_or(char::REPLACEMENT_CHARACTER))
144    ///        .collect::<String>(),
145    ///     "𝄞mus�ic�"
146    /// );
147    /// ```
148    #[stable(feature = "assoc_char_funcs", since = "1.52.0")]
149    #[inline]
150    pub fn decode_utf16<I: IntoIterator<Item = u16>>(iter: I) -> DecodeUtf16<I::IntoIter> {
151        super::decode::decode_utf16(iter)
152    }
153
154    /// Converts a `u32` to a `char`.
155    ///
156    /// Note that all `char`s are valid [`u32`]s, and can be cast to one with
157    /// [`as`](../std/keyword.as.html):
158    ///
159    /// ```
160    /// let c = '💯';
161    /// let i = c as u32;
162    ///
163    /// assert_eq!(128175, i);
164    /// ```
165    ///
166    /// However, the reverse is not true: not all valid [`u32`]s are valid
167    /// `char`s. `from_u32()` will return `None` if the input is not a valid value
168    /// for a `char`.
169    ///
170    /// For an unsafe version of this function which ignores these checks, see
171    /// [`from_u32_unchecked`].
172    ///
173    /// [`from_u32_unchecked`]: #method.from_u32_unchecked
174    ///
175    /// # Examples
176    ///
177    /// Basic usage:
178    ///
179    /// ```
180    /// let c = char::from_u32(0x2764);
181    ///
182    /// assert_eq!(Some('❤'), c);
183    /// ```
184    ///
185    /// Returning `None` when the input is not a valid `char`:
186    ///
187    /// ```
188    /// let c = char::from_u32(0x110000);
189    ///
190    /// assert_eq!(None, c);
191    /// ```
192    #[stable(feature = "assoc_char_funcs", since = "1.52.0")]
193    #[rustc_const_stable(feature = "const_char_convert", since = "1.67.0")]
194    #[must_use]
195    #[inline]
196    pub const fn from_u32(i: u32) -> Option<char> {
197        super::convert::from_u32(i)
198    }
199
200    /// Converts a `u32` to a `char`, ignoring validity.
201    ///
202    /// Note that all `char`s are valid [`u32`]s, and can be cast to one with
203    /// `as`:
204    ///
205    /// ```
206    /// let c = '💯';
207    /// let i = c as u32;
208    ///
209    /// assert_eq!(128175, i);
210    /// ```
211    ///
212    /// However, the reverse is not true: not all valid [`u32`]s are valid
213    /// `char`s. `from_u32_unchecked()` will ignore this, and blindly cast to
214    /// `char`, possibly creating an invalid one.
215    ///
216    /// # Safety
217    ///
218    /// This function is unsafe, as it may construct invalid `char` values.
219    ///
220    /// For a safe version of this function, see the [`from_u32`] function.
221    ///
222    /// [`from_u32`]: #method.from_u32
223    ///
224    /// # Examples
225    ///
226    /// Basic usage:
227    ///
228    /// ```
229    /// let c = unsafe { char::from_u32_unchecked(0x2764) };
230    ///
231    /// assert_eq!('❤', c);
232    /// ```
233    #[stable(feature = "assoc_char_funcs", since = "1.52.0")]
234    #[rustc_const_stable(feature = "const_char_from_u32_unchecked", since = "1.81.0")]
235    #[must_use]
236    #[inline]
237    pub const unsafe fn from_u32_unchecked(i: u32) -> char {
238        // SAFETY: the safety contract must be upheld by the caller.
239        unsafe { super::convert::from_u32_unchecked(i) }
240    }
241
242    /// Converts a digit in the given radix to a `char`.
243    ///
244    /// A 'radix' here is sometimes also called a 'base'. A radix of two
245    /// indicates a binary number, a radix of ten, decimal, and a radix of
246    /// sixteen, hexadecimal, to give some common values. Arbitrary
247    /// radices are supported.
248    ///
249    /// `from_digit()` will return `None` if the input is not a digit in
250    /// the given radix.
251    ///
252    /// # Panics
253    ///
254    /// Panics if given a radix larger than 36.
255    ///
256    /// # Examples
257    ///
258    /// Basic usage:
259    ///
260    /// ```
261    /// let c = char::from_digit(4, 10);
262    ///
263    /// assert_eq!(Some('4'), c);
264    ///
265    /// // Decimal 11 is a single digit in base 16
266    /// let c = char::from_digit(11, 16);
267    ///
268    /// assert_eq!(Some('b'), c);
269    /// ```
270    ///
271    /// Returning `None` when the input is not a digit:
272    ///
273    /// ```
274    /// let c = char::from_digit(20, 10);
275    ///
276    /// assert_eq!(None, c);
277    /// ```
278    ///
279    /// Passing a large radix, causing a panic:
280    ///
281    /// ```should_panic
282    /// // this panics
283    /// let _c = char::from_digit(1, 37);
284    /// ```
285    #[stable(feature = "assoc_char_funcs", since = "1.52.0")]
286    #[rustc_const_stable(feature = "const_char_convert", since = "1.67.0")]
287    #[must_use]
288    #[inline]
289    pub const fn from_digit(num: u32, radix: u32) -> Option<char> {
290        super::convert::from_digit(num, radix)
291    }
292
293    /// Checks if a `char` is a digit in the given radix.
294    ///
295    /// A 'radix' here is sometimes also called a 'base'. A radix of two
296    /// indicates a binary number, a radix of ten, decimal, and a radix of
297    /// sixteen, hexadecimal, to give some common values. Arbitrary
298    /// radices are supported.
299    ///
300    /// Compared to [`is_numeric()`], this function only recognizes the characters
301    /// `0-9`, `a-z` and `A-Z`.
302    ///
303    /// 'Digit' is defined to be only the following characters:
304    ///
305    /// * `0-9`
306    /// * `a-z`
307    /// * `A-Z`
308    ///
309    /// For a more comprehensive understanding of 'digit', see [`is_numeric()`].
310    ///
311    /// [`is_numeric()`]: #method.is_numeric
312    ///
313    /// # Panics
314    ///
315    /// Panics if given a radix smaller than 2 or larger than 36.
316    ///
317    /// # Examples
318    ///
319    /// Basic usage:
320    ///
321    /// ```
322    /// assert!('1'.is_digit(10));
323    /// assert!('f'.is_digit(16));
324    /// assert!(!'f'.is_digit(10));
325    /// ```
326    ///
327    /// Passing a large radix, causing a panic:
328    ///
329    /// ```should_panic
330    /// // this panics
331    /// '1'.is_digit(37);
332    /// ```
333    ///
334    /// Passing a small radix, causing a panic:
335    ///
336    /// ```should_panic
337    /// // this panics
338    /// '1'.is_digit(1);
339    /// ```
340    #[stable(feature = "rust1", since = "1.0.0")]
341    #[rustc_const_stable(feature = "const_char_classify", since = "1.87.0")]
342    #[inline]
343    pub const fn is_digit(self, radix: u32) -> bool {
344        self.to_digit(radix).is_some()
345    }
346
347    /// Converts a `char` to a digit in the given radix.
348    ///
349    /// A 'radix' here is sometimes also called a 'base'. A radix of two
350    /// indicates a binary number, a radix of ten, decimal, and a radix of
351    /// sixteen, hexadecimal, to give some common values. Arbitrary
352    /// radices are supported.
353    ///
354    /// 'Digit' is defined to be only the following characters:
355    ///
356    /// * `0-9`
357    /// * `a-z`
358    /// * `A-Z`
359    ///
360    /// # Errors
361    ///
362    /// Returns `None` if the `char` does not refer to a digit in the given radix.
363    ///
364    /// # Panics
365    ///
366    /// Panics if given a radix smaller than 2 or larger than 36.
367    ///
368    /// # Examples
369    ///
370    /// Basic usage:
371    ///
372    /// ```
373    /// assert_eq!('1'.to_digit(10), Some(1));
374    /// assert_eq!('f'.to_digit(16), Some(15));
375    /// ```
376    ///
377    /// Passing a non-digit results in failure:
378    ///
379    /// ```
380    /// assert_eq!('f'.to_digit(10), None);
381    /// assert_eq!('z'.to_digit(16), None);
382    /// ```
383    ///
384    /// Passing a large radix, causing a panic:
385    ///
386    /// ```should_panic
387    /// // this panics
388    /// let _ = '1'.to_digit(37);
389    /// ```
390    /// Passing a small radix, causing a panic:
391    ///
392    /// ```should_panic
393    /// // this panics
394    /// let _ = '1'.to_digit(1);
395    /// ```
396    #[stable(feature = "rust1", since = "1.0.0")]
397    #[rustc_const_stable(feature = "const_char_convert", since = "1.67.0")]
398    #[rustc_diagnostic_item = "char_to_digit"]
399    #[must_use = "this returns the result of the operation, \
400                  without modifying the original"]
401    #[inline]
402    pub const fn to_digit(self, radix: u32) -> Option<u32> {
403        assert!(
404            radix >= 2 && radix <= 36,
405            "to_digit: invalid radix -- radix must be in the range 2 to 36 inclusive"
406        );
407        // check radix to remove letter handling code when radix is a known constant
408        let value = if self > '9' && radix > 10 {
409            // mask to convert ASCII letters to uppercase
410            const TO_UPPERCASE_MASK: u32 = !0b0010_0000;
411            // Converts an ASCII letter to its corresponding integer value:
412            // A-Z => 10-35, a-z => 10-35. Other characters produce values >= 36.
413            //
414            // Add Overflow Safety:
415            // By applying the mask after the subtraction, the first addendum is
416            // constrained such that it never exceeds u32::MAX - 0x20.
417            ((self as u32).wrapping_sub('A' as u32) & TO_UPPERCASE_MASK) + 10
418        } else {
419            // convert digit to value, non-digits wrap to values > 36
420            (self as u32).wrapping_sub('0' as u32)
421        };
422        // FIXME(const-hack): once then_some is const fn, use it here
423        if value < radix { Some(value) } else { None }
424    }
425
426    /// Returns an iterator that yields the hexadecimal Unicode escape of a
427    /// character as `char`s.
428    ///
429    /// This will escape characters with the Rust syntax of the form
430    /// `\u{NNNNNN}` where `NNNNNN` is a hexadecimal representation.
431    ///
432    /// # Examples
433    ///
434    /// As an iterator:
435    ///
436    /// ```
437    /// for c in '❤'.escape_unicode() {
438    ///     print!("{c}");
439    /// }
440    /// println!();
441    /// ```
442    ///
443    /// Using `println!` directly:
444    ///
445    /// ```
446    /// println!("{}", '❤'.escape_unicode());
447    /// ```
448    ///
449    /// Both are equivalent to:
450    ///
451    /// ```
452    /// println!("\\u{{2764}}");
453    /// ```
454    ///
455    /// Using [`to_string`](../std/string/trait.ToString.html#tymethod.to_string):
456    ///
457    /// ```
458    /// assert_eq!('❤'.escape_unicode().to_string(), "\\u{2764}");
459    /// ```
460    #[must_use = "this returns the escaped char as an iterator, \
461                  without modifying the original"]
462    #[stable(feature = "rust1", since = "1.0.0")]
463    #[inline]
464    pub fn escape_unicode(self) -> EscapeUnicode {
465        EscapeUnicode::new(self)
466    }
467
468    /// An extended version of `escape_debug` that optionally permits escaping
469    /// Extended Grapheme codepoints, single quotes, and double quotes. This
470    /// allows us to format characters like nonspacing marks better when they're
471    /// at the start of a string, and allows escaping single quotes in
472    /// characters, and double quotes in strings.
473    #[inline]
474    pub(crate) fn escape_debug_ext(self, args: EscapeDebugExtArgs) -> EscapeDebug {
475        match self {
476            '\0' => EscapeDebug::backslash(ascii::Char::Digit0),
477            '\t' => EscapeDebug::backslash(ascii::Char::SmallT),
478            '\r' => EscapeDebug::backslash(ascii::Char::SmallR),
479            '\n' => EscapeDebug::backslash(ascii::Char::SmallN),
480            '\\' => EscapeDebug::backslash(ascii::Char::ReverseSolidus),
481            '\"' if args.escape_double_quote => EscapeDebug::backslash(ascii::Char::QuotationMark),
482            '\'' if args.escape_single_quote => EscapeDebug::backslash(ascii::Char::Apostrophe),
483            _ if args.escape_grapheme_extended && self.is_grapheme_extended() => {
484                EscapeDebug::unicode(self)
485            }
486            _ if is_printable(self) => EscapeDebug::printable(self),
487            _ => EscapeDebug::unicode(self),
488        }
489    }
490
491    /// Returns an iterator that yields the literal escape code of a character
492    /// as `char`s.
493    ///
494    /// This will escape the characters similar to the [`Debug`](core::fmt::Debug) implementations
495    /// of `str` or `char`.
496    ///
497    /// # Examples
498    ///
499    /// As an iterator:
500    ///
501    /// ```
502    /// for c in '\n'.escape_debug() {
503    ///     print!("{c}");
504    /// }
505    /// println!();
506    /// ```
507    ///
508    /// Using `println!` directly:
509    ///
510    /// ```
511    /// println!("{}", '\n'.escape_debug());
512    /// ```
513    ///
514    /// Both are equivalent to:
515    ///
516    /// ```
517    /// println!("\\n");
518    /// ```
519    ///
520    /// Using [`to_string`](../std/string/trait.ToString.html#tymethod.to_string):
521    ///
522    /// ```
523    /// assert_eq!('\n'.escape_debug().to_string(), "\\n");
524    /// ```
525    #[must_use = "this returns the escaped char as an iterator, \
526                  without modifying the original"]
527    #[stable(feature = "char_escape_debug", since = "1.20.0")]
528    #[inline]
529    pub fn escape_debug(self) -> EscapeDebug {
530        self.escape_debug_ext(EscapeDebugExtArgs::ESCAPE_ALL)
531    }
532
533    /// Returns an iterator that yields the literal escape code of a character
534    /// as `char`s.
535    ///
536    /// The default is chosen with a bias toward producing literals that are
537    /// legal in a variety of languages, including C++11 and similar C-family
538    /// languages. The exact rules are:
539    ///
540    /// * Tab is escaped as `\t`.
541    /// * Carriage return is escaped as `\r`.
542    /// * Line feed is escaped as `\n`.
543    /// * Single quote is escaped as `\'`.
544    /// * Double quote is escaped as `\"`.
545    /// * Backslash is escaped as `\\`.
546    /// * Any character in the 'printable ASCII' range `0x20` .. `0x7e`
547    ///   inclusive is not escaped.
548    /// * All other characters are given hexadecimal Unicode escapes; see
549    ///   [`escape_unicode`].
550    ///
551    /// [`escape_unicode`]: #method.escape_unicode
552    ///
553    /// # Examples
554    ///
555    /// As an iterator:
556    ///
557    /// ```
558    /// for c in '"'.escape_default() {
559    ///     print!("{c}");
560    /// }
561    /// println!();
562    /// ```
563    ///
564    /// Using `println!` directly:
565    ///
566    /// ```
567    /// println!("{}", '"'.escape_default());
568    /// ```
569    ///
570    /// Both are equivalent to:
571    ///
572    /// ```
573    /// println!("\\\"");
574    /// ```
575    ///
576    /// Using [`to_string`](../std/string/trait.ToString.html#tymethod.to_string):
577    ///
578    /// ```
579    /// assert_eq!('"'.escape_default().to_string(), "\\\"");
580    /// ```
581    #[must_use = "this returns the escaped char as an iterator, \
582                  without modifying the original"]
583    #[stable(feature = "rust1", since = "1.0.0")]
584    #[inline]
585    pub fn escape_default(self) -> EscapeDefault {
586        match self {
587            '\t' => EscapeDefault::backslash(ascii::Char::SmallT),
588            '\r' => EscapeDefault::backslash(ascii::Char::SmallR),
589            '\n' => EscapeDefault::backslash(ascii::Char::SmallN),
590            '\\' | '\'' | '\"' => EscapeDefault::backslash(self.as_ascii().unwrap()),
591            '\x20'..='\x7e' => EscapeDefault::printable(self.as_ascii().unwrap()),
592            _ => EscapeDefault::unicode(self),
593        }
594    }
595
596    /// Returns the number of bytes this `char` would need if encoded in UTF-8.
597    ///
598    /// That number of bytes is always between 1 and 4, inclusive.
599    ///
600    /// # Examples
601    ///
602    /// Basic usage:
603    ///
604    /// ```
605    /// let len = 'A'.len_utf8();
606    /// assert_eq!(len, 1);
607    ///
608    /// let len = 'ß'.len_utf8();
609    /// assert_eq!(len, 2);
610    ///
611    /// let len = 'ℝ'.len_utf8();
612    /// assert_eq!(len, 3);
613    ///
614    /// let len = '💣'.len_utf8();
615    /// assert_eq!(len, 4);
616    /// ```
617    ///
618    /// The `&str` type guarantees that its contents are UTF-8, and so we can compare the length it
619    /// would take if each code point was represented as a `char` vs in the `&str` itself:
620    ///
621    /// ```
622    /// // as chars
623    /// let eastern = '東';
624    /// let capital = '京';
625    ///
626    /// // both can be represented as three bytes
627    /// assert_eq!(3, eastern.len_utf8());
628    /// assert_eq!(3, capital.len_utf8());
629    ///
630    /// // as a &str, these two are encoded in UTF-8
631    /// let tokyo = "東京";
632    ///
633    /// let len = eastern.len_utf8() + capital.len_utf8();
634    ///
635    /// // we can see that they take six bytes total...
636    /// assert_eq!(6, tokyo.len());
637    ///
638    /// // ... just like the &str
639    /// assert_eq!(len, tokyo.len());
640    /// ```
641    #[stable(feature = "rust1", since = "1.0.0")]
642    #[rustc_const_stable(feature = "const_char_len_utf", since = "1.52.0")]
643    #[inline]
644    #[must_use]
645    pub const fn len_utf8(self) -> usize {
646        len_utf8(self as u32)
647    }
648
649    /// Returns the number of 16-bit code units this `char` would need if
650    /// encoded in UTF-16.
651    ///
652    /// That number of code units is always either 1 or 2, for unicode scalar values in
653    /// the [basic multilingual plane] or [supplementary planes] respectively.
654    ///
655    /// See the documentation for [`len_utf8()`] for more explanation of this
656    /// concept. This function is a mirror, but for UTF-16 instead of UTF-8.
657    ///
658    /// [basic multilingual plane]: http://www.unicode.org/glossary/#basic_multilingual_plane
659    /// [supplementary planes]: http://www.unicode.org/glossary/#supplementary_planes
660    /// [`len_utf8()`]: #method.len_utf8
661    ///
662    /// # Examples
663    ///
664    /// Basic usage:
665    ///
666    /// ```
667    /// let n = 'ß'.len_utf16();
668    /// assert_eq!(n, 1);
669    ///
670    /// let len = '💣'.len_utf16();
671    /// assert_eq!(len, 2);
672    /// ```
673    #[stable(feature = "rust1", since = "1.0.0")]
674    #[rustc_const_stable(feature = "const_char_len_utf", since = "1.52.0")]
675    #[inline]
676    #[must_use]
677    pub const fn len_utf16(self) -> usize {
678        len_utf16(self as u32)
679    }
680
681    /// Encodes this character as UTF-8 into the provided byte buffer,
682    /// and then returns the subslice of the buffer that contains the encoded character.
683    ///
684    /// # Panics
685    ///
686    /// Panics if the buffer is not large enough.
687    /// A buffer of length four is large enough to encode any `char`.
688    ///
689    /// # Examples
690    ///
691    /// In both of these examples, 'ß' takes two bytes to encode.
692    ///
693    /// ```
694    /// let mut b = [0; 2];
695    ///
696    /// let result = 'ß'.encode_utf8(&mut b);
697    ///
698    /// assert_eq!(result, "ß");
699    ///
700    /// assert_eq!(result.len(), 2);
701    /// ```
702    ///
703    /// A buffer that's too small:
704    ///
705    /// ```should_panic
706    /// let mut b = [0; 1];
707    ///
708    /// // this panics
709    /// 'ß'.encode_utf8(&mut b);
710    /// ```
711    #[stable(feature = "unicode_encode_char", since = "1.15.0")]
712    #[rustc_const_stable(feature = "const_char_encode_utf8", since = "1.83.0")]
713    #[inline]
714    pub const fn encode_utf8(self, dst: &mut [u8]) -> &mut str {
715        // SAFETY: `char` is not a surrogate, so this is valid UTF-8.
716        unsafe { from_utf8_unchecked_mut(encode_utf8_raw(self as u32, dst)) }
717    }
718
719    /// Encodes this character as native endian UTF-16 into the provided `u16` buffer,
720    /// and then returns the subslice of the buffer that contains the encoded character.
721    ///
722    /// # Panics
723    ///
724    /// Panics if the buffer is not large enough.
725    /// A buffer of length 2 is large enough to encode any `char`.
726    ///
727    /// # Examples
728    ///
729    /// In both of these examples, '𝕊' takes two `u16`s to encode.
730    ///
731    /// ```
732    /// let mut b = [0; 2];
733    ///
734    /// let result = '𝕊'.encode_utf16(&mut b);
735    ///
736    /// assert_eq!(result.len(), 2);
737    /// ```
738    ///
739    /// A buffer that's too small:
740    ///
741    /// ```should_panic
742    /// let mut b = [0; 1];
743    ///
744    /// // this panics
745    /// '𝕊'.encode_utf16(&mut b);
746    /// ```
747    #[stable(feature = "unicode_encode_char", since = "1.15.0")]
748    #[rustc_const_stable(feature = "const_char_encode_utf16", since = "1.84.0")]
749    #[inline]
750    pub const fn encode_utf16(self, dst: &mut [u16]) -> &mut [u16] {
751        encode_utf16_raw(self as u32, dst)
752    }
753
754    /// Returns `true` if this `char` has the `Alphabetic` property.
755    ///
756    /// `Alphabetic` is described in Chapter 4 (Character Properties) of the [Unicode Standard] and
757    /// specified in the [Unicode Character Database][ucd] [`DerivedCoreProperties.txt`].
758    ///
759    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
760    /// [ucd]: https://www.unicode.org/reports/tr44/
761    /// [`DerivedCoreProperties.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt
762    ///
763    /// # Examples
764    ///
765    /// Basic usage:
766    ///
767    /// ```
768    /// assert!('a'.is_alphabetic());
769    /// assert!('京'.is_alphabetic());
770    ///
771    /// let c = '💝';
772    /// // love is many things, but it is not alphabetic
773    /// assert!(!c.is_alphabetic());
774    /// ```
775    #[must_use]
776    #[stable(feature = "rust1", since = "1.0.0")]
777    #[inline]
778    pub fn is_alphabetic(self) -> bool {
779        match self {
780            'a'..='z' | 'A'..='Z' => true,
781            c => c > '\x7f' && unicode::Alphabetic(c),
782        }
783    }
784
785    /// Returns `true` if this `char` has the `Lowercase` property.
786    ///
787    /// `Lowercase` is described in Chapter 4 (Character Properties) of the [Unicode Standard] and
788    /// specified in the [Unicode Character Database][ucd] [`DerivedCoreProperties.txt`].
789    ///
790    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
791    /// [ucd]: https://www.unicode.org/reports/tr44/
792    /// [`DerivedCoreProperties.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt
793    ///
794    /// # Examples
795    ///
796    /// Basic usage:
797    ///
798    /// ```
799    /// assert!('a'.is_lowercase());
800    /// assert!('δ'.is_lowercase());
801    /// assert!(!'A'.is_lowercase());
802    /// assert!(!'Δ'.is_lowercase());
803    ///
804    /// // The various Chinese scripts and punctuation do not have case, and so:
805    /// assert!(!'中'.is_lowercase());
806    /// assert!(!' '.is_lowercase());
807    /// ```
808    ///
809    /// In a const context:
810    ///
811    /// ```
812    /// const CAPITAL_DELTA_IS_LOWERCASE: bool = 'Δ'.is_lowercase();
813    /// assert!(!CAPITAL_DELTA_IS_LOWERCASE);
814    /// ```
815    #[must_use]
816    #[stable(feature = "rust1", since = "1.0.0")]
817    #[rustc_const_stable(feature = "const_unicode_case_lookup", since = "1.84.0")]
818    #[inline]
819    pub const fn is_lowercase(self) -> bool {
820        match self {
821            'a'..='z' => true,
822            c => c > '\x7f' && unicode::Lowercase(c),
823        }
824    }
825
826    /// Returns `true` if this `char` has the `Uppercase` property.
827    ///
828    /// `Uppercase` is described in Chapter 4 (Character Properties) of the [Unicode Standard] and
829    /// specified in the [Unicode Character Database][ucd] [`DerivedCoreProperties.txt`].
830    ///
831    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
832    /// [ucd]: https://www.unicode.org/reports/tr44/
833    /// [`DerivedCoreProperties.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt
834    ///
835    /// # Examples
836    ///
837    /// Basic usage:
838    ///
839    /// ```
840    /// assert!(!'a'.is_uppercase());
841    /// assert!(!'δ'.is_uppercase());
842    /// assert!('A'.is_uppercase());
843    /// assert!('Δ'.is_uppercase());
844    ///
845    /// // The various Chinese scripts and punctuation do not have case, and so:
846    /// assert!(!'中'.is_uppercase());
847    /// assert!(!' '.is_uppercase());
848    /// ```
849    ///
850    /// In a const context:
851    ///
852    /// ```
853    /// const CAPITAL_DELTA_IS_UPPERCASE: bool = 'Δ'.is_uppercase();
854    /// assert!(CAPITAL_DELTA_IS_UPPERCASE);
855    /// ```
856    #[must_use]
857    #[stable(feature = "rust1", since = "1.0.0")]
858    #[rustc_const_stable(feature = "const_unicode_case_lookup", since = "1.84.0")]
859    #[inline]
860    pub const fn is_uppercase(self) -> bool {
861        match self {
862            'A'..='Z' => true,
863            c => c > '\x7f' && unicode::Uppercase(c),
864        }
865    }
866
867    /// Returns `true` if this `char` has the `White_Space` property.
868    ///
869    /// `White_Space` is specified in the [Unicode Character Database][ucd] [`PropList.txt`].
870    ///
871    /// [ucd]: https://www.unicode.org/reports/tr44/
872    /// [`PropList.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
873    ///
874    /// # Examples
875    ///
876    /// Basic usage:
877    ///
878    /// ```
879    /// assert!(' '.is_whitespace());
880    ///
881    /// // line break
882    /// assert!('\n'.is_whitespace());
883    ///
884    /// // a non-breaking space
885    /// assert!('\u{A0}'.is_whitespace());
886    ///
887    /// assert!(!'越'.is_whitespace());
888    /// ```
889    #[must_use]
890    #[stable(feature = "rust1", since = "1.0.0")]
891    #[rustc_const_stable(feature = "const_char_classify", since = "1.87.0")]
892    #[inline]
893    pub const fn is_whitespace(self) -> bool {
894        match self {
895            ' ' | '\x09'..='\x0d' => true,
896            c => c > '\x7f' && unicode::White_Space(c),
897        }
898    }
899
900    /// Returns `true` if this `char` satisfies either [`is_alphabetic()`] or [`is_numeric()`].
901    ///
902    /// [`is_alphabetic()`]: #method.is_alphabetic
903    /// [`is_numeric()`]: #method.is_numeric
904    ///
905    /// # Examples
906    ///
907    /// Basic usage:
908    ///
909    /// ```
910    /// assert!('٣'.is_alphanumeric());
911    /// assert!('7'.is_alphanumeric());
912    /// assert!('৬'.is_alphanumeric());
913    /// assert!('¾'.is_alphanumeric());
914    /// assert!('①'.is_alphanumeric());
915    /// assert!('K'.is_alphanumeric());
916    /// assert!('و'.is_alphanumeric());
917    /// assert!('藏'.is_alphanumeric());
918    /// ```
919    #[must_use]
920    #[stable(feature = "rust1", since = "1.0.0")]
921    #[inline]
922    pub fn is_alphanumeric(self) -> bool {
923        if self.is_ascii() {
924            self.is_ascii_alphanumeric()
925        } else {
926            unicode::Alphabetic(self) || unicode::N(self)
927        }
928    }
929
930    /// Returns `true` if this `char` has the general category for control codes.
931    ///
932    /// Control codes (code points with the general category of `Cc`) are described in Chapter 4
933    /// (Character Properties) of the [Unicode Standard] and specified in the [Unicode Character
934    /// Database][ucd] [`UnicodeData.txt`].
935    ///
936    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
937    /// [ucd]: https://www.unicode.org/reports/tr44/
938    /// [`UnicodeData.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt
939    ///
940    /// # Examples
941    ///
942    /// Basic usage:
943    ///
944    /// ```
945    /// // U+009C, STRING TERMINATOR
946    /// assert!(''.is_control());
947    /// assert!(!'q'.is_control());
948    /// ```
949    #[must_use]
950    #[stable(feature = "rust1", since = "1.0.0")]
951    #[inline]
952    pub fn is_control(self) -> bool {
953        // According to
954        // https://www.unicode.org/policies/stability_policy.html#Property_Value,
955        // the set of codepoints in `Cc` will never change.
956        // So we can just hard-code the patterns to match against instead of using a table.
957        matches!(self, '\0'..='\x1f' | '\x7f'..='\u{9f}')
958    }
959
960    /// Returns `true` if this `char` has the `Grapheme_Extend` property.
961    ///
962    /// `Grapheme_Extend` is described in [Unicode Standard Annex #29 (Unicode Text
963    /// Segmentation)][uax29] and specified in the [Unicode Character Database][ucd]
964    /// [`DerivedCoreProperties.txt`].
965    ///
966    /// [uax29]: https://www.unicode.org/reports/tr29/
967    /// [ucd]: https://www.unicode.org/reports/tr44/
968    /// [`DerivedCoreProperties.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt
969    #[must_use]
970    #[inline]
971    pub(crate) fn is_grapheme_extended(self) -> bool {
972        !self.is_ascii() && unicode::Grapheme_Extend(self)
973    }
974
975    /// Returns `true` if this `char` has the `Cased` property.
976    ///
977    /// `Cased` is described in Chapter 4 (Character Properties) of the [Unicode Standard] and
978    /// specified in the [Unicode Character Database][ucd] [`DerivedCoreProperties.txt`].
979    ///
980    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
981    /// [ucd]: https://www.unicode.org/reports/tr44/
982    /// [`DerivedCoreProperties.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt
983    #[must_use]
984    #[inline]
985    #[doc(hidden)]
986    #[unstable(feature = "char_internals", reason = "exposed only for libstd", issue = "none")]
987    pub fn is_cased(self) -> bool {
988        if self.is_ascii() { self.is_ascii_alphabetic() } else { unicode::Cased(self) }
989    }
990
991    /// Returns `true` if this `char` has the `Case_Ignorable` property.
992    ///
993    /// `Case_Ignorable` is described in Chapter 4 (Character Properties) of the [Unicode Standard] and
994    /// specified in the [Unicode Character Database][ucd] [`DerivedCoreProperties.txt`].
995    ///
996    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
997    /// [ucd]: https://www.unicode.org/reports/tr44/
998    /// [`DerivedCoreProperties.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/DerivedCoreProperties.txt
999    #[must_use]
1000    #[inline]
1001    #[doc(hidden)]
1002    #[unstable(feature = "char_internals", reason = "exposed only for libstd", issue = "none")]
1003    pub fn is_case_ignorable(self) -> bool {
1004        if self.is_ascii() {
1005            matches!(self, '\'' | '.' | ':' | '^' | '`')
1006        } else {
1007            unicode::Case_Ignorable(self)
1008        }
1009    }
1010
1011    /// Returns `true` if this `char` has one of the general categories for numbers.
1012    ///
1013    /// The general categories for numbers (`Nd` for decimal digits, `Nl` for letter-like numeric
1014    /// characters, and `No` for other numeric characters) are specified in the [Unicode Character
1015    /// Database][ucd] [`UnicodeData.txt`].
1016    ///
1017    /// This method doesn't cover everything that could be considered a number, e.g. ideographic numbers like '三'.
1018    /// If you want everything including characters with overlapping purposes then you might want to use
1019    /// a unicode or language-processing library that exposes the appropriate character properties instead
1020    /// of looking at the unicode categories.
1021    ///
1022    /// If you want to parse ASCII decimal digits (0-9) or ASCII base-N, use
1023    /// `is_ascii_digit` or `is_digit` instead.
1024    ///
1025    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
1026    /// [ucd]: https://www.unicode.org/reports/tr44/
1027    /// [`UnicodeData.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt
1028    ///
1029    /// # Examples
1030    ///
1031    /// Basic usage:
1032    ///
1033    /// ```
1034    /// assert!('٣'.is_numeric());
1035    /// assert!('7'.is_numeric());
1036    /// assert!('৬'.is_numeric());
1037    /// assert!('¾'.is_numeric());
1038    /// assert!('①'.is_numeric());
1039    /// assert!(!'K'.is_numeric());
1040    /// assert!(!'و'.is_numeric());
1041    /// assert!(!'藏'.is_numeric());
1042    /// assert!(!'三'.is_numeric());
1043    /// ```
1044    #[must_use]
1045    #[stable(feature = "rust1", since = "1.0.0")]
1046    #[inline]
1047    pub fn is_numeric(self) -> bool {
1048        match self {
1049            '0'..='9' => true,
1050            c => c > '\x7f' && unicode::N(c),
1051        }
1052    }
1053
1054    /// Returns an iterator that yields the lowercase mapping of this `char` as one or more
1055    /// `char`s.
1056    ///
1057    /// If this `char` does not have a lowercase mapping, the iterator yields the same `char`.
1058    ///
1059    /// If this `char` has a one-to-one lowercase mapping given by the [Unicode Character
1060    /// Database][ucd] [`UnicodeData.txt`], the iterator yields that `char`.
1061    ///
1062    /// [ucd]: https://www.unicode.org/reports/tr44/
1063    /// [`UnicodeData.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt
1064    ///
1065    /// If this `char` requires special considerations (e.g. multiple `char`s) the iterator yields
1066    /// the `char`(s) given by [`SpecialCasing.txt`].
1067    ///
1068    /// [`SpecialCasing.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/SpecialCasing.txt
1069    ///
1070    /// This operation performs an unconditional mapping without tailoring. That is, the conversion
1071    /// is independent of context and language.
1072    ///
1073    /// In the [Unicode Standard], Chapter 4 (Character Properties) discusses case mapping in
1074    /// general and Chapter 3 (Conformance) discusses the default algorithm for case conversion.
1075    ///
1076    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
1077    ///
1078    /// # Examples
1079    ///
1080    /// As an iterator:
1081    ///
1082    /// ```
1083    /// for c in 'İ'.to_lowercase() {
1084    ///     print!("{c}");
1085    /// }
1086    /// println!();
1087    /// ```
1088    ///
1089    /// Using `println!` directly:
1090    ///
1091    /// ```
1092    /// println!("{}", 'İ'.to_lowercase());
1093    /// ```
1094    ///
1095    /// Both are equivalent to:
1096    ///
1097    /// ```
1098    /// println!("i\u{307}");
1099    /// ```
1100    ///
1101    /// Using [`to_string`](../std/string/trait.ToString.html#tymethod.to_string):
1102    ///
1103    /// ```
1104    /// assert_eq!('C'.to_lowercase().to_string(), "c");
1105    ///
1106    /// // Sometimes the result is more than one character:
1107    /// assert_eq!('İ'.to_lowercase().to_string(), "i\u{307}");
1108    ///
1109    /// // Characters that do not have both uppercase and lowercase
1110    /// // convert into themselves.
1111    /// assert_eq!('山'.to_lowercase().to_string(), "山");
1112    /// ```
1113    #[must_use = "this returns the lowercase character as a new iterator, \
1114                  without modifying the original"]
1115    #[stable(feature = "rust1", since = "1.0.0")]
1116    #[inline]
1117    pub fn to_lowercase(self) -> ToLowercase {
1118        ToLowercase(CaseMappingIter::new(conversions::to_lower(self)))
1119    }
1120
1121    /// Returns an iterator that yields the uppercase mapping of this `char` as one or more
1122    /// `char`s.
1123    ///
1124    /// If this `char` does not have an uppercase mapping, the iterator yields the same `char`.
1125    ///
1126    /// If this `char` has a one-to-one uppercase mapping given by the [Unicode Character
1127    /// Database][ucd] [`UnicodeData.txt`], the iterator yields that `char`.
1128    ///
1129    /// [ucd]: https://www.unicode.org/reports/tr44/
1130    /// [`UnicodeData.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt
1131    ///
1132    /// If this `char` requires special considerations (e.g. multiple `char`s) the iterator yields
1133    /// the `char`(s) given by [`SpecialCasing.txt`].
1134    ///
1135    /// [`SpecialCasing.txt`]: https://www.unicode.org/Public/UCD/latest/ucd/SpecialCasing.txt
1136    ///
1137    /// This operation performs an unconditional mapping without tailoring. That is, the conversion
1138    /// is independent of context and language.
1139    ///
1140    /// In the [Unicode Standard], Chapter 4 (Character Properties) discusses case mapping in
1141    /// general and Chapter 3 (Conformance) discusses the default algorithm for case conversion.
1142    ///
1143    /// [Unicode Standard]: https://www.unicode.org/versions/latest/
1144    ///
1145    /// # Examples
1146    /// `'ﬅ'` (U+FB05) is a single Unicode code point (a ligature) that maps to "ST" in uppercase.
1147    ///
1148    /// As an iterator:
1149    ///
1150    /// ```
1151    /// for c in 'ﬅ'.to_uppercase() {
1152    ///     print!("{c}");
1153    /// }
1154    /// println!();
1155    /// ```
1156    ///
1157    /// Using `println!` directly:
1158    ///
1159    /// ```
1160    /// println!("{}", 'ﬅ'.to_uppercase());
1161    /// ```
1162    ///
1163    /// Both are equivalent to:
1164    ///
1165    /// ```
1166    /// println!("ST");
1167    /// ```
1168    ///
1169    /// Using [`to_string`](../std/string/trait.ToString.html#tymethod.to_string):
1170    ///
1171    /// ```
1172    /// assert_eq!('c'.to_uppercase().to_string(), "C");
1173    ///
1174    /// // Sometimes the result is more than one character:
1175    /// assert_eq!('ﬅ'.to_uppercase().to_string(), "ST");
1176    ///
1177    /// // Characters that do not have both uppercase and lowercase
1178    /// // convert into themselves.
1179    /// assert_eq!('山'.to_uppercase().to_string(), "山");
1180    /// ```
1181    ///
1182    /// # Note on locale
1183    ///
1184    /// In Turkish, the equivalent of 'i' in Latin has five forms instead of two:
1185    ///
1186    /// * 'Dotless': I / ı, sometimes written ï
1187    /// * 'Dotted': İ / i
1188    ///
1189    /// Note that the lowercase dotted 'i' is the same as the Latin. Therefore:
1190    ///
1191    /// ```
1192    /// let upper_i = 'i'.to_uppercase().to_string();
1193    /// ```
1194    ///
1195    /// The value of `upper_i` here relies on the language of the text: if we're
1196    /// in `en-US`, it should be `"I"`, but if we're in `tr_TR`, it should
1197    /// be `"İ"`. `to_uppercase()` does not take this into account, and so:
1198    ///
1199    /// ```
1200    /// let upper_i = 'i'.to_uppercase().to_string();
1201    ///
1202    /// assert_eq!(upper_i, "I");
1203    /// ```
1204    ///
1205    /// holds across languages.
1206    #[must_use = "this returns the uppercase character as a new iterator, \
1207                  without modifying the original"]
1208    #[stable(feature = "rust1", since = "1.0.0")]
1209    #[inline]
1210    pub fn to_uppercase(self) -> ToUppercase {
1211        ToUppercase(CaseMappingIter::new(conversions::to_upper(self)))
1212    }
1213
1214    /// Checks if the value is within the ASCII range.
1215    ///
1216    /// # Examples
1217    ///
1218    /// ```
1219    /// let ascii = 'a';
1220    /// let non_ascii = '❤';
1221    ///
1222    /// assert!(ascii.is_ascii());
1223    /// assert!(!non_ascii.is_ascii());
1224    /// ```
1225    #[must_use]
1226    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
1227    #[rustc_const_stable(feature = "const_char_is_ascii", since = "1.32.0")]
1228    #[rustc_diagnostic_item = "char_is_ascii"]
1229    #[inline]
1230    pub const fn is_ascii(&self) -> bool {
1231        *self as u32 <= 0x7F
1232    }
1233
1234    /// Returns `Some` if the value is within the ASCII range,
1235    /// or `None` if it's not.
1236    ///
1237    /// This is preferred to [`Self::is_ascii`] when you're passing the value
1238    /// along to something else that can take [`ascii::Char`] rather than
1239    /// needing to check again for itself whether the value is in ASCII.
1240    #[must_use]
1241    #[unstable(feature = "ascii_char", issue = "110998")]
1242    #[inline]
1243    pub const fn as_ascii(&self) -> Option<ascii::Char> {
1244        if self.is_ascii() {
1245            // SAFETY: Just checked that this is ASCII.
1246            Some(unsafe { ascii::Char::from_u8_unchecked(*self as u8) })
1247        } else {
1248            None
1249        }
1250    }
1251
1252    /// Converts this char into an [ASCII character](`ascii::Char`), without
1253    /// checking whether it is valid.
1254    ///
1255    /// # Safety
1256    ///
1257    /// This char must be within the ASCII range, or else this is UB.
1258    #[must_use]
1259    #[unstable(feature = "ascii_char", issue = "110998")]
1260    #[inline]
1261    pub const unsafe fn as_ascii_unchecked(&self) -> ascii::Char {
1262        assert_unsafe_precondition!(
1263            check_library_ub,
1264            "as_ascii_unchecked requires that the char is valid ASCII",
1265            (it: &char = self) => it.is_ascii()
1266        );
1267
1268        // SAFETY: the caller promised that this char is ASCII.
1269        unsafe { ascii::Char::from_u8_unchecked(*self as u8) }
1270    }
1271
1272    /// Makes a copy of the value in its ASCII upper case equivalent.
1273    ///
1274    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
1275    /// but non-ASCII letters are unchanged.
1276    ///
1277    /// To uppercase the value in-place, use [`make_ascii_uppercase()`].
1278    ///
1279    /// To uppercase ASCII characters in addition to non-ASCII characters, use
1280    /// [`to_uppercase()`].
1281    ///
1282    /// # Examples
1283    ///
1284    /// ```
1285    /// let ascii = 'a';
1286    /// let non_ascii = '❤';
1287    ///
1288    /// assert_eq!('A', ascii.to_ascii_uppercase());
1289    /// assert_eq!('❤', non_ascii.to_ascii_uppercase());
1290    /// ```
1291    ///
1292    /// [`make_ascii_uppercase()`]: #method.make_ascii_uppercase
1293    /// [`to_uppercase()`]: #method.to_uppercase
1294    #[must_use = "to uppercase the value in-place, use `make_ascii_uppercase()`"]
1295    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
1296    #[rustc_const_stable(feature = "const_ascii_methods_on_intrinsics", since = "1.52.0")]
1297    #[inline]
1298    pub const fn to_ascii_uppercase(&self) -> char {
1299        if self.is_ascii_lowercase() {
1300            (*self as u8).ascii_change_case_unchecked() as char
1301        } else {
1302            *self
1303        }
1304    }
1305
1306    /// Makes a copy of the value in its ASCII lower case equivalent.
1307    ///
1308    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
1309    /// but non-ASCII letters are unchanged.
1310    ///
1311    /// To lowercase the value in-place, use [`make_ascii_lowercase()`].
1312    ///
1313    /// To lowercase ASCII characters in addition to non-ASCII characters, use
1314    /// [`to_lowercase()`].
1315    ///
1316    /// # Examples
1317    ///
1318    /// ```
1319    /// let ascii = 'A';
1320    /// let non_ascii = '❤';
1321    ///
1322    /// assert_eq!('a', ascii.to_ascii_lowercase());
1323    /// assert_eq!('❤', non_ascii.to_ascii_lowercase());
1324    /// ```
1325    ///
1326    /// [`make_ascii_lowercase()`]: #method.make_ascii_lowercase
1327    /// [`to_lowercase()`]: #method.to_lowercase
1328    #[must_use = "to lowercase the value in-place, use `make_ascii_lowercase()`"]
1329    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
1330    #[rustc_const_stable(feature = "const_ascii_methods_on_intrinsics", since = "1.52.0")]
1331    #[inline]
1332    pub const fn to_ascii_lowercase(&self) -> char {
1333        if self.is_ascii_uppercase() {
1334            (*self as u8).ascii_change_case_unchecked() as char
1335        } else {
1336            *self
1337        }
1338    }
1339
1340    /// Checks that two values are an ASCII case-insensitive match.
1341    ///
1342    /// Equivalent to <code>[to_ascii_lowercase]\(a) == [to_ascii_lowercase]\(b)</code>.
1343    ///
1344    /// # Examples
1345    ///
1346    /// ```
1347    /// let upper_a = 'A';
1348    /// let lower_a = 'a';
1349    /// let lower_z = 'z';
1350    ///
1351    /// assert!(upper_a.eq_ignore_ascii_case(&lower_a));
1352    /// assert!(upper_a.eq_ignore_ascii_case(&upper_a));
1353    /// assert!(!upper_a.eq_ignore_ascii_case(&lower_z));
1354    /// ```
1355    ///
1356    /// [to_ascii_lowercase]: #method.to_ascii_lowercase
1357    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
1358    #[rustc_const_stable(feature = "const_ascii_methods_on_intrinsics", since = "1.52.0")]
1359    #[inline]
1360    pub const fn eq_ignore_ascii_case(&self, other: &char) -> bool {
1361        self.to_ascii_lowercase() == other.to_ascii_lowercase()
1362    }
1363
1364    /// Converts this type to its ASCII upper case equivalent in-place.
1365    ///
1366    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
1367    /// but non-ASCII letters are unchanged.
1368    ///
1369    /// To return a new uppercased value without modifying the existing one, use
1370    /// [`to_ascii_uppercase()`].
1371    ///
1372    /// # Examples
1373    ///
1374    /// ```
1375    /// let mut ascii = 'a';
1376    ///
1377    /// ascii.make_ascii_uppercase();
1378    ///
1379    /// assert_eq!('A', ascii);
1380    /// ```
1381    ///
1382    /// [`to_ascii_uppercase()`]: #method.to_ascii_uppercase
1383    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
1384    #[rustc_const_stable(feature = "const_make_ascii", since = "1.84.0")]
1385    #[inline]
1386    pub const fn make_ascii_uppercase(&mut self) {
1387        *self = self.to_ascii_uppercase();
1388    }
1389
1390    /// Converts this type to its ASCII lower case equivalent in-place.
1391    ///
1392    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
1393    /// but non-ASCII letters are unchanged.
1394    ///
1395    /// To return a new lowercased value without modifying the existing one, use
1396    /// [`to_ascii_lowercase()`].
1397    ///
1398    /// # Examples
1399    ///
1400    /// ```
1401    /// let mut ascii = 'A';
1402    ///
1403    /// ascii.make_ascii_lowercase();
1404    ///
1405    /// assert_eq!('a', ascii);
1406    /// ```
1407    ///
1408    /// [`to_ascii_lowercase()`]: #method.to_ascii_lowercase
1409    #[stable(feature = "ascii_methods_on_intrinsics", since = "1.23.0")]
1410    #[rustc_const_stable(feature = "const_make_ascii", since = "1.84.0")]
1411    #[inline]
1412    pub const fn make_ascii_lowercase(&mut self) {
1413        *self = self.to_ascii_lowercase();
1414    }
1415
1416    /// Checks if the value is an ASCII alphabetic character:
1417    ///
1418    /// - U+0041 'A' ..= U+005A 'Z', or
1419    /// - U+0061 'a' ..= U+007A 'z'.
1420    ///
1421    /// # Examples
1422    ///
1423    /// ```
1424    /// let uppercase_a = 'A';
1425    /// let uppercase_g = 'G';
1426    /// let a = 'a';
1427    /// let g = 'g';
1428    /// let zero = '0';
1429    /// let percent = '%';
1430    /// let space = ' ';
1431    /// let lf = '\n';
1432    /// let esc = '\x1b';
1433    ///
1434    /// assert!(uppercase_a.is_ascii_alphabetic());
1435    /// assert!(uppercase_g.is_ascii_alphabetic());
1436    /// assert!(a.is_ascii_alphabetic());
1437    /// assert!(g.is_ascii_alphabetic());
1438    /// assert!(!zero.is_ascii_alphabetic());
1439    /// assert!(!percent.is_ascii_alphabetic());
1440    /// assert!(!space.is_ascii_alphabetic());
1441    /// assert!(!lf.is_ascii_alphabetic());
1442    /// assert!(!esc.is_ascii_alphabetic());
1443    /// ```
1444    #[must_use]
1445    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1446    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1447    #[inline]
1448    pub const fn is_ascii_alphabetic(&self) -> bool {
1449        matches!(*self, 'A'..='Z' | 'a'..='z')
1450    }
1451
1452    /// Checks if the value is an ASCII uppercase character:
1453    /// U+0041 'A' ..= U+005A 'Z'.
1454    ///
1455    /// # Examples
1456    ///
1457    /// ```
1458    /// let uppercase_a = 'A';
1459    /// let uppercase_g = 'G';
1460    /// let a = 'a';
1461    /// let g = 'g';
1462    /// let zero = '0';
1463    /// let percent = '%';
1464    /// let space = ' ';
1465    /// let lf = '\n';
1466    /// let esc = '\x1b';
1467    ///
1468    /// assert!(uppercase_a.is_ascii_uppercase());
1469    /// assert!(uppercase_g.is_ascii_uppercase());
1470    /// assert!(!a.is_ascii_uppercase());
1471    /// assert!(!g.is_ascii_uppercase());
1472    /// assert!(!zero.is_ascii_uppercase());
1473    /// assert!(!percent.is_ascii_uppercase());
1474    /// assert!(!space.is_ascii_uppercase());
1475    /// assert!(!lf.is_ascii_uppercase());
1476    /// assert!(!esc.is_ascii_uppercase());
1477    /// ```
1478    #[must_use]
1479    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1480    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1481    #[inline]
1482    pub const fn is_ascii_uppercase(&self) -> bool {
1483        matches!(*self, 'A'..='Z')
1484    }
1485
1486    /// Checks if the value is an ASCII lowercase character:
1487    /// U+0061 'a' ..= U+007A 'z'.
1488    ///
1489    /// # Examples
1490    ///
1491    /// ```
1492    /// let uppercase_a = 'A';
1493    /// let uppercase_g = 'G';
1494    /// let a = 'a';
1495    /// let g = 'g';
1496    /// let zero = '0';
1497    /// let percent = '%';
1498    /// let space = ' ';
1499    /// let lf = '\n';
1500    /// let esc = '\x1b';
1501    ///
1502    /// assert!(!uppercase_a.is_ascii_lowercase());
1503    /// assert!(!uppercase_g.is_ascii_lowercase());
1504    /// assert!(a.is_ascii_lowercase());
1505    /// assert!(g.is_ascii_lowercase());
1506    /// assert!(!zero.is_ascii_lowercase());
1507    /// assert!(!percent.is_ascii_lowercase());
1508    /// assert!(!space.is_ascii_lowercase());
1509    /// assert!(!lf.is_ascii_lowercase());
1510    /// assert!(!esc.is_ascii_lowercase());
1511    /// ```
1512    #[must_use]
1513    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1514    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1515    #[inline]
1516    pub const fn is_ascii_lowercase(&self) -> bool {
1517        matches!(*self, 'a'..='z')
1518    }
1519
1520    /// Checks if the value is an ASCII alphanumeric character:
1521    ///
1522    /// - U+0041 'A' ..= U+005A 'Z', or
1523    /// - U+0061 'a' ..= U+007A 'z', or
1524    /// - U+0030 '0' ..= U+0039 '9'.
1525    ///
1526    /// # Examples
1527    ///
1528    /// ```
1529    /// let uppercase_a = 'A';
1530    /// let uppercase_g = 'G';
1531    /// let a = 'a';
1532    /// let g = 'g';
1533    /// let zero = '0';
1534    /// let percent = '%';
1535    /// let space = ' ';
1536    /// let lf = '\n';
1537    /// let esc = '\x1b';
1538    ///
1539    /// assert!(uppercase_a.is_ascii_alphanumeric());
1540    /// assert!(uppercase_g.is_ascii_alphanumeric());
1541    /// assert!(a.is_ascii_alphanumeric());
1542    /// assert!(g.is_ascii_alphanumeric());
1543    /// assert!(zero.is_ascii_alphanumeric());
1544    /// assert!(!percent.is_ascii_alphanumeric());
1545    /// assert!(!space.is_ascii_alphanumeric());
1546    /// assert!(!lf.is_ascii_alphanumeric());
1547    /// assert!(!esc.is_ascii_alphanumeric());
1548    /// ```
1549    #[must_use]
1550    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1551    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1552    #[inline]
1553    pub const fn is_ascii_alphanumeric(&self) -> bool {
1554        matches!(*self, '0'..='9') | matches!(*self, 'A'..='Z') | matches!(*self, 'a'..='z')
1555    }
1556
1557    /// Checks if the value is an ASCII decimal digit:
1558    /// U+0030 '0' ..= U+0039 '9'.
1559    ///
1560    /// # Examples
1561    ///
1562    /// ```
1563    /// let uppercase_a = 'A';
1564    /// let uppercase_g = 'G';
1565    /// let a = 'a';
1566    /// let g = 'g';
1567    /// let zero = '0';
1568    /// let percent = '%';
1569    /// let space = ' ';
1570    /// let lf = '\n';
1571    /// let esc = '\x1b';
1572    ///
1573    /// assert!(!uppercase_a.is_ascii_digit());
1574    /// assert!(!uppercase_g.is_ascii_digit());
1575    /// assert!(!a.is_ascii_digit());
1576    /// assert!(!g.is_ascii_digit());
1577    /// assert!(zero.is_ascii_digit());
1578    /// assert!(!percent.is_ascii_digit());
1579    /// assert!(!space.is_ascii_digit());
1580    /// assert!(!lf.is_ascii_digit());
1581    /// assert!(!esc.is_ascii_digit());
1582    /// ```
1583    #[must_use]
1584    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1585    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1586    #[inline]
1587    pub const fn is_ascii_digit(&self) -> bool {
1588        matches!(*self, '0'..='9')
1589    }
1590
1591    /// Checks if the value is an ASCII octal digit:
1592    /// U+0030 '0' ..= U+0037 '7'.
1593    ///
1594    /// # Examples
1595    ///
1596    /// ```
1597    /// #![feature(is_ascii_octdigit)]
1598    ///
1599    /// let uppercase_a = 'A';
1600    /// let a = 'a';
1601    /// let zero = '0';
1602    /// let seven = '7';
1603    /// let nine = '9';
1604    /// let percent = '%';
1605    /// let lf = '\n';
1606    ///
1607    /// assert!(!uppercase_a.is_ascii_octdigit());
1608    /// assert!(!a.is_ascii_octdigit());
1609    /// assert!(zero.is_ascii_octdigit());
1610    /// assert!(seven.is_ascii_octdigit());
1611    /// assert!(!nine.is_ascii_octdigit());
1612    /// assert!(!percent.is_ascii_octdigit());
1613    /// assert!(!lf.is_ascii_octdigit());
1614    /// ```
1615    #[must_use]
1616    #[unstable(feature = "is_ascii_octdigit", issue = "101288")]
1617    #[inline]
1618    pub const fn is_ascii_octdigit(&self) -> bool {
1619        matches!(*self, '0'..='7')
1620    }
1621
1622    /// Checks if the value is an ASCII hexadecimal digit:
1623    ///
1624    /// - U+0030 '0' ..= U+0039 '9', or
1625    /// - U+0041 'A' ..= U+0046 'F', or
1626    /// - U+0061 'a' ..= U+0066 'f'.
1627    ///
1628    /// # Examples
1629    ///
1630    /// ```
1631    /// let uppercase_a = 'A';
1632    /// let uppercase_g = 'G';
1633    /// let a = 'a';
1634    /// let g = 'g';
1635    /// let zero = '0';
1636    /// let percent = '%';
1637    /// let space = ' ';
1638    /// let lf = '\n';
1639    /// let esc = '\x1b';
1640    ///
1641    /// assert!(uppercase_a.is_ascii_hexdigit());
1642    /// assert!(!uppercase_g.is_ascii_hexdigit());
1643    /// assert!(a.is_ascii_hexdigit());
1644    /// assert!(!g.is_ascii_hexdigit());
1645    /// assert!(zero.is_ascii_hexdigit());
1646    /// assert!(!percent.is_ascii_hexdigit());
1647    /// assert!(!space.is_ascii_hexdigit());
1648    /// assert!(!lf.is_ascii_hexdigit());
1649    /// assert!(!esc.is_ascii_hexdigit());
1650    /// ```
1651    #[must_use]
1652    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1653    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1654    #[inline]
1655    pub const fn is_ascii_hexdigit(&self) -> bool {
1656        matches!(*self, '0'..='9') | matches!(*self, 'A'..='F') | matches!(*self, 'a'..='f')
1657    }
1658
1659    /// Checks if the value is an ASCII punctuation character:
1660    ///
1661    /// - U+0021 ..= U+002F `! " # $ % & ' ( ) * + , - . /`, or
1662    /// - U+003A ..= U+0040 `: ; < = > ? @`, or
1663    /// - U+005B ..= U+0060 ``[ \ ] ^ _ ` ``, or
1664    /// - U+007B ..= U+007E `{ | } ~`
1665    ///
1666    /// # Examples
1667    ///
1668    /// ```
1669    /// let uppercase_a = 'A';
1670    /// let uppercase_g = 'G';
1671    /// let a = 'a';
1672    /// let g = 'g';
1673    /// let zero = '0';
1674    /// let percent = '%';
1675    /// let space = ' ';
1676    /// let lf = '\n';
1677    /// let esc = '\x1b';
1678    ///
1679    /// assert!(!uppercase_a.is_ascii_punctuation());
1680    /// assert!(!uppercase_g.is_ascii_punctuation());
1681    /// assert!(!a.is_ascii_punctuation());
1682    /// assert!(!g.is_ascii_punctuation());
1683    /// assert!(!zero.is_ascii_punctuation());
1684    /// assert!(percent.is_ascii_punctuation());
1685    /// assert!(!space.is_ascii_punctuation());
1686    /// assert!(!lf.is_ascii_punctuation());
1687    /// assert!(!esc.is_ascii_punctuation());
1688    /// ```
1689    #[must_use]
1690    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1691    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1692    #[inline]
1693    pub const fn is_ascii_punctuation(&self) -> bool {
1694        matches!(*self, '!'..='/')
1695            | matches!(*self, ':'..='@')
1696            | matches!(*self, '['..='`')
1697            | matches!(*self, '{'..='~')
1698    }
1699
1700    /// Checks if the value is an ASCII graphic character:
1701    /// U+0021 '!' ..= U+007E '~'.
1702    ///
1703    /// # Examples
1704    ///
1705    /// ```
1706    /// let uppercase_a = 'A';
1707    /// let uppercase_g = 'G';
1708    /// let a = 'a';
1709    /// let g = 'g';
1710    /// let zero = '0';
1711    /// let percent = '%';
1712    /// let space = ' ';
1713    /// let lf = '\n';
1714    /// let esc = '\x1b';
1715    ///
1716    /// assert!(uppercase_a.is_ascii_graphic());
1717    /// assert!(uppercase_g.is_ascii_graphic());
1718    /// assert!(a.is_ascii_graphic());
1719    /// assert!(g.is_ascii_graphic());
1720    /// assert!(zero.is_ascii_graphic());
1721    /// assert!(percent.is_ascii_graphic());
1722    /// assert!(!space.is_ascii_graphic());
1723    /// assert!(!lf.is_ascii_graphic());
1724    /// assert!(!esc.is_ascii_graphic());
1725    /// ```
1726    #[must_use]
1727    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1728    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1729    #[inline]
1730    pub const fn is_ascii_graphic(&self) -> bool {
1731        matches!(*self, '!'..='~')
1732    }
1733
1734    /// Checks if the value is an ASCII whitespace character:
1735    /// U+0020 SPACE, U+0009 HORIZONTAL TAB, U+000A LINE FEED,
1736    /// U+000C FORM FEED, or U+000D CARRIAGE RETURN.
1737    ///
1738    /// Rust uses the WhatWG Infra Standard's [definition of ASCII
1739    /// whitespace][infra-aw]. There are several other definitions in
1740    /// wide use. For instance, [the POSIX locale][pct] includes
1741    /// U+000B VERTICAL TAB as well as all the above characters,
1742    /// but—from the very same specification—[the default rule for
1743    /// "field splitting" in the Bourne shell][bfs] considers *only*
1744    /// SPACE, HORIZONTAL TAB, and LINE FEED as whitespace.
1745    ///
1746    /// If you are writing a program that will process an existing
1747    /// file format, check what that format's definition of whitespace is
1748    /// before using this function.
1749    ///
1750    /// [infra-aw]: https://infra.spec.whatwg.org/#ascii-whitespace
1751    /// [pct]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap07.html#tag_07_03_01
1752    /// [bfs]: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_05
1753    ///
1754    /// # Examples
1755    ///
1756    /// ```
1757    /// let uppercase_a = 'A';
1758    /// let uppercase_g = 'G';
1759    /// let a = 'a';
1760    /// let g = 'g';
1761    /// let zero = '0';
1762    /// let percent = '%';
1763    /// let space = ' ';
1764    /// let lf = '\n';
1765    /// let esc = '\x1b';
1766    ///
1767    /// assert!(!uppercase_a.is_ascii_whitespace());
1768    /// assert!(!uppercase_g.is_ascii_whitespace());
1769    /// assert!(!a.is_ascii_whitespace());
1770    /// assert!(!g.is_ascii_whitespace());
1771    /// assert!(!zero.is_ascii_whitespace());
1772    /// assert!(!percent.is_ascii_whitespace());
1773    /// assert!(space.is_ascii_whitespace());
1774    /// assert!(lf.is_ascii_whitespace());
1775    /// assert!(!esc.is_ascii_whitespace());
1776    /// ```
1777    #[must_use]
1778    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1779    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1780    #[inline]
1781    pub const fn is_ascii_whitespace(&self) -> bool {
1782        matches!(*self, '\t' | '\n' | '\x0C' | '\r' | ' ')
1783    }
1784
1785    /// Checks if the value is an ASCII control character:
1786    /// U+0000 NUL ..= U+001F UNIT SEPARATOR, or U+007F DELETE.
1787    /// Note that most ASCII whitespace characters are control
1788    /// characters, but SPACE is not.
1789    ///
1790    /// # Examples
1791    ///
1792    /// ```
1793    /// let uppercase_a = 'A';
1794    /// let uppercase_g = 'G';
1795    /// let a = 'a';
1796    /// let g = 'g';
1797    /// let zero = '0';
1798    /// let percent = '%';
1799    /// let space = ' ';
1800    /// let lf = '\n';
1801    /// let esc = '\x1b';
1802    ///
1803    /// assert!(!uppercase_a.is_ascii_control());
1804    /// assert!(!uppercase_g.is_ascii_control());
1805    /// assert!(!a.is_ascii_control());
1806    /// assert!(!g.is_ascii_control());
1807    /// assert!(!zero.is_ascii_control());
1808    /// assert!(!percent.is_ascii_control());
1809    /// assert!(!space.is_ascii_control());
1810    /// assert!(lf.is_ascii_control());
1811    /// assert!(esc.is_ascii_control());
1812    /// ```
1813    #[must_use]
1814    #[stable(feature = "ascii_ctype_on_intrinsics", since = "1.24.0")]
1815    #[rustc_const_stable(feature = "const_ascii_ctype_on_intrinsics", since = "1.47.0")]
1816    #[inline]
1817    pub const fn is_ascii_control(&self) -> bool {
1818        matches!(*self, '\0'..='\x1F' | '\x7F')
1819    }
1820}
1821
1822pub(crate) struct EscapeDebugExtArgs {
1823    /// Escape Extended Grapheme codepoints?
1824    pub(crate) escape_grapheme_extended: bool,
1825
1826    /// Escape single quotes?
1827    pub(crate) escape_single_quote: bool,
1828
1829    /// Escape double quotes?
1830    pub(crate) escape_double_quote: bool,
1831}
1832
1833impl EscapeDebugExtArgs {
1834    pub(crate) const ESCAPE_ALL: Self = Self {
1835        escape_grapheme_extended: true,
1836        escape_single_quote: true,
1837        escape_double_quote: true,
1838    };
1839}
1840
1841#[inline]
1842#[must_use]
1843const fn len_utf8(code: u32) -> usize {
1844    match code {
1845        ..MAX_ONE_B => 1,
1846        ..MAX_TWO_B => 2,
1847        ..MAX_THREE_B => 3,
1848        _ => 4,
1849    }
1850}
1851
1852#[inline]
1853#[must_use]
1854const fn len_utf16(code: u32) -> usize {
1855    if (code & 0xFFFF) == code { 1 } else { 2 }
1856}
1857
1858/// Encodes a raw `u32` value as UTF-8 into the provided byte buffer,
1859/// and then returns the subslice of the buffer that contains the encoded character.
1860///
1861/// Unlike `char::encode_utf8`, this method also handles codepoints in the surrogate range.
1862/// (Creating a `char` in the surrogate range is UB.)
1863/// The result is valid [generalized UTF-8] but not valid UTF-8.
1864///
1865/// [generalized UTF-8]: https://simonsapin.github.io/wtf-8/#generalized-utf8
1866///
1867/// # Panics
1868///
1869/// Panics if the buffer is not large enough.
1870/// A buffer of length four is large enough to encode any `char`.
1871#[unstable(feature = "char_internals", reason = "exposed only for libstd", issue = "none")]
1872#[doc(hidden)]
1873#[inline]
1874pub const fn encode_utf8_raw(code: u32, dst: &mut [u8]) -> &mut [u8] {
1875    let len = len_utf8(code);
1876    if dst.len() < len {
1877        const_panic!(
1878            "encode_utf8: buffer does not have enough bytes to encode code point",
1879            "encode_utf8: need {len} bytes to encode U+{code:04X} but buffer has just {dst_len}",
1880            code: u32 = code,
1881            len: usize = len,
1882            dst_len: usize = dst.len(),
1883        );
1884    }
1885
1886    // SAFETY: `dst` is checked to be at least the length needed to encode the codepoint.
1887    unsafe { encode_utf8_raw_unchecked(code, dst.as_mut_ptr()) };
1888
1889    // SAFETY: `<&mut [u8]>::as_mut_ptr` is guaranteed to return a valid pointer and `len` has been tested to be within bounds.
1890    unsafe { slice::from_raw_parts_mut(dst.as_mut_ptr(), len) }
1891}
1892
1893/// Encodes a raw `u32` value as UTF-8 into the byte buffer pointed to by `dst`.
1894///
1895/// Unlike `char::encode_utf8`, this method also handles codepoints in the surrogate range.
1896/// (Creating a `char` in the surrogate range is UB.)
1897/// The result is valid [generalized UTF-8] but not valid UTF-8.
1898///
1899/// [generalized UTF-8]: https://simonsapin.github.io/wtf-8/#generalized-utf8
1900///
1901/// # Safety
1902///
1903/// The behavior is undefined if the buffer pointed to by `dst` is not
1904/// large enough to hold the encoded codepoint. A buffer of length four
1905/// is large enough to encode any `char`.
1906///
1907/// For a safe version of this function, see the [`encode_utf8_raw`] function.
1908#[unstable(feature = "char_internals", reason = "exposed only for libstd", issue = "none")]
1909#[doc(hidden)]
1910#[inline]
1911pub const unsafe fn encode_utf8_raw_unchecked(code: u32, dst: *mut u8) {
1912    let len = len_utf8(code);
1913    // SAFETY: The caller must guarantee that the buffer pointed to by `dst`
1914    // is at least `len` bytes long.
1915    unsafe {
1916        if len == 1 {
1917            *dst = code as u8;
1918            return;
1919        }
1920
1921        let last1 = (code >> 0 & 0x3F) as u8 | TAG_CONT;
1922        let last2 = (code >> 6 & 0x3F) as u8 | TAG_CONT;
1923        let last3 = (code >> 12 & 0x3F) as u8 | TAG_CONT;
1924        let last4 = (code >> 18 & 0x3F) as u8 | TAG_FOUR_B;
1925
1926        if len == 2 {
1927            *dst = last2 | TAG_TWO_B;
1928            *dst.add(1) = last1;
1929            return;
1930        }
1931
1932        if len == 3 {
1933            *dst = last3 | TAG_THREE_B;
1934            *dst.add(1) = last2;
1935            *dst.add(2) = last1;
1936            return;
1937        }
1938
1939        *dst = last4;
1940        *dst.add(1) = last3;
1941        *dst.add(2) = last2;
1942        *dst.add(3) = last1;
1943    }
1944}
1945
1946/// Encodes a raw `u32` value as native endian UTF-16 into the provided `u16` buffer,
1947/// and then returns the subslice of the buffer that contains the encoded character.
1948///
1949/// Unlike `char::encode_utf16`, this method also handles codepoints in the surrogate range.
1950/// (Creating a `char` in the surrogate range is UB.)
1951///
1952/// # Panics
1953///
1954/// Panics if the buffer is not large enough.
1955/// A buffer of length 2 is large enough to encode any `char`.
1956#[unstable(feature = "char_internals", reason = "exposed only for libstd", issue = "none")]
1957#[doc(hidden)]
1958#[inline]
1959pub const fn encode_utf16_raw(mut code: u32, dst: &mut [u16]) -> &mut [u16] {
1960    let len = len_utf16(code);
1961    match (len, &mut *dst) {
1962        (1, [a, ..]) => {
1963            *a = code as u16;
1964        }
1965        (2, [a, b, ..]) => {
1966            code -= 0x1_0000;
1967            *a = (code >> 10) as u16 | 0xD800;
1968            *b = (code & 0x3FF) as u16 | 0xDC00;
1969        }
1970        _ => {
1971            const_panic!(
1972                "encode_utf16: buffer does not have enough bytes to encode code point",
1973                "encode_utf16: need {len} bytes to encode U+{code:04X} but buffer has just {dst_len}",
1974                code: u32 = code,
1975                len: usize = len,
1976                dst_len: usize = dst.len(),
1977            )
1978        }
1979    };
1980    // SAFETY: `<&mut [u16]>::as_mut_ptr` is guaranteed to return a valid pointer and `len` has been tested to be within bounds.
1981    unsafe { slice::from_raw_parts_mut(dst.as_mut_ptr(), len) }
1982}
````