---
title: c_str.rs - source
url: https://doc.rust-lang.org/src/alloc/ffi/c_str.rs.html#841
source: crawler
fetched_at: 2026-05-06T21:23:54.441936265-03:00
rendered_js: false
word_count: 5596
summary: This document defines CString, an owned, nul-terminated string type in Rust designed for safe interoperability with C-style strings.
tags:
    - rust
    - ffi
    - cstring
    - memory-safety
    - interoperability
    - data-types
category: reference
---

## alloc/ffi/ c\_str.rs

````rust
1//! [`CString`] and its related types.
2
3use core::borrow::Borrow;
4use core::ffi::{CStr, c_char};
5use core::num::NonZero;
6use core::slice::memchr;
7use core::str::{self, FromStr, Utf8Error};
8use core::{fmt, mem, ops, ptr, slice};
9
10use crate::borrow::{Cow, ToOwned};
11use crate::boxed::Box;
12use crate::rc::Rc;
13use crate::string::String;
14#[cfg(target_has_atomic = "ptr")]
15use crate::sync::Arc;
16use crate::vec::Vec;
17
18/// A type representing an owned, C-compatible, nul-terminated string with no nul bytes in the
19/// middle.
20///
21/// This type serves the purpose of being able to safely generate a
22/// C-compatible string from a Rust byte slice or vector. An instance of this
23/// type is a static guarantee that the underlying bytes contain no interior 0
24/// bytes ("nul characters") and that the final byte is 0 ("nul terminator").
25///
26/// `CString` is to <code>&[CStr]</code> as [`String`] is to <code>&[str]</code>: the former
27/// in each pair are owned strings; the latter are borrowed
28/// references.
29///
30/// # Creating a `CString`
31///
32/// A `CString` is created from either a byte slice or a byte vector,
33/// or anything that implements <code>[Into]<[Vec]<[u8]>></code> (for
34/// example, you can build a `CString` straight out of a [`String`] or
35/// a <code>&[str]</code>, since both implement that trait).
36/// You can create a `CString` from a literal with `CString::from(c"Text")`.
37///
38/// The [`CString::new`] method will actually check that the provided <code>&[[u8]]</code>
39/// does not have 0 bytes in the middle, and return an error if it
40/// finds one.
41///
42/// # Extracting a raw pointer to the whole C string
43///
44/// `CString` implements an [`as_ptr`][`CStr::as_ptr`] method through the [`Deref`]
45/// trait. This method will give you a `*const c_char` which you can
46/// feed directly to extern functions that expect a nul-terminated
47/// string, like C's `strdup()`. Notice that [`as_ptr`][`CStr::as_ptr`] returns a
48/// read-only pointer; if the C code writes to it, that causes
49/// undefined behavior.
50///
51/// # Extracting a slice of the whole C string
52///
53/// Alternatively, you can obtain a <code>&[[u8]]</code> slice from a
54/// `CString` with the [`CString::as_bytes`] method. Slices produced in this
55/// way do *not* contain the trailing nul terminator. This is useful
56/// when you will be calling an extern function that takes a `*const
57/// u8` argument which is not necessarily nul-terminated, plus another
58/// argument with the length of the string — like C's `strndup()`.
59/// You can of course get the slice's length with its
60/// [`len`][slice::len] method.
61///
62/// If you need a <code>&[[u8]]</code> slice *with* the nul terminator, you
63/// can use [`CString::as_bytes_with_nul`] instead.
64///
65/// Once you have the kind of slice you need (with or without a nul
66/// terminator), you can call the slice's own
67/// [`as_ptr`][slice::as_ptr] method to get a read-only raw pointer to pass to
68/// extern functions. See the documentation for that function for a
69/// discussion on ensuring the lifetime of the raw pointer.
70///
71/// [str]: prim@str "str"
72/// [`Deref`]: ops::Deref
73///
74/// # Examples
75///
76/// ```ignore (extern-declaration)
77/// # fn main() {
78/// use std::ffi::CString;
79/// use std::os::raw::c_char;
80///
81/// extern "C" {
82///     fn my_printer(s: *const c_char);
83/// }
84///
85/// // We are certain that our string doesn't have 0 bytes in the middle,
86/// // so we can .expect()
87/// let c_to_print = CString::new("Hello, world!").expect("CString::new failed");
88/// unsafe {
89///     my_printer(c_to_print.as_ptr());
90/// }
91/// # }
92/// ```
93///
94/// # Safety
95///
96/// `CString` is intended for working with traditional C-style strings
97/// (a sequence of non-nul bytes terminated by a single nul byte); the
98/// primary use case for these kinds of strings is interoperating with C-like
99/// code. Often you will need to transfer ownership to/from that external
100/// code. It is strongly recommended that you thoroughly read through the
101/// documentation of `CString` before use, as improper ownership management
102/// of `CString` instances can lead to invalid memory accesses, memory leaks,
103/// and other memory errors.
104#[derive(PartialEq, PartialOrd, Eq, Ord, Hash, Clone)]
105#[rustc_diagnostic_item = "cstring_type"]
106#[rustc_insignificant_dtor]
107#[stable(feature = "alloc_c_string", since = "1.64.0")]
108pub struct CString {
109    // Invariant 1: the slice ends with a zero byte and has a length of at least one.
110    // Invariant 2: the slice contains only one zero byte.
111    // Improper usage of unsafe function can break Invariant 2, but not Invariant 1.
112    inner: Box<[u8]>,
113}
114
115/// An error indicating that an interior nul byte was found.
116///
117/// While Rust strings may contain nul bytes in the middle, C strings
118/// can't, as that byte would effectively truncate the string.
119///
120/// This error is created by the [`new`][`CString::new`] method on
121/// [`CString`]. See its documentation for more.
122///
123/// # Examples
124///
125/// ```
126/// use std::ffi::{CString, NulError};
127///
128/// let _: NulError = CString::new(b"f\0oo".to_vec()).unwrap_err();
129/// ```
130#[derive(Clone, PartialEq, Eq, Debug)]
131#[stable(feature = "alloc_c_string", since = "1.64.0")]
132pub struct NulError(usize, Vec<u8>);
133
134#[derive(Clone, PartialEq, Eq, Debug)]
135enum FromBytesWithNulErrorKind {
136    InteriorNul(usize),
137    NotNulTerminated,
138}
139
140/// An error indicating that a nul byte was not in the expected position.
141///
142/// The vector used to create a [`CString`] must have one and only one nul byte,
143/// positioned at the end.
144///
145/// This error is created by the [`CString::from_vec_with_nul`] method.
146/// See its documentation for more.
147///
148/// # Examples
149///
150/// ```
151/// use std::ffi::{CString, FromVecWithNulError};
152///
153/// let _: FromVecWithNulError = CString::from_vec_with_nul(b"f\0oo".to_vec()).unwrap_err();
154/// ```
155#[derive(Clone, PartialEq, Eq, Debug)]
156#[stable(feature = "alloc_c_string", since = "1.64.0")]
157pub struct FromVecWithNulError {
158    error_kind: FromBytesWithNulErrorKind,
159    bytes: Vec<u8>,
160}
161
162#[stable(feature = "cstring_from_vec_with_nul", since = "1.58.0")]
163impl FromVecWithNulError {
164    /// Returns a slice of [`u8`]s bytes that were attempted to convert to a [`CString`].
165    ///
166    /// # Examples
167    ///
168    /// Basic usage:
169    ///
170    /// ```
171    /// use std::ffi::CString;
172    ///
173    /// // Some invalid bytes in a vector
174    /// let bytes = b"f\0oo".to_vec();
175    ///
176    /// let value = CString::from_vec_with_nul(bytes.clone());
177    ///
178    /// assert_eq!(&bytes[..], value.unwrap_err().as_bytes());
179    /// ```
180    #[must_use]
181    #[stable(feature = "cstring_from_vec_with_nul", since = "1.58.0")]
182    pub fn as_bytes(&self) -> &[u8] {
183        &self.bytes[..]
184    }
185
186    /// Returns the bytes that were attempted to convert to a [`CString`].
187    ///
188    /// This method is carefully constructed to avoid allocation. It will
189    /// consume the error, moving out the bytes, so that a copy of the bytes
190    /// does not need to be made.
191    ///
192    /// # Examples
193    ///
194    /// Basic usage:
195    ///
196    /// ```
197    /// use std::ffi::CString;
198    ///
199    /// // Some invalid bytes in a vector
200    /// let bytes = b"f\0oo".to_vec();
201    ///
202    /// let value = CString::from_vec_with_nul(bytes.clone());
203    ///
204    /// assert_eq!(bytes, value.unwrap_err().into_bytes());
205    /// ```
206    #[must_use = "`self` will be dropped if the result is not used"]
207    #[stable(feature = "cstring_from_vec_with_nul", since = "1.58.0")]
208    pub fn into_bytes(self) -> Vec<u8> {
209        self.bytes
210    }
211}
212
213/// An error indicating invalid UTF-8 when converting a [`CString`] into a [`String`].
214///
215/// `CString` is just a wrapper over a buffer of bytes with a nul terminator;
216/// [`CString::into_string`] performs UTF-8 validation on those bytes and may
217/// return this error.
218///
219/// This `struct` is created by [`CString::into_string()`]. See
220/// its documentation for more.
221#[derive(Clone, PartialEq, Eq, Debug)]
222#[stable(feature = "alloc_c_string", since = "1.64.0")]
223pub struct IntoStringError {
224    inner: CString,
225    error: Utf8Error,
226}
227
228impl CString {
229    /// Creates a new C-compatible string from a container of bytes.
230    ///
231    /// This function will consume the provided data and use the
232    /// underlying bytes to construct a new string, ensuring that
233    /// there is a trailing 0 byte. This trailing 0 byte will be
234    /// appended by this function; the provided data should *not*
235    /// contain any 0 bytes in it.
236    ///
237    /// # Examples
238    ///
239    /// ```ignore (extern-declaration)
240    /// use std::ffi::CString;
241    /// use std::os::raw::c_char;
242    ///
243    /// extern "C" { fn puts(s: *const c_char); }
244    ///
245    /// let to_print = CString::new("Hello!").expect("CString::new failed");
246    /// unsafe {
247    ///     puts(to_print.as_ptr());
248    /// }
249    /// ```
250    ///
251    /// # Errors
252    ///
253    /// This function will return an error if the supplied bytes contain an
254    /// internal 0 byte. The [`NulError`] returned will contain the bytes as well as
255    /// the position of the nul byte.
256    #[stable(feature = "rust1", since = "1.0.0")]
257    pub fn new<T: Into<Vec<u8>>>(t: T) -> Result<CString, NulError> {
258        trait SpecNewImpl {
259            fn spec_new_impl(self) -> Result<CString, NulError>;
260        }
261
262        impl<T: Into<Vec<u8>>> SpecNewImpl for T {
263            default fn spec_new_impl(self) -> Result<CString, NulError> {
264                let bytes: Vec<u8> = self.into();
265                match memchr::memchr(0, &bytes) {
266                    Some(i) => Err(NulError(i, bytes)),
267                    None => Ok(unsafe { CString::_from_vec_unchecked(bytes) }),
268                }
269            }
270        }
271
272        // Specialization for avoiding reallocation
273        #[inline(always)] // Without that it is not inlined into specializations
274        fn spec_new_impl_bytes(bytes: &[u8]) -> Result<CString, NulError> {
275            // We cannot have such large slice that we would overflow here
276            // but using `checked_add` allows LLVM to assume that capacity never overflows
277            // and generate twice shorter code.
278            // `saturating_add` doesn't help for some reason.
279            let capacity = bytes.len().checked_add(1).unwrap();
280
281            // Allocate before validation to avoid duplication of allocation code.
282            // We still need to allocate and copy memory even if we get an error.
283            let mut buffer = Vec::with_capacity(capacity);
284            buffer.extend(bytes);
285
286            // Check memory of self instead of new buffer.
287            // This allows better optimizations if lto enabled.
288            match memchr::memchr(0, bytes) {
289                Some(i) => Err(NulError(i, buffer)),
290                None => Ok(unsafe { CString::_from_vec_unchecked(buffer) }),
291            }
292        }
293
294        impl SpecNewImpl for &'_ [u8] {
295            fn spec_new_impl(self) -> Result<CString, NulError> {
296                spec_new_impl_bytes(self)
297            }
298        }
299
300        impl SpecNewImpl for &'_ str {
301            fn spec_new_impl(self) -> Result<CString, NulError> {
302                spec_new_impl_bytes(self.as_bytes())
303            }
304        }
305
306        impl SpecNewImpl for &'_ mut [u8] {
307            fn spec_new_impl(self) -> Result<CString, NulError> {
308                spec_new_impl_bytes(self)
309            }
310        }
311
312        t.spec_new_impl()
313    }
314
315    /// Creates a C-compatible string by consuming a byte vector,
316    /// without checking for interior 0 bytes.
317    ///
318    /// Trailing 0 byte will be appended by this function.
319    ///
320    /// This method is equivalent to [`CString::new`] except that no runtime
321    /// assertion is made that `v` contains no 0 bytes, and it requires an
322    /// actual byte vector, not anything that can be converted to one with Into.
323    ///
324    /// # Examples
325    ///
326    /// ```
327    /// use std::ffi::CString;
328    ///
329    /// let raw = b"foo".to_vec();
330    /// unsafe {
331    ///     let c_string = CString::from_vec_unchecked(raw);
332    /// }
333    /// ```
334    #[must_use]
335    #[stable(feature = "rust1", since = "1.0.0")]
336    pub unsafe fn from_vec_unchecked(v: Vec<u8>) -> Self {
337        debug_assert!(memchr::memchr(0, &v).is_none());
338        unsafe { Self::_from_vec_unchecked(v) }
339    }
340
341    unsafe fn _from_vec_unchecked(mut v: Vec<u8>) -> Self {
342        v.reserve_exact(1);
343        v.push(0);
344        Self { inner: v.into_boxed_slice() }
345    }
346
347    /// Retakes ownership of a `CString` that was transferred to C via
348    /// [`CString::into_raw`].
349    ///
350    /// Additionally, the length of the string will be recalculated from the pointer.
351    ///
352    /// # Safety
353    ///
354    /// This should only ever be called with a pointer that was earlier
355    /// obtained by calling [`CString::into_raw`], and the memory it points to must not be accessed
356    /// through any other pointer during the lifetime of reconstructed `CString`.
357    /// Other usage (e.g., trying to take ownership of a string that was allocated by foreign code)
358    /// is likely to lead to undefined behavior or allocator corruption.
359    ///
360    /// This function does not validate ownership of the raw pointer's memory.
361    /// A double-free may occur if the function is called twice on the same raw pointer.
362    /// Additionally, the caller must ensure the pointer is not dangling.
363    ///
364    /// It should be noted that the length isn't just "recomputed," but that
365    /// the recomputed length must match the original length from the
366    /// [`CString::into_raw`] call. This means the [`CString::into_raw`]/`from_raw`
367    /// methods should not be used when passing the string to C functions that can
368    /// modify the string's length.
369    ///
370    /// > **Note:** If you need to borrow a string that was allocated by
371    /// > foreign code, use [`CStr`]. If you need to take ownership of
372    /// > a string that was allocated by foreign code, you will need to
373    /// > make your own provisions for freeing it appropriately, likely
374    /// > with the foreign code's API to do that.
375    ///
376    /// # Examples
377    ///
378    /// Creates a `CString`, pass ownership to an `extern` function (via raw pointer), then retake
379    /// ownership with `from_raw`:
380    ///
381    /// ```ignore (extern-declaration)
382    /// use std::ffi::CString;
383    /// use std::os::raw::c_char;
384    ///
385    /// extern "C" {
386    ///     fn some_extern_function(s: *mut c_char);
387    /// }
388    ///
389    /// let c_string = CString::from(c"Hello!");
390    /// let raw = c_string.into_raw();
391    /// unsafe {
392    ///     some_extern_function(raw);
393    ///     let c_string = CString::from_raw(raw);
394    /// }
395    /// ```
396    #[must_use = "call `drop(from_raw(ptr))` if you intend to drop the `CString`"]
397    #[stable(feature = "cstr_memory", since = "1.4.0")]
398    pub unsafe fn from_raw(ptr: *mut c_char) -> CString {
399        // SAFETY: This is called with a pointer that was obtained from a call
400        // to `CString::into_raw` and the length has not been modified. As such,
401        // we know there is a NUL byte (and only one) at the end and that the
402        // information about the size of the allocation is correct on Rust's
403        // side.
404        unsafe {
405            unsafe extern "C" {
406                /// Provided by libc or compiler_builtins.
407                fn strlen(s: *const c_char) -> usize;
408            }
409            let len = strlen(ptr) + 1; // Including the NUL byte
410            let slice = slice::from_raw_parts_mut(ptr, len);
411            CString { inner: Box::from_raw(slice as *mut [c_char] as *mut [u8]) }
412        }
413    }
414
415    /// Consumes the `CString` and transfers ownership of the string to a C caller.
416    ///
417    /// The pointer which this function returns must be returned to Rust and reconstituted using
418    /// [`CString::from_raw`] to be properly deallocated. Specifically, one
419    /// should *not* use the standard C `free()` function to deallocate
420    /// this string.
421    ///
422    /// Failure to call [`CString::from_raw`] will lead to a memory leak.
423    ///
424    /// The C side must **not** modify the length of the string (by writing a
425    /// nul byte somewhere inside the string or removing the final one) before
426    /// it makes it back into Rust using [`CString::from_raw`]. See the safety section
427    /// in [`CString::from_raw`].
428    ///
429    /// # Examples
430    ///
431    /// ```
432    /// use std::ffi::CString;
433    ///
434    /// let c_string = CString::from(c"foo");
435    ///
436    /// let ptr = c_string.into_raw();
437    ///
438    /// unsafe {
439    ///     assert_eq!(b'f', *ptr as u8);
440    ///     assert_eq!(b'o', *ptr.add(1) as u8);
441    ///     assert_eq!(b'o', *ptr.add(2) as u8);
442    ///     assert_eq!(b'\0', *ptr.add(3) as u8);
443    ///
444    ///     // retake pointer to free memory
445    ///     let _ = CString::from_raw(ptr);
446    /// }
447    /// ```
448    #[inline]
449    #[must_use = "`self` will be dropped if the result is not used"]
450    #[stable(feature = "cstr_memory", since = "1.4.0")]
451    pub fn into_raw(self) -> *mut c_char {
452        Box::into_raw(self.into_inner()) as *mut c_char
453    }
454
455    /// Converts the `CString` into a [`String`] if it contains valid UTF-8 data.
456    ///
457    /// On failure, ownership of the original `CString` is returned.
458    ///
459    /// # Examples
460    ///
461    /// ```
462    /// use std::ffi::CString;
463    ///
464    /// let valid_utf8 = vec![b'f', b'o', b'o'];
465    /// let cstring = CString::new(valid_utf8).expect("CString::new failed");
466    /// assert_eq!(cstring.into_string().expect("into_string() call failed"), "foo");
467    ///
468    /// let invalid_utf8 = vec![b'f', 0xff, b'o', b'o'];
469    /// let cstring = CString::new(invalid_utf8).expect("CString::new failed");
470    /// let err = cstring.into_string().err().expect("into_string().err() failed");
471    /// assert_eq!(err.utf8_error().valid_up_to(), 1);
472    /// ```
473    #[stable(feature = "cstring_into", since = "1.7.0")]
474    pub fn into_string(self) -> Result<String, IntoStringError> {
475        String::from_utf8(self.into_bytes()).map_err(|e| IntoStringError {
476            error: e.utf8_error(),
477            inner: unsafe { Self::_from_vec_unchecked(e.into_bytes()) },
478        })
479    }
480
481    /// Consumes the `CString` and returns the underlying byte buffer.
482    ///
483    /// The returned buffer does **not** contain the trailing nul
484    /// terminator, and it is guaranteed to not have any interior nul
485    /// bytes.
486    ///
487    /// # Examples
488    ///
489    /// ```
490    /// use std::ffi::CString;
491    ///
492    /// let c_string = CString::from(c"foo");
493    /// let bytes = c_string.into_bytes();
494    /// assert_eq!(bytes, vec![b'f', b'o', b'o']);
495    /// ```
496    #[must_use = "`self` will be dropped if the result is not used"]
497    #[stable(feature = "cstring_into", since = "1.7.0")]
498    pub fn into_bytes(self) -> Vec<u8> {
499        let mut vec = self.into_inner().into_vec();
500        let _nul = vec.pop();
501        debug_assert_eq!(_nul, Some(0u8));
502        vec
503    }
504
505    /// Equivalent to [`CString::into_bytes()`] except that the
506    /// returned vector includes the trailing nul terminator.
507    ///
508    /// # Examples
509    ///
510    /// ```
511    /// use std::ffi::CString;
512    ///
513    /// let c_string = CString::from(c"foo");
514    /// let bytes = c_string.into_bytes_with_nul();
515    /// assert_eq!(bytes, vec![b'f', b'o', b'o', b'\0']);
516    /// ```
517    #[must_use = "`self` will be dropped if the result is not used"]
518    #[stable(feature = "cstring_into", since = "1.7.0")]
519    pub fn into_bytes_with_nul(self) -> Vec<u8> {
520        self.into_inner().into_vec()
521    }
522
523    /// Returns the contents of this `CString` as a slice of bytes.
524    ///
525    /// The returned slice does **not** contain the trailing nul
526    /// terminator, and it is guaranteed to not have any interior nul
527    /// bytes. If you need the nul terminator, use
528    /// [`CString::as_bytes_with_nul`] instead.
529    ///
530    /// # Examples
531    ///
532    /// ```
533    /// use std::ffi::CString;
534    ///
535    /// let c_string = CString::from(c"foo");
536    /// let bytes = c_string.as_bytes();
537    /// assert_eq!(bytes, &[b'f', b'o', b'o']);
538    /// ```
539    #[inline]
540    #[must_use]
541    #[stable(feature = "rust1", since = "1.0.0")]
542    pub fn as_bytes(&self) -> &[u8] {
543        // SAFETY: CString has a length at least 1
544        unsafe { self.inner.get_unchecked(..self.inner.len() - 1) }
545    }
546
547    /// Equivalent to [`CString::as_bytes()`] except that the
548    /// returned slice includes the trailing nul terminator.
549    ///
550    /// # Examples
551    ///
552    /// ```
553    /// use std::ffi::CString;
554    ///
555    /// let c_string = CString::from(c"foo");
556    /// let bytes = c_string.as_bytes_with_nul();
557    /// assert_eq!(bytes, &[b'f', b'o', b'o', b'\0']);
558    /// ```
559    #[inline]
560    #[must_use]
561    #[stable(feature = "rust1", since = "1.0.0")]
562    pub fn as_bytes_with_nul(&self) -> &[u8] {
563        &self.inner
564    }
565
566    /// Extracts a [`CStr`] slice containing the entire string.
567    ///
568    /// # Examples
569    ///
570    /// ```
571    /// use std::ffi::{CString, CStr};
572    ///
573    /// let c_string = CString::from(c"foo");
574    /// let cstr = c_string.as_c_str();
575    /// assert_eq!(cstr,
576    ///            CStr::from_bytes_with_nul(b"foo\0").expect("CStr::from_bytes_with_nul failed"));
577    /// ```
578    #[inline]
579    #[must_use]
580    #[stable(feature = "as_c_str", since = "1.20.0")]
581    #[rustc_diagnostic_item = "cstring_as_c_str"]
582    pub fn as_c_str(&self) -> &CStr {
583        unsafe { CStr::from_bytes_with_nul_unchecked(self.as_bytes_with_nul()) }
584    }
585
586    /// Converts this `CString` into a boxed [`CStr`].
587    ///
588    /// # Examples
589    ///
590    /// ```
591    /// let c_string = c"foo".to_owned();
592    /// let boxed = c_string.into_boxed_c_str();
593    /// assert_eq!(boxed.to_bytes_with_nul(), b"foo\0");
594    /// ```
595    #[must_use = "`self` will be dropped if the result is not used"]
596    #[stable(feature = "into_boxed_c_str", since = "1.20.0")]
597    pub fn into_boxed_c_str(self) -> Box<CStr> {
598        unsafe { Box::from_raw(Box::into_raw(self.into_inner()) as *mut CStr) }
599    }
600
601    /// Bypass "move out of struct which implements [`Drop`] trait" restriction.
602    #[inline]
603    fn into_inner(self) -> Box<[u8]> {
604        // Rationale: `mem::forget(self)` invalidates the previous call to `ptr::read(&self.inner)`
605        // so we use `ManuallyDrop` to ensure `self` is not dropped.
606        // Then we can return the box directly without invalidating it.
607        // See https://github.com/rust-lang/rust/issues/62553.
608        let this = mem::ManuallyDrop::new(self);
609        unsafe { ptr::read(&this.inner) }
610    }
611
612    /// Converts a <code>[Vec]<[u8]></code> to a [`CString`] without checking the
613    /// invariants on the given [`Vec`].
614    ///
615    /// # Safety
616    ///
617    /// The given [`Vec`] **must** have one nul byte as its last element.
618    /// This means it cannot be empty nor have any other nul byte anywhere else.
619    ///
620    /// # Example
621    ///
622    /// ```
623    /// use std::ffi::CString;
624    /// assert_eq!(
625    ///     unsafe { CString::from_vec_with_nul_unchecked(b"abc\0".to_vec()) },
626    ///     unsafe { CString::from_vec_unchecked(b"abc".to_vec()) }
627    /// );
628    /// ```
629    #[must_use]
630    #[stable(feature = "cstring_from_vec_with_nul", since = "1.58.0")]
631    pub unsafe fn from_vec_with_nul_unchecked(v: Vec<u8>) -> Self {
632        debug_assert!(memchr::memchr(0, &v).unwrap() + 1 == v.len());
633        unsafe { Self::_from_vec_with_nul_unchecked(v) }
634    }
635
636    unsafe fn _from_vec_with_nul_unchecked(v: Vec<u8>) -> Self {
637        Self { inner: v.into_boxed_slice() }
638    }
639
640    /// Attempts to convert a <code>[Vec]<[u8]></code> to a [`CString`].
641    ///
642    /// Runtime checks are present to ensure there is only one nul byte in the
643    /// [`Vec`], its last element.
644    ///
645    /// # Errors
646    ///
647    /// If a nul byte is present and not the last element or no nul bytes
648    /// is present, an error will be returned.
649    ///
650    /// # Examples
651    ///
652    /// A successful conversion will produce the same result as [`CString::new`]
653    /// when called without the ending nul byte.
654    ///
655    /// ```
656    /// use std::ffi::CString;
657    /// assert_eq!(
658    ///     CString::from_vec_with_nul(b"abc\0".to_vec())
659    ///         .expect("CString::from_vec_with_nul failed"),
660    ///     c"abc".to_owned()
661    /// );
662    /// ```
663    ///
664    /// An incorrectly formatted [`Vec`] will produce an error.
665    ///
666    /// ```
667    /// use std::ffi::{CString, FromVecWithNulError};
668    /// // Interior nul byte
669    /// let _: FromVecWithNulError = CString::from_vec_with_nul(b"a\0bc".to_vec()).unwrap_err();
670    /// // No nul byte
671    /// let _: FromVecWithNulError = CString::from_vec_with_nul(b"abc".to_vec()).unwrap_err();
672    /// ```
673    #[stable(feature = "cstring_from_vec_with_nul", since = "1.58.0")]
674    pub fn from_vec_with_nul(v: Vec<u8>) -> Result<Self, FromVecWithNulError> {
675        let nul_pos = memchr::memchr(0, &v);
676        match nul_pos {
677            Some(nul_pos) if nul_pos + 1 == v.len() => {
678                // SAFETY: We know there is only one nul byte, at the end
679                // of the vec.
680                Ok(unsafe { Self::_from_vec_with_nul_unchecked(v) })
681            }
682            Some(nul_pos) => Err(FromVecWithNulError {
683                error_kind: FromBytesWithNulErrorKind::InteriorNul(nul_pos),
684                bytes: v,
685            }),
686            None => Err(FromVecWithNulError {
687                error_kind: FromBytesWithNulErrorKind::NotNulTerminated,
688                bytes: v,
689            }),
690        }
691    }
692}
693
694// Turns this `CString` into an empty string to prevent
695// memory-unsafe code from working by accident. Inline
696// to prevent LLVM from optimizing it away in debug builds.
697#[stable(feature = "cstring_drop", since = "1.13.0")]
698impl Drop for CString {
699    #[inline]
700    fn drop(&mut self) {
701        unsafe {
702            *self.inner.get_unchecked_mut(0) = 0;
703        }
704    }
705}
706
707#[stable(feature = "rust1", since = "1.0.0")]
708impl ops::Deref for CString {
709    type Target = CStr;
710
711    #[inline]
712    fn deref(&self) -> &CStr {
713        self.as_c_str()
714    }
715}
716
717/// Delegates to the [`CStr`] implementation of [`fmt::Debug`],
718/// showing invalid UTF-8 as hex escapes.
719#[stable(feature = "rust1", since = "1.0.0")]
720impl fmt::Debug for CString {
721    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
722        fmt::Debug::fmt(self.as_c_str(), f)
723    }
724}
725
726#[stable(feature = "cstring_into", since = "1.7.0")]
727impl From<CString> for Vec<u8> {
728    /// Converts a [`CString`] into a <code>[Vec]<[u8]></code>.
729    ///
730    /// The conversion consumes the [`CString`], and removes the terminating NUL byte.
731    #[inline]
732    fn from(s: CString) -> Vec<u8> {
733        s.into_bytes()
734    }
735}
736
737#[stable(feature = "cstr_default", since = "1.10.0")]
738impl Default for CString {
739    /// Creates an empty `CString`.
740    fn default() -> CString {
741        let a: &CStr = Default::default();
742        a.to_owned()
743    }
744}
745
746#[stable(feature = "cstr_borrow", since = "1.3.0")]
747impl Borrow<CStr> for CString {
748    #[inline]
749    fn borrow(&self) -> &CStr {
750        self
751    }
752}
753
754#[stable(feature = "cstring_from_cow_cstr", since = "1.28.0")]
755impl<'a> From<Cow<'a, CStr>> for CString {
756    /// Converts a `Cow<'a, CStr>` into a `CString`, by copying the contents if they are
757    /// borrowed.
758    #[inline]
759    fn from(s: Cow<'a, CStr>) -> Self {
760        s.into_owned()
761    }
762}
763
764#[stable(feature = "box_from_c_str", since = "1.17.0")]
765impl From<&CStr> for Box<CStr> {
766    /// Converts a `&CStr` into a `Box<CStr>`,
767    /// by copying the contents into a newly allocated [`Box`].
768    fn from(s: &CStr) -> Box<CStr> {
769        Box::clone_from_ref(s)
770    }
771}
772
773#[stable(feature = "box_from_mut_slice", since = "1.84.0")]
774impl From<&mut CStr> for Box<CStr> {
775    /// Converts a `&mut CStr` into a `Box<CStr>`,
776    /// by copying the contents into a newly allocated [`Box`].
777    fn from(s: &mut CStr) -> Box<CStr> {
778        Self::from(&*s)
779    }
780}
781
782#[stable(feature = "box_from_cow", since = "1.45.0")]
783impl From<Cow<'_, CStr>> for Box<CStr> {
784    /// Converts a `Cow<'a, CStr>` into a `Box<CStr>`,
785    /// by copying the contents if they are borrowed.
786    #[inline]
787    fn from(cow: Cow<'_, CStr>) -> Box<CStr> {
788        match cow {
789            Cow::Borrowed(s) => Box::from(s),
790            Cow::Owned(s) => Box::from(s),
791        }
792    }
793}
794
795#[stable(feature = "c_string_from_box", since = "1.18.0")]
796impl From<Box<CStr>> for CString {
797    /// Converts a <code>[Box]<[CStr]></code> into a [`CString`] without copying or allocating.
798    #[inline]
799    fn from(s: Box<CStr>) -> CString {
800        let raw = Box::into_raw(s) as *mut [u8];
801        CString { inner: unsafe { Box::from_raw(raw) } }
802    }
803}
804
805#[stable(feature = "cstring_from_vec_of_nonzerou8", since = "1.43.0")]
806impl From<Vec<NonZero<u8>>> for CString {
807    /// Converts a <code>[Vec]<[NonZero]<[u8]>></code> into a [`CString`] without
808    /// copying nor checking for inner nul bytes.
809    #[inline]
810    fn from(v: Vec<NonZero<u8>>) -> CString {
811        unsafe {
812            // Transmute `Vec<NonZero<u8>>` to `Vec<u8>`.
813            let v: Vec<u8> = {
814                // SAFETY:
815                //   - transmuting between `NonZero<u8>` and `u8` is sound;
816                //   - `alloc::Layout<NonZero<u8>> == alloc::Layout<u8>`.
817                let (ptr, len, cap): (*mut NonZero<u8>, _, _) = Vec::into_raw_parts(v);
818                Vec::from_raw_parts(ptr.cast::<u8>(), len, cap)
819            };
820            // SAFETY: `v` cannot contain nul bytes, given the type-level
821            // invariant of `NonZero<u8>`.
822            Self::_from_vec_unchecked(v)
823        }
824    }
825}
826
827#[stable(feature = "c_string_from_str", since = "1.85.0")]
828impl FromStr for CString {
829    type Err = NulError;
830
831    /// Converts a string `s` into a [`CString`].
832    ///
833    /// This method is equivalent to [`CString::new`].
834    #[inline]
835    fn from_str(s: &str) -> Result<Self, Self::Err> {
836        Self::new(s)
837    }
838}
839
840#[stable(feature = "c_string_from_str", since = "1.85.0")]
841impl TryFrom<CString> for String {
842    type Error = IntoStringError;
843
844    /// Converts a [`CString`] into a [`String`] if it contains valid UTF-8 data.
845    ///
846    /// This method is equivalent to [`CString::into_string`].
847    #[inline]
848    fn try_from(value: CString) -> Result<Self, Self::Error> {
849        value.into_string()
850    }
851}
852
853#[stable(feature = "more_box_slice_clone", since = "1.29.0")]
854impl Clone for Box<CStr> {
855    #[inline]
856    fn clone(&self) -> Self {
857        (**self).into()
858    }
859}
860
861#[stable(feature = "box_from_c_string", since = "1.20.0")]
862impl From<CString> for Box<CStr> {
863    /// Converts a [`CString`] into a <code>[Box]<[CStr]></code> without copying or allocating.
864    #[inline]
865    fn from(s: CString) -> Box<CStr> {
866        s.into_boxed_c_str()
867    }
868}
869
870#[stable(feature = "cow_from_cstr", since = "1.28.0")]
871impl<'a> From<CString> for Cow<'a, CStr> {
872    /// Converts a [`CString`] into an owned [`Cow`] without copying or allocating.
873    #[inline]
874    fn from(s: CString) -> Cow<'a, CStr> {
875        Cow::Owned(s)
876    }
877}
878
879#[stable(feature = "cow_from_cstr", since = "1.28.0")]
880impl<'a> From<&'a CStr> for Cow<'a, CStr> {
881    /// Converts a [`CStr`] into a borrowed [`Cow`] without copying or allocating.
882    #[inline]
883    fn from(s: &'a CStr) -> Cow<'a, CStr> {
884        Cow::Borrowed(s)
885    }
886}
887
888#[stable(feature = "cow_from_cstr", since = "1.28.0")]
889impl<'a> From<&'a CString> for Cow<'a, CStr> {
890    /// Converts a `&`[`CString`] into a borrowed [`Cow`] without copying or allocating.
891    #[inline]
892    fn from(s: &'a CString) -> Cow<'a, CStr> {
893        Cow::Borrowed(s.as_c_str())
894    }
895}
896
897#[cfg(target_has_atomic = "ptr")]
898#[stable(feature = "shared_from_slice2", since = "1.24.0")]
899impl From<CString> for Arc<CStr> {
900    /// Converts a [`CString`] into an <code>[Arc]<[CStr]></code> by moving the [`CString`]
901    /// data into a new [`Arc`] buffer.
902    #[inline]
903    fn from(s: CString) -> Arc<CStr> {
904        let arc: Arc<[u8]> = Arc::from(s.into_inner());
905        unsafe { Arc::from_raw(Arc::into_raw(arc) as *const CStr) }
906    }
907}
908
909#[cfg(target_has_atomic = "ptr")]
910#[stable(feature = "shared_from_slice2", since = "1.24.0")]
911impl From<&CStr> for Arc<CStr> {
912    /// Converts a `&CStr` into a `Arc<CStr>`,
913    /// by copying the contents into a newly allocated [`Arc`].
914    #[inline]
915    fn from(s: &CStr) -> Arc<CStr> {
916        let arc: Arc<[u8]> = Arc::from(s.to_bytes_with_nul());
917        unsafe { Arc::from_raw(Arc::into_raw(arc) as *const CStr) }
918    }
919}
920
921#[cfg(target_has_atomic = "ptr")]
922#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
923impl From<&mut CStr> for Arc<CStr> {
924    /// Converts a `&mut CStr` into a `Arc<CStr>`,
925    /// by copying the contents into a newly allocated [`Arc`].
926    #[inline]
927    fn from(s: &mut CStr) -> Arc<CStr> {
928        Arc::from(&*s)
929    }
930}
931
932#[stable(feature = "shared_from_slice2", since = "1.24.0")]
933impl From<CString> for Rc<CStr> {
934    /// Converts a [`CString`] into an <code>[Rc]<[CStr]></code> by moving the [`CString`]
935    /// data into a new [`Rc`] buffer.
936    #[inline]
937    fn from(s: CString) -> Rc<CStr> {
938        let rc: Rc<[u8]> = Rc::from(s.into_inner());
939        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const CStr) }
940    }
941}
942
943#[stable(feature = "shared_from_slice2", since = "1.24.0")]
944impl From<&CStr> for Rc<CStr> {
945    /// Converts a `&CStr` into a `Rc<CStr>`,
946    /// by copying the contents into a newly allocated [`Rc`].
947    #[inline]
948    fn from(s: &CStr) -> Rc<CStr> {
949        let rc: Rc<[u8]> = Rc::from(s.to_bytes_with_nul());
950        unsafe { Rc::from_raw(Rc::into_raw(rc) as *const CStr) }
951    }
952}
953
954#[stable(feature = "shared_from_mut_slice", since = "1.84.0")]
955impl From<&mut CStr> for Rc<CStr> {
956    /// Converts a `&mut CStr` into a `Rc<CStr>`,
957    /// by copying the contents into a newly allocated [`Rc`].
958    #[inline]
959    fn from(s: &mut CStr) -> Rc<CStr> {
960        Rc::from(&*s)
961    }
962}
963
964#[cfg(not(no_global_oom_handling))]
965#[stable(feature = "more_rc_default_impls", since = "1.80.0")]
966impl Default for Rc<CStr> {
967    /// Creates an empty CStr inside an Rc
968    ///
969    /// This may or may not share an allocation with other Rcs on the same thread.
970    #[inline]
971    fn default() -> Self {
972        Rc::from(c"")
973    }
974}
975
976#[stable(feature = "default_box_extra", since = "1.17.0")]
977impl Default for Box<CStr> {
978    fn default() -> Box<CStr> {
979        Box::from(c"")
980    }
981}
982
983impl NulError {
984    /// Returns the position of the nul byte in the slice that caused
985    /// [`CString::new`] to fail.
986    ///
987    /// # Examples
988    ///
989    /// ```
990    /// use std::ffi::CString;
991    ///
992    /// let nul_error = CString::new("foo\0bar").unwrap_err();
993    /// assert_eq!(nul_error.nul_position(), 3);
994    ///
995    /// let nul_error = CString::new("foo bar\0").unwrap_err();
996    /// assert_eq!(nul_error.nul_position(), 7);
997    /// ```
998    #[must_use]
999    #[stable(feature = "rust1", since = "1.0.0")]
1000    pub fn nul_position(&self) -> usize {
1001        self.0
1002    }
1003
1004    /// Consumes this error, returning the underlying vector of bytes which
1005    /// generated the error in the first place.
1006    ///
1007    /// # Examples
1008    ///
1009    /// ```
1010    /// use std::ffi::CString;
1011    ///
1012    /// let nul_error = CString::new("foo\0bar").unwrap_err();
1013    /// assert_eq!(nul_error.into_vec(), b"foo\0bar");
1014    /// ```
1015    #[must_use = "`self` will be dropped if the result is not used"]
1016    #[stable(feature = "rust1", since = "1.0.0")]
1017    pub fn into_vec(self) -> Vec<u8> {
1018        self.1
1019    }
1020}
1021
1022#[stable(feature = "rust1", since = "1.0.0")]
1023impl fmt::Display for NulError {
1024    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1025        write!(f, "nul byte found in provided data at position: {}", self.0)
1026    }
1027}
1028
1029#[stable(feature = "cstring_from_vec_with_nul", since = "1.58.0")]
1030impl fmt::Display for FromVecWithNulError {
1031    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1032        match self.error_kind {
1033            FromBytesWithNulErrorKind::InteriorNul(pos) => {
1034                write!(f, "data provided contains an interior nul byte at pos {pos}")
1035            }
1036            FromBytesWithNulErrorKind::NotNulTerminated => {
1037                write!(f, "data provided is not nul terminated")
1038            }
1039        }
1040    }
1041}
1042
1043impl IntoStringError {
1044    /// Consumes this error, returning original [`CString`] which generated the
1045    /// error.
1046    #[must_use = "`self` will be dropped if the result is not used"]
1047    #[stable(feature = "cstring_into", since = "1.7.0")]
1048    pub fn into_cstring(self) -> CString {
1049        self.inner
1050    }
1051
1052    /// Access the underlying UTF-8 error that was the cause of this error.
1053    #[must_use]
1054    #[stable(feature = "cstring_into", since = "1.7.0")]
1055    pub fn utf8_error(&self) -> Utf8Error {
1056        self.error
1057    }
1058}
1059
1060#[stable(feature = "cstring_into", since = "1.7.0")]
1061impl fmt::Display for IntoStringError {
1062    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1063        "C string contained non-utf8 bytes".fmt(f)
1064    }
1065}
1066
1067#[stable(feature = "cstr_borrow", since = "1.3.0")]
1068impl ToOwned for CStr {
1069    type Owned = CString;
1070
1071    fn to_owned(&self) -> CString {
1072        CString { inner: self.to_bytes_with_nul().into() }
1073    }
1074
1075    fn clone_into(&self, target: &mut CString) {
1076        let mut b = mem::take(&mut target.inner).into_vec();
1077        self.to_bytes_with_nul().clone_into(&mut b);
1078        target.inner = b.into_boxed_slice();
1079    }
1080}
1081
1082#[stable(feature = "cstring_asref", since = "1.7.0")]
1083impl From<&CStr> for CString {
1084    /// Converts a <code>&[CStr]</code> into a [`CString`]
1085    /// by copying the contents into a new allocation.
1086    fn from(s: &CStr) -> CString {
1087        s.to_owned()
1088    }
1089}
1090
1091#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1092impl PartialEq<CStr> for CString {
1093    #[inline]
1094    fn eq(&self, other: &CStr) -> bool {
1095        **self == *other
1096    }
1097
1098    #[inline]
1099    fn ne(&self, other: &CStr) -> bool {
1100        **self != *other
1101    }
1102}
1103
1104#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1105impl PartialEq<&CStr> for CString {
1106    #[inline]
1107    fn eq(&self, other: &&CStr) -> bool {
1108        **self == **other
1109    }
1110
1111    #[inline]
1112    fn ne(&self, other: &&CStr) -> bool {
1113        **self != **other
1114    }
1115}
1116
1117#[cfg(not(no_global_oom_handling))]
1118#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1119impl PartialEq<Cow<'_, CStr>> for CString {
1120    #[inline]
1121    fn eq(&self, other: &Cow<'_, CStr>) -> bool {
1122        **self == **other
1123    }
1124
1125    #[inline]
1126    fn ne(&self, other: &Cow<'_, CStr>) -> bool {
1127        **self != **other
1128    }
1129}
1130
1131#[stable(feature = "cstring_asref", since = "1.7.0")]
1132impl ops::Index<ops::RangeFull> for CString {
1133    type Output = CStr;
1134
1135    #[inline]
1136    fn index(&self, _index: ops::RangeFull) -> &CStr {
1137        self
1138    }
1139}
1140
1141#[stable(feature = "cstring_asref", since = "1.7.0")]
1142impl AsRef<CStr> for CString {
1143    #[inline]
1144    fn as_ref(&self) -> &CStr {
1145        self
1146    }
1147}
1148
1149impl CStr {
1150    /// Converts a `CStr` into a <code>[Cow]<[str]></code>.
1151    ///
1152    /// If the contents of the `CStr` are valid UTF-8 data, this
1153    /// function will return a <code>[Cow]::[Borrowed]\(&[str])</code>
1154    /// with the corresponding <code>&[str]</code> slice. Otherwise, it will
1155    /// replace any invalid UTF-8 sequences with
1156    /// [`U+FFFD REPLACEMENT CHARACTER`][U+FFFD] and return a
1157    /// <code>[Cow]::[Owned]\([String])</code> with the result.
1158    ///
1159    /// [str]: prim@str "str"
1160    /// [Borrowed]: Cow::Borrowed
1161    /// [Owned]: Cow::Owned
1162    /// [U+FFFD]: core::char::REPLACEMENT_CHARACTER "std::char::REPLACEMENT_CHARACTER"
1163    ///
1164    /// # Examples
1165    ///
1166    /// Calling `to_string_lossy` on a `CStr` containing valid UTF-8. The leading
1167    /// `c` on the string literal denotes a `CStr`.
1168    ///
1169    /// ```
1170    /// use std::borrow::Cow;
1171    ///
1172    /// assert_eq!(c"Hello World".to_string_lossy(), Cow::Borrowed("Hello World"));
1173    /// ```
1174    ///
1175    /// Calling `to_string_lossy` on a `CStr` containing invalid UTF-8:
1176    ///
1177    /// ```
1178    /// use std::borrow::Cow;
1179    ///
1180    /// assert_eq!(
1181    ///     c"Hello \xF0\x90\x80World".to_string_lossy(),
1182    ///     Cow::Owned(String::from("Hello �World")) as Cow<'_, str>
1183    /// );
1184    /// ```
1185    #[rustc_allow_incoherent_impl]
1186    #[must_use = "this returns the result of the operation, \
1187                  without modifying the original"]
1188    #[stable(feature = "cstr_to_str", since = "1.4.0")]
1189    pub fn to_string_lossy(&self) -> Cow<'_, str> {
1190        String::from_utf8_lossy(self.to_bytes())
1191    }
1192
1193    /// Converts a <code>[Box]<[CStr]></code> into a [`CString`] without copying or allocating.
1194    ///
1195    /// # Examples
1196    ///
1197    /// ```
1198    /// use std::ffi::{CStr, CString};
1199    ///
1200    /// let boxed: Box<CStr> = Box::from(c"foo");
1201    /// let c_string: CString = c"foo".to_owned();
1202    ///
1203    /// assert_eq!(boxed.into_c_string(), c_string);
1204    /// ```
1205    #[rustc_allow_incoherent_impl]
1206    #[must_use = "`self` will be dropped if the result is not used"]
1207    #[stable(feature = "into_boxed_c_str", since = "1.20.0")]
1208    pub fn into_c_string(self: Box<Self>) -> CString {
1209        CString::from(self)
1210    }
1211}
1212
1213#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1214impl PartialEq<CString> for CStr {
1215    #[inline]
1216    fn eq(&self, other: &CString) -> bool {
1217        *self == **other
1218    }
1219
1220    #[inline]
1221    fn ne(&self, other: &CString) -> bool {
1222        *self != **other
1223    }
1224}
1225
1226#[cfg(not(no_global_oom_handling))]
1227#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1228impl PartialEq<Cow<'_, Self>> for CStr {
1229    #[inline]
1230    fn eq(&self, other: &Cow<'_, Self>) -> bool {
1231        *self == **other
1232    }
1233
1234    #[inline]
1235    fn ne(&self, other: &Cow<'_, Self>) -> bool {
1236        *self != **other
1237    }
1238}
1239
1240#[cfg(not(no_global_oom_handling))]
1241#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1242impl PartialEq<CStr> for Cow<'_, CStr> {
1243    #[inline]
1244    fn eq(&self, other: &CStr) -> bool {
1245        **self == *other
1246    }
1247
1248    #[inline]
1249    fn ne(&self, other: &CStr) -> bool {
1250        **self != *other
1251    }
1252}
1253
1254#[cfg(not(no_global_oom_handling))]
1255#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1256impl PartialEq<&CStr> for Cow<'_, CStr> {
1257    #[inline]
1258    fn eq(&self, other: &&CStr) -> bool {
1259        **self == **other
1260    }
1261
1262    #[inline]
1263    fn ne(&self, other: &&CStr) -> bool {
1264        **self != **other
1265    }
1266}
1267
1268#[cfg(not(no_global_oom_handling))]
1269#[stable(feature = "c_string_eq_c_str", since = "1.90.0")]
1270impl PartialEq<CString> for Cow<'_, CStr> {
1271    #[inline]
1272    fn eq(&self, other: &CString) -> bool {
1273        **self == **other
1274    }
1275
1276    #[inline]
1277    fn ne(&self, other: &CString) -> bool {
1278        **self != **other
1279    }
1280}
1281
1282#[stable(feature = "rust1", since = "1.0.0")]
1283impl core::error::Error for NulError {}
1284
1285#[stable(feature = "cstring_from_vec_with_nul", since = "1.58.0")]
1286impl core::error::Error for FromVecWithNulError {}
1287
1288#[stable(feature = "cstring_into", since = "1.7.0")]
1289impl core::error::Error for IntoStringError {
1290    fn source(&self) -> Option<&(dyn core::error::Error + 'static)> {
1291        Some(&self.error)
1292    }
1293}
````