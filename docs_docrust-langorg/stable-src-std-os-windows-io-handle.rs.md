---
title: handle.rs - source
url: https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#551-553
source: crawler
fetched_at: 2026-05-06T21:31:16.023936548-03:00
rendered_js: false
word_count: 3124
summary: This document defines types for safe Windows OS handle management, providing abstractions for owned and borrowed handles as well as specialized types for handling FFI sentry values like NULL and INVALID_HANDLE_VALUE.
tags:
    - rust
    - windows-api
    - io-safety
    - ffi
    - memory-safety
    - system-handles
category: api
---

## std/os/windows/io/ handle.rs

````rust
1//! Owned and borrowed OS handles.
2
3#![stable(feature = "io_safety", since = "1.63.0")]
4
5use super::raw::{AsRawHandle, FromRawHandle, IntoRawHandle, RawHandle};
6use crate::marker::PhantomData;
7use crate::mem::ManuallyDrop;
8use crate::sys::{AsInner, FromInner, IntoInner, cvt};
9use crate::{fmt, fs, io, ptr, sys};
10
11/// A borrowed handle.
12///
13/// This has a lifetime parameter to tie it to the lifetime of something that
14/// owns the handle.
15///
16/// This uses `repr(transparent)` and has the representation of a host handle,
17/// so it can be used in FFI in places where a handle is passed as an argument,
18/// it is not captured or consumed.
19///
20/// Note that it *may* have the value `-1`, which in `BorrowedHandle` always
21/// represents a valid handle value, such as [the current process handle], and
22/// not `INVALID_HANDLE_VALUE`, despite the two having the same value. See
23/// [here] for the full story.
24///
25/// And, it *may* have the value `NULL` (0), which can occur when consoles are
26/// detached from processes, or when `windows_subsystem` is used.
27///
28/// This type's `.to_owned()` implementation returns another `BorrowedHandle`
29/// rather than an `OwnedHandle`. It just makes a trivial copy of the raw
30/// handle, which is then borrowed under the same lifetime.
31///
32/// [here]: https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443
33/// [the current process handle]: https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess#remarks
34#[derive(Copy, Clone)]
35#[repr(transparent)]
36#[stable(feature = "io_safety", since = "1.63.0")]
37pub struct BorrowedHandle<'handle> {
38    handle: RawHandle,
39    _phantom: PhantomData<&'handle OwnedHandle>,
40}
41
42/// An owned handle.
43///
44/// This closes the handle on drop.
45///
46/// Note that it *may* have the value `-1`, which in `OwnedHandle` always
47/// represents a valid handle value, such as [the current process handle], and
48/// not `INVALID_HANDLE_VALUE`, despite the two having the same value. See
49/// [here] for the full story.
50///
51/// And, it *may* have the value `NULL` (0), which can occur when consoles are
52/// detached from processes, or when `windows_subsystem` is used.
53///
54/// `OwnedHandle` uses [`CloseHandle`] to close its handle on drop. As such,
55/// it must not be used with handles to open registry keys which need to be
56/// closed with [`RegCloseKey`] instead.
57///
58/// [`CloseHandle`]: https://docs.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle
59/// [`RegCloseKey`]: https://docs.microsoft.com/en-us/windows/win32/api/winreg/nf-winreg-regclosekey
60///
61/// [here]: https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443
62/// [the current process handle]: https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess#remarks
63#[repr(transparent)]
64#[stable(feature = "io_safety", since = "1.63.0")]
65pub struct OwnedHandle {
66    handle: RawHandle,
67}
68
69/// FFI type for handles in return values or out parameters, where `NULL` is used
70/// as a sentry value to indicate errors, such as in the return value of `CreateThread`. This uses
71/// `repr(transparent)` and has the representation of a host handle, so that it can be used in such
72/// FFI declarations.
73///
74/// The only thing you can usefully do with a `HandleOrNull` is to convert it into an
75/// `OwnedHandle` using its [`TryFrom`] implementation; this conversion takes care of the check for
76/// `NULL`. This ensures that such FFI calls cannot start using the handle without
77/// checking for `NULL` first.
78///
79/// This type may hold any handle value that [`OwnedHandle`] may hold. As with `OwnedHandle`, when
80/// it holds `-1`, that value is interpreted as a valid handle value, such as
81/// [the current process handle], and not `INVALID_HANDLE_VALUE`.
82///
83/// If this holds a non-null handle, it will close the handle on drop.
84///
85/// [the current process handle]: https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess#remarks
86#[repr(transparent)]
87#[stable(feature = "io_safety", since = "1.63.0")]
88#[derive(Debug)]
89pub struct HandleOrNull(RawHandle);
90
91/// FFI type for handles in return values or out parameters, where `INVALID_HANDLE_VALUE` is used
92/// as a sentry value to indicate errors, such as in the return value of `CreateFileW`. This uses
93/// `repr(transparent)` and has the representation of a host handle, so that it can be used in such
94/// FFI declarations.
95///
96/// The only thing you can usefully do with a `HandleOrInvalid` is to convert it into an
97/// `OwnedHandle` using its [`TryFrom`] implementation; this conversion takes care of the check for
98/// `INVALID_HANDLE_VALUE`. This ensures that such FFI calls cannot start using the handle without
99/// checking for `INVALID_HANDLE_VALUE` first.
100///
101/// This type may hold any handle value that [`OwnedHandle`] may hold, except that when it holds
102/// `-1`, that value is interpreted to mean `INVALID_HANDLE_VALUE`.
103///
104/// If holds a handle other than `INVALID_HANDLE_VALUE`, it will close the handle on drop.
105#[repr(transparent)]
106#[stable(feature = "io_safety", since = "1.63.0")]
107#[derive(Debug)]
108pub struct HandleOrInvalid(RawHandle);
109
110// The Windows [`HANDLE`] type may be transferred across and shared between
111// thread boundaries (despite containing a `*mut void`, which in general isn't
112// `Send` or `Sync`).
113//
114// [`HANDLE`]: std::os::windows::raw::HANDLE
115#[stable(feature = "io_safety", since = "1.63.0")]
116unsafe impl Send for OwnedHandle {}
117#[stable(feature = "io_safety", since = "1.63.0")]
118unsafe impl Send for HandleOrNull {}
119#[stable(feature = "io_safety", since = "1.63.0")]
120unsafe impl Send for HandleOrInvalid {}
121#[stable(feature = "io_safety", since = "1.63.0")]
122unsafe impl Send for BorrowedHandle<'_> {}
123#[stable(feature = "io_safety", since = "1.63.0")]
124unsafe impl Sync for OwnedHandle {}
125#[stable(feature = "io_safety", since = "1.63.0")]
126unsafe impl Sync for HandleOrNull {}
127#[stable(feature = "io_safety", since = "1.63.0")]
128unsafe impl Sync for HandleOrInvalid {}
129#[stable(feature = "io_safety", since = "1.63.0")]
130unsafe impl Sync for BorrowedHandle<'_> {}
131
132impl BorrowedHandle<'_> {
133    /// Returns a `BorrowedHandle` holding the given raw handle.
134    ///
135    /// # Safety
136    ///
137    /// The resource pointed to by `handle` must be a valid open handle, it
138    /// must remain open for the duration of the returned `BorrowedHandle`.
139    ///
140    /// Note that it *may* have the value `INVALID_HANDLE_VALUE` (-1), which is
141    /// sometimes a valid handle value. See [here] for the full story.
142    ///
143    /// And, it *may* have the value `NULL` (0), which can occur when consoles are
144    /// detached from processes, or when `windows_subsystem` is used.
145    ///
146    /// [here]: https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443
147    #[inline]
148    #[rustc_const_stable(feature = "io_safety", since = "1.63.0")]
149    #[stable(feature = "io_safety", since = "1.63.0")]
150    pub const unsafe fn borrow_raw(handle: RawHandle) -> Self {
151        Self { handle, _phantom: PhantomData }
152    }
153}
154
155#[stable(feature = "io_safety", since = "1.63.0")]
156impl TryFrom<HandleOrNull> for OwnedHandle {
157    type Error = NullHandleError;
158
159    #[inline]
160    fn try_from(handle_or_null: HandleOrNull) -> Result<Self, NullHandleError> {
161        let handle_or_null = ManuallyDrop::new(handle_or_null);
162        if handle_or_null.is_valid() {
163            // SAFETY: The handle is not null.
164            Ok(unsafe { OwnedHandle::from_raw_handle(handle_or_null.0) })
165        } else {
166            Err(NullHandleError(()))
167        }
168    }
169}
170
171#[stable(feature = "io_safety", since = "1.63.0")]
172impl Drop for HandleOrNull {
173    #[inline]
174    fn drop(&mut self) {
175        if self.is_valid() {
176            unsafe {
177                let _ = sys::c::CloseHandle(self.0);
178            }
179        }
180    }
181}
182
183impl OwnedHandle {
184    /// Creates a new `OwnedHandle` instance that shares the same underlying
185    /// object as the existing `OwnedHandle` instance.
186    #[stable(feature = "io_safety", since = "1.63.0")]
187    pub fn try_clone(&self) -> io::Result<Self> {
188        self.as_handle().try_clone_to_owned()
189    }
190}
191
192impl BorrowedHandle<'_> {
193    /// Creates a new `OwnedHandle` instance that shares the same underlying
194    /// object as the existing `BorrowedHandle` instance.
195    #[stable(feature = "io_safety", since = "1.63.0")]
196    pub fn try_clone_to_owned(&self) -> io::Result<OwnedHandle> {
197        self.duplicate(0, false, sys::c::DUPLICATE_SAME_ACCESS)
198    }
199
200    pub(crate) fn duplicate(
201        &self,
202        access: u32,
203        inherit: bool,
204        options: u32,
205    ) -> io::Result<OwnedHandle> {
206        let handle = self.as_raw_handle();
207
208        // `Stdin`, `Stdout`, and `Stderr` can all hold null handles, such as
209        // in a process with a detached console. `DuplicateHandle` would fail
210        // if we passed it a null handle, but we can treat null as a valid
211        // handle which doesn't do any I/O, and allow it to be duplicated.
212        if handle.is_null() {
213            return unsafe { Ok(OwnedHandle::from_raw_handle(handle)) };
214        }
215
216        let mut ret = ptr::null_mut();
217        cvt(unsafe {
218            let cur_proc = sys::c::GetCurrentProcess();
219            sys::c::DuplicateHandle(
220                cur_proc,
221                handle,
222                cur_proc,
223                &mut ret,
224                access,
225                inherit as sys::c::BOOL,
226                options,
227            )
228        })?;
229        unsafe { Ok(OwnedHandle::from_raw_handle(ret)) }
230    }
231}
232
233#[stable(feature = "io_safety", since = "1.63.0")]
234impl TryFrom<HandleOrInvalid> for OwnedHandle {
235    type Error = InvalidHandleError;
236
237    #[inline]
238    fn try_from(handle_or_invalid: HandleOrInvalid) -> Result<Self, InvalidHandleError> {
239        let handle_or_invalid = ManuallyDrop::new(handle_or_invalid);
240        if handle_or_invalid.is_valid() {
241            // SAFETY: The handle is not invalid.
242            Ok(unsafe { OwnedHandle::from_raw_handle(handle_or_invalid.0) })
243        } else {
244            Err(InvalidHandleError(()))
245        }
246    }
247}
248
249#[stable(feature = "io_safety", since = "1.63.0")]
250impl Drop for HandleOrInvalid {
251    #[inline]
252    fn drop(&mut self) {
253        if self.is_valid() {
254            unsafe {
255                let _ = sys::c::CloseHandle(self.0);
256            }
257        }
258    }
259}
260
261/// This is the error type used by [`HandleOrNull`] when attempting to convert
262/// into a handle, to indicate that the value is null.
263// The empty field prevents constructing this, and allows extending it in the future.
264#[stable(feature = "io_safety", since = "1.63.0")]
265#[derive(Debug, Clone, PartialEq, Eq)]
266pub struct NullHandleError(());
267
268#[stable(feature = "io_safety", since = "1.63.0")]
269impl fmt::Display for NullHandleError {
270    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
271        "A HandleOrNull could not be converted to a handle because it was null".fmt(fmt)
272    }
273}
274
275#[stable(feature = "io_safety", since = "1.63.0")]
276impl crate::error::Error for NullHandleError {}
277
278/// This is the error type used by [`HandleOrInvalid`] when attempting to
279/// convert into a handle, to indicate that the value is
280/// `INVALID_HANDLE_VALUE`.
281// The empty field prevents constructing this, and allows extending it in the future.
282#[stable(feature = "io_safety", since = "1.63.0")]
283#[derive(Debug, Clone, PartialEq, Eq)]
284pub struct InvalidHandleError(());
285
286#[stable(feature = "io_safety", since = "1.63.0")]
287impl fmt::Display for InvalidHandleError {
288    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
289        "A HandleOrInvalid could not be converted to a handle because it was INVALID_HANDLE_VALUE"
290            .fmt(fmt)
291    }
292}
293
294#[stable(feature = "io_safety", since = "1.63.0")]
295impl crate::error::Error for InvalidHandleError {}
296
297#[stable(feature = "io_safety", since = "1.63.0")]
298impl AsRawHandle for BorrowedHandle<'_> {
299    #[inline]
300    fn as_raw_handle(&self) -> RawHandle {
301        self.handle
302    }
303}
304
305#[stable(feature = "io_safety", since = "1.63.0")]
306impl AsRawHandle for OwnedHandle {
307    #[inline]
308    fn as_raw_handle(&self) -> RawHandle {
309        self.handle
310    }
311}
312
313#[stable(feature = "io_safety", since = "1.63.0")]
314impl IntoRawHandle for OwnedHandle {
315    #[inline]
316    fn into_raw_handle(self) -> RawHandle {
317        ManuallyDrop::new(self).handle
318    }
319}
320
321#[stable(feature = "io_safety", since = "1.63.0")]
322impl FromRawHandle for OwnedHandle {
323    #[inline]
324    unsafe fn from_raw_handle(handle: RawHandle) -> Self {
325        Self { handle }
326    }
327}
328
329impl HandleOrNull {
330    /// Constructs a new instance of `Self` from the given `RawHandle` returned
331    /// from a Windows API that uses null to indicate failure, such as
332    /// `CreateThread`.
333    ///
334    /// Use `HandleOrInvalid` instead of `HandleOrNull` for APIs that
335    /// use `INVALID_HANDLE_VALUE` to indicate failure.
336    ///
337    /// # Safety
338    ///
339    /// The passed `handle` value must either satisfy the safety requirements
340    /// of [`FromRawHandle::from_raw_handle`], or be null. Note that not all
341    /// Windows APIs use null for errors; see [here] for the full story.
342    ///
343    /// [here]: https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443
344    #[stable(feature = "io_safety", since = "1.63.0")]
345    #[inline]
346    pub unsafe fn from_raw_handle(handle: RawHandle) -> Self {
347        Self(handle)
348    }
349
350    fn is_valid(&self) -> bool {
351        !self.0.is_null()
352    }
353}
354
355impl HandleOrInvalid {
356    /// Constructs a new instance of `Self` from the given `RawHandle` returned
357    /// from a Windows API that uses `INVALID_HANDLE_VALUE` to indicate
358    /// failure, such as `CreateFileW`.
359    ///
360    /// Use `HandleOrNull` instead of `HandleOrInvalid` for APIs that
361    /// use null to indicate failure.
362    ///
363    /// # Safety
364    ///
365    /// The passed `handle` value must either satisfy the safety requirements
366    /// of [`FromRawHandle::from_raw_handle`], or be
367    /// `INVALID_HANDLE_VALUE` (-1). Note that not all Windows APIs use
368    /// `INVALID_HANDLE_VALUE` for errors; see [here] for the full story.
369    ///
370    /// [here]: https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443
371    #[stable(feature = "io_safety", since = "1.63.0")]
372    #[inline]
373    pub unsafe fn from_raw_handle(handle: RawHandle) -> Self {
374        Self(handle)
375    }
376
377    fn is_valid(&self) -> bool {
378        self.0 != sys::c::INVALID_HANDLE_VALUE
379    }
380}
381
382#[stable(feature = "io_safety", since = "1.63.0")]
383impl Drop for OwnedHandle {
384    #[inline]
385    fn drop(&mut self) {
386        unsafe {
387            let _ = sys::c::CloseHandle(self.handle);
388        }
389    }
390}
391
392#[stable(feature = "io_safety", since = "1.63.0")]
393impl fmt::Debug for BorrowedHandle<'_> {
394    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
395        f.debug_struct("BorrowedHandle").field("handle", &self.handle).finish()
396    }
397}
398
399#[stable(feature = "io_safety", since = "1.63.0")]
400impl fmt::Debug for OwnedHandle {
401    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
402        f.debug_struct("OwnedHandle").field("handle", &self.handle).finish()
403    }
404}
405
406macro_rules! impl_is_terminal {
407    ($($t:ty),*$(,)?) => {$(
408        #[unstable(feature = "sealed", issue = "none")]
409        impl crate::sealed::Sealed for $t {}
410
411        #[stable(feature = "is_terminal", since = "1.70.0")]
412        impl io::IsTerminal for $t {
413            #[inline]
414            fn is_terminal(&self) -> bool {
415                crate::sys::io::is_terminal(self)
416            }
417        }
418    )*}
419}
420
421impl_is_terminal!(BorrowedHandle<'_>, OwnedHandle);
422
423/// A trait to borrow the handle from an underlying object.
424#[stable(feature = "io_safety", since = "1.63.0")]
425pub trait AsHandle {
426    /// Borrows the handle.
427    ///
428    /// # Example
429    ///
430    /// ```rust,no_run
431    /// use std::fs::File;
432    /// # use std::io;
433    /// use std::os::windows::io::{AsHandle, BorrowedHandle};
434    ///
435    /// let mut f = File::open("foo.txt")?;
436    /// let borrowed_handle: BorrowedHandle<'_> = f.as_handle();
437    /// # Ok::<(), io::Error>(())
438    /// ```
439    #[stable(feature = "io_safety", since = "1.63.0")]
440    fn as_handle(&self) -> BorrowedHandle<'_>;
441}
442
443#[stable(feature = "io_safety", since = "1.63.0")]
444impl<T: AsHandle + ?Sized> AsHandle for &T {
445    #[inline]
446    fn as_handle(&self) -> BorrowedHandle<'_> {
447        T::as_handle(self)
448    }
449}
450
451#[stable(feature = "io_safety", since = "1.63.0")]
452impl<T: AsHandle + ?Sized> AsHandle for &mut T {
453    #[inline]
454    fn as_handle(&self) -> BorrowedHandle<'_> {
455        T::as_handle(self)
456    }
457}
458
459#[stable(feature = "as_windows_ptrs", since = "1.71.0")]
460/// This impl allows implementing traits that require `AsHandle` on Arc.
461/// ```
462/// # #[cfg(windows)] mod group_cfg {
463/// # use std::os::windows::io::AsHandle;
464/// use std::fs::File;
465/// use std::sync::Arc;
466///
467/// trait MyTrait: AsHandle {}
468/// impl MyTrait for Arc<File> {}
469/// impl MyTrait for Box<File> {}
470/// # }
471/// ```
472impl<T: AsHandle + ?Sized> AsHandle for crate::sync::Arc<T> {
473    #[inline]
474    fn as_handle(&self) -> BorrowedHandle<'_> {
475        (**self).as_handle()
476    }
477}
478
479#[stable(feature = "as_windows_ptrs", since = "1.71.0")]
480impl<T: AsHandle + ?Sized> AsHandle for crate::rc::Rc<T> {
481    #[inline]
482    fn as_handle(&self) -> BorrowedHandle<'_> {
483        (**self).as_handle()
484    }
485}
486
487#[unstable(feature = "unique_rc_arc", issue = "112566")]
488impl<T: AsHandle + ?Sized> AsHandle for crate::rc::UniqueRc<T> {
489    #[inline]
490    fn as_handle(&self) -> BorrowedHandle<'_> {
491        (**self).as_handle()
492    }
493}
494
495#[stable(feature = "as_windows_ptrs", since = "1.71.0")]
496impl<T: AsHandle + ?Sized> AsHandle for Box<T> {
497    #[inline]
498    fn as_handle(&self) -> BorrowedHandle<'_> {
499        (**self).as_handle()
500    }
501}
502
503#[stable(feature = "io_safety", since = "1.63.0")]
504impl AsHandle for BorrowedHandle<'_> {
505    #[inline]
506    fn as_handle(&self) -> BorrowedHandle<'_> {
507        *self
508    }
509}
510
511#[stable(feature = "io_safety", since = "1.63.0")]
512impl AsHandle for OwnedHandle {
513    #[inline]
514    fn as_handle(&self) -> BorrowedHandle<'_> {
515        // Safety: `OwnedHandle` and `BorrowedHandle` have the same validity
516        // invariants, and the `BorrowedHandle` is bounded by the lifetime
517        // of `&self`.
518        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
519    }
520}
521
522#[stable(feature = "io_safety", since = "1.63.0")]
523impl AsHandle for fs::File {
524    #[inline]
525    fn as_handle(&self) -> BorrowedHandle<'_> {
526        self.as_inner().as_handle()
527    }
528}
529
530#[stable(feature = "io_safety", since = "1.63.0")]
531impl From<fs::File> for OwnedHandle {
532    /// Takes ownership of a [`File`](fs::File)'s underlying file handle.
533    #[inline]
534    fn from(file: fs::File) -> OwnedHandle {
535        file.into_inner().into_inner().into_inner()
536    }
537}
538
539#[stable(feature = "io_safety", since = "1.63.0")]
540impl From<OwnedHandle> for fs::File {
541    /// Returns a [`File`](fs::File) that takes ownership of the given handle.
542    #[inline]
543    fn from(owned: OwnedHandle) -> Self {
544        Self::from_inner(FromInner::from_inner(FromInner::from_inner(owned)))
545    }
546}
547
548#[stable(feature = "io_safety", since = "1.63.0")]
549impl AsHandle for io::Stdin {
550    #[inline]
551    fn as_handle(&self) -> BorrowedHandle<'_> {
552        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
553    }
554}
555
556#[stable(feature = "io_safety", since = "1.63.0")]
557impl<'a> AsHandle for io::StdinLock<'a> {
558    #[inline]
559    fn as_handle(&self) -> BorrowedHandle<'_> {
560        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
561    }
562}
563
564#[stable(feature = "io_safety", since = "1.63.0")]
565impl AsHandle for io::Stdout {
566    #[inline]
567    fn as_handle(&self) -> BorrowedHandle<'_> {
568        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
569    }
570}
571
572#[stable(feature = "io_safety", since = "1.63.0")]
573impl<'a> AsHandle for io::StdoutLock<'a> {
574    #[inline]
575    fn as_handle(&self) -> BorrowedHandle<'_> {
576        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
577    }
578}
579
580#[stable(feature = "io_safety", since = "1.63.0")]
581impl AsHandle for io::Stderr {
582    #[inline]
583    fn as_handle(&self) -> BorrowedHandle<'_> {
584        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
585    }
586}
587
588#[stable(feature = "io_safety", since = "1.63.0")]
589impl<'a> AsHandle for io::StderrLock<'a> {
590    #[inline]
591    fn as_handle(&self) -> BorrowedHandle<'_> {
592        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
593    }
594}
595
596#[stable(feature = "io_safety", since = "1.63.0")]
597impl AsHandle for crate::process::ChildStdin {
598    #[inline]
599    fn as_handle(&self) -> BorrowedHandle<'_> {
600        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
601    }
602}
603
604#[stable(feature = "io_safety", since = "1.63.0")]
605impl From<crate::process::ChildStdin> for OwnedHandle {
606    /// Takes ownership of a [`ChildStdin`](crate::process::ChildStdin)'s file handle.
607    #[inline]
608    fn from(child_stdin: crate::process::ChildStdin) -> OwnedHandle {
609        unsafe { OwnedHandle::from_raw_handle(child_stdin.into_raw_handle()) }
610    }
611}
612
613#[stable(feature = "io_safety", since = "1.63.0")]
614impl AsHandle for crate::process::ChildStdout {
615    #[inline]
616    fn as_handle(&self) -> BorrowedHandle<'_> {
617        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
618    }
619}
620
621#[stable(feature = "io_safety", since = "1.63.0")]
622impl From<crate::process::ChildStdout> for OwnedHandle {
623    /// Takes ownership of a [`ChildStdout`](crate::process::ChildStdout)'s file handle.
624    #[inline]
625    fn from(child_stdout: crate::process::ChildStdout) -> OwnedHandle {
626        unsafe { OwnedHandle::from_raw_handle(child_stdout.into_raw_handle()) }
627    }
628}
629
630#[stable(feature = "io_safety", since = "1.63.0")]
631impl AsHandle for crate::process::ChildStderr {
632    #[inline]
633    fn as_handle(&self) -> BorrowedHandle<'_> {
634        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
635    }
636}
637
638#[stable(feature = "io_safety", since = "1.63.0")]
639impl From<crate::process::ChildStderr> for OwnedHandle {
640    /// Takes ownership of a [`ChildStderr`](crate::process::ChildStderr)'s file handle.
641    #[inline]
642    fn from(child_stderr: crate::process::ChildStderr) -> OwnedHandle {
643        unsafe { OwnedHandle::from_raw_handle(child_stderr.into_raw_handle()) }
644    }
645}
646
647#[stable(feature = "io_safety", since = "1.63.0")]
648impl<T> AsHandle for crate::thread::JoinHandle<T> {
649    #[inline]
650    fn as_handle(&self) -> BorrowedHandle<'_> {
651        unsafe { BorrowedHandle::borrow_raw(self.as_raw_handle()) }
652    }
653}
654
655#[stable(feature = "io_safety", since = "1.63.0")]
656impl<T> From<crate::thread::JoinHandle<T>> for OwnedHandle {
657    #[inline]
658    fn from(join_handle: crate::thread::JoinHandle<T>) -> OwnedHandle {
659        join_handle.into_inner().into_handle().into_inner()
660    }
661}
662
663#[stable(feature = "anonymous_pipe", since = "1.87.0")]
664impl AsHandle for io::PipeReader {
665    fn as_handle(&self) -> BorrowedHandle<'_> {
666        self.0.as_handle()
667    }
668}
669
670#[stable(feature = "anonymous_pipe", since = "1.87.0")]
671impl From<io::PipeReader> for OwnedHandle {
672    fn from(pipe: io::PipeReader) -> Self {
673        pipe.into_inner().into_inner()
674    }
675}
676
677#[stable(feature = "anonymous_pipe", since = "1.87.0")]
678impl AsHandle for io::PipeWriter {
679    fn as_handle(&self) -> BorrowedHandle<'_> {
680        self.0.as_handle()
681    }
682}
683
684#[stable(feature = "anonymous_pipe", since = "1.87.0")]
685impl From<io::PipeWriter> for OwnedHandle {
686    fn from(pipe: io::PipeWriter) -> Self {
687        pipe.into_inner().into_inner()
688    }
689}
690
691#[stable(feature = "anonymous_pipe", since = "1.87.0")]
692impl From<OwnedHandle> for io::PipeReader {
693    fn from(owned_handle: OwnedHandle) -> Self {
694        Self::from_inner(FromInner::from_inner(owned_handle))
695    }
696}
697
698#[stable(feature = "anonymous_pipe", since = "1.87.0")]
699impl From<OwnedHandle> for io::PipeWriter {
700    fn from(owned_handle: OwnedHandle) -> Self {
701        Self::from_inner(FromInner::from_inner(owned_handle))
702    }
703}
````