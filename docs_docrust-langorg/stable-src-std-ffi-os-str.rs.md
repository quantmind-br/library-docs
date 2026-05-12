---
title: os_str.rs - source
url: https://doc.rust-lang.org/stable/src/std/ffi/os_str.rs.html#1718-1720
source: crawler
fetched_at: 2026-05-06T21:33:42.781258092-03:00
rendered_js: false
word_count: 7957
summary: This document defines the OsStr and OsString types, which provide a platform-agnostic way to represent and manipulate system-native strings that may not strictly adhere to UTF-8 encoding.
tags:
    - rust
    - ffi
    - os-string
    - os-str
    - string-handling
    - cross-platform
category: reference
---

## std/ffi/ os\_str.rs

````rust
1//! The [`OsStr`] and [`OsString`] types and associated utilities.
2
3#[cfg(test)]
4mod tests;
5
6use core::clone::CloneToUninit;
7
8use crate::borrow::{Borrow, Cow};
9use crate::collections::TryReserveError;
10use crate::hash::{Hash, Hasher};
11use crate::ops::{self, Range};
12use crate::rc::Rc;
13use crate::str::FromStr;
14use crate::sync::Arc;
15use crate::sys::os_str::{Buf, Slice};
16use crate::sys::{AsInner, FromInner, IntoInner};
17use crate::{cmp, fmt, slice};
18
19/// A type that can represent owned, mutable platform-native strings, but is
20/// cheaply inter-convertible with Rust strings.
21///
22/// The need for this type arises from the fact that:
23///
24/// * On Unix systems, strings are often arbitrary sequences of non-zero
25///   bytes, in many cases interpreted as UTF-8.
26///
27/// * On Windows, strings are often arbitrary sequences of non-zero 16-bit
28///   values, interpreted as UTF-16 when it is valid to do so.
29///
30/// * In Rust, strings are always valid UTF-8, which may contain zeros.
31///
32/// `OsString` and [`OsStr`] bridge this gap by simultaneously representing Rust
33/// and platform-native string values, and in particular allowing a Rust string
34/// to be converted into an "OS" string with no cost if possible. A consequence
35/// of this is that `OsString` instances are *not* `NUL` terminated; in order
36/// to pass to e.g., Unix system call, you should create a [`CStr`].
37///
38/// `OsString` is to <code>&[OsStr]</code> as [`String`] is to <code>&[str]</code>: the former
39/// in each pair are owned strings; the latter are borrowed
40/// references.
41///
42/// Note, `OsString` and [`OsStr`] internally do not necessarily hold strings in
43/// the form native to the platform; While on Unix, strings are stored as a
44/// sequence of 8-bit values, on Windows, where strings are 16-bit value based
45/// as just discussed, strings are also actually stored as a sequence of 8-bit
46/// values, encoded in a less-strict variant of UTF-8. This is useful to
47/// understand when handling capacity and length values.
48///
49/// # Capacity of `OsString`
50///
51/// Capacity uses units of UTF-8 bytes for OS strings which were created from valid unicode, and
52/// uses units of bytes in an unspecified encoding for other contents. On a given target, all
53/// `OsString` and `OsStr` values use the same units for capacity, so the following will work:
54/// ```
55/// use std::ffi::{OsStr, OsString};
56///
57/// fn concat_os_strings(a: &OsStr, b: &OsStr) -> OsString {
58///     let mut ret = OsString::with_capacity(a.len() + b.len()); // This will allocate
59///     ret.push(a); // This will not allocate further
60///     ret.push(b); // This will not allocate further
61///     ret
62/// }
63/// ```
64///
65/// # Creating an `OsString`
66///
67/// **From a Rust string**: `OsString` implements
68/// <code>[From]<[String]></code>, so you can use <code>my_string.[into]\()</code> to
69/// create an `OsString` from a normal Rust string.
70///
71/// **From slices:** Just like you can start with an empty Rust
72/// [`String`] and then [`String::push_str`] some <code>&[str]</code>
73/// sub-string slices into it, you can create an empty `OsString` with
74/// the [`OsString::new`] method and then push string slices into it with the
75/// [`OsString::push`] method.
76///
77/// # Extracting a borrowed reference to the whole OS string
78///
79/// You can use the [`OsString::as_os_str`] method to get an <code>&[OsStr]</code> from
80/// an `OsString`; this is effectively a borrowed reference to the
81/// whole string.
82///
83/// # Conversions
84///
85/// See the [module's toplevel documentation about conversions][conversions] for a discussion on
86/// the traits which `OsString` implements for [conversions] from/to native representations.
87///
88/// [`CStr`]: crate::ffi::CStr
89/// [conversions]: super#conversions
90/// [into]: Into::into
91#[cfg_attr(not(test), rustc_diagnostic_item = "OsString")]
92#[stable(feature = "rust1", since = "1.0.0")]
93pub struct OsString {
94    inner: Buf,
95}
96
97/// Allows extension traits within `std`.
98#[unstable(feature = "sealed", issue = "none")]
99impl crate::sealed::Sealed for OsString {}
100
101/// Borrowed reference to an OS string (see [`OsString`]).
102///
103/// This type represents a borrowed reference to a string in the operating system's preferred
104/// representation.
105///
106/// `&OsStr` is to [`OsString`] as <code>&[str]</code> is to [`String`]: the
107/// former in each pair are borrowed references; the latter are owned strings.
108///
109/// See the [module's toplevel documentation about conversions][conversions] for a discussion on
110/// the traits which `OsStr` implements for [conversions] from/to native representations.
111///
112/// [conversions]: super#conversions
113#[cfg_attr(not(test), rustc_diagnostic_item = "OsStr")]
114#[stable(feature = "rust1", since = "1.0.0")]
115// `OsStr::from_inner` and `impl CloneToUninit for OsStr` current implementation relies
116// on `OsStr` being layout-compatible with `Slice`.
117// However, `OsStr` layout is considered an implementation detail and must not be relied upon.
118#[repr(transparent)]
119pub struct OsStr {
120    inner: Slice,
121}
122
123/// Allows extension traits within `std`.
124#[unstable(feature = "sealed", issue = "none")]
125impl crate::sealed::Sealed for OsStr {}
126
127impl OsString {
128    /// Constructs a new empty `OsString`.
129    ///
130    /// # Examples
131    ///
132    /// ```
133    /// use std::ffi::OsString;
134    ///
135    /// let os_string = OsString::new();
136    /// ```
137    #[stable(feature = "rust1", since = "1.0.0")]
138    #[must_use]
139    #[inline]
140    #[rustc_const_stable(feature = "const_pathbuf_osstring_new", since = "1.91.0")]
141    pub const fn new() -> OsString {
142        OsString { inner: Buf::from_string(String::new()) }
143    }
144
145    /// Converts bytes to an `OsString` without checking that the bytes contains
146    /// valid [`OsStr`]-encoded data.
147    ///
148    /// The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8.
149    /// By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit
150    /// ASCII.
151    ///
152    /// See the [module's toplevel documentation about conversions][conversions] for safe,
153    /// cross-platform [conversions] from/to native representations.
154    ///
155    /// # Safety
156    ///
157    /// As the encoding is unspecified, callers must pass in bytes that originated as a mixture of
158    /// validated UTF-8 and bytes from [`OsStr::as_encoded_bytes`] from within the same Rust version
159    /// built for the same target platform.  For example, reconstructing an `OsString` from bytes sent
160    /// over the network or stored in a file will likely violate these safety rules.
161    ///
162    /// Due to the encoding being self-synchronizing, the bytes from [`OsStr::as_encoded_bytes`] can be
163    /// split either immediately before or immediately after any valid non-empty UTF-8 substring.
164    ///
165    /// # Example
166    ///
167    /// ```
168    /// use std::ffi::OsStr;
169    ///
170    /// let os_str = OsStr::new("Mary had a little lamb");
171    /// let bytes = os_str.as_encoded_bytes();
172    /// let words = bytes.split(|b| *b == b' ');
173    /// let words: Vec<&OsStr> = words.map(|word| {
174    ///     // SAFETY:
175    ///     // - Each `word` only contains content that originated from `OsStr::as_encoded_bytes`
176    ///     // - Only split with ASCII whitespace which is a non-empty UTF-8 substring
177    ///     unsafe { OsStr::from_encoded_bytes_unchecked(word) }
178    /// }).collect();
179    /// ```
180    ///
181    /// [conversions]: super#conversions
182    #[inline]
183    #[stable(feature = "os_str_bytes", since = "1.74.0")]
184    pub unsafe fn from_encoded_bytes_unchecked(bytes: Vec<u8>) -> Self {
185        OsString { inner: unsafe { Buf::from_encoded_bytes_unchecked(bytes) } }
186    }
187
188    /// Converts to an [`OsStr`] slice.
189    ///
190    /// # Examples
191    ///
192    /// ```
193    /// use std::ffi::{OsString, OsStr};
194    ///
195    /// let os_string = OsString::from("foo");
196    /// let os_str = OsStr::new("foo");
197    /// assert_eq!(os_string.as_os_str(), os_str);
198    /// ```
199    #[cfg_attr(not(test), rustc_diagnostic_item = "os_string_as_os_str")]
200    #[stable(feature = "rust1", since = "1.0.0")]
201    #[must_use]
202    #[inline]
203    pub fn as_os_str(&self) -> &OsStr {
204        self
205    }
206
207    /// Converts the `OsString` into a byte vector.  To convert the byte vector back into an
208    /// `OsString`, use the [`OsString::from_encoded_bytes_unchecked`] function.
209    ///
210    /// The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8.
211    /// By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit
212    /// ASCII.
213    ///
214    /// Note: As the encoding is unspecified, any sub-slice of bytes that is not valid UTF-8 should
215    /// be treated as opaque and only comparable within the same Rust version built for the same
216    /// target platform.  For example, sending the bytes over the network or storing it in a file
217    /// will likely result in incompatible data.  See [`OsString`] for more encoding details
218    /// and [`std::ffi`] for platform-specific, specified conversions.
219    ///
220    /// [`std::ffi`]: crate::ffi
221    #[inline]
222    #[stable(feature = "os_str_bytes", since = "1.74.0")]
223    pub fn into_encoded_bytes(self) -> Vec<u8> {
224        self.inner.into_encoded_bytes()
225    }
226
227    /// Converts the `OsString` into a [`String`] if it contains valid Unicode data.
228    ///
229    /// On failure, ownership of the original `OsString` is returned.
230    ///
231    /// # Examples
232    ///
233    /// ```
234    /// use std::ffi::OsString;
235    ///
236    /// let os_string = OsString::from("foo");
237    /// let string = os_string.into_string();
238    /// assert_eq!(string, Ok(String::from("foo")));
239    /// ```
240    #[stable(feature = "rust1", since = "1.0.0")]
241    #[inline]
242    pub fn into_string(self) -> Result<String, OsString> {
243        self.inner.into_string().map_err(|buf| OsString { inner: buf })
244    }
245
246    /// Extends the string with the given <code>&[OsStr]</code> slice.
247    ///
248    /// # Examples
249    ///
250    /// ```
251    /// use std::ffi::OsString;
252    ///
253    /// let mut os_string = OsString::from("foo");
254    /// os_string.push("bar");
255    /// assert_eq!(&os_string, "foobar");
256    /// ```
257    #[stable(feature = "rust1", since = "1.0.0")]
258    #[inline]
259    #[rustc_confusables("append", "put")]
260    pub fn push<T: AsRef<OsStr>>(&mut self, s: T) {
261        trait SpecPushTo {
262            fn spec_push_to(&self, buf: &mut OsString);
263        }
264
265        impl<T: AsRef<OsStr>> SpecPushTo for T {
266            #[inline]
267            default fn spec_push_to(&self, buf: &mut OsString) {
268                buf.inner.push_slice(&self.as_ref().inner);
269            }
270        }
271
272        // Use a more efficient implementation when the string is UTF-8.
273        macro spec_str($T:ty) {
274            impl SpecPushTo for $T {
275                #[inline]
276                fn spec_push_to(&self, buf: &mut OsString) {
277                    buf.inner.push_str(self);
278                }
279            }
280        }
281        spec_str!(str);
282        spec_str!(String);
283
284        s.spec_push_to(self)
285    }
286
287    /// Creates a new `OsString` with at least the given capacity.
288    ///
289    /// The string will be able to hold at least `capacity` length units of other
290    /// OS strings without reallocating. This method is allowed to allocate for
291    /// more units than `capacity`. If `capacity` is 0, the string will not
292    /// allocate.
293    ///
294    /// See the main `OsString` documentation information about encoding and capacity units.
295    ///
296    /// # Examples
297    ///
298    /// ```
299    /// use std::ffi::OsString;
300    ///
301    /// let mut os_string = OsString::with_capacity(10);
302    /// let capacity = os_string.capacity();
303    ///
304    /// // This push is done without reallocating
305    /// os_string.push("foo");
306    ///
307    /// assert_eq!(capacity, os_string.capacity());
308    /// ```
309    #[stable(feature = "osstring_simple_functions", since = "1.9.0")]
310    #[must_use]
311    #[inline]
312    pub fn with_capacity(capacity: usize) -> OsString {
313        OsString { inner: Buf::with_capacity(capacity) }
314    }
315
316    /// Truncates the `OsString` to zero length.
317    ///
318    /// # Examples
319    ///
320    /// ```
321    /// use std::ffi::OsString;
322    ///
323    /// let mut os_string = OsString::from("foo");
324    /// assert_eq!(&os_string, "foo");
325    ///
326    /// os_string.clear();
327    /// assert_eq!(&os_string, "");
328    /// ```
329    #[stable(feature = "osstring_simple_functions", since = "1.9.0")]
330    #[inline]
331    pub fn clear(&mut self) {
332        self.inner.clear()
333    }
334
335    /// Returns the capacity this `OsString` can hold without reallocating.
336    ///
337    /// See the main `OsString` documentation information about encoding and capacity units.
338    ///
339    /// # Examples
340    ///
341    /// ```
342    /// use std::ffi::OsString;
343    ///
344    /// let os_string = OsString::with_capacity(10);
345    /// assert!(os_string.capacity() >= 10);
346    /// ```
347    #[stable(feature = "osstring_simple_functions", since = "1.9.0")]
348    #[must_use]
349    #[inline]
350    pub fn capacity(&self) -> usize {
351        self.inner.capacity()
352    }
353
354    /// Reserves capacity for at least `additional` more capacity to be inserted
355    /// in the given `OsString`. Does nothing if the capacity is
356    /// already sufficient.
357    ///
358    /// The collection may reserve more space to speculatively avoid frequent reallocations.
359    ///
360    /// See the main `OsString` documentation information about encoding and capacity units.
361    ///
362    /// # Examples
363    ///
364    /// ```
365    /// use std::ffi::OsString;
366    ///
367    /// let mut s = OsString::new();
368    /// s.reserve(10);
369    /// assert!(s.capacity() >= 10);
370    /// ```
371    #[stable(feature = "osstring_simple_functions", since = "1.9.0")]
372    #[inline]
373    pub fn reserve(&mut self, additional: usize) {
374        self.inner.reserve(additional)
375    }
376
377    /// Tries to reserve capacity for at least `additional` more length units
378    /// in the given `OsString`. The string may reserve more space to speculatively avoid
379    /// frequent reallocations. After calling `try_reserve`, capacity will be
380    /// greater than or equal to `self.len() + additional` if it returns `Ok(())`.
381    /// Does nothing if capacity is already sufficient. This method preserves
382    /// the contents even if an error occurs.
383    ///
384    /// See the main `OsString` documentation information about encoding and capacity units.
385    ///
386    /// # Errors
387    ///
388    /// If the capacity overflows, or the allocator reports a failure, then an error
389    /// is returned.
390    ///
391    /// # Examples
392    ///
393    /// ```
394    /// use std::ffi::{OsStr, OsString};
395    /// use std::collections::TryReserveError;
396    ///
397    /// fn process_data(data: &str) -> Result<OsString, TryReserveError> {
398    ///     let mut s = OsString::new();
399    ///
400    ///     // Pre-reserve the memory, exiting if we can't
401    ///     s.try_reserve(OsStr::new(data).len())?;
402    ///
403    ///     // Now we know this can't OOM in the middle of our complex work
404    ///     s.push(data);
405    ///
406    ///     Ok(s)
407    /// }
408    /// # process_data("123").expect("why is the test harness OOMing on 3 bytes?");
409    /// ```
410    #[stable(feature = "try_reserve_2", since = "1.63.0")]
411    #[inline]
412    pub fn try_reserve(&mut self, additional: usize) -> Result<(), TryReserveError> {
413        self.inner.try_reserve(additional)
414    }
415
416    /// Reserves the minimum capacity for at least `additional` more capacity to
417    /// be inserted in the given `OsString`. Does nothing if the capacity is
418    /// already sufficient.
419    ///
420    /// Note that the allocator may give the collection more space than it
421    /// requests. Therefore, capacity can not be relied upon to be precisely
422    /// minimal. Prefer [`reserve`] if future insertions are expected.
423    ///
424    /// [`reserve`]: OsString::reserve
425    ///
426    /// See the main `OsString` documentation information about encoding and capacity units.
427    ///
428    /// # Examples
429    ///
430    /// ```
431    /// use std::ffi::OsString;
432    ///
433    /// let mut s = OsString::new();
434    /// s.reserve_exact(10);
435    /// assert!(s.capacity() >= 10);
436    /// ```
437    #[stable(feature = "osstring_simple_functions", since = "1.9.0")]
438    #[inline]
439    pub fn reserve_exact(&mut self, additional: usize) {
440        self.inner.reserve_exact(additional)
441    }
442
443    /// Tries to reserve the minimum capacity for at least `additional`
444    /// more length units in the given `OsString`. After calling
445    /// `try_reserve_exact`, capacity will be greater than or equal to
446    /// `self.len() + additional` if it returns `Ok(())`.
447    /// Does nothing if the capacity is already sufficient.
448    ///
449    /// Note that the allocator may give the `OsString` more space than it
450    /// requests. Therefore, capacity can not be relied upon to be precisely
451    /// minimal. Prefer [`try_reserve`] if future insertions are expected.
452    ///
453    /// [`try_reserve`]: OsString::try_reserve
454    ///
455    /// See the main `OsString` documentation information about encoding and capacity units.
456    ///
457    /// # Errors
458    ///
459    /// If the capacity overflows, or the allocator reports a failure, then an error
460    /// is returned.
461    ///
462    /// # Examples
463    ///
464    /// ```
465    /// use std::ffi::{OsStr, OsString};
466    /// use std::collections::TryReserveError;
467    ///
468    /// fn process_data(data: &str) -> Result<OsString, TryReserveError> {
469    ///     let mut s = OsString::new();
470    ///
471    ///     // Pre-reserve the memory, exiting if we can't
472    ///     s.try_reserve_exact(OsStr::new(data).len())?;
473    ///
474    ///     // Now we know this can't OOM in the middle of our complex work
475    ///     s.push(data);
476    ///
477    ///     Ok(s)
478    /// }
479    /// # process_data("123").expect("why is the test harness OOMing on 3 bytes?");
480    /// ```
481    #[stable(feature = "try_reserve_2", since = "1.63.0")]
482    #[inline]
483    pub fn try_reserve_exact(&mut self, additional: usize) -> Result<(), TryReserveError> {
484        self.inner.try_reserve_exact(additional)
485    }
486
487    /// Shrinks the capacity of the `OsString` to match its length.
488    ///
489    /// See the main `OsString` documentation information about encoding and capacity units.
490    ///
491    /// # Examples
492    ///
493    /// ```
494    /// use std::ffi::OsString;
495    ///
496    /// let mut s = OsString::from("foo");
497    ///
498    /// s.reserve(100);
499    /// assert!(s.capacity() >= 100);
500    ///
501    /// s.shrink_to_fit();
502    /// assert_eq!(3, s.capacity());
503    /// ```
504    #[stable(feature = "osstring_shrink_to_fit", since = "1.19.0")]
505    #[inline]
506    pub fn shrink_to_fit(&mut self) {
507        self.inner.shrink_to_fit()
508    }
509
510    /// Shrinks the capacity of the `OsString` with a lower bound.
511    ///
512    /// The capacity will remain at least as large as both the length
513    /// and the supplied value.
514    ///
515    /// If the current capacity is less than the lower limit, this is a no-op.
516    ///
517    /// See the main `OsString` documentation information about encoding and capacity units.
518    ///
519    /// # Examples
520    ///
521    /// ```
522    /// use std::ffi::OsString;
523    ///
524    /// let mut s = OsString::from("foo");
525    ///
526    /// s.reserve(100);
527    /// assert!(s.capacity() >= 100);
528    ///
529    /// s.shrink_to(10);
530    /// assert!(s.capacity() >= 10);
531    /// s.shrink_to(0);
532    /// assert!(s.capacity() >= 3);
533    /// ```
534    #[inline]
535    #[stable(feature = "shrink_to", since = "1.56.0")]
536    pub fn shrink_to(&mut self, min_capacity: usize) {
537        self.inner.shrink_to(min_capacity)
538    }
539
540    /// Converts this `OsString` into a boxed [`OsStr`].
541    ///
542    /// # Examples
543    ///
544    /// ```
545    /// use std::ffi::{OsString, OsStr};
546    ///
547    /// let s = OsString::from("hello");
548    ///
549    /// let b: Box<OsStr> = s.into_boxed_os_str();
550    /// ```
551    #[must_use = "`self` will be dropped if the result is not used"]
552    #[stable(feature = "into_boxed_os_str", since = "1.20.0")]
553    pub fn into_boxed_os_str(self) -> Box<OsStr> {
554        let rw = Box::into_raw(self.inner.into_box()) as *mut OsStr;
555        unsafe { Box::from_raw(rw) }
556    }
557
558    /// Consumes and leaks the `OsString`, returning a mutable reference to the contents,
559    /// `&'a mut OsStr`.
560    ///
561    /// The caller has free choice over the returned lifetime, including 'static.
562    /// Indeed, this function is ideally used for data that lives for the remainder of
563    /// the program’s life, as dropping the returned reference will cause a memory leak.
564    ///
565    /// It does not reallocate or shrink the `OsString`, so the leaked allocation may include
566    /// unused capacity that is not part of the returned slice. If you want to discard excess
567    /// capacity, call [`into_boxed_os_str`], and then [`Box::leak`] instead.
568    /// However, keep in mind that trimming the capacity may result in a reallocation and copy.
569    ///
570    /// [`into_boxed_os_str`]: Self::into_boxed_os_str
571    #[stable(feature = "os_string_pathbuf_leak", since = "1.89.0")]
572    #[inline]
573    pub fn leak<'a>(self) -> &'a mut OsStr {
574        OsStr::from_inner_mut(self.inner.leak())
575    }
576
577    /// Truncate the `OsString` to the specified length.
578    ///
579    /// # Panics
580    /// Panics if `len` does not lie on a valid `OsStr` boundary
581    /// (as described in [`OsStr::slice_encoded_bytes`]).
582    #[inline]
583    #[unstable(feature = "os_string_truncate", issue = "133262")]
584    pub fn truncate(&mut self, len: usize) {
585        self.as_os_str().inner.check_public_boundary(len);
586        // SAFETY: The length was just checked to be at a valid boundary.
587        unsafe { self.inner.truncate_unchecked(len) };
588    }
589
590    /// Provides plumbing to `Vec::extend_from_slice` without giving full
591    /// mutable access to the `Vec`.
592    ///
593    /// # Safety
594    ///
595    /// The slice must be valid for the platform encoding (as described in
596    /// [`OsStr::from_encoded_bytes_unchecked`]).
597    ///
598    /// This bypasses the encoding-dependent surrogate joining, so either
599    /// `self` must not end with a leading surrogate half, or `other` must not
600    /// start with a trailing surrogate half.
601    #[inline]
602    pub(crate) unsafe fn extend_from_slice_unchecked(&mut self, other: &[u8]) {
603        // SAFETY: Guaranteed by caller.
604        unsafe { self.inner.extend_from_slice_unchecked(other) };
605    }
606}
607
608#[stable(feature = "rust1", since = "1.0.0")]
609impl From<String> for OsString {
610    /// Converts a [`String`] into an [`OsString`].
611    ///
612    /// This conversion does not allocate or copy memory.
613    #[inline]
614    fn from(s: String) -> OsString {
615        OsString { inner: Buf::from_string(s) }
616    }
617}
618
619#[stable(feature = "rust1", since = "1.0.0")]
620impl<T: ?Sized + AsRef<OsStr>> From<&T> for OsString {
621    /// Copies any value implementing <code>[AsRef]&lt;[OsStr]&gt;</code>
622    /// into a newly allocated [`OsString`].
623    fn from(s: &T) -> OsString {
624        trait SpecToOsString {
625            fn spec_to_os_string(&self) -> OsString;
626        }
627
628        impl<T: AsRef<OsStr>> SpecToOsString for T {
629            #[inline]
630            default fn spec_to_os_string(&self) -> OsString {
631                self.as_ref().to_os_string()
632            }
633        }
634
635        // Preserve the known-UTF-8 property for strings.
636        macro spec_str($T:ty) {
637            impl SpecToOsString for $T {
638                #[inline]
639                fn spec_to_os_string(&self) -> OsString {
640                    OsString::from(String::from(self))
641                }
642            }
643        }
644        spec_str!(str);
645        spec_str!(String);
646
647        s.spec_to_os_string()
648    }
649}
650
651#[stable(feature = "rust1", since = "1.0.0")]
652impl ops::Index<ops::RangeFull> for OsString {
653    type Output = OsStr;
654
655    #[inline]
656    fn index(&self, _index: ops::RangeFull) -> &OsStr {
657        OsStr::from_inner(self.inner.as_slice())
658    }
659}
660
661#[stable(feature = "mut_osstr", since = "1.44.0")]
662impl ops::IndexMut<ops::RangeFull> for OsString {
663    #[inline]
664    fn index_mut(&mut self, _index: ops::RangeFull) -> &mut OsStr {
665        OsStr::from_inner_mut(self.inner.as_mut_slice())
666    }
667}
668
669#[stable(feature = "rust1", since = "1.0.0")]
670impl ops::Deref for OsString {
671    type Target = OsStr;
672
673    #[inline]
674    fn deref(&self) -> &OsStr {
675        &self[..]
676    }
677}
678
679#[stable(feature = "mut_osstr", since = "1.44.0")]
680impl ops::DerefMut for OsString {
681    #[inline]
682    fn deref_mut(&mut self) -> &mut OsStr {
683        &mut self[..]
684    }
685}
686
687#[stable(feature = "osstring_default", since = "1.9.0")]
688impl Default for OsString {
689    /// Constructs an empty `OsString`.
690    #[inline]
691    fn default() -> OsString {
692        OsString::new()
693    }
694}
695
696#[stable(feature = "rust1", since = "1.0.0")]
697impl Clone for OsString {
698    #[inline]
699    fn clone(&self) -> Self {
700        OsString { inner: self.inner.clone() }
701    }
702
703    /// Clones the contents of `source` into `self`.
704    ///
705    /// This method is preferred over simply assigning `source.clone()` to `self`,
706    /// as it avoids reallocation if possible.
707    #[inline]
708    fn clone_from(&mut self, source: &Self) {
709        self.inner.clone_from(&source.inner)
710    }
711}
712
713#[stable(feature = "rust1", since = "1.0.0")]
714impl fmt::Debug for OsString {
715    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
716        fmt::Debug::fmt(&**self, formatter)
717    }
718}
719
720#[stable(feature = "rust1", since = "1.0.0")]
721impl PartialEq for OsString {
722    #[inline]
723    fn eq(&self, other: &OsString) -> bool {
724        &**self == &**other
725    }
726}
727
728#[stable(feature = "rust1", since = "1.0.0")]
729impl PartialEq<str> for OsString {
730    #[inline]
731    fn eq(&self, other: &str) -> bool {
732        &**self == other
733    }
734}
735
736#[stable(feature = "rust1", since = "1.0.0")]
737impl PartialEq<OsString> for str {
738    #[inline]
739    fn eq(&self, other: &OsString) -> bool {
740        &**other == self
741    }
742}
743
744#[stable(feature = "os_str_str_ref_eq", since = "1.29.0")]
745impl PartialEq<&str> for OsString {
746    #[inline]
747    fn eq(&self, other: &&str) -> bool {
748        **self == **other
749    }
750}
751
752#[stable(feature = "os_str_str_ref_eq", since = "1.29.0")]
753impl<'a> PartialEq<OsString> for &'a str {
754    #[inline]
755    fn eq(&self, other: &OsString) -> bool {
756        **other == **self
757    }
758}
759
760#[stable(feature = "rust1", since = "1.0.0")]
761impl Eq for OsString {}
762
763#[stable(feature = "rust1", since = "1.0.0")]
764impl PartialOrd for OsString {
765    #[inline]
766    fn partial_cmp(&self, other: &OsString) -> Option<cmp::Ordering> {
767        (&**self).partial_cmp(&**other)
768    }
769    #[inline]
770    fn lt(&self, other: &OsString) -> bool {
771        &**self < &**other
772    }
773    #[inline]
774    fn le(&self, other: &OsString) -> bool {
775        &**self <= &**other
776    }
777    #[inline]
778    fn gt(&self, other: &OsString) -> bool {
779        &**self > &**other
780    }
781    #[inline]
782    fn ge(&self, other: &OsString) -> bool {
783        &**self >= &**other
784    }
785}
786
787#[stable(feature = "rust1", since = "1.0.0")]
788impl PartialOrd<str> for OsString {
789    #[inline]
790    fn partial_cmp(&self, other: &str) -> Option<cmp::Ordering> {
791        (&**self).partial_cmp(other)
792    }
793}
794
795#[stable(feature = "rust1", since = "1.0.0")]
796impl Ord for OsString {
797    #[inline]
798    fn cmp(&self, other: &OsString) -> cmp::Ordering {
799        (&**self).cmp(&**other)
800    }
801}
802
803#[stable(feature = "rust1", since = "1.0.0")]
804impl Hash for OsString {
805    #[inline]
806    fn hash<H: Hasher>(&self, state: &mut H) {
807        (&**self).hash(state)
808    }
809}
810
811#[stable(feature = "os_string_fmt_write", since = "1.64.0")]
812impl fmt::Write for OsString {
813    fn write_str(&mut self, s: &str) -> fmt::Result {
814        self.push(s);
815        Ok(())
816    }
817}
818
819impl OsStr {
820    /// Coerces into an `OsStr` slice.
821    ///
822    /// # Examples
823    ///
824    /// ```
825    /// use std::ffi::OsStr;
826    ///
827    /// let os_str = OsStr::new("foo");
828    /// ```
829    #[inline]
830    #[stable(feature = "rust1", since = "1.0.0")]
831    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
832    pub const fn new<S: [const] AsRef<OsStr> + ?Sized>(s: &S) -> &OsStr {
833        s.as_ref()
834    }
835
836    /// Converts a slice of bytes to an OS string slice without checking that the string contains
837    /// valid `OsStr`-encoded data.
838    ///
839    /// The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8.
840    /// By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit
841    /// ASCII.
842    ///
843    /// See the [module's toplevel documentation about conversions][conversions] for safe,
844    /// cross-platform [conversions] from/to native representations.
845    ///
846    /// # Safety
847    ///
848    /// As the encoding is unspecified, callers must pass in bytes that originated as a mixture of
849    /// validated UTF-8 and bytes from [`OsStr::as_encoded_bytes`] from within the same Rust version
850    /// built for the same target platform.  For example, reconstructing an `OsStr` from bytes sent
851    /// over the network or stored in a file will likely violate these safety rules.
852    ///
853    /// Due to the encoding being self-synchronizing, the bytes from [`OsStr::as_encoded_bytes`] can be
854    /// split either immediately before or immediately after any valid non-empty UTF-8 substring.
855    ///
856    /// # Example
857    ///
858    /// ```
859    /// use std::ffi::OsStr;
860    ///
861    /// let os_str = OsStr::new("Mary had a little lamb");
862    /// let bytes = os_str.as_encoded_bytes();
863    /// let words = bytes.split(|b| *b == b' ');
864    /// let words: Vec<&OsStr> = words.map(|word| {
865    ///     // SAFETY:
866    ///     // - Each `word` only contains content that originated from `OsStr::as_encoded_bytes`
867    ///     // - Only split with ASCII whitespace which is a non-empty UTF-8 substring
868    ///     unsafe { OsStr::from_encoded_bytes_unchecked(word) }
869    /// }).collect();
870    /// ```
871    ///
872    /// [conversions]: super#conversions
873    #[inline]
874    #[stable(feature = "os_str_bytes", since = "1.74.0")]
875    pub unsafe fn from_encoded_bytes_unchecked(bytes: &[u8]) -> &Self {
876        Self::from_inner(unsafe { Slice::from_encoded_bytes_unchecked(bytes) })
877    }
878
879    #[inline]
880    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
881    const fn from_inner(inner: &Slice) -> &OsStr {
882        // SAFETY: OsStr is just a wrapper of Slice,
883        // therefore converting &Slice to &OsStr is safe.
884        unsafe { &*(inner as *const Slice as *const OsStr) }
885    }
886
887    #[inline]
888    #[rustc_const_unstable(feature = "const_convert", issue = "143773")]
889    const fn from_inner_mut(inner: &mut Slice) -> &mut OsStr {
890        // SAFETY: OsStr is just a wrapper of Slice,
891        // therefore converting &mut Slice to &mut OsStr is safe.
892        // Any method that mutates OsStr must be careful not to
893        // break platform-specific encoding, in particular Wtf8 on Windows.
894        unsafe { &mut *(inner as *mut Slice as *mut OsStr) }
895    }
896
897    /// Yields a <code>&[str]</code> slice if the `OsStr` is valid Unicode.
898    ///
899    /// This conversion may entail doing a check for UTF-8 validity.
900    ///
901    /// # Examples
902    ///
903    /// ```
904    /// use std::ffi::OsStr;
905    ///
906    /// let os_str = OsStr::new("foo");
907    /// assert_eq!(os_str.to_str(), Some("foo"));
908    /// ```
909    #[stable(feature = "rust1", since = "1.0.0")]
910    #[must_use = "this returns the result of the operation, \
911                  without modifying the original"]
912    #[inline]
913    pub fn to_str(&self) -> Option<&str> {
914        self.inner.to_str().ok()
915    }
916
917    /// Converts an `OsStr` to a <code>[Cow]<[str]></code>.
918    ///
919    /// Any non-UTF-8 sequences are replaced with
920    /// [`U+FFFD REPLACEMENT CHARACTER`][U+FFFD].
921    ///
922    /// [U+FFFD]: crate::char::REPLACEMENT_CHARACTER
923    ///
924    /// # Examples
925    ///
926    /// Calling `to_string_lossy` on an `OsStr` with invalid unicode:
927    ///
928    /// ```
929    /// // Note, due to differences in how Unix and Windows represent strings,
930    /// // we are forced to complicate this example, setting up example `OsStr`s
931    /// // with different source data and via different platform extensions.
932    /// // Understand that in reality you could end up with such example invalid
933    /// // sequences simply through collecting user command line arguments, for
934    /// // example.
935    ///
936    /// #[cfg(unix)] {
937    ///     use std::ffi::OsStr;
938    ///     use std::os::unix::ffi::OsStrExt;
939    ///
940    ///     // Here, the values 0x66 and 0x6f correspond to 'f' and 'o'
941    ///     // respectively. The value 0x80 is a lone continuation byte, invalid
942    ///     // in a UTF-8 sequence.
943    ///     let source = [0x66, 0x6f, 0x80, 0x6f];
944    ///     let os_str = OsStr::from_bytes(&source[..]);
945    ///
946    ///     assert_eq!(os_str.to_string_lossy(), "fo�o");
947    /// }
948    /// #[cfg(windows)] {
949    ///     use std::ffi::OsString;
950    ///     use std::os::windows::prelude::*;
951    ///
952    ///     // Here the values 0x0066 and 0x006f correspond to 'f' and 'o'
953    ///     // respectively. The value 0xD800 is a lone surrogate half, invalid
954    ///     // in a UTF-16 sequence.
955    ///     let source = [0x0066, 0x006f, 0xD800, 0x006f];
956    ///     let os_string = OsString::from_wide(&source[..]);
957    ///     let os_str = os_string.as_os_str();
958    ///
959    ///     assert_eq!(os_str.to_string_lossy(), "fo�o");
960    /// }
961    /// ```
962    #[stable(feature = "rust1", since = "1.0.0")]
963    #[must_use = "this returns the result of the operation, \
964                  without modifying the original"]
965    #[inline]
966    pub fn to_string_lossy(&self) -> Cow<'_, str> {
967        self.inner.to_string_lossy()
968    }
969
970    /// Copies the slice into an owned [`OsString`].
971    ///
972    /// # Examples
973    ///
974    /// ```
975    /// use std::ffi::{OsStr, OsString};
976    ///
977    /// let os_str = OsStr::new("foo");
978    /// let os_string = os_str.to_os_string();
979    /// assert_eq!(os_string, OsString::from("foo"));
980    /// ```
981    #[stable(feature = "rust1", since = "1.0.0")]
982    #[must_use = "this returns the result of the operation, \
983                  without modifying the original"]
984    #[inline]
985    #[cfg_attr(not(test), rustc_diagnostic_item = "os_str_to_os_string")]
986    pub fn to_os_string(&self) -> OsString {
987        OsString { inner: self.inner.to_owned() }
988    }
989
990    /// Checks whether the `OsStr` is empty.
991    ///
992    /// # Examples
993    ///
994    /// ```
995    /// use std::ffi::OsStr;
996    ///
997    /// let os_str = OsStr::new("");
998    /// assert!(os_str.is_empty());
999    ///
1000    /// let os_str = OsStr::new("foo");
1001    /// assert!(!os_str.is_empty());
1002    /// ```
1003    #[stable(feature = "osstring_simple_functions", since = "1.9.0")]
1004    #[must_use]
1005    #[inline]
1006    pub fn is_empty(&self) -> bool {
1007        self.inner.inner.is_empty()
1008    }
1009
1010    /// Returns the length of this `OsStr`.
1011    ///
1012    /// Note that this does **not** return the number of bytes in the string in
1013    /// OS string form.
1014    ///
1015    /// The length returned is that of the underlying storage used by `OsStr`.
1016    /// As discussed in the [`OsString`] introduction, [`OsString`] and `OsStr`
1017    /// store strings in a form best suited for cheap inter-conversion between
1018    /// native-platform and Rust string forms, which may differ significantly
1019    /// from both of them, including in storage size and encoding.
1020    ///
1021    /// This number is simply useful for passing to other methods, like
1022    /// [`OsString::with_capacity`] to avoid reallocations.
1023    ///
1024    /// See the main `OsString` documentation information about encoding and capacity units.
1025    ///
1026    /// # Examples
1027    ///
1028    /// ```
1029    /// use std::ffi::OsStr;
1030    ///
1031    /// let os_str = OsStr::new("");
1032    /// assert_eq!(os_str.len(), 0);
1033    ///
1034    /// let os_str = OsStr::new("foo");
1035    /// assert_eq!(os_str.len(), 3);
1036    /// ```
1037    #[stable(feature = "osstring_simple_functions", since = "1.9.0")]
1038    #[must_use]
1039    #[inline]
1040    pub fn len(&self) -> usize {
1041        self.inner.inner.len()
1042    }
1043
1044    /// Converts a <code>[Box]<[OsStr]></code> into an [`OsString`] without copying or allocating.
1045    #[stable(feature = "into_boxed_os_str", since = "1.20.0")]
1046    #[must_use = "`self` will be dropped if the result is not used"]
1047    pub fn into_os_string(self: Box<Self>) -> OsString {
1048        let boxed = unsafe { Box::from_raw(Box::into_raw(self) as *mut Slice) };
1049        OsString { inner: Buf::from_box(boxed) }
1050    }
1051
1052    /// Converts an OS string slice to a byte slice.  To convert the byte slice back into an OS
1053    /// string slice, use the [`OsStr::from_encoded_bytes_unchecked`] function.
1054    ///
1055    /// The byte encoding is an unspecified, platform-specific, self-synchronizing superset of UTF-8.
1056    /// By being a self-synchronizing superset of UTF-8, this encoding is also a superset of 7-bit
1057    /// ASCII.
1058    ///
1059    /// Note: As the encoding is unspecified, any sub-slice of bytes that is not valid UTF-8 should
1060    /// be treated as opaque and only comparable within the same Rust version built for the same
1061    /// target platform.  For example, sending the slice over the network or storing it in a file
1062    /// will likely result in incompatible byte slices.  See [`OsString`] for more encoding details
1063    /// and [`std::ffi`] for platform-specific, specified conversions.
1064    ///
1065    /// [`std::ffi`]: crate::ffi
1066    #[inline]
1067    #[stable(feature = "os_str_bytes", since = "1.74.0")]
1068    pub fn as_encoded_bytes(&self) -> &[u8] {
1069        self.inner.as_encoded_bytes()
1070    }
1071
1072    /// Takes a substring based on a range that corresponds to the return value of
1073    /// [`OsStr::as_encoded_bytes`].
1074    ///
1075    /// The range's start and end must lie on valid `OsStr` boundaries.
1076    /// A valid `OsStr` boundary is one of:
1077    /// - The start of the string
1078    /// - The end of the string
1079    /// - Immediately before a valid non-empty UTF-8 substring
1080    /// - Immediately after a valid non-empty UTF-8 substring
1081    ///
1082    /// # Panics
1083    ///
1084    /// Panics if `range` does not lie on valid `OsStr` boundaries or if it
1085    /// exceeds the end of the string.
1086    ///
1087    /// # Example
1088    ///
1089    /// ```
1090    /// #![feature(os_str_slice)]
1091    ///
1092    /// use std::ffi::OsStr;
1093    ///
1094    /// let os_str = OsStr::new("foo=bar");
1095    /// let bytes = os_str.as_encoded_bytes();
1096    /// if let Some(index) = bytes.iter().position(|b| *b == b'=') {
1097    ///     let key = os_str.slice_encoded_bytes(..index);
1098    ///     let value = os_str.slice_encoded_bytes(index + 1..);
1099    ///     assert_eq!(key, "foo");
1100    ///     assert_eq!(value, "bar");
1101    /// }
1102    /// ```
1103    #[unstable(feature = "os_str_slice", issue = "118485")]
1104    pub fn slice_encoded_bytes<R: ops::RangeBounds<usize>>(&self, range: R) -> &Self {
1105        let encoded_bytes = self.as_encoded_bytes();
1106        let Range { start, end } = slice::range(range, ..encoded_bytes.len());
1107
1108        // `check_public_boundary` should panic if the index does not lie on an
1109        // `OsStr` boundary as described above. It's possible to do this in an
1110        // encoding-agnostic way, but details of the internal encoding might
1111        // permit a more efficient implementation.
1112        self.inner.check_public_boundary(start);
1113        self.inner.check_public_boundary(end);
1114
1115        // SAFETY: `slice::range` ensures that `start` and `end` are valid
1116        let slice = unsafe { encoded_bytes.get_unchecked(start..end) };
1117
1118        // SAFETY: `slice` comes from `self` and we validated the boundaries
1119        unsafe { Self::from_encoded_bytes_unchecked(slice) }
1120    }
1121
1122    /// Converts this string to its ASCII lower case equivalent in-place.
1123    ///
1124    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
1125    /// but non-ASCII letters are unchanged.
1126    ///
1127    /// To return a new lowercased value without modifying the existing one, use
1128    /// [`OsStr::to_ascii_lowercase`].
1129    ///
1130    /// # Examples
1131    ///
1132    /// ```
1133    /// use std::ffi::OsString;
1134    ///
1135    /// let mut s = OsString::from("GRÜßE, JÜRGEN ❤");
1136    ///
1137    /// s.make_ascii_lowercase();
1138    ///
1139    /// assert_eq!("grÜße, jÜrgen ❤", s);
1140    /// ```
1141    #[stable(feature = "osstring_ascii", since = "1.53.0")]
1142    #[inline]
1143    pub fn make_ascii_lowercase(&mut self) {
1144        self.inner.make_ascii_lowercase()
1145    }
1146
1147    /// Converts this string to its ASCII upper case equivalent in-place.
1148    ///
1149    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
1150    /// but non-ASCII letters are unchanged.
1151    ///
1152    /// To return a new uppercased value without modifying the existing one, use
1153    /// [`OsStr::to_ascii_uppercase`].
1154    ///
1155    /// # Examples
1156    ///
1157    /// ```
1158    /// use std::ffi::OsString;
1159    ///
1160    /// let mut s = OsString::from("Grüße, Jürgen ❤");
1161    ///
1162    /// s.make_ascii_uppercase();
1163    ///
1164    /// assert_eq!("GRüßE, JüRGEN ❤", s);
1165    /// ```
1166    #[stable(feature = "osstring_ascii", since = "1.53.0")]
1167    #[inline]
1168    pub fn make_ascii_uppercase(&mut self) {
1169        self.inner.make_ascii_uppercase()
1170    }
1171
1172    /// Returns a copy of this string where each character is mapped to its
1173    /// ASCII lower case equivalent.
1174    ///
1175    /// ASCII letters 'A' to 'Z' are mapped to 'a' to 'z',
1176    /// but non-ASCII letters are unchanged.
1177    ///
1178    /// To lowercase the value in-place, use [`OsStr::make_ascii_lowercase`].
1179    ///
1180    /// # Examples
1181    ///
1182    /// ```
1183    /// use std::ffi::OsString;
1184    /// let s = OsString::from("Grüße, Jürgen ❤");
1185    ///
1186    /// assert_eq!("grüße, jürgen ❤", s.to_ascii_lowercase());
1187    /// ```
1188    #[must_use = "to lowercase the value in-place, use `make_ascii_lowercase`"]
1189    #[stable(feature = "osstring_ascii", since = "1.53.0")]
1190    pub fn to_ascii_lowercase(&self) -> OsString {
1191        OsString::from_inner(self.inner.to_ascii_lowercase())
1192    }
1193
1194    /// Returns a copy of this string where each character is mapped to its
1195    /// ASCII upper case equivalent.
1196    ///
1197    /// ASCII letters 'a' to 'z' are mapped to 'A' to 'Z',
1198    /// but non-ASCII letters are unchanged.
1199    ///
1200    /// To uppercase the value in-place, use [`OsStr::make_ascii_uppercase`].
1201    ///
1202    /// # Examples
1203    ///
1204    /// ```
1205    /// use std::ffi::OsString;
1206    /// let s = OsString::from("Grüße, Jürgen ❤");
1207    ///
1208    /// assert_eq!("GRüßE, JüRGEN ❤", s.to_ascii_uppercase());
1209    /// ```
1210    #[must_use = "to uppercase the value in-place, use `make_ascii_uppercase`"]
1211    #[stable(feature = "osstring_ascii", since = "1.53.0")]
1212    pub fn to_ascii_uppercase(&self) -> OsString {
1213        OsString::from_inner(self.inner.to_ascii_uppercase())
1214    }
1215
1216    /// Checks if all characters in this string are within the ASCII range.
1217    ///
1218    /// An empty string returns `true`.
1219    ///
1220    /// # Examples
1221    ///
1222    /// ```
1223    /// use std::ffi::OsString;
1224    ///
1225    /// let ascii = OsString::from("hello!\n");
1226    /// let non_ascii = OsString::from("Grüße, Jürgen ❤");
1227    ///
1228    /// assert!(ascii.is_ascii());
1229    /// assert!(!non_ascii.is_ascii());
1230    /// ```
1231    #[stable(feature = "osstring_ascii", since = "1.53.0")]
1232    #[must_use]
1233    #[inline]
1234    pub fn is_ascii(&self) -> bool {
1235        self.inner.is_ascii()
1236    }
1237
1238    /// Checks that two strings are an ASCII case-insensitive match.
1239    ///
1240    /// Same as `to_ascii_lowercase(a) == to_ascii_lowercase(b)`,
1241    /// but without allocating and copying temporaries.
1242    ///
1243    /// # Examples
1244    ///
1245    /// ```
1246    /// use std::ffi::OsString;
1247    ///
1248    /// assert!(OsString::from("Ferris").eq_ignore_ascii_case("FERRIS"));
1249    /// assert!(OsString::from("Ferrös").eq_ignore_ascii_case("FERRöS"));
1250    /// assert!(!OsString::from("Ferrös").eq_ignore_ascii_case("FERRÖS"));
1251    /// ```
1252    #[stable(feature = "osstring_ascii", since = "1.53.0")]
1253    pub fn eq_ignore_ascii_case<S: AsRef<OsStr>>(&self, other: S) -> bool {
1254        self.inner.eq_ignore_ascii_case(&other.as_ref().inner)
1255    }
1256
1257    /// Returns an object that implements [`Display`] for safely printing an
1258    /// [`OsStr`] that may contain non-Unicode data. This may perform lossy
1259    /// conversion, depending on the platform.  If you would like an
1260    /// implementation which escapes the [`OsStr`] please use [`Debug`]
1261    /// instead.
1262    ///
1263    /// [`Display`]: fmt::Display
1264    /// [`Debug`]: fmt::Debug
1265    ///
1266    /// # Examples
1267    ///
1268    /// ```
1269    /// use std::ffi::OsStr;
1270    ///
1271    /// let s = OsStr::new("Hello, world!");
1272    /// println!("{}", s.display());
1273    /// ```
1274    #[stable(feature = "os_str_display", since = "1.87.0")]
1275    #[must_use = "this does not display the `OsStr`; \
1276                  it returns an object that can be displayed"]
1277    #[inline]
1278    pub fn display(&self) -> Display<'_> {
1279        Display { os_str: self }
1280    }
1281
1282    /// Returns the same string as a string slice `&OsStr`.
1283    ///
1284    /// This method is redundant when used directly on `&OsStr`, but
1285    /// it helps dereferencing other string-like types to string slices,
1286    /// for example references to `Box<OsStr>` or `Arc<OsStr>`.
1287    #[inline]
1288    #[unstable(feature = "str_as_str", issue = "130366")]
1289    pub const fn as_os_str(&self) -> &OsStr {
1290        self
1291    }
1292}
1293
1294#[stable(feature = "box_from_os_str", since = "1.17.0")]
1295impl From<&OsStr> for Box<OsStr> {
1296    /// Copies the string into a newly allocated <code>[Box]&lt;[OsStr]&gt;</code>.
1297    #[inline]
1298    fn from(s: &OsStr) -> Box<OsStr> {
1299        Box::clone_from_ref(s)
1300    }
1301}
1302
1303#[stable(feature = "box_from_mut_slice", since = "1.84.0")]
1304impl From<&mut OsStr> for Box<OsStr> {
1305    /// Copies the string into a newly allocated <code>[Box]&lt;[OsStr]&gt;</code>.
1306    #[inline]
1307    fn from(s: &mut OsStr) -> Box<OsStr> {
1308        Self::from(&*s)
1309    }
1310}
1311
1312#[stable(feature = "box_from_cow", since = "1.45.0")]
1313impl From<Cow<'_, OsStr>> for Box<OsStr> {
1314    /// Converts a `Cow<'a, OsStr>` into a <code>[Box]&lt;[OsStr]&gt;</code>,
1315    /// by copying the contents if they are borrowed.
1316    #[inline]
1317    fn from(cow: Cow<'_, OsStr>) -> Box<OsStr> {
1318        match cow {
1319            Cow::Borrowed(s) => Box::from(s),
1320            Cow::Owned(s) => Box::from(s),
1321        }
1322    }
1323}
1324
1325#[stable(feature = "os_string_from_box", since = "1.18.0")]
1326impl From<Box<OsStr>> for OsString {
1327    /// Converts a <code>[Box]<[OsStr]></code> into an [`OsString`] without copying or
1328    /// allocating.
1329    #[inline]
1330    fn from(boxed: Box<OsStr>) -> OsString {
1331        boxed.into_os_string()
1332    }
1333}
1334
1335#[stable(feature = "box_from_os_string", since = "1.20.0")]
1336impl From<OsString> for Box<OsStr> {
1337    /// Converts an [`OsString`] into a <code>[Box]<[OsStr]></code> without copying or allocating.
1338    #[inline]
1339    fn from(s: OsString) -> Box<OsStr> {
1340        s.into_boxed_os_str()
1341    }
1342}
1343
1344#[stable(feature = "more_box_slice_clone", since = "1.29.0")]
1345impl Clone for Box<OsStr> {
1346    #[inline]
1347    fn clone(&self) -> Self {
1348        self.to_os_string().into_boxed_os_str()
1349    }
1350}
1351
1352#[unstable(feature = "clone_to_uninit", issue = "126799")]
1353unsafe impl CloneToUninit for OsStr {
1354    #[inline]
1355    #[cfg_attr(debug_assertions, track_caller)]
1356    unsafe fn clone_to_uninit(&self, dst: *mut u8) {
1357        // SAFETY: we're just a transparent wrapper around a platform-specific Slice
1358        unsafe { self.inner.clone_to_uninit(dst) }
1359    }
1360}
1361
1362#[stable(feature = "shared_from_slice2", since = "1.24.0")]
1363impl From<OsString> for Arc<OsStr> {
1364    /// Converts an [`OsString`] into an <code>[Arc]<[OsStr]></code> by moving the [`OsString`]
1365    /// data into a new [`Arc`] buffer.
1366    #[inline]
1367    fn from(s: OsString) -> Arc<OsStr> {
1368        let arc = s.inner.into_arc();
1369        unsafe { Arc::from_raw(Arc::into_raw(arc) as *const OsStr) }
1370    }
1371}
1372
1373#[stable(feature = "shared_from_slice2", since = "1.24.0")]
1374impl From<&OsStr> for Arc<OsStr> {
1375    /// Copies the string into a newly allocated <code>[Arc]&lt;[OsStr]&gt;</code>.
1376    #[inline]
1377    fn from(s: &OsStr) -> Arc<OsStr> {
1378        let arc = s.inner.into_arc();
1379        unsafe { Arc::from_raw(Arc::into_raw(arc) as *const OsStr) }
1380    }
1381}
1382
1383#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
1384impl From<&mut OsStr> for Arc<OsStr> {
1385    /// Copies the string into a newly allocated <code>[Arc]&lt;[OsStr]&gt;</code>.
1386    #[inline]
1387    fn from(s: &mut OsStr) -> Arc<OsStr> {
1388        Arc::from(&*s)
1389    }
1390}
1391
1392#[stable(feature = "shared_from_slice2", since = "1.24.0")]
1393impl From<OsString> for Rc<OsStr> {
1394    /// Converts an [`OsString`] into an <code>[Rc]<[OsStr]></code> by moving the [`OsString`]
1395    /// data into a new [`Rc`] buffer.
1396    #[inline]
1397    fn from(s: OsString) -> Rc<OsStr> {
1398        let rc = s.inner.into_rc();
1399        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const OsStr) }
1400    }
1401}
1402
1403#[stable(feature = "shared_from_slice2", since = "1.24.0")]
1404impl From<&OsStr> for Rc<OsStr> {
1405    /// Copies the string into a newly allocated <code>[Rc]&lt;[OsStr]&gt;</code>.
1406    #[inline]
1407    fn from(s: &OsStr) -> Rc<OsStr> {
1408        let rc = s.inner.into_rc();
1409        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const OsStr) }
1410    }
1411}
1412
1413#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
1414impl From<&mut OsStr> for Rc<OsStr> {
1415    /// Copies the string into a newly allocated <code>[Rc]&lt;[OsStr]&gt;</code>.
1416    #[inline]
1417    fn from(s: &mut OsStr) -> Rc<OsStr> {
1418        Rc::from(&*s)
1419    }
1420}
1421
1422#[stable(feature = "cow_from_osstr", since = "1.28.0")]
1423impl<'a> From<OsString> for Cow<'a, OsStr> {
1424    /// Moves the string into a [`Cow::Owned`].
1425    #[inline]
1426    fn from(s: OsString) -> Cow<'a, OsStr> {
1427        Cow::Owned(s)
1428    }
1429}
1430
1431#[stable(feature = "cow_from_osstr", since = "1.28.0")]
1432impl<'a> From<&'a OsStr> for Cow<'a, OsStr> {
1433    /// Converts the string reference into a [`Cow::Borrowed`].
1434    #[inline]
1435    fn from(s: &'a OsStr) -> Cow<'a, OsStr> {
1436        Cow::Borrowed(s)
1437    }
1438}
1439
1440#[stable(feature = "cow_from_osstr", since = "1.28.0")]
1441impl<'a> From<&'a OsString> for Cow<'a, OsStr> {
1442    /// Converts the string reference into a [`Cow::Borrowed`].
1443    #[inline]
1444    fn from(s: &'a OsString) -> Cow<'a, OsStr> {
1445        Cow::Borrowed(s.as_os_str())
1446    }
1447}
1448
1449#[stable(feature = "osstring_from_cow_osstr", since = "1.28.0")]
1450impl<'a> From<Cow<'a, OsStr>> for OsString {
1451    /// Converts a `Cow<'a, OsStr>` into an [`OsString`],
1452    /// by copying the contents if they are borrowed.
1453    #[inline]
1454    fn from(s: Cow<'a, OsStr>) -> Self {
1455        s.into_owned()
1456    }
1457}
1458
1459#[stable(feature = "str_tryfrom_osstr_impl", since = "1.72.0")]
1460impl<'a> TryFrom<&'a OsStr> for &'a str {
1461    type Error = crate::str::Utf8Error;
1462
1463    /// Tries to convert an `&OsStr` to a `&str`.
1464    ///
1465    /// ```
1466    /// use std::ffi::OsStr;
1467    ///
1468    /// let os_str = OsStr::new("foo");
1469    /// let as_str = <&str>::try_from(os_str).unwrap();
1470    /// assert_eq!(as_str, "foo");
1471    /// ```
1472    fn try_from(value: &'a OsStr) -> Result<Self, Self::Error> {
1473        value.inner.to_str()
1474    }
1475}
1476
1477#[stable(feature = "box_default_extra", since = "1.17.0")]
1478impl Default for Box<OsStr> {
1479    #[inline]
1480    fn default() -> Box<OsStr> {
1481        let rw = Box::into_raw(Slice::empty_box()) as *mut OsStr;
1482        unsafe { Box::from_raw(rw) }
1483    }
1484}
1485
1486#[stable(feature = "osstring_default", since = "1.9.0")]
1487impl Default for &OsStr {
1488    /// Creates an empty `OsStr`.
1489    #[inline]
1490    fn default() -> Self {
1491        OsStr::new("")
1492    }
1493}
1494
1495#[stable(feature = "rust1", since = "1.0.0")]
1496impl PartialEq for OsStr {
1497    #[inline]
1498    fn eq(&self, other: &OsStr) -> bool {
1499        self.as_encoded_bytes().eq(other.as_encoded_bytes())
1500    }
1501}
1502
1503#[stable(feature = "rust1", since = "1.0.0")]
1504impl PartialEq<str> for OsStr {
1505    #[inline]
1506    fn eq(&self, other: &str) -> bool {
1507        *self == *OsStr::new(other)
1508    }
1509}
1510
1511#[stable(feature = "rust1", since = "1.0.0")]
1512impl PartialEq<OsStr> for str {
1513    #[inline]
1514    fn eq(&self, other: &OsStr) -> bool {
1515        *other == *OsStr::new(self)
1516    }
1517}
1518
1519#[stable(feature = "rust1", since = "1.0.0")]
1520impl Eq for OsStr {}
1521
1522#[stable(feature = "rust1", since = "1.0.0")]
1523impl PartialOrd for OsStr {
1524    #[inline]
1525    fn partial_cmp(&self, other: &OsStr) -> Option<cmp::Ordering> {
1526        self.as_encoded_bytes().partial_cmp(other.as_encoded_bytes())
1527    }
1528    #[inline]
1529    fn lt(&self, other: &OsStr) -> bool {
1530        self.as_encoded_bytes().lt(other.as_encoded_bytes())
1531    }
1532    #[inline]
1533    fn le(&self, other: &OsStr) -> bool {
1534        self.as_encoded_bytes().le(other.as_encoded_bytes())
1535    }
1536    #[inline]
1537    fn gt(&self, other: &OsStr) -> bool {
1538        self.as_encoded_bytes().gt(other.as_encoded_bytes())
1539    }
1540    #[inline]
1541    fn ge(&self, other: &OsStr) -> bool {
1542        self.as_encoded_bytes().ge(other.as_encoded_bytes())
1543    }
1544}
1545
1546#[stable(feature = "rust1", since = "1.0.0")]
1547impl PartialOrd<str> for OsStr {
1548    #[inline]
1549    fn partial_cmp(&self, other: &str) -> Option<cmp::Ordering> {
1550        self.partial_cmp(OsStr::new(other))
1551    }
1552}
1553
1554// FIXME (#19470): cannot provide PartialOrd<OsStr> for str until we
1555// have more flexible coherence rules.
1556
1557#[stable(feature = "rust1", since = "1.0.0")]
1558impl Ord for OsStr {
1559    #[inline]
1560    fn cmp(&self, other: &OsStr) -> cmp::Ordering {
1561        self.as_encoded_bytes().cmp(other.as_encoded_bytes())
1562    }
1563}
1564
1565macro_rules! impl_cmp {
1566    ($lhs:ty, $rhs: ty) => {
1567        #[stable(feature = "cmp_os_str", since = "1.8.0")]
1568        impl PartialEq<$rhs> for $lhs {
1569            #[inline]
1570            fn eq(&self, other: &$rhs) -> bool {
1571                <OsStr as PartialEq>::eq(self, other)
1572            }
1573        }
1574
1575        #[stable(feature = "cmp_os_str", since = "1.8.0")]
1576        impl PartialEq<$lhs> for $rhs {
1577            #[inline]
1578            fn eq(&self, other: &$lhs) -> bool {
1579                <OsStr as PartialEq>::eq(self, other)
1580            }
1581        }
1582
1583        #[stable(feature = "cmp_os_str", since = "1.8.0")]
1584        impl PartialOrd<$rhs> for $lhs {
1585            #[inline]
1586            fn partial_cmp(&self, other: &$rhs) -> Option<cmp::Ordering> {
1587                <OsStr as PartialOrd>::partial_cmp(self, other)
1588            }
1589        }
1590
1591        #[stable(feature = "cmp_os_str", since = "1.8.0")]
1592        impl PartialOrd<$lhs> for $rhs {
1593            #[inline]
1594            fn partial_cmp(&self, other: &$lhs) -> Option<cmp::Ordering> {
1595                <OsStr as PartialOrd>::partial_cmp(self, other)
1596            }
1597        }
1598    };
1599}
1600
1601impl_cmp!(OsString, OsStr);
1602impl_cmp!(OsString, &OsStr);
1603impl_cmp!(Cow<'_, OsStr>, OsStr);
1604impl_cmp!(Cow<'_, OsStr>, &OsStr);
1605impl_cmp!(Cow<'_, OsStr>, OsString);
1606
1607#[stable(feature = "rust1", since = "1.0.0")]
1608impl Hash for OsStr {
1609    #[inline]
1610    fn hash<H: Hasher>(&self, state: &mut H) {
1611        self.as_encoded_bytes().hash(state)
1612    }
1613}
1614
1615#[stable(feature = "rust1", since = "1.0.0")]
1616impl fmt::Debug for OsStr {
1617    fn fmt(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
1618        fmt::Debug::fmt(&self.inner, formatter)
1619    }
1620}
1621
1622/// Helper struct for safely printing an [`OsStr`] with [`format!`] and `{}`.
1623///
1624/// An [`OsStr`] might contain non-Unicode data. This `struct` implements the
1625/// [`Display`] trait in a way that mitigates that. It is created by the
1626/// [`display`](OsStr::display) method on [`OsStr`]. This may perform lossy
1627/// conversion, depending on the platform. If you would like an implementation
1628/// which escapes the [`OsStr`] please use [`Debug`] instead.
1629///
1630/// # Examples
1631///
1632/// ```
1633/// use std::ffi::OsStr;
1634///
1635/// let s = OsStr::new("Hello, world!");
1636/// println!("{}", s.display());
1637/// ```
1638///
1639/// [`Display`]: fmt::Display
1640/// [`format!`]: crate::format
1641#[stable(feature = "os_str_display", since = "1.87.0")]
1642pub struct Display<'a> {
1643    os_str: &'a OsStr,
1644}
1645
1646#[stable(feature = "os_str_display", since = "1.87.0")]
1647impl fmt::Debug for Display<'_> {
1648    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1649        fmt::Debug::fmt(&self.os_str, f)
1650    }
1651}
1652
1653#[stable(feature = "os_str_display", since = "1.87.0")]
1654impl fmt::Display for Display<'_> {
1655    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1656        fmt::Display::fmt(&self.os_str.inner, f)
1657    }
1658}
1659
1660#[unstable(feature = "slice_concat_ext", issue = "27747")]
1661impl<S: Borrow<OsStr>> alloc::slice::Join<&OsStr> for [S] {
1662    type Output = OsString;
1663
1664    fn join(slice: &Self, sep: &OsStr) -> OsString {
1665        let Some((first, suffix)) = slice.split_first() else {
1666            return OsString::new();
1667        };
1668        let first_owned = first.borrow().to_owned();
1669        suffix.iter().fold(first_owned, |mut a, b| {
1670            a.push(sep);
1671            a.push(b.borrow());
1672            a
1673        })
1674    }
1675}
1676
1677#[stable(feature = "rust1", since = "1.0.0")]
1678impl Borrow<OsStr> for OsString {
1679    #[inline]
1680    fn borrow(&self) -> &OsStr {
1681        &self[..]
1682    }
1683}
1684
1685#[stable(feature = "rust1", since = "1.0.0")]
1686impl ToOwned for OsStr {
1687    type Owned = OsString;
1688    #[inline]
1689    fn to_owned(&self) -> OsString {
1690        self.to_os_string()
1691    }
1692    #[inline]
1693    fn clone_into(&self, target: &mut OsString) {
1694        self.inner.clone_into(&mut target.inner)
1695    }
1696}
1697
1698#[stable(feature = "rust1", since = "1.0.0")]
1699#[rustc_const_unstable(feature = "const_convert", issue = "143773")]
1700impl const AsRef<OsStr> for OsStr {
1701    #[inline]
1702    fn as_ref(&self) -> &OsStr {
1703        self
1704    }
1705}
1706
1707#[stable(feature = "rust1", since = "1.0.0")]
1708impl AsRef<OsStr> for OsString {
1709    #[inline]
1710    fn as_ref(&self) -> &OsStr {
1711        self
1712    }
1713}
1714
1715#[stable(feature = "rust1", since = "1.0.0")]
1716impl AsRef<OsStr> for str {
1717    #[inline]
1718    fn as_ref(&self) -> &OsStr {
1719        OsStr::from_inner(Slice::from_str(self))
1720    }
1721}
1722
1723#[stable(feature = "rust1", since = "1.0.0")]
1724impl AsRef<OsStr> for String {
1725    #[inline]
1726    fn as_ref(&self) -> &OsStr {
1727        (&**self).as_ref()
1728    }
1729}
1730
1731impl FromInner<Buf> for OsString {
1732    #[inline]
1733    fn from_inner(buf: Buf) -> OsString {
1734        OsString { inner: buf }
1735    }
1736}
1737
1738impl IntoInner<Buf> for OsString {
1739    #[inline]
1740    fn into_inner(self) -> Buf {
1741        self.inner
1742    }
1743}
1744
1745impl AsInner<Slice> for OsStr {
1746    #[inline]
1747    fn as_inner(&self) -> &Slice {
1748        &self.inner
1749    }
1750}
1751
1752#[stable(feature = "osstring_from_str", since = "1.45.0")]
1753impl FromStr for OsString {
1754    type Err = core::convert::Infallible;
1755
1756    #[inline]
1757    fn from_str(s: &str) -> Result<Self, Self::Err> {
1758        Ok(OsString::from(s))
1759    }
1760}
1761
1762#[stable(feature = "osstring_extend", since = "1.52.0")]
1763impl Extend<OsString> for OsString {
1764    #[inline]
1765    fn extend<T: IntoIterator<Item = OsString>>(&mut self, iter: T) {
1766        for s in iter {
1767            self.push(&s);
1768        }
1769    }
1770}
1771
1772#[stable(feature = "osstring_extend", since = "1.52.0")]
1773impl<'a> Extend<&'a OsStr> for OsString {
1774    #[inline]
1775    fn extend<T: IntoIterator<Item = &'a OsStr>>(&mut self, iter: T) {
1776        for s in iter {
1777            self.push(s);
1778        }
1779    }
1780}
1781
1782#[stable(feature = "osstring_extend", since = "1.52.0")]
1783impl<'a> Extend<Cow<'a, OsStr>> for OsString {
1784    #[inline]
1785    fn extend<T: IntoIterator<Item = Cow<'a, OsStr>>>(&mut self, iter: T) {
1786        for s in iter {
1787            self.push(&s);
1788        }
1789    }
1790}
1791
1792#[stable(feature = "osstring_extend", since = "1.52.0")]
1793impl FromIterator<OsString> for OsString {
1794    #[inline]
1795    fn from_iter<I: IntoIterator<Item = OsString>>(iter: I) -> Self {
1796        let mut iterator = iter.into_iter();
1797
1798        // Because we're iterating over `OsString`s, we can avoid at least
1799        // one allocation by getting the first string from the iterator
1800        // and appending to it all the subsequent strings.
1801        match iterator.next() {
1802            None => OsString::new(),
1803            Some(mut buf) => {
1804                buf.extend(iterator);
1805                buf
1806            }
1807        }
1808    }
1809}
1810
1811#[stable(feature = "osstring_extend", since = "1.52.0")]
1812impl<'a> FromIterator<&'a OsStr> for OsString {
1813    #[inline]
1814    fn from_iter<I: IntoIterator<Item = &'a OsStr>>(iter: I) -> Self {
1815        let mut buf = Self::new();
1816        for s in iter {
1817            buf.push(s);
1818        }
1819        buf
1820    }
1821}
1822
1823#[stable(feature = "osstring_extend", since = "1.52.0")]
1824impl<'a> FromIterator<Cow<'a, OsStr>> for OsString {
1825    #[inline]
1826    fn from_iter<I: IntoIterator<Item = Cow<'a, OsStr>>>(iter: I) -> Self {
1827        let mut iterator = iter.into_iter();
1828
1829        // Because we're iterating over `OsString`s, we can avoid at least
1830        // one allocation by getting the first owned string from the iterator
1831        // and appending to it all the subsequent strings.
1832        match iterator.next() {
1833            None => OsString::new(),
1834            Some(Cow::Owned(mut buf)) => {
1835                buf.extend(iterator);
1836                buf
1837            }
1838            Some(Cow::Borrowed(buf)) => {
1839                let mut buf = OsString::from(buf);
1840                buf.extend(iterator);
1841                buf
1842            }
1843        }
1844    }
1845}
````