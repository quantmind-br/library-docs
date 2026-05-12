---
title: raw.rs - source
url: https://doc.rust-lang.org/src/std/os/windows/io/raw.rs.html#103-105
source: crawler
fetched_at: 2026-05-06T21:24:24.203937044-03:00
rendered_js: false
word_count: 1781
summary: This document defines Rust traits for interacting with raw Windows handles and sockets, allowing for the conversion between standard I/O types and platform-specific primitives.
tags:
    - rust
    - windows
    - ffi
    - io-safety
    - system-programming
    - handles
    - sockets
category: api
---

## std/os/windows/io/ raw.rs

```rust
1//! Windows-specific extensions to general I/O primitives.
2
3#![stable(feature = "rust1", since = "1.0.0")]
4
5#[cfg(doc)]
6use crate::os::windows::io::{AsHandle, AsSocket};
7use crate::os::windows::io::{OwnedHandle, OwnedSocket};
8use crate::os::windows::raw;
9use crate::sys::{AsInner, FromInner, IntoInner};
10use crate::{fs, io, net, ptr, sys};
11
12/// Raw HANDLEs.
13#[stable(feature = "rust1", since = "1.0.0")]
14pub type RawHandle = raw::HANDLE;
15
16/// Raw SOCKETs.
17#[stable(feature = "rust1", since = "1.0.0")]
18pub type RawSocket = raw::SOCKET;
19
20/// Extracts raw handles.
21#[stable(feature = "rust1", since = "1.0.0")]
22pub trait AsRawHandle {
23    /// Extracts the raw handle.
24    ///
25    /// This function is typically used to **borrow** an owned handle.
26    /// When used in this way, this method does **not** pass ownership of the
27    /// raw handle to the caller, and the handle is only guaranteed
28    /// to be valid while the original object has not yet been destroyed.
29    ///
30    /// This function may return null, such as when called on [`Stdin`],
31    /// [`Stdout`], or [`Stderr`] when the console is detached.
32    ///
33    /// However, borrowing is not strictly required. See [`AsHandle::as_handle`]
34    /// for an API which strictly borrows a handle.
35    ///
36    /// [`Stdin`]: io::Stdin
37    /// [`Stdout`]: io::Stdout
38    /// [`Stderr`]: io::Stderr
39    #[stable(feature = "rust1", since = "1.0.0")]
40    fn as_raw_handle(&self) -> RawHandle;
41}
42
43/// Constructs I/O objects from raw handles.
44#[stable(feature = "from_raw_os", since = "1.1.0")]
45pub trait FromRawHandle {
46    /// Constructs a new I/O object from the specified raw handle.
47    ///
48    /// This function is typically used to **consume ownership** of the handle
49    /// given, passing responsibility for closing the handle to the returned
50    /// object. When used in this way, the returned object
51    /// will take responsibility for closing it when the object goes out of
52    /// scope.
53    ///
54    /// However, consuming ownership is not strictly required. Use a
55    /// `From<OwnedHandle>::from` implementation for an API which strictly
56    /// consumes ownership.
57    ///
58    /// # Safety
59    ///
60    /// The `handle` passed in must:
61    ///   - be an [owned handle][io-safety]; in particular, it must be open.
62    ///   - be a handle for a resource that may be freed via [`CloseHandle`]
63    ///     (as opposed to `RegCloseKey` or other close functions).
64    ///
65    /// Note that the handle *may* have the value `INVALID_HANDLE_VALUE` (-1),
66    /// which is sometimes a valid handle value. See [here] for the full story.
67    ///
68    /// [`CloseHandle`]: https://docs.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle
69    /// [here]: https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443
70    /// [io-safety]: io#io-safety
71    #[stable(feature = "from_raw_os", since = "1.1.0")]
72    unsafe fn from_raw_handle(handle: RawHandle) -> Self;
73}
74
75/// A trait to express the ability to consume an object and acquire ownership of
76/// its raw `HANDLE`.
77#[stable(feature = "into_raw_os", since = "1.4.0")]
78pub trait IntoRawHandle {
79    /// Consumes this object, returning the raw underlying handle.
80    ///
81    /// This function is typically used to **transfer ownership** of the underlying
82    /// handle to the caller. When used in this way, callers are then the unique
83    /// owners of the handle and must close it once it's no longer needed.
84    ///
85    /// However, transferring ownership is not strictly required. Use a
86    /// `Into<OwnedHandle>::into` implementation for an API which strictly
87    /// transfers ownership.
88    #[must_use = "losing the raw handle may leak resources"]
89    #[stable(feature = "into_raw_os", since = "1.4.0")]
90    fn into_raw_handle(self) -> RawHandle;
91}
92
93#[stable(feature = "rust1", since = "1.0.0")]
94impl AsRawHandle for fs::File {
95    #[inline]
96    fn as_raw_handle(&self) -> RawHandle {
97        self.as_inner().as_raw_handle() as RawHandle
98    }
99}
100
101#[stable(feature = "asraw_stdio", since = "1.21.0")]
102impl AsRawHandle for io::Stdin {
103    fn as_raw_handle(&self) -> RawHandle {
104        stdio_handle(unsafe { sys::c::GetStdHandle(sys::c::STD_INPUT_HANDLE) as RawHandle })
105    }
106}
107
108#[stable(feature = "asraw_stdio", since = "1.21.0")]
109impl AsRawHandle for io::Stdout {
110    fn as_raw_handle(&self) -> RawHandle {
111        stdio_handle(unsafe { sys::c::GetStdHandle(sys::c::STD_OUTPUT_HANDLE) as RawHandle })
112    }
113}
114
115#[stable(feature = "asraw_stdio", since = "1.21.0")]
116impl AsRawHandle for io::Stderr {
117    fn as_raw_handle(&self) -> RawHandle {
118        stdio_handle(unsafe { sys::c::GetStdHandle(sys::c::STD_ERROR_HANDLE) as RawHandle })
119    }
120}
121
122#[stable(feature = "asraw_stdio_locks", since = "1.35.0")]
123impl<'a> AsRawHandle for io::StdinLock<'a> {
124    fn as_raw_handle(&self) -> RawHandle {
125        stdio_handle(unsafe { sys::c::GetStdHandle(sys::c::STD_INPUT_HANDLE) as RawHandle })
126    }
127}
128
129#[stable(feature = "asraw_stdio_locks", since = "1.35.0")]
130impl<'a> AsRawHandle for io::StdoutLock<'a> {
131    fn as_raw_handle(&self) -> RawHandle {
132        stdio_handle(unsafe { sys::c::GetStdHandle(sys::c::STD_OUTPUT_HANDLE) as RawHandle })
133    }
134}
135
136#[stable(feature = "asraw_stdio_locks", since = "1.35.0")]
137impl<'a> AsRawHandle for io::StderrLock<'a> {
138    fn as_raw_handle(&self) -> RawHandle {
139        stdio_handle(unsafe { sys::c::GetStdHandle(sys::c::STD_ERROR_HANDLE) as RawHandle })
140    }
141}
142
143// Translate a handle returned from `GetStdHandle` into a handle to return to
144// the user.
145fn stdio_handle(raw: RawHandle) -> RawHandle {
146    // `GetStdHandle` isn't expected to actually fail, so when it returns
147    // `INVALID_HANDLE_VALUE`, it means we were launched from a parent which
148    // didn't provide us with stdio handles, such as a parent with a detached
149    // console. In that case, return null to the user, which is consistent
150    // with what they'd get in the parent, and which avoids the problem that
151    // `INVALID_HANDLE_VALUE` aliases the current process handle.
152    if raw == sys::c::INVALID_HANDLE_VALUE { ptr::null_mut() } else { raw }
153}
154
155#[stable(feature = "from_raw_os", since = "1.1.0")]
156impl FromRawHandle for fs::File {
157    #[inline]
158    unsafe fn from_raw_handle(handle: RawHandle) -> fs::File {
159        unsafe {
160            let handle = handle as sys::c::HANDLE;
161            fs::File::from_inner(sys::fs::File::from_inner(FromInner::from_inner(
162                OwnedHandle::from_raw_handle(handle),
163            )))
164        }
165    }
166}
167
168#[stable(feature = "into_raw_os", since = "1.4.0")]
169impl IntoRawHandle for fs::File {
170    #[inline]
171    fn into_raw_handle(self) -> RawHandle {
172        self.into_inner().into_raw_handle() as *mut _
173    }
174}
175
176/// Extracts raw sockets.
177#[stable(feature = "rust1", since = "1.0.0")]
178pub trait AsRawSocket {
179    /// Extracts the raw socket.
180    ///
181    /// This function is typically used to **borrow** an owned socket.
182    /// When used in this way, this method does **not** pass ownership of the
183    /// raw socket to the caller, and the socket is only guaranteed
184    /// to be valid while the original object has not yet been destroyed.
185    ///
186    /// However, borrowing is not strictly required. See [`AsSocket::as_socket`]
187    /// for an API which strictly borrows a socket.
188    #[stable(feature = "rust1", since = "1.0.0")]
189    fn as_raw_socket(&self) -> RawSocket;
190}
191
192/// Creates I/O objects from raw sockets.
193#[stable(feature = "from_raw_os", since = "1.1.0")]
194pub trait FromRawSocket {
195    /// Constructs a new I/O object from the specified raw socket.
196    ///
197    /// This function is typically used to **consume ownership** of the socket
198    /// given, passing responsibility for closing the socket to the returned
199    /// object. When used in this way, the returned object
200    /// will take responsibility for closing it when the object goes out of
201    /// scope.
202    ///
203    /// However, consuming ownership is not strictly required. Use a
204    /// `From<OwnedSocket>::from` implementation for an API which strictly
205    /// consumes ownership.
206    ///
207    /// # Safety
208    ///
209    /// The `socket` passed in must:
210    ///   - be an [owned socket][io-safety]; in particular, it must be open.
211    ///   - be a socket that may be freed via [`closesocket`].
212    ///
213    /// [`closesocket`]: https://docs.microsoft.com/en-us/windows/win32/api/winsock2/nf-winsock2-closesocket
214    /// [io-safety]: io#io-safety
215    #[stable(feature = "from_raw_os", since = "1.1.0")]
216    unsafe fn from_raw_socket(sock: RawSocket) -> Self;
217}
218
219/// A trait to express the ability to consume an object and acquire ownership of
220/// its raw `SOCKET`.
221#[stable(feature = "into_raw_os", since = "1.4.0")]
222pub trait IntoRawSocket {
223    /// Consumes this object, returning the raw underlying socket.
224    ///
225    /// This function is typically used to **transfer ownership** of the underlying
226    /// socket to the caller. When used in this way, callers are then the unique
227    /// owners of the socket and must close it once it's no longer needed.
228    ///
229    /// However, transferring ownership is not strictly required. Use a
230    /// `Into<OwnedSocket>::into` implementation for an API which strictly
231    /// transfers ownership.
232    #[must_use = "losing the raw socket may leak resources"]
233    #[stable(feature = "into_raw_os", since = "1.4.0")]
234    fn into_raw_socket(self) -> RawSocket;
235}
236
237#[stable(feature = "rust1", since = "1.0.0")]
238impl AsRawSocket for net::TcpStream {
239    #[inline]
240    fn as_raw_socket(&self) -> RawSocket {
241        self.as_inner().socket().as_raw_socket()
242    }
243}
244#[stable(feature = "rust1", since = "1.0.0")]
245impl AsRawSocket for net::TcpListener {
246    #[inline]
247    fn as_raw_socket(&self) -> RawSocket {
248        self.as_inner().socket().as_raw_socket()
249    }
250}
251#[stable(feature = "rust1", since = "1.0.0")]
252impl AsRawSocket for net::UdpSocket {
253    #[inline]
254    fn as_raw_socket(&self) -> RawSocket {
255        self.as_inner().socket().as_raw_socket()
256    }
257}
258
259#[stable(feature = "from_raw_os", since = "1.1.0")]
260impl FromRawSocket for net::TcpStream {
261    #[inline]
262    unsafe fn from_raw_socket(sock: RawSocket) -> net::TcpStream {
263        unsafe {
264            let sock = sys::net::Socket::from_inner(OwnedSocket::from_raw_socket(sock));
265            net::TcpStream::from_inner(sys::net::TcpStream::from_inner(sock))
266        }
267    }
268}
269#[stable(feature = "from_raw_os", since = "1.1.0")]
270impl FromRawSocket for net::TcpListener {
271    #[inline]
272    unsafe fn from_raw_socket(sock: RawSocket) -> net::TcpListener {
273        unsafe {
274            let sock = sys::net::Socket::from_inner(OwnedSocket::from_raw_socket(sock));
275            net::TcpListener::from_inner(sys::net::TcpListener::from_inner(sock))
276        }
277    }
278}
279#[stable(feature = "from_raw_os", since = "1.1.0")]
280impl FromRawSocket for net::UdpSocket {
281    #[inline]
282    unsafe fn from_raw_socket(sock: RawSocket) -> net::UdpSocket {
283        unsafe {
284            let sock = sys::net::Socket::from_inner(OwnedSocket::from_raw_socket(sock));
285            net::UdpSocket::from_inner(sys::net::UdpSocket::from_inner(sock))
286        }
287    }
288}
289
290#[stable(feature = "into_raw_os", since = "1.4.0")]
291impl IntoRawSocket for net::TcpStream {
292    #[inline]
293    fn into_raw_socket(self) -> RawSocket {
294        self.into_inner().into_socket().into_inner().into_raw_socket()
295    }
296}
297
298#[stable(feature = "into_raw_os", since = "1.4.0")]
299impl IntoRawSocket for net::TcpListener {
300    #[inline]
301    fn into_raw_socket(self) -> RawSocket {
302        self.into_inner().into_socket().into_inner().into_raw_socket()
303    }
304}
305
306#[stable(feature = "into_raw_os", since = "1.4.0")]
307impl IntoRawSocket for net::UdpSocket {
308    #[inline]
309    fn into_raw_socket(self) -> RawSocket {
310        self.into_inner().into_socket().into_inner().into_raw_socket()
311    }
312}
313
314#[stable(feature = "anonymous_pipe", since = "1.87.0")]
315impl AsRawHandle for io::PipeReader {
316    fn as_raw_handle(&self) -> RawHandle {
317        self.0.as_raw_handle()
318    }
319}
320
321#[stable(feature = "anonymous_pipe", since = "1.87.0")]
322impl FromRawHandle for io::PipeReader {
323    unsafe fn from_raw_handle(raw_handle: RawHandle) -> Self {
324        unsafe { Self::from_inner(FromRawHandle::from_raw_handle(raw_handle)) }
325    }
326}
327
328#[stable(feature = "anonymous_pipe", since = "1.87.0")]
329impl IntoRawHandle for io::PipeReader {
330    fn into_raw_handle(self) -> RawHandle {
331        self.0.into_raw_handle()
332    }
333}
334
335#[stable(feature = "anonymous_pipe", since = "1.87.0")]
336impl AsRawHandle for io::PipeWriter {
337    fn as_raw_handle(&self) -> RawHandle {
338        self.0.as_raw_handle()
339    }
340}
341
342#[stable(feature = "anonymous_pipe", since = "1.87.0")]
343impl FromRawHandle for io::PipeWriter {
344    unsafe fn from_raw_handle(raw_handle: RawHandle) -> Self {
345        unsafe { Self::from_inner(FromRawHandle::from_raw_handle(raw_handle)) }
346    }
347}
348
349#[stable(feature = "anonymous_pipe", since = "1.87.0")]
350impl IntoRawHandle for io::PipeWriter {
351    fn into_raw_handle(self) -> RawHandle {
352        self.0.into_raw_handle()
353    }
354}
```