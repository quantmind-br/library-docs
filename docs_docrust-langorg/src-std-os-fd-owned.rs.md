---
title: owned.rs - source
url: https://doc.rust-lang.org/src/std/os/fd/owned.rs.html#484-489
source: crawler
fetched_at: 2026-05-06T21:24:20.244319649-03:00
rendered_js: false
word_count: 2436
summary: This document defines the BorrowedFd and OwnedFd types, which provide a safe, RAII-based abstraction for managing Unix-like file descriptors in Rust.
tags:
    - rust
    - io-safety
    - file-descriptor
    - unix
    - ffi
    - memory-management
category: reference
---

## std/os/fd/ owned.rs

````rust
1//! Owned and borrowed Unix-like file descriptors.
2
3#![stable(feature = "io_safety", since = "1.63.0")]
4#![deny(unsafe_op_in_unsafe_fn)]
5
6#[cfg(target_os = "motor")]
7use moto_rt::libc;
8
9use super::raw::{AsRawFd, FromRawFd, IntoRawFd, RawFd};
10#[cfg(not(target_os = "trusty"))]
11use crate::fs;
12use crate::marker::PhantomData;
13use crate::mem::ManuallyDrop;
14#[cfg(not(any(
15    target_arch = "wasm32",
16    target_env = "sgx",
17    target_os = "hermit",
18    target_os = "trusty",
19    target_os = "motor"
20)))]
21use crate::sys::cvt;
22#[cfg(not(target_os = "trusty"))]
23use crate::sys::{AsInner, FromInner, IntoInner};
24use crate::{fmt, io};
25
26type ValidRawFd = core::num::niche_types::NotAllOnes<RawFd>;
27
28/// A borrowed file descriptor.
29///
30/// This has a lifetime parameter to tie it to the lifetime of something that owns the file
31/// descriptor. For the duration of that lifetime, it is guaranteed that nobody will close the file
32/// descriptor.
33///
34/// This uses `repr(transparent)` and has the representation of a host file
35/// descriptor, so it can be used in FFI in places where a file descriptor is
36/// passed as an argument, it is not captured or consumed, and it never has the
37/// value `-1`.
38///
39/// This type does not have a [`ToOwned`][crate::borrow::ToOwned]
40/// implementation. Calling `.to_owned()` on a variable of this type will call
41/// it on `&BorrowedFd` and use `Clone::clone()` like `ToOwned` does for all
42/// types implementing `Clone`. The result will be descriptor borrowed under
43/// the same lifetime.
44///
45/// To obtain an [`OwnedFd`], you can use [`BorrowedFd::try_clone_to_owned`]
46/// instead, but this is not supported on all platforms.
47#[derive(Copy, Clone)]
48#[repr(transparent)]
49#[rustc_nonnull_optimization_guaranteed]
50#[stable(feature = "io_safety", since = "1.63.0")]
51pub struct BorrowedFd<'fd> {
52    fd: ValidRawFd,
53    _phantom: PhantomData<&'fd OwnedFd>,
54}
55
56/// An owned file descriptor.
57///
58/// This closes the file descriptor on drop. It is guaranteed that nobody else will close the file
59/// descriptor.
60///
61/// This uses `repr(transparent)` and has the representation of a host file
62/// descriptor, so it can be used in FFI in places where a file descriptor is
63/// passed as a consumed argument or returned as an owned value, and it never
64/// has the value `-1`.
65///
66/// You can use [`AsFd::as_fd`] to obtain a [`BorrowedFd`].
67#[repr(transparent)]
68#[rustc_nonnull_optimization_guaranteed]
69#[stable(feature = "io_safety", since = "1.63.0")]
70pub struct OwnedFd {
71    fd: ValidRawFd,
72}
73
74impl BorrowedFd<'_> {
75    /// Returns a `BorrowedFd` holding the given raw file descriptor.
76    ///
77    /// # Safety
78    ///
79    /// The resource pointed to by `fd` must remain open for the duration of
80    /// the returned `BorrowedFd`.
81    ///
82    /// # Panics
83    ///
84    /// Panics if the raw file descriptor has the value `-1`.
85    #[inline]
86    #[track_caller]
87    #[rustc_const_stable(feature = "io_safety", since = "1.63.0")]
88    #[stable(feature = "io_safety", since = "1.63.0")]
89    pub const unsafe fn borrow_raw(fd: RawFd) -> Self {
90        Self { fd: ValidRawFd::new(fd).expect("fd != -1"), _phantom: PhantomData }
91    }
92}
93
94impl OwnedFd {
95    /// Creates a new `OwnedFd` instance that shares the same underlying file
96    /// description as the existing `OwnedFd` instance.
97    #[stable(feature = "io_safety", since = "1.63.0")]
98    pub fn try_clone(&self) -> io::Result<Self> {
99        self.as_fd().try_clone_to_owned()
100    }
101}
102
103impl BorrowedFd<'_> {
104    /// Creates a new `OwnedFd` instance that shares the same underlying file
105    /// description as the existing `BorrowedFd` instance.
106    #[cfg(not(any(
107        target_arch = "wasm32",
108        target_os = "hermit",
109        target_os = "trusty",
110        target_os = "motor"
111    )))]
112    #[stable(feature = "io_safety", since = "1.63.0")]
113    pub fn try_clone_to_owned(&self) -> io::Result<OwnedFd> {
114        // We want to atomically duplicate this file descriptor and set the
115        // CLOEXEC flag, and currently that's done via F_DUPFD_CLOEXEC. This
116        // is a POSIX flag that was added to Linux in 2.6.24.
117        #[cfg(not(any(target_os = "espidf", target_os = "vita")))]
118        let cmd = libc::F_DUPFD_CLOEXEC;
119
120        // For ESP-IDF, F_DUPFD is used instead, because the CLOEXEC semantics
121        // will never be supported, as this is a bare metal framework with
122        // no capabilities for multi-process execution. While F_DUPFD is also
123        // not supported yet, it might be (currently it returns ENOSYS).
124        #[cfg(any(target_os = "espidf", target_os = "vita"))]
125        let cmd = libc::F_DUPFD;
126
127        // Avoid using file descriptors below 3 as they are used for stdio
128        let fd = cvt(unsafe { libc::fcntl(self.as_raw_fd(), cmd, 3) })?;
129        Ok(unsafe { OwnedFd::from_raw_fd(fd) })
130    }
131
132    /// Creates a new `OwnedFd` instance that shares the same underlying file
133    /// description as the existing `BorrowedFd` instance.
134    #[cfg(any(target_arch = "wasm32", target_os = "hermit", target_os = "trusty"))]
135    #[stable(feature = "io_safety", since = "1.63.0")]
136    pub fn try_clone_to_owned(&self) -> io::Result<OwnedFd> {
137        Err(io::Error::UNSUPPORTED_PLATFORM)
138    }
139
140    /// Creates a new `OwnedFd` instance that shares the same underlying file
141    /// description as the existing `BorrowedFd` instance.
142    #[cfg(target_os = "motor")]
143    #[stable(feature = "io_safety", since = "1.63.0")]
144    pub fn try_clone_to_owned(&self) -> io::Result<OwnedFd> {
145        let fd = moto_rt::fs::duplicate(self.as_raw_fd()).map_err(crate::sys::map_motor_error)?;
146        Ok(unsafe { OwnedFd::from_raw_fd(fd) })
147    }
148}
149
150#[stable(feature = "io_safety", since = "1.63.0")]
151impl AsRawFd for BorrowedFd<'_> {
152    #[inline]
153    fn as_raw_fd(&self) -> RawFd {
154        self.fd.as_inner()
155    }
156}
157
158#[stable(feature = "io_safety", since = "1.63.0")]
159impl AsRawFd for OwnedFd {
160    #[inline]
161    fn as_raw_fd(&self) -> RawFd {
162        self.fd.as_inner()
163    }
164}
165
166#[stable(feature = "io_safety", since = "1.63.0")]
167impl IntoRawFd for OwnedFd {
168    #[inline]
169    fn into_raw_fd(self) -> RawFd {
170        ManuallyDrop::new(self).fd.as_inner()
171    }
172}
173
174#[stable(feature = "io_safety", since = "1.63.0")]
175impl FromRawFd for OwnedFd {
176    /// Constructs a new instance of `Self` from the given raw file descriptor.
177    ///
178    /// # Safety
179    ///
180    /// The resource pointed to by `fd` must be open and suitable for assuming
181    /// [ownership][io-safety]. The resource must not require any cleanup other than `close`.
182    ///
183    /// [io-safety]: io#io-safety
184    ///
185    /// # Panics
186    ///
187    /// Panics if the raw file descriptor has the value `-1`.
188    #[inline]
189    #[track_caller]
190    unsafe fn from_raw_fd(fd: RawFd) -> Self {
191        Self { fd: ValidRawFd::new(fd).expect("fd != -1") }
192    }
193}
194
195#[stable(feature = "io_safety", since = "1.63.0")]
196impl Drop for OwnedFd {
197    #[inline]
198    fn drop(&mut self) {
199        unsafe {
200            // Note that errors are ignored when closing a file descriptor. According to POSIX 2024,
201            // we can and indeed should retry `close` on `EINTR`
202            // (https://pubs.opengroup.org/onlinepubs/9799919799.2024edition/functions/close.html),
203            // but it is not clear yet how well widely-used implementations are conforming with this
204            // mandate since older versions of POSIX left the state of the FD after an `EINTR`
205            // unspecified. Ignoring errors is "fine" because some of the major Unices (in
206            // particular, Linux) do make sure to always close the FD, even when `close()` is
207            // interrupted, and the scenario is rare to begin with. If we retried on a
208            // not-POSIX-compliant implementation, the consequences could be really bad since we may
209            // close the wrong FD. Helpful link to an epic discussion by POSIX workgroup that led to
210            // the latest POSIX wording: http://austingroupbugs.net/view.php?id=529
211            #[cfg(not(target_os = "hermit"))]
212            {
213                #[cfg(unix)]
214                crate::sys::fs::debug_assert_fd_is_open(self.fd.as_inner());
215
216                let _ = libc::close(self.fd.as_inner());
217            }
218            #[cfg(target_os = "hermit")]
219            let _ = hermit_abi::close(self.fd.as_inner());
220        }
221    }
222}
223
224#[stable(feature = "io_safety", since = "1.63.0")]
225impl fmt::Debug for BorrowedFd<'_> {
226    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
227        f.debug_struct("BorrowedFd").field("fd", &self.fd).finish()
228    }
229}
230
231#[stable(feature = "io_safety", since = "1.63.0")]
232impl fmt::Debug for OwnedFd {
233    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
234        f.debug_struct("OwnedFd").field("fd", &self.fd).finish()
235    }
236}
237
238macro_rules! impl_is_terminal {
239    ($($t:ty),*$(,)?) => {$(
240        #[unstable(feature = "sealed", issue = "none")]
241        impl crate::sealed::Sealed for $t {}
242
243        #[stable(feature = "is_terminal", since = "1.70.0")]
244        impl io::IsTerminal for $t {
245            #[inline]
246            fn is_terminal(&self) -> bool {
247                crate::sys::io::is_terminal(self)
248            }
249        }
250    )*}
251}
252
253impl_is_terminal!(BorrowedFd<'_>, OwnedFd);
254
255/// A trait to borrow the file descriptor from an underlying object.
256///
257/// This is only available on unix platforms and must be imported in order to
258/// call the method. Windows platforms have a corresponding `AsHandle` and
259/// `AsSocket` set of traits.
260#[stable(feature = "io_safety", since = "1.63.0")]
261pub trait AsFd {
262    /// Borrows the file descriptor.
263    ///
264    /// # Example
265    ///
266    /// ```rust,no_run
267    /// use std::fs::File;
268    /// # use std::io;
269    /// # #[cfg(any(unix, target_os = "wasi"))]
270    /// # use std::os::fd::{AsFd, BorrowedFd};
271    ///
272    /// let mut f = File::open("foo.txt")?;
273    /// # #[cfg(any(unix, target_os = "wasi"))]
274    /// let borrowed_fd: BorrowedFd<'_> = f.as_fd();
275    /// # Ok::<(), io::Error>(())
276    /// ```
277    #[stable(feature = "io_safety", since = "1.63.0")]
278    fn as_fd(&self) -> BorrowedFd<'_>;
279}
280
281#[stable(feature = "io_safety", since = "1.63.0")]
282impl<T: AsFd + ?Sized> AsFd for &T {
283    #[inline]
284    fn as_fd(&self) -> BorrowedFd<'_> {
285        T::as_fd(self)
286    }
287}
288
289#[stable(feature = "io_safety", since = "1.63.0")]
290impl<T: AsFd + ?Sized> AsFd for &mut T {
291    #[inline]
292    fn as_fd(&self) -> BorrowedFd<'_> {
293        T::as_fd(self)
294    }
295}
296
297#[stable(feature = "io_safety", since = "1.63.0")]
298impl AsFd for BorrowedFd<'_> {
299    #[inline]
300    fn as_fd(&self) -> BorrowedFd<'_> {
301        *self
302    }
303}
304
305#[stable(feature = "io_safety", since = "1.63.0")]
306impl AsFd for OwnedFd {
307    #[inline]
308    fn as_fd(&self) -> BorrowedFd<'_> {
309        // Safety: `OwnedFd` and `BorrowedFd` have the same validity
310        // invariants, and the `BorrowedFd` is bounded by the lifetime
311        // of `&self`.
312        unsafe { BorrowedFd::borrow_raw(self.as_raw_fd()) }
313    }
314}
315
316#[stable(feature = "io_safety", since = "1.63.0")]
317#[cfg(not(target_os = "trusty"))]
318impl AsFd for fs::File {
319    #[inline]
320    fn as_fd(&self) -> BorrowedFd<'_> {
321        self.as_inner().as_fd()
322    }
323}
324
325#[stable(feature = "io_safety", since = "1.63.0")]
326#[cfg(not(target_os = "trusty"))]
327impl From<fs::File> for OwnedFd {
328    /// Takes ownership of a [`File`](fs::File)'s underlying file descriptor.
329    #[inline]
330    fn from(file: fs::File) -> OwnedFd {
331        file.into_inner().into_inner().into_inner()
332    }
333}
334
335#[stable(feature = "io_safety", since = "1.63.0")]
336#[cfg(not(target_os = "trusty"))]
337impl From<OwnedFd> for fs::File {
338    /// Returns a [`File`](fs::File) that takes ownership of the given
339    /// file descriptor.
340    #[inline]
341    fn from(owned_fd: OwnedFd) -> Self {
342        Self::from_inner(FromInner::from_inner(FromInner::from_inner(owned_fd)))
343    }
344}
345
346#[stable(feature = "io_safety", since = "1.63.0")]
347#[cfg(not(target_os = "trusty"))]
348impl AsFd for crate::net::TcpStream {
349    #[inline]
350    fn as_fd(&self) -> BorrowedFd<'_> {
351        self.as_inner().socket().as_fd()
352    }
353}
354
355#[stable(feature = "io_safety", since = "1.63.0")]
356#[cfg(not(target_os = "trusty"))]
357impl From<crate::net::TcpStream> for OwnedFd {
358    /// Takes ownership of a [`TcpStream`](crate::net::TcpStream)'s socket file descriptor.
359    #[inline]
360    fn from(tcp_stream: crate::net::TcpStream) -> OwnedFd {
361        tcp_stream.into_inner().into_socket().into_inner().into_inner().into()
362    }
363}
364
365#[stable(feature = "io_safety", since = "1.63.0")]
366#[cfg(not(target_os = "trusty"))]
367impl From<OwnedFd> for crate::net::TcpStream {
368    #[inline]
369    fn from(owned_fd: OwnedFd) -> Self {
370        Self::from_inner(FromInner::from_inner(FromInner::from_inner(FromInner::from_inner(
371            owned_fd,
372        ))))
373    }
374}
375
376#[stable(feature = "io_safety", since = "1.63.0")]
377#[cfg(not(target_os = "trusty"))]
378impl AsFd for crate::net::TcpListener {
379    #[inline]
380    fn as_fd(&self) -> BorrowedFd<'_> {
381        self.as_inner().socket().as_fd()
382    }
383}
384
385#[stable(feature = "io_safety", since = "1.63.0")]
386#[cfg(not(target_os = "trusty"))]
387impl From<crate::net::TcpListener> for OwnedFd {
388    /// Takes ownership of a [`TcpListener`](crate::net::TcpListener)'s socket file descriptor.
389    #[inline]
390    fn from(tcp_listener: crate::net::TcpListener) -> OwnedFd {
391        tcp_listener.into_inner().into_socket().into_inner().into_inner().into()
392    }
393}
394
395#[stable(feature = "io_safety", since = "1.63.0")]
396#[cfg(not(target_os = "trusty"))]
397impl From<OwnedFd> for crate::net::TcpListener {
398    #[inline]
399    fn from(owned_fd: OwnedFd) -> Self {
400        Self::from_inner(FromInner::from_inner(FromInner::from_inner(FromInner::from_inner(
401            owned_fd,
402        ))))
403    }
404}
405
406#[stable(feature = "io_safety", since = "1.63.0")]
407#[cfg(not(target_os = "trusty"))]
408impl AsFd for crate::net::UdpSocket {
409    #[inline]
410    fn as_fd(&self) -> BorrowedFd<'_> {
411        self.as_inner().socket().as_fd()
412    }
413}
414
415#[stable(feature = "io_safety", since = "1.63.0")]
416#[cfg(not(target_os = "trusty"))]
417impl From<crate::net::UdpSocket> for OwnedFd {
418    /// Takes ownership of a [`UdpSocket`](crate::net::UdpSocket)'s file descriptor.
419    #[inline]
420    fn from(udp_socket: crate::net::UdpSocket) -> OwnedFd {
421        udp_socket.into_inner().into_socket().into_inner().into_inner().into()
422    }
423}
424
425#[stable(feature = "io_safety", since = "1.63.0")]
426#[cfg(not(target_os = "trusty"))]
427impl From<OwnedFd> for crate::net::UdpSocket {
428    #[inline]
429    fn from(owned_fd: OwnedFd) -> Self {
430        Self::from_inner(FromInner::from_inner(FromInner::from_inner(FromInner::from_inner(
431            owned_fd,
432        ))))
433    }
434}
435
436#[stable(feature = "asfd_ptrs", since = "1.64.0")]
437/// This impl allows implementing traits that require `AsFd` on Arc.
438/// ```
439/// # #[cfg(any(unix, target_os = "wasi"))] mod group_cfg {
440/// # #[cfg(target_os = "wasi")]
441/// # use std::os::wasi::io::AsFd;
442/// # #[cfg(unix)]
443/// # use std::os::unix::io::AsFd;
444/// use std::net::UdpSocket;
445/// use std::sync::Arc;
446///
447/// trait MyTrait: AsFd {}
448/// impl MyTrait for Arc<UdpSocket> {}
449/// impl MyTrait for Box<UdpSocket> {}
450/// # }
451/// ```
452impl<T: AsFd + ?Sized> AsFd for crate::sync::Arc<T> {
453    #[inline]
454    fn as_fd(&self) -> BorrowedFd<'_> {
455        (**self).as_fd()
456    }
457}
458
459#[stable(feature = "asfd_rc", since = "1.69.0")]
460impl<T: AsFd + ?Sized> AsFd for crate::rc::Rc<T> {
461    #[inline]
462    fn as_fd(&self) -> BorrowedFd<'_> {
463        (**self).as_fd()
464    }
465}
466
467#[unstable(feature = "unique_rc_arc", issue = "112566")]
468impl<T: AsFd + ?Sized> AsFd for crate::rc::UniqueRc<T> {
469    #[inline]
470    fn as_fd(&self) -> BorrowedFd<'_> {
471        (**self).as_fd()
472    }
473}
474
475#[stable(feature = "asfd_ptrs", since = "1.64.0")]
476impl<T: AsFd + ?Sized> AsFd for Box<T> {
477    #[inline]
478    fn as_fd(&self) -> BorrowedFd<'_> {
479        (**self).as_fd()
480    }
481}
482
483#[stable(feature = "io_safety", since = "1.63.0")]
484impl AsFd for io::Stdin {
485    #[inline]
486    fn as_fd(&self) -> BorrowedFd<'_> {
487        unsafe { BorrowedFd::borrow_raw(0) }
488    }
489}
490
491#[stable(feature = "io_safety", since = "1.63.0")]
492impl<'a> AsFd for io::StdinLock<'a> {
493    #[inline]
494    fn as_fd(&self) -> BorrowedFd<'_> {
495        // SAFETY: user code should not close stdin out from under the standard library
496        unsafe { BorrowedFd::borrow_raw(0) }
497    }
498}
499
500#[stable(feature = "io_safety", since = "1.63.0")]
501impl AsFd for io::Stdout {
502    #[inline]
503    fn as_fd(&self) -> BorrowedFd<'_> {
504        unsafe { BorrowedFd::borrow_raw(1) }
505    }
506}
507
508#[stable(feature = "io_safety", since = "1.63.0")]
509impl<'a> AsFd for io::StdoutLock<'a> {
510    #[inline]
511    fn as_fd(&self) -> BorrowedFd<'_> {
512        // SAFETY: user code should not close stdout out from under the standard library
513        unsafe { BorrowedFd::borrow_raw(1) }
514    }
515}
516
517#[stable(feature = "io_safety", since = "1.63.0")]
518impl AsFd for io::Stderr {
519    #[inline]
520    fn as_fd(&self) -> BorrowedFd<'_> {
521        unsafe { BorrowedFd::borrow_raw(2) }
522    }
523}
524
525#[stable(feature = "io_safety", since = "1.63.0")]
526impl<'a> AsFd for io::StderrLock<'a> {
527    #[inline]
528    fn as_fd(&self) -> BorrowedFd<'_> {
529        // SAFETY: user code should not close stderr out from under the standard library
530        unsafe { BorrowedFd::borrow_raw(2) }
531    }
532}
533
534#[stable(feature = "anonymous_pipe", since = "1.87.0")]
535#[cfg(not(target_os = "trusty"))]
536impl AsFd for io::PipeReader {
537    fn as_fd(&self) -> BorrowedFd<'_> {
538        self.0.as_fd()
539    }
540}
541
542#[stable(feature = "anonymous_pipe", since = "1.87.0")]
543#[cfg(not(target_os = "trusty"))]
544impl From<io::PipeReader> for OwnedFd {
545    fn from(pipe: io::PipeReader) -> Self {
546        pipe.0.into_inner()
547    }
548}
549
550#[stable(feature = "anonymous_pipe", since = "1.87.0")]
551#[cfg(not(target_os = "trusty"))]
552impl AsFd for io::PipeWriter {
553    fn as_fd(&self) -> BorrowedFd<'_> {
554        self.0.as_fd()
555    }
556}
557
558#[stable(feature = "anonymous_pipe", since = "1.87.0")]
559#[cfg(not(target_os = "trusty"))]
560impl From<io::PipeWriter> for OwnedFd {
561    fn from(pipe: io::PipeWriter) -> Self {
562        pipe.0.into_inner()
563    }
564}
565
566#[stable(feature = "anonymous_pipe", since = "1.87.0")]
567#[cfg(not(target_os = "trusty"))]
568impl From<OwnedFd> for io::PipeReader {
569    fn from(owned_fd: OwnedFd) -> Self {
570        Self(FromInner::from_inner(owned_fd))
571    }
572}
573
574#[stable(feature = "anonymous_pipe", since = "1.87.0")]
575#[cfg(not(target_os = "trusty"))]
576impl From<OwnedFd> for io::PipeWriter {
577    fn from(owned_fd: OwnedFd) -> Self {
578        Self(FromInner::from_inner(owned_fd))
579    }
580}
````