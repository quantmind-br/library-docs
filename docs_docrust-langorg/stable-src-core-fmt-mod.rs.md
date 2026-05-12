---
title: mod.rs - source
url: https://doc.rust-lang.org/stable/src/core/fmt/mod.rs.html#2910
source: crawler
fetched_at: 2026-05-06T21:33:48.372592344-03:00
rendered_js: false
word_count: 12631
summary: This module provides the foundational traits, types, and utilities for formatting and printing data in Rust, including support for custom formatting implementations and buffer writing.
tags:
    - rust
    - formatting
    - traits
    - io
    - string-manipulation
category: api
---

## core/fmt/ mod.rs

````rust
1//! Utilities for formatting and printing strings.
2
3#![stable(feature = "rust1", since = "1.0.0")]
4
5use crate::cell::{Cell, Ref, RefCell, RefMut, SyncUnsafeCell, UnsafeCell};
6use crate::char::EscapeDebugExtArgs;
7use crate::hint::assert_unchecked;
8use crate::marker::{PhantomData, PointeeSized};
9use crate::num::fmt as numfmt;
10use crate::ops::Deref;
11use crate::ptr::NonNull;
12use crate::{iter, mem, result, str};
13
14mod builders;
15#[cfg(not(no_fp_fmt_parse))]
16mod float;
17#[cfg(no_fp_fmt_parse)]
18mod nofloat;
19mod num;
20mod num_buffer;
21mod rt;
22
23#[stable(feature = "fmt_flags_align", since = "1.28.0")]
24#[rustc_diagnostic_item = "Alignment"]
25/// Possible alignments returned by `Formatter::align`
26#[derive(Copy, Clone, Debug, PartialEq, Eq)]
27pub enum Alignment {
28    #[stable(feature = "fmt_flags_align", since = "1.28.0")]
29    /// Indication that contents should be left-aligned.
30    Left,
31    #[stable(feature = "fmt_flags_align", since = "1.28.0")]
32    /// Indication that contents should be right-aligned.
33    Right,
34    #[stable(feature = "fmt_flags_align", since = "1.28.0")]
35    /// Indication that contents should be center-aligned.
36    Center,
37}
38
39#[unstable(feature = "int_format_into", issue = "138215")]
40pub use num_buffer::{NumBuffer, NumBufferTrait};
41
42#[stable(feature = "debug_builders", since = "1.2.0")]
43pub use self::builders::{DebugList, DebugMap, DebugSet, DebugStruct, DebugTuple};
44#[stable(feature = "fmt_from_fn", since = "1.93.0")]
45pub use self::builders::{FromFn, from_fn};
46
47/// The type returned by formatter methods.
48///
49/// # Examples
50///
51/// ```
52/// use std::fmt;
53///
54/// #[derive(Debug)]
55/// struct Triangle {
56///     a: f32,
57///     b: f32,
58///     c: f32
59/// }
60///
61/// impl fmt::Display for Triangle {
62///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
63///         write!(f, "({}, {}, {})", self.a, self.b, self.c)
64///     }
65/// }
66///
67/// let pythagorean_triple = Triangle { a: 3.0, b: 4.0, c: 5.0 };
68///
69/// assert_eq!(format!("{pythagorean_triple}"), "(3, 4, 5)");
70/// ```
71#[stable(feature = "rust1", since = "1.0.0")]
72pub type Result = result::Result<(), Error>;
73
74/// The error type which is returned from formatting a message into a stream.
75///
76/// This type does not support transmission of an error other than that an error
77/// occurred. This is because, despite the existence of this error,
78/// string formatting is considered an infallible operation.
79/// `fmt()` implementors should not return this `Error` unless they received it from their
80/// [`Formatter`]. The only time your code should create a new instance of this
81/// error is when implementing `fmt::Write`, in order to cancel the formatting operation when
82/// writing to the underlying stream fails.
83///
84/// Any extra information must be arranged to be transmitted through some other means,
85/// such as storing it in a field to be consulted after the formatting operation has been
86/// cancelled. (For example, this is how [`std::io::Write::write_fmt()`] propagates IO errors
87/// during writing.)
88///
89/// This type, `fmt::Error`, should not be
90/// confused with [`std::io::Error`] or [`std::error::Error`], which you may also
91/// have in scope.
92///
93/// [`std::io::Error`]: ../../std/io/struct.Error.html
94/// [`std::io::Write::write_fmt()`]: ../../std/io/trait.Write.html#method.write_fmt
95/// [`std::error::Error`]: ../../std/error/trait.Error.html
96///
97/// # Examples
98///
99/// ```rust
100/// use std::fmt::{self, write};
101///
102/// let mut output = String::new();
103/// if let Err(fmt::Error) = write(&mut output, format_args!("Hello {}!", "world")) {
104///     panic!("An error occurred");
105/// }
106/// ```
107#[stable(feature = "rust1", since = "1.0.0")]
108#[derive(Copy, Clone, Debug, Default, Eq, Hash, Ord, PartialEq, PartialOrd)]
109pub struct Error;
110
111/// A trait for writing or formatting into Unicode-accepting buffers or streams.
112///
113/// This trait only accepts UTF-8–encoded data and is not [flushable]. If you only
114/// want to accept Unicode and you don't need flushing, you should implement this trait;
115/// otherwise you should implement [`std::io::Write`].
116///
117/// [`std::io::Write`]: ../../std/io/trait.Write.html
118/// [flushable]: ../../std/io/trait.Write.html#tymethod.flush
119#[stable(feature = "rust1", since = "1.0.0")]
120#[rustc_diagnostic_item = "FmtWrite"]
121pub trait Write {
122    /// Writes a string slice into this writer, returning whether the write
123    /// succeeded.
124    ///
125    /// This method can only succeed if the entire string slice was successfully
126    /// written, and this method will not return until all data has been
127    /// written or an error occurs.
128    ///
129    /// # Errors
130    ///
131    /// This function will return an instance of [`std::fmt::Error`][Error] on error.
132    ///
133    /// The purpose of that error is to abort the formatting operation when the underlying
134    /// destination encounters some error preventing it from accepting more text;
135    /// in particular, it does not communicate any information about *what* error occurred.
136    /// It should generally be propagated rather than handled, at least when implementing
137    /// formatting traits.
138    ///
139    /// # Examples
140    ///
141    /// ```
142    /// use std::fmt::{Error, Write};
143    ///
144    /// fn writer<W: Write>(f: &mut W, s: &str) -> Result<(), Error> {
145    ///     f.write_str(s)
146    /// }
147    ///
148    /// let mut buf = String::new();
149    /// writer(&mut buf, "hola")?;
150    /// assert_eq!(&buf, "hola");
151    /// # std::fmt::Result::Ok(())
152    /// ```
153    #[stable(feature = "rust1", since = "1.0.0")]
154    fn write_str(&mut self, s: &str) -> Result;
155
156    /// Writes a [`char`] into this writer, returning whether the write succeeded.
157    ///
158    /// A single [`char`] may be encoded as more than one byte.
159    /// This method can only succeed if the entire byte sequence was successfully
160    /// written, and this method will not return until all data has been
161    /// written or an error occurs.
162    ///
163    /// # Errors
164    ///
165    /// This function will return an instance of [`Error`] on error.
166    ///
167    /// # Examples
168    ///
169    /// ```
170    /// use std::fmt::{Error, Write};
171    ///
172    /// fn writer<W: Write>(f: &mut W, c: char) -> Result<(), Error> {
173    ///     f.write_char(c)
174    /// }
175    ///
176    /// let mut buf = String::new();
177    /// writer(&mut buf, 'a')?;
178    /// writer(&mut buf, 'b')?;
179    /// assert_eq!(&buf, "ab");
180    /// # std::fmt::Result::Ok(())
181    /// ```
182    #[stable(feature = "fmt_write_char", since = "1.1.0")]
183    fn write_char(&mut self, c: char) -> Result {
184        self.write_str(c.encode_utf8(&mut [0; char::MAX_LEN_UTF8]))
185    }
186
187    /// Glue for usage of the [`write!`] macro with implementors of this trait.
188    ///
189    /// This method should generally not be invoked manually, but rather through
190    /// the [`write!`] macro itself.
191    ///
192    /// # Errors
193    ///
194    /// This function will return an instance of [`Error`] on error. Please see
195    /// [write_str](Write::write_str) for details.
196    ///
197    /// # Examples
198    ///
199    /// ```
200    /// use std::fmt::{Error, Write};
201    ///
202    /// fn writer<W: Write>(f: &mut W, s: &str) -> Result<(), Error> {
203    ///     f.write_fmt(format_args!("{s}"))
204    /// }
205    ///
206    /// let mut buf = String::new();
207    /// writer(&mut buf, "world")?;
208    /// assert_eq!(&buf, "world");
209    /// # std::fmt::Result::Ok(())
210    /// ```
211    #[stable(feature = "rust1", since = "1.0.0")]
212    fn write_fmt(&mut self, args: Arguments<'_>) -> Result {
213        // We use a specialization for `Sized` types to avoid an indirection
214        // through `&mut self`
215        trait SpecWriteFmt {
216            fn spec_write_fmt(self, args: Arguments<'_>) -> Result;
217        }
218
219        impl<W: Write + ?Sized> SpecWriteFmt for &mut W {
220            #[inline]
221            default fn spec_write_fmt(mut self, args: Arguments<'_>) -> Result {
222                if let Some(s) = args.as_statically_known_str() {
223                    self.write_str(s)
224                } else {
225                    write(&mut self, args)
226                }
227            }
228        }
229
230        impl<W: Write> SpecWriteFmt for &mut W {
231            #[inline]
232            fn spec_write_fmt(self, args: Arguments<'_>) -> Result {
233                if let Some(s) = args.as_statically_known_str() {
234                    self.write_str(s)
235                } else {
236                    write(self, args)
237                }
238            }
239        }
240
241        self.spec_write_fmt(args)
242    }
243}
244
245#[stable(feature = "fmt_write_blanket_impl", since = "1.4.0")]
246impl<W: Write + ?Sized> Write for &mut W {
247    fn write_str(&mut self, s: &str) -> Result {
248        (**self).write_str(s)
249    }
250
251    fn write_char(&mut self, c: char) -> Result {
252        (**self).write_char(c)
253    }
254
255    fn write_fmt(&mut self, args: Arguments<'_>) -> Result {
256        (**self).write_fmt(args)
257    }
258}
259
260/// The signedness of a [`Formatter`] (or of a [`FormattingOptions`]).
261#[derive(Copy, Clone, Debug, PartialEq, Eq)]
262#[unstable(feature = "formatting_options", issue = "118117")]
263pub enum Sign {
264    /// Represents the `+` flag.
265    Plus,
266    /// Represents the `-` flag.
267    Minus,
268}
269
270/// Specifies whether the [`Debug`] trait should use lower-/upper-case
271/// hexadecimal or normal integers.
272#[derive(Copy, Clone, Debug, PartialEq, Eq)]
273#[unstable(feature = "formatting_options", issue = "118117")]
274pub enum DebugAsHex {
275    /// Use lower-case hexadecimal integers for the `Debug` trait (like [the `x?` type](../../std/fmt/index.html#formatting-traits)).
276    Lower,
277    /// Use upper-case hexadecimal integers for the `Debug` trait (like [the `X?` type](../../std/fmt/index.html#formatting-traits)).
278    Upper,
279}
280
281/// Options for formatting.
282///
283/// `FormattingOptions` is a [`Formatter`] without an attached [`Write`] trait.
284/// It is mainly used to construct `Formatter` instances.
285#[derive(Copy, Clone, Debug, PartialEq, Eq)]
286#[unstable(feature = "formatting_options", issue = "118117")]
287pub struct FormattingOptions {
288    /// Flags, with the following bit fields:
289    ///
290    /// ```text
291    ///   31  30  29  28  27  26  25  24  23  22  21  20                              0
292    /// ┌───┬───────┬───┬───┬───┬───┬───┬───┬───┬───┬──────────────────────────────────┐
293    /// │ 0 │ align │ p │ w │ X?│ x?│'0'│ # │ - │ + │               fill               │
294    /// └───┴───────┴───┴───┴───┴───┴───┴───┴───┴───┴──────────────────────────────────┘
295    ///   │     │     │   │  └─┬───────────────────┘ └─┬──────────────────────────────┘
296    ///   │     │     │   │    │                       └─ The fill character (21 bits char).
297    ///   │     │     │   │    └─ The debug upper/lower hex, zero pad, alternate, and plus/minus flags.
298    ///   │     │     │   └─ Whether a width is set. (The value is stored separately.)
299    ///   │     │     └─ Whether a precision is set. (The value is stored separately.)
300    ///   │     ├─ 0: Align left. (<)
301    ///   │     ├─ 1: Align right. (>)
302    ///   │     ├─ 2: Align center. (^)
303    ///   │     └─ 3: Alignment not set. (default)
304    ///   └─ Always zero.
305    /// ```
306    // Note: This could use a pattern type with range 0x0000_0000..=0x7dd0ffff.
307    // It's unclear if that's useful, though.
308    flags: u32,
309    /// Width if width flag (bit 27) above is set. Otherwise, always 0.
310    width: u16,
311    /// Precision if precision flag (bit 28) above is set. Otherwise, always 0.
312    precision: u16,
313}
314
315// This needs to match with compiler/rustc_ast_lowering/src/format.rs.
316mod flags {
317    pub(super) const SIGN_PLUS_FLAG: u32 = 1 << 21;
318    pub(super) const SIGN_MINUS_FLAG: u32 = 1 << 22;
319    pub(super) const ALTERNATE_FLAG: u32 = 1 << 23;
320    pub(super) const SIGN_AWARE_ZERO_PAD_FLAG: u32 = 1 << 24;
321    pub(super) const DEBUG_LOWER_HEX_FLAG: u32 = 1 << 25;
322    pub(super) const DEBUG_UPPER_HEX_FLAG: u32 = 1 << 26;
323    pub(super) const WIDTH_FLAG: u32 = 1 << 27;
324    pub(super) const PRECISION_FLAG: u32 = 1 << 28;
325    pub(super) const ALIGN_BITS: u32 = 0b11 << 29;
326    pub(super) const ALIGN_LEFT: u32 = 0 << 29;
327    pub(super) const ALIGN_RIGHT: u32 = 1 << 29;
328    pub(super) const ALIGN_CENTER: u32 = 2 << 29;
329    pub(super) const ALIGN_UNKNOWN: u32 = 3 << 29;
330}
331
332impl FormattingOptions {
333    /// Construct a new `FormatterBuilder` with the supplied `Write` trait
334    /// object for output that is equivalent to the `{}` formatting
335    /// specifier:
336    ///
337    /// - no flags,
338    /// - filled with spaces,
339    /// - no alignment,
340    /// - no width,
341    /// - no precision, and
342    /// - no [`DebugAsHex`] output mode.
343    #[unstable(feature = "formatting_options", issue = "118117")]
344    pub const fn new() -> Self {
345        Self { flags: ' ' as u32 | flags::ALIGN_UNKNOWN, width: 0, precision: 0 }
346    }
347
348    /// Sets or removes the sign (the `+` or the `-` flag).
349    ///
350    /// - `+`: This is intended for numeric types and indicates that the sign
351    ///   should always be printed. By default only the negative sign of signed
352    ///   values is printed, and the sign of positive or unsigned values is
353    ///   omitted. This flag indicates that the correct sign (+ or -) should
354    ///   always be printed.
355    /// - `-`: Currently not used
356    #[unstable(feature = "formatting_options", issue = "118117")]
357    pub const fn sign(&mut self, sign: Option<Sign>) -> &mut Self {
358        let sign = match sign {
359            None => 0,
360            Some(Sign::Plus) => flags::SIGN_PLUS_FLAG,
361            Some(Sign::Minus) => flags::SIGN_MINUS_FLAG,
362        };
363        self.flags = self.flags & !(flags::SIGN_PLUS_FLAG | flags::SIGN_MINUS_FLAG) | sign;
364        self
365    }
366    /// Sets or unsets the `0` flag.
367    ///
368    /// This is used to indicate for integer formats that the padding to width should both be done with a 0 character as well as be sign-aware
369    #[unstable(feature = "formatting_options", issue = "118117")]
370    pub const fn sign_aware_zero_pad(&mut self, sign_aware_zero_pad: bool) -> &mut Self {
371        if sign_aware_zero_pad {
372            self.flags |= flags::SIGN_AWARE_ZERO_PAD_FLAG;
373        } else {
374            self.flags &= !flags::SIGN_AWARE_ZERO_PAD_FLAG;
375        }
376        self
377    }
378    /// Sets or unsets the `#` flag.
379    ///
380    /// This flag indicates that the "alternate" form of printing should be
381    /// used. The alternate forms are:
382    /// - [`Debug`] : pretty-print the [`Debug`] formatting (adds linebreaks and indentation)
383    /// - [`LowerHex`] as well as [`UpperHex`] - precedes the argument with a `0x`
384    /// - [`Octal`] - precedes the argument with a `0o`
385    /// - [`Binary`] - precedes the argument with a `0b`
386    #[unstable(feature = "formatting_options", issue = "118117")]
387    pub const fn alternate(&mut self, alternate: bool) -> &mut Self {
388        if alternate {
389            self.flags |= flags::ALTERNATE_FLAG;
390        } else {
391            self.flags &= !flags::ALTERNATE_FLAG;
392        }
393        self
394    }
395    /// Sets the fill character.
396    ///
397    /// The optional fill character and alignment is provided normally in
398    /// conjunction with the width parameter. This indicates that if the value
399    /// being formatted is smaller than width some extra characters will be
400    /// printed around it.
401    #[unstable(feature = "formatting_options", issue = "118117")]
402    pub const fn fill(&mut self, fill: char) -> &mut Self {
403        self.flags = self.flags & (u32::MAX << 21) | fill as u32;
404        self
405    }
406    /// Sets or removes the alignment.
407    ///
408    /// The alignment specifies how the value being formatted should be
409    /// positioned if it is smaller than the width of the formatter.
410    #[unstable(feature = "formatting_options", issue = "118117")]
411    pub const fn align(&mut self, align: Option<Alignment>) -> &mut Self {
412        let align: u32 = match align {
413            Some(Alignment::Left) => flags::ALIGN_LEFT,
414            Some(Alignment::Right) => flags::ALIGN_RIGHT,
415            Some(Alignment::Center) => flags::ALIGN_CENTER,
416            None => flags::ALIGN_UNKNOWN,
417        };
418        self.flags = self.flags & !flags::ALIGN_BITS | align;
419        self
420    }
421    /// Sets or removes the width.
422    ///
423    /// This is a parameter for the “minimum width” that the format should take
424    /// up. If the value’s string does not fill up this many characters, then
425    /// the padding specified by [`FormattingOptions::fill`]/[`FormattingOptions::align`]
426    /// will be used to take up the required space.
427    #[unstable(feature = "formatting_options", issue = "118117")]
428    pub const fn width(&mut self, width: Option<u16>) -> &mut Self {
429        if let Some(width) = width {
430            self.flags |= flags::WIDTH_FLAG;
431            self.width = width;
432        } else {
433            self.flags &= !flags::WIDTH_FLAG;
434            self.width = 0;
435        }
436        self
437    }
438    /// Sets or removes the precision.
439    ///
440    /// - For non-numeric types, this can be considered a “maximum width”. If
441    ///   the resulting string is longer than this width, then it is truncated
442    ///   down to this many characters and that truncated value is emitted with
443    ///   proper fill, alignment and width if those parameters are set.
444    /// - For integral types, this is ignored.
445    /// - For floating-point types, this indicates how many digits after the
446    /// decimal point should be printed.
447    #[unstable(feature = "formatting_options", issue = "118117")]
448    pub const fn precision(&mut self, precision: Option<u16>) -> &mut Self {
449        if let Some(precision) = precision {
450            self.flags |= flags::PRECISION_FLAG;
451            self.precision = precision;
452        } else {
453            self.flags &= !flags::PRECISION_FLAG;
454            self.precision = 0;
455        }
456        self
457    }
458    /// Specifies whether the [`Debug`] trait should use lower-/upper-case
459    /// hexadecimal or normal integers
460    #[unstable(feature = "formatting_options", issue = "118117")]
461    pub const fn debug_as_hex(&mut self, debug_as_hex: Option<DebugAsHex>) -> &mut Self {
462        let debug_as_hex = match debug_as_hex {
463            None => 0,
464            Some(DebugAsHex::Lower) => flags::DEBUG_LOWER_HEX_FLAG,
465            Some(DebugAsHex::Upper) => flags::DEBUG_UPPER_HEX_FLAG,
466        };
467        self.flags = self.flags & !(flags::DEBUG_LOWER_HEX_FLAG | flags::DEBUG_UPPER_HEX_FLAG)
468            | debug_as_hex;
469        self
470    }
471
472    /// Returns the current sign (the `+` or the `-` flag).
473    #[unstable(feature = "formatting_options", issue = "118117")]
474    pub const fn get_sign(&self) -> Option<Sign> {
475        if self.flags & flags::SIGN_PLUS_FLAG != 0 {
476            Some(Sign::Plus)
477        } else if self.flags & flags::SIGN_MINUS_FLAG != 0 {
478            Some(Sign::Minus)
479        } else {
480            None
481        }
482    }
483    /// Returns the current `0` flag.
484    #[unstable(feature = "formatting_options", issue = "118117")]
485    pub const fn get_sign_aware_zero_pad(&self) -> bool {
486        self.flags & flags::SIGN_AWARE_ZERO_PAD_FLAG != 0
487    }
488    /// Returns the current `#` flag.
489    #[unstable(feature = "formatting_options", issue = "118117")]
490    pub const fn get_alternate(&self) -> bool {
491        self.flags & flags::ALTERNATE_FLAG != 0
492    }
493    /// Returns the current fill character.
494    #[unstable(feature = "formatting_options", issue = "118117")]
495    pub const fn get_fill(&self) -> char {
496        // SAFETY: We only ever put a valid `char` in the lower 21 bits of the flags field.
497        unsafe { char::from_u32_unchecked(self.flags & 0x1FFFFF) }
498    }
499    /// Returns the current alignment.
500    #[unstable(feature = "formatting_options", issue = "118117")]
501    pub const fn get_align(&self) -> Option<Alignment> {
502        match self.flags & flags::ALIGN_BITS {
503            flags::ALIGN_LEFT => Some(Alignment::Left),
504            flags::ALIGN_RIGHT => Some(Alignment::Right),
505            flags::ALIGN_CENTER => Some(Alignment::Center),
506            _ => None,
507        }
508    }
509    /// Returns the current width.
510    #[unstable(feature = "formatting_options", issue = "118117")]
511    pub const fn get_width(&self) -> Option<u16> {
512        if self.flags & flags::WIDTH_FLAG != 0 { Some(self.width) } else { None }
513    }
514    /// Returns the current precision.
515    #[unstable(feature = "formatting_options", issue = "118117")]
516    pub const fn get_precision(&self) -> Option<u16> {
517        if self.flags & flags::PRECISION_FLAG != 0 { Some(self.precision) } else { None }
518    }
519    /// Returns the current precision.
520    #[unstable(feature = "formatting_options", issue = "118117")]
521    pub const fn get_debug_as_hex(&self) -> Option<DebugAsHex> {
522        if self.flags & flags::DEBUG_LOWER_HEX_FLAG != 0 {
523            Some(DebugAsHex::Lower)
524        } else if self.flags & flags::DEBUG_UPPER_HEX_FLAG != 0 {
525            Some(DebugAsHex::Upper)
526        } else {
527            None
528        }
529    }
530
531    /// Creates a [`Formatter`] that writes its output to the given [`Write`] trait.
532    ///
533    /// You may alternatively use [`Formatter::new()`].
534    #[unstable(feature = "formatting_options", issue = "118117")]
535    pub const fn create_formatter<'a>(self, write: &'a mut (dyn Write + 'a)) -> Formatter<'a> {
536        Formatter { options: self, buf: write }
537    }
538}
539
540#[unstable(feature = "formatting_options", issue = "118117")]
541impl Default for FormattingOptions {
542    /// Same as [`FormattingOptions::new()`].
543    fn default() -> Self {
544        // The `#[derive(Default)]` implementation would set `fill` to `\0` instead of space.
545        Self::new()
546    }
547}
548
549/// Configuration for formatting.
550///
551/// A `Formatter` represents various options related to formatting. Users do not
552/// construct `Formatter`s directly; a mutable reference to one is passed to
553/// the `fmt` method of all formatting traits, like [`Debug`] and [`Display`].
554///
555/// To interact with a `Formatter`, you'll call various methods to change the
556/// various options related to formatting. For examples, please see the
557/// documentation of the methods defined on `Formatter` below.
558#[allow(missing_debug_implementations)]
559#[stable(feature = "rust1", since = "1.0.0")]
560#[rustc_diagnostic_item = "Formatter"]
561pub struct Formatter<'a> {
562    options: FormattingOptions,
563
564    buf: &'a mut (dyn Write + 'a),
565}
566
567impl<'a> Formatter<'a> {
568    /// Creates a new formatter with given [`FormattingOptions`].
569    ///
570    /// If `write` is a reference to a formatter, it is recommended to use
571    /// [`Formatter::with_options`] instead as this can borrow the underlying
572    /// `write`, thereby bypassing one layer of indirection.
573    ///
574    /// You may alternatively use [`FormattingOptions::create_formatter()`].
575    #[unstable(feature = "formatting_options", issue = "118117")]
576    pub const fn new(write: &'a mut (dyn Write + 'a), options: FormattingOptions) -> Self {
577        Formatter { options, buf: write }
578    }
579
580    /// Creates a new formatter based on this one with given [`FormattingOptions`].
581    #[unstable(feature = "formatting_options", issue = "118117")]
582    pub const fn with_options<'b>(&'b mut self, options: FormattingOptions) -> Formatter<'b> {
583        Formatter { options, buf: self.buf }
584    }
585}
586
587/// This structure represents a safely precompiled version of a format string
588/// and its arguments. This cannot be generated at runtime because it cannot
589/// safely be done, so no constructors are given and the fields are private
590/// to prevent modification.
591///
592/// The [`format_args!`] macro will safely create an instance of this structure.
593/// The macro validates the format string at compile-time so usage of the
594/// [`write()`] and [`format()`] functions can be safely performed.
595///
596/// You can use the `Arguments<'a>` that [`format_args!`] returns in `Debug`
597/// and `Display` contexts as seen below. The example also shows that `Debug`
598/// and `Display` format to the same thing: the interpolated format string
599/// in `format_args!`.
600///
601/// ```rust
602/// let debug = format!("{:?}", format_args!("{} foo {:?}", 1, 2));
603/// let display = format!("{}", format_args!("{} foo {:?}", 1, 2));
604/// assert_eq!("1 foo 2", display);
605/// assert_eq!(display, debug);
606/// ```
607///
608/// [`format()`]: ../../std/fmt/fn.format.html
609//
610// Internal representation:
611//
612// fmt::Arguments is represented in one of two ways:
613//
614// 1) String literal representation (e.g. format_args!("hello"))
615//             ┌────────────────────────────────┐
616//   template: │           *const u8            │ ─▷ "hello"
617//             ├──────────────────────────────┬─┤
618//   args:     │             len              │1│ (lowest bit is 1; field contains `len << 1 | 1`)
619//             └──────────────────────────────┴─┘
620//   In this representation, there are no placeholders and `fmt::Arguments::as_str()` returns Some.
621//   The pointer points to the start of a static `str`. The length is given by `args as usize >> 1`.
622//   (The length of a `&str` is isize::MAX at most, so it always fits in a usize minus one bit.)
623//
624//   `fmt::Arguments::from_str()` constructs this representation from a `&'static str`.
625//
626// 2) Placeholders representation (e.g. format_args!("hello {name}\n"))
627//             ┌────────────────────────────────┐
628//   template: │           *const u8            │ ─▷ b"\x06hello \xC0\x01\n\x00"
629//             ├────────────────────────────────┤
630//   args:     │     &'a [Argument<'a>; _]     0│ (lower bit is 0 due to alignment of Argument type)
631//             └────────────────────────────────┘
632//   In this representation, the template is a byte sequence encoding both the literal string pieces
633//   and the placeholders (including their options/flags).
634//
635//   The `args` pointer points to an array of `fmt::Argument<'a>` values, of sufficient length to
636//   match the placeholders in the template.
637//
638//   `fmt::Arguments::new()` constructs this representation from a template byte slice and a slice
639//   of arguments. This function is unsafe, as the template is assumed to be valid and the args
640//   slice is assumed to have elements matching the template.
641//
642//   The template byte sequence is the concatenation of parts of the following types:
643//
644//   - Literal string piece:
645//         Pieces that must be formatted verbatim (e.g. "hello " and "\n" in "hello {name}\n")
646//         appear literally in the template byte sequence, prefixed by their length.
647//
648//         For pieces of up to 127 bytes, these are  represented as a single byte containing the
649//         length followed directly by the bytes of the string:
650//         ┌───┬────────────────────────────┐
651//         │len│    `len` bytes (utf-8)     │ (e.g. b"\x06hello ")
652//         └───┴────────────────────────────┘
653//
654//         For larger pieces up to u16::MAX bytes, these are  represented as a 0x80 followed by
655//         their length in 16-bit little endian, followed by the bytes of the string:
656//         ┌────┬─────────┬───────────────────────────┐
657//         │0x80│   len   │   `len` bytes (utf-8)     │ (e.g. b"\x80\x00\x01hello … ")
658//         └────┴─────────┴───────────────────────────┘
659//
660//         Longer pieces are split into multiple pieces of max u16::MAX bytes (at utf-8 boundaries).
661//
662//   - Placeholder:
663//         Placeholders (e.g. `{name}` in "hello {name}") are represented as a byte with the highest
664//         two bits set, followed by zero or more fields depending on the flags in the first byte:
665//         ┌──────────┬┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┬┄┄┄┄┄┄┄┄┄┄┄┬┄┄┄┄┄┄┄┄┄┄┄┬┄┄┄┄┄┄┄┄┄┄┄┐
666//         │0b11______│       flags       ┊   width   ┊ precision ┊ arg_index ┊ (e.g. b"\xC2\x05\0")
667//         └────││││││┴┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┴┄┄┄┄┄┄┄┄┄┄┄┴┄┄┄┄┄┄┄┄┄┄┄┴┄┄┄┄┄┄┄┄┄┄┄┘
668//              ││││││        32 bit          16 bit      16 bit      16 bit
669//              │││││└─ flags present
670//              ││││└─ width present
671//              │││└─ precision present
672//              ││└─ arg_index present
673//              │└─ width indirect
674//              └─ precision indirect
675//
676//         All fields other than the first byte are optional and only present when their
677//         corresponding flag is set in the first byte.
678//
679//         So, a fully default placeholder without any options is just a single byte:
680//         ┌──────────┐
681//         │0b11000000│ (b"\xC0")
682//         └──────────┘
683//
684//         The fields are stored as little endian.
685//
686//         The `flags` fields corresponds to the `flags` field of `FormattingOptions`.
687//         See doc comment of `FormattingOptions::flags` for details.
688//
689//         The `width` and `precision` fields correspond to their respective fields in
690//         `FormattingOptions`. However, if their "indirect" flag is set, the field contains the
691//         index in the `args` array where the dynamic width or precision is stored, rather than the
692//         value directly.
693//
694//         The `arg_index` field is the index into the `args` array for the argument to be
695//         formatted.
696//
697//         If omitted, the flags, width and precision of the default FormattingOptions::new() are
698//         used.
699//
700//         If the `arg_index` is omitted, the next argument in the `args` array is used (starting
701//         at 0).
702//
703//   - End:
704//         A single zero byte marks the end of the template:
705//         ┌───┐
706//         │ 0 │ ("\0")
707//         └───┘
708//
709//         (Note that a zero byte may also occur naturally as part of the string pieces or flags,
710//         width, precision and arg_index fields above. That is, the template byte sequence ends
711//         with a 0 byte, but isn't terminated by the first 0 byte.)
712//
713#[lang = "format_arguments"]
714#[stable(feature = "rust1", since = "1.0.0")]
715#[derive(Copy, Clone)]
716pub struct Arguments<'a> {
717    template: NonNull<u8>,
718    args: NonNull<rt::Argument<'a>>,
719}
720
721/// Used by the format_args!() macro to create a fmt::Arguments object.
722#[doc(hidden)]
723#[rustc_diagnostic_item = "FmtArgumentsNew"]
724#[unstable(feature = "fmt_internals", issue = "none")]
725impl<'a> Arguments<'a> {
726    // SAFETY: The caller must ensure that the provided template and args encode a valid
727    // fmt::Arguments, as documented above.
728    #[inline]
729    pub unsafe fn new<const N: usize, const M: usize>(
730        template: &'a [u8; N],
731        args: &'a [rt::Argument<'a>; M],
732    ) -> Arguments<'a> {
733        // SAFETY: Responsibility of the caller.
734        unsafe { Arguments { template: mem::transmute(template), args: mem::transmute(args) } }
735    }
736
737    // Same as `from_str`, but not const.
738    // Used by format_args!() expansion when arguments are inlined,
739    // e.g. format_args!("{}", 123), which is not allowed in const.
740    #[inline]
741    pub fn from_str_nonconst(s: &'static str) -> Arguments<'a> {
742        Arguments::from_str(s)
743    }
744}
745
746#[doc(hidden)]
747#[unstable(feature = "fmt_internals", issue = "none")]
748impl<'a> Arguments<'a> {
749    /// Estimates the length of the formatted text.
750    ///
751    /// This is intended to be used for setting initial `String` capacity
752    /// when using `format!`. Note: this is neither the lower nor upper bound.
753    #[inline]
754    pub fn estimated_capacity(&self) -> usize {
755        if let Some(s) = self.as_str() {
756            return s.len();
757        }
758        // Iterate over the template, counting the length of literal pieces.
759        let mut length = 0usize;
760        let mut starts_with_placeholder = false;
761        let mut template = self.template;
762        loop {
763            // SAFETY: We can assume the template is valid.
764            unsafe {
765                let n = template.read();
766                template = template.add(1);
767                if n == 0 {
768                    // End of template.
769                    break;
770                } else if n < 128 {
771                    // Short literal string piece.
772                    length += n as usize;
773                    template = template.add(n as usize);
774                } else if n == 128 {
775                    // Long literal string piece.
776                    let len = usize::from(u16::from_le_bytes(template.cast_array().read()));
777                    length += len;
778                    template = template.add(2 + len);
779                } else {
780                    assert_unchecked(n >= 0xC0);
781                    // Placeholder piece.
782                    if length == 0 {
783                        starts_with_placeholder = true;
784                    }
785                    // Skip remainder of placeholder:
786                    let skip = (n & 1 != 0) as usize * 4 // flags (32 bit)
787                        + (n & 2 != 0) as usize * 2  // width     (16 bit)
788                        + (n & 4 != 0) as usize * 2  // precision (16 bit)
789                        + (n & 8 != 0) as usize * 2; // arg_index (16 bit)
790                    template = template.add(skip as usize);
791                }
792            }
793        }
794
795        if starts_with_placeholder && length < 16 {
796            // If the format string starts with a placeholder,
797            // don't preallocate anything, unless length
798            // of literal pieces is significant.
799            0
800        } else {
801            // There are some placeholders, so any additional push
802            // will reallocate the string. To avoid that,
803            // we're "pre-doubling" the capacity here.
804            length.wrapping_mul(2)
805        }
806    }
807}
808
809impl<'a> Arguments<'a> {
810    /// Create a `fmt::Arguments` object for a single static string.
811    ///
812    /// Formatting this `fmt::Arguments` will just produce the string as-is.
813    #[inline]
814    #[unstable(feature = "fmt_arguments_from_str", issue = "148905")]
815    pub const fn from_str(s: &'static str) -> Arguments<'a> {
816        // SAFETY: This is the "static str" representation of fmt::Arguments; see above.
817        unsafe {
818            Arguments {
819                template: mem::transmute(s.as_ptr()),
820                args: mem::transmute(s.len() << 1 | 1),
821            }
822        }
823    }
824
825    /// Gets the formatted string, if it has no arguments to be formatted at runtime.
826    ///
827    /// This can be used to avoid allocations in some cases.
828    ///
829    /// # Guarantees
830    ///
831    /// For `format_args!("just a literal")`, this function is guaranteed to
832    /// return `Some("just a literal")`.
833    ///
834    /// For most cases with placeholders, this function will return `None`.
835    ///
836    /// However, the compiler may perform optimizations that can cause this
837    /// function to return `Some(_)` even if the format string contains
838    /// placeholders. For example, `format_args!("Hello, {}!", "world")` may be
839    /// optimized to `format_args!("Hello, world!")`, such that `as_str()`
840    /// returns `Some("Hello, world!")`.
841    ///
842    /// The behavior for anything but the trivial case (without placeholders)
843    /// is not guaranteed, and should not be relied upon for anything other
844    /// than optimization.
845    ///
846    /// # Examples
847    ///
848    /// ```rust
849    /// use std::fmt::Arguments;
850    ///
851    /// fn write_str(_: &str) { /* ... */ }
852    ///
853    /// fn write_fmt(args: &Arguments<'_>) {
854    ///     if let Some(s) = args.as_str() {
855    ///         write_str(s)
856    ///     } else {
857    ///         write_str(&args.to_string());
858    ///     }
859    /// }
860    /// ```
861    ///
862    /// ```rust
863    /// assert_eq!(format_args!("hello").as_str(), Some("hello"));
864    /// assert_eq!(format_args!("").as_str(), Some(""));
865    /// assert_eq!(format_args!("{:?}", std::env::current_dir()).as_str(), None);
866    /// ```
867    #[stable(feature = "fmt_as_str", since = "1.52.0")]
868    #[rustc_const_stable(feature = "const_arguments_as_str", since = "1.84.0")]
869    #[must_use]
870    #[inline]
871    pub const fn as_str(&self) -> Option<&'static str> {
872        // SAFETY: During const eval, `self.args` must have come from a usize,
873        // not a pointer, because that's the only way to create a fmt::Arguments in const.
874        // (I.e. only fmt::Arguments::from_str is const, fmt::Arguments::new is not.)
875        //
876        // Outside const eval, transmuting a pointer to a usize is fine.
877        let bits: usize = unsafe { mem::transmute(self.args) };
878        if bits & 1 == 1 {
879            // SAFETY: This fmt::Arguments stores a &'static str. See encoding documentation above.
880            Some(unsafe {
881                str::from_utf8_unchecked(crate::slice::from_raw_parts(
882                    self.template.as_ptr(),
883                    bits >> 1,
884                ))
885            })
886        } else {
887            None
888        }
889    }
890
891    /// Same as [`Arguments::as_str`], but will only return `Some(s)` if it can be determined at compile time.
892    #[unstable(feature = "fmt_internals", reason = "internal to standard library", issue = "none")]
893    #[must_use]
894    #[inline]
895    #[doc(hidden)]
896    pub fn as_statically_known_str(&self) -> Option<&'static str> {
897        let s = self.as_str();
898        if core::intrinsics::is_val_statically_known(s.is_some()) { s } else { None }
899    }
900}
901
902// Manually implementing these results in better error messages.
903#[stable(feature = "rust1", since = "1.0.0")]
904impl !Send for Arguments<'_> {}
905#[stable(feature = "rust1", since = "1.0.0")]
906impl !Sync for Arguments<'_> {}
907
908#[stable(feature = "rust1", since = "1.0.0")]
909impl Debug for Arguments<'_> {
910    fn fmt(&self, fmt: &mut Formatter<'_>) -> Result {
911        Display::fmt(self, fmt)
912    }
913}
914
915#[stable(feature = "rust1", since = "1.0.0")]
916impl Display for Arguments<'_> {
917    fn fmt(&self, fmt: &mut Formatter<'_>) -> Result {
918        write(fmt.buf, *self)
919    }
920}
921
922/// `?` formatting.
923///
924/// `Debug` should format the output in a programmer-facing, debugging context.
925///
926/// Generally speaking, you should just `derive` a `Debug` implementation.
927///
928/// When used with the alternate format specifier `#?`, the output is pretty-printed.
929///
930/// For more information on formatters, see [the module-level documentation][module].
931///
932/// [module]: ../../std/fmt/index.html
933///
934/// This trait can be used with `#[derive]` if all fields implement `Debug`. When
935/// `derive`d for structs, it will use the name of the `struct`, then `{`, then a
936/// comma-separated list of each field's name and `Debug` value, then `}`. For
937/// `enum`s, it will use the name of the variant and, if applicable, `(`, then the
938/// `Debug` values of the fields, then `)`.
939///
940/// # Stability
941///
942/// Derived `Debug` formats are not stable, and so may change with future Rust
943/// versions. Additionally, `Debug` implementations of types provided by the
944/// standard library (`std`, `core`, `alloc`, etc.) are not stable, and
945/// may also change with future Rust versions.
946///
947/// # Examples
948///
949/// Deriving an implementation:
950///
951/// ```
952/// #[derive(Debug)]
953/// struct Point {
954///     x: i32,
955///     y: i32,
956/// }
957///
958/// let origin = Point { x: 0, y: 0 };
959///
960/// assert_eq!(
961///     format!("The origin is: {origin:?}"),
962///     "The origin is: Point { x: 0, y: 0 }",
963/// );
964/// ```
965///
966/// Manually implementing:
967///
968/// ```
969/// use std::fmt;
970///
971/// struct Point {
972///     x: i32,
973///     y: i32,
974/// }
975///
976/// impl fmt::Debug for Point {
977///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
978///         f.debug_struct("Point")
979///          .field("x", &self.x)
980///          .field("y", &self.y)
981///          .finish()
982///     }
983/// }
984///
985/// let origin = Point { x: 0, y: 0 };
986///
987/// assert_eq!(
988///     format!("The origin is: {origin:?}"),
989///     "The origin is: Point { x: 0, y: 0 }",
990/// );
991/// ```
992///
993/// There are a number of helper methods on the [`Formatter`] struct to help you with manual
994/// implementations, such as [`debug_struct`].
995///
996/// [`debug_struct`]: Formatter::debug_struct
997///
998/// Types that do not wish to use the standard suite of debug representations
999/// provided by the `Formatter` trait (`debug_struct`, `debug_tuple`,
1000/// `debug_list`, `debug_set`, `debug_map`) can do something totally custom by
1001/// manually writing an arbitrary representation to the `Formatter`.
1002///
1003/// ```
1004/// # use std::fmt;
1005/// # struct Point {
1006/// #     x: i32,
1007/// #     y: i32,
1008/// # }
1009/// #
1010/// impl fmt::Debug for Point {
1011///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1012///         write!(f, "Point [{} {}]", self.x, self.y)
1013///     }
1014/// }
1015/// ```
1016///
1017/// `Debug` implementations using either `derive` or the debug builder API
1018/// on [`Formatter`] support pretty-printing using the alternate flag: `{:#?}`.
1019///
1020/// Pretty-printing with `#?`:
1021///
1022/// ```
1023/// #[derive(Debug)]
1024/// struct Point {
1025///     x: i32,
1026///     y: i32,
1027/// }
1028///
1029/// let origin = Point { x: 0, y: 0 };
1030///
1031/// let expected = "The origin is: Point {
1032///     x: 0,
1033///     y: 0,
1034/// }";
1035/// assert_eq!(format!("The origin is: {origin:#?}"), expected);
1036/// ```
1037#[stable(feature = "rust1", since = "1.0.0")]
1038#[rustc_on_unimplemented(
1039    on(
1040        crate_local,
1041        note = "add `#[derive(Debug)]` to `{Self}` or manually `impl {This} for {Self}`"
1042    ),
1043    on(
1044        from_desugaring = "FormatLiteral",
1045        label = "`{Self}` cannot be formatted using `{{:?}}` because it doesn't implement `{This}`"
1046    ),
1047    message = "`{Self}` doesn't implement `{This}`"
1048)]
1049#[doc(alias = "{:?}")]
1050#[rustc_diagnostic_item = "Debug"]
1051#[rustc_trivial_field_reads]
1052pub trait Debug: PointeeSized {
1053    #[doc = include_str!("fmt_trait_method_doc.md")]
1054    ///
1055    /// # Examples
1056    ///
1057    /// ```
1058    /// use std::fmt;
1059    ///
1060    /// struct Position {
1061    ///     longitude: f32,
1062    ///     latitude: f32,
1063    /// }
1064    ///
1065    /// impl fmt::Debug for Position {
1066    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1067    ///         f.debug_tuple("")
1068    ///          .field(&self.longitude)
1069    ///          .field(&self.latitude)
1070    ///          .finish()
1071    ///     }
1072    /// }
1073    ///
1074    /// let position = Position { longitude: 1.987, latitude: 2.983 };
1075    /// assert_eq!(format!("{position:?}"), "(1.987, 2.983)");
1076    ///
1077    /// assert_eq!(format!("{position:#?}"), "(
1078    ///     1.987,
1079    ///     2.983,
1080    /// )");
1081    /// ```
1082    #[stable(feature = "rust1", since = "1.0.0")]
1083    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1084}
1085
1086// Separate module to reexport the macro `Debug` from prelude without the trait `Debug`.
1087pub(crate) mod macros {
1088    /// Derive macro generating an impl of the trait `Debug`.
1089    #[rustc_builtin_macro]
1090    #[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
1091    #[allow_internal_unstable(core_intrinsics, fmt_helpers_for_derive)]
1092    pub macro Debug($item:item) {
1093        /* compiler built-in */
1094    }
1095}
1096#[stable(feature = "builtin_macro_prelude", since = "1.38.0")]
1097#[doc(inline)]
1098pub use macros::Debug;
1099
1100/// Format trait for an empty format, `{}`.
1101///
1102/// Implementing this trait for a type will automatically implement the
1103/// [`ToString`][tostring] trait for the type, allowing the usage
1104/// of the [`.to_string()`][tostring_function] method. Prefer implementing
1105/// the `Display` trait for a type, rather than [`ToString`][tostring].
1106///
1107/// `Display` is similar to [`Debug`], but `Display` is for user-facing
1108/// output, and so cannot be derived.
1109///
1110/// For more information on formatters, see [the module-level documentation][module].
1111///
1112/// [module]: ../../std/fmt/index.html
1113/// [tostring]: ../../std/string/trait.ToString.html
1114/// [tostring_function]: ../../std/string/trait.ToString.html#tymethod.to_string
1115///
1116/// # Completeness and parseability
1117///
1118/// `Display` for a type might not necessarily be a lossless or complete representation of the type.
1119/// It may omit internal state, precision, or other information the type does not consider important
1120/// for user-facing output, as determined by the type. As such, the output of `Display` might not be
1121/// possible to parse, and even if it is, the result of parsing might not exactly match the original
1122/// value.
1123///
1124/// However, if a type has a lossless `Display` implementation whose output is meant to be
1125/// conveniently machine-parseable and not just meant for human consumption, then the type may wish
1126/// to accept the same format in `FromStr`, and document that usage. Having both `Display` and
1127/// `FromStr` implementations where the result of `Display` cannot be parsed with `FromStr` may
1128/// surprise users.
1129///
1130/// # Internationalization
1131///
1132/// Because a type can only have one `Display` implementation, it is often preferable
1133/// to only implement `Display` when there is a single most "obvious" way that
1134/// values can be formatted as text. This could mean formatting according to the
1135/// "invariant" culture and "undefined" locale, or it could mean that the type
1136/// display is designed for a specific culture/locale, such as developer logs.
1137///
1138/// If not all values have a justifiably canonical textual format or if you want
1139/// to support alternative formats not covered by the standard set of possible
1140/// [formatting traits], the most flexible approach is display adapters: methods
1141/// like [`str::escape_default`] or [`Path::display`] which create a wrapper
1142/// implementing `Display` to output the specific display format.
1143///
1144/// [formatting traits]: ../../std/fmt/index.html#formatting-traits
1145/// [`Path::display`]: ../../std/path/struct.Path.html#method.display
1146///
1147/// # Examples
1148///
1149/// Implementing `Display` on a type:
1150///
1151/// ```
1152/// use std::fmt;
1153///
1154/// struct Point {
1155///     x: i32,
1156///     y: i32,
1157/// }
1158///
1159/// impl fmt::Display for Point {
1160///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1161///         write!(f, "({}, {})", self.x, self.y)
1162///     }
1163/// }
1164///
1165/// let origin = Point { x: 0, y: 0 };
1166///
1167/// assert_eq!(format!("The origin is: {origin}"), "The origin is: (0, 0)");
1168/// ```
1169#[rustc_on_unimplemented(
1170    on(
1171        any(Self = "std::path::Path", Self = "std::path::PathBuf"),
1172        label = "`{Self}` cannot be formatted with the default formatter; call `.display()` on it",
1173        note = "call `.display()` or `.to_string_lossy()` to safely print paths, \
1174                as they may contain non-Unicode data",
1175    ),
1176    on(
1177        from_desugaring = "FormatLiteral",
1178        note = "in format strings you may be able to use `{{:?}}` (or {{:#?}} for pretty-print) instead",
1179        label = "`{Self}` cannot be formatted with the default formatter",
1180    ),
1181    message = "`{Self}` doesn't implement `{This}`"
1182)]
1183#[doc(alias = "{}")]
1184#[rustc_diagnostic_item = "Display"]
1185#[stable(feature = "rust1", since = "1.0.0")]
1186pub trait Display: PointeeSized {
1187    #[doc = include_str!("fmt_trait_method_doc.md")]
1188    ///
1189    /// # Examples
1190    ///
1191    /// ```
1192    /// use std::fmt;
1193    ///
1194    /// struct Position {
1195    ///     longitude: f32,
1196    ///     latitude: f32,
1197    /// }
1198    ///
1199    /// impl fmt::Display for Position {
1200    ///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1201    ///         write!(f, "({}, {})", self.longitude, self.latitude)
1202    ///     }
1203    /// }
1204    ///
1205    /// assert_eq!(
1206    ///     "(1.987, 2.983)",
1207    ///     format!("{}", Position { longitude: 1.987, latitude: 2.983, }),
1208    /// );
1209    /// ```
1210    #[stable(feature = "rust1", since = "1.0.0")]
1211    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1212}
1213
1214/// `o` formatting.
1215///
1216/// The `Octal` trait should format its output as a number in base-8.
1217///
1218/// For primitive signed integers (`i8` to `i128`, and `isize`),
1219/// negative values are formatted as the two’s complement representation.
1220///
1221/// The alternate flag, `#`, adds a `0o` in front of the output.
1222///
1223/// For more information on formatters, see [the module-level documentation][module].
1224///
1225/// [module]: ../../std/fmt/index.html
1226///
1227/// # Examples
1228///
1229/// Basic usage with `i32`:
1230///
1231/// ```
1232/// let x = 42; // 42 is '52' in octal
1233///
1234/// assert_eq!(format!("{x:o}"), "52");
1235/// assert_eq!(format!("{x:#o}"), "0o52");
1236///
1237/// assert_eq!(format!("{:o}", -16), "37777777760");
1238/// ```
1239///
1240/// Implementing `Octal` on a type:
1241///
1242/// ```
1243/// use std::fmt;
1244///
1245/// struct Length(i32);
1246///
1247/// impl fmt::Octal for Length {
1248///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1249///         let val = self.0;
1250///
1251///         fmt::Octal::fmt(&val, f) // delegate to i32's implementation
1252///     }
1253/// }
1254///
1255/// let l = Length(9);
1256///
1257/// assert_eq!(format!("l as octal is: {l:o}"), "l as octal is: 11");
1258///
1259/// assert_eq!(format!("l as octal is: {l:#06o}"), "l as octal is: 0o0011");
1260/// ```
1261#[stable(feature = "rust1", since = "1.0.0")]
1262pub trait Octal: PointeeSized {
1263    #[doc = include_str!("fmt_trait_method_doc.md")]
1264    #[stable(feature = "rust1", since = "1.0.0")]
1265    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1266}
1267
1268/// `b` formatting.
1269///
1270/// The `Binary` trait should format its output as a number in binary.
1271///
1272/// For primitive signed integers ([`i8`] to [`i128`], and [`isize`]),
1273/// negative values are formatted as the two’s complement representation.
1274///
1275/// The alternate flag, `#`, adds a `0b` in front of the output.
1276///
1277/// For more information on formatters, see [the module-level documentation][module].
1278///
1279/// [module]: ../../std/fmt/index.html
1280///
1281/// # Examples
1282///
1283/// Basic usage with [`i32`]:
1284///
1285/// ```
1286/// let x = 42; // 42 is '101010' in binary
1287///
1288/// assert_eq!(format!("{x:b}"), "101010");
1289/// assert_eq!(format!("{x:#b}"), "0b101010");
1290///
1291/// assert_eq!(format!("{:b}", -16), "11111111111111111111111111110000");
1292/// ```
1293///
1294/// Implementing `Binary` on a type:
1295///
1296/// ```
1297/// use std::fmt;
1298///
1299/// struct Length(i32);
1300///
1301/// impl fmt::Binary for Length {
1302///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1303///         let val = self.0;
1304///
1305///         fmt::Binary::fmt(&val, f) // delegate to i32's implementation
1306///     }
1307/// }
1308///
1309/// let l = Length(107);
1310///
1311/// assert_eq!(format!("l as binary is: {l:b}"), "l as binary is: 1101011");
1312///
1313/// assert_eq!(
1314///     // Note that the `0b` prefix added by `#` is included in the total width, so we
1315///     // need to add two to correctly display all 32 bits.
1316///     format!("l as binary is: {l:#034b}"),
1317///     "l as binary is: 0b00000000000000000000000001101011"
1318/// );
1319/// ```
1320#[stable(feature = "rust1", since = "1.0.0")]
1321pub trait Binary: PointeeSized {
1322    #[doc = include_str!("fmt_trait_method_doc.md")]
1323    #[stable(feature = "rust1", since = "1.0.0")]
1324    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1325}
1326
1327/// `x` formatting.
1328///
1329/// The `LowerHex` trait should format its output as a number in hexadecimal, with `a` through `f`
1330/// in lower case.
1331///
1332/// For primitive signed integers (`i8` to `i128`, and `isize`),
1333/// negative values are formatted as the two’s complement representation.
1334///
1335/// The alternate flag, `#`, adds a `0x` in front of the output.
1336///
1337/// For more information on formatters, see [the module-level documentation][module].
1338///
1339/// [module]: ../../std/fmt/index.html
1340///
1341/// # Examples
1342///
1343/// Basic usage with `i32`:
1344///
1345/// ```
1346/// let y = 42; // 42 is '2a' in hex
1347///
1348/// assert_eq!(format!("{y:x}"), "2a");
1349/// assert_eq!(format!("{y:#x}"), "0x2a");
1350///
1351/// assert_eq!(format!("{:x}", -16), "fffffff0");
1352/// ```
1353///
1354/// Implementing `LowerHex` on a type:
1355///
1356/// ```
1357/// use std::fmt;
1358///
1359/// struct Length(i32);
1360///
1361/// impl fmt::LowerHex for Length {
1362///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1363///         let val = self.0;
1364///
1365///         fmt::LowerHex::fmt(&val, f) // delegate to i32's implementation
1366///     }
1367/// }
1368///
1369/// let l = Length(9);
1370///
1371/// assert_eq!(format!("l as hex is: {l:x}"), "l as hex is: 9");
1372///
1373/// assert_eq!(format!("l as hex is: {l:#010x}"), "l as hex is: 0x00000009");
1374/// ```
1375#[stable(feature = "rust1", since = "1.0.0")]
1376pub trait LowerHex: PointeeSized {
1377    #[doc = include_str!("fmt_trait_method_doc.md")]
1378    #[stable(feature = "rust1", since = "1.0.0")]
1379    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1380}
1381
1382/// `X` formatting.
1383///
1384/// The `UpperHex` trait should format its output as a number in hexadecimal, with `A` through `F`
1385/// in upper case.
1386///
1387/// For primitive signed integers (`i8` to `i128`, and `isize`),
1388/// negative values are formatted as the two’s complement representation.
1389///
1390/// The alternate flag, `#`, adds a `0x` in front of the output.
1391///
1392/// For more information on formatters, see [the module-level documentation][module].
1393///
1394/// [module]: ../../std/fmt/index.html
1395///
1396/// # Examples
1397///
1398/// Basic usage with `i32`:
1399///
1400/// ```
1401/// let y = 42; // 42 is '2A' in hex
1402///
1403/// assert_eq!(format!("{y:X}"), "2A");
1404/// assert_eq!(format!("{y:#X}"), "0x2A");
1405///
1406/// assert_eq!(format!("{:X}", -16), "FFFFFFF0");
1407/// ```
1408///
1409/// Implementing `UpperHex` on a type:
1410///
1411/// ```
1412/// use std::fmt;
1413///
1414/// struct Length(i32);
1415///
1416/// impl fmt::UpperHex for Length {
1417///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1418///         let val = self.0;
1419///
1420///         fmt::UpperHex::fmt(&val, f) // delegate to i32's implementation
1421///     }
1422/// }
1423///
1424/// let l = Length(i32::MAX);
1425///
1426/// assert_eq!(format!("l as hex is: {l:X}"), "l as hex is: 7FFFFFFF");
1427///
1428/// assert_eq!(format!("l as hex is: {l:#010X}"), "l as hex is: 0x7FFFFFFF");
1429/// ```
1430#[stable(feature = "rust1", since = "1.0.0")]
1431pub trait UpperHex: PointeeSized {
1432    #[doc = include_str!("fmt_trait_method_doc.md")]
1433    #[stable(feature = "rust1", since = "1.0.0")]
1434    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1435}
1436
1437/// `p` formatting.
1438///
1439/// The `Pointer` trait should format its output as a memory location. This is commonly presented
1440/// as hexadecimal. For more information on formatters, see [the module-level documentation][module].
1441///
1442/// Printing of pointers is not a reliable way to discover how Rust programs are implemented.
1443/// The act of reading an address changes the program itself, and may change how the data is represented
1444/// in memory, and may affect which optimizations are applied to the code.
1445///
1446/// The printed pointer values are not guaranteed to be stable nor unique identifiers of objects.
1447/// Rust allows moving values to different memory locations, and may reuse the same memory locations
1448/// for different purposes.
1449///
1450/// There is no guarantee that the printed value can be converted back to a pointer.
1451///
1452/// [module]: ../../std/fmt/index.html
1453///
1454/// # Examples
1455///
1456/// Basic usage with `&i32`:
1457///
1458/// ```
1459/// let x = &42;
1460///
1461/// let address = format!("{x:p}"); // this produces something like '0x7f06092ac6d0'
1462/// ```
1463///
1464/// Implementing `Pointer` on a type:
1465///
1466/// ```
1467/// use std::fmt;
1468///
1469/// struct Length(i32);
1470///
1471/// impl fmt::Pointer for Length {
1472///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1473///         // use `as` to convert to a `*const T`, which implements Pointer, which we can use
1474///
1475///         let ptr = self as *const Self;
1476///         fmt::Pointer::fmt(&ptr, f)
1477///     }
1478/// }
1479///
1480/// let l = Length(42);
1481///
1482/// println!("l is in memory here: {l:p}");
1483///
1484/// let l_ptr = format!("{l:018p}");
1485/// assert_eq!(l_ptr.len(), 18);
1486/// assert_eq!(&l_ptr[..2], "0x");
1487/// ```
1488#[stable(feature = "rust1", since = "1.0.0")]
1489#[rustc_diagnostic_item = "Pointer"]
1490pub trait Pointer: PointeeSized {
1491    #[doc = include_str!("fmt_trait_method_doc.md")]
1492    #[stable(feature = "rust1", since = "1.0.0")]
1493    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1494}
1495
1496/// `e` formatting.
1497///
1498/// The `LowerExp` trait should format its output in scientific notation with a lower-case `e`.
1499///
1500/// For more information on formatters, see [the module-level documentation][module].
1501///
1502/// [module]: ../../std/fmt/index.html
1503///
1504/// # Examples
1505///
1506/// Basic usage with `f64`:
1507///
1508/// ```
1509/// let x = 42.0; // 42.0 is '4.2e1' in scientific notation
1510///
1511/// assert_eq!(format!("{x:e}"), "4.2e1");
1512/// ```
1513///
1514/// Implementing `LowerExp` on a type:
1515///
1516/// ```
1517/// use std::fmt;
1518///
1519/// struct Length(i32);
1520///
1521/// impl fmt::LowerExp for Length {
1522///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1523///         let val = f64::from(self.0);
1524///         fmt::LowerExp::fmt(&val, f) // delegate to f64's implementation
1525///     }
1526/// }
1527///
1528/// let l = Length(100);
1529///
1530/// assert_eq!(
1531///     format!("l in scientific notation is: {l:e}"),
1532///     "l in scientific notation is: 1e2"
1533/// );
1534///
1535/// assert_eq!(
1536///     format!("l in scientific notation is: {l:05e}"),
1537///     "l in scientific notation is: 001e2"
1538/// );
1539/// ```
1540#[stable(feature = "rust1", since = "1.0.0")]
1541pub trait LowerExp: PointeeSized {
1542    #[doc = include_str!("fmt_trait_method_doc.md")]
1543    #[stable(feature = "rust1", since = "1.0.0")]
1544    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1545}
1546
1547/// `E` formatting.
1548///
1549/// The `UpperExp` trait should format its output in scientific notation with an upper-case `E`.
1550///
1551/// For more information on formatters, see [the module-level documentation][module].
1552///
1553/// [module]: ../../std/fmt/index.html
1554///
1555/// # Examples
1556///
1557/// Basic usage with `f64`:
1558///
1559/// ```
1560/// let x = 42.0; // 42.0 is '4.2E1' in scientific notation
1561///
1562/// assert_eq!(format!("{x:E}"), "4.2E1");
1563/// ```
1564///
1565/// Implementing `UpperExp` on a type:
1566///
1567/// ```
1568/// use std::fmt;
1569///
1570/// struct Length(i32);
1571///
1572/// impl fmt::UpperExp for Length {
1573///     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1574///         let val = f64::from(self.0);
1575///         fmt::UpperExp::fmt(&val, f) // delegate to f64's implementation
1576///     }
1577/// }
1578///
1579/// let l = Length(100);
1580///
1581/// assert_eq!(
1582///     format!("l in scientific notation is: {l:E}"),
1583///     "l in scientific notation is: 1E2"
1584/// );
1585///
1586/// assert_eq!(
1587///     format!("l in scientific notation is: {l:05E}"),
1588///     "l in scientific notation is: 001E2"
1589/// );
1590/// ```
1591#[stable(feature = "rust1", since = "1.0.0")]
1592pub trait UpperExp: PointeeSized {
1593    #[doc = include_str!("fmt_trait_method_doc.md")]
1594    #[stable(feature = "rust1", since = "1.0.0")]
1595    fn fmt(&self, f: &mut Formatter<'_>) -> Result;
1596}
1597
1598/// Takes an output stream and an `Arguments` struct that can be precompiled with
1599/// the `format_args!` macro.
1600///
1601/// The arguments will be formatted according to the specified format string
1602/// into the output stream provided.
1603///
1604/// # Examples
1605///
1606/// Basic usage:
1607///
1608/// ```
1609/// use std::fmt;
1610///
1611/// let mut output = String::new();
1612/// fmt::write(&mut output, format_args!("Hello {}!", "world"))
1613///     .expect("Error occurred while trying to write in String");
1614/// assert_eq!(output, "Hello world!");
1615/// ```
1616///
1617/// Please note that using [`write!`] might be preferable. Example:
1618///
1619/// ```
1620/// use std::fmt::Write;
1621///
1622/// let mut output = String::new();
1623/// write!(&mut output, "Hello {}!", "world")
1624///     .expect("Error occurred while trying to write in String");
1625/// assert_eq!(output, "Hello world!");
1626/// ```
1627///
1628/// [`write!`]: crate::write!
1629#[stable(feature = "rust1", since = "1.0.0")]
1630pub fn write(output: &mut dyn Write, fmt: Arguments<'_>) -> Result {
1631    if let Some(s) = fmt.as_str() {
1632        return output.write_str(s);
1633    }
1634
1635    let mut template = fmt.template;
1636    let args = fmt.args;
1637
1638    let mut arg_index = 0;
1639
1640    // See comment on `fmt::Arguments` for the details of how the template is encoded.
1641
1642    // This must match the encoding from `expand_format_args` in
1643    // compiler/rustc_ast_lowering/src/format.rs.
1644    loop {
1645        // SAFETY: We can assume the template is valid.
1646        let n = unsafe {
1647            let n = template.read();
1648            template = template.add(1);
1649            n
1650        };
1651
1652        if n == 0 {
1653            // End of template.
1654            return Ok(());
1655        } else if n < 0x80 {
1656            // Literal string piece of length `n`.
1657
1658            // SAFETY: We can assume the strings in the template are valid.
1659            let s = unsafe {
1660                let s = crate::str::from_raw_parts(template.as_ptr(), n as usize);
1661                template = template.add(n as usize);
1662                s
1663            };
1664            output.write_str(s)?;
1665        } else if n == 0x80 {
1666            // Literal string piece with a 16-bit length.
1667
1668            // SAFETY: We can assume the strings in the template are valid.
1669            let s = unsafe {
1670                let len = usize::from(u16::from_le_bytes(template.cast_array().read()));
1671                template = template.add(2);
1672                let s = crate::str::from_raw_parts(template.as_ptr(), len);
1673                template = template.add(len);
1674                s
1675            };
1676            output.write_str(s)?;
1677        } else if n == 0xC0 {
1678            // Placeholder for next argument with default options.
1679            //
1680            // Having this as a separate case improves performance for the common case.
1681
1682            // SAFETY: We can assume the template only refers to arguments that exist.
1683            unsafe {
1684                args.add(arg_index)
1685                    .as_ref()
1686                    .fmt(&mut Formatter::new(output, FormattingOptions::new()))?;
1687            }
1688            arg_index += 1;
1689        } else {
1690            // SAFETY: We can assume the template is valid.
1691            unsafe { assert_unchecked(n > 0xC0) };
1692
1693            // Placeholder with custom options.
1694
1695            let mut opt = FormattingOptions::new();
1696
1697            // SAFETY: We can assume the template is valid.
1698            unsafe {
1699                if n & 1 != 0 {
1700                    opt.flags = u32::from_le_bytes(template.cast_array().read());
1701                    template = template.add(4);
1702                }
1703                if n & 2 != 0 {
1704                    opt.width = u16::from_le_bytes(template.cast_array().read());
1705                    template = template.add(2);
1706                }
1707                if n & 4 != 0 {
1708                    opt.precision = u16::from_le_bytes(template.cast_array().read());
1709                    template = template.add(2);
1710                }
1711                if n & 8 != 0 {
1712                    arg_index = usize::from(u16::from_le_bytes(template.cast_array().read()));
1713                    template = template.add(2);
1714                }
1715            }
1716            if n & 16 != 0 {
1717                // Dynamic width from a usize argument.
1718                // SAFETY: We can assume the template only refers to arguments that exist.
1719                unsafe {
1720                    opt.width = args.add(opt.width as usize).as_ref().as_u16().unwrap_unchecked();
1721                }
1722            }
1723            if n & 32 != 0 {
1724                // Dynamic precision from a usize argument.
1725                // SAFETY: We can assume the template only refers to arguments that exist.
1726                unsafe {
1727                    opt.precision =
1728                        args.add(opt.precision as usize).as_ref().as_u16().unwrap_unchecked();
1729                }
1730            }
1731
1732            // SAFETY: We can assume the template only refers to arguments that exist.
1733            unsafe {
1734                args.add(arg_index).as_ref().fmt(&mut Formatter::new(output, opt))?;
1735            }
1736            arg_index += 1;
1737        }
1738    }
1739}
1740
1741/// Padding after the end of something. Returned by `Formatter::padding`.
1742#[must_use = "don't forget to write the post padding"]
1743pub(crate) struct PostPadding {
1744    fill: char,
1745    padding: u16,
1746}
1747
1748impl PostPadding {
1749    fn new(fill: char, padding: u16) -> PostPadding {
1750        PostPadding { fill, padding }
1751    }
1752
1753    /// Writes this post padding.
1754    pub(crate) fn write(self, f: &mut Formatter<'_>) -> Result {
1755        for _ in 0..self.padding {
1756            f.buf.write_char(self.fill)?;
1757        }
1758        Ok(())
1759    }
1760}
1761
1762impl<'a> Formatter<'a> {
1763    fn wrap_buf<'b, 'c, F>(&'b mut self, wrap: F) -> Formatter<'c>
1764    where
1765        'b: 'c,
1766        F: FnOnce(&'b mut (dyn Write + 'b)) -> &'c mut (dyn Write + 'c),
1767    {
1768        Formatter {
1769            // We want to change this
1770            buf: wrap(self.buf),
1771
1772            // And preserve these
1773            options: self.options,
1774        }
1775    }
1776
1777    // Helper methods used for padding and processing formatting arguments that
1778    // all formatting traits can use.
1779
1780    /// Performs the correct padding for an integer which has already been
1781    /// emitted into a str. The str should *not* contain the sign for the
1782    /// integer, that will be added by this method.
1783    ///
1784    /// # Arguments
1785    ///
1786    /// * is_nonnegative - whether the original integer was either positive or zero.
1787    /// * prefix - if the '#' character (Alternate) is provided, this
1788    ///   is the prefix to put in front of the number.
1789    /// * buf - the byte array that the number has been formatted into
1790    ///
1791    /// This function will correctly account for the flags provided as well as
1792    /// the minimum width. It will not take precision into account.
1793    ///
1794    /// # Examples
1795    ///
1796    /// ```
1797    /// use std::fmt;
1798    ///
1799    /// struct Foo { nb: i32 }
1800    ///
1801    /// impl Foo {
1802    ///     fn new(nb: i32) -> Foo {
1803    ///         Foo {
1804    ///             nb,
1805    ///         }
1806    ///     }
1807    /// }
1808    ///
1809    /// impl fmt::Display for Foo {
1810    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
1811    ///         // We need to remove "-" from the number output.
1812    ///         let tmp = self.nb.abs().to_string();
1813    ///
1814    ///         formatter.pad_integral(self.nb >= 0, "Foo ", &tmp)
1815    ///     }
1816    /// }
1817    ///
1818    /// assert_eq!(format!("{}", Foo::new(2)), "2");
1819    /// assert_eq!(format!("{}", Foo::new(-1)), "-1");
1820    /// assert_eq!(format!("{}", Foo::new(0)), "0");
1821    /// assert_eq!(format!("{:#}", Foo::new(-1)), "-Foo 1");
1822    /// assert_eq!(format!("{:0>#8}", Foo::new(-1)), "00-Foo 1");
1823    /// ```
1824    #[stable(feature = "rust1", since = "1.0.0")]
1825    pub fn pad_integral(&mut self, is_nonnegative: bool, prefix: &str, buf: &str) -> Result {
1826        let mut width = buf.len();
1827
1828        let mut sign = None;
1829        if !is_nonnegative {
1830            sign = Some('-');
1831            width += 1;
1832        } else if self.sign_plus() {
1833            sign = Some('+');
1834            width += 1;
1835        }
1836
1837        let prefix = if self.alternate() {
1838            width += prefix.chars().count();
1839            Some(prefix)
1840        } else {
1841            None
1842        };
1843
1844        // Writes the sign if it exists, and then the prefix if it was requested
1845        #[inline(never)]
1846        fn write_prefix(f: &mut Formatter<'_>, sign: Option<char>, prefix: Option<&str>) -> Result {
1847            if let Some(c) = sign {
1848                f.buf.write_char(c)?;
1849            }
1850            if let Some(prefix) = prefix { f.buf.write_str(prefix) } else { Ok(()) }
1851        }
1852
1853        // The `width` field is more of a `min-width` parameter at this point.
1854        let min = self.options.width;
1855        if width >= usize::from(min) {
1856            // We're over the minimum width, so then we can just write the bytes.
1857            write_prefix(self, sign, prefix)?;
1858            self.buf.write_str(buf)
1859        } else if self.sign_aware_zero_pad() {
1860            // The sign and prefix goes before the padding if the fill character
1861            // is zero
1862            let old_options = self.options;
1863            self.options.fill('0').align(Some(Alignment::Right));
1864            write_prefix(self, sign, prefix)?;
1865            let post_padding = self.padding(min - width as u16, Alignment::Right)?;
1866            self.buf.write_str(buf)?;
1867            post_padding.write(self)?;
1868            self.options = old_options;
1869            Ok(())
1870        } else {
1871            // Otherwise, the sign and prefix goes after the padding
1872            let post_padding = self.padding(min - width as u16, Alignment::Right)?;
1873            write_prefix(self, sign, prefix)?;
1874            self.buf.write_str(buf)?;
1875            post_padding.write(self)
1876        }
1877    }
1878
1879    /// Takes a string slice and emits it to the internal buffer after applying
1880    /// the relevant formatting flags specified.
1881    ///
1882    /// The flags recognized for generic strings are:
1883    ///
1884    /// * width - the minimum width of what to emit
1885    /// * fill/align - what to emit and where to emit it if the string
1886    ///                provided needs to be padded
1887    /// * precision - the maximum length to emit, the string is truncated if it
1888    ///               is longer than this length
1889    ///
1890    /// Notably this function ignores the `flag` parameters.
1891    ///
1892    /// # Examples
1893    ///
1894    /// ```
1895    /// use std::fmt;
1896    ///
1897    /// struct Foo;
1898    ///
1899    /// impl fmt::Display for Foo {
1900    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
1901    ///         formatter.pad("Foo")
1902    ///     }
1903    /// }
1904    ///
1905    /// assert_eq!(format!("{Foo:<4}"), "Foo ");
1906    /// assert_eq!(format!("{Foo:0>4}"), "0Foo");
1907    /// ```
1908    #[stable(feature = "rust1", since = "1.0.0")]
1909    pub fn pad(&mut self, s: &str) -> Result {
1910        // Make sure there's a fast path up front.
1911        if self.options.flags & (flags::WIDTH_FLAG | flags::PRECISION_FLAG) == 0 {
1912            return self.buf.write_str(s);
1913        }
1914
1915        // The `precision` field can be interpreted as a maximum width for the
1916        // string being formatted.
1917        let (s, char_count) = if let Some(max_char_count) = self.options.get_precision() {
1918            let mut iter = s.char_indices();
1919            let remaining = match iter.advance_by(usize::from(max_char_count)) {
1920                Ok(()) => 0,
1921                Err(remaining) => remaining.get(),
1922            };
1923            // SAFETY: The offset of `.char_indices()` is guaranteed to be
1924            // in-bounds and between character boundaries.
1925            let truncated = unsafe { s.get_unchecked(..iter.offset()) };
1926            (truncated, usize::from(max_char_count) - remaining)
1927        } else {
1928            // Use the optimized char counting algorithm for the full string.
1929            (s, s.chars().count())
1930        };
1931
1932        // The `width` field is more of a minimum width parameter at this point.
1933        if char_count < usize::from(self.options.width) {
1934            // If we're under the minimum width, then fill up the minimum width
1935            // with the specified string + some alignment.
1936            let post_padding =
1937                self.padding(self.options.width - char_count as u16, Alignment::Left)?;
1938            self.buf.write_str(s)?;
1939            post_padding.write(self)
1940        } else {
1941            // If we're over the minimum width or there is no minimum width, we
1942            // can just emit the string.
1943            self.buf.write_str(s)
1944        }
1945    }
1946
1947    /// Writes the pre-padding and returns the unwritten post-padding.
1948    ///
1949    /// Callers are responsible for ensuring post-padding is written after the
1950    /// thing that is being padded.
1951    pub(crate) fn padding(
1952        &mut self,
1953        padding: u16,
1954        default: Alignment,
1955    ) -> result::Result<PostPadding, Error> {
1956        let align = self.options.get_align().unwrap_or(default);
1957        let fill = self.options.get_fill();
1958
1959        let padding_left = match align {
1960            Alignment::Left => 0,
1961            Alignment::Right => padding,
1962            Alignment::Center => padding / 2,
1963        };
1964
1965        for _ in 0..padding_left {
1966            self.buf.write_char(fill)?;
1967        }
1968
1969        Ok(PostPadding::new(fill, padding - padding_left))
1970    }
1971
1972    /// Takes the formatted parts and applies the padding.
1973    ///
1974    /// Assumes that the caller already has rendered the parts with required precision,
1975    /// so that `self.precision` can be ignored.
1976    ///
1977    /// # Safety
1978    ///
1979    /// Any `numfmt::Part::Copy` parts in `formatted` must contain valid UTF-8.
1980    unsafe fn pad_formatted_parts(&mut self, formatted: &numfmt::Formatted<'_>) -> Result {
1981        if self.options.width == 0 {
1982            // this is the common case and we take a shortcut
1983            // SAFETY: Per the precondition.
1984            unsafe { self.write_formatted_parts(formatted) }
1985        } else {
1986            // for the sign-aware zero padding, we render the sign first and
1987            // behave as if we had no sign from the beginning.
1988            let mut formatted = formatted.clone();
1989            let mut width = self.options.width;
1990            let old_options = self.options;
1991            if self.sign_aware_zero_pad() {
1992                // a sign always goes first
1993                let sign = formatted.sign;
1994                self.buf.write_str(sign)?;
1995
1996                // remove the sign from the formatted parts
1997                formatted.sign = "";
1998                width = width.saturating_sub(sign.len() as u16);
1999                self.options.fill('0').align(Some(Alignment::Right));
2000            }
2001
2002            // remaining parts go through the ordinary padding process.
2003            let len = formatted.len();
2004            let ret = if usize::from(width) <= len {
2005                // no padding
2006                // SAFETY: Per the precondition.
2007                unsafe { self.write_formatted_parts(&formatted) }
2008            } else {
2009                let post_padding = self.padding(width - len as u16, Alignment::Right)?;
2010                // SAFETY: Per the precondition.
2011                unsafe {
2012                    self.write_formatted_parts(&formatted)?;
2013                }
2014                post_padding.write(self)
2015            };
2016            self.options = old_options;
2017            ret
2018        }
2019    }
2020
2021    /// # Safety
2022    ///
2023    /// Any `numfmt::Part::Copy` parts in `formatted` must contain valid UTF-8.
2024    unsafe fn write_formatted_parts(&mut self, formatted: &numfmt::Formatted<'_>) -> Result {
2025        unsafe fn write_bytes(buf: &mut dyn Write, s: &[u8]) -> Result {
2026            // SAFETY: This is used for `numfmt::Part::Num` and `numfmt::Part::Copy`.
2027            // It's safe to use for `numfmt::Part::Num` since every char `c` is between
2028            // `b'0'` and `b'9'`, which means `s` is valid UTF-8. It's safe to use for
2029            // `numfmt::Part::Copy` due to this function's precondition.
2030            buf.write_str(unsafe { str::from_utf8_unchecked(s) })
2031        }
2032
2033        if !formatted.sign.is_empty() {
2034            self.buf.write_str(formatted.sign)?;
2035        }
2036        for part in formatted.parts {
2037            match *part {
2038                numfmt::Part::Zero(mut nzeroes) => {
2039                    const ZEROES: &str = // 64 zeroes
2040                        "0000000000000000000000000000000000000000000000000000000000000000";
2041                    while nzeroes > ZEROES.len() {
2042                        self.buf.write_str(ZEROES)?;
2043                        nzeroes -= ZEROES.len();
2044                    }
2045                    if nzeroes > 0 {
2046                        self.buf.write_str(&ZEROES[..nzeroes])?;
2047                    }
2048                }
2049                numfmt::Part::Num(mut v) => {
2050                    let mut s = [0; 5];
2051                    let len = part.len();
2052                    for c in s[..len].iter_mut().rev() {
2053                        *c = b'0' + (v % 10) as u8;
2054                        v /= 10;
2055                    }
2056                    // SAFETY: Per the precondition.
2057                    unsafe {
2058                        write_bytes(self.buf, &s[..len])?;
2059                    }
2060                }
2061                // SAFETY: Per the precondition.
2062                numfmt::Part::Copy(buf) => unsafe {
2063                    write_bytes(self.buf, buf)?;
2064                },
2065            }
2066        }
2067        Ok(())
2068    }
2069
2070    /// Writes some data to the underlying buffer contained within this
2071    /// formatter.
2072    ///
2073    /// # Examples
2074    ///
2075    /// ```
2076    /// use std::fmt;
2077    ///
2078    /// struct Foo;
2079    ///
2080    /// impl fmt::Display for Foo {
2081    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2082    ///         formatter.write_str("Foo")
2083    ///         // This is equivalent to:
2084    ///         // write!(formatter, "Foo")
2085    ///     }
2086    /// }
2087    ///
2088    /// assert_eq!(format!("{Foo}"), "Foo");
2089    /// assert_eq!(format!("{Foo:0>8}"), "Foo");
2090    /// ```
2091    #[stable(feature = "rust1", since = "1.0.0")]
2092    pub fn write_str(&mut self, data: &str) -> Result {
2093        self.buf.write_str(data)
2094    }
2095
2096    /// Glue for usage of the [`write!`] macro with implementors of this trait.
2097    ///
2098    /// This method should generally not be invoked manually, but rather through
2099    /// the [`write!`] macro itself.
2100    ///
2101    /// Writes some formatted information into this instance.
2102    ///
2103    /// # Examples
2104    ///
2105    /// ```
2106    /// use std::fmt;
2107    ///
2108    /// struct Foo(i32);
2109    ///
2110    /// impl fmt::Display for Foo {
2111    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2112    ///         formatter.write_fmt(format_args!("Foo {}", self.0))
2113    ///     }
2114    /// }
2115    ///
2116    /// assert_eq!(format!("{}", Foo(-1)), "Foo -1");
2117    /// assert_eq!(format!("{:0>8}", Foo(2)), "Foo 2");
2118    /// ```
2119    #[stable(feature = "rust1", since = "1.0.0")]
2120    #[inline]
2121    pub fn write_fmt(&mut self, fmt: Arguments<'_>) -> Result {
2122        if let Some(s) = fmt.as_statically_known_str() {
2123            self.buf.write_str(s)
2124        } else {
2125            write(self.buf, fmt)
2126        }
2127    }
2128
2129    /// Returns flags for formatting.
2130    #[must_use]
2131    #[stable(feature = "rust1", since = "1.0.0")]
2132    #[deprecated(
2133        since = "1.24.0",
2134        note = "use the `sign_plus`, `sign_minus`, `alternate`, \
2135                or `sign_aware_zero_pad` methods instead"
2136    )]
2137    pub fn flags(&self) -> u32 {
2138        // Extract the debug upper/lower hex, zero pad, alternate, and plus/minus flags
2139        // to stay compatible with older versions of Rust.
2140        self.options.flags >> 21 & 0x3F
2141    }
2142
2143    /// Returns the character used as 'fill' whenever there is alignment.
2144    ///
2145    /// # Examples
2146    ///
2147    /// ```
2148    /// use std::fmt;
2149    ///
2150    /// struct Foo;
2151    ///
2152    /// impl fmt::Display for Foo {
2153    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2154    ///         let c = formatter.fill();
2155    ///         if let Some(width) = formatter.width() {
2156    ///             for _ in 0..width {
2157    ///                 write!(formatter, "{c}")?;
2158    ///             }
2159    ///             Ok(())
2160    ///         } else {
2161    ///             write!(formatter, "{c}")
2162    ///         }
2163    ///     }
2164    /// }
2165    ///
2166    /// // We set alignment to the right with ">".
2167    /// assert_eq!(format!("{Foo:G>3}"), "GGG");
2168    /// assert_eq!(format!("{Foo:t>6}"), "tttttt");
2169    /// ```
2170    #[must_use]
2171    #[stable(feature = "fmt_flags", since = "1.5.0")]
2172    pub fn fill(&self) -> char {
2173        self.options.get_fill()
2174    }
2175
2176    /// Returns a flag indicating what form of alignment was requested.
2177    ///
2178    /// # Examples
2179    ///
2180    /// ```
2181    /// use std::fmt::{self, Alignment};
2182    ///
2183    /// struct Foo;
2184    ///
2185    /// impl fmt::Display for Foo {
2186    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2187    ///         let s = if let Some(s) = formatter.align() {
2188    ///             match s {
2189    ///                 Alignment::Left    => "left",
2190    ///                 Alignment::Right   => "right",
2191    ///                 Alignment::Center  => "center",
2192    ///             }
2193    ///         } else {
2194    ///             "into the void"
2195    ///         };
2196    ///         write!(formatter, "{s}")
2197    ///     }
2198    /// }
2199    ///
2200    /// assert_eq!(format!("{Foo:<}"), "left");
2201    /// assert_eq!(format!("{Foo:>}"), "right");
2202    /// assert_eq!(format!("{Foo:^}"), "center");
2203    /// assert_eq!(format!("{Foo}"), "into the void");
2204    /// ```
2205    #[must_use]
2206    #[stable(feature = "fmt_flags_align", since = "1.28.0")]
2207    pub fn align(&self) -> Option<Alignment> {
2208        self.options.get_align()
2209    }
2210
2211    /// Returns the optionally specified integer width that the output should be.
2212    ///
2213    /// # Examples
2214    ///
2215    /// ```
2216    /// use std::fmt;
2217    ///
2218    /// struct Foo(i32);
2219    ///
2220    /// impl fmt::Display for Foo {
2221    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2222    ///         if let Some(width) = formatter.width() {
2223    ///             // If we received a width, we use it
2224    ///             write!(formatter, "{:width$}", format!("Foo({})", self.0), width = width)
2225    ///         } else {
2226    ///             // Otherwise we do nothing special
2227    ///             write!(formatter, "Foo({})", self.0)
2228    ///         }
2229    ///     }
2230    /// }
2231    ///
2232    /// assert_eq!(format!("{:10}", Foo(23)), "Foo(23)   ");
2233    /// assert_eq!(format!("{}", Foo(23)), "Foo(23)");
2234    /// ```
2235    #[must_use]
2236    #[stable(feature = "fmt_flags", since = "1.5.0")]
2237    pub fn width(&self) -> Option<usize> {
2238        if self.options.flags & flags::WIDTH_FLAG == 0 {
2239            None
2240        } else {
2241            Some(self.options.width as usize)
2242        }
2243    }
2244
2245    /// Returns the optionally specified precision for numeric types.
2246    /// Alternatively, the maximum width for string types.
2247    ///
2248    /// # Examples
2249    ///
2250    /// ```
2251    /// use std::fmt;
2252    ///
2253    /// struct Foo(f32);
2254    ///
2255    /// impl fmt::Display for Foo {
2256    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2257    ///         if let Some(precision) = formatter.precision() {
2258    ///             // If we received a precision, we use it.
2259    ///             write!(formatter, "Foo({1:.*})", precision, self.0)
2260    ///         } else {
2261    ///             // Otherwise we default to 2.
2262    ///             write!(formatter, "Foo({:.2})", self.0)
2263    ///         }
2264    ///     }
2265    /// }
2266    ///
2267    /// assert_eq!(format!("{:.4}", Foo(23.2)), "Foo(23.2000)");
2268    /// assert_eq!(format!("{}", Foo(23.2)), "Foo(23.20)");
2269    /// ```
2270    #[must_use]
2271    #[stable(feature = "fmt_flags", since = "1.5.0")]
2272    pub fn precision(&self) -> Option<usize> {
2273        if self.options.flags & flags::PRECISION_FLAG == 0 {
2274            None
2275        } else {
2276            Some(self.options.precision as usize)
2277        }
2278    }
2279
2280    /// Determines if the `+` flag was specified.
2281    ///
2282    /// # Examples
2283    ///
2284    /// ```
2285    /// use std::fmt;
2286    ///
2287    /// struct Foo(i32);
2288    ///
2289    /// impl fmt::Display for Foo {
2290    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2291    ///         if formatter.sign_plus() {
2292    ///             write!(formatter,
2293    ///                    "Foo({}{})",
2294    ///                    if self.0 < 0 { '-' } else { '+' },
2295    ///                    self.0.abs())
2296    ///         } else {
2297    ///             write!(formatter, "Foo({})", self.0)
2298    ///         }
2299    ///     }
2300    /// }
2301    ///
2302    /// assert_eq!(format!("{:+}", Foo(23)), "Foo(+23)");
2303    /// assert_eq!(format!("{:+}", Foo(-23)), "Foo(-23)");
2304    /// assert_eq!(format!("{}", Foo(23)), "Foo(23)");
2305    /// ```
2306    #[must_use]
2307    #[stable(feature = "fmt_flags", since = "1.5.0")]
2308    pub fn sign_plus(&self) -> bool {
2309        self.options.flags & flags::SIGN_PLUS_FLAG != 0
2310    }
2311
2312    /// Determines if the `-` flag was specified.
2313    ///
2314    /// # Examples
2315    ///
2316    /// ```
2317    /// use std::fmt;
2318    ///
2319    /// struct Foo(i32);
2320    ///
2321    /// impl fmt::Display for Foo {
2322    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2323    ///         if formatter.sign_minus() {
2324    ///             // You want a minus sign? Have one!
2325    ///             write!(formatter, "-Foo({})", self.0)
2326    ///         } else {
2327    ///             write!(formatter, "Foo({})", self.0)
2328    ///         }
2329    ///     }
2330    /// }
2331    ///
2332    /// assert_eq!(format!("{:-}", Foo(23)), "-Foo(23)");
2333    /// assert_eq!(format!("{}", Foo(23)), "Foo(23)");
2334    /// ```
2335    #[must_use]
2336    #[stable(feature = "fmt_flags", since = "1.5.0")]
2337    pub fn sign_minus(&self) -> bool {
2338        self.options.flags & flags::SIGN_MINUS_FLAG != 0
2339    }
2340
2341    /// Determines if the `#` flag was specified.
2342    ///
2343    /// # Examples
2344    ///
2345    /// ```
2346    /// use std::fmt;
2347    ///
2348    /// struct Foo(i32);
2349    ///
2350    /// impl fmt::Display for Foo {
2351    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2352    ///         if formatter.alternate() {
2353    ///             write!(formatter, "Foo({})", self.0)
2354    ///         } else {
2355    ///             write!(formatter, "{}", self.0)
2356    ///         }
2357    ///     }
2358    /// }
2359    ///
2360    /// assert_eq!(format!("{:#}", Foo(23)), "Foo(23)");
2361    /// assert_eq!(format!("{}", Foo(23)), "23");
2362    /// ```
2363    #[must_use]
2364    #[stable(feature = "fmt_flags", since = "1.5.0")]
2365    pub fn alternate(&self) -> bool {
2366        self.options.flags & flags::ALTERNATE_FLAG != 0
2367    }
2368
2369    /// Determines if the `0` flag was specified.
2370    ///
2371    /// # Examples
2372    ///
2373    /// ```
2374    /// use std::fmt;
2375    ///
2376    /// struct Foo(i32);
2377    ///
2378    /// impl fmt::Display for Foo {
2379    ///     fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
2380    ///         assert!(formatter.sign_aware_zero_pad());
2381    ///         assert_eq!(formatter.width(), Some(4));
2382    ///         // We ignore the formatter's options.
2383    ///         write!(formatter, "{}", self.0)
2384    ///     }
2385    /// }
2386    ///
2387    /// assert_eq!(format!("{:04}", Foo(23)), "23");
2388    /// ```
2389    #[must_use]
2390    #[stable(feature = "fmt_flags", since = "1.5.0")]
2391    pub fn sign_aware_zero_pad(&self) -> bool {
2392        self.options.flags & flags::SIGN_AWARE_ZERO_PAD_FLAG != 0
2393    }
2394
2395    // FIXME: Decide what public API we want for these two flags.
2396    // https://github.com/rust-lang/rust/issues/48584
2397    fn debug_lower_hex(&self) -> bool {
2398        self.options.flags & flags::DEBUG_LOWER_HEX_FLAG != 0
2399    }
2400    fn debug_upper_hex(&self) -> bool {
2401        self.options.flags & flags::DEBUG_UPPER_HEX_FLAG != 0
2402    }
2403
2404    /// Creates a [`DebugStruct`] builder designed to assist with creation of
2405    /// [`fmt::Debug`] implementations for structs.
2406    ///
2407    /// [`fmt::Debug`]: self::Debug
2408    ///
2409    /// # Examples
2410    ///
2411    /// ```rust
2412    /// use std::fmt;
2413    /// use std::net::Ipv4Addr;
2414    ///
2415    /// struct Foo {
2416    ///     bar: i32,
2417    ///     baz: String,
2418    ///     addr: Ipv4Addr,
2419    /// }
2420    ///
2421    /// impl fmt::Debug for Foo {
2422    ///     fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2423    ///         fmt.debug_struct("Foo")
2424    ///             .field("bar", &self.bar)
2425    ///             .field("baz", &self.baz)
2426    ///             .field("addr", &format_args!("{}", self.addr))
2427    ///             .finish()
2428    ///     }
2429    /// }
2430    ///
2431    /// assert_eq!(
2432    ///     "Foo { bar: 10, baz: \"Hello World\", addr: 127.0.0.1 }",
2433    ///     format!("{:?}", Foo {
2434    ///         bar: 10,
2435    ///         baz: "Hello World".to_string(),
2436    ///         addr: Ipv4Addr::new(127, 0, 0, 1),
2437    ///     })
2438    /// );
2439    /// ```
2440    #[stable(feature = "debug_builders", since = "1.2.0")]
2441    pub fn debug_struct<'b>(&'b mut self, name: &str) -> DebugStruct<'b, 'a> {
2442        builders::debug_struct_new(self, name)
2443    }
2444
2445    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2446    /// binaries. `debug_struct_fields_finish` is more general, but this is
2447    /// faster for 1 field.
2448    #[doc(hidden)]
2449    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2450    pub fn debug_struct_field1_finish<'b>(
2451        &'b mut self,
2452        name: &str,
2453        name1: &str,
2454        value1: &dyn Debug,
2455    ) -> Result {
2456        let mut builder = builders::debug_struct_new(self, name);
2457        builder.field(name1, value1);
2458        builder.finish()
2459    }
2460
2461    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2462    /// binaries. `debug_struct_fields_finish` is more general, but this is
2463    /// faster for 2 fields.
2464    #[doc(hidden)]
2465    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2466    pub fn debug_struct_field2_finish<'b>(
2467        &'b mut self,
2468        name: &str,
2469        name1: &str,
2470        value1: &dyn Debug,
2471        name2: &str,
2472        value2: &dyn Debug,
2473    ) -> Result {
2474        let mut builder = builders::debug_struct_new(self, name);
2475        builder.field(name1, value1);
2476        builder.field(name2, value2);
2477        builder.finish()
2478    }
2479
2480    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2481    /// binaries. `debug_struct_fields_finish` is more general, but this is
2482    /// faster for 3 fields.
2483    #[doc(hidden)]
2484    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2485    pub fn debug_struct_field3_finish<'b>(
2486        &'b mut self,
2487        name: &str,
2488        name1: &str,
2489        value1: &dyn Debug,
2490        name2: &str,
2491        value2: &dyn Debug,
2492        name3: &str,
2493        value3: &dyn Debug,
2494    ) -> Result {
2495        let mut builder = builders::debug_struct_new(self, name);
2496        builder.field(name1, value1);
2497        builder.field(name2, value2);
2498        builder.field(name3, value3);
2499        builder.finish()
2500    }
2501
2502    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2503    /// binaries. `debug_struct_fields_finish` is more general, but this is
2504    /// faster for 4 fields.
2505    #[doc(hidden)]
2506    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2507    pub fn debug_struct_field4_finish<'b>(
2508        &'b mut self,
2509        name: &str,
2510        name1: &str,
2511        value1: &dyn Debug,
2512        name2: &str,
2513        value2: &dyn Debug,
2514        name3: &str,
2515        value3: &dyn Debug,
2516        name4: &str,
2517        value4: &dyn Debug,
2518    ) -> Result {
2519        let mut builder = builders::debug_struct_new(self, name);
2520        builder.field(name1, value1);
2521        builder.field(name2, value2);
2522        builder.field(name3, value3);
2523        builder.field(name4, value4);
2524        builder.finish()
2525    }
2526
2527    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2528    /// binaries. `debug_struct_fields_finish` is more general, but this is
2529    /// faster for 5 fields.
2530    #[doc(hidden)]
2531    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2532    pub fn debug_struct_field5_finish<'b>(
2533        &'b mut self,
2534        name: &str,
2535        name1: &str,
2536        value1: &dyn Debug,
2537        name2: &str,
2538        value2: &dyn Debug,
2539        name3: &str,
2540        value3: &dyn Debug,
2541        name4: &str,
2542        value4: &dyn Debug,
2543        name5: &str,
2544        value5: &dyn Debug,
2545    ) -> Result {
2546        let mut builder = builders::debug_struct_new(self, name);
2547        builder.field(name1, value1);
2548        builder.field(name2, value2);
2549        builder.field(name3, value3);
2550        builder.field(name4, value4);
2551        builder.field(name5, value5);
2552        builder.finish()
2553    }
2554
2555    /// Shrinks `derive(Debug)` code, for faster compilation and smaller binaries.
2556    /// For the cases not covered by `debug_struct_field[12345]_finish`.
2557    #[doc(hidden)]
2558    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2559    pub fn debug_struct_fields_finish<'b>(
2560        &'b mut self,
2561        name: &str,
2562        names: &[&str],
2563        values: &[&dyn Debug],
2564    ) -> Result {
2565        assert_eq!(names.len(), values.len());
2566        let mut builder = builders::debug_struct_new(self, name);
2567        for (name, value) in iter::zip(names, values) {
2568            builder.field(name, value);
2569        }
2570        builder.finish()
2571    }
2572
2573    /// Creates a `DebugTuple` builder designed to assist with creation of
2574    /// `fmt::Debug` implementations for tuple structs.
2575    ///
2576    /// # Examples
2577    ///
2578    /// ```rust
2579    /// use std::fmt;
2580    /// use std::marker::PhantomData;
2581    ///
2582    /// struct Foo<T>(i32, String, PhantomData<T>);
2583    ///
2584    /// impl<T> fmt::Debug for Foo<T> {
2585    ///     fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2586    ///         fmt.debug_tuple("Foo")
2587    ///             .field(&self.0)
2588    ///             .field(&self.1)
2589    ///             .field(&format_args!("_"))
2590    ///             .finish()
2591    ///     }
2592    /// }
2593    ///
2594    /// assert_eq!(
2595    ///     "Foo(10, \"Hello\", _)",
2596    ///     format!("{:?}", Foo(10, "Hello".to_string(), PhantomData::<u8>))
2597    /// );
2598    /// ```
2599    #[stable(feature = "debug_builders", since = "1.2.0")]
2600    pub fn debug_tuple<'b>(&'b mut self, name: &str) -> DebugTuple<'b, 'a> {
2601        builders::debug_tuple_new(self, name)
2602    }
2603
2604    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2605    /// binaries. `debug_tuple_fields_finish` is more general, but this is faster
2606    /// for 1 field.
2607    #[doc(hidden)]
2608    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2609    pub fn debug_tuple_field1_finish<'b>(&'b mut self, name: &str, value1: &dyn Debug) -> Result {
2610        let mut builder = builders::debug_tuple_new(self, name);
2611        builder.field(value1);
2612        builder.finish()
2613    }
2614
2615    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2616    /// binaries. `debug_tuple_fields_finish` is more general, but this is faster
2617    /// for 2 fields.
2618    #[doc(hidden)]
2619    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2620    pub fn debug_tuple_field2_finish<'b>(
2621        &'b mut self,
2622        name: &str,
2623        value1: &dyn Debug,
2624        value2: &dyn Debug,
2625    ) -> Result {
2626        let mut builder = builders::debug_tuple_new(self, name);
2627        builder.field(value1);
2628        builder.field(value2);
2629        builder.finish()
2630    }
2631
2632    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2633    /// binaries. `debug_tuple_fields_finish` is more general, but this is faster
2634    /// for 3 fields.
2635    #[doc(hidden)]
2636    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2637    pub fn debug_tuple_field3_finish<'b>(
2638        &'b mut self,
2639        name: &str,
2640        value1: &dyn Debug,
2641        value2: &dyn Debug,
2642        value3: &dyn Debug,
2643    ) -> Result {
2644        let mut builder = builders::debug_tuple_new(self, name);
2645        builder.field(value1);
2646        builder.field(value2);
2647        builder.field(value3);
2648        builder.finish()
2649    }
2650
2651    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2652    /// binaries. `debug_tuple_fields_finish` is more general, but this is faster
2653    /// for 4 fields.
2654    #[doc(hidden)]
2655    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2656    pub fn debug_tuple_field4_finish<'b>(
2657        &'b mut self,
2658        name: &str,
2659        value1: &dyn Debug,
2660        value2: &dyn Debug,
2661        value3: &dyn Debug,
2662        value4: &dyn Debug,
2663    ) -> Result {
2664        let mut builder = builders::debug_tuple_new(self, name);
2665        builder.field(value1);
2666        builder.field(value2);
2667        builder.field(value3);
2668        builder.field(value4);
2669        builder.finish()
2670    }
2671
2672    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2673    /// binaries. `debug_tuple_fields_finish` is more general, but this is faster
2674    /// for 5 fields.
2675    #[doc(hidden)]
2676    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2677    pub fn debug_tuple_field5_finish<'b>(
2678        &'b mut self,
2679        name: &str,
2680        value1: &dyn Debug,
2681        value2: &dyn Debug,
2682        value3: &dyn Debug,
2683        value4: &dyn Debug,
2684        value5: &dyn Debug,
2685    ) -> Result {
2686        let mut builder = builders::debug_tuple_new(self, name);
2687        builder.field(value1);
2688        builder.field(value2);
2689        builder.field(value3);
2690        builder.field(value4);
2691        builder.field(value5);
2692        builder.finish()
2693    }
2694
2695    /// Shrinks `derive(Debug)` code, for faster compilation and smaller
2696    /// binaries. For the cases not covered by `debug_tuple_field[12345]_finish`.
2697    #[doc(hidden)]
2698    #[unstable(feature = "fmt_helpers_for_derive", issue = "none")]
2699    pub fn debug_tuple_fields_finish<'b>(
2700        &'b mut self,
2701        name: &str,
2702        values: &[&dyn Debug],
2703    ) -> Result {
2704        let mut builder = builders::debug_tuple_new(self, name);
2705        for value in values {
2706            builder.field(value);
2707        }
2708        builder.finish()
2709    }
2710
2711    /// Creates a `DebugList` builder designed to assist with creation of
2712    /// `fmt::Debug` implementations for list-like structures.
2713    ///
2714    /// # Examples
2715    ///
2716    /// ```rust
2717    /// use std::fmt;
2718    ///
2719    /// struct Foo(Vec<i32>);
2720    ///
2721    /// impl fmt::Debug for Foo {
2722    ///     fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2723    ///         fmt.debug_list().entries(self.0.iter()).finish()
2724    ///     }
2725    /// }
2726    ///
2727    /// assert_eq!(format!("{:?}", Foo(vec![10, 11])), "[10, 11]");
2728    /// ```
2729    #[stable(feature = "debug_builders", since = "1.2.0")]
2730    pub fn debug_list<'b>(&'b mut self) -> DebugList<'b, 'a> {
2731        builders::debug_list_new(self)
2732    }
2733
2734    /// Creates a `DebugSet` builder designed to assist with creation of
2735    /// `fmt::Debug` implementations for set-like structures.
2736    ///
2737    /// # Examples
2738    ///
2739    /// ```rust
2740    /// use std::fmt;
2741    ///
2742    /// struct Foo(Vec<i32>);
2743    ///
2744    /// impl fmt::Debug for Foo {
2745    ///     fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2746    ///         fmt.debug_set().entries(self.0.iter()).finish()
2747    ///     }
2748    /// }
2749    ///
2750    /// assert_eq!(format!("{:?}", Foo(vec![10, 11])), "{10, 11}");
2751    /// ```
2752    ///
2753    /// [`format_args!`]: crate::format_args
2754    ///
2755    /// In this more complex example, we use [`format_args!`] and `.debug_set()`
2756    /// to build a list of match arms:
2757    ///
2758    /// ```rust
2759    /// use std::fmt;
2760    ///
2761    /// struct Arm<'a, L, R>(&'a (L, R));
2762    /// struct Table<'a, K, V>(&'a [(K, V)], V);
2763    ///
2764    /// impl<'a, L, R> fmt::Debug for Arm<'a, L, R>
2765    /// where
2766    ///     L: 'a + fmt::Debug, R: 'a + fmt::Debug
2767    /// {
2768    ///     fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2769    ///         L::fmt(&(self.0).0, fmt)?;
2770    ///         fmt.write_str(" => ")?;
2771    ///         R::fmt(&(self.0).1, fmt)
2772    ///     }
2773    /// }
2774    ///
2775    /// impl<'a, K, V> fmt::Debug for Table<'a, K, V>
2776    /// where
2777    ///     K: 'a + fmt::Debug, V: 'a + fmt::Debug
2778    /// {
2779    ///     fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2780    ///         fmt.debug_set()
2781    ///         .entries(self.0.iter().map(Arm))
2782    ///         .entry(&Arm(&(format_args!("_"), &self.1)))
2783    ///         .finish()
2784    ///     }
2785    /// }
2786    /// ```
2787    #[stable(feature = "debug_builders", since = "1.2.0")]
2788    pub fn debug_set<'b>(&'b mut self) -> DebugSet<'b, 'a> {
2789        builders::debug_set_new(self)
2790    }
2791
2792    /// Creates a `DebugMap` builder designed to assist with creation of
2793    /// `fmt::Debug` implementations for map-like structures.
2794    ///
2795    /// # Examples
2796    ///
2797    /// ```rust
2798    /// use std::fmt;
2799    ///
2800    /// struct Foo(Vec<(String, i32)>);
2801    ///
2802    /// impl fmt::Debug for Foo {
2803    ///     fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
2804    ///         fmt.debug_map().entries(self.0.iter().map(|&(ref k, ref v)| (k, v))).finish()
2805    ///     }
2806    /// }
2807    ///
2808    /// assert_eq!(
2809    ///     format!("{:?}",  Foo(vec![("A".to_string(), 10), ("B".to_string(), 11)])),
2810    ///     r#"{"A": 10, "B": 11}"#
2811    ///  );
2812    /// ```
2813    #[stable(feature = "debug_builders", since = "1.2.0")]
2814    pub fn debug_map<'b>(&'b mut self) -> DebugMap<'b, 'a> {
2815        builders::debug_map_new(self)
2816    }
2817
2818    /// Returns the sign of this formatter (`+` or `-`).
2819    #[unstable(feature = "formatting_options", issue = "118117")]
2820    pub const fn sign(&self) -> Option<Sign> {
2821        self.options.get_sign()
2822    }
2823
2824    /// Returns the formatting options this formatter corresponds to.
2825    #[unstable(feature = "formatting_options", issue = "118117")]
2826    pub const fn options(&self) -> FormattingOptions {
2827        self.options
2828    }
2829}
2830
2831#[stable(since = "1.2.0", feature = "formatter_write")]
2832impl Write for Formatter<'_> {
2833    fn write_str(&mut self, s: &str) -> Result {
2834        self.buf.write_str(s)
2835    }
2836
2837    fn write_char(&mut self, c: char) -> Result {
2838        self.buf.write_char(c)
2839    }
2840
2841    #[inline]
2842    fn write_fmt(&mut self, args: Arguments<'_>) -> Result {
2843        if let Some(s) = args.as_statically_known_str() {
2844            self.buf.write_str(s)
2845        } else {
2846            write(self.buf, args)
2847        }
2848    }
2849}
2850
2851#[stable(feature = "rust1", since = "1.0.0")]
2852impl Display for Error {
2853    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2854        Display::fmt("an error occurred when formatting an argument", f)
2855    }
2856}
2857
2858// Implementations of the core formatting traits
2859
2860macro_rules! fmt_refs {
2861    ($($tr:ident),*) => {
2862        $(
2863        #[stable(feature = "rust1", since = "1.0.0")]
2864        impl<T: PointeeSized + $tr> $tr for &T {
2865            fn fmt(&self, f: &mut Formatter<'_>) -> Result { $tr::fmt(&**self, f) }
2866        }
2867        #[stable(feature = "rust1", since = "1.0.0")]
2868        impl<T: PointeeSized + $tr> $tr for &mut T {
2869            fn fmt(&self, f: &mut Formatter<'_>) -> Result { $tr::fmt(&**self, f) }
2870        }
2871        )*
2872    }
2873}
2874
2875fmt_refs! { Debug, Display, Octal, Binary, LowerHex, UpperHex, LowerExp, UpperExp }
2876
2877#[unstable(feature = "never_type", issue = "35121")]
2878impl Debug for ! {
2879    #[inline]
2880    fn fmt(&self, _: &mut Formatter<'_>) -> Result {
2881        *self
2882    }
2883}
2884
2885#[unstable(feature = "never_type", issue = "35121")]
2886impl Display for ! {
2887    #[inline]
2888    fn fmt(&self, _: &mut Formatter<'_>) -> Result {
2889        *self
2890    }
2891}
2892
2893#[stable(feature = "rust1", since = "1.0.0")]
2894impl Debug for bool {
2895    #[inline]
2896    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2897        Display::fmt(self, f)
2898    }
2899}
2900
2901#[stable(feature = "rust1", since = "1.0.0")]
2902impl Display for bool {
2903    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2904        Display::fmt(if *self { "true" } else { "false" }, f)
2905    }
2906}
2907
2908#[stable(feature = "rust1", since = "1.0.0")]
2909impl Debug for str {
2910    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2911        f.write_char('"')?;
2912
2913        // substring we know is printable
2914        let mut printable_range = 0..0;
2915
2916        fn needs_escape(b: u8) -> bool {
2917            b > 0x7E || b < 0x20 || b == b'\\' || b == b'"'
2918        }
2919
2920        // the loop here first skips over runs of printable ASCII as a fast path.
2921        // other chars (unicode, or ASCII that needs escaping) are then handled per-`char`.
2922        let mut rest = self;
2923        while rest.len() > 0 {
2924            let Some(non_printable_start) = rest.as_bytes().iter().position(|&b| needs_escape(b))
2925            else {
2926                printable_range.end += rest.len();
2927                break;
2928            };
2929
2930            printable_range.end += non_printable_start;
2931            // SAFETY: the position was derived from an iterator, so is known to be within bounds, and at a char boundary
2932            rest = unsafe { rest.get_unchecked(non_printable_start..) };
2933
2934            let mut chars = rest.chars();
2935            if let Some(c) = chars.next() {
2936                let esc = c.escape_debug_ext(EscapeDebugExtArgs {
2937                    escape_grapheme_extended: true,
2938                    escape_single_quote: false,
2939                    escape_double_quote: true,
2940                });
2941                if esc.len() != 1 {
2942                    f.write_str(&self[printable_range.clone()])?;
2943                    Display::fmt(&esc, f)?;
2944                    printable_range.start = printable_range.end + c.len_utf8();
2945                }
2946                printable_range.end += c.len_utf8();
2947            }
2948            rest = chars.as_str();
2949        }
2950
2951        f.write_str(&self[printable_range])?;
2952
2953        f.write_char('"')
2954    }
2955}
2956
2957#[stable(feature = "rust1", since = "1.0.0")]
2958impl Display for str {
2959    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2960        f.pad(self)
2961    }
2962}
2963
2964#[stable(feature = "rust1", since = "1.0.0")]
2965impl Debug for char {
2966    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2967        f.write_char('\'')?;
2968        let esc = self.escape_debug_ext(EscapeDebugExtArgs {
2969            escape_grapheme_extended: true,
2970            escape_single_quote: true,
2971            escape_double_quote: false,
2972        });
2973        Display::fmt(&esc, f)?;
2974        f.write_char('\'')
2975    }
2976}
2977
2978#[stable(feature = "rust1", since = "1.0.0")]
2979impl Display for char {
2980    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2981        if f.options.flags & (flags::WIDTH_FLAG | flags::PRECISION_FLAG) == 0 {
2982            f.write_char(*self)
2983        } else {
2984            f.pad(self.encode_utf8(&mut [0; char::MAX_LEN_UTF8]))
2985        }
2986    }
2987}
2988
2989#[stable(feature = "rust1", since = "1.0.0")]
2990impl<T: PointeeSized> Pointer for *const T {
2991    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
2992        if <<T as core::ptr::Pointee>::Metadata as core::unit::IsUnit>::is_unit() {
2993            pointer_fmt_inner(self.expose_provenance(), f)
2994        } else {
2995            f.debug_struct("Pointer")
2996                .field_with("addr", |f| pointer_fmt_inner(self.expose_provenance(), f))
2997                .field("metadata", &core::ptr::metadata(*self))
2998                .finish()
2999        }
3000    }
3001}
3002
3003/// Since the formatting will be identical for all pointer types, uses a
3004/// non-monomorphized implementation for the actual formatting to reduce the
3005/// amount of codegen work needed.
3006///
3007/// This uses `ptr_addr: usize` and not `ptr: *const ()` to be able to use this for
3008/// `fn(...) -> ...` without using [problematic] "Oxford Casts".
3009///
3010/// [problematic]: https://github.com/rust-lang/rust/issues/95489
3011pub(crate) fn pointer_fmt_inner(ptr_addr: usize, f: &mut Formatter<'_>) -> Result {
3012    let old_options = f.options;
3013
3014    // The alternate flag is already treated by LowerHex as being special-
3015    // it denotes whether to prefix with 0x. We use it to work out whether
3016    // or not to zero extend, and then unconditionally set it to get the
3017    // prefix.
3018    if f.options.get_alternate() {
3019        f.options.sign_aware_zero_pad(true);
3020
3021        if f.options.get_width().is_none() {
3022            f.options.width(Some((usize::BITS / 4) as u16 + 2));
3023        }
3024    }
3025    f.options.alternate(true);
3026
3027    let ret = LowerHex::fmt(&ptr_addr, f);
3028
3029    f.options = old_options;
3030
3031    ret
3032}
3033
3034#[stable(feature = "rust1", since = "1.0.0")]
3035impl<T: PointeeSized> Pointer for *mut T {
3036    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3037        Pointer::fmt(&(*self as *const T), f)
3038    }
3039}
3040
3041#[stable(feature = "rust1", since = "1.0.0")]
3042impl<T: PointeeSized> Pointer for &T {
3043    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3044        Pointer::fmt(&(*self as *const T), f)
3045    }
3046}
3047
3048#[stable(feature = "rust1", since = "1.0.0")]
3049impl<T: PointeeSized> Pointer for &mut T {
3050    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3051        Pointer::fmt(&(&**self as *const T), f)
3052    }
3053}
3054
3055// Implementation of Display/Debug for various core types
3056
3057#[stable(feature = "rust1", since = "1.0.0")]
3058impl<T: PointeeSized> Debug for *const T {
3059    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3060        Pointer::fmt(self, f)
3061    }
3062}
3063#[stable(feature = "rust1", since = "1.0.0")]
3064impl<T: PointeeSized> Debug for *mut T {
3065    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3066        Pointer::fmt(self, f)
3067    }
3068}
3069
3070macro_rules! peel {
3071    ($name:ident, $($other:ident,)*) => (tuple! { $($other,)* })
3072}
3073
3074macro_rules! tuple {
3075    () => ();
3076    ( $($name:ident,)+ ) => (
3077        maybe_tuple_doc! {
3078            $($name)+ @
3079            #[stable(feature = "rust1", since = "1.0.0")]
3080            impl<$($name:Debug),+> Debug for ($($name,)+) {
3081                #[allow(non_snake_case, unused_assignments)]
3082                fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3083                    let mut builder = f.debug_tuple("");
3084                    let ($(ref $name,)+) = *self;
3085                    $(
3086                        builder.field(&$name);
3087                    )+
3088
3089                    builder.finish()
3090                }
3091            }
3092        }
3093        peel! { $($name,)+ }
3094    )
3095}
3096
3097macro_rules! maybe_tuple_doc {
3098    ($a:ident @ #[$meta:meta] $item:item) => {
3099        #[doc(fake_variadic)]
3100        #[doc = "This trait is implemented for tuples up to twelve items long."]
3101        #[$meta]
3102        $item
3103    };
3104    ($a:ident $($rest_a:ident)+ @ #[$meta:meta] $item:item) => {
3105        #[doc(hidden)]
3106        #[$meta]
3107        $item
3108    };
3109}
3110
3111tuple! { E, D, C, B, A, Z, Y, X, W, V, U, T, }
3112
3113#[stable(feature = "rust1", since = "1.0.0")]
3114impl<T: Debug> Debug for [T] {
3115    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3116        f.debug_list().entries(self.iter()).finish()
3117    }
3118}
3119
3120#[stable(feature = "rust1", since = "1.0.0")]
3121impl Debug for () {
3122    #[inline]
3123    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3124        f.pad("()")
3125    }
3126}
3127#[stable(feature = "rust1", since = "1.0.0")]
3128impl<T: ?Sized> Debug for PhantomData<T> {
3129    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3130        write!(f, "PhantomData<{}>", crate::any::type_name::<T>())
3131    }
3132}
3133
3134#[stable(feature = "rust1", since = "1.0.0")]
3135impl<T: Copy + Debug> Debug for Cell<T> {
3136    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3137        f.debug_struct("Cell").field("value", &self.get()).finish()
3138    }
3139}
3140
3141#[stable(feature = "rust1", since = "1.0.0")]
3142impl<T: ?Sized + Debug> Debug for RefCell<T> {
3143    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3144        let mut d = f.debug_struct("RefCell");
3145        match self.try_borrow() {
3146            Ok(borrow) => d.field("value", &borrow),
3147            Err(_) => d.field("value", &format_args!("<borrowed>")),
3148        };
3149        d.finish()
3150    }
3151}
3152
3153#[stable(feature = "rust1", since = "1.0.0")]
3154impl<T: ?Sized + Debug> Debug for Ref<'_, T> {
3155    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3156        Debug::fmt(&**self, f)
3157    }
3158}
3159
3160#[stable(feature = "rust1", since = "1.0.0")]
3161impl<T: ?Sized + Debug> Debug for RefMut<'_, T> {
3162    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3163        Debug::fmt(&*(self.deref()), f)
3164    }
3165}
3166
3167#[stable(feature = "core_impl_debug", since = "1.9.0")]
3168impl<T: ?Sized> Debug for UnsafeCell<T> {
3169    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3170        f.debug_struct("UnsafeCell").finish_non_exhaustive()
3171    }
3172}
3173
3174#[unstable(feature = "sync_unsafe_cell", issue = "95439")]
3175impl<T: ?Sized> Debug for SyncUnsafeCell<T> {
3176    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
3177        f.debug_struct("SyncUnsafeCell").finish_non_exhaustive()
3178    }
3179}
3180
3181// If you expected tests to be here, look instead at coretests/tests/fmt/;
3182// it's a lot easier than creating all of the rt::Piece structures here.
3183// There are also tests in alloctests/tests/fmt.rs, for those that need allocations.
````