---
title: mod.rs - source
url: https://doc.rust-lang.org/stable/src/std/os/unix/io/mod.rs.html#201
source: crawler
fetched_at: 2026-05-06T21:31:28.80813524-03:00
rendered_js: false
word_count: 1420
summary: This module provides Unix-specific extensions for managing I/O safety through RawFd, BorrowedFd, and OwnedFd types, mirroring Rust's pointer safety concepts.
tags:
    - unix
    - io-safety
    - file-descriptor
    - rust-std
    - memory-safety
    - resource-ownership
category: concept
---

## std/os/unix/io/ mod.rs

````rust
1//! Unix-specific extensions to general I/O primitives.
2//!
3//! Just like raw pointers, raw file descriptors point to resources with
4//! dynamic lifetimes, and they can dangle if they outlive their resources
5//! or be forged if they're created from invalid values.
6//!
7//! This module provides three types for representing file descriptors,
8//! with different ownership properties: raw, borrowed, and owned, which are
9//! analogous to types used for representing pointers. These types reflect concepts of [I/O
10//! safety][io-safety] on Unix.
11//!
12//! | Type               | Analogous to |
13//! | ------------------ | ------------ |
14//! | [`RawFd`]          | `*const _`   |
15//! | [`BorrowedFd<'a>`] | `&'a Arc<_>` |
16//! | [`OwnedFd`]        | `Arc<_>`     |
17//!
18//! Like raw pointers, `RawFd` values are primitive values. And in new code,
19//! they should be considered unsafe to do I/O on (analogous to dereferencing
20//! them). Rust did not always provide this guidance, so existing code in the
21//! Rust ecosystem often doesn't mark `RawFd` usage as unsafe.
22//! Libraries are encouraged to migrate,
23//! either by adding `unsafe` to APIs that dereference `RawFd` values, or by
24//! using to `BorrowedFd` or `OwnedFd` instead.
25//!
26//! The use of `Arc` for borrowed/owned file descriptors may be surprising. Unix file descriptors
27//! are mere references to internal kernel objects called "open file descriptions", and the same
28//! open file description can be referenced by multiple file descriptors (e.g. if `dup` is used).
29//! State such as the offset within the file is shared among all file descriptors that refer to the
30//! same open file description, and the kernel internally does reference-counting to only close the
31//! underlying resource once all file descriptors referencing it are closed. That's why `Arc` (and
32//! not `Box`) is the closest Rust analogy to an "owned" file descriptor.
33//!
34//! Like references, `BorrowedFd` values are tied to a lifetime, to ensure
35//! that they don't outlive the resource they point to. These are safe to
36//! use. `BorrowedFd` values may be used in APIs which provide safe access to
37//! any system call except for:
38//!
39//!  - `close`, because that would end the dynamic lifetime of the resource
40//!    without ending the lifetime of the file descriptor. (Equivalently:
41//!    an `&Arc<_>` cannot be `drop`ed.)
42//!
43//!  - `dup2`/`dup3`, in the second argument, because this argument is
44//!    closed and assigned a new resource, which may break the assumptions of
45//!    other code using that file descriptor.
46//!
47//! `BorrowedFd` values may be used in APIs which provide safe access to `dup` system calls, so code
48//! working with `OwnedFd` cannot assume to have exclusive access to the underlying open file
49//! description. (Equivalently: `&Arc` may be used in APIs that provide safe access to `clone`, so
50//! code working with an `Arc` cannot assume that the reference count is 1.)
51//!
52//! `BorrowedFd` values may also be used with `mmap`, since `mmap` uses the
53//! provided file descriptor in a manner similar to `dup` and does not require
54//! the `BorrowedFd` passed to it to live for the lifetime of the resulting
55//! mapping. That said, `mmap` is unsafe for other reasons: it operates on raw
56//! pointers, and it can have undefined behavior if the underlying storage is
57//! mutated. Mutations may come from other processes, or from the same process
58//! if the API provides `BorrowedFd` access, since as mentioned earlier,
59//! `BorrowedFd` values may be used in APIs which provide safe access to any
60//! system call. Consequently, code using `mmap` and presenting a safe API must
61//! take full responsibility for ensuring that safe Rust code cannot evoke
62//! undefined behavior through it.
63//!
64//! Like `Arc`, `OwnedFd` values conceptually own one reference to the resource they point to,
65//! and decrement the reference count when they are dropped (by calling `close`).
66//! When the reference count reaches 0, the underlying open file description will be freed
67//! by the kernel.
68//!
69//! See the [`io` module docs][io-safety] for a general explanation of I/O safety.
70//!
71//! ## `/proc/self/mem` and similar OS features
72//!
73//! Some platforms have special files, such as `/proc/self/mem`, which
74//! provide read and write access to the process's memory. Such reads
75//! and writes happen outside the control of the Rust compiler, so they do not
76//! uphold Rust's memory safety guarantees.
77//!
78//! This does not mean that all APIs that might allow `/proc/self/mem`
79//! to be opened and read from or written must be `unsafe`. Rust's safety guarantees
80//! only cover what the program itself can do, and not what entities outside
81//! the program can do to it. `/proc/self/mem` is considered to be such an
82//! external entity, along with `/proc/self/fd/*`, debugging interfaces, and people with physical
83//! access to the hardware. This is true even in cases where the program is controlling the external
84//! entity.
85//!
86//! If you desire to comprehensively prevent programs from reaching out and
87//! causing external entities to reach back in and violate memory safety, it's
88//! necessary to use *sandboxing*, which is outside the scope of `std`.
89//!
90//! [`BorrowedFd<'a>`]: crate::os::unix::io::BorrowedFd
91//! [io-safety]: crate::io#io-safety
92
93#![stable(feature = "rust1", since = "1.0.0")]
94
95use crate::io::{self, Stderr, StderrLock, Stdin, StdinLock, Stdout, StdoutLock, Write};
96#[stable(feature = "rust1", since = "1.0.0")]
97pub use crate::os::fd::*;
98#[allow(unused_imports)] // not used on all targets
99use crate::sys::cvt;
100
101// Tests for this module
102#[cfg(test)]
103mod tests;
104
105#[unstable(feature = "stdio_swap", issue = "150667")]
106pub trait StdioExt: crate::sealed::Sealed {
107    /// Redirects the stdio file descriptor to point to the file description underpinning `fd`.
108    ///
109    /// Rust std::io write buffers (if any) are flushed, but other runtimes
110    /// (e.g. C stdio) or libraries that acquire a clone of the file descriptor
111    /// will not be aware of this change.
112    ///
113    /// # Platform-specific behavior
114    ///
115    /// This is [currently] implemented using
116    ///
117    /// - `fd_renumber` on wasip1
118    /// - `dup2` on most unixes
119    ///
120    /// [currently]: crate::io#platform-specific-behavior
121    ///
122    /// ```
123    /// #![feature(stdio_swap)]
124    /// use std::io::{self, Read, Write};
125    /// use std::os::unix::io::StdioExt;
126    ///
127    /// fn main() -> io::Result<()> {
128    ///    let (reader, mut writer) = io::pipe()?;
129    ///    let mut stdin = io::stdin();
130    ///    stdin.set_fd(reader)?;
131    ///    writer.write_all(b"Hello, world!")?;
132    ///    let mut buffer = vec![0; 13];
133    ///    assert_eq!(stdin.read(&mut buffer)?, 13);
134    ///    assert_eq!(&buffer, b"Hello, world!");
135    ///    Ok(())
136    /// }
137    /// ```
138    fn set_fd<T: Into<OwnedFd>>(&mut self, fd: T) -> io::Result<()>;
139
140    /// Redirects the stdio file descriptor and returns a new `OwnedFd`
141    /// backed by the previous file description.
142    ///
143    /// See [`set_fd()`] for details.
144    ///
145    /// [`set_fd()`]: StdioExt::set_fd
146    fn replace_fd<T: Into<OwnedFd>>(&mut self, replace_with: T) -> io::Result<OwnedFd>;
147
148    /// Redirects the stdio file descriptor to the null device (`/dev/null`)
149    /// and returns a new `OwnedFd` backed by the previous file description.
150    ///
151    /// Programs that communicate structured data via stdio can use this early in `main()` to
152    /// extract the fds, treat them as other IO types (`File`, `UnixStream`, etc),
153    /// apply custom buffering or avoid interference from stdio use later in the program.
154    ///
155    /// See [`set_fd()`] for additional details.
156    ///
157    /// [`set_fd()`]: StdioExt::set_fd
158    fn take_fd(&mut self) -> io::Result<OwnedFd>;
159}
160
161macro io_ext_impl($stdio_ty:ty, $stdio_lock_ty:ty, $writer:literal) {
162    #[unstable(feature = "stdio_swap", issue = "150667")]
163    impl StdioExt for $stdio_ty {
164        fn set_fd<T: Into<OwnedFd>>(&mut self, fd: T) -> io::Result<()> {
165            self.lock().set_fd(fd)
166        }
167
168        fn take_fd(&mut self) -> io::Result<OwnedFd> {
169            self.lock().take_fd()
170        }
171
172        fn replace_fd<T: Into<OwnedFd>>(&mut self, replace_with: T) -> io::Result<OwnedFd> {
173            self.lock().replace_fd(replace_with)
174        }
175    }
176
177    #[unstable(feature = "stdio_swap", issue = "150667")]
178    impl StdioExt for $stdio_lock_ty {
179        fn set_fd<T: Into<OwnedFd>>(&mut self, fd: T) -> io::Result<()> {
180            #[cfg($writer)]
181            self.flush()?;
182            replace_stdio_fd(self.as_fd(), fd.into())
183        }
184
185        fn take_fd(&mut self) -> io::Result<OwnedFd> {
186            let null = null_fd()?;
187            let cloned = self.as_fd().try_clone_to_owned()?;
188            self.set_fd(null)?;
189            Ok(cloned)
190        }
191
192        fn replace_fd<T: Into<OwnedFd>>(&mut self, replace_with: T) -> io::Result<OwnedFd> {
193            let cloned = self.as_fd().try_clone_to_owned()?;
194            self.set_fd(replace_with)?;
195            Ok(cloned)
196        }
197    }
198}
199
200io_ext_impl!(Stdout, StdoutLock<'_>, true);
201io_ext_impl!(Stdin, StdinLock<'_>, false);
202io_ext_impl!(Stderr, StderrLock<'_>, true);
203
204fn null_fd() -> io::Result<OwnedFd> {
205    let null_dev = crate::fs::OpenOptions::new().read(true).write(true).open("/dev/null")?;
206    Ok(null_dev.into())
207}
208
209/// Replaces the underlying file descriptor with the one from `other`.
210/// Does not set CLOEXEC.
211fn replace_stdio_fd(this: BorrowedFd<'_>, other: OwnedFd) -> io::Result<()> {
212    cfg_select! {
213        all(target_os = "wasi", target_env = "p1") => {
214            cvt(unsafe { libc::__wasilibc_fd_renumber(other.as_raw_fd(), this.as_raw_fd()) }).map(|_| ())
215        }
216        not(any(
217            target_arch = "wasm32",
218            target_os = "hermit",
219            target_os = "trusty",
220            target_os = "motor"
221        )) => {
222            cvt(unsafe {libc::dup2(other.as_raw_fd(), this.as_raw_fd())}).map(|_| ())
223        }
224        _ => {
225            let _ = (this, other);
226            Err(io::Error::UNSUPPORTED_PLATFORM)
227        }
228    }
229}
````