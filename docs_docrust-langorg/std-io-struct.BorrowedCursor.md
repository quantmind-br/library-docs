---
title: BorrowedCursor in std::io - Rust
url: https://doc.rust-lang.org/std/io/struct.BorrowedCursor.html
source: crawler
fetched_at: 2026-05-06T21:24:27.451508108-03:00
rendered_js: false
word_count: 771
summary: BorrowedCursor provides a writeable view into the unfilled portion of a BorrowedBuf, allowing for safe manual or automated data insertion and buffer management.
tags:
    - rust
    - io
    - buffer
    - memory-management
    - experimental-api
    - nightly
category: reference
---

## Struct BorrowedCursor

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#201)

```rust
pub struct BorrowedCursor<'a> { /* private fields */ }
```

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Expand description

A writeable view of the unfilled portion of a [`BorrowedBuf`](https://doc.rust-lang.org/std/io/struct.BorrowedBuf.html "struct std::io::BorrowedBuf").

The unfilled portion consists of an initialized and an uninitialized part; see [`BorrowedBuf`](https://doc.rust-lang.org/std/io/struct.BorrowedBuf.html "struct std::io::BorrowedBuf") for details.

Data can be written directly to the cursor by using [`append`](https://doc.rust-lang.org/std/io/struct.BorrowedCursor.html#method.append "method std::io::BorrowedCursor::append") or indirectly by getting a slice of part or all of the cursor and writing into the slice. In the indirect case, the caller must call [`advance`](https://doc.rust-lang.org/std/io/struct.BorrowedCursor.html#method.advance "method std::io::BorrowedCursor::advance") after writing to inform the cursor how many bytes have been written.

Once data is written to the cursor, it becomes part of the filled portion of the underlying `BorrowedBuf` and can no longer be accessed or re-written by the cursor. I.e., the cursor tracks the unfilled part of the underlying `BorrowedBuf`.

The lifetime `'a` is a bound on the lifetime of the underlying buffer (which means it is a bound on the data in that buffer by transitivity).

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#209)[§](#impl-BorrowedCursor%3C'a%3E)

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#215)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Reborrows this cursor by cloning it with a smaller lifetime.

Since a cursor maintains unique access to its underlying buffer, the borrowed cursor is not accessible while the new cursor exists.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#229)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Returns the available space in the cursor.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#237)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Returns the number of bytes written to the `BorrowedBuf` this cursor was created from.

In particular, the count returned is shared by all reborrows of the cursor.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#243)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Returns a mutable reference to the initialized portion of the cursor.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#257)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Returns a mutable reference to the whole cursor.

##### [§](#safety)Safety

The caller must not uninitialize any bytes in the initialized portion of the cursor.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#275)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Advances the cursor by asserting that `n` bytes have been filled.

After advancing, the `n` bytes are no longer accessible via the cursor and can only be accessed via the underlying buffer. I.e., the buffer’s filled portion grows by `n` elements and its unfilled portion (and the capacity of this cursor) shrinks by `n` elements.

If less than `n` bytes initialized (by the cursor’s point of view), `set_init` should be called first.

##### [§](#panics)Panics

Panics if there are less than `n` bytes initialized.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#294)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Advances the cursor by asserting that `n` bytes have been filled.

After advancing, the `n` bytes are no longer accessible via the cursor and can only be accessed via the underlying buffer. I.e., the buffer’s filled portion grows by `n` elements and its unfilled portion (and the capacity of this cursor) shrinks by `n` elements.

##### [§](#safety-1)Safety

The caller must ensure that the first `n` bytes of the cursor have been properly initialised.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#302)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Initializes all bytes in the cursor.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#325)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Asserts that the first `n` unfilled bytes of the cursor are initialized.

`BorrowedBuf` assumes that bytes are never de-initialized, so this method does nothing when called with fewer bytes than are already known to be initialized.

##### [§](#safety-2)Safety

The caller must ensure that the first `n` bytes of the buffer have already been initialized.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#336)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Appends data to the cursor, advancing position within its buffer.

##### [§](#panics-1)Panics

Panics if `self.capacity()` is less than `buf.len()`.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#360)

🔬This is a nightly-only experimental API. (`core_io_borrowed_buf` [#117693](https://github.com/rust-lang/rust/issues/117693))

Runs the given closure with a `BorrowedBuf` containing the unfilled part of the cursor.

This enables inspecting what was written to the cursor.

##### [§](#panics-2)Panics

Panics if the `BorrowedBuf` given to the closure is replaced by another one.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#200)[§](#impl-Debug-for-BorrowedCursor%3C'a%3E)

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#75)[§](#impl-From%3CBorrowedCursor%3C'data%3E%3E-for-BorrowedBuf%3C'data%3E)

Creates a new `BorrowedBuf` from a cursor.

Use `BorrowedCursor::with_unfilled_buf` instead for a safer alternative.

[Source](https://doc.rust-lang.org/src/core/io/borrowed_buf.rs.html#77)[§](#method.from)

Converts to this type from the input type.

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#672-717)[§](#impl-Write-for-BorrowedCursor%3C'a%3E)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#674-678)[§](#method.write)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#681-691)[§](#method.write_vectored)

Like [`write`](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#694-696)[§](#method.is_write_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#699-701)[§](#method.write_all)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#704-711)[§](#method.write_all_vectored)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_all_vectored)

[Source](https://doc.rust-lang.org/src/std/io/impls.rs.html#714-716)[§](#method.flush)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#tymethod.flush)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/std/io/trait.Write.html#method.by_ref)

[§](#impl-Freeze-for-BorrowedCursor%3C'a%3E)

[§](#impl-RefUnwindSafe-for-BorrowedCursor%3C'a%3E)

[§](#impl-Send-for-BorrowedCursor%3C'a%3E)

[§](#impl-Sync-for-BorrowedCursor%3C'a%3E)

[§](#impl-Unpin-for-BorrowedCursor%3C'a%3E)

[§](#impl-UnsafeUnpin-for-BorrowedCursor%3C'a%3E)

[§](#impl-UnwindSafe-for-BorrowedCursor%3C'a%3E)