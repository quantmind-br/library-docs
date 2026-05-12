---
title: BorrowedHandle in std::os::windows::io - Rust
url: https://doc.rust-lang.org/stable/std/os/windows/io/struct.BorrowedHandle.html
source: crawler
fetched_at: 2026-05-06T21:31:17.06892639-03:00
rendered_js: false
word_count: 262
summary: The BorrowedHandle struct represents a temporary, lifetime-bound reference to a Windows OS handle for use in safe FFI operations.
tags:
    - rust
    - windows-api
    - ffi
    - memory-safety
    - system-programming
    - handles
category: reference
---

## Struct BorrowedHandle

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#37-40)

```rust
pub struct BorrowedHandle<'handle> { /* private fields */ }
```

Available on **Windows** only.

Expand description

A borrowed handle.

This has a lifetime parameter to tie it to the lifetime of something that owns the handle.

This uses `repr(transparent)` and has the representation of a host handle, so it can be used in FFI in places where a handle is passed as an argument, it is not captured or consumed.

Note that it *may* have the value `-1`, which in `BorrowedHandle` always represents a valid handle value, such as [the current process handle](https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess#remarks), and not `INVALID_HANDLE_VALUE`, despite the two having the same value. See [here](https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443) for the full story.

And, it *may* have the value `NULL` (0), which can occur when consoles are detached from processes, or when `windows_subsystem` is used.

This type’s `.to_owned()` implementation returns another `BorrowedHandle` rather than an `OwnedHandle`. It just makes a trivial copy of the raw handle, which is then borrowed under the same lifetime.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#132-153)[§](#impl-BorrowedHandle%3C'_%3E)

1.63.0 (const: 1.63.0) · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#150-152)

Returns a `BorrowedHandle` holding the given raw handle.

##### [§](#safety)Safety

The resource pointed to by `handle` must be a valid open handle, it must remain open for the duration of the returned `BorrowedHandle`.

Note that it *may* have the value `INVALID_HANDLE_VALUE` (-1), which is sometimes a valid handle value. See [here](https://devblogs.microsoft.com/oldnewthing/20040302-00/?p=40443) for the full story.

And, it *may* have the value `NULL` (0), which can occur when consoles are detached from processes, or when `windows_subsystem` is used.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#192-231)[§](#impl-BorrowedHandle%3C'_%3E-1)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#196-198)

Creates a new `OwnedHandle` instance that shares the same underlying object as the existing `BorrowedHandle` instance.

[§](#impl-Freeze-for-BorrowedHandle%3C'handle%3E)

[§](#impl-RefUnwindSafe-for-BorrowedHandle%3C'handle%3E)

[§](#impl-Unpin-for-BorrowedHandle%3C'handle%3E)

[§](#impl-UnsafeUnpin-for-BorrowedHandle%3C'handle%3E)

[§](#impl-UnwindSafe-for-BorrowedHandle%3C'handle%3E)