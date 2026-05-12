---
title: ascii_char.rs - source
url: https://doc.rust-lang.org/src/core/ascii/ascii_char.rs.html#1171
source: crawler
fetched_at: 2026-05-06T21:29:18.251809602-03:00
rendered_js: false
word_count: 4584
summary: This document defines the AsciiChar enumeration in Rust, representing the 128 Unicode characters of the Basic Latin block. It explains the performance advantages of using this type for ASCII-only data to ensure valid UTF-8 without requiring runtime checks.
tags:
    - rust
    - ascii
    - unicode
    - character-encoding
    - data-types
    - utf-8
category: reference
---

## core/ascii/ ascii\_char.rs

````rust
1//! This uses the name `AsciiChar`, even though it's not exposed that way right now,
2//! because it avoids a whole bunch of "are you sure you didn't mean `char`?"
3//! suggestions from rustc if you get anything slightly wrong in here, and overall
4//! helps with clarity as we're also referring to `char` intentionally in here.
5
6use crate::mem::transmute;
7use crate::{assert_unsafe_precondition, fmt};
8
9/// One of the 128 Unicode characters from U+0000 through U+007F,
10/// often known as the [ASCII] subset.
11///
12/// Officially, this is the first [block] in Unicode, _Basic Latin_.
13/// For details, see the [*C0 Controls and Basic Latin*][chart] code chart.
14///
15/// This block was based on older 7-bit character code standards such as
16/// ANSI X3.4-1977, ISO 646-1973, and [NIST FIPS 1-2].
17///
18/// # When to use this
19///
20/// The main advantage of this subset is that it's always valid UTF-8.  As such,
21/// the `&[ascii::Char]` -> `&str` conversion function (as well as other related
22/// ones) are O(1): *no* runtime checks are needed.
23///
24/// If you're consuming strings, you should usually handle Unicode and thus
25/// accept `str`s, not limit yourself to `ascii::Char`s.
26///
27/// However, certain formats are intentionally designed to produce ASCII-only
28/// output in order to be 8-bit-clean.  In those cases, it can be simpler and
29/// faster to generate `ascii::Char`s instead of dealing with the variable width
30/// properties of general UTF-8 encoded strings, while still allowing the result
31/// to be used freely with other Rust things that deal in general `str`s.
32///
33/// For example, a UUID library might offer a way to produce the string
34/// representation of a UUID as an `[ascii::Char; 36]` to avoid memory
35/// allocation yet still allow it to be used as UTF-8 via `as_str` without
36/// paying for validation (or needing `unsafe` code) the way it would if it
37/// were provided as a `[u8; 36]`.
38///
39/// # Layout
40///
41/// This type is guaranteed to have a size and alignment of 1 byte.
42///
43/// # Names
44///
45/// The variants on this type are [Unicode names][NamesList] of the characters
46/// in upper camel case, with a few tweaks:
47/// - For `<control>` characters, the primary alias name is used.
48/// - `LATIN` is dropped, as this block has no non-latin letters.
49/// - `LETTER` is dropped, as `CAPITAL`/`SMALL` suffices in this block.
50/// - `DIGIT`s use a single digit rather than writing out `ZERO`, `ONE`, etc.
51///
52/// [ASCII]: https://www.unicode.org/glossary/index.html#ASCII
53/// [block]: https://www.unicode.org/glossary/index.html#block
54/// [chart]: https://www.unicode.org/charts/PDF/U0000.pdf
55/// [NIST FIPS 1-2]: https://nvlpubs.nist.gov/nistpubs/Legacy/FIPS/fipspub1-2-1977.pdf
56/// [NamesList]: https://www.unicode.org/Public/15.0.0/ucd/NamesList.txt
57#[derive(Copy, Hash)]
58#[derive_const(Clone, Eq, PartialEq, Ord, PartialOrd)]
59#[unstable(feature = "ascii_char", issue = "110998")]
60#[repr(u8)]
61pub enum AsciiChar {
62    /// U+0000 (The default variant)
63    #[unstable(feature = "ascii_char_variants", issue = "110998")]
64    Null = 0,
65    /// U+0001
66    #[unstable(feature = "ascii_char_variants", issue = "110998")]
67    StartOfHeading = 1,
68    /// U+0002
69    #[unstable(feature = "ascii_char_variants", issue = "110998")]
70    StartOfText = 2,
71    /// U+0003
72    #[unstable(feature = "ascii_char_variants", issue = "110998")]
73    EndOfText = 3,
74    /// U+0004
75    #[unstable(feature = "ascii_char_variants", issue = "110998")]
76    EndOfTransmission = 4,
77    /// U+0005
78    #[unstable(feature = "ascii_char_variants", issue = "110998")]
79    Enquiry = 5,
80    /// U+0006
81    #[unstable(feature = "ascii_char_variants", issue = "110998")]
82    Acknowledge = 6,
83    /// U+0007
84    #[unstable(feature = "ascii_char_variants", issue = "110998")]
85    Bell = 7,
86    /// U+0008
87    #[unstable(feature = "ascii_char_variants", issue = "110998")]
88    Backspace = 8,
89    /// U+0009
90    #[unstable(feature = "ascii_char_variants", issue = "110998")]
91    CharacterTabulation = 9,
92    /// U+000A
93    #[unstable(feature = "ascii_char_variants", issue = "110998")]
94    LineFeed = 10,
95    /// U+000B
96    #[unstable(feature = "ascii_char_variants", issue = "110998")]
97    LineTabulation = 11,
98    /// U+000C
99    #[unstable(feature = "ascii_char_variants", issue = "110998")]
100    FormFeed = 12,
101    /// U+000D
102    #[unstable(feature = "ascii_char_variants", issue = "110998")]
103    CarriageReturn = 13,
104    /// U+000E
105    #[unstable(feature = "ascii_char_variants", issue = "110998")]
106    ShiftOut = 14,
107    /// U+000F
108    #[unstable(feature = "ascii_char_variants", issue = "110998")]
109    ShiftIn = 15,
110    /// U+0010
111    #[unstable(feature = "ascii_char_variants", issue = "110998")]
112    DataLinkEscape = 16,
113    /// U+0011
114    #[unstable(feature = "ascii_char_variants", issue = "110998")]
115    DeviceControlOne = 17,
116    /// U+0012
117    #[unstable(feature = "ascii_char_variants", issue = "110998")]
118    DeviceControlTwo = 18,
119    /// U+0013
120    #[unstable(feature = "ascii_char_variants", issue = "110998")]
121    DeviceControlThree = 19,
122    /// U+0014
123    #[unstable(feature = "ascii_char_variants", issue = "110998")]
124    DeviceControlFour = 20,
125    /// U+0015
126    #[unstable(feature = "ascii_char_variants", issue = "110998")]
127    NegativeAcknowledge = 21,
128    /// U+0016
129    #[unstable(feature = "ascii_char_variants", issue = "110998")]
130    SynchronousIdle = 22,
131    /// U+0017
132    #[unstable(feature = "ascii_char_variants", issue = "110998")]
133    EndOfTransmissionBlock = 23,
134    /// U+0018
135    #[unstable(feature = "ascii_char_variants", issue = "110998")]
136    Cancel = 24,
137    /// U+0019
138    #[unstable(feature = "ascii_char_variants", issue = "110998")]
139    EndOfMedium = 25,
140    /// U+001A
141    #[unstable(feature = "ascii_char_variants", issue = "110998")]
142    Substitute = 26,
143    /// U+001B
144    #[unstable(feature = "ascii_char_variants", issue = "110998")]
145    Escape = 27,
146    /// U+001C
147    #[unstable(feature = "ascii_char_variants", issue = "110998")]
148    InformationSeparatorFour = 28,
149    /// U+001D
150    #[unstable(feature = "ascii_char_variants", issue = "110998")]
151    InformationSeparatorThree = 29,
152    /// U+001E
153    #[unstable(feature = "ascii_char_variants", issue = "110998")]
154    InformationSeparatorTwo = 30,
155    /// U+001F
156    #[unstable(feature = "ascii_char_variants", issue = "110998")]
157    InformationSeparatorOne = 31,
158    /// U+0020
159    #[unstable(feature = "ascii_char_variants", issue = "110998")]
160    Space = 32,
161    /// U+0021
162    #[unstable(feature = "ascii_char_variants", issue = "110998")]
163    ExclamationMark = 33,
164    /// U+0022
165    #[unstable(feature = "ascii_char_variants", issue = "110998")]
166    QuotationMark = 34,
167    /// U+0023
168    #[unstable(feature = "ascii_char_variants", issue = "110998")]
169    NumberSign = 35,
170    /// U+0024
171    #[unstable(feature = "ascii_char_variants", issue = "110998")]
172    DollarSign = 36,
173    /// U+0025
174    #[unstable(feature = "ascii_char_variants", issue = "110998")]
175    PercentSign = 37,
176    /// U+0026
177    #[unstable(feature = "ascii_char_variants", issue = "110998")]
178    Ampersand = 38,
179    /// U+0027
180    #[unstable(feature = "ascii_char_variants", issue = "110998")]
181    Apostrophe = 39,
182    /// U+0028
183    #[unstable(feature = "ascii_char_variants", issue = "110998")]
184    LeftParenthesis = 40,
185    /// U+0029
186    #[unstable(feature = "ascii_char_variants", issue = "110998")]
187    RightParenthesis = 41,
188    /// U+002A
189    #[unstable(feature = "ascii_char_variants", issue = "110998")]
190    Asterisk = 42,
191    /// U+002B
192    #[unstable(feature = "ascii_char_variants", issue = "110998")]
193    PlusSign = 43,
194    /// U+002C
195    #[unstable(feature = "ascii_char_variants", issue = "110998")]
196    Comma = 44,
197    /// U+002D
198    #[unstable(feature = "ascii_char_variants", issue = "110998")]
199    HyphenMinus = 45,
200    /// U+002E
201    #[unstable(feature = "ascii_char_variants", issue = "110998")]
202    FullStop = 46,
203    /// U+002F
204    #[unstable(feature = "ascii_char_variants", issue = "110998")]
205    Solidus = 47,
206    /// U+0030
207    #[unstable(feature = "ascii_char_variants", issue = "110998")]
208    Digit0 = 48,
209    /// U+0031
210    #[unstable(feature = "ascii_char_variants", issue = "110998")]
211    Digit1 = 49,
212    /// U+0032
213    #[unstable(feature = "ascii_char_variants", issue = "110998")]
214    Digit2 = 50,
215    /// U+0033
216    #[unstable(feature = "ascii_char_variants", issue = "110998")]
217    Digit3 = 51,
218    /// U+0034
219    #[unstable(feature = "ascii_char_variants", issue = "110998")]
220    Digit4 = 52,
221    /// U+0035
222    #[unstable(feature = "ascii_char_variants", issue = "110998")]
223    Digit5 = 53,
224    /// U+0036
225    #[unstable(feature = "ascii_char_variants", issue = "110998")]
226    Digit6 = 54,
227    /// U+0037
228    #[unstable(feature = "ascii_char_variants", issue = "110998")]
229    Digit7 = 55,
230    /// U+0038
231    #[unstable(feature = "ascii_char_variants", issue = "110998")]
232    Digit8 = 56,
233    /// U+0039
234    #[unstable(feature = "ascii_char_variants", issue = "110998")]
235    Digit9 = 57,
236    /// U+003A
237    #[unstable(feature = "ascii_char_variants", issue = "110998")]
238    Colon = 58,
239    /// U+003B
240    #[unstable(feature = "ascii_char_variants", issue = "110998")]
241    Semicolon = 59,
242    /// U+003C
243    #[unstable(feature = "ascii_char_variants", issue = "110998")]
244    LessThanSign = 60,
245    /// U+003D
246    #[unstable(feature = "ascii_char_variants", issue = "110998")]
247    EqualsSign = 61,
248    /// U+003E
249    #[unstable(feature = "ascii_char_variants", issue = "110998")]
250    GreaterThanSign = 62,
251    /// U+003F
252    #[unstable(feature = "ascii_char_variants", issue = "110998")]
253    QuestionMark = 63,
254    /// U+0040
255    #[unstable(feature = "ascii_char_variants", issue = "110998")]
256    CommercialAt = 64,
257    /// U+0041
258    #[unstable(feature = "ascii_char_variants", issue = "110998")]
259    CapitalA = 65,
260    /// U+0042
261    #[unstable(feature = "ascii_char_variants", issue = "110998")]
262    CapitalB = 66,
263    /// U+0043
264    #[unstable(feature = "ascii_char_variants", issue = "110998")]
265    CapitalC = 67,
266    /// U+0044
267    #[unstable(feature = "ascii_char_variants", issue = "110998")]
268    CapitalD = 68,
269    /// U+0045
270    #[unstable(feature = "ascii_char_variants", issue = "110998")]
271    CapitalE = 69,
272    /// U+0046
273    #[unstable(feature = "ascii_char_variants", issue = "110998")]
274    CapitalF = 70,
275    /// U+0047
276    #[unstable(feature = "ascii_char_variants", issue = "110998")]
277    CapitalG = 71,
278    /// U+0048
279    #[unstable(feature = "ascii_char_variants", issue = "110998")]
280    CapitalH = 72,
281    /// U+0049
282    #[unstable(feature = "ascii_char_variants", issue = "110998")]
283    CapitalI = 73,
284    /// U+004A
285    #[unstable(feature = "ascii_char_variants", issue = "110998")]
286    CapitalJ = 74,
287    /// U+004B
288    #[unstable(feature = "ascii_char_variants", issue = "110998")]
289    CapitalK = 75,
290    /// U+004C
291    #[unstable(feature = "ascii_char_variants", issue = "110998")]
292    CapitalL = 76,
293    /// U+004D
294    #[unstable(feature = "ascii_char_variants", issue = "110998")]
295    CapitalM = 77,
296    /// U+004E
297    #[unstable(feature = "ascii_char_variants", issue = "110998")]
298    CapitalN = 78,
299    /// U+004F
300    #[unstable(feature = "ascii_char_variants", issue = "110998")]
301    CapitalO = 79,
302    /// U+0050
303    #[unstable(feature = "ascii_char_variants", issue = "110998")]
304    CapitalP = 80,
305    /// U+0051
306    #[unstable(feature = "ascii_char_variants", issue = "110998")]
307    CapitalQ = 81,
308    /// U+0052
309    #[unstable(feature = "ascii_char_variants", issue = "110998")]
310    CapitalR = 82,
311    /// U+0053
312    #[unstable(feature = "ascii_char_variants", issue = "110998")]
313    CapitalS = 83,
314    /// U+0054
315    #[unstable(feature = "ascii_char_variants", issue = "110998")]
316    CapitalT = 84,
317    /// U+0055
318    #[unstable(feature = "ascii_char_variants", issue = "110998")]
319    CapitalU = 85,
320    /// U+0056
321    #[unstable(feature = "ascii_char_variants", issue = "110998")]
322    CapitalV = 86,
323    /// U+0057
324    #[unstable(feature = "ascii_char_variants", issue = "110998")]
325    CapitalW = 87,
326    /// U+0058
327    #[unstable(feature = "ascii_char_variants", issue = "110998")]
328    CapitalX = 88,
329    /// U+0059
330    #[unstable(feature = "ascii_char_variants", issue = "110998")]
331    CapitalY = 89,
332    /// U+005A
333    #[unstable(feature = "ascii_char_variants", issue = "110998")]
334    CapitalZ = 90,
335    /// U+005B
336    #[unstable(feature = "ascii_char_variants", issue = "110998")]
337    LeftSquareBracket = 91,
338    /// U+005C
339    #[unstable(feature = "ascii_char_variants", issue = "110998")]
340    ReverseSolidus = 92,
341    /// U+005D
342    #[unstable(feature = "ascii_char_variants", issue = "110998")]
343    RightSquareBracket = 93,
344    /// U+005E
345    #[unstable(feature = "ascii_char_variants", issue = "110998")]
346    CircumflexAccent = 94,
347    /// U+005F
348    #[unstable(feature = "ascii_char_variants", issue = "110998")]
349    LowLine = 95,
350    /// U+0060
351    #[unstable(feature = "ascii_char_variants", issue = "110998")]
352    GraveAccent = 96,
353    /// U+0061
354    #[unstable(feature = "ascii_char_variants", issue = "110998")]
355    SmallA = 97,
356    /// U+0062
357    #[unstable(feature = "ascii_char_variants", issue = "110998")]
358    SmallB = 98,
359    /// U+0063
360    #[unstable(feature = "ascii_char_variants", issue = "110998")]
361    SmallC = 99,
362    /// U+0064
363    #[unstable(feature = "ascii_char_variants", issue = "110998")]
364    SmallD = 100,
365    /// U+0065
366    #[unstable(feature = "ascii_char_variants", issue = "110998")]
367    SmallE = 101,
368    /// U+0066
369    #[unstable(feature = "ascii_char_variants", issue = "110998")]
370    SmallF = 102,
371    /// U+0067
372    #[unstable(feature = "ascii_char_variants", issue = "110998")]
373    SmallG = 103,
374    /// U+0068
375    #[unstable(feature = "ascii_char_variants", issue = "110998")]
376    SmallH = 104,
377    /// U+0069
378    #[unstable(feature = "ascii_char_variants", issue = "110998")]
379    SmallI = 105,
380    /// U+006A
381    #[unstable(feature = "ascii_char_variants", issue = "110998")]
382    SmallJ = 106,
383    /// U+006B
384    #[unstable(feature = "ascii_char_variants", issue = "110998")]
385    SmallK = 107,
386    /// U+006C
387    #[unstable(feature = "ascii_char_variants", issue = "110998")]
388    SmallL = 108,
389    /// U+006D
390    #[unstable(feature = "ascii_char_variants", issue = "110998")]
391    SmallM = 109,
392    /// U+006E
393    #[unstable(feature = "ascii_char_variants", issue = "110998")]
394    SmallN = 110,
395    /// U+006F
396    #[unstable(feature = "ascii_char_variants", issue = "110998")]
397    SmallO = 111,
398    /// U+0070
399    #[unstable(feature = "ascii_char_variants", issue = "110998")]
400    SmallP = 112,
401    /// U+0071
402    #[unstable(feature = "ascii_char_variants", issue = "110998")]
403    SmallQ = 113,
404    /// U+0072
405    #[unstable(feature = "ascii_char_variants", issue = "110998")]
406    SmallR = 114,
407    /// U+0073
408    #[unstable(feature = "ascii_char_variants", issue = "110998")]
409    SmallS = 115,
410    /// U+0074
411    #[unstable(feature = "ascii_char_variants", issue = "110998")]
412    SmallT = 116,
413    /// U+0075
414    #[unstable(feature = "ascii_char_variants", issue = "110998")]
415    SmallU = 117,
416    /// U+0076
417    #[unstable(feature = "ascii_char_variants", issue = "110998")]
418    SmallV = 118,
419    /// U+0077
420    #[unstable(feature = "ascii_char_variants", issue = "110998")]
421    SmallW = 119,
422    /// U+0078
423    #[unstable(feature = "ascii_char_variants", issue = "110998")]
424    SmallX = 120,
425    /// U+0079
426    #[unstable(feature = "ascii_char_variants", issue = "110998")]
427    SmallY = 121,
428    /// U+007A
429    #[unstable(feature = "ascii_char_variants", issue = "110998")]
430    SmallZ = 122,
431    /// U+007B
432    #[unstable(feature = "ascii_char_variants", issue = "110998")]
433    LeftCurlyBracket = 123,
434    /// U+007C
435    #[unstable(feature = "ascii_char_variants", issue = "110998")]
436    VerticalLine = 124,
437    /// U+007D
438    #[unstable(feature = "ascii_char_variants", issue = "110998")]
439    RightCurlyBracket = 125,
440    /// U+007E
441    #[unstable(feature = "ascii_char_variants", issue = "110998")]
442    Tilde = 126,
443    /// U+007F
444    #[unstable(feature = "ascii_char_variants", issue = "110998")]
445    Delete = 127,
446}
447
448impl AsciiChar {
449    /// The character with the lowest ASCII code.
450    #[unstable(feature = "ascii_char", issue = "110998")]
451    pub const MIN: Self = Self::Null;
452
453    /// The character with the highest ASCII code.
454    #[unstable(feature = "ascii_char", issue = "110998")]
455    pub const MAX: Self = Self::Delete;
456
457    /// Creates an ASCII character from the byte `b`,
458    /// or returns `None` if it's too large.
459    #[unstable(feature = "ascii_char", issue = "110998")]
460    #[inline]
461    pub const fn from_u8(b: u8) -> Option<Self> {
462        if b <= 127 {
463            // SAFETY: Just checked that `b` is in-range
464            Some(unsafe { Self::from_u8_unchecked(b) })
465        } else {
466            None
467        }
468    }
469
470    /// Creates an ASCII character from the byte `b`,
471    /// without checking whether it's valid.
472    ///
473    /// # Safety
474    ///
475    /// `b` must be in `0..=127`, or else this is UB.
476    #[unstable(feature = "ascii_char", issue = "110998")]
477    #[inline]
478    pub const unsafe fn from_u8_unchecked(b: u8) -> Self {
479        // SAFETY: Our safety precondition is that `b` is in-range.
480        unsafe { transmute(b) }
481    }
482
483    /// When passed the *number* `0`, `1`, …, `9`, returns the *character*
484    /// `'0'`, `'1'`, …, `'9'` respectively.
485    ///
486    /// If `d >= 10`, returns `None`.
487    #[unstable(feature = "ascii_char", issue = "110998")]
488    #[inline]
489    pub const fn digit(d: u8) -> Option<Self> {
490        if d < 10 {
491            // SAFETY: Just checked it's in-range.
492            Some(unsafe { Self::digit_unchecked(d) })
493        } else {
494            None
495        }
496    }
497
498    /// When passed the *number* `0`, `1`, …, `9`, returns the *character*
499    /// `'0'`, `'1'`, …, `'9'` respectively, without checking that it's in-range.
500    ///
501    /// # Safety
502    ///
503    /// This is immediate UB if called with `d > 64`.
504    ///
505    /// If `d >= 10` and `d <= 64`, this is allowed to return any value or panic.
506    /// Notably, it should not be expected to return hex digits, or any other
507    /// reasonable extension of the decimal digits.
508    ///
509    /// (This loose safety condition is intended to simplify soundness proofs
510    /// when writing code using this method, since the implementation doesn't
511    /// need something really specific, not to make those other arguments do
512    /// something useful. It might be tightened before stabilization.)
513    #[unstable(feature = "ascii_char", issue = "110998")]
514    #[inline]
515    #[track_caller]
516    pub const unsafe fn digit_unchecked(d: u8) -> Self {
517        assert_unsafe_precondition!(
518            check_library_ub,
519            "`ascii::Char::digit_unchecked` input cannot exceed 9.",
520            (d: u8 = d) => d < 10
521        );
522
523        // SAFETY: `'0'` through `'9'` are U+00030 through U+0039,
524        // so because `d` must be 64 or less the addition can return at most
525        // 112 (0x70), which doesn't overflow and is within the ASCII range.
526        unsafe {
527            let byte = b'0'.unchecked_add(d);
528            Self::from_u8_unchecked(byte)
529        }
530    }
531
532    /// Gets this ASCII character as a byte.
533    #[unstable(feature = "ascii_char", issue = "110998")]
534    #[inline]
535    pub const fn to_u8(self) -> u8 {
536        self as u8
537    }
538
539    /// Gets this ASCII character as a `char` Unicode Scalar Value.
540    #[unstable(feature = "ascii_char", issue = "110998")]
541    #[inline]
542    pub const fn to_char(self) -> char {
543        self as u8 as char
544    }
545
546    /// Views this ASCII character as a one-code-unit UTF-8 `str`.
547    #[unstable(feature = "ascii_char", issue = "110998")]
548    #[inline]
549    pub const fn as_str(&self) -> &str {
550        crate::slice::from_ref(self).as_str()
551    }
552
553    /// Makes a copy of the value in its upper case equivalent.
554    ///
555    /// Letters 'a' to 'z' are mapped to 'A' to 'Z'.
556    ///
557    /// To uppercase the value in-place, use [`make_uppercase`].
558    ///
559    /// # Examples
560    ///
561    /// ```
562    /// #![feature(ascii_char, ascii_char_variants)]
563    /// use std::ascii;
564    ///
565    /// let lowercase_a = ascii::Char::SmallA;
566    ///
567    /// assert_eq!(
568    ///     ascii::Char::CapitalA,
569    ///     lowercase_a.to_uppercase(),
570    /// );
571    /// ```
572    ///
573    /// [`make_uppercase`]: Self::make_uppercase
574    #[must_use = "to uppercase the value in-place, use `make_uppercase()`"]
575    #[unstable(feature = "ascii_char", issue = "110998")]
576    #[inline]
577    pub const fn to_uppercase(self) -> Self {
578        let uppercase_byte = self.to_u8().to_ascii_uppercase();
579        // SAFETY: Toggling the 6th bit won't convert ASCII to non-ASCII.
580        unsafe { Self::from_u8_unchecked(uppercase_byte) }
581    }
582
583    /// Makes a copy of the value in its lower case equivalent.
584    ///
585    /// Letters 'A' to 'Z' are mapped to 'a' to 'z'.
586    ///
587    /// To lowercase the value in-place, use [`make_lowercase`].
588    ///
589    /// # Examples
590    ///
591    /// ```
592    /// #![feature(ascii_char, ascii_char_variants)]
593    /// use std::ascii;
594    ///
595    /// let uppercase_a = ascii::Char::CapitalA;
596    ///
597    /// assert_eq!(
598    ///     ascii::Char::SmallA,
599    ///     uppercase_a.to_lowercase(),
600    /// );
601    /// ```
602    ///
603    /// [`make_lowercase`]: Self::make_lowercase
604    #[must_use = "to lowercase the value in-place, use `make_lowercase()`"]
605    #[unstable(feature = "ascii_char", issue = "110998")]
606    #[inline]
607    pub const fn to_lowercase(self) -> Self {
608        let lowercase_byte = self.to_u8().to_ascii_lowercase();
609        // SAFETY: Setting the 6th bit won't convert ASCII to non-ASCII.
610        unsafe { Self::from_u8_unchecked(lowercase_byte) }
611    }
612
613    /// Checks that two values are a case-insensitive match.
614    ///
615    /// This is equivalent to `to_lowercase(a) == to_lowercase(b)`.
616    ///
617    /// # Examples
618    ///
619    /// ```
620    /// #![feature(ascii_char, ascii_char_variants)]
621    /// use std::ascii;
622    ///
623    /// let lowercase_a = ascii::Char::SmallA;
624    /// let uppercase_a = ascii::Char::CapitalA;
625    ///
626    /// assert!(lowercase_a.eq_ignore_case(uppercase_a));
627    /// ```
628    #[unstable(feature = "ascii_char", issue = "110998")]
629    #[inline]
630    pub const fn eq_ignore_case(self, other: Self) -> bool {
631        // FIXME(const-hack) `arg.to_u8().to_ascii_lowercase()` -> `arg.to_lowercase()`
632        // once `PartialEq` is const for `Self`.
633        self.to_u8().to_ascii_lowercase() == other.to_u8().to_ascii_lowercase()
634    }
635
636    /// Converts this value to its upper case equivalent in-place.
637    ///
638    /// Letters 'a' to 'z' are mapped to 'A' to 'Z'.
639    ///
640    /// To return a new uppercased value without modifying the existing one, use
641    /// [`to_uppercase`].
642    ///
643    /// # Examples
644    ///
645    /// ```
646    /// #![feature(ascii_char, ascii_char_variants)]
647    /// use std::ascii;
648    ///
649    /// let mut letter_a = ascii::Char::SmallA;
650    ///
651    /// letter_a.make_uppercase();
652    ///
653    /// assert_eq!(ascii::Char::CapitalA, letter_a);
654    /// ```
655    ///
656    /// [`to_uppercase`]: Self::to_uppercase
657    #[unstable(feature = "ascii_char", issue = "110998")]
658    #[inline]
659    pub const fn make_uppercase(&mut self) {
660        *self = self.to_uppercase();
661    }
662
663    /// Converts this value to its lower case equivalent in-place.
664    ///
665    /// Letters 'A' to 'Z' are mapped to 'a' to 'z'.
666    ///
667    /// To return a new lowercased value without modifying the existing one, use
668    /// [`to_lowercase`].
669    ///
670    /// # Examples
671    ///
672    /// ```
673    /// #![feature(ascii_char, ascii_char_variants)]
674    /// use std::ascii;
675    ///
676    /// let mut letter_a = ascii::Char::CapitalA;
677    ///
678    /// letter_a.make_lowercase();
679    ///
680    /// assert_eq!(ascii::Char::SmallA, letter_a);
681    /// ```
682    ///
683    /// [`to_lowercase`]: Self::to_lowercase
684    #[unstable(feature = "ascii_char", issue = "110998")]
685    #[inline]
686    pub const fn make_lowercase(&mut self) {
687        *self = self.to_lowercase();
688    }
689
690    /// Checks if the value is an alphabetic character:
691    ///
692    /// - 0x41 'A' ..= 0x5A 'Z', or
693    /// - 0x61 'a' ..= 0x7A 'z'.
694    ///
695    /// # Examples
696    ///
697    /// ```
698    /// #![feature(ascii_char, ascii_char_variants)]
699    /// use std::ascii;
700    ///
701    /// let uppercase_a = ascii::Char::CapitalA;
702    /// let uppercase_g = ascii::Char::CapitalG;
703    /// let a = ascii::Char::SmallA;
704    /// let g = ascii::Char::SmallG;
705    /// let zero = ascii::Char::Digit0;
706    /// let percent = ascii::Char::PercentSign;
707    /// let space = ascii::Char::Space;
708    /// let lf = ascii::Char::LineFeed;
709    /// let esc = ascii::Char::Escape;
710    ///
711    /// assert!(uppercase_a.is_alphabetic());
712    /// assert!(uppercase_g.is_alphabetic());
713    /// assert!(a.is_alphabetic());
714    /// assert!(g.is_alphabetic());
715    /// assert!(!zero.is_alphabetic());
716    /// assert!(!percent.is_alphabetic());
717    /// assert!(!space.is_alphabetic());
718    /// assert!(!lf.is_alphabetic());
719    /// assert!(!esc.is_alphabetic());
720    /// ```
721    #[must_use]
722    #[unstable(feature = "ascii_char", issue = "110998")]
723    #[inline]
724    pub const fn is_alphabetic(self) -> bool {
725        self.to_u8().is_ascii_alphabetic()
726    }
727
728    /// Checks if the value is an uppercase character:
729    /// 0x41 'A' ..= 0x5A 'Z'.
730    ///
731    /// # Examples
732    ///
733    /// ```
734    /// #![feature(ascii_char, ascii_char_variants)]
735    /// use std::ascii;
736    ///
737    /// let uppercase_a = ascii::Char::CapitalA;
738    /// let uppercase_g = ascii::Char::CapitalG;
739    /// let a = ascii::Char::SmallA;
740    /// let g = ascii::Char::SmallG;
741    /// let zero = ascii::Char::Digit0;
742    /// let percent = ascii::Char::PercentSign;
743    /// let space = ascii::Char::Space;
744    /// let lf = ascii::Char::LineFeed;
745    /// let esc = ascii::Char::Escape;
746    ///
747    /// assert!(uppercase_a.is_uppercase());
748    /// assert!(uppercase_g.is_uppercase());
749    /// assert!(!a.is_uppercase());
750    /// assert!(!g.is_uppercase());
751    /// assert!(!zero.is_uppercase());
752    /// assert!(!percent.is_uppercase());
753    /// assert!(!space.is_uppercase());
754    /// assert!(!lf.is_uppercase());
755    /// assert!(!esc.is_uppercase());
756    /// ```
757    #[must_use]
758    #[unstable(feature = "ascii_char", issue = "110998")]
759    #[inline]
760    pub const fn is_uppercase(self) -> bool {
761        self.to_u8().is_ascii_uppercase()
762    }
763
764    /// Checks if the value is a lowercase character:
765    /// 0x61 'a' ..= 0x7A 'z'.
766    ///
767    /// # Examples
768    ///
769    /// ```
770    /// #![feature(ascii_char, ascii_char_variants)]
771    /// use std::ascii;
772    ///
773    /// let uppercase_a = ascii::Char::CapitalA;
774    /// let uppercase_g = ascii::Char::CapitalG;
775    /// let a = ascii::Char::SmallA;
776    /// let g = ascii::Char::SmallG;
777    /// let zero = ascii::Char::Digit0;
778    /// let percent = ascii::Char::PercentSign;
779    /// let space = ascii::Char::Space;
780    /// let lf = ascii::Char::LineFeed;
781    /// let esc = ascii::Char::Escape;
782    ///
783    /// assert!(!uppercase_a.is_lowercase());
784    /// assert!(!uppercase_g.is_lowercase());
785    /// assert!(a.is_lowercase());
786    /// assert!(g.is_lowercase());
787    /// assert!(!zero.is_lowercase());
788    /// assert!(!percent.is_lowercase());
789    /// assert!(!space.is_lowercase());
790    /// assert!(!lf.is_lowercase());
791    /// assert!(!esc.is_lowercase());
792    /// ```
793    #[must_use]
794    #[unstable(feature = "ascii_char", issue = "110998")]
795    #[inline]
796    pub const fn is_lowercase(self) -> bool {
797        self.to_u8().is_ascii_lowercase()
798    }
799
800    /// Checks if the value is an alphanumeric character:
801    ///
802    /// - 0x41 'A' ..= 0x5A 'Z', or
803    /// - 0x61 'a' ..= 0x7A 'z', or
804    /// - 0x30 '0' ..= 0x39 '9'.
805    ///
806    /// # Examples
807    ///
808    /// ```
809    /// #![feature(ascii_char, ascii_char_variants)]
810    /// use std::ascii;
811    ///
812    /// let uppercase_a = ascii::Char::CapitalA;
813    /// let uppercase_g = ascii::Char::CapitalG;
814    /// let a = ascii::Char::SmallA;
815    /// let g = ascii::Char::SmallG;
816    /// let zero = ascii::Char::Digit0;
817    /// let percent = ascii::Char::PercentSign;
818    /// let space = ascii::Char::Space;
819    /// let lf = ascii::Char::LineFeed;
820    /// let esc = ascii::Char::Escape;
821    ///
822    /// assert!(uppercase_a.is_alphanumeric());
823    /// assert!(uppercase_g.is_alphanumeric());
824    /// assert!(a.is_alphanumeric());
825    /// assert!(g.is_alphanumeric());
826    /// assert!(zero.is_alphanumeric());
827    /// assert!(!percent.is_alphanumeric());
828    /// assert!(!space.is_alphanumeric());
829    /// assert!(!lf.is_alphanumeric());
830    /// assert!(!esc.is_alphanumeric());
831    /// ```
832    #[must_use]
833    #[unstable(feature = "ascii_char", issue = "110998")]
834    #[inline]
835    pub const fn is_alphanumeric(self) -> bool {
836        self.to_u8().is_ascii_alphanumeric()
837    }
838
839    /// Checks if the value is a decimal digit:
840    /// 0x30 '0' ..= 0x39 '9'.
841    ///
842    /// # Examples
843    ///
844    /// ```
845    /// #![feature(ascii_char, ascii_char_variants)]
846    /// use std::ascii;
847    ///
848    /// let uppercase_a = ascii::Char::CapitalA;
849    /// let uppercase_g = ascii::Char::CapitalG;
850    /// let a = ascii::Char::SmallA;
851    /// let g = ascii::Char::SmallG;
852    /// let zero = ascii::Char::Digit0;
853    /// let percent = ascii::Char::PercentSign;
854    /// let space = ascii::Char::Space;
855    /// let lf = ascii::Char::LineFeed;
856    /// let esc = ascii::Char::Escape;
857    ///
858    /// assert!(!uppercase_a.is_digit());
859    /// assert!(!uppercase_g.is_digit());
860    /// assert!(!a.is_digit());
861    /// assert!(!g.is_digit());
862    /// assert!(zero.is_digit());
863    /// assert!(!percent.is_digit());
864    /// assert!(!space.is_digit());
865    /// assert!(!lf.is_digit());
866    /// assert!(!esc.is_digit());
867    /// ```
868    #[must_use]
869    #[unstable(feature = "ascii_char", issue = "110998")]
870    #[inline]
871    pub const fn is_digit(self) -> bool {
872        self.to_u8().is_ascii_digit()
873    }
874
875    /// Checks if the value is an octal digit:
876    /// 0x30 '0' ..= 0x37 '7'.
877    ///
878    /// # Examples
879    ///
880    /// ```
881    /// #![feature(ascii_char, ascii_char_variants)]
882    ///
883    /// use std::ascii;
884    ///
885    /// let uppercase_a = ascii::Char::CapitalA;
886    /// let a = ascii::Char::SmallA;
887    /// let zero = ascii::Char::Digit0;
888    /// let seven = ascii::Char::Digit7;
889    /// let eight = ascii::Char::Digit8;
890    /// let percent = ascii::Char::PercentSign;
891    /// let lf = ascii::Char::LineFeed;
892    /// let esc = ascii::Char::Escape;
893    ///
894    /// assert!(!uppercase_a.is_octdigit());
895    /// assert!(!a.is_octdigit());
896    /// assert!(zero.is_octdigit());
897    /// assert!(seven.is_octdigit());
898    /// assert!(!eight.is_octdigit());
899    /// assert!(!percent.is_octdigit());
900    /// assert!(!lf.is_octdigit());
901    /// assert!(!esc.is_octdigit());
902    /// ```
903    #[must_use]
904    // This is blocked on two unstable features. Please ensure both are
905    // stabilized before marking this method as stable.
906    #[unstable(feature = "ascii_char", issue = "110998")]
907    // #[unstable(feature = "is_ascii_octdigit", issue = "101288")]
908    #[inline]
909    pub const fn is_octdigit(self) -> bool {
910        self.to_u8().is_ascii_octdigit()
911    }
912
913    /// Checks if the value is a hexadecimal digit:
914    ///
915    /// - 0x30 '0' ..= 0x39 '9', or
916    /// - 0x41 'A' ..= 0x46 'F', or
917    /// - 0x61 'a' ..= 0x66 'f'.
918    ///
919    /// # Examples
920    ///
921    /// ```
922    /// #![feature(ascii_char, ascii_char_variants)]
923    /// use std::ascii;
924    ///
925    /// let uppercase_a = ascii::Char::CapitalA;
926    /// let uppercase_g = ascii::Char::CapitalG;
927    /// let a = ascii::Char::SmallA;
928    /// let g = ascii::Char::SmallG;
929    /// let zero = ascii::Char::Digit0;
930    /// let percent = ascii::Char::PercentSign;
931    /// let space = ascii::Char::Space;
932    /// let lf = ascii::Char::LineFeed;
933    /// let esc = ascii::Char::Escape;
934    ///
935    /// assert!(uppercase_a.is_hexdigit());
936    /// assert!(!uppercase_g.is_hexdigit());
937    /// assert!(a.is_hexdigit());
938    /// assert!(!g.is_hexdigit());
939    /// assert!(zero.is_hexdigit());
940    /// assert!(!percent.is_hexdigit());
941    /// assert!(!space.is_hexdigit());
942    /// assert!(!lf.is_hexdigit());
943    /// assert!(!esc.is_hexdigit());
944    /// ```
945    #[must_use]
946    #[unstable(feature = "ascii_char", issue = "110998")]
947    #[inline]
948    pub const fn is_hexdigit(self) -> bool {
949        self.to_u8().is_ascii_hexdigit()
950    }
951
952    /// Checks if the value is a punctuation character:
953    ///
954    /// - 0x21 ..= 0x2F `! " # $ % & ' ( ) * + , - . /`, or
955    /// - 0x3A ..= 0x40 `: ; < = > ? @`, or
956    /// - 0x5B ..= 0x60 `` [ \ ] ^ _ ` ``, or
957    /// - 0x7B ..= 0x7E `{ | } ~`
958    ///
959    /// # Examples
960    ///
961    /// ```
962    /// #![feature(ascii_char, ascii_char_variants)]
963    /// use std::ascii;
964    ///
965    /// let uppercase_a = ascii::Char::CapitalA;
966    /// let uppercase_g = ascii::Char::CapitalG;
967    /// let a = ascii::Char::SmallA;
968    /// let g = ascii::Char::SmallG;
969    /// let zero = ascii::Char::Digit0;
970    /// let percent = ascii::Char::PercentSign;
971    /// let space = ascii::Char::Space;
972    /// let lf = ascii::Char::LineFeed;
973    /// let esc = ascii::Char::Escape;
974    ///
975    /// assert!(!uppercase_a.is_punctuation());
976    /// assert!(!uppercase_g.is_punctuation());
977    /// assert!(!a.is_punctuation());
978    /// assert!(!g.is_punctuation());
979    /// assert!(!zero.is_punctuation());
980    /// assert!(percent.is_punctuation());
981    /// assert!(!space.is_punctuation());
982    /// assert!(!lf.is_punctuation());
983    /// assert!(!esc.is_punctuation());
984    /// ```
985    #[must_use]
986    #[unstable(feature = "ascii_char", issue = "110998")]
987    #[inline]
988    pub const fn is_punctuation(self) -> bool {
989        self.to_u8().is_ascii_punctuation()
990    }
991
992    /// Checks if the value is a graphic character:
993    /// 0x21 '!' ..= 0x7E '~'.
994    ///
995    /// # Examples
996    ///
997    /// ```
998    /// #![feature(ascii_char, ascii_char_variants)]
999    /// use std::ascii;
1000    ///
1001    /// let uppercase_a = ascii::Char::CapitalA;
1002    /// let uppercase_g = ascii::Char::CapitalG;
1003    /// let a = ascii::Char::SmallA;
1004    /// let g = ascii::Char::SmallG;
1005    /// let zero = ascii::Char::Digit0;
1006    /// let percent = ascii::Char::PercentSign;
1007    /// let space = ascii::Char::Space;
1008    /// let lf = ascii::Char::LineFeed;
1009    /// let esc = ascii::Char::Escape;
1010    ///
1011    /// assert!(uppercase_a.is_graphic());
1012    /// assert!(uppercase_g.is_graphic());
1013    /// assert!(a.is_graphic());
1014    /// assert!(g.is_graphic());
1015    /// assert!(zero.is_graphic());
1016    /// assert!(percent.is_graphic());
1017    /// assert!(!space.is_graphic());
1018    /// assert!(!lf.is_graphic());
1019    /// assert!(!esc.is_graphic());
1020    /// ```
1021    #[must_use]
1022    #[unstable(feature = "ascii_char", issue = "110998")]
1023    #[inline]
1024    pub const fn is_graphic(self) -> bool {
1025        self.to_u8().is_ascii_graphic()
1026    }
1027
1028    /// Checks if the value is a whitespace character:
1029    /// 0x20 SPACE, 0x09 HORIZONTAL TAB, 0x0A LINE FEED,
1030    /// 0x0C FORM FEED, or 0x0D CARRIAGE RETURN.
1031    ///
1032    /// Rust uses the WhatWG Infra Standard's [definition of ASCII
1033    /// whitespace][infra-aw]. There are several other definitions in
1034    /// wide use. For instance, [the POSIX locale][pct] includes
1035    /// 0x0B VERTICAL TAB as well as all the above characters,
1036    /// but—from the very same specification—[the default rule for
1037    /// "field splitting" in the Bourne shell][bfs] considers *only*
1038    /// SPACE, HORIZONTAL TAB, and LINE FEED as whitespace.
1039    ///
1040    /// If you are writing a program that will process an existing
1041    /// file format, check what that format's definition of whitespace is
1042    /// before using this function.
1043    ///
1044    /// [infra-aw]: https://infra.spec.whatwg.org/#ascii-whitespace
1045    /// [pct]: https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap07.html#tag_07_03_01
1046    /// [bfs]: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_05
1047    ///
1048    /// # Examples
1049    ///
1050    /// ```
1051    /// #![feature(ascii_char, ascii_char_variants)]
1052    /// use std::ascii;
1053    ///
1054    /// let uppercase_a = ascii::Char::CapitalA;
1055    /// let uppercase_g = ascii::Char::CapitalG;
1056    /// let a = ascii::Char::SmallA;
1057    /// let g = ascii::Char::SmallG;
1058    /// let zero = ascii::Char::Digit0;
1059    /// let percent = ascii::Char::PercentSign;
1060    /// let space = ascii::Char::Space;
1061    /// let lf = ascii::Char::LineFeed;
1062    /// let esc = ascii::Char::Escape;
1063    ///
1064    /// assert!(!uppercase_a.is_whitespace());
1065    /// assert!(!uppercase_g.is_whitespace());
1066    /// assert!(!a.is_whitespace());
1067    /// assert!(!g.is_whitespace());
1068    /// assert!(!zero.is_whitespace());
1069    /// assert!(!percent.is_whitespace());
1070    /// assert!(space.is_whitespace());
1071    /// assert!(lf.is_whitespace());
1072    /// assert!(!esc.is_whitespace());
1073    /// ```
1074    #[must_use]
1075    #[unstable(feature = "ascii_char", issue = "110998")]
1076    #[inline]
1077    pub const fn is_whitespace(self) -> bool {
1078        self.to_u8().is_ascii_whitespace()
1079    }
1080
1081    /// Checks if the value is a control character:
1082    /// 0x00 NUL ..= 0x1F UNIT SEPARATOR, or 0x7F DELETE.
1083    /// Note that most whitespace characters are control
1084    /// characters, but SPACE is not.
1085    ///
1086    /// # Examples
1087    ///
1088    /// ```
1089    /// #![feature(ascii_char, ascii_char_variants)]
1090    /// use std::ascii;
1091    ///
1092    /// let uppercase_a = ascii::Char::CapitalA;
1093    /// let uppercase_g = ascii::Char::CapitalG;
1094    /// let a = ascii::Char::SmallA;
1095    /// let g = ascii::Char::SmallG;
1096    /// let zero = ascii::Char::Digit0;
1097    /// let percent = ascii::Char::PercentSign;
1098    /// let space = ascii::Char::Space;
1099    /// let lf = ascii::Char::LineFeed;
1100    /// let esc = ascii::Char::Escape;
1101    ///
1102    /// assert!(!uppercase_a.is_control());
1103    /// assert!(!uppercase_g.is_control());
1104    /// assert!(!a.is_control());
1105    /// assert!(!g.is_control());
1106    /// assert!(!zero.is_control());
1107    /// assert!(!percent.is_control());
1108    /// assert!(!space.is_control());
1109    /// assert!(lf.is_control());
1110    /// assert!(esc.is_control());
1111    /// ```
1112    #[must_use]
1113    #[unstable(feature = "ascii_char", issue = "110998")]
1114    #[inline]
1115    pub const fn is_control(self) -> bool {
1116        self.to_u8().is_ascii_control()
1117    }
1118
1119    /// Returns an iterator that produces an escaped version of a
1120    /// character.
1121    ///
1122    /// The behavior is identical to
1123    /// [`ascii::escape_default`](crate::ascii::escape_default).
1124    ///
1125    /// # Examples
1126    ///
1127    /// ```
1128    /// #![feature(ascii_char, ascii_char_variants)]
1129    /// use std::ascii;
1130    ///
1131    /// let zero = ascii::Char::Digit0;
1132    /// let tab = ascii::Char::CharacterTabulation;
1133    /// let cr = ascii::Char::CarriageReturn;
1134    /// let lf = ascii::Char::LineFeed;
1135    /// let apostrophe = ascii::Char::Apostrophe;
1136    /// let double_quote = ascii::Char::QuotationMark;
1137    /// let backslash = ascii::Char::ReverseSolidus;
1138    ///
1139    /// assert_eq!("0", zero.escape_ascii().to_string());
1140    /// assert_eq!("\\t", tab.escape_ascii().to_string());
1141    /// assert_eq!("\\r", cr.escape_ascii().to_string());
1142    /// assert_eq!("\\n", lf.escape_ascii().to_string());
1143    /// assert_eq!("\\'", apostrophe.escape_ascii().to_string());
1144    /// assert_eq!("\\\"", double_quote.escape_ascii().to_string());
1145    /// assert_eq!("\\\\", backslash.escape_ascii().to_string());
1146    /// ```
1147    #[must_use = "this returns the escaped character as an iterator, \
1148                  without modifying the original"]
1149    #[unstable(feature = "ascii_char", issue = "110998")]
1150    #[inline]
1151    pub fn escape_ascii(self) -> super::EscapeDefault {
1152        super::escape_default(self.to_u8())
1153    }
1154}
1155
1156macro_rules! into_int_impl {
1157    ($($ty:ty)*) => {
1158        $(
1159            #[unstable(feature = "ascii_char", issue = "110998")]
1160            #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1161            impl const From<AsciiChar> for $ty {
1162                #[inline]
1163                fn from(chr: AsciiChar) -> $ty {
1164                    chr as u8 as $ty
1165                }
1166            }
1167        )*
1168    }
1169}
1170
1171into_int_impl!(u8 u16 u32 u64 u128 char);
1172
1173impl [AsciiChar] {
1174    /// Views this slice of ASCII characters as a UTF-8 `str`.
1175    #[unstable(feature = "ascii_char", issue = "110998")]
1176    #[inline]
1177    pub const fn as_str(&self) -> &str {
1178        let ascii_ptr: *const Self = self;
1179        let str_ptr = ascii_ptr as *const str;
1180        // SAFETY: Each ASCII codepoint in UTF-8 is encoded as one single-byte
1181        // code unit having the same value as the ASCII byte.
1182        unsafe { &*str_ptr }
1183    }
1184
1185    /// Views this slice of ASCII characters as a slice of `u8` bytes.
1186    #[unstable(feature = "ascii_char", issue = "110998")]
1187    #[inline]
1188    pub const fn as_bytes(&self) -> &[u8] {
1189        self.as_str().as_bytes()
1190    }
1191}
1192
1193#[unstable(feature = "ascii_char", issue = "110998")]
1194impl fmt::Display for AsciiChar {
1195    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1196        <str as fmt::Display>::fmt(self.as_str(), f)
1197    }
1198}
1199
1200#[unstable(feature = "ascii_char", issue = "110998")]
1201impl fmt::Debug for AsciiChar {
1202    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1203        use AsciiChar::{Apostrophe, Null, ReverseSolidus as Backslash};
1204
1205        fn backslash(a: AsciiChar) -> ([AsciiChar; 6], usize) {
1206            ([Apostrophe, Backslash, a, Apostrophe, Null, Null], 4)
1207        }
1208
1209        let (buf, len) = match self {
1210            AsciiChar::Null => backslash(AsciiChar::Digit0),
1211            AsciiChar::CharacterTabulation => backslash(AsciiChar::SmallT),
1212            AsciiChar::CarriageReturn => backslash(AsciiChar::SmallR),
1213            AsciiChar::LineFeed => backslash(AsciiChar::SmallN),
1214            AsciiChar::ReverseSolidus => backslash(AsciiChar::ReverseSolidus),
1215            AsciiChar::Apostrophe => backslash(AsciiChar::Apostrophe),
1216            _ if self.to_u8().is_ascii_control() => {
1217                const HEX_DIGITS: [AsciiChar; 16] = *b"0123456789abcdef".as_ascii().unwrap();
1218
1219                let byte = self.to_u8();
1220                let hi = HEX_DIGITS[usize::from(byte >> 4)];
1221                let lo = HEX_DIGITS[usize::from(byte & 0xf)];
1222                ([Apostrophe, Backslash, AsciiChar::SmallX, hi, lo, Apostrophe], 6)
1223            }
1224            _ => ([Apostrophe, *self, Apostrophe, Null, Null, Null], 3),
1225        };
1226
1227        f.write_str(buf[..len].as_str())
1228    }
1229}
````