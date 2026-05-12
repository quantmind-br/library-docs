---
title: mod.rs - source
url: https://doc.rust-lang.org/src/std/io/mod.rs.html#1274-1284
source: crawler
fetched_at: 2026-05-06T21:24:32.200082859-03:00
rendered_js: false
word_count: 14790
summary: This document provides an overview of the Rust standard library's input and output module, explaining key traits like Read, Write, Seek, and BufRead, as well as essential utilities for buffered I/O, standard stream handling, and error management.
tags:
    - rust
    - io
    - buffered-io
    - streams
    - traits
    - standard-library
category: concept
---

## std/io/ mod.rs

````rust
1//! Traits, helpers, and type definitions for core I/O functionality.
2//!
3//! The `std::io` module contains a number of common things you'll need
4//! when doing input and output. The most core part of this module is
5//! the [`Read`] and [`Write`] traits, which provide the
6//! most general interface for reading and writing input and output.
7//!
8//! ## Read and Write
9//!
10//! Because they are traits, [`Read`] and [`Write`] are implemented by a number
11//! of other types, and you can implement them for your types too. As such,
12//! you'll see a few different types of I/O throughout the documentation in
13//! this module: [`File`]s, [`TcpStream`]s, and sometimes even [`Vec<T>`]s. For
14//! example, [`Read`] adds a [`read`][`Read::read`] method, which we can use on
15//! [`File`]s:
16//!
17//! ```no_run
18//! use std::io;
19//! use std::io::prelude::*;
20//! use std::fs::File;
21//!
22//! fn main() -> io::Result<()> {
23//!     let mut f = File::open("foo.txt")?;
24//!     let mut buffer = [0; 10];
25//!
26//!     // read up to 10 bytes
27//!     let n = f.read(&mut buffer)?;
28//!
29//!     println!("The bytes: {:?}", &buffer[..n]);
30//!     Ok(())
31//! }
32//! ```
33//!
34//! [`Read`] and [`Write`] are so important, implementors of the two traits have a
35//! nickname: readers and writers. So you'll sometimes see 'a reader' instead
36//! of 'a type that implements the [`Read`] trait'. Much easier!
37//!
38//! ## Seek and BufRead
39//!
40//! Beyond that, there are two important traits that are provided: [`Seek`]
41//! and [`BufRead`]. Both of these build on top of a reader to control
42//! how the reading happens. [`Seek`] lets you control where the next byte is
43//! coming from:
44//!
45//! ```no_run
46//! use std::io;
47//! use std::io::prelude::*;
48//! use std::io::SeekFrom;
49//! use std::fs::File;
50//!
51//! fn main() -> io::Result<()> {
52//!     let mut f = File::open("foo.txt")?;
53//!     let mut buffer = [0; 10];
54//!
55//!     // skip to the last 10 bytes of the file
56//!     f.seek(SeekFrom::End(-10))?;
57//!
58//!     // read up to 10 bytes
59//!     let n = f.read(&mut buffer)?;
60//!
61//!     println!("The bytes: {:?}", &buffer[..n]);
62//!     Ok(())
63//! }
64//! ```
65//!
66//! [`BufRead`] uses an internal buffer to provide a number of other ways to read, but
67//! to show it off, we'll need to talk about buffers in general. Keep reading!
68//!
69//! ## BufReader and BufWriter
70//!
71//! Byte-based interfaces are unwieldy and can be inefficient, as we'd need to be
72//! making near-constant calls to the operating system. To help with this,
73//! `std::io` comes with two structs, [`BufReader`] and [`BufWriter`], which wrap
74//! readers and writers. The wrapper uses a buffer, reducing the number of
75//! calls and providing nicer methods for accessing exactly what you want.
76//!
77//! For example, [`BufReader`] works with the [`BufRead`] trait to add extra
78//! methods to any reader:
79//!
80//! ```no_run
81//! use std::io;
82//! use std::io::prelude::*;
83//! use std::io::BufReader;
84//! use std::fs::File;
85//!
86//! fn main() -> io::Result<()> {
87//!     let f = File::open("foo.txt")?;
88//!     let mut reader = BufReader::new(f);
89//!     let mut buffer = String::new();
90//!
91//!     // read a line into buffer
92//!     reader.read_line(&mut buffer)?;
93//!
94//!     println!("{buffer}");
95//!     Ok(())
96//! }
97//! ```
98//!
99//! [`BufWriter`] doesn't add any new ways of writing; it just buffers every call
100//! to [`write`][`Write::write`]:
101//!
102//! ```no_run
103//! use std::io;
104//! use std::io::prelude::*;
105//! use std::io::BufWriter;
106//! use std::fs::File;
107//!
108//! fn main() -> io::Result<()> {
109//!     let f = File::create("foo.txt")?;
110//!     {
111//!         let mut writer = BufWriter::new(f);
112//!
113//!         // write a byte to the buffer
114//!         writer.write(&[42])?;
115//!
116//!     } // the buffer is flushed once writer goes out of scope
117//!
118//!     Ok(())
119//! }
120//! ```
121//!
122//! ## Standard input and output
123//!
124//! A very common source of input is standard input:
125//!
126//! ```no_run
127//! use std::io;
128//!
129//! fn main() -> io::Result<()> {
130//!     let mut input = String::new();
131//!
132//!     io::stdin().read_line(&mut input)?;
133//!
134//!     println!("You typed: {}", input.trim());
135//!     Ok(())
136//! }
137//! ```
138//!
139//! Note that you cannot use the [`?` operator] in functions that do not return
140//! a [`Result<T, E>`][`Result`]. Instead, you can call [`.unwrap()`]
141//! or `match` on the return value to catch any possible errors:
142//!
143//! ```no_run
144//! use std::io;
145//!
146//! let mut input = String::new();
147//!
148//! io::stdin().read_line(&mut input).unwrap();
149//! ```
150//!
151//! And a very common source of output is standard output:
152//!
153//! ```no_run
154//! use std::io;
155//! use std::io::prelude::*;
156//!
157//! fn main() -> io::Result<()> {
158//!     io::stdout().write(&[42])?;
159//!     Ok(())
160//! }
161//! ```
162//!
163//! Of course, using [`io::stdout`] directly is less common than something like
164//! [`println!`].
165//!
166//! ## Iterator types
167//!
168//! A large number of the structures provided by `std::io` are for various
169//! ways of iterating over I/O. For example, [`Lines`] is used to split over
170//! lines:
171//!
172//! ```no_run
173//! use std::io;
174//! use std::io::prelude::*;
175//! use std::io::BufReader;
176//! use std::fs::File;
177//!
178//! fn main() -> io::Result<()> {
179//!     let f = File::open("foo.txt")?;
180//!     let reader = BufReader::new(f);
181//!
182//!     for line in reader.lines() {
183//!         println!("{}", line?);
184//!     }
185//!     Ok(())
186//! }
187//! ```
188//!
189//! ## Functions
190//!
191//! There are a number of [functions][functions-list] that offer access to various
192//! features. For example, we can use three of these functions to copy everything
193//! from standard input to standard output:
194//!
195//! ```no_run
196//! use std::io;
197//!
198//! fn main() -> io::Result<()> {
199//!     io::copy(&mut io::stdin(), &mut io::stdout())?;
200//!     Ok(())
201//! }
202//! ```
203//!
204//! [functions-list]: #functions-1
205//!
206//! ## io::Result
207//!
208//! Last, but certainly not least, is [`io::Result`]. This type is used
209//! as the return type of many `std::io` functions that can cause an error, and
210//! can be returned from your own functions as well. Many of the examples in this
211//! module use the [`?` operator]:
212//!
213//! ```
214//! use std::io;
215//!
216//! fn read_input() -> io::Result<()> {
217//!     let mut input = String::new();
218//!
219//!     io::stdin().read_line(&mut input)?;
220//!
221//!     println!("You typed: {}", input.trim());
222//!
223//!     Ok(())
224//! }
225//! ```
226//!
227//! The return type of `read_input()`, [`io::Result<()>`][`io::Result`], is a very
228//! common type for functions which don't have a 'real' return value, but do want to
229//! return errors if they happen. In this case, the only purpose of this function is
230//! to read the line and print it, so we use `()`.
231//!
232//! ## Platform-specific behavior
233//!
234//! Many I/O functions throughout the standard library are documented to indicate
235//! what various library or syscalls they are delegated to. This is done to help
236//! applications both understand what's happening under the hood as well as investigate
237//! any possibly unclear semantics. Note, however, that this is informative, not a binding
238//! contract. The implementation of many of these functions are subject to change over
239//! time and may call fewer or more syscalls/library functions.
240//!
241//! ## I/O Safety
242//!
243//! Rust follows an I/O safety discipline that is comparable to its memory safety discipline. This
244//! means that file descriptors can be *exclusively owned*. (Here, "file descriptor" is meant to
245//! subsume similar concepts that exist across a wide range of operating systems even if they might
246//! use a different name, such as "handle".) An exclusively owned file descriptor is one that no
247//! other code is allowed to access in any way, but the owner is allowed to access and even close
248//! it any time. A type that owns its file descriptor should usually close it in its `drop`
249//! function. Types like [`File`] own their file descriptor. Similarly, file descriptors
250//! can be *borrowed*, granting the temporary right to perform operations on this file descriptor.
251//! This indicates that the file descriptor will not be closed for the lifetime of the borrow, but
252//! it does *not* imply any right to close this file descriptor, since it will likely be owned by
253//! someone else.
254//!
255//! The platform-specific parts of the Rust standard library expose types that reflect these
256//! concepts, see [`os::unix`] and [`os::windows`].
257//!
258//! To uphold I/O safety, it is crucial that no code acts on file descriptors it does not own or
259//! borrow, and no code closes file descriptors it does not own. In other words, a safe function
260//! that takes a regular integer, treats it as a file descriptor, and acts on it, is *unsound*.
261//!
262//! Not upholding I/O safety and acting on a file descriptor without proof of ownership can lead to
263//! misbehavior and even Undefined Behavior in code that relies on ownership of its file
264//! descriptors: a closed file descriptor could be re-allocated, so the original owner of that file
265//! descriptor is now working on the wrong file. Some code might even rely on fully encapsulating
266//! its file descriptors with no operations being performed by any other part of the program.
267//!
268//! Note that exclusive ownership of a file descriptor does *not* imply exclusive ownership of the
269//! underlying kernel object that the file descriptor references (also called "open file description" on
270//! some operating systems). File descriptors basically work like [`Arc`]: when you receive an owned
271//! file descriptor, you cannot know whether there are any other file descriptors that reference the
272//! same kernel object. However, when you create a new kernel object, you know that you are holding
273//! the only reference to it. Just be careful not to lend it to anyone, since they can obtain a
274//! clone and then you can no longer know what the reference count is! In that sense, [`OwnedFd`] is
275//! like `Arc` and [`BorrowedFd<'a>`] is like `&'a Arc` (and similar for the Windows types). In
276//! particular, given a `BorrowedFd<'a>`, you are not allowed to close the file descriptor -- just
277//! like how, given a `&'a Arc`, you are not allowed to decrement the reference count and
278//! potentially free the underlying object. There is no equivalent to `Box` for file descriptors in
279//! the standard library (that would be a type that guarantees that the reference count is `1`),
280//! however, it would be possible for a crate to define a type with those semantics.
281//!
282//! [`File`]: crate::fs::File
283//! [`TcpStream`]: crate::net::TcpStream
284//! [`io::stdout`]: stdout
285//! [`io::Result`]: self::Result
286//! [`?` operator]: ../../book/appendix-02-operators.html
287//! [`Result`]: crate::result::Result
288//! [`.unwrap()`]: crate::result::Result::unwrap
289//! [`os::unix`]: ../os/unix/io/index.html
290//! [`os::windows`]: ../os/windows/io/index.html
291//! [`OwnedFd`]: ../os/fd/struct.OwnedFd.html
292//! [`BorrowedFd<'a>`]: ../os/fd/struct.BorrowedFd.html
293//! [`Arc`]: crate::sync::Arc
294
295#![stable(feature = "rust1", since = "1.0.0")]
296
297#[cfg(test)]
298mod tests;
299
300#[unstable(feature = "read_buf", issue = "78485")]
301pub use core::io::{BorrowedBuf, BorrowedCursor};
302use core::slice::memchr;
303
304#[stable(feature = "bufwriter_into_parts", since = "1.56.0")]
305pub use self::buffered::WriterPanicked;
306#[unstable(feature = "raw_os_error_ty", issue = "107792")]
307pub use self::error::RawOsError;
308#[doc(hidden)]
309#[unstable(feature = "io_const_error_internals", issue = "none")]
310pub use self::error::SimpleMessage;
311#[unstable(feature = "io_const_error", issue = "133448")]
312pub use self::error::const_error;
313#[stable(feature = "anonymous_pipe", since = "1.87.0")]
314pub use self::pipe::{PipeReader, PipeWriter, pipe};
315#[stable(feature = "is_terminal", since = "1.70.0")]
316pub use self::stdio::IsTerminal;
317pub(crate) use self::stdio::attempt_print_to_stderr;
318#[unstable(feature = "print_internals", issue = "none")]
319#[doc(hidden)]
320pub use self::stdio::{_eprint, _print};
321#[unstable(feature = "internal_output_capture", issue = "none")]
322#[doc(no_inline, hidden)]
323pub use self::stdio::{set_output_capture, try_set_output_capture};
324#[stable(feature = "rust1", since = "1.0.0")]
325pub use self::{
326    buffered::{BufReader, BufWriter, IntoInnerError, LineWriter},
327    copy::copy,
328    cursor::Cursor,
329    error::{Error, ErrorKind, Result},
330    stdio::{Stderr, StderrLock, Stdin, StdinLock, Stdout, StdoutLock, stderr, stdin, stdout},
331    util::{Empty, Repeat, Sink, empty, repeat, sink},
332};
333use crate::mem::{MaybeUninit, take};
334use crate::ops::{Deref, DerefMut};
335use crate::{cmp, fmt, slice, str, sys};
336
337mod buffered;
338pub(crate) mod copy;
339mod cursor;
340mod error;
341mod impls;
342mod pipe;
343pub mod prelude;
344mod stdio;
345mod util;
346
347const DEFAULT_BUF_SIZE: usize = crate::sys::io::DEFAULT_BUF_SIZE;
348
349pub(crate) use stdio::cleanup;
350
351struct Guard<'a> {
352    buf: &'a mut Vec<u8>,
353    len: usize,
354}
355
356impl Drop for Guard<'_> {
357    fn drop(&mut self) {
358        unsafe {
359            self.buf.set_len(self.len);
360        }
361    }
362}
363
364// Several `read_to_string` and `read_line` methods in the standard library will
365// append data into a `String` buffer, but we need to be pretty careful when
366// doing this. The implementation will just call `.as_mut_vec()` and then
367// delegate to a byte-oriented reading method, but we must ensure that when
368// returning we never leave `buf` in a state such that it contains invalid UTF-8
369// in its bounds.
370//
371// To this end, we use an RAII guard (to protect against panics) which updates
372// the length of the string when it is dropped. This guard initially truncates
373// the string to the prior length and only after we've validated that the
374// new contents are valid UTF-8 do we allow it to set a longer length.
375//
376// The unsafety in this function is twofold:
377//
378// 1. We're looking at the raw bytes of `buf`, so we take on the burden of UTF-8
379//    checks.
380// 2. We're passing a raw buffer to the function `f`, and it is expected that
381//    the function only *appends* bytes to the buffer. We'll get undefined
382//    behavior if existing bytes are overwritten to have non-UTF-8 data.
383pub(crate) unsafe fn append_to_string<F>(buf: &mut String, f: F) -> Result<usize>
384where
385    F: FnOnce(&mut Vec<u8>) -> Result<usize>,
386{
387    let mut g = Guard { len: buf.len(), buf: unsafe { buf.as_mut_vec() } };
388    let ret = f(g.buf);
389
390    // SAFETY: the caller promises to only append data to `buf`
391    let appended = unsafe { g.buf.get_unchecked(g.len..) };
392    if str::from_utf8(appended).is_err() {
393        ret.and_then(|_| Err(Error::INVALID_UTF8))
394    } else {
395        g.len = g.buf.len();
396        ret
397    }
398}
399
400// Here we must serve many masters with conflicting goals:
401//
402// - avoid allocating unless necessary
403// - avoid overallocating if we know the exact size (#89165)
404// - avoid passing large buffers to readers that always initialize the free capacity if they perform short reads (#23815, #23820)
405// - pass large buffers to readers that do not initialize the spare capacity. this can amortize per-call overheads
406// - and finally pass not-too-small and not-too-large buffers to Windows read APIs because they manage to suffer from both problems
407//   at the same time, i.e. small reads suffer from syscall overhead, all reads incur costs proportional to buffer size (#110650)
408//
409pub(crate) fn default_read_to_end<R: Read + ?Sized>(
410    r: &mut R,
411    buf: &mut Vec<u8>,
412    size_hint: Option<usize>,
413) -> Result<usize> {
414    let start_len = buf.len();
415    let start_cap = buf.capacity();
416    // Optionally limit the maximum bytes read on each iteration.
417    // This adds an arbitrary fiddle factor to allow for more data than we expect.
418    let mut max_read_size = size_hint
419        .and_then(|s| s.checked_add(1024)?.checked_next_multiple_of(DEFAULT_BUF_SIZE))
420        .unwrap_or(DEFAULT_BUF_SIZE);
421
422    let mut initialized = 0; // Extra initialized bytes from previous loop iteration
423
424    const PROBE_SIZE: usize = 32;
425
426    fn small_probe_read<R: Read + ?Sized>(r: &mut R, buf: &mut Vec<u8>) -> Result<usize> {
427        let mut probe = [0u8; PROBE_SIZE];
428
429        loop {
430            match r.read(&mut probe) {
431                Ok(n) => {
432                    // there is no way to recover from allocation failure here
433                    // because the data has already been read.
434                    buf.extend_from_slice(&probe[..n]);
435                    return Ok(n);
436                }
437                Err(ref e) if e.is_interrupted() => continue,
438                Err(e) => return Err(e),
439            }
440        }
441    }
442
443    // avoid inflating empty/small vecs before we have determined that there's anything to read
444    if (size_hint.is_none() || size_hint == Some(0)) && buf.capacity() - buf.len() < PROBE_SIZE {
445        let read = small_probe_read(r, buf)?;
446
447        if read == 0 {
448            return Ok(0);
449        }
450    }
451
452    let mut consecutive_short_reads = 0;
453
454    loop {
455        if buf.len() == buf.capacity() && buf.capacity() == start_cap {
456            // The buffer might be an exact fit. Let's read into a probe buffer
457            // and see if it returns `Ok(0)`. If so, we've avoided an
458            // unnecessary doubling of the capacity. But if not, append the
459            // probe buffer to the primary buffer and let its capacity grow.
460            let read = small_probe_read(r, buf)?;
461
462            if read == 0 {
463                return Ok(buf.len() - start_len);
464            }
465        }
466
467        if buf.len() == buf.capacity() {
468            // buf is full, need more space
469            buf.try_reserve(PROBE_SIZE)?;
470        }
471
472        let mut spare = buf.spare_capacity_mut();
473        let buf_len = cmp::min(spare.len(), max_read_size);
474        spare = &mut spare[..buf_len];
475        let mut read_buf: BorrowedBuf<'_> = spare.into();
476
477        // SAFETY: These bytes were initialized but not filled in the previous loop
478        unsafe {
479            read_buf.set_init(initialized);
480        }
481
482        let mut cursor = read_buf.unfilled();
483        let result = loop {
484            match r.read_buf(cursor.reborrow()) {
485                Err(e) if e.is_interrupted() => continue,
486                // Do not stop now in case of error: we might have received both data
487                // and an error
488                res => break res,
489            }
490        };
491
492        let unfilled_but_initialized = cursor.init_mut().len();
493        let bytes_read = cursor.written();
494        let was_fully_initialized = read_buf.init_len() == buf_len;
495
496        // SAFETY: BorrowedBuf's invariants mean this much memory is initialized.
497        unsafe {
498            let new_len = bytes_read + buf.len();
499            buf.set_len(new_len);
500        }
501
502        // Now that all data is pushed to the vector, we can fail without data loss
503        result?;
504
505        if bytes_read == 0 {
506            return Ok(buf.len() - start_len);
507        }
508
509        if bytes_read < buf_len {
510            consecutive_short_reads += 1;
511        } else {
512            consecutive_short_reads = 0;
513        }
514
515        // store how much was initialized but not filled
516        initialized = unfilled_but_initialized;
517
518        // Use heuristics to determine the max read size if no initial size hint was provided
519        if size_hint.is_none() {
520            // The reader is returning short reads but it doesn't call ensure_init().
521            // In that case we no longer need to restrict read sizes to avoid
522            // initialization costs.
523            // When reading from disk we usually don't get any short reads except at EOF.
524            // So we wait for at least 2 short reads before uncapping the read buffer;
525            // this helps with the Windows issue.
526            if !was_fully_initialized && consecutive_short_reads > 1 {
527                max_read_size = usize::MAX;
528            }
529
530            // we have passed a larger buffer than previously and the
531            // reader still hasn't returned a short read
532            if buf_len >= max_read_size && bytes_read == buf_len {
533                max_read_size = max_read_size.saturating_mul(2);
534            }
535        }
536    }
537}
538
539pub(crate) fn default_read_to_string<R: Read + ?Sized>(
540    r: &mut R,
541    buf: &mut String,
542    size_hint: Option<usize>,
543) -> Result<usize> {
544    // Note that we do *not* call `r.read_to_end()` here. We are passing
545    // `&mut Vec<u8>` (the raw contents of `buf`) into the `read_to_end`
546    // method to fill it up. An arbitrary implementation could overwrite the
547    // entire contents of the vector, not just append to it (which is what
548    // we are expecting).
549    //
550    // To prevent extraneously checking the UTF-8-ness of the entire buffer
551    // we pass it to our hardcoded `default_read_to_end` implementation which
552    // we know is guaranteed to only read data into the end of the buffer.
553    unsafe { append_to_string(buf, |b| default_read_to_end(r, b, size_hint)) }
554}
555
556pub(crate) fn default_read_vectored<F>(read: F, bufs: &mut [IoSliceMut<'_>]) -> Result<usize>
557where
558    F: FnOnce(&mut [u8]) -> Result<usize>,
559{
560    let buf = bufs.iter_mut().find(|b| !b.is_empty()).map_or(&mut [][..], |b| &mut **b);
561    read(buf)
562}
563
564pub(crate) fn default_write_vectored<F>(write: F, bufs: &[IoSlice<'_>]) -> Result<usize>
565where
566    F: FnOnce(&[u8]) -> Result<usize>,
567{
568    let buf = bufs.iter().find(|b| !b.is_empty()).map_or(&[][..], |b| &**b);
569    write(buf)
570}
571
572pub(crate) fn default_read_exact<R: Read + ?Sized>(this: &mut R, mut buf: &mut [u8]) -> Result<()> {
573    while !buf.is_empty() {
574        match this.read(buf) {
575            Ok(0) => break,
576            Ok(n) => {
577                buf = &mut buf[n..];
578            }
579            Err(ref e) if e.is_interrupted() => {}
580            Err(e) => return Err(e),
581        }
582    }
583    if !buf.is_empty() { Err(Error::READ_EXACT_EOF) } else { Ok(()) }
584}
585
586pub(crate) fn default_read_buf<F>(read: F, mut cursor: BorrowedCursor<'_>) -> Result<()>
587where
588    F: FnOnce(&mut [u8]) -> Result<usize>,
589{
590    let n = read(cursor.ensure_init().init_mut())?;
591    cursor.advance(n);
592    Ok(())
593}
594
595pub(crate) fn default_read_buf_exact<R: Read + ?Sized>(
596    this: &mut R,
597    mut cursor: BorrowedCursor<'_>,
598) -> Result<()> {
599    while cursor.capacity() > 0 {
600        let prev_written = cursor.written();
601        match this.read_buf(cursor.reborrow()) {
602            Ok(()) => {}
603            Err(e) if e.is_interrupted() => continue,
604            Err(e) => return Err(e),
605        }
606
607        if cursor.written() == prev_written {
608            return Err(Error::READ_EXACT_EOF);
609        }
610    }
611
612    Ok(())
613}
614
615pub(crate) fn default_write_fmt<W: Write + ?Sized>(
616    this: &mut W,
617    args: fmt::Arguments<'_>,
618) -> Result<()> {
619    // Create a shim which translates a `Write` to a `fmt::Write` and saves off
620    // I/O errors, instead of discarding them.
621    struct Adapter<'a, T: ?Sized + 'a> {
622        inner: &'a mut T,
623        error: Result<()>,
624    }
625
626    impl<T: Write + ?Sized> fmt::Write for Adapter<'_, T> {
627        fn write_str(&mut self, s: &str) -> fmt::Result {
628            match self.inner.write_all(s.as_bytes()) {
629                Ok(()) => Ok(()),
630                Err(e) => {
631                    self.error = Err(e);
632                    Err(fmt::Error)
633                }
634            }
635        }
636    }
637
638    let mut output = Adapter { inner: this, error: Ok(()) };
639    match fmt::write(&mut output, args) {
640        Ok(()) => Ok(()),
641        Err(..) => {
642            // Check whether the error came from the underlying `Write`.
643            if output.error.is_err() {
644                output.error
645            } else {
646                // This shouldn't happen: the underlying stream did not error,
647                // but somehow the formatter still errored?
648                panic!(
649                    "a formatting trait implementation returned an error when the underlying stream did not"
650                );
651            }
652        }
653    }
654}
655
656/// The `Read` trait allows for reading bytes from a source.
657///
658/// Implementors of the `Read` trait are called 'readers'.
659///
660/// Readers are defined by one required method, [`read()`]. Each call to [`read()`]
661/// will attempt to pull bytes from this source into a provided buffer. A
662/// number of other methods are implemented in terms of [`read()`], giving
663/// implementors a number of ways to read bytes while only needing to implement
664/// a single method.
665///
666/// Readers are intended to be composable with one another. Many implementors
667/// throughout [`std::io`] take and provide types which implement the `Read`
668/// trait.
669///
670/// Please note that each call to [`read()`] may involve a system call, and
671/// therefore, using something that implements [`BufRead`], such as
672/// [`BufReader`], will be more efficient.
673///
674/// Repeated calls to the reader use the same cursor, so for example
675/// calling `read_to_end` twice on a [`File`] will only return the file's
676/// contents once. It's recommended to first call `rewind()` in that case.
677///
678/// # Examples
679///
680/// [`File`]s implement `Read`:
681///
682/// ```no_run
683/// use std::io;
684/// use std::io::prelude::*;
685/// use std::fs::File;
686///
687/// fn main() -> io::Result<()> {
688///     let mut f = File::open("foo.txt")?;
689///     let mut buffer = [0; 10];
690///
691///     // read up to 10 bytes
692///     f.read(&mut buffer)?;
693///
694///     let mut buffer = Vec::new();
695///     // read the whole file
696///     f.read_to_end(&mut buffer)?;
697///
698///     // read into a String, so that you don't need to do the conversion.
699///     let mut buffer = String::new();
700///     f.read_to_string(&mut buffer)?;
701///
702///     // and more! See the other methods for more details.
703///     Ok(())
704/// }
705/// ```
706///
707/// Read from [`&str`] because [`&[u8]`][prim@slice] implements `Read`:
708///
709/// ```no_run
710/// # use std::io;
711/// use std::io::prelude::*;
712///
713/// fn main() -> io::Result<()> {
714///     let mut b = "This string will be read".as_bytes();
715///     let mut buffer = [0; 10];
716///
717///     // read up to 10 bytes
718///     b.read(&mut buffer)?;
719///
720///     // etc... it works exactly as a File does!
721///     Ok(())
722/// }
723/// ```
724///
725/// [`read()`]: Read::read
726/// [`&str`]: prim@str
727/// [`std::io`]: self
728/// [`File`]: crate::fs::File
729#[stable(feature = "rust1", since = "1.0.0")]
730#[doc(notable_trait)]
731#[cfg_attr(not(test), rustc_diagnostic_item = "IoRead")]
732pub trait Read {
733    /// Pull some bytes from this source into the specified buffer, returning
734    /// how many bytes were read.
735    ///
736    /// This function does not provide any guarantees about whether it blocks
737    /// waiting for data, but if an object needs to block for a read and cannot,
738    /// it will typically signal this via an [`Err`] return value.
739    ///
740    /// If the return value of this method is [`Ok(n)`], then implementations must
741    /// guarantee that `0 <= n <= buf.len()`. A nonzero `n` value indicates
742    /// that the buffer `buf` has been filled in with `n` bytes of data from this
743    /// source. If `n` is `0`, then it can indicate one of two scenarios:
744    ///
745    /// 1. This reader has reached its "end of file" and will likely no longer
746    ///    be able to produce bytes. Note that this does not mean that the
747    ///    reader will *always* no longer be able to produce bytes. As an example,
748    ///    on Linux, this method will call the `recv` syscall for a [`TcpStream`],
749    ///    where returning zero indicates the connection was shut down correctly. While
750    ///    for [`File`], it is possible to reach the end of file and get zero as result,
751    ///    but if more data is appended to the file, future calls to `read` will return
752    ///    more data.
753    /// 2. The buffer specified was 0 bytes in length.
754    ///
755    /// It is not an error if the returned value `n` is smaller than the buffer size,
756    /// even when the reader is not at the end of the stream yet.
757    /// This may happen for example because fewer bytes are actually available right now
758    /// (e. g. being close to end-of-file) or because read() was interrupted by a signal.
759    ///
760    /// As this trait is safe to implement, callers in unsafe code cannot rely on
761    /// `n <= buf.len()` for safety.
762    /// Extra care needs to be taken when `unsafe` functions are used to access the read bytes.
763    /// Callers have to ensure that no unchecked out-of-bounds accesses are possible even if
764    /// `n > buf.len()`.
765    ///
766    /// *Implementations* of this method can make no assumptions about the contents of `buf` when
767    /// this function is called. It is recommended that implementations only write data to `buf`
768    /// instead of reading its contents.
769    ///
770    /// Correspondingly, however, *callers* of this method in unsafe code must not assume
771    /// any guarantees about how the implementation uses `buf`. The trait is safe to implement,
772    /// so it is possible that the code that's supposed to write to the buffer might also read
773    /// from it. It is your responsibility to make sure that `buf` is initialized
774    /// before calling `read`. Calling `read` with an uninitialized `buf` (of the kind one
775    /// obtains via [`MaybeUninit<T>`]) is not safe, and can lead to undefined behavior.
776    ///
777    /// [`MaybeUninit<T>`]: crate::mem::MaybeUninit
778    ///
779    /// # Errors
780    ///
781    /// If this function encounters any form of I/O or other error, an error
782    /// variant will be returned. If an error is returned then it must be
783    /// guaranteed that no bytes were read.
784    ///
785    /// An error of the [`ErrorKind::Interrupted`] kind is non-fatal and the read
786    /// operation should be retried if there is nothing else to do.
787    ///
788    /// # Examples
789    ///
790    /// [`File`]s implement `Read`:
791    ///
792    /// [`Ok(n)`]: Ok
793    /// [`File`]: crate::fs::File
794    /// [`TcpStream`]: crate::net::TcpStream
795    ///
796    /// ```no_run
797    /// use std::io;
798    /// use std::io::prelude::*;
799    /// use std::fs::File;
800    ///
801    /// fn main() -> io::Result<()> {
802    ///     let mut f = File::open("foo.txt")?;
803    ///     let mut buffer = [0; 10];
804    ///
805    ///     // read up to 10 bytes
806    ///     let n = f.read(&mut buffer[..])?;
807    ///
808    ///     println!("The bytes: {:?}", &buffer[..n]);
809    ///     Ok(())
810    /// }
811    /// ```
812    #[stable(feature = "rust1", since = "1.0.0")]
813    fn read(&mut self, buf: &mut [u8]) -> Result<usize>;
814
815    /// Like `read`, except that it reads into a slice of buffers.
816    ///
817    /// Data is copied to fill each buffer in order, with the final buffer
818    /// written to possibly being only partially filled. This method must
819    /// behave equivalently to a single call to `read` with concatenated
820    /// buffers.
821    ///
822    /// The default implementation calls `read` with either the first nonempty
823    /// buffer provided, or an empty one if none exists.
824    #[stable(feature = "iovec", since = "1.36.0")]
825    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> Result<usize> {
826        default_read_vectored(|b| self.read(b), bufs)
827    }
828
829    /// Determines if this `Read`er has an efficient `read_vectored`
830    /// implementation.
831    ///
832    /// If a `Read`er does not override the default `read_vectored`
833    /// implementation, code using it may want to avoid the method all together
834    /// and coalesce writes into a single buffer for higher performance.
835    ///
836    /// The default implementation returns `false`.
837    #[unstable(feature = "can_vector", issue = "69941")]
838    fn is_read_vectored(&self) -> bool {
839        false
840    }
841
842    /// Reads all bytes until EOF in this source, placing them into `buf`.
843    ///
844    /// All bytes read from this source will be appended to the specified buffer
845    /// `buf`. This function will continuously call [`read()`] to append more data to
846    /// `buf` until [`read()`] returns either [`Ok(0)`] or an error of
847    /// non-[`ErrorKind::Interrupted`] kind.
848    ///
849    /// If successful, this function will return the total number of bytes read.
850    ///
851    /// # Errors
852    ///
853    /// If this function encounters an error of the kind
854    /// [`ErrorKind::Interrupted`] then the error is ignored and the operation
855    /// will continue.
856    ///
857    /// If any other read error is encountered then this function immediately
858    /// returns. Any bytes which have already been read will be appended to
859    /// `buf`.
860    ///
861    /// # Examples
862    ///
863    /// [`File`]s implement `Read`:
864    ///
865    /// [`read()`]: Read::read
866    /// [`Ok(0)`]: Ok
867    /// [`File`]: crate::fs::File
868    ///
869    /// ```no_run
870    /// use std::io;
871    /// use std::io::prelude::*;
872    /// use std::fs::File;
873    ///
874    /// fn main() -> io::Result<()> {
875    ///     let mut f = File::open("foo.txt")?;
876    ///     let mut buffer = Vec::new();
877    ///
878    ///     // read the whole file
879    ///     f.read_to_end(&mut buffer)?;
880    ///     Ok(())
881    /// }
882    /// ```
883    ///
884    /// (See also the [`std::fs::read`] convenience function for reading from a
885    /// file.)
886    ///
887    /// [`std::fs::read`]: crate::fs::read
888    ///
889    /// ## Implementing `read_to_end`
890    ///
891    /// When implementing the `io::Read` trait, it is recommended to allocate
892    /// memory using [`Vec::try_reserve`]. However, this behavior is not guaranteed
893    /// by all implementations, and `read_to_end` may not handle out-of-memory
894    /// situations gracefully.
895    ///
896    /// ```no_run
897    /// # use std::io::{self, BufRead};
898    /// # struct Example { example_datasource: io::Empty } impl Example {
899    /// # fn get_some_data_for_the_example(&self) -> &'static [u8] { &[] }
900    /// fn read_to_end(&mut self, dest_vec: &mut Vec<u8>) -> io::Result<usize> {
901    ///     let initial_vec_len = dest_vec.len();
902    ///     loop {
903    ///         let src_buf = self.example_datasource.fill_buf()?;
904    ///         if src_buf.is_empty() {
905    ///             break;
906    ///         }
907    ///         dest_vec.try_reserve(src_buf.len())?;
908    ///         dest_vec.extend_from_slice(src_buf);
909    ///
910    ///         // Any irreversible side effects should happen after `try_reserve` succeeds,
911    ///         // to avoid losing data on allocation error.
912    ///         let read = src_buf.len();
913    ///         self.example_datasource.consume(read);
914    ///     }
915    ///     Ok(dest_vec.len() - initial_vec_len)
916    /// }
917    /// # }
918    /// ```
919    ///
920    /// # Usage Notes
921    ///
922    /// `read_to_end` attempts to read a source until EOF, but many sources are continuous streams
923    /// that do not send EOF. In these cases, `read_to_end` will block indefinitely. Standard input
924    /// is one such stream which may be finite if piped, but is typically continuous. For example,
925    /// `cat file | my-rust-program` will correctly terminate with an `EOF` upon closure of cat.
926    /// Reading user input or running programs that remain open indefinitely will never terminate
927    /// the stream with `EOF` (e.g. `yes | my-rust-program`).
928    ///
929    /// Using `.lines()` with a [`BufReader`] or using [`read`] can provide a better solution
930    ///
931    ///[`read`]: Read::read
932    ///
933    /// [`Vec::try_reserve`]: crate::vec::Vec::try_reserve
934    #[stable(feature = "rust1", since = "1.0.0")]
935    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> Result<usize> {
936        default_read_to_end(self, buf, None)
937    }
938
939    /// Reads all bytes until EOF in this source, appending them to `buf`.
940    ///
941    /// If successful, this function returns the number of bytes which were read
942    /// and appended to `buf`.
943    ///
944    /// # Errors
945    ///
946    /// If the data in this stream is *not* valid UTF-8 then an error is
947    /// returned and `buf` is unchanged.
948    ///
949    /// See [`read_to_end`] for other error semantics.
950    ///
951    /// [`read_to_end`]: Read::read_to_end
952    ///
953    /// # Examples
954    ///
955    /// [`File`]s implement `Read`:
956    ///
957    /// [`File`]: crate::fs::File
958    ///
959    /// ```no_run
960    /// use std::io;
961    /// use std::io::prelude::*;
962    /// use std::fs::File;
963    ///
964    /// fn main() -> io::Result<()> {
965    ///     let mut f = File::open("foo.txt")?;
966    ///     let mut buffer = String::new();
967    ///
968    ///     f.read_to_string(&mut buffer)?;
969    ///     Ok(())
970    /// }
971    /// ```
972    ///
973    /// (See also the [`std::fs::read_to_string`] convenience function for
974    /// reading from a file.)
975    ///
976    /// # Usage Notes
977    ///
978    /// `read_to_string` attempts to read a source until EOF, but many sources are continuous streams
979    /// that do not send EOF. In these cases, `read_to_string` will block indefinitely. Standard input
980    /// is one such stream which may be finite if piped, but is typically continuous. For example,
981    /// `cat file | my-rust-program` will correctly terminate with an `EOF` upon closure of cat.
982    /// Reading user input or running programs that remain open indefinitely will never terminate
983    /// the stream with `EOF` (e.g. `yes | my-rust-program`).
984    ///
985    /// Using `.lines()` with a [`BufReader`] or using [`read`] can provide a better solution
986    ///
987    ///[`read`]: Read::read
988    ///
989    /// [`std::fs::read_to_string`]: crate::fs::read_to_string
990    #[stable(feature = "rust1", since = "1.0.0")]
991    fn read_to_string(&mut self, buf: &mut String) -> Result<usize> {
992        default_read_to_string(self, buf, None)
993    }
994
995    /// Reads the exact number of bytes required to fill `buf`.
996    ///
997    /// This function reads as many bytes as necessary to completely fill the
998    /// specified buffer `buf`.
999    ///
1000    /// *Implementations* of this method can make no assumptions about the contents of `buf` when
1001    /// this function is called. It is recommended that implementations only write data to `buf`
1002    /// instead of reading its contents. The documentation on [`read`] has a more detailed
1003    /// explanation of this subject.
1004    ///
1005    /// # Errors
1006    ///
1007    /// If this function encounters an error of the kind
1008    /// [`ErrorKind::Interrupted`] then the error is ignored and the operation
1009    /// will continue.
1010    ///
1011    /// If this function encounters an "end of file" before completely filling
1012    /// the buffer, it returns an error of the kind [`ErrorKind::UnexpectedEof`].
1013    /// The contents of `buf` are unspecified in this case.
1014    ///
1015    /// If any other read error is encountered then this function immediately
1016    /// returns. The contents of `buf` are unspecified in this case.
1017    ///
1018    /// If this function returns an error, it is unspecified how many bytes it
1019    /// has read, but it will never read more than would be necessary to
1020    /// completely fill the buffer.
1021    ///
1022    /// # Examples
1023    ///
1024    /// [`File`]s implement `Read`:
1025    ///
1026    /// [`read`]: Read::read
1027    /// [`File`]: crate::fs::File
1028    ///
1029    /// ```no_run
1030    /// use std::io;
1031    /// use std::io::prelude::*;
1032    /// use std::fs::File;
1033    ///
1034    /// fn main() -> io::Result<()> {
1035    ///     let mut f = File::open("foo.txt")?;
1036    ///     let mut buffer = [0; 10];
1037    ///
1038    ///     // read exactly 10 bytes
1039    ///     f.read_exact(&mut buffer)?;
1040    ///     Ok(())
1041    /// }
1042    /// ```
1043    #[stable(feature = "read_exact", since = "1.6.0")]
1044    fn read_exact(&mut self, buf: &mut [u8]) -> Result<()> {
1045        default_read_exact(self, buf)
1046    }
1047
1048    /// Pull some bytes from this source into the specified buffer.
1049    ///
1050    /// This is equivalent to the [`read`](Read::read) method, except that it is passed a [`BorrowedCursor`] rather than `[u8]` to allow use
1051    /// with uninitialized buffers. The new data will be appended to any existing contents of `buf`.
1052    ///
1053    /// The default implementation delegates to `read`.
1054    ///
1055    /// This method makes it possible to return both data and an error but it is advised against.
1056    #[unstable(feature = "read_buf", issue = "78485")]
1057    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> Result<()> {
1058        default_read_buf(|b| self.read(b), buf)
1059    }
1060
1061    /// Reads the exact number of bytes required to fill `cursor`.
1062    ///
1063    /// This is similar to the [`read_exact`](Read::read_exact) method, except
1064    /// that it is passed a [`BorrowedCursor`] rather than `[u8]` to allow use
1065    /// with uninitialized buffers.
1066    ///
1067    /// # Errors
1068    ///
1069    /// If this function encounters an error of the kind [`ErrorKind::Interrupted`]
1070    /// then the error is ignored and the operation will continue.
1071    ///
1072    /// If this function encounters an "end of file" before completely filling
1073    /// the buffer, it returns an error of the kind [`ErrorKind::UnexpectedEof`].
1074    ///
1075    /// If any other read error is encountered then this function immediately
1076    /// returns.
1077    ///
1078    /// If this function returns an error, all bytes read will be appended to `cursor`.
1079    #[unstable(feature = "read_buf", issue = "78485")]
1080    fn read_buf_exact(&mut self, cursor: BorrowedCursor<'_>) -> Result<()> {
1081        default_read_buf_exact(self, cursor)
1082    }
1083
1084    /// Creates a "by reference" adapter for this instance of `Read`.
1085    ///
1086    /// The returned adapter also implements `Read` and will simply borrow this
1087    /// current reader.
1088    ///
1089    /// # Examples
1090    ///
1091    /// [`File`]s implement `Read`:
1092    ///
1093    /// [`File`]: crate::fs::File
1094    ///
1095    /// ```no_run
1096    /// use std::io;
1097    /// use std::io::Read;
1098    /// use std::fs::File;
1099    ///
1100    /// fn main() -> io::Result<()> {
1101    ///     let mut f = File::open("foo.txt")?;
1102    ///     let mut buffer = Vec::new();
1103    ///     let mut other_buffer = Vec::new();
1104    ///
1105    ///     {
1106    ///         let reference = f.by_ref();
1107    ///
1108    ///         // read at most 5 bytes
1109    ///         reference.take(5).read_to_end(&mut buffer)?;
1110    ///
1111    ///     } // drop our &mut reference so we can use f again
1112    ///
1113    ///     // original file still usable, read the rest
1114    ///     f.read_to_end(&mut other_buffer)?;
1115    ///     Ok(())
1116    /// }
1117    /// ```
1118    #[stable(feature = "rust1", since = "1.0.0")]
1119    fn by_ref(&mut self) -> &mut Self
1120    where
1121        Self: Sized,
1122    {
1123        self
1124    }
1125
1126    /// Transforms this `Read` instance to an [`Iterator`] over its bytes.
1127    ///
1128    /// The returned type implements [`Iterator`] where the [`Item`] is
1129    /// <code>[Result]<[u8], [io::Error]></code>.
1130    /// The yielded item is [`Ok`] if a byte was successfully read and [`Err`]
1131    /// otherwise. EOF is mapped to returning [`None`] from this iterator.
1132    ///
1133    /// The default implementation calls `read` for each byte,
1134    /// which can be very inefficient for data that's not in memory,
1135    /// such as [`File`]. Consider using a [`BufReader`] in such cases.
1136    ///
1137    /// # Examples
1138    ///
1139    /// [`File`]s implement `Read`:
1140    ///
1141    /// [`Item`]: Iterator::Item
1142    /// [`File`]: crate::fs::File "fs::File"
1143    /// [Result]: crate::result::Result "Result"
1144    /// [io::Error]: self::Error "io::Error"
1145    ///
1146    /// ```no_run
1147    /// use std::io;
1148    /// use std::io::prelude::*;
1149    /// use std::io::BufReader;
1150    /// use std::fs::File;
1151    ///
1152    /// fn main() -> io::Result<()> {
1153    ///     let f = BufReader::new(File::open("foo.txt")?);
1154    ///
1155    ///     for byte in f.bytes() {
1156    ///         println!("{}", byte?);
1157    ///     }
1158    ///     Ok(())
1159    /// }
1160    /// ```
1161    #[stable(feature = "rust1", since = "1.0.0")]
1162    fn bytes(self) -> Bytes<Self>
1163    where
1164        Self: Sized,
1165    {
1166        Bytes { inner: self }
1167    }
1168
1169    /// Creates an adapter which will chain this stream with another.
1170    ///
1171    /// The returned `Read` instance will first read all bytes from this object
1172    /// until EOF is encountered. Afterwards the output is equivalent to the
1173    /// output of `next`.
1174    ///
1175    /// # Examples
1176    ///
1177    /// [`File`]s implement `Read`:
1178    ///
1179    /// [`File`]: crate::fs::File
1180    ///
1181    /// ```no_run
1182    /// use std::io;
1183    /// use std::io::prelude::*;
1184    /// use std::fs::File;
1185    ///
1186    /// fn main() -> io::Result<()> {
1187    ///     let f1 = File::open("foo.txt")?;
1188    ///     let f2 = File::open("bar.txt")?;
1189    ///
1190    ///     let mut handle = f1.chain(f2);
1191    ///     let mut buffer = String::new();
1192    ///
1193    ///     // read the value into a String. We could use any Read method here,
1194    ///     // this is just one example.
1195    ///     handle.read_to_string(&mut buffer)?;
1196    ///     Ok(())
1197    /// }
1198    /// ```
1199    #[stable(feature = "rust1", since = "1.0.0")]
1200    fn chain<R: Read>(self, next: R) -> Chain<Self, R>
1201    where
1202        Self: Sized,
1203    {
1204        Chain { first: self, second: next, done_first: false }
1205    }
1206
1207    /// Creates an adapter which will read at most `limit` bytes from it.
1208    ///
1209    /// This function returns a new instance of `Read` which will read at most
1210    /// `limit` bytes, after which it will always return EOF ([`Ok(0)`]). Any
1211    /// read errors will not count towards the number of bytes read and future
1212    /// calls to [`read()`] may succeed.
1213    ///
1214    /// # Examples
1215    ///
1216    /// [`File`]s implement `Read`:
1217    ///
1218    /// [`File`]: crate::fs::File
1219    /// [`Ok(0)`]: Ok
1220    /// [`read()`]: Read::read
1221    ///
1222    /// ```no_run
1223    /// use std::io;
1224    /// use std::io::prelude::*;
1225    /// use std::fs::File;
1226    ///
1227    /// fn main() -> io::Result<()> {
1228    ///     let f = File::open("foo.txt")?;
1229    ///     let mut buffer = [0; 5];
1230    ///
1231    ///     // read at most five bytes
1232    ///     let mut handle = f.take(5);
1233    ///
1234    ///     handle.read(&mut buffer)?;
1235    ///     Ok(())
1236    /// }
1237    /// ```
1238    #[stable(feature = "rust1", since = "1.0.0")]
1239    fn take(self, limit: u64) -> Take<Self>
1240    where
1241        Self: Sized,
1242    {
1243        Take { inner: self, len: limit, limit }
1244    }
1245
1246    /// Read and return a fixed array of bytes from this source.
1247    ///
1248    /// This function uses an array sized based on a const generic size known at compile time. You
1249    /// can specify the size with turbofish (`reader.read_array::<8>()`), or let type inference
1250    /// determine the number of bytes needed based on how the return value gets used. For instance,
1251    /// this function works well with functions like [`u64::from_le_bytes`] to turn an array of
1252    /// bytes into an integer of the same size.
1253    ///
1254    /// Like `read_exact`, if this function encounters an "end of file" before reading the desired
1255    /// number of bytes, it returns an error of the kind [`ErrorKind::UnexpectedEof`].
1256    ///
1257    /// ```
1258    /// #![feature(read_array)]
1259    /// use std::io::Cursor;
1260    /// use std::io::prelude::*;
1261    ///
1262    /// fn main() -> std::io::Result<()> {
1263    ///     let mut buf = Cursor::new([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2]);
1264    ///     let x = u64::from_le_bytes(buf.read_array()?);
1265    ///     let y = u32::from_be_bytes(buf.read_array()?);
1266    ///     let z = u16::from_be_bytes(buf.read_array()?);
1267    ///     assert_eq!(x, 0x807060504030201);
1268    ///     assert_eq!(y, 0x9080706);
1269    ///     assert_eq!(z, 0x504);
1270    ///     Ok(())
1271    /// }
1272    /// ```
1273    #[unstable(feature = "read_array", issue = "148848")]
1274    fn read_array<const N: usize>(&mut self) -> Result<[u8; N]>
1275    where
1276        Self: Sized,
1277    {
1278        let mut buf = [MaybeUninit::uninit(); N];
1279        let mut borrowed_buf = BorrowedBuf::from(buf.as_mut_slice());
1280        self.read_buf_exact(borrowed_buf.unfilled())?;
1281        // Guard against incorrect `read_buf_exact` implementations.
1282        assert_eq!(borrowed_buf.len(), N);
1283        Ok(unsafe { MaybeUninit::array_assume_init(buf) })
1284    }
1285}
1286
1287/// Reads all bytes from a [reader][Read] into a new [`String`].
1288///
1289/// This is a convenience function for [`Read::read_to_string`]. Using this
1290/// function avoids having to create a variable first and provides more type
1291/// safety since you can only get the buffer out if there were no errors. (If you
1292/// use [`Read::read_to_string`] you have to remember to check whether the read
1293/// succeeded because otherwise your buffer will be empty or only partially full.)
1294///
1295/// # Performance
1296///
1297/// The downside of this function's increased ease of use and type safety is
1298/// that it gives you less control over performance. For example, you can't
1299/// pre-allocate memory like you can using [`String::with_capacity`] and
1300/// [`Read::read_to_string`]. Also, you can't re-use the buffer if an error
1301/// occurs while reading.
1302///
1303/// In many cases, this function's performance will be adequate and the ease of use
1304/// and type safety tradeoffs will be worth it. However, there are cases where you
1305/// need more control over performance, and in those cases you should definitely use
1306/// [`Read::read_to_string`] directly.
1307///
1308/// Note that in some special cases, such as when reading files, this function will
1309/// pre-allocate memory based on the size of the input it is reading. In those
1310/// cases, the performance should be as good as if you had used
1311/// [`Read::read_to_string`] with a manually pre-allocated buffer.
1312///
1313/// # Errors
1314///
1315/// This function forces you to handle errors because the output (the `String`)
1316/// is wrapped in a [`Result`]. See [`Read::read_to_string`] for the errors
1317/// that can occur. If any error occurs, you will get an [`Err`], so you
1318/// don't have to worry about your buffer being empty or partially full.
1319///
1320/// # Examples
1321///
1322/// ```no_run
1323/// # use std::io;
1324/// fn main() -> io::Result<()> {
1325///     let stdin = io::read_to_string(io::stdin())?;
1326///     println!("Stdin was:");
1327///     println!("{stdin}");
1328///     Ok(())
1329/// }
1330/// ```
1331///
1332/// # Usage Notes
1333///
1334/// `read_to_string` attempts to read a source until EOF, but many sources are continuous streams
1335/// that do not send EOF. In these cases, `read_to_string` will block indefinitely. Standard input
1336/// is one such stream which may be finite if piped, but is typically continuous. For example,
1337/// `cat file | my-rust-program` will correctly terminate with an `EOF` upon closure of cat.
1338/// Reading user input or running programs that remain open indefinitely will never terminate
1339/// the stream with `EOF` (e.g. `yes | my-rust-program`).
1340///
1341/// Using `.lines()` with a [`BufReader`] or using [`read`] can provide a better solution
1342///
1343///[`read`]: Read::read
1344///
1345#[stable(feature = "io_read_to_string", since = "1.65.0")]
1346pub fn read_to_string<R: Read>(mut reader: R) -> Result<String> {
1347    let mut buf = String::new();
1348    reader.read_to_string(&mut buf)?;
1349    Ok(buf)
1350}
1351
1352/// A buffer type used with `Read::read_vectored`.
1353///
1354/// It is semantically a wrapper around a `&mut [u8]`, but is guaranteed to be
1355/// ABI compatible with the `iovec` type on Unix platforms and `WSABUF` on
1356/// Windows.
1357#[stable(feature = "iovec", since = "1.36.0")]
1358#[repr(transparent)]
1359pub struct IoSliceMut<'a>(sys::io::IoSliceMut<'a>);
1360
1361#[stable(feature = "iovec_send_sync", since = "1.44.0")]
1362unsafe impl<'a> Send for IoSliceMut<'a> {}
1363
1364#[stable(feature = "iovec_send_sync", since = "1.44.0")]
1365unsafe impl<'a> Sync for IoSliceMut<'a> {}
1366
1367#[stable(feature = "iovec", since = "1.36.0")]
1368impl<'a> fmt::Debug for IoSliceMut<'a> {
1369    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
1370        fmt::Debug::fmt(self.0.as_slice(), fmt)
1371    }
1372}
1373
1374impl<'a> IoSliceMut<'a> {
1375    /// Creates a new `IoSliceMut` wrapping a byte slice.
1376    ///
1377    /// # Panics
1378    ///
1379    /// Panics on Windows if the slice is larger than 4GB.
1380    #[stable(feature = "iovec", since = "1.36.0")]
1381    #[inline]
1382    pub fn new(buf: &'a mut [u8]) -> IoSliceMut<'a> {
1383        IoSliceMut(sys::io::IoSliceMut::new(buf))
1384    }
1385
1386    /// Advance the internal cursor of the slice.
1387    ///
1388    /// Also see [`IoSliceMut::advance_slices`] to advance the cursors of
1389    /// multiple buffers.
1390    ///
1391    /// # Panics
1392    ///
1393    /// Panics when trying to advance beyond the end of the slice.
1394    ///
1395    /// # Examples
1396    ///
1397    /// ```
1398    /// use std::io::IoSliceMut;
1399    /// use std::ops::Deref;
1400    ///
1401    /// let mut data = [1; 8];
1402    /// let mut buf = IoSliceMut::new(&mut data);
1403    ///
1404    /// // Mark 3 bytes as read.
1405    /// buf.advance(3);
1406    /// assert_eq!(buf.deref(), [1; 5].as_ref());
1407    /// ```
1408    #[stable(feature = "io_slice_advance", since = "1.81.0")]
1409    #[inline]
1410    pub fn advance(&mut self, n: usize) {
1411        self.0.advance(n)
1412    }
1413
1414    /// Advance a slice of slices.
1415    ///
1416    /// Shrinks the slice to remove any `IoSliceMut`s that are fully advanced over.
1417    /// If the cursor ends up in the middle of an `IoSliceMut`, it is modified
1418    /// to start at that cursor.
1419    ///
1420    /// For example, if we have a slice of two 8-byte `IoSliceMut`s, and we advance by 10 bytes,
1421    /// the result will only include the second `IoSliceMut`, advanced by 2 bytes.
1422    ///
1423    /// # Panics
1424    ///
1425    /// Panics when trying to advance beyond the end of the slices.
1426    ///
1427    /// # Examples
1428    ///
1429    /// ```
1430    /// use std::io::IoSliceMut;
1431    /// use std::ops::Deref;
1432    ///
1433    /// let mut buf1 = [1; 8];
1434    /// let mut buf2 = [2; 16];
1435    /// let mut buf3 = [3; 8];
1436    /// let mut bufs = &mut [
1437    ///     IoSliceMut::new(&mut buf1),
1438    ///     IoSliceMut::new(&mut buf2),
1439    ///     IoSliceMut::new(&mut buf3),
1440    /// ][..];
1441    ///
1442    /// // Mark 10 bytes as read.
1443    /// IoSliceMut::advance_slices(&mut bufs, 10);
1444    /// assert_eq!(bufs[0].deref(), [2; 14].as_ref());
1445    /// assert_eq!(bufs[1].deref(), [3; 8].as_ref());
1446    /// ```
1447    #[stable(feature = "io_slice_advance", since = "1.81.0")]
1448    #[inline]
1449    pub fn advance_slices(bufs: &mut &mut [IoSliceMut<'a>], n: usize) {
1450        // Number of buffers to remove.
1451        let mut remove = 0;
1452        // Remaining length before reaching n.
1453        let mut left = n;
1454        for buf in bufs.iter() {
1455            if let Some(remainder) = left.checked_sub(buf.len()) {
1456                left = remainder;
1457                remove += 1;
1458            } else {
1459                break;
1460            }
1461        }
1462
1463        *bufs = &mut take(bufs)[remove..];
1464        if bufs.is_empty() {
1465            assert!(left == 0, "advancing io slices beyond their length");
1466        } else {
1467            bufs[0].advance(left);
1468        }
1469    }
1470
1471    /// Get the underlying bytes as a mutable slice with the original lifetime.
1472    ///
1473    /// # Examples
1474    ///
1475    /// ```
1476    /// #![feature(io_slice_as_bytes)]
1477    /// use std::io::IoSliceMut;
1478    ///
1479    /// let mut data = *b"abcdef";
1480    /// let io_slice = IoSliceMut::new(&mut data);
1481    /// io_slice.into_slice()[0] = b'A';
1482    ///
1483    /// assert_eq!(&data, b"Abcdef");
1484    /// ```
1485    #[unstable(feature = "io_slice_as_bytes", issue = "132818")]
1486    pub const fn into_slice(self) -> &'a mut [u8] {
1487        self.0.into_slice()
1488    }
1489}
1490
1491#[stable(feature = "iovec", since = "1.36.0")]
1492impl<'a> Deref for IoSliceMut<'a> {
1493    type Target = [u8];
1494
1495    #[inline]
1496    fn deref(&self) -> &[u8] {
1497        self.0.as_slice()
1498    }
1499}
1500
1501#[stable(feature = "iovec", since = "1.36.0")]
1502impl<'a> DerefMut for IoSliceMut<'a> {
1503    #[inline]
1504    fn deref_mut(&mut self) -> &mut [u8] {
1505        self.0.as_mut_slice()
1506    }
1507}
1508
1509/// A buffer type used with `Write::write_vectored`.
1510///
1511/// It is semantically a wrapper around a `&[u8]`, but is guaranteed to be
1512/// ABI compatible with the `iovec` type on Unix platforms and `WSABUF` on
1513/// Windows.
1514#[stable(feature = "iovec", since = "1.36.0")]
1515#[derive(Copy, Clone)]
1516#[repr(transparent)]
1517pub struct IoSlice<'a>(sys::io::IoSlice<'a>);
1518
1519#[stable(feature = "iovec_send_sync", since = "1.44.0")]
1520unsafe impl<'a> Send for IoSlice<'a> {}
1521
1522#[stable(feature = "iovec_send_sync", since = "1.44.0")]
1523unsafe impl<'a> Sync for IoSlice<'a> {}
1524
1525#[stable(feature = "iovec", since = "1.36.0")]
1526impl<'a> fmt::Debug for IoSlice<'a> {
1527    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
1528        fmt::Debug::fmt(self.0.as_slice(), fmt)
1529    }
1530}
1531
1532impl<'a> IoSlice<'a> {
1533    /// Creates a new `IoSlice` wrapping a byte slice.
1534    ///
1535    /// # Panics
1536    ///
1537    /// Panics on Windows if the slice is larger than 4GB.
1538    #[stable(feature = "iovec", since = "1.36.0")]
1539    #[must_use]
1540    #[inline]
1541    pub fn new(buf: &'a [u8]) -> IoSlice<'a> {
1542        IoSlice(sys::io::IoSlice::new(buf))
1543    }
1544
1545    /// Advance the internal cursor of the slice.
1546    ///
1547    /// Also see [`IoSlice::advance_slices`] to advance the cursors of multiple
1548    /// buffers.
1549    ///
1550    /// # Panics
1551    ///
1552    /// Panics when trying to advance beyond the end of the slice.
1553    ///
1554    /// # Examples
1555    ///
1556    /// ```
1557    /// use std::io::IoSlice;
1558    /// use std::ops::Deref;
1559    ///
1560    /// let data = [1; 8];
1561    /// let mut buf = IoSlice::new(&data);
1562    ///
1563    /// // Mark 3 bytes as read.
1564    /// buf.advance(3);
1565    /// assert_eq!(buf.deref(), [1; 5].as_ref());
1566    /// ```
1567    #[stable(feature = "io_slice_advance", since = "1.81.0")]
1568    #[inline]
1569    pub fn advance(&mut self, n: usize) {
1570        self.0.advance(n)
1571    }
1572
1573    /// Advance a slice of slices.
1574    ///
1575    /// Shrinks the slice to remove any `IoSlice`s that are fully advanced over.
1576    /// If the cursor ends up in the middle of an `IoSlice`, it is modified
1577    /// to start at that cursor.
1578    ///
1579    /// For example, if we have a slice of two 8-byte `IoSlice`s, and we advance by 10 bytes,
1580    /// the result will only include the second `IoSlice`, advanced by 2 bytes.
1581    ///
1582    /// # Panics
1583    ///
1584    /// Panics when trying to advance beyond the end of the slices.
1585    ///
1586    /// # Examples
1587    ///
1588    /// ```
1589    /// use std::io::IoSlice;
1590    /// use std::ops::Deref;
1591    ///
1592    /// let buf1 = [1; 8];
1593    /// let buf2 = [2; 16];
1594    /// let buf3 = [3; 8];
1595    /// let mut bufs = &mut [
1596    ///     IoSlice::new(&buf1),
1597    ///     IoSlice::new(&buf2),
1598    ///     IoSlice::new(&buf3),
1599    /// ][..];
1600    ///
1601    /// // Mark 10 bytes as written.
1602    /// IoSlice::advance_slices(&mut bufs, 10);
1603    /// assert_eq!(bufs[0].deref(), [2; 14].as_ref());
1604    /// assert_eq!(bufs[1].deref(), [3; 8].as_ref());
1605    #[stable(feature = "io_slice_advance", since = "1.81.0")]
1606    #[inline]
1607    pub fn advance_slices(bufs: &mut &mut [IoSlice<'a>], n: usize) {
1608        // Number of buffers to remove.
1609        let mut remove = 0;
1610        // Remaining length before reaching n. This prevents overflow
1611        // that could happen if the length of slices in `bufs` were instead
1612        // accumulated. Those slice may be aliased and, if they are large
1613        // enough, their added length may overflow a `usize`.
1614        let mut left = n;
1615        for buf in bufs.iter() {
1616            if let Some(remainder) = left.checked_sub(buf.len()) {
1617                left = remainder;
1618                remove += 1;
1619            } else {
1620                break;
1621            }
1622        }
1623
1624        *bufs = &mut take(bufs)[remove..];
1625        if bufs.is_empty() {
1626            assert!(left == 0, "advancing io slices beyond their length");
1627        } else {
1628            bufs[0].advance(left);
1629        }
1630    }
1631
1632    /// Get the underlying bytes as a slice with the original lifetime.
1633    ///
1634    /// This doesn't borrow from `self`, so is less restrictive than calling
1635    /// `.deref()`, which does.
1636    ///
1637    /// # Examples
1638    ///
1639    /// ```
1640    /// #![feature(io_slice_as_bytes)]
1641    /// use std::io::IoSlice;
1642    ///
1643    /// let data = b"abcdef";
1644    ///
1645    /// let mut io_slice = IoSlice::new(data);
1646    /// let tail = &io_slice.as_slice()[3..];
1647    ///
1648    /// // This works because `tail` doesn't borrow `io_slice`
1649    /// io_slice = IoSlice::new(tail);
1650    ///
1651    /// assert_eq!(io_slice.as_slice(), b"def");
1652    /// ```
1653    #[unstable(feature = "io_slice_as_bytes", issue = "132818")]
1654    pub const fn as_slice(self) -> &'a [u8] {
1655        self.0.as_slice()
1656    }
1657}
1658
1659#[stable(feature = "iovec", since = "1.36.0")]
1660impl<'a> Deref for IoSlice<'a> {
1661    type Target = [u8];
1662
1663    #[inline]
1664    fn deref(&self) -> &[u8] {
1665        self.0.as_slice()
1666    }
1667}
1668
1669/// A trait for objects which are byte-oriented sinks.
1670///
1671/// Implementors of the `Write` trait are sometimes called 'writers'.
1672///
1673/// Writers are defined by two required methods, [`write`] and [`flush`]:
1674///
1675/// * The [`write`] method will attempt to write some data into the object,
1676///   returning how many bytes were successfully written.
1677///
1678/// * The [`flush`] method is useful for adapters and explicit buffers
1679///   themselves for ensuring that all buffered data has been pushed out to the
1680///   'true sink'.
1681///
1682/// Writers are intended to be composable with one another. Many implementors
1683/// throughout [`std::io`] take and provide types which implement the `Write`
1684/// trait.
1685///
1686/// [`write`]: Write::write
1687/// [`flush`]: Write::flush
1688/// [`std::io`]: self
1689///
1690/// # Examples
1691///
1692/// ```no_run
1693/// use std::io::prelude::*;
1694/// use std::fs::File;
1695///
1696/// fn main() -> std::io::Result<()> {
1697///     let data = b"some bytes";
1698///
1699///     let mut pos = 0;
1700///     let mut buffer = File::create("foo.txt")?;
1701///
1702///     while pos < data.len() {
1703///         let bytes_written = buffer.write(&data[pos..])?;
1704///         pos += bytes_written;
1705///     }
1706///     Ok(())
1707/// }
1708/// ```
1709///
1710/// The trait also provides convenience methods like [`write_all`], which calls
1711/// `write` in a loop until its entire input has been written.
1712///
1713/// [`write_all`]: Write::write_all
1714#[stable(feature = "rust1", since = "1.0.0")]
1715#[doc(notable_trait)]
1716#[cfg_attr(not(test), rustc_diagnostic_item = "IoWrite")]
1717pub trait Write {
1718    /// Writes a buffer into this writer, returning how many bytes were written.
1719    ///
1720    /// This function will attempt to write the entire contents of `buf`, but
1721    /// the entire write might not succeed, or the write may also generate an
1722    /// error. Typically, a call to `write` represents one attempt to write to
1723    /// any wrapped object.
1724    ///
1725    /// Calls to `write` are not guaranteed to block waiting for data to be
1726    /// written, and a write which would otherwise block can be indicated through
1727    /// an [`Err`] variant.
1728    ///
1729    /// If this method consumed `n > 0` bytes of `buf` it must return [`Ok(n)`].
1730    /// If the return value is `Ok(n)` then `n` must satisfy `n <= buf.len()`.
1731    /// A return value of `Ok(0)` typically means that the underlying object is
1732    /// no longer able to accept bytes and will likely not be able to in the
1733    /// future as well, or that the buffer provided is empty.
1734    ///
1735    /// # Errors
1736    ///
1737    /// Each call to `write` may generate an I/O error indicating that the
1738    /// operation could not be completed. If an error is returned then no bytes
1739    /// in the buffer were written to this writer.
1740    ///
1741    /// It is **not** considered an error if the entire buffer could not be
1742    /// written to this writer.
1743    ///
1744    /// An error of the [`ErrorKind::Interrupted`] kind is non-fatal and the
1745    /// write operation should be retried if there is nothing else to do.
1746    ///
1747    /// # Examples
1748    ///
1749    /// ```no_run
1750    /// use std::io::prelude::*;
1751    /// use std::fs::File;
1752    ///
1753    /// fn main() -> std::io::Result<()> {
1754    ///     let mut buffer = File::create("foo.txt")?;
1755    ///
1756    ///     // Writes some prefix of the byte string, not necessarily all of it.
1757    ///     buffer.write(b"some bytes")?;
1758    ///     Ok(())
1759    /// }
1760    /// ```
1761    ///
1762    /// [`Ok(n)`]: Ok
1763    #[stable(feature = "rust1", since = "1.0.0")]
1764    fn write(&mut self, buf: &[u8]) -> Result<usize>;
1765
1766    /// Like [`write`], except that it writes from a slice of buffers.
1767    ///
1768    /// Data is copied from each buffer in order, with the final buffer
1769    /// read from possibly being only partially consumed. This method must
1770    /// behave as a call to [`write`] with the buffers concatenated would.
1771    ///
1772    /// The default implementation calls [`write`] with either the first nonempty
1773    /// buffer provided, or an empty one if none exists.
1774    ///
1775    /// # Examples
1776    ///
1777    /// ```no_run
1778    /// use std::io::IoSlice;
1779    /// use std::io::prelude::*;
1780    /// use std::fs::File;
1781    ///
1782    /// fn main() -> std::io::Result<()> {
1783    ///     let data1 = [1; 8];
1784    ///     let data2 = [15; 8];
1785    ///     let io_slice1 = IoSlice::new(&data1);
1786    ///     let io_slice2 = IoSlice::new(&data2);
1787    ///
1788    ///     let mut buffer = File::create("foo.txt")?;
1789    ///
1790    ///     // Writes some prefix of the byte string, not necessarily all of it.
1791    ///     buffer.write_vectored(&[io_slice1, io_slice2])?;
1792    ///     Ok(())
1793    /// }
1794    /// ```
1795    ///
1796    /// [`write`]: Write::write
1797    #[stable(feature = "iovec", since = "1.36.0")]
1798    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> Result<usize> {
1799        default_write_vectored(|b| self.write(b), bufs)
1800    }
1801
1802    /// Determines if this `Write`r has an efficient [`write_vectored`]
1803    /// implementation.
1804    ///
1805    /// If a `Write`r does not override the default [`write_vectored`]
1806    /// implementation, code using it may want to avoid the method all together
1807    /// and coalesce writes into a single buffer for higher performance.
1808    ///
1809    /// The default implementation returns `false`.
1810    ///
1811    /// [`write_vectored`]: Write::write_vectored
1812    #[unstable(feature = "can_vector", issue = "69941")]
1813    fn is_write_vectored(&self) -> bool {
1814        false
1815    }
1816
1817    /// Flushes this output stream, ensuring that all intermediately buffered
1818    /// contents reach their destination.
1819    ///
1820    /// # Errors
1821    ///
1822    /// It is considered an error if not all bytes could be written due to
1823    /// I/O errors or EOF being reached.
1824    ///
1825    /// # Examples
1826    ///
1827    /// ```no_run
1828    /// use std::io::prelude::*;
1829    /// use std::io::BufWriter;
1830    /// use std::fs::File;
1831    ///
1832    /// fn main() -> std::io::Result<()> {
1833    ///     let mut buffer = BufWriter::new(File::create("foo.txt")?);
1834    ///
1835    ///     buffer.write_all(b"some bytes")?;
1836    ///     buffer.flush()?;
1837    ///     Ok(())
1838    /// }
1839    /// ```
1840    #[stable(feature = "rust1", since = "1.0.0")]
1841    fn flush(&mut self) -> Result<()>;
1842
1843    /// Attempts to write an entire buffer into this writer.
1844    ///
1845    /// This method will continuously call [`write`] until there is no more data
1846    /// to be written or an error of non-[`ErrorKind::Interrupted`] kind is
1847    /// returned. This method will not return until the entire buffer has been
1848    /// successfully written or such an error occurs. The first error that is
1849    /// not of [`ErrorKind::Interrupted`] kind generated from this method will be
1850    /// returned.
1851    ///
1852    /// If the buffer contains no data, this will never call [`write`].
1853    ///
1854    /// # Errors
1855    ///
1856    /// This function will return the first error of
1857    /// non-[`ErrorKind::Interrupted`] kind that [`write`] returns.
1858    ///
1859    /// [`write`]: Write::write
1860    ///
1861    /// # Examples
1862    ///
1863    /// ```no_run
1864    /// use std::io::prelude::*;
1865    /// use std::fs::File;
1866    ///
1867    /// fn main() -> std::io::Result<()> {
1868    ///     let mut buffer = File::create("foo.txt")?;
1869    ///
1870    ///     buffer.write_all(b"some bytes")?;
1871    ///     Ok(())
1872    /// }
1873    /// ```
1874    #[stable(feature = "rust1", since = "1.0.0")]
1875    fn write_all(&mut self, mut buf: &[u8]) -> Result<()> {
1876        while !buf.is_empty() {
1877            match self.write(buf) {
1878                Ok(0) => {
1879                    return Err(Error::WRITE_ALL_EOF);
1880                }
1881                Ok(n) => buf = &buf[n..],
1882                Err(ref e) if e.is_interrupted() => {}
1883                Err(e) => return Err(e),
1884            }
1885        }
1886        Ok(())
1887    }
1888
1889    /// Attempts to write multiple buffers into this writer.
1890    ///
1891    /// This method will continuously call [`write_vectored`] until there is no
1892    /// more data to be written or an error of non-[`ErrorKind::Interrupted`]
1893    /// kind is returned. This method will not return until all buffers have
1894    /// been successfully written or such an error occurs. The first error that
1895    /// is not of [`ErrorKind::Interrupted`] kind generated from this method
1896    /// will be returned.
1897    ///
1898    /// If the buffer contains no data, this will never call [`write_vectored`].
1899    ///
1900    /// # Notes
1901    ///
1902    /// Unlike [`write_vectored`], this takes a *mutable* reference to
1903    /// a slice of [`IoSlice`]s, not an immutable one. That's because we need to
1904    /// modify the slice to keep track of the bytes already written.
1905    ///
1906    /// Once this function returns, the contents of `bufs` are unspecified, as
1907    /// this depends on how many calls to [`write_vectored`] were necessary. It is
1908    /// best to understand this function as taking ownership of `bufs` and to
1909    /// not use `bufs` afterwards. The underlying buffers, to which the
1910    /// [`IoSlice`]s point (but not the [`IoSlice`]s themselves), are unchanged and
1911    /// can be reused.
1912    ///
1913    /// [`write_vectored`]: Write::write_vectored
1914    ///
1915    /// # Examples
1916    ///
1917    /// ```
1918    /// #![feature(write_all_vectored)]
1919    /// # fn main() -> std::io::Result<()> {
1920    ///
1921    /// use std::io::{Write, IoSlice};
1922    ///
1923    /// let mut writer = Vec::new();
1924    /// let bufs = &mut [
1925    ///     IoSlice::new(&[1]),
1926    ///     IoSlice::new(&[2, 3]),
1927    ///     IoSlice::new(&[4, 5, 6]),
1928    /// ];
1929    ///
1930    /// writer.write_all_vectored(bufs)?;
1931    /// // Note: the contents of `bufs` is now undefined, see the Notes section.
1932    ///
1933    /// assert_eq!(writer, &[1, 2, 3, 4, 5, 6]);
1934    /// # Ok(()) }
1935    /// ```
1936    #[unstable(feature = "write_all_vectored", issue = "70436")]
1937    fn write_all_vectored(&mut self, mut bufs: &mut [IoSlice<'_>]) -> Result<()> {
1938        // Guarantee that bufs is empty if it contains no data,
1939        // to avoid calling write_vectored if there is no data to be written.
1940        IoSlice::advance_slices(&mut bufs, 0);
1941        while !bufs.is_empty() {
1942            match self.write_vectored(bufs) {
1943                Ok(0) => {
1944                    return Err(Error::WRITE_ALL_EOF);
1945                }
1946                Ok(n) => IoSlice::advance_slices(&mut bufs, n),
1947                Err(ref e) if e.is_interrupted() => {}
1948                Err(e) => return Err(e),
1949            }
1950        }
1951        Ok(())
1952    }
1953
1954    /// Writes a formatted string into this writer, returning any error
1955    /// encountered.
1956    ///
1957    /// This method is primarily used to interface with the
1958    /// [`format_args!()`] macro, and it is rare that this should
1959    /// explicitly be called. The [`write!()`] macro should be favored to
1960    /// invoke this method instead.
1961    ///
1962    /// This function internally uses the [`write_all`] method on
1963    /// this trait and hence will continuously write data so long as no errors
1964    /// are received. This also means that partial writes are not indicated in
1965    /// this signature.
1966    ///
1967    /// [`write_all`]: Write::write_all
1968    ///
1969    /// # Errors
1970    ///
1971    /// This function will return any I/O error reported while formatting.
1972    ///
1973    /// # Examples
1974    ///
1975    /// ```no_run
1976    /// use std::io::prelude::*;
1977    /// use std::fs::File;
1978    ///
1979    /// fn main() -> std::io::Result<()> {
1980    ///     let mut buffer = File::create("foo.txt")?;
1981    ///
1982    ///     // this call
1983    ///     write!(buffer, "{:.*}", 2, 1.234567)?;
1984    ///     // turns into this:
1985    ///     buffer.write_fmt(format_args!("{:.*}", 2, 1.234567))?;
1986    ///     Ok(())
1987    /// }
1988    /// ```
1989    #[stable(feature = "rust1", since = "1.0.0")]
1990    fn write_fmt(&mut self, args: fmt::Arguments<'_>) -> Result<()> {
1991        if let Some(s) = args.as_statically_known_str() {
1992            self.write_all(s.as_bytes())
1993        } else {
1994            default_write_fmt(self, args)
1995        }
1996    }
1997
1998    /// Creates a "by reference" adapter for this instance of `Write`.
1999    ///
2000    /// The returned adapter also implements `Write` and will simply borrow this
2001    /// current writer.
2002    ///
2003    /// # Examples
2004    ///
2005    /// ```no_run
2006    /// use std::io::Write;
2007    /// use std::fs::File;
2008    ///
2009    /// fn main() -> std::io::Result<()> {
2010    ///     let mut buffer = File::create("foo.txt")?;
2011    ///
2012    ///     let reference = buffer.by_ref();
2013    ///
2014    ///     // we can use reference just like our original buffer
2015    ///     reference.write_all(b"some bytes")?;
2016    ///     Ok(())
2017    /// }
2018    /// ```
2019    #[stable(feature = "rust1", since = "1.0.0")]
2020    fn by_ref(&mut self) -> &mut Self
2021    where
2022        Self: Sized,
2023    {
2024        self
2025    }
2026}
2027
2028/// The `Seek` trait provides a cursor which can be moved within a stream of
2029/// bytes.
2030///
2031/// The stream typically has a fixed size, allowing seeking relative to either
2032/// end or the current offset.
2033///
2034/// # Examples
2035///
2036/// [`File`]s implement `Seek`:
2037///
2038/// [`File`]: crate::fs::File
2039///
2040/// ```no_run
2041/// use std::io;
2042/// use std::io::prelude::*;
2043/// use std::fs::File;
2044/// use std::io::SeekFrom;
2045///
2046/// fn main() -> io::Result<()> {
2047///     let mut f = File::open("foo.txt")?;
2048///
2049///     // move the cursor 42 bytes from the start of the file
2050///     f.seek(SeekFrom::Start(42))?;
2051///     Ok(())
2052/// }
2053/// ```
2054#[stable(feature = "rust1", since = "1.0.0")]
2055#[cfg_attr(not(test), rustc_diagnostic_item = "IoSeek")]
2056pub trait Seek {
2057    /// Seek to an offset, in bytes, in a stream.
2058    ///
2059    /// A seek beyond the end of a stream is allowed, but behavior is defined
2060    /// by the implementation.
2061    ///
2062    /// If the seek operation completed successfully,
2063    /// this method returns the new position from the start of the stream.
2064    /// That position can be used later with [`SeekFrom::Start`].
2065    ///
2066    /// # Errors
2067    ///
2068    /// Seeking can fail, for example because it might involve flushing a buffer.
2069    ///
2070    /// Seeking to a negative offset is considered an error.
2071    #[stable(feature = "rust1", since = "1.0.0")]
2072    fn seek(&mut self, pos: SeekFrom) -> Result<u64>;
2073
2074    /// Rewind to the beginning of a stream.
2075    ///
2076    /// This is a convenience method, equivalent to `seek(SeekFrom::Start(0))`.
2077    ///
2078    /// # Errors
2079    ///
2080    /// Rewinding can fail, for example because it might involve flushing a buffer.
2081    ///
2082    /// # Example
2083    ///
2084    /// ```no_run
2085    /// use std::io::{Read, Seek, Write};
2086    /// use std::fs::OpenOptions;
2087    ///
2088    /// let mut f = OpenOptions::new()
2089    ///     .write(true)
2090    ///     .read(true)
2091    ///     .create(true)
2092    ///     .open("foo.txt")?;
2093    ///
2094    /// let hello = "Hello!\n";
2095    /// write!(f, "{hello}")?;
2096    /// f.rewind()?;
2097    ///
2098    /// let mut buf = String::new();
2099    /// f.read_to_string(&mut buf)?;
2100    /// assert_eq!(&buf, hello);
2101    /// # std::io::Result::Ok(())
2102    /// ```
2103    #[stable(feature = "seek_rewind", since = "1.55.0")]
2104    fn rewind(&mut self) -> Result<()> {
2105        self.seek(SeekFrom::Start(0))?;
2106        Ok(())
2107    }
2108
2109    /// Returns the length of this stream (in bytes).
2110    ///
2111    /// The default implementation uses up to three seek operations. If this
2112    /// method returns successfully, the seek position is unchanged (i.e. the
2113    /// position before calling this method is the same as afterwards).
2114    /// However, if this method returns an error, the seek position is
2115    /// unspecified.
2116    ///
2117    /// If you need to obtain the length of *many* streams and you don't care
2118    /// about the seek position afterwards, you can reduce the number of seek
2119    /// operations by simply calling `seek(SeekFrom::End(0))` and using its
2120    /// return value (it is also the stream length).
2121    ///
2122    /// Note that length of a stream can change over time (for example, when
2123    /// data is appended to a file). So calling this method multiple times does
2124    /// not necessarily return the same length each time.
2125    ///
2126    /// # Example
2127    ///
2128    /// ```no_run
2129    /// #![feature(seek_stream_len)]
2130    /// use std::{
2131    ///     io::{self, Seek},
2132    ///     fs::File,
2133    /// };
2134    ///
2135    /// fn main() -> io::Result<()> {
2136    ///     let mut f = File::open("foo.txt")?;
2137    ///
2138    ///     let len = f.stream_len()?;
2139    ///     println!("The file is currently {len} bytes long");
2140    ///     Ok(())
2141    /// }
2142    /// ```
2143    #[unstable(feature = "seek_stream_len", issue = "59359")]
2144    fn stream_len(&mut self) -> Result<u64> {
2145        stream_len_default(self)
2146    }
2147
2148    /// Returns the current seek position from the start of the stream.
2149    ///
2150    /// This is equivalent to `self.seek(SeekFrom::Current(0))`.
2151    ///
2152    /// # Example
2153    ///
2154    /// ```no_run
2155    /// use std::{
2156    ///     io::{self, BufRead, BufReader, Seek},
2157    ///     fs::File,
2158    /// };
2159    ///
2160    /// fn main() -> io::Result<()> {
2161    ///     let mut f = BufReader::new(File::open("foo.txt")?);
2162    ///
2163    ///     let before = f.stream_position()?;
2164    ///     f.read_line(&mut String::new())?;
2165    ///     let after = f.stream_position()?;
2166    ///
2167    ///     println!("The first line was {} bytes long", after - before);
2168    ///     Ok(())
2169    /// }
2170    /// ```
2171    #[stable(feature = "seek_convenience", since = "1.51.0")]
2172    fn stream_position(&mut self) -> Result<u64> {
2173        self.seek(SeekFrom::Current(0))
2174    }
2175
2176    /// Seeks relative to the current position.
2177    ///
2178    /// This is equivalent to `self.seek(SeekFrom::Current(offset))` but
2179    /// doesn't return the new position which can allow some implementations
2180    /// such as [`BufReader`] to perform more efficient seeks.
2181    ///
2182    /// # Example
2183    ///
2184    /// ```no_run
2185    /// use std::{
2186    ///     io::{self, Seek},
2187    ///     fs::File,
2188    /// };
2189    ///
2190    /// fn main() -> io::Result<()> {
2191    ///     let mut f = File::open("foo.txt")?;
2192    ///     f.seek_relative(10)?;
2193    ///     assert_eq!(f.stream_position()?, 10);
2194    ///     Ok(())
2195    /// }
2196    /// ```
2197    ///
2198    /// [`BufReader`]: crate::io::BufReader
2199    #[stable(feature = "seek_seek_relative", since = "1.80.0")]
2200    fn seek_relative(&mut self, offset: i64) -> Result<()> {
2201        self.seek(SeekFrom::Current(offset))?;
2202        Ok(())
2203    }
2204}
2205
2206pub(crate) fn stream_len_default<T: Seek + ?Sized>(self_: &mut T) -> Result<u64> {
2207    let old_pos = self_.stream_position()?;
2208    let len = self_.seek(SeekFrom::End(0))?;
2209
2210    // Avoid seeking a third time when we were already at the end of the
2211    // stream. The branch is usually way cheaper than a seek operation.
2212    if old_pos != len {
2213        self_.seek(SeekFrom::Start(old_pos))?;
2214    }
2215
2216    Ok(len)
2217}
2218
2219/// Enumeration of possible methods to seek within an I/O object.
2220///
2221/// It is used by the [`Seek`] trait.
2222#[derive(Copy, PartialEq, Eq, Clone, Debug)]
2223#[stable(feature = "rust1", since = "1.0.0")]
2224#[cfg_attr(not(test), rustc_diagnostic_item = "SeekFrom")]
2225pub enum SeekFrom {
2226    /// Sets the offset to the provided number of bytes.
2227    #[stable(feature = "rust1", since = "1.0.0")]
2228    Start(#[stable(feature = "rust1", since = "1.0.0")] u64),
2229
2230    /// Sets the offset to the size of this object plus the specified number of
2231    /// bytes.
2232    ///
2233    /// It is possible to seek beyond the end of an object, but it's an error to
2234    /// seek before byte 0.
2235    #[stable(feature = "rust1", since = "1.0.0")]
2236    End(#[stable(feature = "rust1", since = "1.0.0")] i64),
2237
2238    /// Sets the offset to the current position plus the specified number of
2239    /// bytes.
2240    ///
2241    /// It is possible to seek beyond the end of an object, but it's an error to
2242    /// seek before byte 0.
2243    #[stable(feature = "rust1", since = "1.0.0")]
2244    Current(#[stable(feature = "rust1", since = "1.0.0")] i64),
2245}
2246
2247fn read_until<R: BufRead + ?Sized>(r: &mut R, delim: u8, buf: &mut Vec<u8>) -> Result<usize> {
2248    let mut read = 0;
2249    loop {
2250        let (done, used) = {
2251            let available = match r.fill_buf() {
2252                Ok(n) => n,
2253                Err(ref e) if e.is_interrupted() => continue,
2254                Err(e) => return Err(e),
2255            };
2256            match memchr::memchr(delim, available) {
2257                Some(i) => {
2258                    buf.extend_from_slice(&available[..=i]);
2259                    (true, i + 1)
2260                }
2261                None => {
2262                    buf.extend_from_slice(available);
2263                    (false, available.len())
2264                }
2265            }
2266        };
2267        r.consume(used);
2268        read += used;
2269        if done || used == 0 {
2270            return Ok(read);
2271        }
2272    }
2273}
2274
2275fn skip_until<R: BufRead + ?Sized>(r: &mut R, delim: u8) -> Result<usize> {
2276    let mut read = 0;
2277    loop {
2278        let (done, used) = {
2279            let available = match r.fill_buf() {
2280                Ok(n) => n,
2281                Err(ref e) if e.kind() == ErrorKind::Interrupted => continue,
2282                Err(e) => return Err(e),
2283            };
2284            match memchr::memchr(delim, available) {
2285                Some(i) => (true, i + 1),
2286                None => (false, available.len()),
2287            }
2288        };
2289        r.consume(used);
2290        read += used;
2291        if done || used == 0 {
2292            return Ok(read);
2293        }
2294    }
2295}
2296
2297/// A `BufRead` is a type of `Read`er which has an internal buffer, allowing it
2298/// to perform extra ways of reading.
2299///
2300/// For example, reading line-by-line is inefficient without using a buffer, so
2301/// if you want to read by line, you'll need `BufRead`, which includes a
2302/// [`read_line`] method as well as a [`lines`] iterator.
2303///
2304/// # Examples
2305///
2306/// A locked standard input implements `BufRead`:
2307///
2308/// ```no_run
2309/// use std::io;
2310/// use std::io::prelude::*;
2311///
2312/// let stdin = io::stdin();
2313/// for line in stdin.lock().lines() {
2314///     println!("{}", line?);
2315/// }
2316/// # std::io::Result::Ok(())
2317/// ```
2318///
2319/// If you have something that implements [`Read`], you can use the [`BufReader`
2320/// type][`BufReader`] to turn it into a `BufRead`.
2321///
2322/// For example, [`File`] implements [`Read`], but not `BufRead`.
2323/// [`BufReader`] to the rescue!
2324///
2325/// [`File`]: crate::fs::File
2326/// [`read_line`]: BufRead::read_line
2327/// [`lines`]: BufRead::lines
2328///
2329/// ```no_run
2330/// use std::io::{self, BufReader};
2331/// use std::io::prelude::*;
2332/// use std::fs::File;
2333///
2334/// fn main() -> io::Result<()> {
2335///     let f = File::open("foo.txt")?;
2336///     let f = BufReader::new(f);
2337///
2338///     for line in f.lines() {
2339///         let line = line?;
2340///         println!("{line}");
2341///     }
2342///
2343///     Ok(())
2344/// }
2345/// ```
2346#[stable(feature = "rust1", since = "1.0.0")]
2347#[cfg_attr(not(test), rustc_diagnostic_item = "IoBufRead")]
2348pub trait BufRead: Read {
2349    /// Returns the contents of the internal buffer, filling it with more data, via `Read` methods, if empty.
2350    ///
2351    /// This is a lower-level method and is meant to be used together with [`consume`],
2352    /// which can be used to mark bytes that should not be returned by subsequent calls to `read`.
2353    ///
2354    /// [`consume`]: BufRead::consume
2355    ///
2356    /// Returns an empty buffer when the stream has reached EOF.
2357    ///
2358    /// # Errors
2359    ///
2360    /// This function will return an I/O error if a `Read` method was called, but returned an error.
2361    ///
2362    /// # Examples
2363    ///
2364    /// A locked standard input implements `BufRead`:
2365    ///
2366    /// ```no_run
2367    /// use std::io;
2368    /// use std::io::prelude::*;
2369    ///
2370    /// let stdin = io::stdin();
2371    /// let mut stdin = stdin.lock();
2372    ///
2373    /// let buffer = stdin.fill_buf()?;
2374    ///
2375    /// // work with buffer
2376    /// println!("{buffer:?}");
2377    ///
2378    /// // mark the bytes we worked with as read
2379    /// let length = buffer.len();
2380    /// stdin.consume(length);
2381    /// # std::io::Result::Ok(())
2382    /// ```
2383    #[stable(feature = "rust1", since = "1.0.0")]
2384    fn fill_buf(&mut self) -> Result<&[u8]>;
2385
2386    /// Marks the given `amount` of additional bytes from the internal buffer as having been read.
2387    /// Subsequent calls to `read` only return bytes that have not been marked as read.
2388    ///
2389    /// This is a lower-level method and is meant to be used together with [`fill_buf`],
2390    /// which can be used to fill the internal buffer via `Read` methods.
2391    ///
2392    /// It is a logic error if `amount` exceeds the number of unread bytes in the internal buffer, which is returned by [`fill_buf`].
2393    ///
2394    /// # Examples
2395    ///
2396    /// Since `consume()` is meant to be used with [`fill_buf`],
2397    /// that method's example includes an example of `consume()`.
2398    ///
2399    /// [`fill_buf`]: BufRead::fill_buf
2400    #[stable(feature = "rust1", since = "1.0.0")]
2401    fn consume(&mut self, amount: usize);
2402
2403    /// Checks if there is any data left to be `read`.
2404    ///
2405    /// This function may fill the buffer to check for data,
2406    /// so this function returns `Result<bool>`, not `bool`.
2407    ///
2408    /// The default implementation calls `fill_buf` and checks that the
2409    /// returned slice is empty (which means that there is no data left,
2410    /// since EOF is reached).
2411    ///
2412    /// # Errors
2413    ///
2414    /// This function will return an I/O error if a `Read` method was called, but returned an error.
2415    ///
2416    /// Examples
2417    ///
2418    /// ```
2419    /// #![feature(buf_read_has_data_left)]
2420    /// use std::io;
2421    /// use std::io::prelude::*;
2422    ///
2423    /// let stdin = io::stdin();
2424    /// let mut stdin = stdin.lock();
2425    ///
2426    /// while stdin.has_data_left()? {
2427    ///     let mut line = String::new();
2428    ///     stdin.read_line(&mut line)?;
2429    ///     // work with line
2430    ///     println!("{line:?}");
2431    /// }
2432    /// # std::io::Result::Ok(())
2433    /// ```
2434    #[unstable(feature = "buf_read_has_data_left", issue = "86423")]
2435    fn has_data_left(&mut self) -> Result<bool> {
2436        self.fill_buf().map(|b| !b.is_empty())
2437    }
2438
2439    /// Reads all bytes into `buf` until the delimiter `byte` or EOF is reached.
2440    ///
2441    /// This function will read bytes from the underlying stream until the
2442    /// delimiter or EOF is found. Once found, all bytes up to, and including,
2443    /// the delimiter (if found) will be appended to `buf`.
2444    ///
2445    /// If successful, this function will return the total number of bytes read.
2446    ///
2447    /// This function is blocking and should be used carefully: it is possible for
2448    /// an attacker to continuously send bytes without ever sending the delimiter
2449    /// or EOF.
2450    ///
2451    /// # Errors
2452    ///
2453    /// This function will ignore all instances of [`ErrorKind::Interrupted`] and
2454    /// will otherwise return any errors returned by [`fill_buf`].
2455    ///
2456    /// If an I/O error is encountered then all bytes read so far will be
2457    /// present in `buf` and its length will have been adjusted appropriately.
2458    ///
2459    /// [`fill_buf`]: BufRead::fill_buf
2460    ///
2461    /// # Examples
2462    ///
2463    /// [`std::io::Cursor`][`Cursor`] is a type that implements `BufRead`. In
2464    /// this example, we use [`Cursor`] to read all the bytes in a byte slice
2465    /// in hyphen delimited segments:
2466    ///
2467    /// ```
2468    /// use std::io::{self, BufRead};
2469    ///
2470    /// let mut cursor = io::Cursor::new(b"lorem-ipsum");
2471    /// let mut buf = vec![];
2472    ///
2473    /// // cursor is at 'l'
2474    /// let num_bytes = cursor.read_until(b'-', &mut buf)
2475    ///     .expect("reading from cursor won't fail");
2476    /// assert_eq!(num_bytes, 6);
2477    /// assert_eq!(buf, b"lorem-");
2478    /// buf.clear();
2479    ///
2480    /// // cursor is at 'i'
2481    /// let num_bytes = cursor.read_until(b'-', &mut buf)
2482    ///     .expect("reading from cursor won't fail");
2483    /// assert_eq!(num_bytes, 5);
2484    /// assert_eq!(buf, b"ipsum");
2485    /// buf.clear();
2486    ///
2487    /// // cursor is at EOF
2488    /// let num_bytes = cursor.read_until(b'-', &mut buf)
2489    ///     .expect("reading from cursor won't fail");
2490    /// assert_eq!(num_bytes, 0);
2491    /// assert_eq!(buf, b"");
2492    /// ```
2493    #[stable(feature = "rust1", since = "1.0.0")]
2494    fn read_until(&mut self, byte: u8, buf: &mut Vec<u8>) -> Result<usize> {
2495        read_until(self, byte, buf)
2496    }
2497
2498    /// Skips all bytes until the delimiter `byte` or EOF is reached.
2499    ///
2500    /// This function will read (and discard) bytes from the underlying stream until the
2501    /// delimiter or EOF is found.
2502    ///
2503    /// If successful, this function will return the total number of bytes read,
2504    /// including the delimiter byte if found.
2505    ///
2506    /// This is useful for efficiently skipping data such as NUL-terminated strings
2507    /// in binary file formats without buffering.
2508    ///
2509    /// This function is blocking and should be used carefully: it is possible for
2510    /// an attacker to continuously send bytes without ever sending the delimiter
2511    /// or EOF.
2512    ///
2513    /// # Errors
2514    ///
2515    /// This function will ignore all instances of [`ErrorKind::Interrupted`] and
2516    /// will otherwise return any errors returned by [`fill_buf`].
2517    ///
2518    /// If an I/O error is encountered then all bytes read so far will be
2519    /// present in `buf` and its length will have been adjusted appropriately.
2520    ///
2521    /// [`fill_buf`]: BufRead::fill_buf
2522    ///
2523    /// # Examples
2524    ///
2525    /// [`std::io::Cursor`][`Cursor`] is a type that implements `BufRead`. In
2526    /// this example, we use [`Cursor`] to read some NUL-terminated information
2527    /// about Ferris from a binary string, skipping the fun fact:
2528    ///
2529    /// ```
2530    /// use std::io::{self, BufRead};
2531    ///
2532    /// let mut cursor = io::Cursor::new(b"Ferris\0Likes long walks on the beach\0Crustacean\0!");
2533    ///
2534    /// // read name
2535    /// let mut name = Vec::new();
2536    /// let num_bytes = cursor.read_until(b'\0', &mut name)
2537    ///     .expect("reading from cursor won't fail");
2538    /// assert_eq!(num_bytes, 7);
2539    /// assert_eq!(name, b"Ferris\0");
2540    ///
2541    /// // skip fun fact
2542    /// let num_bytes = cursor.skip_until(b'\0')
2543    ///     .expect("reading from cursor won't fail");
2544    /// assert_eq!(num_bytes, 30);
2545    ///
2546    /// // read animal type
2547    /// let mut animal = Vec::new();
2548    /// let num_bytes = cursor.read_until(b'\0', &mut animal)
2549    ///     .expect("reading from cursor won't fail");
2550    /// assert_eq!(num_bytes, 11);
2551    /// assert_eq!(animal, b"Crustacean\0");
2552    ///
2553    /// // reach EOF
2554    /// let num_bytes = cursor.skip_until(b'\0')
2555    ///     .expect("reading from cursor won't fail");
2556    /// assert_eq!(num_bytes, 1);
2557    /// ```
2558    #[stable(feature = "bufread_skip_until", since = "1.83.0")]
2559    fn skip_until(&mut self, byte: u8) -> Result<usize> {
2560        skip_until(self, byte)
2561    }
2562
2563    /// Reads all bytes until a newline (the `0xA` byte) is reached, and append
2564    /// them to the provided `String` buffer.
2565    ///
2566    /// Previous content of the buffer will be preserved. To avoid appending to
2567    /// the buffer, you need to [`clear`] it first.
2568    ///
2569    /// This function will read bytes from the underlying stream until the
2570    /// newline delimiter (the `0xA` byte) or EOF is found. Once found, all bytes
2571    /// up to, and including, the delimiter (if found) will be appended to
2572    /// `buf`.
2573    ///
2574    /// If successful, this function will return the total number of bytes read.
2575    ///
2576    /// If this function returns [`Ok(0)`], the stream has reached EOF.
2577    ///
2578    /// This function is blocking and should be used carefully: it is possible for
2579    /// an attacker to continuously send bytes without ever sending a newline
2580    /// or EOF. You can use [`take`] to limit the maximum number of bytes read.
2581    ///
2582    /// [`Ok(0)`]: Ok
2583    /// [`clear`]: String::clear
2584    /// [`take`]: crate::io::Read::take
2585    ///
2586    /// # Errors
2587    ///
2588    /// This function has the same error semantics as [`read_until`] and will
2589    /// also return an error if the read bytes are not valid UTF-8. If an I/O
2590    /// error is encountered then `buf` may contain some bytes already read in
2591    /// the event that all data read so far was valid UTF-8.
2592    ///
2593    /// [`read_until`]: BufRead::read_until
2594    ///
2595    /// # Examples
2596    ///
2597    /// [`std::io::Cursor`][`Cursor`] is a type that implements `BufRead`. In
2598    /// this example, we use [`Cursor`] to read all the lines in a byte slice:
2599    ///
2600    /// ```
2601    /// use std::io::{self, BufRead};
2602    ///
2603    /// let mut cursor = io::Cursor::new(b"foo\nbar");
2604    /// let mut buf = String::new();
2605    ///
2606    /// // cursor is at 'f'
2607    /// let num_bytes = cursor.read_line(&mut buf)
2608    ///     .expect("reading from cursor won't fail");
2609    /// assert_eq!(num_bytes, 4);
2610    /// assert_eq!(buf, "foo\n");
2611    /// buf.clear();
2612    ///
2613    /// // cursor is at 'b'
2614    /// let num_bytes = cursor.read_line(&mut buf)
2615    ///     .expect("reading from cursor won't fail");
2616    /// assert_eq!(num_bytes, 3);
2617    /// assert_eq!(buf, "bar");
2618    /// buf.clear();
2619    ///
2620    /// // cursor is at EOF
2621    /// let num_bytes = cursor.read_line(&mut buf)
2622    ///     .expect("reading from cursor won't fail");
2623    /// assert_eq!(num_bytes, 0);
2624    /// assert_eq!(buf, "");
2625    /// ```
2626    #[stable(feature = "rust1", since = "1.0.0")]
2627    fn read_line(&mut self, buf: &mut String) -> Result<usize> {
2628        // Note that we are not calling the `.read_until` method here, but
2629        // rather our hardcoded implementation. For more details as to why, see
2630        // the comments in `default_read_to_string`.
2631        unsafe { append_to_string(buf, |b| read_until(self, b'\n', b)) }
2632    }
2633
2634    /// Returns an iterator over the contents of this reader split on the byte
2635    /// `byte`.
2636    ///
2637    /// The iterator returned from this function will return instances of
2638    /// <code>[io::Result]<[Vec]\<u8>></code>. Each vector returned will *not* have
2639    /// the delimiter byte at the end.
2640    ///
2641    /// This function will yield errors whenever [`read_until`] would have
2642    /// also yielded an error.
2643    ///
2644    /// [io::Result]: self::Result "io::Result"
2645    /// [`read_until`]: BufRead::read_until
2646    ///
2647    /// # Examples
2648    ///
2649    /// [`std::io::Cursor`][`Cursor`] is a type that implements `BufRead`. In
2650    /// this example, we use [`Cursor`] to iterate over all hyphen delimited
2651    /// segments in a byte slice
2652    ///
2653    /// ```
2654    /// use std::io::{self, BufRead};
2655    ///
2656    /// let cursor = io::Cursor::new(b"lorem-ipsum-dolor");
2657    ///
2658    /// let mut split_iter = cursor.split(b'-').map(|l| l.unwrap());
2659    /// assert_eq!(split_iter.next(), Some(b"lorem".to_vec()));
2660    /// assert_eq!(split_iter.next(), Some(b"ipsum".to_vec()));
2661    /// assert_eq!(split_iter.next(), Some(b"dolor".to_vec()));
2662    /// assert_eq!(split_iter.next(), None);
2663    /// ```
2664    #[stable(feature = "rust1", since = "1.0.0")]
2665    fn split(self, byte: u8) -> Split<Self>
2666    where
2667        Self: Sized,
2668    {
2669        Split { buf: self, delim: byte }
2670    }
2671
2672    /// Returns an iterator over the lines of this reader.
2673    ///
2674    /// The iterator returned from this function will yield instances of
2675    /// <code>[io::Result]<[String]></code>. Each string returned will *not* have a newline
2676    /// byte (the `0xA` byte) or `CRLF` (`0xD`, `0xA` bytes) at the end.
2677    ///
2678    /// [io::Result]: self::Result "io::Result"
2679    ///
2680    /// # Examples
2681    ///
2682    /// [`std::io::Cursor`][`Cursor`] is a type that implements `BufRead`. In
2683    /// this example, we use [`Cursor`] to iterate over all the lines in a byte
2684    /// slice.
2685    ///
2686    /// ```
2687    /// use std::io::{self, BufRead};
2688    ///
2689    /// let cursor = io::Cursor::new(b"lorem\nipsum\r\ndolor");
2690    ///
2691    /// let mut lines_iter = cursor.lines().map(|l| l.unwrap());
2692    /// assert_eq!(lines_iter.next(), Some(String::from("lorem")));
2693    /// assert_eq!(lines_iter.next(), Some(String::from("ipsum")));
2694    /// assert_eq!(lines_iter.next(), Some(String::from("dolor")));
2695    /// assert_eq!(lines_iter.next(), None);
2696    /// ```
2697    ///
2698    /// # Errors
2699    ///
2700    /// Each line of the iterator has the same error semantics as [`BufRead::read_line`].
2701    #[stable(feature = "rust1", since = "1.0.0")]
2702    fn lines(self) -> Lines<Self>
2703    where
2704        Self: Sized,
2705    {
2706        Lines { buf: self }
2707    }
2708}
2709
2710/// Adapter to chain together two readers.
2711///
2712/// This struct is generally created by calling [`chain`] on a reader.
2713/// Please see the documentation of [`chain`] for more details.
2714///
2715/// [`chain`]: Read::chain
2716#[stable(feature = "rust1", since = "1.0.0")]
2717#[derive(Debug)]
2718pub struct Chain<T, U> {
2719    first: T,
2720    second: U,
2721    done_first: bool,
2722}
2723
2724impl<T, U> Chain<T, U> {
2725    /// Consumes the `Chain`, returning the wrapped readers.
2726    ///
2727    /// # Examples
2728    ///
2729    /// ```no_run
2730    /// use std::io;
2731    /// use std::io::prelude::*;
2732    /// use std::fs::File;
2733    ///
2734    /// fn main() -> io::Result<()> {
2735    ///     let mut foo_file = File::open("foo.txt")?;
2736    ///     let mut bar_file = File::open("bar.txt")?;
2737    ///
2738    ///     let chain = foo_file.chain(bar_file);
2739    ///     let (foo_file, bar_file) = chain.into_inner();
2740    ///     Ok(())
2741    /// }
2742    /// ```
2743    #[stable(feature = "more_io_inner_methods", since = "1.20.0")]
2744    pub fn into_inner(self) -> (T, U) {
2745        (self.first, self.second)
2746    }
2747
2748    /// Gets references to the underlying readers in this `Chain`.
2749    ///
2750    /// Care should be taken to avoid modifying the internal I/O state of the
2751    /// underlying readers as doing so may corrupt the internal state of this
2752    /// `Chain`.
2753    ///
2754    /// # Examples
2755    ///
2756    /// ```no_run
2757    /// use std::io;
2758    /// use std::io::prelude::*;
2759    /// use std::fs::File;
2760    ///
2761    /// fn main() -> io::Result<()> {
2762    ///     let mut foo_file = File::open("foo.txt")?;
2763    ///     let mut bar_file = File::open("bar.txt")?;
2764    ///
2765    ///     let chain = foo_file.chain(bar_file);
2766    ///     let (foo_file, bar_file) = chain.get_ref();
2767    ///     Ok(())
2768    /// }
2769    /// ```
2770    #[stable(feature = "more_io_inner_methods", since = "1.20.0")]
2771    pub fn get_ref(&self) -> (&T, &U) {
2772        (&self.first, &self.second)
2773    }
2774
2775    /// Gets mutable references to the underlying readers in this `Chain`.
2776    ///
2777    /// Care should be taken to avoid modifying the internal I/O state of the
2778    /// underlying readers as doing so may corrupt the internal state of this
2779    /// `Chain`.
2780    ///
2781    /// # Examples
2782    ///
2783    /// ```no_run
2784    /// use std::io;
2785    /// use std::io::prelude::*;
2786    /// use std::fs::File;
2787    ///
2788    /// fn main() -> io::Result<()> {
2789    ///     let mut foo_file = File::open("foo.txt")?;
2790    ///     let mut bar_file = File::open("bar.txt")?;
2791    ///
2792    ///     let mut chain = foo_file.chain(bar_file);
2793    ///     let (foo_file, bar_file) = chain.get_mut();
2794    ///     Ok(())
2795    /// }
2796    /// ```
2797    #[stable(feature = "more_io_inner_methods", since = "1.20.0")]
2798    pub fn get_mut(&mut self) -> (&mut T, &mut U) {
2799        (&mut self.first, &mut self.second)
2800    }
2801}
2802
2803#[stable(feature = "rust1", since = "1.0.0")]
2804impl<T: Read, U: Read> Read for Chain<T, U> {
2805    fn read(&mut self, buf: &mut [u8]) -> Result<usize> {
2806        if !self.done_first {
2807            match self.first.read(buf)? {
2808                0 if !buf.is_empty() => self.done_first = true,
2809                n => return Ok(n),
2810            }
2811        }
2812        self.second.read(buf)
2813    }
2814
2815    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> Result<usize> {
2816        if !self.done_first {
2817            match self.first.read_vectored(bufs)? {
2818                0 if bufs.iter().any(|b| !b.is_empty()) => self.done_first = true,
2819                n => return Ok(n),
2820            }
2821        }
2822        self.second.read_vectored(bufs)
2823    }
2824
2825    #[inline]
2826    fn is_read_vectored(&self) -> bool {
2827        self.first.is_read_vectored() || self.second.is_read_vectored()
2828    }
2829
2830    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> Result<usize> {
2831        let mut read = 0;
2832        if !self.done_first {
2833            read += self.first.read_to_end(buf)?;
2834            self.done_first = true;
2835        }
2836        read += self.second.read_to_end(buf)?;
2837        Ok(read)
2838    }
2839
2840    // We don't override `read_to_string` here because an UTF-8 sequence could
2841    // be split between the two parts of the chain
2842
2843    fn read_buf(&mut self, mut buf: BorrowedCursor<'_>) -> Result<()> {
2844        if buf.capacity() == 0 {
2845            return Ok(());
2846        }
2847
2848        if !self.done_first {
2849            let old_len = buf.written();
2850            self.first.read_buf(buf.reborrow())?;
2851
2852            if buf.written() != old_len {
2853                return Ok(());
2854            } else {
2855                self.done_first = true;
2856            }
2857        }
2858        self.second.read_buf(buf)
2859    }
2860}
2861
2862#[stable(feature = "chain_bufread", since = "1.9.0")]
2863impl<T: BufRead, U: BufRead> BufRead for Chain<T, U> {
2864    fn fill_buf(&mut self) -> Result<&[u8]> {
2865        if !self.done_first {
2866            match self.first.fill_buf()? {
2867                buf if buf.is_empty() => self.done_first = true,
2868                buf => return Ok(buf),
2869            }
2870        }
2871        self.second.fill_buf()
2872    }
2873
2874    fn consume(&mut self, amt: usize) {
2875        if !self.done_first { self.first.consume(amt) } else { self.second.consume(amt) }
2876    }
2877
2878    fn read_until(&mut self, byte: u8, buf: &mut Vec<u8>) -> Result<usize> {
2879        let mut read = 0;
2880        if !self.done_first {
2881            let n = self.first.read_until(byte, buf)?;
2882            read += n;
2883
2884            match buf.last() {
2885                Some(b) if *b == byte && n != 0 => return Ok(read),
2886                _ => self.done_first = true,
2887            }
2888        }
2889        read += self.second.read_until(byte, buf)?;
2890        Ok(read)
2891    }
2892
2893    // We don't override `read_line` here because an UTF-8 sequence could be
2894    // split between the two parts of the chain
2895}
2896
2897impl<T, U> SizeHint for Chain<T, U> {
2898    #[inline]
2899    fn lower_bound(&self) -> usize {
2900        SizeHint::lower_bound(&self.first) + SizeHint::lower_bound(&self.second)
2901    }
2902
2903    #[inline]
2904    fn upper_bound(&self) -> Option<usize> {
2905        match (SizeHint::upper_bound(&self.first), SizeHint::upper_bound(&self.second)) {
2906            (Some(first), Some(second)) => first.checked_add(second),
2907            _ => None,
2908        }
2909    }
2910}
2911
2912/// Reader adapter which limits the bytes read from an underlying reader.
2913///
2914/// This struct is generally created by calling [`take`] on a reader.
2915/// Please see the documentation of [`take`] for more details.
2916///
2917/// [`take`]: Read::take
2918#[stable(feature = "rust1", since = "1.0.0")]
2919#[derive(Debug)]
2920pub struct Take<T> {
2921    inner: T,
2922    len: u64,
2923    limit: u64,
2924}
2925
2926impl<T> Take<T> {
2927    /// Returns the number of bytes that can be read before this instance will
2928    /// return EOF.
2929    ///
2930    /// # Note
2931    ///
2932    /// This instance may reach `EOF` after reading fewer bytes than indicated by
2933    /// this method if the underlying [`Read`] instance reaches EOF.
2934    ///
2935    /// # Examples
2936    ///
2937    /// ```no_run
2938    /// use std::io;
2939    /// use std::io::prelude::*;
2940    /// use std::fs::File;
2941    ///
2942    /// fn main() -> io::Result<()> {
2943    ///     let f = File::open("foo.txt")?;
2944    ///
2945    ///     // read at most five bytes
2946    ///     let handle = f.take(5);
2947    ///
2948    ///     println!("limit: {}", handle.limit());
2949    ///     Ok(())
2950    /// }
2951    /// ```
2952    #[stable(feature = "rust1", since = "1.0.0")]
2953    pub fn limit(&self) -> u64 {
2954        self.limit
2955    }
2956
2957    /// Returns the number of bytes read so far.
2958    #[unstable(feature = "seek_io_take_position", issue = "97227")]
2959    pub fn position(&self) -> u64 {
2960        self.len - self.limit
2961    }
2962
2963    /// Sets the number of bytes that can be read before this instance will
2964    /// return EOF. This is the same as constructing a new `Take` instance, so
2965    /// the amount of bytes read and the previous limit value don't matter when
2966    /// calling this method.
2967    ///
2968    /// # Examples
2969    ///
2970    /// ```no_run
2971    /// use std::io;
2972    /// use std::io::prelude::*;
2973    /// use std::fs::File;
2974    ///
2975    /// fn main() -> io::Result<()> {
2976    ///     let f = File::open("foo.txt")?;
2977    ///
2978    ///     // read at most five bytes
2979    ///     let mut handle = f.take(5);
2980    ///     handle.set_limit(10);
2981    ///
2982    ///     assert_eq!(handle.limit(), 10);
2983    ///     Ok(())
2984    /// }
2985    /// ```
2986    #[stable(feature = "take_set_limit", since = "1.27.0")]
2987    pub fn set_limit(&mut self, limit: u64) {
2988        self.len = limit;
2989        self.limit = limit;
2990    }
2991
2992    /// Consumes the `Take`, returning the wrapped reader.
2993    ///
2994    /// # Examples
2995    ///
2996    /// ```no_run
2997    /// use std::io;
2998    /// use std::io::prelude::*;
2999    /// use std::fs::File;
3000    ///
3001    /// fn main() -> io::Result<()> {
3002    ///     let mut file = File::open("foo.txt")?;
3003    ///
3004    ///     let mut buffer = [0; 5];
3005    ///     let mut handle = file.take(5);
3006    ///     handle.read(&mut buffer)?;
3007    ///
3008    ///     let file = handle.into_inner();
3009    ///     Ok(())
3010    /// }
3011    /// ```
3012    #[stable(feature = "io_take_into_inner", since = "1.15.0")]
3013    pub fn into_inner(self) -> T {
3014        self.inner
3015    }
3016
3017    /// Gets a reference to the underlying reader.
3018    ///
3019    /// Care should be taken to avoid modifying the internal I/O state of the
3020    /// underlying reader as doing so may corrupt the internal limit of this
3021    /// `Take`.
3022    ///
3023    /// # Examples
3024    ///
3025    /// ```no_run
3026    /// use std::io;
3027    /// use std::io::prelude::*;
3028    /// use std::fs::File;
3029    ///
3030    /// fn main() -> io::Result<()> {
3031    ///     let mut file = File::open("foo.txt")?;
3032    ///
3033    ///     let mut buffer = [0; 5];
3034    ///     let mut handle = file.take(5);
3035    ///     handle.read(&mut buffer)?;
3036    ///
3037    ///     let file = handle.get_ref();
3038    ///     Ok(())
3039    /// }
3040    /// ```
3041    #[stable(feature = "more_io_inner_methods", since = "1.20.0")]
3042    pub fn get_ref(&self) -> &T {
3043        &self.inner
3044    }
3045
3046    /// Gets a mutable reference to the underlying reader.
3047    ///
3048    /// Care should be taken to avoid modifying the internal I/O state of the
3049    /// underlying reader as doing so may corrupt the internal limit of this
3050    /// `Take`.
3051    ///
3052    /// # Examples
3053    ///
3054    /// ```no_run
3055    /// use std::io;
3056    /// use std::io::prelude::*;
3057    /// use std::fs::File;
3058    ///
3059    /// fn main() -> io::Result<()> {
3060    ///     let mut file = File::open("foo.txt")?;
3061    ///
3062    ///     let mut buffer = [0; 5];
3063    ///     let mut handle = file.take(5);
3064    ///     handle.read(&mut buffer)?;
3065    ///
3066    ///     let file = handle.get_mut();
3067    ///     Ok(())
3068    /// }
3069    /// ```
3070    #[stable(feature = "more_io_inner_methods", since = "1.20.0")]
3071    pub fn get_mut(&mut self) -> &mut T {
3072        &mut self.inner
3073    }
3074}
3075
3076#[stable(feature = "rust1", since = "1.0.0")]
3077impl<T: Read> Read for Take<T> {
3078    fn read(&mut self, buf: &mut [u8]) -> Result<usize> {
3079        // Don't call into inner reader at all at EOF because it may still block
3080        if self.limit == 0 {
3081            return Ok(0);
3082        }
3083
3084        let max = cmp::min(buf.len() as u64, self.limit) as usize;
3085        let n = self.inner.read(&mut buf[..max])?;
3086        assert!(n as u64 <= self.limit, "number of read bytes exceeds limit");
3087        self.limit -= n as u64;
3088        Ok(n)
3089    }
3090
3091    fn read_buf(&mut self, mut buf: BorrowedCursor<'_>) -> Result<()> {
3092        // Don't call into inner reader at all at EOF because it may still block
3093        if self.limit == 0 {
3094            return Ok(());
3095        }
3096
3097        if self.limit < buf.capacity() as u64 {
3098            // The condition above guarantees that `self.limit` fits in `usize`.
3099            let limit = self.limit as usize;
3100
3101            let extra_init = cmp::min(limit, buf.init_mut().len());
3102
3103            // SAFETY: no uninit data is written to ibuf
3104            let ibuf = unsafe { &mut buf.as_mut()[..limit] };
3105
3106            let mut sliced_buf: BorrowedBuf<'_> = ibuf.into();
3107
3108            // SAFETY: extra_init bytes of ibuf are known to be initialized
3109            unsafe {
3110                sliced_buf.set_init(extra_init);
3111            }
3112
3113            let mut cursor = sliced_buf.unfilled();
3114            let result = self.inner.read_buf(cursor.reborrow());
3115
3116            let new_init = cursor.init_mut().len();
3117            let filled = sliced_buf.len();
3118
3119            // cursor / sliced_buf / ibuf must drop here
3120
3121            unsafe {
3122                // SAFETY: filled bytes have been filled and therefore initialized
3123                buf.advance_unchecked(filled);
3124                // SAFETY: new_init bytes of buf's unfilled buffer have been initialized
3125                buf.set_init(new_init);
3126            }
3127
3128            self.limit -= filled as u64;
3129
3130            result
3131        } else {
3132            let written = buf.written();
3133            let result = self.inner.read_buf(buf.reborrow());
3134            self.limit -= (buf.written() - written) as u64;
3135            result
3136        }
3137    }
3138}
3139
3140#[stable(feature = "rust1", since = "1.0.0")]
3141impl<T: BufRead> BufRead for Take<T> {
3142    fn fill_buf(&mut self) -> Result<&[u8]> {
3143        // Don't call into inner reader at all at EOF because it may still block
3144        if self.limit == 0 {
3145            return Ok(&[]);
3146        }
3147
3148        let buf = self.inner.fill_buf()?;
3149        let cap = cmp::min(buf.len() as u64, self.limit) as usize;
3150        Ok(&buf[..cap])
3151    }
3152
3153    fn consume(&mut self, amt: usize) {
3154        // Don't let callers reset the limit by passing an overlarge value
3155        let amt = cmp::min(amt as u64, self.limit) as usize;
3156        self.limit -= amt as u64;
3157        self.inner.consume(amt);
3158    }
3159}
3160
3161impl<T> SizeHint for Take<T> {
3162    #[inline]
3163    fn lower_bound(&self) -> usize {
3164        cmp::min(SizeHint::lower_bound(&self.inner) as u64, self.limit) as usize
3165    }
3166
3167    #[inline]
3168    fn upper_bound(&self) -> Option<usize> {
3169        match SizeHint::upper_bound(&self.inner) {
3170            Some(upper_bound) => Some(cmp::min(upper_bound as u64, self.limit) as usize),
3171            None => self.limit.try_into().ok(),
3172        }
3173    }
3174}
3175
3176#[stable(feature = "seek_io_take", since = "1.89.0")]
3177impl<T: Seek> Seek for Take<T> {
3178    fn seek(&mut self, pos: SeekFrom) -> Result<u64> {
3179        let new_position = match pos {
3180            SeekFrom::Start(v) => Some(v),
3181            SeekFrom::Current(v) => self.position().checked_add_signed(v),
3182            SeekFrom::End(v) => self.len.checked_add_signed(v),
3183        };
3184        let new_position = match new_position {
3185            Some(v) if v <= self.len => v,
3186            _ => return Err(ErrorKind::InvalidInput.into()),
3187        };
3188        while new_position != self.position() {
3189            if let Some(offset) = new_position.checked_signed_diff(self.position()) {
3190                self.inner.seek_relative(offset)?;
3191                self.limit = self.limit.wrapping_sub(offset as u64);
3192                break;
3193            }
3194            let offset = if new_position > self.position() { i64::MAX } else { i64::MIN };
3195            self.inner.seek_relative(offset)?;
3196            self.limit = self.limit.wrapping_sub(offset as u64);
3197        }
3198        Ok(new_position)
3199    }
3200
3201    fn stream_len(&mut self) -> Result<u64> {
3202        Ok(self.len)
3203    }
3204
3205    fn stream_position(&mut self) -> Result<u64> {
3206        Ok(self.position())
3207    }
3208
3209    fn seek_relative(&mut self, offset: i64) -> Result<()> {
3210        if !self.position().checked_add_signed(offset).is_some_and(|p| p <= self.len) {
3211            return Err(ErrorKind::InvalidInput.into());
3212        }
3213        self.inner.seek_relative(offset)?;
3214        self.limit = self.limit.wrapping_sub(offset as u64);
3215        Ok(())
3216    }
3217}
3218
3219/// An iterator over `u8` values of a reader.
3220///
3221/// This struct is generally created by calling [`bytes`] on a reader.
3222/// Please see the documentation of [`bytes`] for more details.
3223///
3224/// [`bytes`]: Read::bytes
3225#[stable(feature = "rust1", since = "1.0.0")]
3226#[derive(Debug)]
3227pub struct Bytes<R> {
3228    inner: R,
3229}
3230
3231#[stable(feature = "rust1", since = "1.0.0")]
3232impl<R: Read> Iterator for Bytes<R> {
3233    type Item = Result<u8>;
3234
3235    // Not `#[inline]`. This function gets inlined even without it, but having
3236    // the inline annotation can result in worse code generation. See #116785.
3237    fn next(&mut self) -> Option<Result<u8>> {
3238        SpecReadByte::spec_read_byte(&mut self.inner)
3239    }
3240
3241    #[inline]
3242    fn size_hint(&self) -> (usize, Option<usize>) {
3243        SizeHint::size_hint(&self.inner)
3244    }
3245}
3246
3247/// For the specialization of `Bytes::next`.
3248trait SpecReadByte {
3249    fn spec_read_byte(&mut self) -> Option<Result<u8>>;
3250}
3251
3252impl<R> SpecReadByte for R
3253where
3254    Self: Read,
3255{
3256    #[inline]
3257    default fn spec_read_byte(&mut self) -> Option<Result<u8>> {
3258        inlined_slow_read_byte(self)
3259    }
3260}
3261
3262/// Reads a single byte in a slow, generic way. This is used by the default
3263/// `spec_read_byte`.
3264#[inline]
3265fn inlined_slow_read_byte<R: Read>(reader: &mut R) -> Option<Result<u8>> {
3266    let mut byte = 0;
3267    loop {
3268        return match reader.read(slice::from_mut(&mut byte)) {
3269            Ok(0) => None,
3270            Ok(..) => Some(Ok(byte)),
3271            Err(ref e) if e.is_interrupted() => continue,
3272            Err(e) => Some(Err(e)),
3273        };
3274    }
3275}
3276
3277// Used by `BufReader::spec_read_byte`, for which the `inline(never)` is
3278// important.
3279#[inline(never)]
3280fn uninlined_slow_read_byte<R: Read>(reader: &mut R) -> Option<Result<u8>> {
3281    inlined_slow_read_byte(reader)
3282}
3283
3284trait SizeHint {
3285    fn lower_bound(&self) -> usize;
3286
3287    fn upper_bound(&self) -> Option<usize>;
3288
3289    fn size_hint(&self) -> (usize, Option<usize>) {
3290        (self.lower_bound(), self.upper_bound())
3291    }
3292}
3293
3294impl<T: ?Sized> SizeHint for T {
3295    #[inline]
3296    default fn lower_bound(&self) -> usize {
3297        0
3298    }
3299
3300    #[inline]
3301    default fn upper_bound(&self) -> Option<usize> {
3302        None
3303    }
3304}
3305
3306impl<T> SizeHint for &mut T {
3307    #[inline]
3308    fn lower_bound(&self) -> usize {
3309        SizeHint::lower_bound(*self)
3310    }
3311
3312    #[inline]
3313    fn upper_bound(&self) -> Option<usize> {
3314        SizeHint::upper_bound(*self)
3315    }
3316}
3317
3318impl<T> SizeHint for Box<T> {
3319    #[inline]
3320    fn lower_bound(&self) -> usize {
3321        SizeHint::lower_bound(&**self)
3322    }
3323
3324    #[inline]
3325    fn upper_bound(&self) -> Option<usize> {
3326        SizeHint::upper_bound(&**self)
3327    }
3328}
3329
3330impl SizeHint for &[u8] {
3331    #[inline]
3332    fn lower_bound(&self) -> usize {
3333        self.len()
3334    }
3335
3336    #[inline]
3337    fn upper_bound(&self) -> Option<usize> {
3338        Some(self.len())
3339    }
3340}
3341
3342/// An iterator over the contents of an instance of `BufRead` split on a
3343/// particular byte.
3344///
3345/// This struct is generally created by calling [`split`] on a `BufRead`.
3346/// Please see the documentation of [`split`] for more details.
3347///
3348/// [`split`]: BufRead::split
3349#[stable(feature = "rust1", since = "1.0.0")]
3350#[derive(Debug)]
3351pub struct Split<B> {
3352    buf: B,
3353    delim: u8,
3354}
3355
3356#[stable(feature = "rust1", since = "1.0.0")]
3357impl<B: BufRead> Iterator for Split<B> {
3358    type Item = Result<Vec<u8>>;
3359
3360    fn next(&mut self) -> Option<Result<Vec<u8>>> {
3361        let mut buf = Vec::new();
3362        match self.buf.read_until(self.delim, &mut buf) {
3363            Ok(0) => None,
3364            Ok(_n) => {
3365                if buf[buf.len() - 1] == self.delim {
3366                    buf.pop();
3367                }
3368                Some(Ok(buf))
3369            }
3370            Err(e) => Some(Err(e)),
3371        }
3372    }
3373}
3374
3375/// An iterator over the lines of an instance of `BufRead`.
3376///
3377/// This struct is generally created by calling [`lines`] on a `BufRead`.
3378/// Please see the documentation of [`lines`] for more details.
3379///
3380/// [`lines`]: BufRead::lines
3381#[stable(feature = "rust1", since = "1.0.0")]
3382#[derive(Debug)]
3383#[cfg_attr(not(test), rustc_diagnostic_item = "IoLines")]
3384pub struct Lines<B> {
3385    buf: B,
3386}
3387
3388#[stable(feature = "rust1", since = "1.0.0")]
3389impl<B: BufRead> Iterator for Lines<B> {
3390    type Item = Result<String>;
3391
3392    fn next(&mut self) -> Option<Result<String>> {
3393        let mut buf = String::new();
3394        match self.buf.read_line(&mut buf) {
3395            Ok(0) => None,
3396            Ok(_n) => {
3397                if buf.ends_with('\n') {
3398                    buf.pop();
3399                    if buf.ends_with('\r') {
3400                        buf.pop();
3401                    }
3402                }
3403                Some(Ok(buf))
3404            }
3405            Err(e) => Some(Err(e)),
3406        }
3407    }
3408}
````