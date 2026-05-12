---
title: BorrowedFd in std::os::fd - Rust
url: https://doc.rust-lang.org/stable/std/os/fd/struct.BorrowedFd.html
source: crawler
fetched_at: 2026-05-06T21:31:14.388077232-03:00
rendered_js: false
word_count: 241
summary: This document provides the reference documentation for BorrowedFd, a Rust struct representing a borrowed file descriptor with an associated lifetime to ensure safe resource management.
tags:
    - rust
    - file-descriptor
    - memory-safety
    - ffi
    - system-programming
    - resource-management
category: reference
---

## Struct BorrowedFd

1.66.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#51-54)

```rust
pub struct BorrowedFd<'fd> { /* private fields */ }
```

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

Expand description

A borrowed file descriptor.

This has a lifetime parameter to tie it to the lifetime of something that owns the file descriptor. For the duration of that lifetime, it is guaranteed that nobody will close the file descriptor.

This uses `repr(transparent)` and has the representation of a host file descriptor, so it can be used in FFI in places where a file descriptor is passed as an argument, it is not captured or consumed, and it never has the value `-1`.

This type does not have a [`ToOwned`](https://doc.rust-lang.org/stable/std/borrow/trait.ToOwned.html "trait std::borrow::ToOwned") implementation. Calling `.to_owned()` on a variable of this type will call it on `&BorrowedFd` and use `Clone::clone()` like `ToOwned` does for all types implementing `Clone`. The result will be descriptor borrowed under the same lifetime.

To obtain an [`OwnedFd`](https://doc.rust-lang.org/stable/std/os/fd/struct.OwnedFd.html "struct std::os::fd::OwnedFd"), you can use [`BorrowedFd::try_clone_to_owned`](https://doc.rust-lang.org/stable/std/os/fd/struct.BorrowedFd.html#method.try_clone_to_owned "method std::os::fd::BorrowedFd::try_clone_to_owned") instead, but this is not supported on all platforms.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#74-92)[§](#impl-BorrowedFd%3C'_%3E)

1.63.0 (const: 1.63.0) · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#89-91)

Returns a `BorrowedFd` holding the given raw file descriptor.

##### [§](#safety)Safety

The resource pointed to by `fd` must remain open for the duration of the returned `BorrowedFd`.

##### [§](#panics)Panics

Panics if the raw file descriptor has the value `-1`.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#103-148)[§](#impl-BorrowedFd%3C'_%3E-1)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#113-130)

Available on **neither WebAssembly nor HermitCore nor `target_os=trusty` nor `target_os=motor`** .

Creates a new `OwnedFd` instance that shares the same underlying file description as the existing `BorrowedFd` instance.

[§](#impl-Freeze-for-BorrowedFd%3C'fd%3E)

[§](#impl-RefUnwindSafe-for-BorrowedFd%3C'fd%3E)

[§](#impl-Send-for-BorrowedFd%3C'fd%3E)

[§](#impl-Sync-for-BorrowedFd%3C'fd%3E)

[§](#impl-Unpin-for-BorrowedFd%3C'fd%3E)

[§](#impl-UnsafeUnpin-for-BorrowedFd%3C'fd%3E)

[§](#impl-UnwindSafe-for-BorrowedFd%3C'fd%3E)