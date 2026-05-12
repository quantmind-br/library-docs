---
title: process.rs - source
url: https://doc.rust-lang.org/src/std/process.rs.html#2579-2584
source: crawler
fetched_at: 2026-05-06T21:26:39.874693862-03:00
rendered_js: false
word_count: 10581
summary: This document explains how to spawn and manage child processes in Rust using the Command struct, including I/O redirection and platform-specific considerations for Windows argument handling.
tags:
    - rust
    - process-management
    - child-process
    - command-execution
    - standard-library
    - io-redirection
    - windows-api
category: reference
---

````rust
1//! A module for working with processes.
2//!
3//! This module is mostly concerned with spawning and interacting with child
4//! processes, but it also provides [`abort`] and [`exit`] for terminating the
5//! current process.
6//!
7//! # Spawning a process
8//!
9//! The [`Command`] struct is used to configure and spawn processes:
10//!
11//! ```no_run
12//! use std::process::Command;
13//!
14//! let output = Command::new("echo")
15//!     .arg("Hello world")
16//!     .output()
17//!     .expect("Failed to execute command");
18//!
19//! assert_eq!(b"Hello world\n", output.stdout.as_slice());
20//! ```
21//!
22//! Several methods on [`Command`], such as [`spawn`] or [`output`], can be used
23//! to spawn a process. In particular, [`output`] spawns the child process and
24//! waits until the process terminates, while [`spawn`] will return a [`Child`]
25//! that represents the spawned child process.
26//!
27//! # Handling I/O
28//!
29//! The [`stdout`], [`stdin`], and [`stderr`] of a child process can be
30//! configured by passing an [`Stdio`] to the corresponding method on
31//! [`Command`]. Once spawned, they can be accessed from the [`Child`]. For
32//! example, piping output from one command into another command can be done
33//! like so:
34//!
35//! ```no_run
36//! use std::process::{Command, Stdio};
37//!
38//! // stdout must be configured with `Stdio::piped` in order to use
39//! // `echo_child.stdout`
40//! let echo_child = Command::new("echo")
41//!     .arg("Oh no, a tpyo!")
42//!     .stdout(Stdio::piped())
43//!     .spawn()
44//!     .expect("Failed to start echo process");
45//!
46//! // Note that `echo_child` is moved here, but we won't be needing
47//! // `echo_child` anymore
48//! let echo_out = echo_child.stdout.expect("Failed to open echo stdout");
49//!
50//! let mut sed_child = Command::new("sed")
51//!     .arg("s/tpyo/typo/")
52//!     .stdin(Stdio::from(echo_out))
53//!     .stdout(Stdio::piped())
54//!     .spawn()
55//!     .expect("Failed to start sed process");
56//!
57//! let output = sed_child.wait_with_output().expect("Failed to wait on sed");
58//! assert_eq!(b"Oh no, a typo!\n", output.stdout.as_slice());
59//! ```
60//!
61//! Note that [`ChildStderr`] and [`ChildStdout`] implement [`Read`] and
62//! [`ChildStdin`] implements [`Write`]:
63//!
64//! ```no_run
65//! use std::process::{Command, Stdio};
66//! use std::io::Write;
67//!
68//! let mut child = Command::new("/bin/cat")
69//!     .stdin(Stdio::piped())
70//!     .stdout(Stdio::piped())
71//!     .spawn()
72//!     .expect("failed to execute child");
73//!
74//! // If the child process fills its stdout buffer, it may end up
75//! // waiting until the parent reads the stdout, and not be able to
76//! // read stdin in the meantime, causing a deadlock.
77//! // Writing from another thread ensures that stdout is being read
78//! // at the same time, avoiding the problem.
79//! let mut stdin = child.stdin.take().expect("failed to get stdin");
80//! std::thread::spawn(move || {
81//!     stdin.write_all(b"test").expect("failed to write to stdin");
82//! });
83//!
84//! let output = child
85//!     .wait_with_output()
86//!     .expect("failed to wait on child");
87//!
88//! assert_eq!(b"test", output.stdout.as_slice());
89//! ```
90//!
91//! # Windows argument splitting
92//!
93//! On Unix systems arguments are passed to a new process as an array of strings,
94//! but on Windows arguments are passed as a single commandline string and it is
95//! up to the child process to parse it into an array. Therefore the parent and
96//! child processes must agree on how the commandline string is encoded.
97//!
98//! Most programs use the standard C run-time `argv`, which in practice results
99//! in consistent argument handling. However, some programs have their own way of
100//! parsing the commandline string. In these cases using [`arg`] or [`args`] may
101//! result in the child process seeing a different array of arguments than the
102//! parent process intended.
103//!
104//! Two ways of mitigating this are:
105//!
106//! * Validate untrusted input so that only a safe subset is allowed.
107//! * Use [`raw_arg`] to build a custom commandline. This bypasses the escaping
108//!   rules used by [`arg`] so should be used with due caution.
109//!
110//! `cmd.exe` and `.bat` files use non-standard argument parsing and are especially
111//! vulnerable to malicious input as they may be used to run arbitrary shell
112//! commands. Untrusted arguments should be restricted as much as possible.
113//! For examples on handling this see [`raw_arg`].
114//!
115//! ### Batch file special handling
116//!
117//! On Windows, `Command` uses the Windows API function [`CreateProcessW`] to
118//! spawn new processes. An undocumented feature of this function is that
119//! when given a `.bat` file as the application to run, it will automatically
120//! convert that into running `cmd.exe /c` with the batch file as the next argument.
121//!
122//! For historical reasons Rust currently preserves this behavior when using
123//! [`Command::new`], and escapes the arguments according to `cmd.exe` rules.
124//! Due to the complexity of `cmd.exe` argument handling, it might not be
125//! possible to safely escape some special characters, and using them will result
126//! in an error being returned at process spawn. The set of unescapeable
127//! special characters might change between releases.
128//!
129//! Also note that running batch scripts in this way may be removed in the
130//! future and so should not be relied upon.
131//!
132//! [`spawn`]: Command::spawn
133//! [`output`]: Command::output
134//!
135//! [`stdout`]: Command::stdout
136//! [`stdin`]: Command::stdin
137//! [`stderr`]: Command::stderr
138//!
139//! [`Write`]: io::Write
140//! [`Read`]: io::Read
141//!
142//! [`arg`]: Command::arg
143//! [`args`]: Command::args
144//! [`raw_arg`]: crate::os::windows::process::CommandExt::raw_arg
145//!
146//! [`CreateProcessW`]: https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
147
148#![stable(feature = "process", since = "1.0.0")]
149#![deny(unsafe_op_in_unsafe_fn)]
150
151#[cfg(all(
152    test,
153    not(any(
154        target_os = "emscripten",
155        target_os = "wasi",
156        target_env = "sgx",
157        target_os = "xous",
158        target_os = "trusty",
159    ))
160))]
161mod tests;
162
163use crate::convert::Infallible;
164use crate::ffi::OsStr;
165use crate::io::prelude::*;
166use crate::io::{self, BorrowedCursor, IoSlice, IoSliceMut};
167use crate::num::NonZero;
168use crate::path::Path;
169use crate::sys::{AsInner, AsInnerMut, FromInner, IntoInner, process as imp};
170use crate::{fmt, format_args_nl, fs, str};
171
172/// Representation of a running or exited child process.
173///
174/// This structure is used to represent and manage child processes. A child
175/// process is created via the [`Command`] struct, which configures the
176/// spawning process and can itself be constructed using a builder-style
177/// interface.
178///
179/// There is no implementation of [`Drop`] for child processes,
180/// so if you do not ensure the `Child` has exited then it will continue to
181/// run, even after the `Child` handle to the child process has gone out of
182/// scope.
183///
184/// Calling [`wait`] (or other functions that wrap around it) will make
185/// the parent process wait until the child has actually exited before
186/// continuing.
187///
188/// # Warning
189///
190/// On some systems, calling [`wait`] or similar is necessary for the OS to
191/// release resources. A process that terminated but has not been waited on is
192/// still around as a "zombie". Leaving too many zombies around may exhaust
193/// global resources (for example process IDs).
194///
195/// The standard library does *not* automatically wait on child processes (not
196/// even if the `Child` is dropped), it is up to the application developer to do
197/// so. As a consequence, dropping `Child` handles without waiting on them first
198/// is not recommended in long-running applications.
199///
200/// # Examples
201///
202/// ```should_panic
203/// use std::process::Command;
204///
205/// let mut child = Command::new("/bin/cat")
206///     .arg("file.txt")
207///     .spawn()
208///     .expect("failed to execute child");
209///
210/// let ecode = child.wait().expect("failed to wait on child");
211///
212/// assert!(ecode.success());
213/// ```
214///
215/// [`wait`]: Child::wait
216#[stable(feature = "process", since = "1.0.0")]
217#[cfg_attr(not(test), rustc_diagnostic_item = "Child")]
218pub struct Child {
219    pub(crate) handle: imp::Process,
220
221    /// The handle for writing to the child's standard input (stdin), if it
222    /// has been captured. You might find it helpful to do
223    ///
224    /// ```ignore (incomplete)
225    /// let stdin = child.stdin.take().expect("handle present");
226    /// ```
227    ///
228    /// to avoid partially moving the `child` and thus blocking yourself from calling
229    /// functions on `child` while using `stdin`.
230    #[stable(feature = "process", since = "1.0.0")]
231    pub stdin: Option<ChildStdin>,
232
233    /// The handle for reading from the child's standard output (stdout), if it
234    /// has been captured. You might find it helpful to do
235    ///
236    /// ```ignore (incomplete)
237    /// let stdout = child.stdout.take().expect("handle present");
238    /// ```
239    ///
240    /// to avoid partially moving the `child` and thus blocking yourself from calling
241    /// functions on `child` while using `stdout`.
242    #[stable(feature = "process", since = "1.0.0")]
243    pub stdout: Option<ChildStdout>,
244
245    /// The handle for reading from the child's standard error (stderr), if it
246    /// has been captured. You might find it helpful to do
247    ///
248    /// ```ignore (incomplete)
249    /// let stderr = child.stderr.take().expect("handle present");
250    /// ```
251    ///
252    /// to avoid partially moving the `child` and thus blocking yourself from calling
253    /// functions on `child` while using `stderr`.
254    #[stable(feature = "process", since = "1.0.0")]
255    pub stderr: Option<ChildStderr>,
256}
257
258/// Allows extension traits within `std`.
259#[unstable(feature = "sealed", issue = "none")]
260impl crate::sealed::Sealed for Child {}
261
262impl AsInner<imp::Process> for Child {
263    #[inline]
264    fn as_inner(&self) -> &imp::Process {
265        &self.handle
266    }
267}
268
269impl FromInner<(imp::Process, StdioPipes)> for Child {
270    fn from_inner((handle, io): (imp::Process, StdioPipes)) -> Child {
271        Child {
272            handle,
273            stdin: io.stdin.map(ChildStdin::from_inner),
274            stdout: io.stdout.map(ChildStdout::from_inner),
275            stderr: io.stderr.map(ChildStderr::from_inner),
276        }
277    }
278}
279
280impl IntoInner<imp::Process> for Child {
281    fn into_inner(self) -> imp::Process {
282        self.handle
283    }
284}
285
286#[stable(feature = "std_debug", since = "1.16.0")]
287impl fmt::Debug for Child {
288    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
289        f.debug_struct("Child")
290            .field("stdin", &self.stdin)
291            .field("stdout", &self.stdout)
292            .field("stderr", &self.stderr)
293            .finish_non_exhaustive()
294    }
295}
296
297/// The pipes connected to a spawned process.
298///
299/// Used to pass pipe handles between this module and [`imp`].
300pub(crate) struct StdioPipes {
301    pub stdin: Option<imp::ChildPipe>,
302    pub stdout: Option<imp::ChildPipe>,
303    pub stderr: Option<imp::ChildPipe>,
304}
305
306/// A handle to a child process's standard input (stdin).
307///
308/// This struct is used in the [`stdin`] field on [`Child`].
309///
310/// When an instance of `ChildStdin` is [dropped], the `ChildStdin`'s underlying
311/// file handle will be closed. If the child process was blocked on input prior
312/// to being dropped, it will become unblocked after dropping.
313///
314/// [`stdin`]: Child::stdin
315/// [dropped]: Drop
316#[stable(feature = "process", since = "1.0.0")]
317pub struct ChildStdin {
318    inner: imp::ChildPipe,
319}
320
321// In addition to the `impl`s here, `ChildStdin` also has `impl`s for
322// `AsFd`/`From<OwnedFd>`/`Into<OwnedFd>` and
323// `AsRawFd`/`IntoRawFd`/`FromRawFd`, on Unix and WASI, and
324// `AsHandle`/`From<OwnedHandle>`/`Into<OwnedHandle>` and
325// `AsRawHandle`/`IntoRawHandle`/`FromRawHandle` on Windows.
326
327#[stable(feature = "process", since = "1.0.0")]
328impl Write for ChildStdin {
329    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
330        (&*self).write(buf)
331    }
332
333    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
334        (&*self).write_vectored(bufs)
335    }
336
337    fn is_write_vectored(&self) -> bool {
338        io::Write::is_write_vectored(&&*self)
339    }
340
341    #[inline]
342    fn flush(&mut self) -> io::Result<()> {
343        (&*self).flush()
344    }
345}
346
347#[stable(feature = "write_mt", since = "1.48.0")]
348impl Write for &ChildStdin {
349    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
350        self.inner.write(buf)
351    }
352
353    fn write_vectored(&mut self, bufs: &[IoSlice<'_>]) -> io::Result<usize> {
354        self.inner.write_vectored(bufs)
355    }
356
357    fn is_write_vectored(&self) -> bool {
358        self.inner.is_write_vectored()
359    }
360
361    #[inline]
362    fn flush(&mut self) -> io::Result<()> {
363        Ok(())
364    }
365}
366
367impl AsInner<imp::ChildPipe> for ChildStdin {
368    #[inline]
369    fn as_inner(&self) -> &imp::ChildPipe {
370        &self.inner
371    }
372}
373
374impl IntoInner<imp::ChildPipe> for ChildStdin {
375    fn into_inner(self) -> imp::ChildPipe {
376        self.inner
377    }
378}
379
380impl FromInner<imp::ChildPipe> for ChildStdin {
381    fn from_inner(pipe: imp::ChildPipe) -> ChildStdin {
382        ChildStdin { inner: pipe }
383    }
384}
385
386#[stable(feature = "std_debug", since = "1.16.0")]
387impl fmt::Debug for ChildStdin {
388    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
389        f.debug_struct("ChildStdin").finish_non_exhaustive()
390    }
391}
392
393/// A handle to a child process's standard output (stdout).
394///
395/// This struct is used in the [`stdout`] field on [`Child`].
396///
397/// When an instance of `ChildStdout` is [dropped], the `ChildStdout`'s
398/// underlying file handle will be closed.
399///
400/// [`stdout`]: Child::stdout
401/// [dropped]: Drop
402#[stable(feature = "process", since = "1.0.0")]
403pub struct ChildStdout {
404    inner: imp::ChildPipe,
405}
406
407// In addition to the `impl`s here, `ChildStdout` also has `impl`s for
408// `AsFd`/`From<OwnedFd>`/`Into<OwnedFd>` and
409// `AsRawFd`/`IntoRawFd`/`FromRawFd`, on Unix and WASI, and
410// `AsHandle`/`From<OwnedHandle>`/`Into<OwnedHandle>` and
411// `AsRawHandle`/`IntoRawHandle`/`FromRawHandle` on Windows.
412
413#[stable(feature = "process", since = "1.0.0")]
414impl Read for ChildStdout {
415    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
416        self.inner.read(buf)
417    }
418
419    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> io::Result<()> {
420        self.inner.read_buf(buf)
421    }
422
423    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> io::Result<usize> {
424        self.inner.read_vectored(bufs)
425    }
426
427    #[inline]
428    fn is_read_vectored(&self) -> bool {
429        self.inner.is_read_vectored()
430    }
431
432    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> io::Result<usize> {
433        self.inner.read_to_end(buf)
434    }
435}
436
437impl AsInner<imp::ChildPipe> for ChildStdout {
438    #[inline]
439    fn as_inner(&self) -> &imp::ChildPipe {
440        &self.inner
441    }
442}
443
444impl IntoInner<imp::ChildPipe> for ChildStdout {
445    fn into_inner(self) -> imp::ChildPipe {
446        self.inner
447    }
448}
449
450impl FromInner<imp::ChildPipe> for ChildStdout {
451    fn from_inner(pipe: imp::ChildPipe) -> ChildStdout {
452        ChildStdout { inner: pipe }
453    }
454}
455
456#[stable(feature = "std_debug", since = "1.16.0")]
457impl fmt::Debug for ChildStdout {
458    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
459        f.debug_struct("ChildStdout").finish_non_exhaustive()
460    }
461}
462
463/// A handle to a child process's stderr.
464///
465/// This struct is used in the [`stderr`] field on [`Child`].
466///
467/// When an instance of `ChildStderr` is [dropped], the `ChildStderr`'s
468/// underlying file handle will be closed.
469///
470/// [`stderr`]: Child::stderr
471/// [dropped]: Drop
472#[stable(feature = "process", since = "1.0.0")]
473pub struct ChildStderr {
474    inner: imp::ChildPipe,
475}
476
477// In addition to the `impl`s here, `ChildStderr` also has `impl`s for
478// `AsFd`/`From<OwnedFd>`/`Into<OwnedFd>` and
479// `AsRawFd`/`IntoRawFd`/`FromRawFd`, on Unix and WASI, and
480// `AsHandle`/`From<OwnedHandle>`/`Into<OwnedHandle>` and
481// `AsRawHandle`/`IntoRawHandle`/`FromRawHandle` on Windows.
482
483#[stable(feature = "process", since = "1.0.0")]
484impl Read for ChildStderr {
485    fn read(&mut self, buf: &mut [u8]) -> io::Result<usize> {
486        self.inner.read(buf)
487    }
488
489    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> io::Result<()> {
490        self.inner.read_buf(buf)
491    }
492
493    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> io::Result<usize> {
494        self.inner.read_vectored(bufs)
495    }
496
497    #[inline]
498    fn is_read_vectored(&self) -> bool {
499        self.inner.is_read_vectored()
500    }
501
502    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> io::Result<usize> {
503        self.inner.read_to_end(buf)
504    }
505}
506
507impl AsInner<imp::ChildPipe> for ChildStderr {
508    #[inline]
509    fn as_inner(&self) -> &imp::ChildPipe {
510        &self.inner
511    }
512}
513
514impl IntoInner<imp::ChildPipe> for ChildStderr {
515    fn into_inner(self) -> imp::ChildPipe {
516        self.inner
517    }
518}
519
520impl FromInner<imp::ChildPipe> for ChildStderr {
521    fn from_inner(pipe: imp::ChildPipe) -> ChildStderr {
522        ChildStderr { inner: pipe }
523    }
524}
525
526#[stable(feature = "std_debug", since = "1.16.0")]
527impl fmt::Debug for ChildStderr {
528    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
529        f.debug_struct("ChildStderr").finish_non_exhaustive()
530    }
531}
532
533/// A process builder, providing fine-grained control
534/// over how a new process should be spawned.
535///
536/// A default configuration can be
537/// generated using `Command::new(program)`, where `program` gives a path to the
538/// program to be executed. Additional builder methods allow the configuration
539/// to be changed (for example, by adding arguments) prior to spawning:
540///
541/// ```
542/// # if cfg!(not(all(target_vendor = "apple", not(target_os = "macos")))) {
543/// use std::process::Command;
544///
545/// let output = if cfg!(target_os = "windows") {
546///     Command::new("cmd")
547///         .args(["/C", "echo hello"])
548///         .output()
549///         .expect("failed to execute process")
550/// } else {
551///     Command::new("sh")
552///         .arg("-c")
553///         .arg("echo hello")
554///         .output()
555///         .expect("failed to execute process")
556/// };
557///
558/// let hello = output.stdout;
559/// # }
560/// ```
561///
562/// `Command` can be reused to spawn multiple processes. The builder methods
563/// change the command without needing to immediately spawn the process.
564///
565/// ```no_run
566/// use std::process::Command;
567///
568/// let mut echo_hello = Command::new("sh");
569/// echo_hello.arg("-c").arg("echo hello");
570/// let hello_1 = echo_hello.output().expect("failed to execute process");
571/// let hello_2 = echo_hello.output().expect("failed to execute process");
572/// ```
573///
574/// Similarly, you can call builder methods after spawning a process and then
575/// spawn a new process with the modified settings.
576///
577/// ```no_run
578/// use std::process::Command;
579///
580/// let mut list_dir = Command::new("ls");
581///
582/// // Execute `ls` in the current directory of the program.
583/// list_dir.status().expect("process failed to execute");
584///
585/// println!();
586///
587/// // Change `ls` to execute in the root directory.
588/// list_dir.current_dir("/");
589///
590/// // And then execute `ls` again but in the root directory.
591/// list_dir.status().expect("process failed to execute");
592/// ```
593#[stable(feature = "process", since = "1.0.0")]
594#[cfg_attr(not(test), rustc_diagnostic_item = "Command")]
595pub struct Command {
596    inner: imp::Command,
597}
598
599/// Allows extension traits within `std`.
600#[unstable(feature = "sealed", issue = "none")]
601impl crate::sealed::Sealed for Command {}
602
603impl Command {
604    /// Constructs a new `Command` for launching the program at
605    /// path `program`, with the following default configuration:
606    ///
607    /// * No arguments to the program
608    /// * Inherit the current process's environment
609    /// * Inherit the current process's working directory
610    /// * Inherit stdin/stdout/stderr for [`spawn`] or [`status`], but create pipes for [`output`]
611    ///
612    /// [`spawn`]: Self::spawn
613    /// [`status`]: Self::status
614    /// [`output`]: Self::output
615    ///
616    /// Builder methods are provided to change these defaults and
617    /// otherwise configure the process.
618    ///
619    /// If `program` is not an absolute path, the `PATH` will be searched in
620    /// an OS-defined way.
621    ///
622    /// The search path to be used may be controlled by setting the
623    /// `PATH` environment variable on the Command,
624    /// but this has some implementation limitations on Windows
625    /// (see issue #37519).
626    ///
627    /// # Platform-specific behavior
628    ///
629    /// Note on Windows: For executable files with the .exe extension,
630    /// it can be omitted when specifying the program for this Command.
631    /// However, if the file has a different extension,
632    /// a filename including the extension needs to be provided,
633    /// otherwise the file won't be found.
634    ///
635    /// # Examples
636    ///
637    /// ```no_run
638    /// use std::process::Command;
639    ///
640    /// Command::new("sh")
641    ///     .spawn()
642    ///     .expect("sh command failed to start");
643    /// ```
644    ///
645    /// # Caveats
646    ///
647    /// [`Command::new`] is only intended to accept the path of the program. If you pass a program
648    /// path along with arguments like `Command::new("ls -l").spawn()`, it will try to search for
649    /// `ls -l` literally. The arguments need to be passed separately, such as via [`arg`] or
650    /// [`args`].
651    ///
652    /// ```no_run
653    /// use std::process::Command;
654    ///
655    /// Command::new("ls")
656    ///     .arg("-l") // arg passed separately
657    ///     .spawn()
658    ///     .expect("ls command failed to start");
659    /// ```
660    ///
661    /// [`arg`]: Self::arg
662    /// [`args`]: Self::args
663    #[stable(feature = "process", since = "1.0.0")]
664    pub fn new<S: AsRef<OsStr>>(program: S) -> Command {
665        Command { inner: imp::Command::new(program.as_ref()) }
666    }
667
668    /// Adds an argument to pass to the program.
669    ///
670    /// Only one argument can be passed per use. So instead of:
671    ///
672    /// ```no_run
673    /// # std::process::Command::new("sh")
674    /// .arg("-C /path/to/repo")
675    /// # ;
676    /// ```
677    ///
678    /// usage would be:
679    ///
680    /// ```no_run
681    /// # std::process::Command::new("sh")
682    /// .arg("-C")
683    /// .arg("/path/to/repo")
684    /// # ;
685    /// ```
686    ///
687    /// To pass multiple arguments see [`args`].
688    ///
689    /// [`args`]: Command::args
690    ///
691    /// Note that the argument is not passed through a shell, but given
692    /// literally to the program. This means that shell syntax like quotes,
693    /// escaped characters, word splitting, glob patterns, variable substitution,
694    /// etc. have no effect.
695    ///
696    /// <div class="warning">
697    ///
698    /// On Windows, use caution with untrusted inputs. Most applications use the
699    /// standard convention for decoding arguments passed to them. These are safe to
700    /// use with `arg`. However, some applications such as `cmd.exe` and `.bat` files
701    /// use a non-standard way of decoding arguments. They are therefore vulnerable
702    /// to malicious input.
703    ///
704    /// In the case of `cmd.exe` this is especially important because a malicious
705    /// argument can potentially run arbitrary shell commands.
706    ///
707    /// See [Windows argument splitting][windows-args] for more details
708    /// or [`raw_arg`] for manually implementing non-standard argument encoding.
709    ///
710    /// [`raw_arg`]: crate::os::windows::process::CommandExt::raw_arg
711    /// [windows-args]: crate::process#windows-argument-splitting
712    ///
713    /// </div>
714    ///
715    /// # Examples
716    ///
717    /// ```no_run
718    /// use std::process::Command;
719    ///
720    /// Command::new("ls")
721    ///     .arg("-l")
722    ///     .arg("-a")
723    ///     .spawn()
724    ///     .expect("ls command failed to start");
725    /// ```
726    #[stable(feature = "process", since = "1.0.0")]
727    pub fn arg<S: AsRef<OsStr>>(&mut self, arg: S) -> &mut Command {
728        self.inner.arg(arg.as_ref());
729        self
730    }
731
732    /// Adds multiple arguments to pass to the program.
733    ///
734    /// To pass a single argument see [`arg`].
735    ///
736    /// [`arg`]: Command::arg
737    ///
738    /// Note that the arguments are not passed through a shell, but given
739    /// literally to the program. This means that shell syntax like quotes,
740    /// escaped characters, word splitting, glob patterns, variable substitution, etc.
741    /// have no effect.
742    ///
743    /// <div class="warning">
744    ///
745    /// On Windows, use caution with untrusted inputs. Most applications use the
746    /// standard convention for decoding arguments passed to them. These are safe to
747    /// use with `arg`. However, some applications such as `cmd.exe` and `.bat` files
748    /// use a non-standard way of decoding arguments. They are therefore vulnerable
749    /// to malicious input.
750    ///
751    /// In the case of `cmd.exe` this is especially important because a malicious
752    /// argument can potentially run arbitrary shell commands.
753    ///
754    /// See [Windows argument splitting][windows-args] for more details
755    /// or [`raw_arg`] for manually implementing non-standard argument encoding.
756    ///
757    /// [`raw_arg`]: crate::os::windows::process::CommandExt::raw_arg
758    /// [windows-args]: crate::process#windows-argument-splitting
759    ///
760    /// </div>
761    ///
762    /// # Examples
763    ///
764    /// ```no_run
765    /// use std::process::Command;
766    ///
767    /// Command::new("ls")
768    ///     .args(["-l", "-a"])
769    ///     .spawn()
770    ///     .expect("ls command failed to start");
771    /// ```
772    #[stable(feature = "process", since = "1.0.0")]
773    pub fn args<I, S>(&mut self, args: I) -> &mut Command
774    where
775        I: IntoIterator<Item = S>,
776        S: AsRef<OsStr>,
777    {
778        for arg in args {
779            self.arg(arg.as_ref());
780        }
781        self
782    }
783
784    /// Inserts or updates an explicit environment variable mapping.
785    ///
786    /// This method allows you to add an environment variable mapping to the spawned process or
787    /// overwrite a previously set value. You can use [`Command::envs`] to set multiple environment
788    /// variables simultaneously.
789    ///
790    /// Child processes will inherit environment variables from their parent process by default.
791    /// Environment variables explicitly set using [`Command::env`] take precedence over inherited
792    /// variables. You can disable environment variable inheritance entirely using
793    /// [`Command::env_clear`] or for a single key using [`Command::env_remove`].
794    ///
795    /// Note that environment variable names are case-insensitive (but
796    /// case-preserving) on Windows and case-sensitive on all other platforms.
797    ///
798    /// # Examples
799    ///
800    /// ```no_run
801    /// use std::process::Command;
802    ///
803    /// Command::new("ls")
804    ///     .env("PATH", "/bin")
805    ///     .spawn()
806    ///     .expect("ls command failed to start");
807    /// ```
808    #[stable(feature = "process", since = "1.0.0")]
809    pub fn env<K, V>(&mut self, key: K, val: V) -> &mut Command
810    where
811        K: AsRef<OsStr>,
812        V: AsRef<OsStr>,
813    {
814        self.inner.env_mut().set(key.as_ref(), val.as_ref());
815        self
816    }
817
818    /// Inserts or updates multiple explicit environment variable mappings.
819    ///
820    /// This method allows you to add multiple environment variable mappings to the spawned process
821    /// or overwrite previously set values. You can use [`Command::env`] to set a single environment
822    /// variable.
823    ///
824    /// Child processes will inherit environment variables from their parent process by default.
825    /// Environment variables explicitly set using [`Command::envs`] take precedence over inherited
826    /// variables. You can disable environment variable inheritance entirely using
827    /// [`Command::env_clear`] or for a single key using [`Command::env_remove`].
828    ///
829    /// Note that environment variable names are case-insensitive (but case-preserving) on Windows
830    /// and case-sensitive on all other platforms.
831    ///
832    /// # Examples
833    ///
834    /// ```no_run
835    /// use std::process::{Command, Stdio};
836    /// use std::env;
837    /// use std::collections::HashMap;
838    ///
839    /// let filtered_env : HashMap<String, String> =
840    ///     env::vars().filter(|&(ref k, _)|
841    ///         k == "TERM" || k == "TZ" || k == "LANG" || k == "PATH"
842    ///     ).collect();
843    ///
844    /// Command::new("printenv")
845    ///     .stdin(Stdio::null())
846    ///     .stdout(Stdio::inherit())
847    ///     .env_clear()
848    ///     .envs(&filtered_env)
849    ///     .spawn()
850    ///     .expect("printenv failed to start");
851    /// ```
852    #[stable(feature = "command_envs", since = "1.19.0")]
853    pub fn envs<I, K, V>(&mut self, vars: I) -> &mut Command
854    where
855        I: IntoIterator<Item = (K, V)>,
856        K: AsRef<OsStr>,
857        V: AsRef<OsStr>,
858    {
859        for (ref key, ref val) in vars {
860            self.inner.env_mut().set(key.as_ref(), val.as_ref());
861        }
862        self
863    }
864
865    /// Removes an explicitly set environment variable and prevents inheriting it from a parent
866    /// process.
867    ///
868    /// This method will remove the explicit value of an environment variable set via
869    /// [`Command::env`] or [`Command::envs`]. In addition, it will prevent the spawned child
870    /// process from inheriting that environment variable from its parent process.
871    ///
872    /// After calling [`Command::env_remove`], the value associated with its key from
873    /// [`Command::get_envs`] will be [`None`].
874    ///
875    /// To clear all explicitly set environment variables and disable all environment variable
876    /// inheritance, you can use [`Command::env_clear`].
877    ///
878    /// # Examples
879    ///
880    /// Prevent any inherited `GIT_DIR` variable from changing the target of the `git` command,
881    /// while allowing all other variables, like `GIT_AUTHOR_NAME`.
882    ///
883    /// ```no_run
884    /// use std::process::Command;
885    ///
886    /// Command::new("git")
887    ///     .arg("commit")
888    ///     .env_remove("GIT_DIR")
889    ///     .spawn()?;
890    /// # std::io::Result::Ok(())
891    /// ```
892    #[stable(feature = "process", since = "1.0.0")]
893    pub fn env_remove<K: AsRef<OsStr>>(&mut self, key: K) -> &mut Command {
894        self.inner.env_mut().remove(key.as_ref());
895        self
896    }
897
898    /// Clears all explicitly set environment variables and prevents inheriting any parent process
899    /// environment variables.
900    ///
901    /// This method will remove all explicitly added environment variables set via [`Command::env`]
902    /// or [`Command::envs`]. In addition, it will prevent the spawned child process from inheriting
903    /// any environment variable from its parent process.
904    ///
905    /// After calling [`Command::env_clear`], the iterator from [`Command::get_envs`] will be
906    /// empty.
907    ///
908    /// You can use [`Command::env_remove`] to clear a single mapping.
909    ///
910    /// # Examples
911    ///
912    /// The behavior of `sort` is affected by `LANG` and `LC_*` environment variables.
913    /// Clearing the environment makes `sort`'s behavior independent of the parent processes' language.
914    ///
915    /// ```no_run
916    /// use std::process::Command;
917    ///
918    /// Command::new("sort")
919    ///     .arg("file.txt")
920    ///     .env_clear()
921    ///     .spawn()?;
922    /// # std::io::Result::Ok(())
923    /// ```
924    #[stable(feature = "process", since = "1.0.0")]
925    pub fn env_clear(&mut self) -> &mut Command {
926        self.inner.env_mut().clear();
927        self
928    }
929
930    /// Sets the working directory for the child process.
931    ///
932    /// # Platform-specific behavior
933    ///
934    /// If the program path is relative (e.g., `"./script.sh"`), it's ambiguous
935    /// whether it should be interpreted relative to the parent's working
936    /// directory or relative to `current_dir`. The behavior in this case is
937    /// platform specific and unstable, and it's recommended to use
938    /// [`canonicalize`] to get an absolute program path instead.
939    ///
940    /// # Examples
941    ///
942    /// ```no_run
943    /// use std::process::Command;
944    ///
945    /// Command::new("ls")
946    ///     .current_dir("/bin")
947    ///     .spawn()
948    ///     .expect("ls command failed to start");
949    /// ```
950    ///
951    /// [`canonicalize`]: crate::fs::canonicalize
952    #[stable(feature = "process", since = "1.0.0")]
953    pub fn current_dir<P: AsRef<Path>>(&mut self, dir: P) -> &mut Command {
954        self.inner.cwd(dir.as_ref().as_ref());
955        self
956    }
957
958    /// Configuration for the child process's standard input (stdin) handle.
959    ///
960    /// Defaults to [`inherit`] when used with [`spawn`] or [`status`], and
961    /// defaults to [`piped`] when used with [`output`].
962    ///
963    /// [`inherit`]: Stdio::inherit
964    /// [`piped`]: Stdio::piped
965    /// [`spawn`]: Self::spawn
966    /// [`status`]: Self::status
967    /// [`output`]: Self::output
968    ///
969    /// # Examples
970    ///
971    /// ```no_run
972    /// use std::process::{Command, Stdio};
973    ///
974    /// Command::new("ls")
975    ///     .stdin(Stdio::null())
976    ///     .spawn()
977    ///     .expect("ls command failed to start");
978    /// ```
979    #[stable(feature = "process", since = "1.0.0")]
980    pub fn stdin<T: Into<Stdio>>(&mut self, cfg: T) -> &mut Command {
981        self.inner.stdin(cfg.into().0);
982        self
983    }
984
985    /// Configuration for the child process's standard output (stdout) handle.
986    ///
987    /// Defaults to [`inherit`] when used with [`spawn`] or [`status`], and
988    /// defaults to [`piped`] when used with [`output`].
989    ///
990    /// [`inherit`]: Stdio::inherit
991    /// [`piped`]: Stdio::piped
992    /// [`spawn`]: Self::spawn
993    /// [`status`]: Self::status
994    /// [`output`]: Self::output
995    ///
996    /// # Examples
997    ///
998    /// ```no_run
999    /// use std::process::{Command, Stdio};
1000    ///
1001    /// Command::new("ls")
1002    ///     .stdout(Stdio::null())
1003    ///     .spawn()
1004    ///     .expect("ls command failed to start");
1005    /// ```
1006    #[stable(feature = "process", since = "1.0.0")]
1007    pub fn stdout<T: Into<Stdio>>(&mut self, cfg: T) -> &mut Command {
1008        self.inner.stdout(cfg.into().0);
1009        self
1010    }
1011
1012    /// Configuration for the child process's standard error (stderr) handle.
1013    ///
1014    /// Defaults to [`inherit`] when used with [`spawn`] or [`status`], and
1015    /// defaults to [`piped`] when used with [`output`].
1016    ///
1017    /// [`inherit`]: Stdio::inherit
1018    /// [`piped`]: Stdio::piped
1019    /// [`spawn`]: Self::spawn
1020    /// [`status`]: Self::status
1021    /// [`output`]: Self::output
1022    ///
1023    /// # Examples
1024    ///
1025    /// ```no_run
1026    /// use std::process::{Command, Stdio};
1027    ///
1028    /// Command::new("ls")
1029    ///     .stderr(Stdio::null())
1030    ///     .spawn()
1031    ///     .expect("ls command failed to start");
1032    /// ```
1033    #[stable(feature = "process", since = "1.0.0")]
1034    pub fn stderr<T: Into<Stdio>>(&mut self, cfg: T) -> &mut Command {
1035        self.inner.stderr(cfg.into().0);
1036        self
1037    }
1038
1039    /// Executes the command as a child process, returning a handle to it.
1040    ///
1041    /// By default, stdin, stdout and stderr are inherited from the parent.
1042    ///
1043    /// # Examples
1044    ///
1045    /// ```no_run
1046    /// use std::process::Command;
1047    ///
1048    /// Command::new("ls")
1049    ///     .spawn()
1050    ///     .expect("ls command failed to start");
1051    /// ```
1052    #[stable(feature = "process", since = "1.0.0")]
1053    pub fn spawn(&mut self) -> io::Result<Child> {
1054        self.inner.spawn(imp::Stdio::Inherit, true).map(Child::from_inner)
1055    }
1056
1057    /// Executes the command as a child process, waiting for it to finish and
1058    /// collecting all of its output.
1059    ///
1060    /// By default, stdout and stderr are captured (and used to provide the
1061    /// resulting output). Stdin is not inherited from the parent and any
1062    /// attempt by the child process to read from the stdin stream will result
1063    /// in the stream immediately closing.
1064    ///
1065    /// # Examples
1066    ///
1067    /// ```should_panic
1068    /// use std::process::Command;
1069    /// use std::io::{self, Write};
1070    /// let output = Command::new("/bin/cat")
1071    ///     .arg("file.txt")
1072    ///     .output()?;
1073    ///
1074    /// println!("status: {}", output.status);
1075    /// io::stdout().write_all(&output.stdout)?;
1076    /// io::stderr().write_all(&output.stderr)?;
1077    ///
1078    /// assert!(output.status.success());
1079    /// # io::Result::Ok(())
1080    /// ```
1081    #[stable(feature = "process", since = "1.0.0")]
1082    pub fn output(&mut self) -> io::Result<Output> {
1083        let (status, stdout, stderr) = imp::output(&mut self.inner)?;
1084        Ok(Output { status: ExitStatus(status), stdout, stderr })
1085    }
1086
1087    /// Executes a command as a child process, waiting for it to finish and
1088    /// collecting its status.
1089    ///
1090    /// By default, stdin, stdout and stderr are inherited from the parent.
1091    ///
1092    /// # Examples
1093    ///
1094    /// ```should_panic
1095    /// use std::process::Command;
1096    ///
1097    /// let status = Command::new("/bin/cat")
1098    ///     .arg("file.txt")
1099    ///     .status()
1100    ///     .expect("failed to execute process");
1101    ///
1102    /// println!("process finished with: {status}");
1103    ///
1104    /// assert!(status.success());
1105    /// ```
1106    #[stable(feature = "process", since = "1.0.0")]
1107    pub fn status(&mut self) -> io::Result<ExitStatus> {
1108        self.inner
1109            .spawn(imp::Stdio::Inherit, true)
1110            .map(Child::from_inner)
1111            .and_then(|mut p| p.wait())
1112    }
1113
1114    /// Returns the path to the program that was given to [`Command::new`].
1115    ///
1116    /// # Examples
1117    ///
1118    /// ```
1119    /// use std::process::Command;
1120    ///
1121    /// let cmd = Command::new("echo");
1122    /// assert_eq!(cmd.get_program(), "echo");
1123    /// ```
1124    #[must_use]
1125    #[stable(feature = "command_access", since = "1.57.0")]
1126    pub fn get_program(&self) -> &OsStr {
1127        self.inner.get_program()
1128    }
1129
1130    /// Returns an iterator of the arguments that will be passed to the program.
1131    ///
1132    /// This does not include the path to the program as the first argument;
1133    /// it only includes the arguments specified with [`Command::arg`] and
1134    /// [`Command::args`].
1135    ///
1136    /// # Examples
1137    ///
1138    /// ```
1139    /// use std::ffi::OsStr;
1140    /// use std::process::Command;
1141    ///
1142    /// let mut cmd = Command::new("echo");
1143    /// cmd.arg("first").arg("second");
1144    /// let args: Vec<&OsStr> = cmd.get_args().collect();
1145    /// assert_eq!(args, &["first", "second"]);
1146    /// ```
1147    #[stable(feature = "command_access", since = "1.57.0")]
1148    pub fn get_args(&self) -> CommandArgs<'_> {
1149        CommandArgs { inner: self.inner.get_args() }
1150    }
1151
1152    /// Returns an iterator of the environment variables explicitly set for the child process.
1153    ///
1154    /// Environment variables explicitly set using [`Command::env`], [`Command::envs`], and
1155    /// [`Command::env_remove`] can be retrieved with this method.
1156    ///
1157    /// Note that this output does not include environment variables inherited from the parent
1158    /// process.
1159    ///
1160    /// Each element is a tuple key/value pair `(&OsStr, Option<&OsStr>)`. A [`None`] value
1161    /// indicates its key was explicitly removed via [`Command::env_remove`]. The associated key for
1162    /// the [`None`] value will no longer inherit from its parent process.
1163    ///
1164    /// An empty iterator can indicate that no explicit mappings were added or that
1165    /// [`Command::env_clear`] was called. After calling [`Command::env_clear`], the child process
1166    /// will not inherit any environment variables from its parent process.
1167    ///
1168    /// # Examples
1169    ///
1170    /// ```
1171    /// use std::ffi::OsStr;
1172    /// use std::process::Command;
1173    ///
1174    /// let mut cmd = Command::new("ls");
1175    /// cmd.env("TERM", "dumb").env_remove("TZ");
1176    /// let envs: Vec<(&OsStr, Option<&OsStr>)> = cmd.get_envs().collect();
1177    /// assert_eq!(envs, &[
1178    ///     (OsStr::new("TERM"), Some(OsStr::new("dumb"))),
1179    ///     (OsStr::new("TZ"), None)
1180    /// ]);
1181    /// ```
1182    #[stable(feature = "command_access", since = "1.57.0")]
1183    pub fn get_envs(&self) -> CommandEnvs<'_> {
1184        CommandEnvs { iter: self.inner.get_envs() }
1185    }
1186
1187    /// Returns the working directory for the child process.
1188    ///
1189    /// This returns [`None`] if the working directory will not be changed.
1190    ///
1191    /// # Examples
1192    ///
1193    /// ```
1194    /// use std::path::Path;
1195    /// use std::process::Command;
1196    ///
1197    /// let mut cmd = Command::new("ls");
1198    /// assert_eq!(cmd.get_current_dir(), None);
1199    /// cmd.current_dir("/bin");
1200    /// assert_eq!(cmd.get_current_dir(), Some(Path::new("/bin")));
1201    /// ```
1202    #[must_use]
1203    #[stable(feature = "command_access", since = "1.57.0")]
1204    pub fn get_current_dir(&self) -> Option<&Path> {
1205        self.inner.get_current_dir()
1206    }
1207
1208    /// Returns whether the environment will be cleared for the child process.
1209    ///
1210    /// This returns `true` if [`Command::env_clear`] was called, and `false` otherwise.
1211    /// When `true`, the child process will not inherit any environment variables from
1212    /// its parent process.
1213    ///
1214    /// # Examples
1215    ///
1216    /// ```
1217    /// #![feature(command_resolved_envs)]
1218    /// use std::process::Command;
1219    ///
1220    /// let mut cmd = Command::new("ls");
1221    /// assert_eq!(cmd.get_env_clear(), false);
1222    ///
1223    /// cmd.env_clear();
1224    /// assert_eq!(cmd.get_env_clear(), true);
1225    /// ```
1226    #[must_use]
1227    #[unstable(feature = "command_resolved_envs", issue = "149070")]
1228    pub fn get_env_clear(&self) -> bool {
1229        self.inner.get_env_clear()
1230    }
1231}
1232
1233#[stable(feature = "rust1", since = "1.0.0")]
1234impl fmt::Debug for Command {
1235    /// Format the program and arguments of a Command for display. Any
1236    /// non-utf8 data is lossily converted using the utf8 replacement
1237    /// character.
1238    ///
1239    /// The default format approximates a shell invocation of the program along with its
1240    /// arguments. It does not include most of the other command properties. The output is not guaranteed to work
1241    /// (e.g. due to lack of shell-escaping or differences in path resolution).
1242    /// On some platforms you can use [the alternate syntax] to show more fields.
1243    ///
1244    /// Note that the debug implementation is platform-specific.
1245    ///
1246    /// [the alternate syntax]: fmt#sign0
1247    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1248        self.inner.fmt(f)
1249    }
1250}
1251
1252impl AsInner<imp::Command> for Command {
1253    #[inline]
1254    fn as_inner(&self) -> &imp::Command {
1255        &self.inner
1256    }
1257}
1258
1259impl AsInnerMut<imp::Command> for Command {
1260    #[inline]
1261    fn as_inner_mut(&mut self) -> &mut imp::Command {
1262        &mut self.inner
1263    }
1264}
1265
1266/// An iterator over the command arguments.
1267///
1268/// This struct is created by [`Command::get_args`]. See its documentation for
1269/// more.
1270#[must_use = "iterators are lazy and do nothing unless consumed"]
1271#[stable(feature = "command_access", since = "1.57.0")]
1272#[derive(Debug)]
1273pub struct CommandArgs<'a> {
1274    inner: imp::CommandArgs<'a>,
1275}
1276
1277#[stable(feature = "command_access", since = "1.57.0")]
1278impl<'a> Iterator for CommandArgs<'a> {
1279    type Item = &'a OsStr;
1280    fn next(&mut self) -> Option<&'a OsStr> {
1281        self.inner.next()
1282    }
1283    fn size_hint(&self) -> (usize, Option<usize>) {
1284        self.inner.size_hint()
1285    }
1286}
1287
1288#[stable(feature = "command_access", since = "1.57.0")]
1289impl<'a> ExactSizeIterator for CommandArgs<'a> {
1290    fn len(&self) -> usize {
1291        self.inner.len()
1292    }
1293    fn is_empty(&self) -> bool {
1294        self.inner.is_empty()
1295    }
1296}
1297
1298/// An iterator over the command environment variables.
1299///
1300/// This struct is created by
1301/// [`Command::get_envs`][crate::process::Command::get_envs]. See its
1302/// documentation for more.
1303#[must_use = "iterators are lazy and do nothing unless consumed"]
1304#[stable(feature = "command_access", since = "1.57.0")]
1305pub struct CommandEnvs<'a> {
1306    iter: imp::CommandEnvs<'a>,
1307}
1308
1309#[stable(feature = "command_access", since = "1.57.0")]
1310impl<'a> Iterator for CommandEnvs<'a> {
1311    type Item = (&'a OsStr, Option<&'a OsStr>);
1312
1313    fn next(&mut self) -> Option<Self::Item> {
1314        self.iter.next()
1315    }
1316
1317    fn size_hint(&self) -> (usize, Option<usize>) {
1318        self.iter.size_hint()
1319    }
1320}
1321
1322#[stable(feature = "command_access", since = "1.57.0")]
1323impl<'a> ExactSizeIterator for CommandEnvs<'a> {
1324    fn len(&self) -> usize {
1325        self.iter.len()
1326    }
1327
1328    fn is_empty(&self) -> bool {
1329        self.iter.is_empty()
1330    }
1331}
1332
1333#[stable(feature = "command_access", since = "1.57.0")]
1334impl<'a> fmt::Debug for CommandEnvs<'a> {
1335    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1336        self.iter.fmt(f)
1337    }
1338}
1339
1340/// The output of a finished process.
1341///
1342/// This is returned in a Result by either the [`output`] method of a
1343/// [`Command`], or the [`wait_with_output`] method of a [`Child`]
1344/// process.
1345///
1346/// [`output`]: Command::output
1347/// [`wait_with_output`]: Child::wait_with_output
1348#[derive(PartialEq, Eq, Clone)]
1349#[stable(feature = "process", since = "1.0.0")]
1350pub struct Output {
1351    /// The status (exit code) of the process.
1352    #[stable(feature = "process", since = "1.0.0")]
1353    pub status: ExitStatus,
1354    /// The data that the process wrote to stdout.
1355    #[stable(feature = "process", since = "1.0.0")]
1356    pub stdout: Vec<u8>,
1357    /// The data that the process wrote to stderr.
1358    #[stable(feature = "process", since = "1.0.0")]
1359    pub stderr: Vec<u8>,
1360}
1361
1362impl Output {
1363    /// Returns an error if a nonzero exit status was received.
1364    ///
1365    /// If the [`Command`] exited successfully,
1366    /// `self` is returned.
1367    ///
1368    /// This is equivalent to calling [`exit_ok`](ExitStatus::exit_ok)
1369    /// on [`Output.status`](Output::status).
1370    ///
1371    /// Note that this will throw away the [`Output::stderr`] field in the error case.
1372    /// If the child process outputs useful informantion to stderr, you can:
1373    /// * Use `cmd.stderr(Stdio::inherit())` to forward the
1374    ///   stderr child process to the parent's stderr,
1375    ///   usually printing it to console where the user can see it.
1376    ///   This is usually correct for command-line applications.
1377    /// * Capture `stderr` using a custom error type.
1378    ///   This is usually correct for libraries.
1379    ///
1380    /// # Examples
1381    ///
1382    /// ```
1383    /// #![feature(exit_status_error)]
1384    /// # #[cfg(all(unix, not(target_os = "android"), not(all(target_vendor = "apple", not(target_os = "macos")))))] {
1385    /// use std::process::Command;
1386    /// assert!(Command::new("false").output().unwrap().exit_ok().is_err());
1387    /// # }
1388    /// ```
1389    #[unstable(feature = "exit_status_error", issue = "84908")]
1390    pub fn exit_ok(self) -> Result<Self, ExitStatusError> {
1391        self.status.exit_ok()?;
1392        Ok(self)
1393    }
1394}
1395
1396// If either stderr or stdout are valid utf8 strings it prints the valid
1397// strings, otherwise it prints the byte sequence instead
1398#[stable(feature = "process_output_debug", since = "1.7.0")]
1399impl fmt::Debug for Output {
1400    fn fmt(&self, fmt: &mut fmt::Formatter<'_>) -> fmt::Result {
1401        let stdout_utf8 = str::from_utf8(&self.stdout);
1402        let stdout_debug: &dyn fmt::Debug = match stdout_utf8 {
1403            Ok(ref s) => s,
1404            Err(_) => &self.stdout,
1405        };
1406
1407        let stderr_utf8 = str::from_utf8(&self.stderr);
1408        let stderr_debug: &dyn fmt::Debug = match stderr_utf8 {
1409            Ok(ref s) => s,
1410            Err(_) => &self.stderr,
1411        };
1412
1413        fmt.debug_struct("Output")
1414            .field("status", &self.status)
1415            .field("stdout", stdout_debug)
1416            .field("stderr", stderr_debug)
1417            .finish()
1418    }
1419}
1420
1421/// Describes what to do with a standard I/O stream for a child process when
1422/// passed to the [`stdin`], [`stdout`], and [`stderr`] methods of [`Command`].
1423///
1424/// [`stdin`]: Command::stdin
1425/// [`stdout`]: Command::stdout
1426/// [`stderr`]: Command::stderr
1427#[stable(feature = "process", since = "1.0.0")]
1428pub struct Stdio(imp::Stdio);
1429
1430impl Stdio {
1431    /// A new pipe should be arranged to connect the parent and child processes.
1432    ///
1433    /// # Examples
1434    ///
1435    /// With stdout:
1436    ///
1437    /// ```no_run
1438    /// use std::process::{Command, Stdio};
1439    ///
1440    /// let output = Command::new("echo")
1441    ///     .arg("Hello, world!")
1442    ///     .stdout(Stdio::piped())
1443    ///     .output()
1444    ///     .expect("Failed to execute command");
1445    ///
1446    /// assert_eq!(String::from_utf8_lossy(&output.stdout), "Hello, world!\n");
1447    /// // Nothing echoed to console
1448    /// ```
1449    ///
1450    /// With stdin:
1451    ///
1452    /// ```no_run
1453    /// use std::io::Write;
1454    /// use std::process::{Command, Stdio};
1455    ///
1456    /// let mut child = Command::new("rev")
1457    ///     .stdin(Stdio::piped())
1458    ///     .stdout(Stdio::piped())
1459    ///     .spawn()
1460    ///     .expect("Failed to spawn child process");
1461    ///
1462    /// let mut stdin = child.stdin.take().expect("Failed to open stdin");
1463    /// std::thread::spawn(move || {
1464    ///     stdin.write_all("Hello, world!".as_bytes()).expect("Failed to write to stdin");
1465    /// });
1466    ///
1467    /// let output = child.wait_with_output().expect("Failed to read stdout");
1468    /// assert_eq!(String::from_utf8_lossy(&output.stdout), "!dlrow ,olleH");
1469    /// ```
1470    ///
1471    /// Writing more than a pipe buffer's worth of input to stdin without also reading
1472    /// stdout and stderr at the same time may cause a deadlock.
1473    /// This is an issue when running any program that doesn't guarantee that it reads
1474    /// its entire stdin before writing more than a pipe buffer's worth of output.
1475    /// The size of a pipe buffer varies on different targets.
1476    ///
1477    #[must_use]
1478    #[stable(feature = "process", since = "1.0.0")]
1479    pub fn piped() -> Stdio {
1480        Stdio(imp::Stdio::MakePipe)
1481    }
1482
1483    /// The child inherits from the corresponding parent descriptor.
1484    ///
1485    /// # Examples
1486    ///
1487    /// With stdout:
1488    ///
1489    /// ```no_run
1490    /// use std::process::{Command, Stdio};
1491    ///
1492    /// let output = Command::new("echo")
1493    ///     .arg("Hello, world!")
1494    ///     .stdout(Stdio::inherit())
1495    ///     .output()
1496    ///     .expect("Failed to execute command");
1497    ///
1498    /// assert_eq!(String::from_utf8_lossy(&output.stdout), "");
1499    /// // "Hello, world!" echoed to console
1500    /// ```
1501    ///
1502    /// With stdin:
1503    ///
1504    /// ```no_run
1505    /// use std::process::{Command, Stdio};
1506    /// use std::io::{self, Write};
1507    ///
1508    /// let output = Command::new("rev")
1509    ///     .stdin(Stdio::inherit())
1510    ///     .stdout(Stdio::piped())
1511    ///     .output()?;
1512    ///
1513    /// print!("You piped in the reverse of: ");
1514    /// io::stdout().write_all(&output.stdout)?;
1515    /// # io::Result::Ok(())
1516    /// ```
1517    #[must_use]
1518    #[stable(feature = "process", since = "1.0.0")]
1519    pub fn inherit() -> Stdio {
1520        Stdio(imp::Stdio::Inherit)
1521    }
1522
1523    /// This stream will be ignored. This is the equivalent of attaching the
1524    /// stream to `/dev/null`.
1525    ///
1526    /// # Examples
1527    ///
1528    /// With stdout:
1529    ///
1530    /// ```no_run
1531    /// use std::process::{Command, Stdio};
1532    ///
1533    /// let output = Command::new("echo")
1534    ///     .arg("Hello, world!")
1535    ///     .stdout(Stdio::null())
1536    ///     .output()
1537    ///     .expect("Failed to execute command");
1538    ///
1539    /// assert_eq!(String::from_utf8_lossy(&output.stdout), "");
1540    /// // Nothing echoed to console
1541    /// ```
1542    ///
1543    /// With stdin:
1544    ///
1545    /// ```no_run
1546    /// use std::process::{Command, Stdio};
1547    ///
1548    /// let output = Command::new("rev")
1549    ///     .stdin(Stdio::null())
1550    ///     .stdout(Stdio::piped())
1551    ///     .output()
1552    ///     .expect("Failed to execute command");
1553    ///
1554    /// assert_eq!(String::from_utf8_lossy(&output.stdout), "");
1555    /// // Ignores any piped-in input
1556    /// ```
1557    #[must_use]
1558    #[stable(feature = "process", since = "1.0.0")]
1559    pub fn null() -> Stdio {
1560        Stdio(imp::Stdio::Null)
1561    }
1562
1563    /// Returns `true` if this requires [`Command`] to create a new pipe.
1564    ///
1565    /// # Example
1566    ///
1567    /// ```
1568    /// #![feature(stdio_makes_pipe)]
1569    /// use std::process::Stdio;
1570    ///
1571    /// let io = Stdio::piped();
1572    /// assert_eq!(io.makes_pipe(), true);
1573    /// ```
1574    #[unstable(feature = "stdio_makes_pipe", issue = "98288")]
1575    pub fn makes_pipe(&self) -> bool {
1576        matches!(self.0, imp::Stdio::MakePipe)
1577    }
1578}
1579
1580impl FromInner<imp::Stdio> for Stdio {
1581    fn from_inner(inner: imp::Stdio) -> Stdio {
1582        Stdio(inner)
1583    }
1584}
1585
1586#[stable(feature = "std_debug", since = "1.16.0")]
1587impl fmt::Debug for Stdio {
1588    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1589        f.debug_struct("Stdio").finish_non_exhaustive()
1590    }
1591}
1592
1593#[stable(feature = "stdio_from", since = "1.20.0")]
1594impl From<ChildStdin> for Stdio {
1595    /// Converts a [`ChildStdin`] into a [`Stdio`].
1596    ///
1597    /// # Examples
1598    ///
1599    /// `ChildStdin` will be converted to `Stdio` using `Stdio::from` under the hood.
1600    ///
1601    /// ```rust,no_run
1602    /// use std::process::{Command, Stdio};
1603    ///
1604    /// let reverse = Command::new("rev")
1605    ///     .stdin(Stdio::piped())
1606    ///     .spawn()
1607    ///     .expect("failed reverse command");
1608    ///
1609    /// let _echo = Command::new("echo")
1610    ///     .arg("Hello, world!")
1611    ///     .stdout(reverse.stdin.unwrap()) // Converted into a Stdio here
1612    ///     .output()
1613    ///     .expect("failed echo command");
1614    ///
1615    /// // "!dlrow ,olleH" echoed to console
1616    /// ```
1617    fn from(child: ChildStdin) -> Stdio {
1618        Stdio::from_inner(child.into_inner().into())
1619    }
1620}
1621
1622#[stable(feature = "stdio_from", since = "1.20.0")]
1623impl From<ChildStdout> for Stdio {
1624    /// Converts a [`ChildStdout`] into a [`Stdio`].
1625    ///
1626    /// # Examples
1627    ///
1628    /// `ChildStdout` will be converted to `Stdio` using `Stdio::from` under the hood.
1629    ///
1630    /// ```rust,no_run
1631    /// use std::process::{Command, Stdio};
1632    ///
1633    /// let hello = Command::new("echo")
1634    ///     .arg("Hello, world!")
1635    ///     .stdout(Stdio::piped())
1636    ///     .spawn()
1637    ///     .expect("failed echo command");
1638    ///
1639    /// let reverse = Command::new("rev")
1640    ///     .stdin(hello.stdout.unwrap())  // Converted into a Stdio here
1641    ///     .output()
1642    ///     .expect("failed reverse command");
1643    ///
1644    /// assert_eq!(reverse.stdout, b"!dlrow ,olleH\n");
1645    /// ```
1646    fn from(child: ChildStdout) -> Stdio {
1647        Stdio::from_inner(child.into_inner().into())
1648    }
1649}
1650
1651#[stable(feature = "stdio_from", since = "1.20.0")]
1652impl From<ChildStderr> for Stdio {
1653    /// Converts a [`ChildStderr`] into a [`Stdio`].
1654    ///
1655    /// # Examples
1656    ///
1657    /// ```rust,no_run
1658    /// use std::process::{Command, Stdio};
1659    ///
1660    /// let reverse = Command::new("rev")
1661    ///     .arg("non_existing_file.txt")
1662    ///     .stderr(Stdio::piped())
1663    ///     .spawn()
1664    ///     .expect("failed reverse command");
1665    ///
1666    /// let cat = Command::new("cat")
1667    ///     .arg("-")
1668    ///     .stdin(reverse.stderr.unwrap()) // Converted into a Stdio here
1669    ///     .output()
1670    ///     .expect("failed echo command");
1671    ///
1672    /// assert_eq!(
1673    ///     String::from_utf8_lossy(&cat.stdout),
1674    ///     "rev: cannot open non_existing_file.txt: No such file or directory\n"
1675    /// );
1676    /// ```
1677    fn from(child: ChildStderr) -> Stdio {
1678        Stdio::from_inner(child.into_inner().into())
1679    }
1680}
1681
1682#[stable(feature = "stdio_from", since = "1.20.0")]
1683impl From<fs::File> for Stdio {
1684    /// Converts a [`File`](fs::File) into a [`Stdio`].
1685    ///
1686    /// # Examples
1687    ///
1688    /// `File` will be converted to `Stdio` using `Stdio::from` under the hood.
1689    ///
1690    /// ```rust,no_run
1691    /// use std::fs::File;
1692    /// use std::process::Command;
1693    ///
1694    /// // With the `foo.txt` file containing "Hello, world!"
1695    /// let file = File::open("foo.txt")?;
1696    ///
1697    /// let reverse = Command::new("rev")
1698    ///     .stdin(file)  // Implicit File conversion into a Stdio
1699    ///     .output()?;
1700    ///
1701    /// assert_eq!(reverse.stdout, b"!dlrow ,olleH");
1702    /// # std::io::Result::Ok(())
1703    /// ```
1704    fn from(file: fs::File) -> Stdio {
1705        Stdio::from_inner(file.into_inner().into())
1706    }
1707}
1708
1709#[stable(feature = "stdio_from_stdio", since = "1.74.0")]
1710impl From<io::Stdout> for Stdio {
1711    /// Redirect command stdout/stderr to our stdout
1712    ///
1713    /// # Examples
1714    ///
1715    /// ```rust
1716    /// #![feature(exit_status_error)]
1717    /// use std::io;
1718    /// use std::process::Command;
1719    ///
1720    /// # fn test() -> Result<(), Box<dyn std::error::Error>> {
1721    /// let output = Command::new("whoami")
1722    // "whoami" is a command which exists on both Unix and Windows,
1723    // and which succeeds, producing some stdout output but no stderr.
1724    ///     .stdout(io::stdout())
1725    ///     .output()?;
1726    /// output.status.exit_ok()?;
1727    /// assert!(output.stdout.is_empty());
1728    /// # Ok(())
1729    /// # }
1730    /// #
1731    /// # if cfg!(all(unix, not(target_os = "android"), not(all(target_vendor = "apple", not(target_os = "macos"))))) {
1732    /// #     test().unwrap();
1733    /// # }
1734    /// ```
1735    fn from(inherit: io::Stdout) -> Stdio {
1736        Stdio::from_inner(inherit.into())
1737    }
1738}
1739
1740#[stable(feature = "stdio_from_stdio", since = "1.74.0")]
1741impl From<io::Stderr> for Stdio {
1742    /// Redirect command stdout/stderr to our stderr
1743    ///
1744    /// # Examples
1745    ///
1746    /// ```rust
1747    /// #![feature(exit_status_error)]
1748    /// use std::io;
1749    /// use std::process::Command;
1750    ///
1751    /// # fn test() -> Result<(), Box<dyn std::error::Error>> {
1752    /// let output = Command::new("whoami")
1753    ///     .stdout(io::stderr())
1754    ///     .output()?;
1755    /// output.status.exit_ok()?;
1756    /// assert!(output.stdout.is_empty());
1757    /// # Ok(())
1758    /// # }
1759    /// #
1760    /// # if cfg!(all(unix, not(target_os = "android"), not(all(target_vendor = "apple", not(target_os = "macos"))))) {
1761    /// #     test().unwrap();
1762    /// # }
1763    /// ```
1764    fn from(inherit: io::Stderr) -> Stdio {
1765        Stdio::from_inner(inherit.into())
1766    }
1767}
1768
1769#[stable(feature = "anonymous_pipe", since = "1.87.0")]
1770impl From<io::PipeWriter> for Stdio {
1771    fn from(pipe: io::PipeWriter) -> Self {
1772        Stdio::from_inner(pipe.into_inner().into())
1773    }
1774}
1775
1776#[stable(feature = "anonymous_pipe", since = "1.87.0")]
1777impl From<io::PipeReader> for Stdio {
1778    fn from(pipe: io::PipeReader) -> Self {
1779        Stdio::from_inner(pipe.into_inner().into())
1780    }
1781}
1782
1783/// Describes the result of a process after it has terminated.
1784///
1785/// This `struct` is used to represent the exit status or other termination of a child process.
1786/// Child processes are created via the [`Command`] struct and their exit
1787/// status is exposed through the [`status`] method, or the [`wait`] method
1788/// of a [`Child`] process.
1789///
1790/// An `ExitStatus` represents every possible disposition of a process.  On Unix this
1791/// is the **wait status**.  It is *not* simply an *exit status* (a value passed to `exit`).
1792///
1793/// For proper error reporting of failed processes, print the value of `ExitStatus` or
1794/// `ExitStatusError` using their implementations of [`Display`](crate::fmt::Display).
1795///
1796/// # Differences from `ExitCode`
1797///
1798/// [`ExitCode`] is intended for terminating the currently running process, via
1799/// the `Termination` trait, in contrast to `ExitStatus`, which represents the
1800/// termination of a child process. These APIs are separate due to platform
1801/// compatibility differences and their expected usage; it is not generally
1802/// possible to exactly reproduce an `ExitStatus` from a child for the current
1803/// process after the fact.
1804///
1805/// [`status`]: Command::status
1806/// [`wait`]: Child::wait
1807//
1808// We speak slightly loosely (here and in various other places in the stdlib docs) about `exit`
1809// vs `_exit`.  Naming of Unix system calls is not standardised across Unices, so terminology is a
1810// matter of convention and tradition.  For clarity we usually speak of `exit`, even when we might
1811// mean an underlying system call such as `_exit`.
1812#[derive(PartialEq, Eq, Clone, Copy, Debug)]
1813#[stable(feature = "process", since = "1.0.0")]
1814pub struct ExitStatus(imp::ExitStatus);
1815
1816/// The default value is one which indicates successful completion.
1817#[stable(feature = "process_exitstatus_default", since = "1.73.0")]
1818impl Default for ExitStatus {
1819    fn default() -> Self {
1820        // Ideally this would be done by ExitCode::default().into() but that is complicated.
1821        ExitStatus::from_inner(imp::ExitStatus::default())
1822    }
1823}
1824
1825/// Allows extension traits within `std`.
1826#[unstable(feature = "sealed", issue = "none")]
1827impl crate::sealed::Sealed for ExitStatus {}
1828
1829impl ExitStatus {
1830    /// Was termination successful?  Returns a `Result`.
1831    ///
1832    /// # Examples
1833    ///
1834    /// ```
1835    /// #![feature(exit_status_error)]
1836    /// # if cfg!(all(unix, not(all(target_vendor = "apple", not(target_os = "macos"))))) {
1837    /// use std::process::Command;
1838    ///
1839    /// let status = Command::new("ls")
1840    ///     .arg("/dev/nonexistent")
1841    ///     .status()
1842    ///     .expect("ls could not be executed");
1843    ///
1844    /// println!("ls: {status}");
1845    /// status.exit_ok().expect_err("/dev/nonexistent could be listed!");
1846    /// # } // cfg!(unix)
1847    /// ```
1848    #[unstable(feature = "exit_status_error", issue = "84908")]
1849    pub fn exit_ok(&self) -> Result<(), ExitStatusError> {
1850        self.0.exit_ok().map_err(ExitStatusError)
1851    }
1852
1853    /// Was termination successful? Signal termination is not considered a
1854    /// success, and success is defined as a zero exit status.
1855    ///
1856    /// # Examples
1857    ///
1858    /// ```rust,no_run
1859    /// use std::process::Command;
1860    ///
1861    /// let status = Command::new("mkdir")
1862    ///     .arg("projects")
1863    ///     .status()
1864    ///     .expect("failed to execute mkdir");
1865    ///
1866    /// if status.success() {
1867    ///     println!("'projects/' directory created");
1868    /// } else {
1869    ///     println!("failed to create 'projects/' directory: {status}");
1870    /// }
1871    /// ```
1872    #[must_use]
1873    #[stable(feature = "process", since = "1.0.0")]
1874    pub fn success(&self) -> bool {
1875        self.0.exit_ok().is_ok()
1876    }
1877
1878    /// Returns the exit code of the process, if any.
1879    ///
1880    /// In Unix terms the return value is the **exit status**: the value passed to `exit`, if the
1881    /// process finished by calling `exit`.  Note that on Unix the exit status is truncated to 8
1882    /// bits, and that values that didn't come from a program's call to `exit` may be invented by the
1883    /// runtime system (often, for example, 255, 254, 127 or 126).
1884    ///
1885    /// On Unix, this will return `None` if the process was terminated by a signal.
1886    /// [`ExitStatusExt`](crate::os::unix::process::ExitStatusExt) is an
1887    /// extension trait for extracting any such signal, and other details, from the `ExitStatus`.
1888    ///
1889    /// # Examples
1890    ///
1891    /// ```no_run
1892    /// use std::process::Command;
1893    ///
1894    /// let status = Command::new("mkdir")
1895    ///     .arg("projects")
1896    ///     .status()
1897    ///     .expect("failed to execute mkdir");
1898    ///
1899    /// match status.code() {
1900    ///     Some(code) => println!("Exited with status code: {code}"),
1901    ///     None => println!("Process terminated by signal")
1902    /// }
1903    /// ```
1904    #[must_use]
1905    #[stable(feature = "process", since = "1.0.0")]
1906    pub fn code(&self) -> Option<i32> {
1907        self.0.code()
1908    }
1909}
1910
1911impl AsInner<imp::ExitStatus> for ExitStatus {
1912    #[inline]
1913    fn as_inner(&self) -> &imp::ExitStatus {
1914        &self.0
1915    }
1916}
1917
1918impl FromInner<imp::ExitStatus> for ExitStatus {
1919    fn from_inner(s: imp::ExitStatus) -> ExitStatus {
1920        ExitStatus(s)
1921    }
1922}
1923
1924#[stable(feature = "process", since = "1.0.0")]
1925impl fmt::Display for ExitStatus {
1926    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
1927        self.0.fmt(f)
1928    }
1929}
1930
1931/// Allows extension traits within `std`.
1932#[unstable(feature = "sealed", issue = "none")]
1933impl crate::sealed::Sealed for ExitStatusError {}
1934
1935/// Describes the result of a process after it has failed
1936///
1937/// Produced by the [`.exit_ok`](ExitStatus::exit_ok) method on [`ExitStatus`].
1938///
1939/// # Examples
1940///
1941/// ```
1942/// #![feature(exit_status_error)]
1943/// # if cfg!(all(unix, not(target_os = "android"), not(all(target_vendor = "apple", not(target_os = "macos"))))) {
1944/// use std::process::{Command, ExitStatusError};
1945///
1946/// fn run(cmd: &str) -> Result<(), ExitStatusError> {
1947///     Command::new(cmd).status().unwrap().exit_ok()?;
1948///     Ok(())
1949/// }
1950///
1951/// run("true").unwrap();
1952/// run("false").unwrap_err();
1953/// # } // cfg!(unix)
1954/// ```
1955#[derive(PartialEq, Eq, Clone, Copy, Debug)]
1956#[unstable(feature = "exit_status_error", issue = "84908")]
1957// The definition of imp::ExitStatusError should ideally be such that
1958// Result<(), imp::ExitStatusError> has an identical representation to imp::ExitStatus.
1959pub struct ExitStatusError(imp::ExitStatusError);
1960
1961#[unstable(feature = "exit_status_error", issue = "84908")]
1962impl ExitStatusError {
1963    /// Reports the exit code, if applicable, from an `ExitStatusError`.
1964    ///
1965    /// In Unix terms the return value is the **exit status**: the value passed to `exit`, if the
1966    /// process finished by calling `exit`.  Note that on Unix the exit status is truncated to 8
1967    /// bits, and that values that didn't come from a program's call to `exit` may be invented by the
1968    /// runtime system (often, for example, 255, 254, 127 or 126).
1969    ///
1970    /// On Unix, this will return `None` if the process was terminated by a signal.  If you want to
1971    /// handle such situations specially, consider using methods from
1972    /// [`ExitStatusExt`](crate::os::unix::process::ExitStatusExt).
1973    ///
1974    /// If the process finished by calling `exit` with a nonzero value, this will return
1975    /// that exit status.
1976    ///
1977    /// If the error was something else, it will return `None`.
1978    ///
1979    /// If the process exited successfully (ie, by calling `exit(0)`), there is no
1980    /// `ExitStatusError`.  So the return value from `ExitStatusError::code()` is always nonzero.
1981    ///
1982    /// # Examples
1983    ///
1984    /// ```
1985    /// #![feature(exit_status_error)]
1986    /// # #[cfg(all(unix, not(target_os = "android"), not(all(target_vendor = "apple", not(target_os = "macos")))))] {
1987    /// use std::process::Command;
1988    ///
1989    /// let bad = Command::new("false").status().unwrap().exit_ok().unwrap_err();
1990    /// assert_eq!(bad.code(), Some(1));
1991    /// # } // #[cfg(unix)]
1992    /// ```
1993    #[must_use]
1994    pub fn code(&self) -> Option<i32> {
1995        self.code_nonzero().map(Into::into)
1996    }
1997
1998    /// Reports the exit code, if applicable, from an `ExitStatusError`, as a [`NonZero`].
1999    ///
2000    /// This is exactly like [`code()`](Self::code), except that it returns a <code>[NonZero]<[i32]></code>.
2001    ///
2002    /// Plain `code`, returning a plain integer, is provided because it is often more convenient.
2003    /// The returned value from `code()` is indeed also nonzero; use `code_nonzero()` when you want
2004    /// a type-level guarantee of nonzeroness.
2005    ///
2006    /// # Examples
2007    ///
2008    /// ```
2009    /// #![feature(exit_status_error)]
2010    ///
2011    /// # if cfg!(all(unix, not(target_os = "android"), not(all(target_vendor = "apple", not(target_os = "macos"))))) {
2012    /// use std::num::NonZero;
2013    /// use std::process::Command;
2014    ///
2015    /// let bad = Command::new("false").status().unwrap().exit_ok().unwrap_err();
2016    /// assert_eq!(bad.code_nonzero().unwrap(), NonZero::new(1).unwrap());
2017    /// # } // cfg!(unix)
2018    /// ```
2019    #[must_use]
2020    pub fn code_nonzero(&self) -> Option<NonZero<i32>> {
2021        self.0.code()
2022    }
2023
2024    /// Converts an `ExitStatusError` (back) to an `ExitStatus`.
2025    #[must_use]
2026    pub fn into_status(&self) -> ExitStatus {
2027        ExitStatus(self.0.into())
2028    }
2029}
2030
2031#[unstable(feature = "exit_status_error", issue = "84908")]
2032impl From<ExitStatusError> for ExitStatus {
2033    fn from(error: ExitStatusError) -> Self {
2034        Self(error.0.into())
2035    }
2036}
2037
2038#[unstable(feature = "exit_status_error", issue = "84908")]
2039impl fmt::Display for ExitStatusError {
2040    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
2041        write!(f, "process exited unsuccessfully: {}", self.into_status())
2042    }
2043}
2044
2045#[unstable(feature = "exit_status_error", issue = "84908")]
2046impl crate::error::Error for ExitStatusError {}
2047
2048/// This type represents the status code the current process can return
2049/// to its parent under normal termination.
2050///
2051/// `ExitCode` is intended to be consumed only by the standard library (via
2052/// [`Termination::report()`]). For forwards compatibility with potentially
2053/// unusual targets, this type currently does not provide `Eq`, `Hash`, or
2054/// access to the raw value. This type does provide `PartialEq` for
2055/// comparison, but note that there may potentially be multiple failure
2056/// codes, some of which will _not_ compare equal to `ExitCode::FAILURE`.
2057/// The standard library provides the canonical `SUCCESS` and `FAILURE`
2058/// exit codes as well as `From<u8> for ExitCode` for constructing other
2059/// arbitrary exit codes.
2060///
2061/// # Portability
2062///
2063/// Numeric values used in this type don't have portable meanings, and
2064/// different platforms may mask different amounts of them.
2065///
2066/// For the platform's canonical successful and unsuccessful codes, see
2067/// the [`SUCCESS`] and [`FAILURE`] associated items.
2068///
2069/// [`SUCCESS`]: ExitCode::SUCCESS
2070/// [`FAILURE`]: ExitCode::FAILURE
2071///
2072/// # Differences from `ExitStatus`
2073///
2074/// `ExitCode` is intended for terminating the currently running process, via
2075/// the `Termination` trait, in contrast to [`ExitStatus`], which represents the
2076/// termination of a child process. These APIs are separate due to platform
2077/// compatibility differences and their expected usage; it is not generally
2078/// possible to exactly reproduce an `ExitStatus` from a child for the current
2079/// process after the fact.
2080///
2081/// # Examples
2082///
2083/// `ExitCode` can be returned from the `main` function of a crate, as it implements
2084/// [`Termination`]:
2085///
2086/// ```
2087/// use std::process::ExitCode;
2088/// # fn check_foo() -> bool { true }
2089///
2090/// fn main() -> ExitCode {
2091///     if !check_foo() {
2092///         return ExitCode::from(42);
2093///     }
2094///
2095///     ExitCode::SUCCESS
2096/// }
2097/// ```
2098#[derive(Clone, Copy, Debug, PartialEq)]
2099#[stable(feature = "process_exitcode", since = "1.61.0")]
2100pub struct ExitCode(imp::ExitCode);
2101
2102/// Allows extension traits within `std`.
2103#[unstable(feature = "sealed", issue = "none")]
2104impl crate::sealed::Sealed for ExitCode {}
2105
2106#[stable(feature = "process_exitcode", since = "1.61.0")]
2107impl ExitCode {
2108    /// The canonical `ExitCode` for successful termination on this platform.
2109    ///
2110    /// Note that a `()`-returning `main` implicitly results in a successful
2111    /// termination, so there's no need to return this from `main` unless
2112    /// you're also returning other possible codes.
2113    #[stable(feature = "process_exitcode", since = "1.61.0")]
2114    pub const SUCCESS: ExitCode = ExitCode(imp::ExitCode::SUCCESS);
2115
2116    /// The canonical `ExitCode` for unsuccessful termination on this platform.
2117    ///
2118    /// If you're only returning this and `SUCCESS` from `main`, consider
2119    /// instead returning `Err(_)` and `Ok(())` respectively, which will
2120    /// return the same codes (but will also `eprintln!` the error).
2121    #[stable(feature = "process_exitcode", since = "1.61.0")]
2122    pub const FAILURE: ExitCode = ExitCode(imp::ExitCode::FAILURE);
2123
2124    /// Exit the current process with the given `ExitCode`.
2125    ///
2126    /// Note that this has the same caveats as [`process::exit()`][exit], namely that this function
2127    /// terminates the process immediately, so no destructors on the current stack or any other
2128    /// thread's stack will be run. Also see those docs for some important notes on interop with C
2129    /// code. If a clean shutdown is needed, it is recommended to simply return this ExitCode from
2130    /// the `main` function, as demonstrated in the [type documentation](#examples).
2131    ///
2132    /// # Differences from `process::exit()`
2133    ///
2134    /// `process::exit()` accepts any `i32` value as the exit code for the process; however, there
2135    /// are platforms that only use a subset of that value (see [`process::exit` platform-specific
2136    /// behavior][exit#platform-specific-behavior]). `ExitCode` exists because of this; only
2137    /// `ExitCode`s that are supported by a majority of our platforms can be created, so those
2138    /// problems don't exist (as much) with this method.
2139    ///
2140    /// # Examples
2141    ///
2142    /// ```
2143    /// #![feature(exitcode_exit_method)]
2144    /// # use std::process::ExitCode;
2145    /// # use std::fmt;
2146    /// # enum UhOhError { GenericProblem, Specific, WithCode { exit_code: ExitCode, _x: () } }
2147    /// # impl fmt::Display for UhOhError {
2148    /// #     fn fmt(&self, _: &mut fmt::Formatter<'_>) -> fmt::Result { unimplemented!() }
2149    /// # }
2150    /// // there's no way to gracefully recover from an UhOhError, so we just
2151    /// // print a message and exit
2152    /// fn handle_unrecoverable_error(err: UhOhError) -> ! {
2153    ///     eprintln!("UH OH! {err}");
2154    ///     let code = match err {
2155    ///         UhOhError::GenericProblem => ExitCode::FAILURE,
2156    ///         UhOhError::Specific => ExitCode::from(3),
2157    ///         UhOhError::WithCode { exit_code, .. } => exit_code,
2158    ///     };
2159    ///     code.exit_process()
2160    /// }
2161    /// ```
2162    #[unstable(feature = "exitcode_exit_method", issue = "97100")]
2163    pub fn exit_process(self) -> ! {
2164        exit(self.to_i32())
2165    }
2166}
2167
2168impl ExitCode {
2169    // This is private/perma-unstable because ExitCode is opaque; we don't know that i32 will serve
2170    // all usecases, for example windows seems to use u32, unix uses the 8-15th bits of an i32, we
2171    // likely want to isolate users anything that could restrict the platform specific
2172    // representation of an ExitCode
2173    //
2174    // More info: https://internals.rust-lang.org/t/mini-pre-rfc-redesigning-process-exitstatus/5426
2175    /// Converts an `ExitCode` into an i32
2176    #[unstable(
2177        feature = "process_exitcode_internals",
2178        reason = "exposed only for libstd",
2179        issue = "none"
2180    )]
2181    #[inline]
2182    #[doc(hidden)]
2183    pub fn to_i32(self) -> i32 {
2184        self.0.as_i32()
2185    }
2186}
2187
2188/// The default value is [`ExitCode::SUCCESS`]
2189#[stable(feature = "process_exitcode_default", since = "1.75.0")]
2190impl Default for ExitCode {
2191    fn default() -> Self {
2192        ExitCode::SUCCESS
2193    }
2194}
2195
2196#[stable(feature = "process_exitcode", since = "1.61.0")]
2197impl From<u8> for ExitCode {
2198    /// Constructs an `ExitCode` from an arbitrary u8 value.
2199    fn from(code: u8) -> Self {
2200        ExitCode(imp::ExitCode::from(code))
2201    }
2202}
2203
2204impl AsInner<imp::ExitCode> for ExitCode {
2205    #[inline]
2206    fn as_inner(&self) -> &imp::ExitCode {
2207        &self.0
2208    }
2209}
2210
2211impl FromInner<imp::ExitCode> for ExitCode {
2212    fn from_inner(s: imp::ExitCode) -> ExitCode {
2213        ExitCode(s)
2214    }
2215}
2216
2217impl Child {
2218    /// Forces the child process to exit. If the child has already exited, `Ok(())`
2219    /// is returned.
2220    ///
2221    /// The mapping to [`ErrorKind`]s is not part of the compatibility contract of the function.
2222    ///
2223    /// This is equivalent to sending a SIGKILL on Unix platforms.
2224    ///
2225    /// # Examples
2226    ///
2227    /// ```no_run
2228    /// use std::process::Command;
2229    ///
2230    /// let mut command = Command::new("yes");
2231    /// if let Ok(mut child) = command.spawn() {
2232    ///     child.kill().expect("command couldn't be killed");
2233    /// } else {
2234    ///     println!("yes command didn't start");
2235    /// }
2236    /// ```
2237    ///
2238    /// [`ErrorKind`]: io::ErrorKind
2239    /// [`InvalidInput`]: io::ErrorKind::InvalidInput
2240    #[stable(feature = "process", since = "1.0.0")]
2241    #[cfg_attr(not(test), rustc_diagnostic_item = "child_kill")]
2242    pub fn kill(&mut self) -> io::Result<()> {
2243        self.handle.kill()
2244    }
2245
2246    /// Returns the OS-assigned process identifier associated with this child.
2247    ///
2248    /// # Examples
2249    ///
2250    /// ```no_run
2251    /// use std::process::Command;
2252    ///
2253    /// let mut command = Command::new("ls");
2254    /// if let Ok(child) = command.spawn() {
2255    ///     println!("Child's ID is {}", child.id());
2256    /// } else {
2257    ///     println!("ls command didn't start");
2258    /// }
2259    /// ```
2260    #[must_use]
2261    #[stable(feature = "process_id", since = "1.3.0")]
2262    #[cfg_attr(not(test), rustc_diagnostic_item = "child_id")]
2263    pub fn id(&self) -> u32 {
2264        self.handle.id()
2265    }
2266
2267    /// Waits for the child to exit completely, returning the status that it
2268    /// exited with. This function will continue to have the same return value
2269    /// after it has been called at least once.
2270    ///
2271    /// The stdin handle to the child process, if any, will be closed
2272    /// before waiting. This helps avoid deadlock: it ensures that the
2273    /// child does not block waiting for input from the parent, while
2274    /// the parent waits for the child to exit.
2275    ///
2276    /// # Examples
2277    ///
2278    /// ```no_run
2279    /// use std::process::Command;
2280    ///
2281    /// let mut command = Command::new("ls");
2282    /// if let Ok(mut child) = command.spawn() {
2283    ///     child.wait().expect("command wasn't running");
2284    ///     println!("Child has finished its execution!");
2285    /// } else {
2286    ///     println!("ls command didn't start");
2287    /// }
2288    /// ```
2289    #[stable(feature = "process", since = "1.0.0")]
2290    pub fn wait(&mut self) -> io::Result<ExitStatus> {
2291        drop(self.stdin.take());
2292        self.handle.wait().map(ExitStatus)
2293    }
2294
2295    /// Attempts to collect the exit status of the child if it has already
2296    /// exited.
2297    ///
2298    /// This function will not block the calling thread and will only
2299    /// check to see if the child process has exited or not. If the child has
2300    /// exited then on Unix the process ID is reaped. This function is
2301    /// guaranteed to repeatedly return a successful exit status so long as the
2302    /// child has already exited.
2303    ///
2304    /// If the child has exited, then `Ok(Some(status))` is returned. If the
2305    /// exit status is not available at this time then `Ok(None)` is returned.
2306    /// If an error occurs, then that error is returned.
2307    ///
2308    /// Note that unlike `wait`, this function will not attempt to drop stdin.
2309    ///
2310    /// # Examples
2311    ///
2312    /// ```no_run
2313    /// use std::process::Command;
2314    ///
2315    /// let mut child = Command::new("ls").spawn()?;
2316    ///
2317    /// match child.try_wait() {
2318    ///     Ok(Some(status)) => println!("exited with: {status}"),
2319    ///     Ok(None) => {
2320    ///         println!("status not ready yet, let's really wait");
2321    ///         let res = child.wait();
2322    ///         println!("result: {res:?}");
2323    ///     }
2324    ///     Err(e) => println!("error attempting to wait: {e}"),
2325    /// }
2326    /// # std::io::Result::Ok(())
2327    /// ```
2328    #[stable(feature = "process_try_wait", since = "1.18.0")]
2329    pub fn try_wait(&mut self) -> io::Result<Option<ExitStatus>> {
2330        Ok(self.handle.try_wait()?.map(ExitStatus))
2331    }
2332
2333    /// Simultaneously waits for the child to exit and collect all remaining
2334    /// output on the stdout/stderr handles, returning an `Output`
2335    /// instance.
2336    ///
2337    /// The stdin handle to the child process, if any, will be closed
2338    /// before waiting. This helps avoid deadlock: it ensures that the
2339    /// child does not block waiting for input from the parent, while
2340    /// the parent waits for the child to exit.
2341    ///
2342    /// By default, stdin, stdout and stderr are inherited from the parent.
2343    /// In order to capture the output into this `Result<Output>` it is
2344    /// necessary to create new pipes between parent and child. Use
2345    /// `stdout(Stdio::piped())` or `stderr(Stdio::piped())`, respectively.
2346    ///
2347    /// # Examples
2348    ///
2349    /// ```should_panic
2350    /// use std::process::{Command, Stdio};
2351    ///
2352    /// let child = Command::new("/bin/cat")
2353    ///     .arg("file.txt")
2354    ///     .stdout(Stdio::piped())
2355    ///     .spawn()
2356    ///     .expect("failed to execute child");
2357    ///
2358    /// let output = child
2359    ///     .wait_with_output()
2360    ///     .expect("failed to wait on child");
2361    ///
2362    /// assert!(output.status.success());
2363    /// ```
2364    ///
2365    #[stable(feature = "process", since = "1.0.0")]
2366    pub fn wait_with_output(mut self) -> io::Result<Output> {
2367        drop(self.stdin.take());
2368
2369        let (mut stdout, mut stderr) = (Vec::new(), Vec::new());
2370        match (self.stdout.take(), self.stderr.take()) {
2371            (None, None) => {}
2372            (Some(mut out), None) => {
2373                let res = out.read_to_end(&mut stdout);
2374                res.unwrap();
2375            }
2376            (None, Some(mut err)) => {
2377                let res = err.read_to_end(&mut stderr);
2378                res.unwrap();
2379            }
2380            (Some(out), Some(err)) => {
2381                let res = imp::read_output(out.inner, &mut stdout, err.inner, &mut stderr);
2382                res.unwrap();
2383            }
2384        }
2385
2386        let status = self.wait()?;
2387        Ok(Output { status, stdout, stderr })
2388    }
2389}
2390
2391/// Terminates the current process with the specified exit code.
2392///
2393/// This function will never return and will immediately terminate the current
2394/// process. The exit code is passed through to the underlying OS and will be
2395/// available for consumption by another process.
2396///
2397/// Note that because this function never returns, and that it terminates the
2398/// process, no destructors on the current stack or any other thread's stack
2399/// will be run. If a clean shutdown is needed it is recommended to only call
2400/// this function at a known point where there are no more destructors left
2401/// to run; or, preferably, simply return a type implementing [`Termination`]
2402/// (such as [`ExitCode`] or `Result`) from the `main` function and avoid this
2403/// function altogether:
2404///
2405/// ```
2406/// # use std::io::Error as MyError;
2407/// fn main() -> Result<(), MyError> {
2408///     // ...
2409///     Ok(())
2410/// }
2411/// ```
2412///
2413/// In its current implementation, this function will execute exit handlers registered with `atexit`
2414/// as well as other platform-specific exit handlers (e.g. `fini` sections of ELF shared objects).
2415/// This means that Rust requires that all exit handlers are safe to execute at any time. In
2416/// particular, if an exit handler cleans up some state that might be concurrently accessed by other
2417/// threads, it is required that the exit handler performs suitable synchronization with those
2418/// threads. (The alternative to this requirement would be to not run exit handlers at all, which is
2419/// considered undesirable. Note that returning from `main` also calls `exit`, so making `exit` an
2420/// unsafe operation is not an option.)
2421///
2422/// ## Platform-specific behavior
2423///
2424/// **Unix**: On Unix-like platforms, it is unlikely that all 32 bits of `exit`
2425/// will be visible to a parent process inspecting the exit code. On most
2426/// Unix-like platforms, only the eight least-significant bits are considered.
2427///
2428/// For example, the exit code for this example will be `0` on Linux, but `256`
2429/// on Windows:
2430///
2431/// ```no_run
2432/// use std::process;
2433///
2434/// process::exit(0x0100);
2435/// ```
2436///
2437/// ### Safe interop with C code
2438///
2439/// On Unix, this function is currently implemented using the `exit` C function [`exit`][C-exit]. As
2440/// of C23, the C standard does not permit multiple threads to call `exit` concurrently. Rust
2441/// mitigates this with a lock, but if C code calls `exit`, that can still cause undefined behavior.
2442/// Note that returning from `main` is equivalent to calling `exit`.
2443///
2444/// Therefore, it is undefined behavior to have two concurrent threads perform the following
2445/// without synchronization:
2446/// - One thread calls Rust's `exit` function or returns from Rust's `main` function
2447/// - Another thread calls the C function `exit` or `quick_exit`, or returns from C's `main` function
2448///
2449/// Note that if a binary contains multiple copies of the Rust runtime (e.g., when combining
2450/// multiple `cdylib` or `staticlib`), they each have their own separate lock, so from the
2451/// perspective of code running in one of the Rust runtimes, the "outside" Rust code is basically C
2452/// code, and concurrent `exit` again causes undefined behavior.
2453///
2454/// Individual C implementations might provide more guarantees than the standard and permit concurrent
2455/// calls to `exit`; consult the documentation of your C implementation for details.
2456///
2457/// For some of the on-going discussion to make `exit` thread-safe in C, see:
2458/// - [Rust issue #126600](https://github.com/rust-lang/rust/issues/126600)
2459/// - [Austin Group Bugzilla (for POSIX)](https://austingroupbugs.net/view.php?id=1845)
2460/// - [GNU C library Bugzilla](https://sourceware.org/bugzilla/show_bug.cgi?id=31997)
2461///
2462/// [C-exit]: https://en.cppreference.com/w/c/program/exit
2463#[stable(feature = "rust1", since = "1.0.0")]
2464#[cfg_attr(not(test), rustc_diagnostic_item = "process_exit")]
2465pub fn exit(code: i32) -> ! {
2466    crate::rt::cleanup();
2467    crate::sys::exit::exit(code)
2468}
2469
2470/// Terminates the process in an abnormal fashion.
2471///
2472/// The function will never return and will immediately terminate the current
2473/// process in a platform specific "abnormal" manner. As a consequence,
2474/// no destructors on the current stack or any other thread's stack
2475/// will be run, Rust IO buffers (eg, from `BufWriter`) will not be flushed,
2476/// and C stdio buffers will (on most platforms) not be flushed.
2477///
2478/// This is in contrast to the default behavior of [`panic!`] which unwinds
2479/// the current thread's stack and calls all destructors.
2480/// When `panic="abort"` is set, either as an argument to `rustc` or in a
2481/// crate's Cargo.toml, [`panic!`] and `abort` are similar. However,
2482/// [`panic!`] will still call the [panic hook] while `abort` will not.
2483///
2484/// If a clean shutdown is needed it is recommended to only call
2485/// this function at a known point where there are no more destructors left
2486/// to run.
2487///
2488/// The process's termination will be similar to that from the C `abort()`
2489/// function.  On Unix, the process will terminate with signal `SIGABRT`, which
2490/// typically means that the shell prints "Aborted".
2491///
2492/// # Examples
2493///
2494/// ```no_run
2495/// use std::process;
2496///
2497/// fn main() {
2498///     println!("aborting");
2499///
2500///     process::abort();
2501///
2502///     // execution never gets here
2503/// }
2504/// ```
2505///
2506/// The `abort` function terminates the process, so the destructor will not
2507/// get run on the example below:
2508///
2509/// ```no_run
2510/// use std::process;
2511///
2512/// struct HasDrop;
2513///
2514/// impl Drop for HasDrop {
2515///     fn drop(&mut self) {
2516///         println!("This will never be printed!");
2517///     }
2518/// }
2519///
2520/// fn main() {
2521///     let _x = HasDrop;
2522///     process::abort();
2523///     // the destructor implemented for HasDrop will never get run
2524/// }
2525/// ```
2526///
2527/// [panic hook]: crate::panic::set_hook
2528#[stable(feature = "process_abort", since = "1.17.0")]
2529#[cold]
2530#[cfg_attr(not(test), rustc_diagnostic_item = "process_abort")]
2531#[cfg_attr(miri, track_caller)] // even without panics, this helps for Miri backtraces
2532pub fn abort() -> ! {
2533    crate::sys::abort_internal();
2534}
2535
2536/// Returns the OS-assigned process identifier associated with this process.
2537///
2538/// # Examples
2539///
2540/// ```no_run
2541/// use std::process;
2542///
2543/// println!("My pid is {}", process::id());
2544/// ```
2545#[must_use]
2546#[stable(feature = "getpid", since = "1.26.0")]
2547pub fn id() -> u32 {
2548    crate::sys::os::getpid()
2549}
2550
2551/// A trait for implementing arbitrary return types in the `main` function.
2552///
2553/// The C-main function only supports returning integers.
2554/// So, every type implementing the `Termination` trait has to be converted
2555/// to an integer.
2556///
2557/// The default implementations are returning `libc::EXIT_SUCCESS` to indicate
2558/// a successful execution. In case of a failure, `libc::EXIT_FAILURE` is returned.
2559///
2560/// Because different runtimes have different specifications on the return value
2561/// of the `main` function, this trait is likely to be available only on
2562/// standard library's runtime for convenience. Other runtimes are not required
2563/// to provide similar functionality.
2564#[cfg_attr(not(any(test, doctest)), lang = "termination")]
2565#[stable(feature = "termination_trait_lib", since = "1.61.0")]
2566#[rustc_on_unimplemented(on(
2567    cause = "MainFunctionType",
2568    message = "`main` has invalid return type `{Self}`",
2569    label = "`main` can only return types that implement `{This}`"
2570))]
2571pub trait Termination {
2572    /// Is called to get the representation of the value as status code.
2573    /// This status code is returned to the operating system.
2574    #[stable(feature = "termination_trait_lib", since = "1.61.0")]
2575    fn report(self) -> ExitCode;
2576}
2577
2578#[stable(feature = "termination_trait_lib", since = "1.61.0")]
2579impl Termination for () {
2580    #[inline]
2581    fn report(self) -> ExitCode {
2582        ExitCode::SUCCESS
2583    }
2584}
2585
2586#[stable(feature = "termination_trait_lib", since = "1.61.0")]
2587impl Termination for ! {
2588    fn report(self) -> ExitCode {
2589        self
2590    }
2591}
2592
2593#[stable(feature = "termination_trait_lib", since = "1.61.0")]
2594impl Termination for Infallible {
2595    fn report(self) -> ExitCode {
2596        match self {}
2597    }
2598}
2599
2600#[stable(feature = "termination_trait_lib", since = "1.61.0")]
2601impl Termination for ExitCode {
2602    #[inline]
2603    fn report(self) -> ExitCode {
2604        self
2605    }
2606}
2607
2608#[stable(feature = "termination_trait_lib", since = "1.61.0")]
2609impl<T: Termination, E: fmt::Debug> Termination for Result<T, E> {
2610    fn report(self) -> ExitCode {
2611        match self {
2612            Ok(val) => val.report(),
2613            Err(err) => {
2614                io::attempt_print_to_stderr(format_args_nl!("Error: {err:?}"));
2615                ExitCode::FAILURE
2616            }
2617        }
2618    }
2619}
````