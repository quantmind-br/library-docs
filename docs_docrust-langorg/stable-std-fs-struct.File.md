---
title: File in std::fs - Rust
url: https://doc.rust-lang.org/stable/std/fs/struct.File.html
source: crawler
fetched_at: 2026-05-06T21:28:12.706636083-03:00
rendered_js: false
word_count: 4069
summary: This document provides documentation for the Rust standard library File struct, which facilitates filesystem operations including reading, writing, and seeking through an open file handle.
tags:
    - rust
    - filesystem
    - file-io
    - std-fs
    - buffered-io
    - system-programming
category: api
---

## Struct File

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#135-137)

```rust
pub struct File { /* private fields */ }
```

Expand description

An object providing access to an open file on the filesystem.

An instance of a `File` can be read and/or written depending on what options it was opened with. Files also implement [`Seek`](https://doc.rust-lang.org/stable/std/io/trait.Seek.html "trait std::io::Seek") to alter the logical cursor that the file contains internally.

Files are automatically closed when they go out of scope. Errors detected on closing are ignored by the implementation of `Drop`. Use the method [`sync_all`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.sync_all "method std::fs::File::sync_all") if these errors must be manually handled.

`File` does not buffer reads and writes. For efficiency, consider wrapping the file in a [`BufReader`](https://doc.rust-lang.org/stable/std/io/struct.BufReader.html "struct std::io::BufReader") or [`BufWriter`](https://doc.rust-lang.org/stable/std/io/struct.BufWriter.html "struct std::io::BufWriter") when performing many small [`read`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.read "method std::fs::File::read") or [`write`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.write "method std::fs::File::write") calls, unless unbuffered reads and writes are required.

## [§](#examples)Examples

Creates a new file and write bytes to it (you can also use [`write`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.write "method std::fs::File::write")):

```rust
use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::create("foo.txt")?;
    file.write_all(b"Hello, world!")?;
    Ok(())
}
```

Reads the contents of a file into a [`String`](https://doc.rust-lang.org/stable/std/string/struct.String.html "struct std::string::String") (you can also use [`read`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.read "method std::fs::File::read")):

```rust
use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("foo.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    assert_eq!(contents, "Hello, world!");
    Ok(())
}
```

Using a buffered [`Read`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.read "method std::fs::File::read")er:

```rust
use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let file = File::open("foo.txt")?;
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents)?;
    assert_eq!(contents, "Hello, world!");
    Ok(())
}
```

Note that, although read and write methods require a `&mut File`, because of the interfaces for [`Read`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.read "method std::fs::File::read") and [`Write`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.write "method std::fs::File::write"), the holder of a `&File` can still modify the file, either through methods that take `&File` or by retrieving the underlying OS object and modifying the file that way. Additionally, many operating systems allow concurrent modification of files by different processes. Avoid assuming that holding a `&File` means that the file will not change.

## [§](#platform-specific-behavior)Platform-specific behavior

On Windows, the implementation of [`Read`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.read "method std::fs::File::read") and [`Write`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.write "method std::fs::File::write") traits for `File` perform synchronous I/O operations. Therefore the underlying file must not have been opened for asynchronous I/O (e.g. by using `FILE_FLAG_OVERLAPPED`).

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#542-1278)[§](#impl-File)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#570-572)

Attempts to open a file in read-only mode.

See the [`OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open") method for more details.

If you only need to read the entire file contents, consider [`std::fs::read()`](https://doc.rust-lang.org/stable/std/fs/fn.read.html "fn std::fs::read") or [`std::fs::read_to_string()`](https://doc.rust-lang.org/stable/std/fs/fn.read_to_string.html "fn std::fs::read_to_string") instead.

##### [§](#errors)Errors

This function will return an error if `path` does not already exist. Other errors may also be returned according to [`OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open").

##### [§](#examples-1)Examples

```rust
use std::fs::File;
use std::io::Read;

fn main() -> std::io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let mut data = vec![];
    f.read_to_end(&mut data)?;
    Ok(())
}
```

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#606-611)

🔬This is a nightly-only experimental API. (`file_buffered` [#130804](https://github.com/rust-lang/rust/issues/130804))

Attempts to open a file in read-only mode with buffering.

See the [`OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open") method, the [`BufReader`](https://doc.rust-lang.org/stable/std/io/struct.BufReader.html "struct std::io::BufReader") type, and the [`BufRead`](https://doc.rust-lang.org/stable/std/io/trait.BufRead.html "trait std::io::BufRead") trait for more details.

If you only need to read the entire file contents, consider [`std::fs::read()`](https://doc.rust-lang.org/stable/std/fs/fn.read.html "fn std::fs::read") or [`std::fs::read_to_string()`](https://doc.rust-lang.org/stable/std/fs/fn.read_to_string.html "fn std::fs::read_to_string") instead.

##### [§](#errors-1)Errors

This function will return an error if `path` does not already exist, or if memory allocation fails for the new buffer. Other errors may also be returned according to [`OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open").

##### [§](#examples-2)Examples

```rust
#![feature(file_buffered)]
use std::fs::File;
use std::io::BufRead;

fn main() -> std::io::Result<()> {
    let mut f = File::open_buffered("foo.txt")?;
    assert!(f.capacity() > 0);
    for (line, i) in f.lines().zip(1..) {
        println!("{i:6}: {}", line?);
    }
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#638-640)

Opens a file in write-only mode.

This function will create a file if it does not exist, and will truncate it if it does.

Depending on the platform, this function may fail if the full directory path does not exist. See the [`OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open") function for more details.

See also [`std::fs::write()`](https://doc.rust-lang.org/stable/std/fs/fn.write.html "fn std::fs::write") for a simple function to create a file with some given data.

##### [§](#examples-3)Examples

```rust
use std::fs::File;
use std::io::Write;

fn main() -> std::io::Result<()> {
    let mut f = File::create("foo.txt")?;
    f.write_all(&1234_u32.to_be_bytes())?;
    Ok(())
}
```

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#674-679)

🔬This is a nightly-only experimental API. (`file_buffered` [#130804](https://github.com/rust-lang/rust/issues/130804))

Opens a file in write-only mode with buffering.

This function will create a file if it does not exist, and will truncate it if it does.

Depending on the platform, this function may fail if the full directory path does not exist.

See the [`OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open") method and the [`BufWriter`](https://doc.rust-lang.org/stable/std/io/struct.BufWriter.html "struct std::io::BufWriter") type for more details.

See also [`std::fs::write()`](https://doc.rust-lang.org/stable/std/fs/fn.write.html "fn std::fs::write") for a simple function to create a file with some given data.

##### [§](#examples-4)Examples

```rust
#![feature(file_buffered)]
use std::fs::File;
use std::io::Write;

fn main() -> std::io::Result<()> {
    let mut f = File::create_buffered("foo.txt")?;
    assert!(f.capacity() > 0);
    for i in 0..100 {
        writeln!(&mut f, "{i}")?;
    }
    f.flush()?;
    Ok(())
}
```

1.77.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#712-714)

Creates a new file in read-write mode; error if the file exists.

This function will create a file if it does not exist, or return an error if it does. This way, if the call succeeds, the file returned is guaranteed to be new. If a file exists at the target location, creating a new file will fail with [`AlreadyExists`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.AlreadyExists "variant std::io::ErrorKind::AlreadyExists") or another error based on the situation. See [`OpenOptions::open`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.open "method std::fs::OpenOptions::open") for a non-exhaustive list of likely errors.

This option is useful because it is atomic. Otherwise between checking whether a file exists and creating a new one, the file may have been created by another process (a [TOCTOU](https://doc.rust-lang.org/stable/std/fs/index.html#time-of-check-to-time-of-use-toctou "mod std::fs") race condition / attack).

This can also be written using `File::options().read(true).write(true).create_new(true).open(...)`.

##### [§](#examples-5)Examples

```rust
use std::fs::File;
use std::io::Write;

fn main() -> std::io::Result<()> {
    let mut f = File::create_new("foo.txt")?;
    f.write_all("Hello, world!".as_bytes())?;
    Ok(())
}
```

1.58.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#745-747)

Returns a new OpenOptions object.

This function returns a new OpenOptions object that you can use to open or create a file with specific options if `open()` or `create()` are not appropriate.

It is equivalent to `OpenOptions::new()`, but allows you to write more readable code. Instead of `OpenOptions::new().append(true).open("example.log")`, you can write `File::options().append(true).open("example.log")`. This also avoids the need to import `OpenOptions`.

See the [`OpenOptions::new`](https://doc.rust-lang.org/stable/std/fs/struct.OpenOptions.html#method.new "associated function std::fs::OpenOptions::new") function for more details.

##### [§](#examples-6)Examples

```rust
use std::fs::File;
use std::io::Write;

fn main() -> std::io::Result<()> {
    let mut f = File::options().append(true).open("example.log")?;
    writeln!(&mut f, "new line")?;
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#780-782)

Attempts to sync all OS-internal file content and metadata to disk.

This function will attempt to ensure that all in-memory data reaches the filesystem before returning.

This can be used to handle errors that would otherwise only be caught when the `File` is closed, as dropping a `File` will ignore all errors. Note, however, that `sync_all` is generally more expensive than closing a file by dropping it, because the latter is not required to block until the data has been written to the filesystem.

If synchronizing the metadata is not required, use [`sync_data`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.sync_data "method std::fs::File::sync_data") instead.

##### [§](#examples-7)Examples

```rust
use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut f = File::create("foo.txt")?;
    f.write_all(b"Hello, world!")?;

    f.sync_all()?;
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#812-814)

This function is similar to [`sync_all`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.sync_all "method std::fs::File::sync_all"), except that it might not synchronize file metadata to the filesystem.

This is intended for use cases that must synchronize content, but don’t need the metadata on disk. The goal of this method is to reduce disk operations.

Note that some platforms may simply implement this in terms of [`sync_all`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.sync_all "method std::fs::File::sync_all").

##### [§](#examples-8)Examples

```rust
use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut f = File::create("foo.txt")?;
    f.write_all(b"Hello, world!")?;

    f.sync_data()?;
    Ok(())
}
```

1.89.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#865-867)

Acquire an exclusive lock on the file. Blocks until the lock can be acquired.

This acquires an exclusive lock; no other file handle to this file may acquire another lock.

This lock may be advisory or mandatory. This lock is meant to interact with [`lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock "method std::fs::File::lock"), [`try_lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock "method std::fs::File::try_lock"), [`lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock_shared "method std::fs::File::lock_shared"), [`try_lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock_shared "method std::fs::File::try_lock_shared"), and [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock"). Its interactions with other methods, such as [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") and [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") are platform specific, and it may or may not cause non-lockholders to block.

If this file handle/descriptor, or a clone of it, already holds a lock the exact behavior is unspecified and platform dependent, including the possibility that it will deadlock. However, if this method returns, then an exclusive lock is held.

If the file is not open for writing, it is unspecified whether this function returns an error.

The lock will be released when this file (along with any other file descriptors/handles duplicated or inherited from it) is closed, or if the [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock") method is called.

##### [§](#platform-specific-behavior-1)Platform-specific behavior

This function currently corresponds to the `flock` function on Unix with the `LOCK_EX` flag, and the `LockFileEx` function on Windows with the `LOCKFILE_EXCLUSIVE_LOCK` flag. Note that, this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

On Windows, locking a file will fail if the file is opened only for append. To lock a file, open it with one of `.read(true)`, `.read(true).append(true)`, or `.write(true)`.

##### [§](#examples-9)Examples

```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    let f = File::create("foo.txt")?;
    f.lock()?;
    Ok(())
}
```

1.89.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#917-919)

Acquire a shared (non-exclusive) lock on the file. Blocks until the lock can be acquired.

This acquires a shared lock; more than one file handle may hold a shared lock, but none may hold an exclusive lock at the same time.

This lock may be advisory or mandatory. This lock is meant to interact with [`lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock "method std::fs::File::lock"), [`try_lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock "method std::fs::File::try_lock"), [`lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock_shared "method std::fs::File::lock_shared"), [`try_lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock_shared "method std::fs::File::try_lock_shared"), and [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock"). Its interactions with other methods, such as [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") and [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") are platform specific, and it may or may not cause non-lockholders to block.

If this file handle/descriptor, or a clone of it, already holds a lock, the exact behavior is unspecified and platform dependent, including the possibility that it will deadlock. However, if this method returns, then a shared lock is held.

The lock will be released when this file (along with any other file descriptors/handles duplicated or inherited from it) is closed, or if the [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock") method is called.

##### [§](#platform-specific-behavior-2)Platform-specific behavior

This function currently corresponds to the `flock` function on Unix with the `LOCK_SH` flag, and the `LockFileEx` function on Windows. Note that, this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

On Windows, locking a file will fail if the file is opened only for append. To lock a file, open it with one of `.read(true)`, `.read(true).append(true)`, or `.write(true)`.

##### [§](#examples-10)Examples

```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    let f = File::open("foo.txt")?;
    f.lock_shared()?;
    Ok(())
}
```

1.89.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#981-983)

Try to acquire an exclusive lock on the file.

Returns `Err(TryLockError::WouldBlock)` if a different lock is already held on this file (via another handle/descriptor).

This acquires an exclusive lock; no other file handle to this file may acquire another lock.

This lock may be advisory or mandatory. This lock is meant to interact with [`lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock "method std::fs::File::lock"), [`try_lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock "method std::fs::File::try_lock"), [`lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock_shared "method std::fs::File::lock_shared"), [`try_lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock_shared "method std::fs::File::try_lock_shared"), and [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock"). Its interactions with other methods, such as [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") and [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") are platform specific, and it may or may not cause non-lockholders to block.

If this file handle/descriptor, or a clone of it, already holds a lock, the exact behavior is unspecified and platform dependent, including the possibility that it will deadlock. However, if this method returns `Ok(())`, then it has acquired an exclusive lock.

If the file is not open for writing, it is unspecified whether this function returns an error.

The lock will be released when this file (along with any other file descriptors/handles duplicated or inherited from it) is closed, or if the [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock") method is called.

##### [§](#platform-specific-behavior-3)Platform-specific behavior

This function currently corresponds to the `flock` function on Unix with the `LOCK_EX` and `LOCK_NB` flags, and the `LockFileEx` function on Windows with the `LOCKFILE_EXCLUSIVE_LOCK` and `LOCKFILE_FAIL_IMMEDIATELY` flags. Note that, this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

On Windows, locking a file will fail if the file is opened only for append. To lock a file, open it with one of `.read(true)`, `.read(true).append(true)`, or `.write(true)`.

##### [§](#examples-11)Examples

```rust
use std::fs::{File, TryLockError};

fn main() -> std::io::Result<()> {
    let f = File::create("foo.txt")?;
    // Explicit handling of the WouldBlock error
    match f.try_lock() {
        Ok(_) => (),
        Err(TryLockError::WouldBlock) => (), // Lock not acquired
        Err(TryLockError::Error(err)) => return Err(err),
    }
    // Alternately, propagate the error as an io::Error
    f.try_lock()?;
    Ok(())
}
```

1.89.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1045-1047)

Try to acquire a shared (non-exclusive) lock on the file.

Returns `Err(TryLockError::WouldBlock)` if a different lock is already held on this file (via another handle/descriptor).

This acquires a shared lock; more than one file handle may hold a shared lock, but none may hold an exclusive lock at the same time.

This lock may be advisory or mandatory. This lock is meant to interact with [`lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock "method std::fs::File::lock"), [`try_lock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock "method std::fs::File::try_lock"), [`lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.lock_shared "method std::fs::File::lock_shared"), [`try_lock_shared`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.try_lock_shared "method std::fs::File::try_lock_shared"), and [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock"). Its interactions with other methods, such as [`read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") and [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") are platform specific, and it may or may not cause non-lockholders to block.

If this file handle, or a clone of it, already holds a lock, the exact behavior is unspecified and platform dependent, including the possibility that it will deadlock. However, if this method returns `Ok(())`, then it has acquired a shared lock.

The lock will be released when this file (along with any other file descriptors/handles duplicated or inherited from it) is closed, or if the [`unlock`](https://doc.rust-lang.org/stable/std/fs/struct.File.html#method.unlock "method std::fs::File::unlock") method is called.

##### [§](#platform-specific-behavior-4)Platform-specific behavior

This function currently corresponds to the `flock` function on Unix with the `LOCK_SH` and `LOCK_NB` flags, and the `LockFileEx` function on Windows with the `LOCKFILE_FAIL_IMMEDIATELY` flag. Note that, this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

On Windows, locking a file will fail if the file is opened only for append. To lock a file, open it with one of `.read(true)`, `.read(true).append(true)`, or `.write(true)`.

##### [§](#examples-12)Examples

```rust
use std::fs::{File, TryLockError};

fn main() -> std::io::Result<()> {
    let f = File::open("foo.txt")?;
    // Explicit handling of the WouldBlock error
    match f.try_lock_shared() {
        Ok(_) => (),
        Err(TryLockError::WouldBlock) => (), // Lock not acquired
        Err(TryLockError::Error(err)) => return Err(err),
    }
    // Alternately, propagate the error as an io::Error
    f.try_lock_shared()?;

    Ok(())
}
```

1.89.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1082-1084)

Release all locks on the file.

All locks are released when the file (along with any other file descriptors/handles duplicated or inherited from it) is closed. This method allows releasing locks without closing the file.

If no lock is currently held via this file descriptor/handle, this method may return an error, or may return successfully without taking any action.

##### [§](#platform-specific-behavior-5)Platform-specific behavior

This function currently corresponds to the `flock` function on Unix with the `LOCK_UN` flag, and the `UnlockFile` function on Windows. Note that, this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

On Windows, locking a file will fail if the file is opened only for append. To lock a file, open it with one of `.read(true)`, `.read(true).append(true)`, or `.write(true)`.

##### [§](#examples-13)Examples

```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    let f = File::open("foo.txt")?;
    f.lock()?;
    f.unlock()?;
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1120-1122)

Truncates or extends the underlying file, updating the size of this file to become `size`.

If the `size` is less than the current file’s size, then the file will be shrunk. If it is greater than the current file’s size, then the file will be extended to `size` and have all of the intermediate data filled in with 0s.

The file’s cursor isn’t changed. In particular, if the cursor was at the end and the file is shrunk using this operation, the cursor will now be past the end.

##### [§](#errors-2)Errors

This function will return an error if the file is not opened for writing. Also, [`std::io::ErrorKind::InvalidInput`](https://doc.rust-lang.org/stable/std/io/enum.ErrorKind.html#variant.InvalidInput "variant std::io::ErrorKind::InvalidInput") will be returned if the desired length would cause an overflow due to the implementation specifics.

##### [§](#examples-14)Examples

```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    let mut f = File::create("foo.txt")?;
    f.set_len(10)?;
    Ok(())
}
```

Note that this method alters the content of the underlying file, even though it takes `&self` rather than `&mut self`.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1138-1140)

Queries metadata about the underlying file.

##### [§](#examples-15)Examples

```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let metadata = f.metadata()?;
    Ok(())
}
```

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1182-1184)

Creates a new `File` instance that shares the same underlying file handle as the existing `File` instance. Reads, writes, and seeks will affect both `File` instances simultaneously.

##### [§](#examples-16)Examples

Creates two handles for a file named `foo.txt`:

```rust
use std::fs::File;

fn main() -> std::io::Result<()> {
    let mut file = File::open("foo.txt")?;
    let file_copy = file.try_clone()?;
    Ok(())
}
```

Assuming there’s a file named `foo.txt` with contents `abcdef\n`, create two handles, seek one of them, and read the remaining bytes from the other handle:

```rust
use std::fs::File;
use std::io::SeekFrom;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut file = File::open("foo.txt")?;
    let mut file_copy = file.try_clone()?;

    file.seek(SeekFrom::Start(3))?;

    let mut contents = vec![];
    file_copy.read_to_end(&mut contents)?;
    assert_eq!(contents, b"def\n");
    Ok(())
}
```

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1220-1222)

Changes the permissions on the underlying file.

##### [§](#platform-specific-behavior-6)Platform-specific behavior

This function currently corresponds to the `fchmod` function on Unix and the `SetFileInformationByHandle` function on Windows. Note that, this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

##### [§](#errors-3)Errors

This function will return an error if the user lacks permission change attributes on the underlying file. It may also return an error in other os-specific unspecified cases.

##### [§](#examples-17)Examples

```rust
fn main() -> std::io::Result<()> {
    use std::fs::File;

    let file = File::open("foo.txt")?;
    let mut perms = file.metadata()?.permissions();
    perms.set_readonly(true);
    file.set_permissions(perms)?;
    Ok(())
}
```

Note that this method alters the permissions of the underlying file, even though it takes `&self` rather than `&mut self`.

1.75.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1266-1268)

Changes the timestamps of the underlying file.

##### [§](#platform-specific-behavior-7)Platform-specific behavior

This function currently corresponds to the `futimens` function on Unix (falling back to `futimes` on macOS before 10.13) and the `SetFileTime` function on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

On most platforms, including UNIX and Windows platforms, this function can also change the timestamps of a directory. To get a `File` representing a directory in order to call `set_times`, open the directory with `File::open` without attempting to obtain write permission.

##### [§](#errors-4)Errors

This function will return an error if the user lacks permission to change timestamps on the underlying file. It may also return an error in other os-specific unspecified cases.

This function may return an error if the operating system lacks support to change one or more of the timestamps set in the `FileTimes` structure.

##### [§](#examples-18)Examples

```rust
fn main() -> std::io::Result<()> {
    use std::fs::{self, File, FileTimes};

    let src = fs::metadata("src")?;
    let dest = File::open("dest")?;
    let times = FileTimes::new()
        .set_accessed(src.accessed()?)
        .set_modified(src.modified()?);
    dest.set_times(times)?;
    Ok(())
}
```

1.75.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1275-1277)

Changes the modification time of the underlying file.

This is an alias for `set_times(FileTimes::new().set_modified(time))`.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#318-323)[§](#impl-AsFd-for-File)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#523-528)[§](#impl-AsHandle-for-File)

Available on **Windows** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/raw.rs.html#172-177)[§](#impl-AsRawFd-for-File)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#94-99)[§](#impl-AsRawHandle-for-File)

Available on **Windows** only.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1304-1308)[§](#impl-Debug-for-File)

1.15.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#349-365)[§](#impl-FileExt-for-File)

Available on **Unix** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#350-352)[§](#method.read_at)

Reads a number of bytes starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#tymethod.read_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#353-355)[§](#method.read_buf_at)

🔬This is a nightly-only experimental API. (`read_buf_at` [#140771](https://github.com/rust-lang/rust/issues/140771))

Reads some bytes starting from a given offset into the buffer. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#method.read_buf_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#356-358)[§](#method.read_vectored_at)

🔬This is a nightly-only experimental API. (`unix_file_vectored_at` [#89517](https://github.com/rust-lang/rust/issues/89517))

Like `read_at`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#method.read_vectored_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#359-361)[§](#method.write_at)

Writes a number of bytes starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#tymethod.write_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#362-364)[§](#method.write_vectored_at)

🔬This is a nightly-only experimental API. (`unix_file_vectored_at` [#89517](https://github.com/rust-lang/rust/issues/89517))

Like `write_at`, except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#method.write_vectored_at)

1.33.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#118-132)[§](#method.read_exact_at)

Reads the exact number of bytes required to fill `buf` from the given offset. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#method.read_exact_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#202-217)[§](#method.read_buf_exact_at)

🔬This is a nightly-only experimental API. (`read_buf_at` [#140771](https://github.com/rust-lang/rust/issues/140771))

Reads the exact number of bytes required to fill the buffer from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#method.read_buf_exact_at)

1.33.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/fs.rs.html#330-345)[§](#method.write_all_at)

Attempts to write an entire buffer starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/unix/fs/trait.FileExt.html#method.write_all_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#226-304)[§](#impl-FileExt-for-File-1)

Available on **WASI** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#227-229)[§](#method.read_at-1)

🔬This is a nightly-only experimental API. (`wasi_ext` [#71213](https://github.com/rust-lang/rust/issues/71213))

Reads a number of bytes starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/wasi/fs/trait.FileExt.html#tymethod.read_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#231-233)[§](#method.read_buf_at-1)

🔬This is a nightly-only experimental API. (`wasi_ext` [#71213](https://github.com/rust-lang/rust/issues/71213))

Reads some bytes starting from a given offset into the buffer. [Read more](https://doc.rust-lang.org/stable/std/os/wasi/fs/trait.FileExt.html#tymethod.read_buf_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#235-237)[§](#method.read_vectored_at-1)

🔬This is a nightly-only experimental API. (`wasi_ext` [#71213](https://github.com/rust-lang/rust/issues/71213))

Reads a number of bytes starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/wasi/fs/trait.FileExt.html#tymethod.read_vectored_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#239-241)[§](#method.write_at-1)

🔬This is a nightly-only experimental API. (`wasi_ext` [#71213](https://github.com/rust-lang/rust/issues/71213))

Writes a number of bytes starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/wasi/fs/trait.FileExt.html#tymethod.write_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#243-245)[§](#method.write_vectored_at-1)

🔬This is a nightly-only experimental API. (`wasi_ext` [#71213](https://github.com/rust-lang/rust/issues/71213))

Writes a number of bytes starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/wasi/fs/trait.FileExt.html#tymethod.write_vectored_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#84-98)[§](#method.read_exact_at-1)

🔬This is a nightly-only experimental API. (`wasi_ext` [#71213](https://github.com/rust-lang/rust/issues/71213))

Reads the exact number of byte required to fill `buf` from the given offset. [Read more](https://doc.rust-lang.org/stable/std/os/wasi/fs/trait.FileExt.html#method.read_exact_at)

[Source](https://doc.rust-lang.org/stable/src/std/os/wasi/fs.rs.html#152-167)[§](#method.write_all_at-1)

🔬This is a nightly-only experimental API. (`wasi_ext` [#71213](https://github.com/rust-lang/rust/issues/71213))

Attempts to write an entire buffer starting from a given offset. [Read more](https://doc.rust-lang.org/stable/std/os/wasi/fs/trait.FileExt.html#method.write_all_at)

1.15.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/fs.rs.html#126-138)[§](#impl-FileExt-for-File-2)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/fs.rs.html#127-129)[§](#method.seek_read)

Seeks to a given position and reads a number of bytes. [Read more](https://doc.rust-lang.org/stable/std/os/windows/fs/trait.FileExt.html#tymethod.seek_read)

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/fs.rs.html#131-133)[§](#method.seek_read_buf)

🔬This is a nightly-only experimental API. (`read_buf_at` [#140771](https://github.com/rust-lang/rust/issues/140771))

Seeks to a given position and reads some bytes into the buffer. [Read more](https://doc.rust-lang.org/stable/std/os/windows/fs/trait.FileExt.html#method.seek_read_buf)

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/fs.rs.html#135-137)[§](#method.seek_write)

Seeks to a given position and writes a number of bytes. [Read more](https://doc.rust-lang.org/stable/std/os/windows/fs/trait.FileExt.html#tymethod.seek_write)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#327-333)[§](#impl-From%3CFile%3E-for-OwnedFd)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#330-332)[§](#method.from-2)

Takes ownership of a [`File`](https://doc.rust-lang.org/stable/std/fs/struct.File.html "struct std::fs::File")’s underlying file descriptor.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#531-537)[§](#impl-From%3CFile%3E-for-OwnedHandle)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#534-536)[§](#method.from)

Takes ownership of a [`File`](https://doc.rust-lang.org/stable/std/fs/struct.File.html "struct std::fs::File")’s underlying file handle.

1.20.0 · [Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#1683-1707)[§](#impl-From%3CFile%3E-for-Stdio)

[Source](https://doc.rust-lang.org/stable/src/std/process.rs.html#1704-1706)[§](#method.from-4)

Converts a [`File`](https://doc.rust-lang.org/stable/std/fs/struct.File.html "struct std::fs::File") into a [`Stdio`](https://doc.rust-lang.org/stable/std/process/struct.Stdio.html "struct std::process::Stdio").

##### [§](#examples-19)Examples

`File` will be converted to `Stdio` using `Stdio::from` under the hood.

```rust
use std::fs::File;
use std::process::Command;

// With the `foo.txt` file containing "Hello, world!"
let file = File::open("foo.txt")?;

let reverse = Command::new("rev")
    .stdin(file)  // Implicit File conversion into a Stdio
    .output()?;

assert_eq!(reverse.stdout, b"!dlrow ,olleH");
```

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#337-344)[§](#impl-From%3COwnedFd%3E-for-File)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#341-343)[§](#method.from-3)

Returns a [`File`](https://doc.rust-lang.org/stable/std/fs/struct.File.html "struct std::fs::File") that takes ownership of the given file descriptor.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#540-546)[§](#impl-From%3COwnedHandle%3E-for-File)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#543-545)[§](#method.from-1)

Returns a [`File`](https://doc.rust-lang.org/stable/std/fs/struct.File.html "struct std::fs::File") that takes ownership of the given handle.

1.1.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/raw.rs.html#180-185)[§](#impl-FromRawFd-for-File)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/raw.rs.html#182-184)[§](#method.from_raw_fd)

Constructs a new instance of `Self` from the given raw file descriptor. [Read more](https://doc.rust-lang.org/stable/std/os/fd/trait.FromRawFd.html#tymethod.from_raw_fd)

1.1.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#156-166)[§](#impl-FromRawHandle-for-File)

Available on **Windows** only.

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/raw.rs.html#188-193)[§](#impl-IntoRawFd-for-File)

Available on **(Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`) and non-`target_os=trusty`** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/fd/raw.rs.html#190-192)[§](#method.into_raw_fd)

Consumes this object, returning the raw underlying file descriptor. [Read more](https://doc.rust-lang.org/stable/std/os/fd/trait.IntoRawFd.html#tymethod.into_raw_fd)

1.4.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/raw.rs.html#169-174)[§](#impl-IntoRawHandle-for-File)

Available on **Windows** only.

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-File)

[Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#method.is_terminal)

Returns `true` if the descriptor/handle refers to a terminal/tty. [Read more](https://doc.rust-lang.org/stable/std/io/trait.IsTerminal.html#tymethod.is_terminal)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1320-1386)[§](#impl-Read-for-%26File)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1333-1335)[§](#method.read)

Reads some bytes from the file.

See [`Read::read`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") docs for more info.

##### [§](#platform-specific-behavior-8)Platform-specific behavior

This function currently corresponds to the `read` function on Unix and the `NtReadFile` function on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1349-1351)[§](#method.read_vectored)

Like `read`, except that it reads into a slice of buffers.

See [`Read::read_vectored`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_vectored "method std::io::Read::read_vectored") docs for more info.

##### [§](#platform-specific-behavior-9)Platform-specific behavior

This function currently corresponds to the `readv` function on Unix and falls back to the `read` implementation on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1369-1371)[§](#method.is_read_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if `File` has an efficient `read_vectored` implementation.

See [`Read::is_read_vectored`](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.is_read_vectored "method std::io::Read::is_read_vectored") docs for more info.

##### [§](#platform-specific-behavior-10)Platform-specific behavior

This function currently returns `true` on Unix and `false` on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1354-1356)[§](#method.read_buf)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1374-1378)[§](#method.read_to_end)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1381-1385)[§](#method.read_to_string)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_string)

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1044-1046)[§](#method.read_exact)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1080-1082)[§](#method.read_buf_exact)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf_exact)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1200-1205)[§](#method.chain)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1239-1244)[§](#method.take)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_array)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1492-1512)[§](#impl-Read-for-File)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1493-1495)[§](#method.read-1)

Pull some bytes from this source into the specified buffer, returning how many bytes were read. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#tymethod.read)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1496-1498)[§](#method.read_vectored-1)

Like `read`, except that it reads into a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1499-1501)[§](#method.read_buf-1)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1503-1505)[§](#method.is_read_vectored-1)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.is_read_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1506-1508)[§](#method.read_to_end-1)

Reads all bytes until EOF in this source, placing them into `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_end)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1509-1511)[§](#method.read_to_string-1)

Reads all bytes until EOF in this source, appending them to `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_to_string)

1.6.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1044-1046)[§](#method.read_exact-1)

Reads the exact number of bytes required to fill `buf`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_exact)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1080-1082)[§](#method.read_buf_exact-1)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_buf_exact)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1119-1124)[§](#method.by_ref-2)

Creates a “by reference” adapter for this instance of `Read`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1162-1167)[§](#method.bytes-1)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/stable/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.bytes)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1200-1205)[§](#method.chain-1)

Creates an adapter which will chain this stream with another. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.chain)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1239-1244)[§](#method.take-1)

Creates an adapter which will read at most `limit` bytes from it. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.take)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1274-1284)[§](#method.read_array-1)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Read.html#method.read_array)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1452-1489)[§](#impl-Seek-for-%26File)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1464-1466)[§](#method.seek)

Seek to an offset, in bytes in a file.

See [`Seek::seek`](https://doc.rust-lang.org/stable/std/io/trait.Seek.html#tymethod.seek "method std::io::Seek::seek") docs for more info.

##### [§](#platform-specific-behavior-15)Platform-specific behavior

This function currently corresponds to the `lseek64` function on Unix and the `SetFilePointerEx` function on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1479-1484)[§](#method.stream_len)

🔬This is a nightly-only experimental API. (`seek_stream_len` [#59359](https://github.com/rust-lang/rust/issues/59359))

Returns the length of this file (in bytes).

See [`Seek::stream_len`](https://doc.rust-lang.org/stable/std/io/trait.Seek.html#method.stream_len "method std::io::Seek::stream_len") docs for more info.

##### [§](#platform-specific-behavior-16)Platform-specific behavior

This function currently corresponds to the `statx` function on Linux (with fallbacks) and the `GetFileSizeEx` function on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1486-1488)[§](#method.stream_position)

Returns the current seek position from the start of the stream. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Seek.html#method.stream_position)

1.55.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2104-2107)[§](#method.rewind)

Rewind to the beginning of a stream. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Seek.html#method.rewind)

1.80.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2200-2203)[§](#method.seek_relative)

Seeks relative to the current position. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Seek.html#method.seek_relative)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1531-1541)[§](#impl-Seek-for-File)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1388-1450)[§](#impl-Write-for-%26File)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1400-1402)[§](#method.write)

Writes some bytes to the file.

See [`Write::write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write") docs for more info.

##### [§](#platform-specific-behavior-11)Platform-specific behavior

This function currently corresponds to the `write` function on Unix and the `NtWriteFile` function on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1415-1417)[§](#method.write_vectored)

Like `write`, except that it writes into a slice of buffers.

See [`Write::write_vectored`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_vectored "method std::io::Write::write_vectored") docs for more info.

##### [§](#platform-specific-behavior-12)Platform-specific behavior

This function currently corresponds to the `writev` function on Unix and falls back to the `write` implementation on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1430-1432)[§](#method.is_write_vectored)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if `File` has an efficient `write_vectored` implementation.

See [`Write::is_write_vectored`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.is_write_vectored "method std::io::Write::is_write_vectored") docs for more info.

##### [§](#platform-specific-behavior-13)Platform-specific behavior

This function currently returns `true` on Unix and `false` on Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1447-1449)[§](#method.flush)

Flushes the file, ensuring that all intermediately buffered contents reach their destination.

See [`Write::flush`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.flush "method std::io::Write::flush") docs for more info.

##### [§](#platform-specific-behavior-14)Platform-specific behavior

Since a `File` structure doesn’t contain any buffers, this function is currently a no-op on Unix and Windows. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1875-1887)[§](#method.write_all)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1937-1952)[§](#method.write_all_vectored)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-1)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.by_ref)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1514-1529)[§](#impl-Write-for-File)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1515-1517)[§](#method.write-1)

Writes a buffer into this writer, returning how many bytes were written. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1518-1520)[§](#method.write_vectored-1)

Like [`write`](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.write "method std::io::Write::write"), except that it writes from a slice of buffers. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_vectored)

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1522-1524)[§](#method.is_write_vectored-1)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

[Source](https://doc.rust-lang.org/stable/src/std/fs.rs.html#1526-1528)[§](#method.flush-1)

Flushes this output stream, ensuring that all intermediately buffered contents reach their destination. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#tymethod.flush)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1875-1887)[§](#method.write_all-1)

Attempts to write an entire buffer into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all)

[Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1937-1952)[§](#method.write_all_vectored-1)

🔬This is a nightly-only experimental API. (`write_all_vectored` [#70436](https://github.com/rust-lang/rust/issues/70436))

Attempts to write multiple buffers into this writer. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_all_vectored)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#1990-1996)[§](#method.write_fmt-1)

Writes a formatted string into this writer, returning any error encountered. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.write_fmt)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/mod.rs.html#2020-2025)[§](#method.by_ref-3)

Creates a “by reference” adapter for this instance of `Write`. [Read more](https://doc.rust-lang.org/stable/std/io/trait.Write.html#method.by_ref)

[§](#impl-Freeze-for-File)

[§](#impl-RefUnwindSafe-for-File)

[§](#impl-Send-for-File)

[§](#impl-Sync-for-File)

[§](#impl-Unpin-for-File)

[§](#impl-UnsafeUnpin-for-File)

[§](#impl-UnwindSafe-for-File)