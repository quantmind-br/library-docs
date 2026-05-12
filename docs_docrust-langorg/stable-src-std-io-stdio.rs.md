---
title: stdio.rs - source
url: https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#372-376
source: crawler
fetched_at: 2026-05-06T21:31:10.917283611-03:00
rendered_js: false
word_count: 5837
summary: This document defines low-level raw handles for standard input, output, and error streams in Rust, providing unbuffered and unsynchronized access to the underlying system I/O.
tags:
    - rust
    - stdio
    - system-io
    - low-level
    - raw-handle
    - stream-handling
category: reference
---

## std/io/ stdio.rs

````rust
1#![cfg_attr(test, allow(unused))]
2
3#[cfg(test)]
4mod tests;
5
6use crate::cell::{Cell, RefCell};
7use crate::fmt;
8use crate::fs::File;
9use crate::io::prelude::*;
10use crate::io::{
11    self, BorrowedCursor, BufReader, IoSlice, IoSliceMut, LineWriter, Lines, SpecReadByte,
12};
13use crate::panic::{RefUnwindSafe, UnwindSafe};
14use crate::sync::atomic::{Atomic, AtomicBool, Ordering};
15use crate::sync::{Arc, Mutex, MutexGuard, OnceLock, ReentrantLock, ReentrantLockGuard};
16use crate::sys::stdio;
17use crate::thread::AccessError;
18
19type LocalStream = Arc<Mutex<Vec<u8>>>;
20
21thread_local! {
22    /// Used by the test crate to capture the output of the print macros and panics.
23    static OUTPUT_CAPTURE: Cell<Option<LocalStream>> = const {
24        Cell::new(None)
25    }
26}
27
28/// Flag to indicate OUTPUT_CAPTURE is used.
29///
30/// If it is None and was never set on any thread, this flag is set to false,
31/// and OUTPUT_CAPTURE can be safely ignored on all threads, saving some time
32/// and memory registering an unused thread local.
33///
34/// Note about memory ordering: This contains information about whether a
35/// thread local variable might be in use. Although this is a global flag, the
36/// memory ordering between threads does not matter: we only want this flag to
37/// have a consistent order between set_output_capture and print_to *within
38/// the same thread*. Within the same thread, things always have a perfectly
39/// consistent order. So Ordering::Relaxed is fine.
40static OUTPUT_CAPTURE_USED: Atomic<bool> = AtomicBool::new(false);
41
42/// A handle to a raw instance of the standard input stream of this process.
43///
44/// This handle is not synchronized or buffered in any fashion. Constructed via
45/// the `std::io::stdio::stdin_raw` function.
46struct StdinRaw(stdio::Stdin);
47
48/// A handle to a raw instance of the standard output stream of this process.
49///
50/// This handle is not synchronized or buffered in any fashion. Constructed via
51/// the `std::io::stdio::stdout_raw` function.
52struct StdoutRaw(stdio::Stdout);
53
54/// A handle to a raw instance of the standard output stream of this process.
55///
56/// This handle is not synchronized or buffered in any fashion. Constructed via
57/// the `std::io::stdio::stderr_raw` function.
58struct StderrRaw(stdio::Stderr);
59
60/// Constructs a new raw handle to the standard input of this process.
61///
62/// The returned handle does not interact with any other handles created nor
63/// handles returned by `std::io::stdin`. Data buffered by the `std::io::stdin`
64/// handles is **not** available to raw handles returned from this function.
65///
66/// The returned handle has no external synchronization or buffering.
67#[unstable(feature = "libstd_sys_internals", issue = "none")]
68const fn stdin_raw() -> StdinRaw {
69    StdinRaw(stdio::Stdin::new())
70}
71
72/// Constructs a new raw handle to the standard output stream of this process.
73///
74/// The returned handle does not interact with any other handles created nor
75/// handles returned by `std::io::stdout`. Note that data is buffered by the
76/// `std::io::stdout` handles so writes which happen via this raw handle may
77/// appear before previous writes.
78///
79/// The returned handle has no external synchronization or buffering layered on
80/// top.
81#[unstable(feature = "libstd_sys_internals", issue = "none")]
82const fn stdout_raw() -> StdoutRaw {
83    StdoutRaw(stdio::Stdout::new())
84}
85
86/// Constructs a new raw handle to the standard error stream of this process.
87///
88/// The returned handle does not interact with any other handles created nor
89/// handles returned by `std::io::stderr`.
90///
91/// The returned handle has no external synchronization or buffering layered on
92/// top.
93#[unstable(feature = "libstd_sys_internals", issue = "none")]
94const fn stderr_raw() -> StderrRaw {
95    StderrRaw(stdio::Stderr::new())
96}
97
98impl Read for StdinRaw {
99    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
100        handle_ebadf(self.0.read(buf), || Ok(0))
101    }
102
103    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> io::Result<()> {
104        handle_ebadf(self.0.read_buf(buf), || Ok(()))
105    }
106
107    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> io::Result<usize> {
108        handle_ebadf(self.0.read_vectored(bufs), || Ok(0))
109    }
110
111    #[inline]
112    fn is_read_vectored(&self) -> bool {
113        self.0.is_read_vectored()
114    }
115
116    fn read_exact(&mut self, buf: &mut [u8]) -> io::Result<()> {
117        if buf.is_empty() {
118            return Ok(());
119        }
120        handle_ebadf(self.0.read_exact(buf), || Err(io::Error::READ_EXACT_EOF))
121    }
122
123    fn read_buf_exact(&mut self, buf: BorrowedCursor<'_>) -> io::Result<()> {
124        if buf.capacity() == 0 {
125            return Ok(());
126        }
127        handle_ebadf(self.0.read_buf_exact(buf), || Err(io::Error::READ_EXACT_EOF))
128    }
129
130    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> io::Result<usize> {
131        handle_ebadf(self.0.read_to_end(buf), || Ok(0))
132    }
133
134    fn read_to_string(&mut self, buf: &mut String) -> io::Result<usize> {
135        handle_ebadf(self.0.read_to_string(buf), || Ok(0))
136    }
137}
138
139impl Write for StdoutRaw {
140    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
141        handle_ebadf(self.0.write(buf), || Ok(buf.len()))
142    }
143
144    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
145        let total = || Ok(bufs.iter().map(|b| b.len()).sum());
146        handle_ebadf(self.0.write_vectored(bufs), total)
147    }
148
149    #[inline]
150    fn is_write_vectored(&self) -> bool {
151        self.0.is_write_vectored()
152    }
153
154    fn flush(&mut self) -> io::Result<()> {
155        handle_ebadf(self.0.flush(), || Ok(()))
156    }
157
158    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
159        handle_ebadf(self.0.write_all(buf), || Ok(()))
160    }
161
162    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
163        handle_ebadf(self.0.write_all_vectored(bufs), || Ok(()))
164    }
165
166    fn write_fmt(&mut self, fmt: fmt::Arguments<'_>) -> io::Result<()> {
167        handle_ebadf(self.0.write_fmt(fmt), || Ok(()))
168    }
169}
170
171impl Write for StderrRaw {
172    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
173        handle_ebadf(self.0.write(buf), || Ok(buf.len()))
174    }
175
176    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
177        let total = || Ok(bufs.iter().map(|b| b.len()).sum());
178        handle_ebadf(self.0.write_vectored(bufs), total)
179    }
180
181    #[inline]
182    fn is_write_vectored(&self) -> bool {
183        self.0.is_write_vectored()
184    }
185
186    fn flush(&mut self) -> io::Result<()> {
187        handle_ebadf(self.0.flush(), || Ok(()))
188    }
189
190    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
191        handle_ebadf(self.0.write_all(buf), || Ok(()))
192    }
193
194    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
195        handle_ebadf(self.0.write_all_vectored(bufs), || Ok(()))
196    }
197
198    fn write_fmt(&mut self, fmt: fmt::Arguments<'_>) -> io::Result<()> {
199        handle_ebadf(self.0.write_fmt(fmt), || Ok(()))
200    }
201}
202
203fn handle_ebadf<T>(r: io::Result<T>, default: impl FnOnce() -> io::Result<T>) -> io::Result<T> {
204    match r {
205        Err(ref e) if stdio::is_ebadf(e) => default(),
206        r => r,
207    }
208}
209
210/// A handle to the standard input stream of a process.
211///
212/// Each handle is a shared reference to a global buffer of input data to this
213/// process. A handle can be `lock`'d to gain full access to [`BufRead`] methods
214/// (e.g., `.lines()`). Reads to this handle are otherwise locked with respect
215/// to other reads.
216///
217/// This handle implements the `Read` trait, but beware that concurrent reads
218/// of `Stdin` must be executed with care.
219///
220/// Created by the [`io::stdin`] method.
221///
222/// [`io::stdin`]: stdin
223///
224/// ### Note: Windows Portability Considerations
225///
226/// When operating in a console, the Windows implementation of this stream does not support
227/// non-UTF-8 byte sequences. Attempting to read bytes that are not valid UTF-8 will return
228/// an error.
229///
230/// In a process with a detached console, such as one using
231/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
232/// the contained handle will be null. In such cases, the standard library's `Read` and
233/// `Write` will do nothing and silently succeed. All other I/O operations, via the
234/// standard library or via raw Windows API calls, will fail.
235///
236/// # Examples
237///
238/// ```no_run
239/// use std::io;
240///
241/// fn main() -> io::Result<()> {
242///     let mut buffer = String::new();
243///     let stdin = io::stdin(); // We get `Stdin` here.
244///     stdin.read_line(&mut buffer)?;
245///     Ok(())
246/// }
247/// ```
248#[stable(feature = "rust1", since = "1.0.0")]
249#[cfg_attr(not(test), rustc_diagnostic_item = "Stdin")]
250pub struct Stdin {
251    inner: &'static Mutex<BufReader<StdinRaw>>,
252}
253
254/// A locked reference to the [`Stdin`] handle.
255///
256/// This handle implements both the [`Read`] and [`BufRead`] traits, and
257/// is constructed via the [`Stdin::lock`] method.
258///
259/// ### Note: Windows Portability Considerations
260///
261/// When operating in a console, the Windows implementation of this stream does not support
262/// non-UTF-8 byte sequences. Attempting to read bytes that are not valid UTF-8 will return
263/// an error.
264///
265/// In a process with a detached console, such as one using
266/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
267/// the contained handle will be null. In such cases, the standard library's `Read` and
268/// `Write` will do nothing and silently succeed. All other I/O operations, via the
269/// standard library or via raw Windows API calls, will fail.
270///
271/// # Examples
272///
273/// ```no_run
274/// use std::io::{self, BufRead};
275///
276/// fn main() -> io::Result<()> {
277///     let mut buffer = String::new();
278///     let stdin = io::stdin(); // We get `Stdin` here.
279///     {
280///         let mut handle = stdin.lock(); // We get `StdinLock` here.
281///         handle.read_line(&mut buffer)?;
282///     } // `StdinLock` is dropped here.
283///     Ok(())
284/// }
285/// ```
286#[must_use = "if unused stdin will immediately unlock"]
287#[stable(feature = "rust1", since = "1.0.0")]
288pub struct StdinLock<'a> {
289    inner: MutexGuard<'a, BufReader<StdinRaw>>,
290}
291
292/// Constructs a new handle to the standard input of the current process.
293///
294/// Each handle returned is a reference to a shared global buffer whose access
295/// is synchronized via a mutex. If you need more explicit control over
296/// locking, see the [`Stdin::lock`] method.
297///
298/// ### Note: Windows Portability Considerations
299///
300/// When operating in a console, the Windows implementation of this stream does not support
301/// non-UTF-8 byte sequences. Attempting to read bytes that are not valid UTF-8 will return
302/// an error.
303///
304/// In a process with a detached console, such as one using
305/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
306/// the contained handle will be null. In such cases, the standard library's `Read` and
307/// `Write` will do nothing and silently succeed. All other I/O operations, via the
308/// standard library or via raw Windows API calls, will fail.
309///
310/// # Examples
311///
312/// Using implicit synchronization:
313///
314/// ```no_run
315/// use std::io;
316///
317/// fn main() -> io::Result<()> {
318///     let mut buffer = String::new();
319///     io::stdin().read_line(&mut buffer)?;
320///     Ok(())
321/// }
322/// ```
323///
324/// Using explicit synchronization:
325///
326/// ```no_run
327/// use std::io::{self, BufRead};
328///
329/// fn main() -> io::Result<()> {
330///     let mut buffer = String::new();
331///     let stdin = io::stdin();
332///     let mut handle = stdin.lock();
333///
334///     handle.read_line(&mut buffer)?;
335///     Ok(())
336/// }
337/// ```
338#[must_use]
339#[stable(feature = "rust1", since = "1.0.0")]
340pub fn stdin() -> Stdin {
341    static INSTANCE: OnceLock<Mutex<BufReader<StdinRaw>>> = OnceLock::new();
342    Stdin {
343        inner: INSTANCE.get_or_init(|| {
344            Mutex::new(BufReader::with_capacity(stdio::STDIN_BUF_SIZE, stdin_raw()))
345        }),
346    }
347}
348
349impl Stdin {
350    /// Locks this handle to the standard input stream, returning a readable
351    /// guard.
352    ///
353    /// The lock is released when the returned lock goes out of scope. The
354    /// returned guard also implements the [`Read`] and [`BufRead`] traits for
355    /// accessing the underlying data.
356    ///
357    /// # Examples
358    ///
359    /// ```no_run
360    /// use std::io::{self, BufRead};
361    ///
362    /// fn main() -> io::Result<()> {
363    ///     let mut buffer = String::new();
364    ///     let stdin = io::stdin();
365    ///     let mut handle = stdin.lock();
366    ///
367    ///     handle.read_line(&mut buffer)?;
368    ///     Ok(())
369    /// }
370    /// ```
371    #[stable(feature = "rust1", since = "1.0.0")]
372    pub fn lock(&self) -> StdinLock<'static> {
373        // Locks this handle with 'static lifetime. This depends on the
374        // implementation detail that the underlying `Mutex` is static.
375        StdinLock { inner: self.inner.lock().unwrap_or_else(|e| e.into_inner()) }
376    }
377
378    /// Locks this handle and reads a line of input, appending it to the specified buffer.
379    ///
380    /// For detailed semantics of this method, see the documentation on
381    /// [`BufRead::read_line`]. In particular:
382    /// * Previous content of the buffer will be preserved. To avoid appending
383    ///   to the buffer, you need to [`clear`] it first.
384    /// * The trailing newline character, if any, is included in the buffer.
385    ///
386    /// [`clear`]: String::clear
387    ///
388    /// # Examples
389    ///
390    /// ```no_run
391    /// use std::io;
392    ///
393    /// let mut input = String::new();
394    /// match io::stdin().read_line(&mut input) {
395    ///     Ok(n) => {
396    ///         println!("{n} bytes read");
397    ///         println!("{input}");
398    ///     }
399    ///     Err(error) => println!("error: {error}"),
400    /// }
401    /// ```
402    ///
403    /// You can run the example one of two ways:
404    ///
405    /// - Pipe some text to it, e.g., `printf foo | path/to/executable`
406    /// - Give it text interactively by running the executable directly,
407    ///   in which case it will wait for the Enter key to be pressed before
408    ///   continuing
409    #[stable(feature = "rust1", since = "1.0.0")]
410    #[rustc_confusables("get_line")]
411    pub fn read_line(&self, buf: &mut String) -> io::Result<usize> {
412        self.lock().read_line(buf)
413    }
414
415    /// Consumes this handle and returns an iterator over input lines.
416    ///
417    /// For detailed semantics of this method, see the documentation on
418    /// [`BufRead::lines`].
419    ///
420    /// # Examples
421    ///
422    /// ```no_run
423    /// use std::io;
424    ///
425    /// let lines = io::stdin().lines();
426    /// for line in lines {
427    ///     println!("got a line: {}", line.unwrap());
428    /// }
429    /// ```
430    #[must_use = "`self` will be dropped if the result is not used"]
431    #[stable(feature = "stdin_forwarders", since = "1.62.0")]
432    pub fn lines(self) -> Lines<StdinLock<'static>> {
433        self.lock().lines()
434    }
435}
436
437#[stable(feature = "std_debug", since = "1.16.0")]
438impl fmt::Debug for Stdin {
439    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
440        f.debug_struct("Stdin").finish_non_exhaustive()
441    }
442}
443
444#[stable(feature = "rust1", since = "1.0.0")]
445impl Read for Stdin {
446    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
447        self.lock().read(buf)
448    }
449    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> io::Result<()> {
450        self.lock().read_buf(buf)
451    }
452    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> io::Result<usize> {
453        self.lock().read_vectored(bufs)
454    }
455    #[inline]
456    fn is_read_vectored(&self) -> bool {
457        self.lock().is_read_vectored()
458    }
459    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> io::Result<usize> {
460        self.lock().read_to_end(buf)
461    }
462    fn read_to_string(&mut self, buf: &mut String) -> io::Result<usize> {
463        self.lock().read_to_string(buf)
464    }
465    fn read_exact(&mut self, buf: &mut [u8]) -> io::Result<()> {
466        self.lock().read_exact(buf)
467    }
468    fn read_buf_exact(&mut self, cursor: BorrowedCursor<'_>) -> io::Result<()> {
469        self.lock().read_buf_exact(cursor)
470    }
471}
472
473#[stable(feature = "read_shared_stdin", since = "1.78.0")]
474impl Read for &Stdin {
475    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
476        self.lock().read(buf)
477    }
478    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> io::Result<()> {
479        self.lock().read_buf(buf)
480    }
481    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> io::Result<usize> {
482        self.lock().read_vectored(bufs)
483    }
484    #[inline]
485    fn is_read_vectored(&self) -> bool {
486        self.lock().is_read_vectored()
487    }
488    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> io::Result<usize> {
489        self.lock().read_to_end(buf)
490    }
491    fn read_to_string(&mut self, buf: &mut String) -> io::Result<usize> {
492        self.lock().read_to_string(buf)
493    }
494    fn read_exact(&mut self, buf: &mut [u8]) -> io::Result<()> {
495        self.lock().read_exact(buf)
496    }
497    fn read_buf_exact(&mut self, cursor: BorrowedCursor<'_>) -> io::Result<()> {
498        self.lock().read_buf_exact(cursor)
499    }
500}
501
502// only used by platform-dependent io::copy specializations, i.e. unused on some platforms
503#[cfg(any(target_os = "linux", target_os = "android"))]
504impl StdinLock<'_> {
505    pub(crate) fn as_mut_buf(&mut self) -> &mut BufReader<impl Read> {
506        &mut self.inner
507    }
508}
509
510#[stable(feature = "rust1", since = "1.0.0")]
511impl Read for StdinLock<'_> {
512    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
513        self.inner.read(buf)
514    }
515
516    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> io::Result<()> {
517        self.inner.read_buf(buf)
518    }
519
520    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> io::Result<usize> {
521        self.inner.read_vectored(bufs)
522    }
523
524    #[inline]
525    fn is_read_vectored(&self) -> bool {
526        self.inner.is_read_vectored()
527    }
528
529    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> io::Result<usize> {
530        self.inner.read_to_end(buf)
531    }
532
533    fn read_to_string(&mut self, buf: &mut String) -> io::Result<usize> {
534        self.inner.read_to_string(buf)
535    }
536
537    fn read_exact(&mut self, buf: &mut [u8]) -> io::Result<()> {
538        self.inner.read_exact(buf)
539    }
540
541    fn read_buf_exact(&mut self, cursor: BorrowedCursor<'_>) -> io::Result<()> {
542        self.inner.read_buf_exact(cursor)
543    }
544}
545
546impl SpecReadByte for StdinLock<'_> {
547    #[inline]
548    fn spec_read_byte(&mut self) -> Option<io::Result<u8>> {
549        BufReader::spec_read_byte(&mut *self.inner)
550    }
551}
552
553#[stable(feature = "rust1", since = "1.0.0")]
554impl BufRead for StdinLock<'_> {
555    fn fill_buf(&mut self) -> io::Result<&[u8]> {
556        self.inner.fill_buf()
557    }
558
559    fn consume(&mut self, n: usize) {
560        self.inner.consume(n)
561    }
562
563    fn read_until(&mut self, byte: u8, buf: &mut Vec<u8>) -> io::Result<usize> {
564        self.inner.read_until(byte, buf)
565    }
566
567    fn read_line(&mut self, buf: &mut String) -> io::Result<usize> {
568        self.inner.read_line(buf)
569    }
570}
571
572#[stable(feature = "std_debug", since = "1.16.0")]
573impl fmt::Debug for StdinLock<'_> {
574    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
575        f.debug_struct("StdinLock").finish_non_exhaustive()
576    }
577}
578
579/// A handle to the global standard output stream of the current process.
580///
581/// Each handle shares a global buffer of data to be written to the standard
582/// output stream. Access is also synchronized via a lock and explicit control
583/// over locking is available via the [`lock`] method.
584///
585/// By default, the handle is line-buffered when connected to a terminal, meaning
586/// it flushes automatically when a newline (`\n`) is encountered. For immediate
587/// output, you can manually call the [`flush`] method. When the handle goes out
588/// of scope, the buffer is automatically flushed.
589///
590/// Created by the [`io::stdout`] method.
591///
592/// ### Note: Windows Portability Considerations
593///
594/// When operating in a console, the Windows implementation of this stream does not support
595/// non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return
596/// an error.
597///
598/// In a process with a detached console, such as one using
599/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
600/// the contained handle will be null. In such cases, the standard library's `Read` and
601/// `Write` will do nothing and silently succeed. All other I/O operations, via the
602/// standard library or via raw Windows API calls, will fail.
603///
604/// [`lock`]: Stdout::lock
605/// [`flush`]: Write::flush
606/// [`io::stdout`]: stdout
607#[stable(feature = "rust1", since = "1.0.0")]
608pub struct Stdout {
609    // FIXME: this should be LineWriter or BufWriter depending on the state of
610    //        stdout (tty or not). Note that if this is not line buffered it
611    //        should also flush-on-panic or some form of flush-on-abort.
612    inner: &'static ReentrantLock<RefCell<LineWriter<StdoutRaw>>>,
613}
614
615/// A locked reference to the [`Stdout`] handle.
616///
617/// This handle implements the [`Write`] trait, and is constructed via
618/// the [`Stdout::lock`] method. See its documentation for more.
619///
620/// By default, the handle is line-buffered when connected to a terminal, meaning
621/// it flushes automatically when a newline (`\n`) is encountered. For immediate
622/// output, you can manually call the [`flush`] method. When the handle goes out
623/// of scope, the buffer is automatically flushed.
624///
625/// ### Note: Windows Portability Considerations
626///
627/// When operating in a console, the Windows implementation of this stream does not support
628/// non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return
629/// an error.
630///
631/// In a process with a detached console, such as one using
632/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
633/// the contained handle will be null. In such cases, the standard library's `Read` and
634/// `Write` will do nothing and silently succeed. All other I/O operations, via the
635/// standard library or via raw Windows API calls, will fail.
636///
637/// [`flush`]: Write::flush
638#[must_use = "if unused stdout will immediately unlock"]
639#[stable(feature = "rust1", since = "1.0.0")]
640pub struct StdoutLock<'a> {
641    inner: ReentrantLockGuard<'a, RefCell<LineWriter<StdoutRaw>>>,
642}
643
644static STDOUT: OnceLock<ReentrantLock<RefCell<LineWriter<StdoutRaw>>>> = OnceLock::new();
645
646/// Constructs a new handle to the standard output of the current process.
647///
648/// Each handle returned is a reference to a shared global buffer whose access
649/// is synchronized via a mutex. If you need more explicit control over
650/// locking, see the [`Stdout::lock`] method.
651///
652/// By default, the handle is line-buffered when connected to a terminal, meaning
653/// it flushes automatically when a newline (`\n`) is encountered. For immediate
654/// output, you can manually call the [`flush`] method. When the handle goes out
655/// of scope, the buffer is automatically flushed.
656///
657/// ### Note: Windows Portability Considerations
658///
659/// When operating in a console, the Windows implementation of this stream does not support
660/// non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return
661/// an error.
662///
663/// In a process with a detached console, such as one using
664/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
665/// the contained handle will be null. In such cases, the standard library's `Read` and
666/// `Write` will do nothing and silently succeed. All other I/O operations, via the
667/// standard library or via raw Windows API calls, will fail.
668///
669/// # Examples
670///
671/// Using implicit synchronization:
672///
673/// ```no_run
674/// use std::io::{self, Write};
675///
676/// fn main() -> io::Result<()> {
677///     io::stdout().write_all(b"hello world")?;
678///
679///     Ok(())
680/// }
681/// ```
682///
683/// Using explicit synchronization:
684///
685/// ```no_run
686/// use std::io::{self, Write};
687///
688/// fn main() -> io::Result<()> {
689///     let stdout = io::stdout();
690///     let mut handle = stdout.lock();
691///
692///     handle.write_all(b"hello world")?;
693///
694///     Ok(())
695/// }
696/// ```
697///
698/// Ensuring output is flushed immediately:
699///
700/// ```no_run
701/// use std::io::{self, Write};
702///
703/// fn main() -> io::Result<()> {
704///     let mut stdout = io::stdout();
705///     stdout.write_all(b"hello, ")?;
706///     stdout.flush()?;                // Manual flush
707///     stdout.write_all(b"world!\n")?; // Automatically flushed
708///     Ok(())
709/// }
710/// ```
711///
712/// [`flush`]: Write::flush
713#[must_use]
714#[stable(feature = "rust1", since = "1.0.0")]
715#[cfg_attr(not(test), rustc_diagnostic_item = "io_stdout")]
716pub fn stdout() -> Stdout {
717    Stdout {
718        inner: STDOUT
719            .get_or_init(|| ReentrantLock::new(RefCell::new(LineWriter::new(stdout_raw())))),
720    }
721}
722
723// Flush the data and disable buffering during shutdown
724// by replacing the line writer by one with zero
725// buffering capacity.
726pub fn cleanup() {
727    let mut initialized = false;
728    let stdout = STDOUT.get_or_init(|| {
729        initialized = true;
730        ReentrantLock::new(RefCell::new(LineWriter::with_capacity(0, stdout_raw())))
731    });
732
733    if !initialized {
734        // The buffer was previously initialized, overwrite it here.
735        // We use try_lock() instead of lock(), because someone
736        // might have leaked a StdoutLock, which would
737        // otherwise cause a deadlock here.
738        if let Some(lock) = stdout.try_lock() {
739            *lock.borrow_mut() = LineWriter::with_capacity(0, stdout_raw());
740        }
741    }
742}
743
744impl Stdout {
745    /// Locks this handle to the standard output stream, returning a writable
746    /// guard.
747    ///
748    /// The lock is released when the returned lock goes out of scope. The
749    /// returned guard also implements the `Write` trait for writing data.
750    ///
751    /// # Examples
752    ///
753    /// ```no_run
754    /// use std::io::{self, Write};
755    ///
756    /// fn main() -> io::Result<()> {
757    ///     let mut stdout = io::stdout().lock();
758    ///
759    ///     stdout.write_all(b"hello world")?;
760    ///
761    ///     Ok(())
762    /// }
763    /// ```
764    #[stable(feature = "rust1", since = "1.0.0")]
765    pub fn lock(&self) -> StdoutLock<'static> {
766        // Locks this handle with 'static lifetime. This depends on the
767        // implementation detail that the underlying `ReentrantMutex` is
768        // static.
769        StdoutLock { inner: self.inner.lock() }
770    }
771}
772
773#[stable(feature = "catch_unwind", since = "1.9.0")]
774impl UnwindSafe for Stdout {}
775
776#[stable(feature = "catch_unwind", since = "1.9.0")]
777impl RefUnwindSafe for Stdout {}
778
779#[stable(feature = "std_debug", since = "1.16.0")]
780impl fmt::Debug for Stdout {
781    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
782        f.debug_struct("Stdout").finish_non_exhaustive()
783    }
784}
785
786#[stable(feature = "rust1", since = "1.0.0")]
787impl Write for Stdout {
788    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
789        (&*self).write(buf)
790    }
791    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
792        (&*self).write_vectored(bufs)
793    }
794    #[inline]
795    fn is_write_vectored(&self) -> bool {
796        io::Write::is_write_vectored(&&*self)
797    }
798    fn flush(&mut self) -> io::Result<()> {
799        (&*self).flush()
800    }
801    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
802        (&*self).write_all(buf)
803    }
804    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
805        (&*self).write_all_vectored(bufs)
806    }
807    fn write_fmt(&mut self, args: fmt::Arguments<'_>) -> io::Result<()> {
808        (&*self).write_fmt(args)
809    }
810}
811
812#[stable(feature = "write_mt", since = "1.48.0")]
813impl Write for &Stdout {
814    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
815        self.lock().write(buf)
816    }
817    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
818        self.lock().write_vectored(bufs)
819    }
820    #[inline]
821    fn is_write_vectored(&self) -> bool {
822        self.lock().is_write_vectored()
823    }
824    fn flush(&mut self) -> io::Result<()> {
825        self.lock().flush()
826    }
827    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
828        self.lock().write_all(buf)
829    }
830    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
831        self.lock().write_all_vectored(bufs)
832    }
833    fn write_fmt(&mut self, args: fmt::Arguments<'_>) -> io::Result<()> {
834        self.lock().write_fmt(args)
835    }
836}
837
838#[stable(feature = "catch_unwind", since = "1.9.0")]
839impl UnwindSafe for StdoutLock<'_> {}
840
841#[stable(feature = "catch_unwind", since = "1.9.0")]
842impl RefUnwindSafe for StdoutLock<'_> {}
843
844#[stable(feature = "rust1", since = "1.0.0")]
845impl Write for StdoutLock<'_> {
846    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
847        self.inner.borrow_mut().write(buf)
848    }
849    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
850        self.inner.borrow_mut().write_vectored(bufs)
851    }
852    #[inline]
853    fn is_write_vectored(&self) -> bool {
854        self.inner.borrow_mut().is_write_vectored()
855    }
856    fn flush(&mut self) -> io::Result<()> {
857        self.inner.borrow_mut().flush()
858    }
859    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
860        self.inner.borrow_mut().write_all(buf)
861    }
862    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
863        self.inner.borrow_mut().write_all_vectored(bufs)
864    }
865}
866
867#[stable(feature = "std_debug", since = "1.16.0")]
868impl fmt::Debug for StdoutLock<'_> {
869    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
870        f.debug_struct("StdoutLock").finish_non_exhaustive()
871    }
872}
873
874/// A handle to the standard error stream of a process.
875///
876/// For more information, see the [`io::stderr`] method.
877///
878/// [`io::stderr`]: stderr
879///
880/// ### Note: Windows Portability Considerations
881///
882/// When operating in a console, the Windows implementation of this stream does not support
883/// non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return
884/// an error.
885///
886/// In a process with a detached console, such as one using
887/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
888/// the contained handle will be null. In such cases, the standard library's `Read` and
889/// `Write` will do nothing and silently succeed. All other I/O operations, via the
890/// standard library or via raw Windows API calls, will fail.
891#[stable(feature = "rust1", since = "1.0.0")]
892pub struct Stderr {
893    inner: &'static ReentrantLock<RefCell<StderrRaw>>,
894}
895
896/// A locked reference to the [`Stderr`] handle.
897///
898/// This handle implements the [`Write`] trait and is constructed via
899/// the [`Stderr::lock`] method. See its documentation for more.
900///
901/// ### Note: Windows Portability Considerations
902///
903/// When operating in a console, the Windows implementation of this stream does not support
904/// non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return
905/// an error.
906///
907/// In a process with a detached console, such as one using
908/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
909/// the contained handle will be null. In such cases, the standard library's `Read` and
910/// `Write` will do nothing and silently succeed. All other I/O operations, via the
911/// standard library or via raw Windows API calls, will fail.
912#[must_use = "if unused stderr will immediately unlock"]
913#[stable(feature = "rust1", since = "1.0.0")]
914pub struct StderrLock<'a> {
915    inner: ReentrantLockGuard<'a, RefCell<StderrRaw>>,
916}
917
918/// Constructs a new handle to the standard error of the current process.
919///
920/// This handle is not buffered.
921///
922/// ### Note: Windows Portability Considerations
923///
924/// When operating in a console, the Windows implementation of this stream does not support
925/// non-UTF-8 byte sequences. Attempting to write bytes that are not valid UTF-8 will return
926/// an error.
927///
928/// In a process with a detached console, such as one using
929/// `#![windows_subsystem = "windows"]`, or in a child process spawned from such a process,
930/// the contained handle will be null. In such cases, the standard library's `Read` and
931/// `Write` will do nothing and silently succeed. All other I/O operations, via the
932/// standard library or via raw Windows API calls, will fail.
933///
934/// # Examples
935///
936/// Using implicit synchronization:
937///
938/// ```no_run
939/// use std::io::{self, Write};
940///
941/// fn main() -> io::Result<()> {
942///     io::stderr().write_all(b"hello world")?;
943///
944///     Ok(())
945/// }
946/// ```
947///
948/// Using explicit synchronization:
949///
950/// ```no_run
951/// use std::io::{self, Write};
952///
953/// fn main() -> io::Result<()> {
954///     let stderr = io::stderr();
955///     let mut handle = stderr.lock();
956///
957///     handle.write_all(b"hello world")?;
958///
959///     Ok(())
960/// }
961/// ```
962#[must_use]
963#[stable(feature = "rust1", since = "1.0.0")]
964#[cfg_attr(not(test), rustc_diagnostic_item = "io_stderr")]
965pub fn stderr() -> Stderr {
966    // Note that unlike `stdout()` we don't use `at_exit` here to register a
967    // destructor. Stderr is not buffered, so there's no need to run a
968    // destructor for flushing the buffer
969    static INSTANCE: ReentrantLock<RefCell<StderrRaw>> =
970        ReentrantLock::new(RefCell::new(stderr_raw()));
971
972    Stderr { inner: &INSTANCE }
973}
974
975impl Stderr {
976    /// Locks this handle to the standard error stream, returning a writable
977    /// guard.
978    ///
979    /// The lock is released when the returned lock goes out of scope. The
980    /// returned guard also implements the [`Write`] trait for writing data.
981    ///
982    /// # Examples
983    ///
984    /// ```
985    /// use std::io::{self, Write};
986    ///
987    /// fn foo() -> io::Result<()> {
988    ///     let stderr = io::stderr();
989    ///     let mut handle = stderr.lock();
990    ///
991    ///     handle.write_all(b"hello world")?;
992    ///
993    ///     Ok(())
994    /// }
995    /// ```
996    #[stable(feature = "rust1", since = "1.0.0")]
997    pub fn lock(&self) -> StderrLock<'static> {
998        // Locks this handle with 'static lifetime. This depends on the
999        // implementation detail that the underlying `ReentrantMutex` is
1000        // static.
1001        StderrLock { inner: self.inner.lock() }
1002    }
1003}
1004
1005#[stable(feature = "catch_unwind", since = "1.9.0")]
1006impl UnwindSafe for Stderr {}
1007
1008#[stable(feature = "catch_unwind", since = "1.9.0")]
1009impl RefUnwindSafe for Stderr {}
1010
1011#[stable(feature = "std_debug", since = "1.16.0")]
1012impl fmt::Debug for Stderr {
1013    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1014        f.debug_struct("Stderr").finish_non_exhaustive()
1015    }
1016}
1017
1018#[stable(feature = "rust1", since = "1.0.0")]
1019impl Write for Stderr {
1020    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
1021        (&*self).write(buf)
1022    }
1023    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
1024        (&*self).write_vectored(bufs)
1025    }
1026    #[inline]
1027    fn is_write_vectored(&self) -> bool {
1028        io::Write::is_write_vectored(&&*self)
1029    }
1030    fn flush(&mut self) -> io::Result<()> {
1031        (&*self).flush()
1032    }
1033    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
1034        (&*self).write_all(buf)
1035    }
1036    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
1037        (&*self).write_all_vectored(bufs)
1038    }
1039    fn write_fmt(&mut self, args: fmt::Arguments<'_>) -> io::Result<()> {
1040        (&*self).write_fmt(args)
1041    }
1042}
1043
1044#[stable(feature = "write_mt", since = "1.48.0")]
1045impl Write for &Stderr {
1046    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
1047        self.lock().write(buf)
1048    }
1049    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
1050        self.lock().write_vectored(bufs)
1051    }
1052    #[inline]
1053    fn is_write_vectored(&self) -> bool {
1054        self.lock().is_write_vectored()
1055    }
1056    fn flush(&mut self) -> io::Result<()> {
1057        self.lock().flush()
1058    }
1059    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
1060        self.lock().write_all(buf)
1061    }
1062    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
1063        self.lock().write_all_vectored(bufs)
1064    }
1065    fn write_fmt(&mut self, args: fmt::Arguments<'_>) -> io::Result<()> {
1066        self.lock().write_fmt(args)
1067    }
1068}
1069
1070#[stable(feature = "catch_unwind", since = "1.9.0")]
1071impl UnwindSafe for StderrLock<'_> {}
1072
1073#[stable(feature = "catch_unwind", since = "1.9.0")]
1074impl RefUnwindSafe for StderrLock<'_> {}
1075
1076#[stable(feature = "rust1", since = "1.0.0")]
1077impl Write for StderrLock<'_> {
1078    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
1079        self.inner.borrow_mut().write(buf)
1080    }
1081    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
1082        self.inner.borrow_mut().write_vectored(bufs)
1083    }
1084    #[inline]
1085    fn is_write_vectored(&self) -> bool {
1086        self.inner.borrow_mut().is_write_vectored()
1087    }
1088    fn flush(&mut self) -> io::Result<()> {
1089        self.inner.borrow_mut().flush()
1090    }
1091    fn write_all(&mut self, buf: &[u8]) -> io::Result<()> {
1092        self.inner.borrow_mut().write_all(buf)
1093    }
1094    fn write_all_vectored(&mut self, bufs: &mut [IoSlice<'_>]) -> io::Result<()> {
1095        self.inner.borrow_mut().write_all_vectored(bufs)
1096    }
1097}
1098
1099#[stable(feature = "std_debug", since = "1.16.0")]
1100impl fmt::Debug for StderrLock<'_> {
1101    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1102        f.debug_struct("StderrLock").finish_non_exhaustive()
1103    }
1104}
1105
1106/// Sets the thread-local output capture buffer and returns the old one.
1107#[unstable(
1108    feature = "internal_output_capture",
1109    reason = "this function is meant for use in the test crate \
1110        and may disappear in the future",
1111    issue = "none"
1112)]
1113#[doc(hidden)]
1114pub fn set_output_capture(sink: Option<LocalStream>) -> Option<LocalStream> {
1115    try_set_output_capture(sink).expect(
1116        "cannot access a Thread Local Storage value \
1117         during or after destruction",
1118    )
1119}
1120
1121/// Tries to set the thread-local output capture buffer and returns the old one.
1122/// This may fail once thread-local destructors are called. It's used in panic
1123/// handling instead of `set_output_capture`.
1124#[unstable(
1125    feature = "internal_output_capture",
1126    reason = "this function is meant for use in the test crate \
1127    and may disappear in the future",
1128    issue = "none"
1129)]
1130#[doc(hidden)]
1131pub fn try_set_output_capture(
1132    sink: Option<LocalStream>,
1133) -> Result<Option<LocalStream>, AccessError> {
1134    if sink.is_none() && !OUTPUT_CAPTURE_USED.load(Ordering::Relaxed) {
1135        // OUTPUT_CAPTURE is definitely None since OUTPUT_CAPTURE_USED is false.
1136        return Ok(None);
1137    }
1138    OUTPUT_CAPTURE_USED.store(true, Ordering::Relaxed);
1139    OUTPUT_CAPTURE.try_with(move |slot| slot.replace(sink))
1140}
1141
1142/// Writes `args` to the capture buffer if enabled and possible, or `global_s`
1143/// otherwise. `label` identifies the stream in a panic message.
1144///
1145/// This function is used to print error messages, so it takes extra
1146/// care to avoid causing a panic when `OUTPUT_CAPTURE` is unusable.
1147/// For instance, if the TLS key for output capturing is already destroyed, or
1148/// if the local stream is in use by another thread, it will just fall back to
1149/// the global stream.
1150///
1151/// However, if the actual I/O causes an error, this function does panic.
1152///
1153/// Writing to non-blocking stdout/stderr can cause an error, which will lead
1154/// this function to panic.
1155fn print_to<T>(args: fmt::Arguments<'_>, global_s: fn() -> T, label: &str)
1156where
1157    T: Write,
1158{
1159    if print_to_buffer_if_capture_used(args) {
1160        // Successfully wrote to capture buffer.
1161        return;
1162    }
1163
1164    if let Err(e) = global_s().write_fmt(args) {
1165        panic!("failed printing to {label}: {e}");
1166    }
1167}
1168
1169fn print_to_buffer_if_capture_used(args: fmt::Arguments<'_>) -> bool {
1170    OUTPUT_CAPTURE_USED.load(Ordering::Relaxed)
1171        && OUTPUT_CAPTURE.try_with(|s| {
1172            // Note that we completely remove a local sink to write to in case
1173            // our printing recursively panics/prints, so the recursive
1174            // panic/print goes to the global sink instead of our local sink.
1175            s.take().map(|w| {
1176                let _ = w.lock().unwrap_or_else(|e| e.into_inner()).write_fmt(args);
1177                s.set(Some(w));
1178            })
1179        }) == Ok(Some(()))
1180}
1181
1182/// Used by impl Termination for Result to print error after `main` or a test
1183/// has returned. Should avoid panicking, although we can't help it if one of
1184/// the Display impls inside args decides to.
1185pub(crate) fn attempt_print_to_stderr(args: fmt::Arguments<'_>) {
1186    if print_to_buffer_if_capture_used(args) {
1187        return;
1188    }
1189
1190    // Ignore error if the write fails, for example because stderr is already
1191    // closed. There is not much point panicking at this point.
1192    let _ = stderr().write_fmt(args);
1193}
1194
1195/// Trait to determine if a descriptor/handle refers to a terminal/tty.
1196#[stable(feature = "is_terminal", since = "1.70.0")]
1197pub trait IsTerminal: crate::sealed::Sealed {
1198    /// Returns `true` if the descriptor/handle refers to a terminal/tty.
1199    ///
1200    /// On platforms where Rust does not know how to detect a terminal yet, this will return
1201    /// `false`. This will also return `false` if an unexpected error occurred, such as from
1202    /// passing an invalid file descriptor.
1203    ///
1204    /// # Platform-specific behavior
1205    ///
1206    /// On Windows, in addition to detecting consoles, this currently uses some heuristics to
1207    /// detect older msys/cygwin/mingw pseudo-terminals based on device name: devices with names
1208    /// starting with `msys-` or `cygwin-` and ending in `-pty` will be considered terminals.
1209    /// Note that this [may change in the future][changes].
1210    ///
1211    /// # Examples
1212    ///
1213    /// An example of a type for which `IsTerminal` is implemented is [`Stdin`]:
1214    ///
1215    /// ```no_run
1216    /// use std::io::{self, IsTerminal, Write};
1217    ///
1218    /// fn main() -> io::Result<()> {
1219    ///     let stdin = io::stdin();
1220    ///
1221    ///     // Indicate that the user is prompted for input, if this is a terminal.
1222    ///     if stdin.is_terminal() {
1223    ///         print!("> ");
1224    ///         io::stdout().flush()?;
1225    ///     }
1226    ///
1227    ///     let mut name = String::new();
1228    ///     let _ = stdin.read_line(&mut name)?;
1229    ///
1230    ///     println!("Hello {}", name.trim_end());
1231    ///
1232    ///     Ok(())
1233    /// }
1234    /// ```
1235    ///
1236    /// The example can be run in two ways:
1237    ///
1238    /// - If you run this example by piping some text to it, e.g. `echo "foo" | path/to/executable`
1239    ///   it will print: `Hello foo`.
1240    /// - If you instead run the example interactively by running `path/to/executable` directly, it will
1241    ///   prompt for input.
1242    ///
1243    /// [changes]: io#platform-specific-behavior
1244    /// [`Stdin`]: crate::io::Stdin
1245    #[doc(alias = "isatty")]
1246    #[stable(feature = "is_terminal", since = "1.70.0")]
1247    fn is_terminal(&self) -> bool;
1248}
1249
1250macro_rules! impl_is_terminal {
1251    ($($t:ty),*$(,)?) => {$(
1252        #[unstable(feature = "sealed", issue = "none")]
1253        impl crate::sealed::Sealed for $t {}
1254
1255        #[stable(feature = "is_terminal", since = "1.70.0")]
1256        impl IsTerminal for $t {
1257            #[inline]
1258            fn is_terminal(&self) -> bool {
1259                crate::sys::io::is_terminal(self)
1260            }
1261        }
1262    )*}
1263}
1264
1265impl_is_terminal!(File, Stdin, StdinLock<'_>, Stdout, StdoutLock<'_>, Stderr, StderrLock<'_>);
1266
1267#[unstable(
1268    feature = "print_internals",
1269    reason = "implementation detail which may disappear or be replaced at any time",
1270    issue = "none"
1271)]
1272#[doc(hidden)]
1273#[cfg(not(test))]
1274pub fn _print(args: fmt::Arguments<'_>) {
1275    print_to(args, stdout, "stdout");
1276}
1277
1278#[unstable(
1279    feature = "print_internals",
1280    reason = "implementation detail which may disappear or be replaced at any time",
1281    issue = "none"
1282)]
1283#[doc(hidden)]
1284#[cfg(not(test))]
1285pub fn _eprint(args: fmt::Arguments<'_>) {
1286    print_to(args, stderr, "stderr");
1287}
1288
1289#[cfg(test)]
1290pub use realstd::io::{_eprint, _print};
````