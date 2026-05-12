---
title: raw.rs - source
url: https://doc.rust-lang.org/src/std/os/fd/raw.rs.html#197-202
source: crawler
fetched_at: 2026-05-06T21:24:23.053223068-03:00
rendered_js: false
word_count: 1368
summary: This document defines the raw file descriptor type and standard traits for interoperability between Rust objects and platform-specific file descriptors on Unix-like systems.
tags:
    - rust
    - unix
    - file-descriptors
    - traits
    - io-safety
    - low-level-api
category: api
---

## std/os/fd/ raw.rs

````rust
1//! Raw Unix-like file descriptors.
2
3#![stable(feature = "rust1", since = "1.0.0")]
4
5#[cfg(target_os = "hermit")]
6use hermit_abi as libc;
7#[cfg(target_os = "motor")]
8use moto_rt::libc;
9
10#[cfg(target_os = "motor")]
11use super::owned::OwnedFd;
12#[cfg(not(target_os = "trusty"))]
13use crate::fs;
14use crate::io;
15#[cfg(target_os = "hermit")]
16use crate::os::hermit::io::OwnedFd;
17#[cfg(all(not(target_os = "hermit"), not(target_os = "motor")))]
18use crate::os::raw;
19#[cfg(all(doc, not(target_arch = "wasm32")))]
20use crate::os::unix::io::AsFd;
21#[cfg(unix)]
22use crate::os::unix::io::OwnedFd;
23#[cfg(target_os = "wasi")]
24use crate::os::wasi::io::OwnedFd;
25#[cfg(not(target_os = "trusty"))]
26use crate::sys::{AsInner, FromInner, IntoInner};
27
28/// Raw file descriptors.
29#[stable(feature = "rust1", since = "1.0.0")]
30#[cfg(all(not(target_os = "hermit"), not(target_os = "motor")))]
31pub type RawFd = raw::c_int;
32#[stable(feature = "rust1", since = "1.0.0")]
33#[cfg(any(target_os = "hermit", target_os = "motor"))]
34pub type RawFd = i32;
35
36/// A trait to extract the raw file descriptor from an underlying object.
37///
38/// This is only available on unix and WASI platforms and must be imported in
39/// order to call the method. Windows platforms have a corresponding
40/// `AsRawHandle` and `AsRawSocket` set of traits.
41#[stable(feature = "rust1", since = "1.0.0")]
42pub trait AsRawFd {
43    /// Extracts the raw file descriptor.
44    ///
45    /// This function is typically used to **borrow** an owned file descriptor.
46    /// When used in this way, this method does **not** pass ownership of the
47    /// raw file descriptor to the caller, and the file descriptor is only
48    /// guaranteed to be valid while the original object has not yet been
49    /// destroyed.
50    ///
51    /// However, borrowing is not strictly required. See [`AsFd::as_fd`]
52    /// for an API which strictly borrows a file descriptor.
53    ///
54    /// # Example
55    ///
56    /// ```no_run
57    /// use std::fs::File;
58    /// # use std::io;
59    /// #[cfg(any(unix, target_os = "wasi"))]
60    /// use std::os::fd::{AsRawFd, RawFd};
61    ///
62    /// let mut f = File::open("foo.txt")?;
63    /// // Note that `raw_fd` is only valid as long as `f` exists.
64    /// #[cfg(any(unix, target_os = "wasi"))]
65    /// let raw_fd: RawFd = f.as_raw_fd();
66    /// # Ok::<(), io::Error>(())
67    /// ```
68    #[stable(feature = "rust1", since = "1.0.0")]
69    fn as_raw_fd(&self) -> RawFd;
70}
71
72/// A trait to express the ability to construct an object from a raw file
73/// descriptor.
74#[stable(feature = "from_raw_os", since = "1.1.0")]
75pub trait FromRawFd {
76    /// Constructs a new instance of `Self` from the given raw file
77    /// descriptor.
78    ///
79    /// This function is typically used to **consume ownership** of the
80    /// specified file descriptor. When used in this way, the returned object
81    /// will take responsibility for closing it when the object goes out of
82    /// scope.
83    ///
84    /// However, consuming ownership is not strictly required. Use a
85    /// [`From<OwnedFd>::from`] implementation for an API which strictly
86    /// consumes ownership.
87    ///
88    /// # Safety
89    ///
90    /// The `fd` passed in must be an [owned file descriptor][io-safety];
91    /// in particular, it must be open.
92    ///
93    /// [io-safety]: io#io-safety
94    ///
95    /// # Example
96    ///
97    /// ```no_run
98    /// use std::fs::File;
99    /// # use std::io;
100    /// #[cfg(any(unix, target_os = "wasi"))]
101    /// use std::os::fd::{FromRawFd, IntoRawFd, RawFd};
102    ///
103    /// let f = File::open("foo.txt")?;
104    /// # #[cfg(any(unix, target_os = "wasi"))]
105    /// let raw_fd: RawFd = f.into_raw_fd();
106    /// // SAFETY: no other functions should call `from_raw_fd`, so there
107    /// // is only one owner for the file descriptor.
108    /// # #[cfg(any(unix, target_os = "wasi"))]
109    /// let f = unsafe { File::from_raw_fd(raw_fd) };
110    /// # Ok::<(), io::Error>(())
111    /// ```
112    #[stable(feature = "from_raw_os", since = "1.1.0")]
113    unsafe fn from_raw_fd(fd: RawFd) -> Self;
114}
115
116/// A trait to express the ability to consume an object and acquire ownership of
117/// its raw file descriptor.
118#[stable(feature = "into_raw_os", since = "1.4.0")]
119pub trait IntoRawFd {
120    /// Consumes this object, returning the raw underlying file descriptor.
121    ///
122    /// This function is typically used to **transfer ownership** of the underlying
123    /// file descriptor to the caller. When used in this way, callers are then the unique
124    /// owners of the file descriptor and must close it once it's no longer needed.
125    ///
126    /// However, transferring ownership is not strictly required. Use a
127    /// [`Into<OwnedFd>::into`] implementation for an API which strictly
128    /// transfers ownership.
129    ///
130    /// # Example
131    ///
132    /// ```no_run
133    /// use std::fs::File;
134    /// # use std::io;
135    /// #[cfg(any(unix, target_os = "wasi"))]
136    /// use std::os::fd::{IntoRawFd, RawFd};
137    ///
138    /// let f = File::open("foo.txt")?;
139    /// #[cfg(any(unix, target_os = "wasi"))]
140    /// let raw_fd: RawFd = f.into_raw_fd();
141    /// # Ok::<(), io::Error>(())
142    /// ```
143    #[must_use = "losing the raw file descriptor may leak resources"]
144    #[stable(feature = "into_raw_os", since = "1.4.0")]
145    fn into_raw_fd(self) -> RawFd;
146}
147
148#[stable(feature = "raw_fd_reflexive_traits", since = "1.48.0")]
149impl AsRawFd for RawFd {
150    #[inline]
151    fn as_raw_fd(&self) -> RawFd {
152        *self
153    }
154}
155#[stable(feature = "raw_fd_reflexive_traits", since = "1.48.0")]
156impl IntoRawFd for RawFd {
157    #[inline]
158    fn into_raw_fd(self) -> RawFd {
159        self
160    }
161}
162#[stable(feature = "raw_fd_reflexive_traits", since = "1.48.0")]
163impl FromRawFd for RawFd {
164    #[inline]
165    unsafe fn from_raw_fd(fd: RawFd) -> RawFd {
166        fd
167    }
168}
169
170#[stable(feature = "rust1", since = "1.0.0")]
171#[cfg(not(target_os = "trusty"))]
172impl AsRawFd for fs::File {
173    #[inline]
174    fn as_raw_fd(&self) -> RawFd {
175        self.as_inner().as_raw_fd()
176    }
177}
178#[stable(feature = "from_raw_os", since = "1.1.0")]
179#[cfg(not(target_os = "trusty"))]
180impl FromRawFd for fs::File {
181    #[inline]
182    unsafe fn from_raw_fd(fd: RawFd) -> fs::File {
183        unsafe { fs::File::from(OwnedFd::from_raw_fd(fd)) }
184    }
185}
186#[stable(feature = "into_raw_os", since = "1.4.0")]
187#[cfg(not(target_os = "trusty"))]
188impl IntoRawFd for fs::File {
189    #[inline]
190    fn into_raw_fd(self) -> RawFd {
191        self.into_inner().into_inner().into_raw_fd()
192    }
193}
194
195#[stable(feature = "asraw_stdio", since = "1.21.0")]
196#[cfg(not(target_os = "trusty"))]
197impl AsRawFd for io::Stdin {
198    #[inline]
199    fn as_raw_fd(&self) -> RawFd {
200        libc::STDIN_FILENO
201    }
202}
203
204#[stable(feature = "asraw_stdio", since = "1.21.0")]
205impl AsRawFd for io::Stdout {
206    #[inline]
207    fn as_raw_fd(&self) -> RawFd {
208        libc::STDOUT_FILENO
209    }
210}
211
212#[stable(feature = "asraw_stdio", since = "1.21.0")]
213impl AsRawFd for io::Stderr {
214    #[inline]
215    fn as_raw_fd(&self) -> RawFd {
216        libc::STDERR_FILENO
217    }
218}
219
220#[stable(feature = "asraw_stdio_locks", since = "1.35.0")]
221#[cfg(not(target_os = "trusty"))]
222impl<'a> AsRawFd for io::StdinLock<'a> {
223    #[inline]
224    fn as_raw_fd(&self) -> RawFd {
225        libc::STDIN_FILENO
226    }
227}
228
229#[stable(feature = "asraw_stdio_locks", since = "1.35.0")]
230impl<'a> AsRawFd for io::StdoutLock<'a> {
231    #[inline]
232    fn as_raw_fd(&self) -> RawFd {
233        libc::STDOUT_FILENO
234    }
235}
236
237#[stable(feature = "asraw_stdio_locks", since = "1.35.0")]
238impl<'a> AsRawFd for io::StderrLock<'a> {
239    #[inline]
240    fn as_raw_fd(&self) -> RawFd {
241        libc::STDERR_FILENO
242    }
243}
244
245/// This impl allows implementing traits that require `AsRawFd` on Arc.
246/// ```
247/// # #[cfg(any(unix, target_os = "wasi"))] mod group_cfg {
248/// # #[cfg(target_os = "wasi")]
249/// # use std::os::wasi::io::AsRawFd;
250/// # #[cfg(unix)]
251/// # use std::os::unix::io::AsRawFd;
252/// use std::net::UdpSocket;
253/// use std::sync::Arc;
254/// trait MyTrait: AsRawFd {
255/// }
256/// impl MyTrait for Arc<UdpSocket> {}
257/// impl MyTrait for Box<UdpSocket> {}
258/// # }
259/// ```
260#[stable(feature = "asrawfd_ptrs", since = "1.63.0")]
261impl<T: AsRawFd> AsRawFd for crate::sync::Arc<T> {
262    #[inline]
263    fn as_raw_fd(&self) -> RawFd {
264        (**self).as_raw_fd()
265    }
266}
267
268#[stable(feature = "asfd_rc", since = "1.69.0")]
269impl<T: AsRawFd> AsRawFd for crate::rc::Rc<T> {
270    #[inline]
271    fn as_raw_fd(&self) -> RawFd {
272        (**self).as_raw_fd()
273    }
274}
275
276#[unstable(feature = "unique_rc_arc", issue = "112566")]
277impl<T: AsRawFd + ?Sized> AsRawFd for crate::rc::UniqueRc<T> {
278    #[inline]
279    fn as_raw_fd(&self) -> RawFd {
280        (**self).as_raw_fd()
281    }
282}
283
284#[stable(feature = "asrawfd_ptrs", since = "1.63.0")]
285impl<T: AsRawFd> AsRawFd for Box<T> {
286    #[inline]
287    fn as_raw_fd(&self) -> RawFd {
288        (**self).as_raw_fd()
289    }
290}
291
292#[stable(feature = "anonymous_pipe", since = "1.87.0")]
293#[cfg(not(target_os = "trusty"))]
294impl AsRawFd for io::PipeReader {
295    fn as_raw_fd(&self) -> RawFd {
296        self.0.as_raw_fd()
297    }
298}
299
300#[stable(feature = "anonymous_pipe", since = "1.87.0")]
301#[cfg(not(target_os = "trusty"))]
302impl FromRawFd for io::PipeReader {
303    unsafe fn from_raw_fd(raw_fd: RawFd) -> Self {
304        Self::from_inner(unsafe { FromRawFd::from_raw_fd(raw_fd) })
305    }
306}
307
308#[stable(feature = "anonymous_pipe", since = "1.87.0")]
309#[cfg(not(target_os = "trusty"))]
310impl IntoRawFd for io::PipeReader {
311    fn into_raw_fd(self) -> RawFd {
312        self.0.into_raw_fd()
313    }
314}
315
316#[stable(feature = "anonymous_pipe", since = "1.87.0")]
317#[cfg(not(target_os = "trusty"))]
318impl AsRawFd for io::PipeWriter {
319    fn as_raw_fd(&self) -> RawFd {
320        self.0.as_raw_fd()
321    }
322}
323
324#[stable(feature = "anonymous_pipe", since = "1.87.0")]
325#[cfg(not(target_os = "trusty"))]
326impl FromRawFd for io::PipeWriter {
327    unsafe fn from_raw_fd(raw_fd: RawFd) -> Self {
328        Self::from_inner(unsafe { FromRawFd::from_raw_fd(raw_fd) })
329    }
330}
331
332#[stable(feature = "anonymous_pipe", since = "1.87.0")]
333#[cfg(not(target_os = "trusty"))]
334impl IntoRawFd for io::PipeWriter {
335    fn into_raw_fd(self) -> RawFd {
336        self.0.into_raw_fd()
337    }
338}
````