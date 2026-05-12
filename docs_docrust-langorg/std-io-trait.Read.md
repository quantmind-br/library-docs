---
title: Read in std::io - Rust
url: https://doc.rust-lang.org/std/io/trait.Read.html#method.read_array
source: crawler
fetched_at: 2026-05-06T21:24:32.947609016-03:00
rendered_js: false
word_count: 1901
summary: The Read trait provides a standardized interface for byte-oriented input, allowing types to be read from a source via a buffer-based API.
tags:
    - rust
    - io
    - trait
    - byte-streams
    - buffered-input
category: reference
---

## Trait Read

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#732-1285)

```rust
pub trait Read {
Show 13 methods    // Required method
    fn read(&mut self, buf: &mut [u8]) -> Result<usize>;

    // Provided methods
    fn read_vectored(&mut self, bufs: &mut [IoSliceMut<'_>]) -> Result<usize> { ... }
    fn is_read_vectored(&self) -> bool { ... }
    fn read_to_end(&mut self, buf: &mut Vec<u8>) -> Result<usize> { ... }
    fn read_to_string(&mut self, buf: &mut String) -> Result<usize> { ... }
    fn read_exact(&mut self, buf: &mut [u8]) -> Result<()> { ... }
    fn read_buf(&mut self, buf: BorrowedCursor<'_>) -> Result<()> { ... }
    fn read_buf_exact(&mut self, cursor: BorrowedCursor<'_>) -> Result<()> { ... }
    fn by_ref(&mut self) -> &mut Self
       where Self: Sized { ... }
    fn bytes(self) -> Bytes<Self> ⓘ
       where Self: Sized { ... }
    fn chain<R: Read>(self, next: R) -> Chain<Self, R> ⓘ
       where Self: Sized { ... }
    fn take(self, limit: u64) -> Take<Self> ⓘ
       where Self: Sized { ... }
    fn read_array<const N: usize>(&mut self) -> Result<[u8; N]>
       where Self: Sized { ... }
}
```

Expand description

The `Read` trait allows for reading bytes from a source.

Implementors of the `Read` trait are called ‘readers’.

Readers are defined by one required method, [`read()`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read"). Each call to [`read()`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") will attempt to pull bytes from this source into a provided buffer. A number of other methods are implemented in terms of [`read()`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read"), giving implementors a number of ways to read bytes while only needing to implement a single method.

Readers are intended to be composable with one another. Many implementors throughout [`std::io`](https://doc.rust-lang.org/std/io/index.html "mod std::io") take and provide types which implement the `Read` trait.

Please note that each call to [`read()`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") may involve a system call, and therefore, using something that implements [`BufRead`](https://doc.rust-lang.org/std/io/trait.BufRead.html "trait std::io::BufRead"), such as [`BufReader`](https://doc.rust-lang.org/std/io/struct.BufReader.html "struct std::io::BufReader"), will be more efficient.

Repeated calls to the reader use the same cursor, so for example calling `read_to_end` twice on a [`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File") will only return the file’s contents once. It’s recommended to first call `rewind()` in that case.

## [§](#examples)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let mut buffer = [0; 10];

    // read up to 10 bytes
    f.read(&mut buffer)?;

    let mut buffer = Vec::new();
    // read the whole file
    f.read_to_end(&mut buffer)?;

    // read into a String, so that you don't need to do the conversion.
    let mut buffer = String::new();
    f.read_to_string(&mut buffer)?;

    // and more! See the other methods for more details.
    Ok(())
}
```

Read from [`&str`](https://doc.rust-lang.org/std/primitive.str.html "primitive str") because [`&[u8]`](https://doc.rust-lang.org/std/primitive.slice.html "primitive slice") implements `Read`:

```rust
use std::io::prelude::*;

fn main() -> io::Result<()> {
    let mut b = "This string will be read".as_bytes();
    let mut buffer = [0; 10];

    // read up to 10 bytes
    b.read(&mut buffer)?;

    // etc... it works exactly as a File does!
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#813)

Pull some bytes from this source into the specified buffer, returning how many bytes were read.

This function does not provide any guarantees about whether it blocks waiting for data, but if an object needs to block for a read and cannot, it will typically signal this via an [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") return value.

If the return value of this method is [`Ok(n)`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok"), then implementations must guarantee that `0 <= n <= buf.len()`. A nonzero `n` value indicates that the buffer `buf` has been filled in with `n` bytes of data from this source. If `n` is `0`, then it can indicate one of two scenarios:

1. This reader has reached its “end of file” and will likely no longer be able to produce bytes. Note that this does not mean that the reader will *always* no longer be able to produce bytes. As an example, on Linux, this method will call the `recv` syscall for a [`TcpStream`](https://doc.rust-lang.org/std/net/struct.TcpStream.html "struct std::net::TcpStream"), where returning zero indicates the connection was shut down correctly. While for [`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File"), it is possible to reach the end of file and get zero as result, but if more data is appended to the file, future calls to `read` will return more data.
2. The buffer specified was 0 bytes in length.

It is not an error if the returned value `n` is smaller than the buffer size, even when the reader is not at the end of the stream yet. This may happen for example because fewer bytes are actually available right now (e. g. being close to end-of-file) or because read() was interrupted by a signal.

As this trait is safe to implement, callers in unsafe code cannot rely on `n <= buf.len()` for safety. Extra care needs to be taken when `unsafe` functions are used to access the read bytes. Callers have to ensure that no unchecked out-of-bounds accesses are possible even if `n > buf.len()`.

*Implementations* of this method can make no assumptions about the contents of `buf` when this function is called. It is recommended that implementations only write data to `buf` instead of reading its contents.

Correspondingly, however, *callers* of this method in unsafe code must not assume any guarantees about how the implementation uses `buf`. The trait is safe to implement, so it is possible that the code that’s supposed to write to the buffer might also read from it. It is your responsibility to make sure that `buf` is initialized before calling `read`. Calling `read` with an uninitialized `buf` (of the kind one obtains via [`MaybeUninit<T>`](https://doc.rust-lang.org/std/mem/union.MaybeUninit.html "union std::mem::MaybeUninit")) is not safe, and can lead to undefined behavior.

##### [§](#errors)Errors

If this function encounters any form of I/O or other error, an error variant will be returned. If an error is returned then it must be guaranteed that no bytes were read.

An error of the [`ErrorKind::Interrupted`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.Interrupted "variant std::io::ErrorKind::Interrupted") kind is non-fatal and the read operation should be retried if there is nothing else to do.

##### [§](#examples-1)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let mut buffer = [0; 10];

    // read up to 10 bytes
    let n = f.read(&mut buffer[..])?;

    println!("The bytes: {:?}", &buffer[..n]);
    Ok(())
}
```

1.36.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#825-827)

Like `read`, except that it reads into a slice of buffers.

Data is copied to fill each buffer in order, with the final buffer written to possibly being only partially filled. This method must behave equivalently to a single call to `read` with concatenated buffers.

The default implementation calls `read` with either the first nonempty buffer provided, or an empty one if none exists.

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#838-840)

🔬This is a nightly-only experimental API. (`can_vector` [#69941](https://github.com/rust-lang/rust/issues/69941))

Determines if this `Read`er has an efficient `read_vectored` implementation.

If a `Read`er does not override the default `read_vectored` implementation, code using it may want to avoid the method all together and coalesce writes into a single buffer for higher performance.

The default implementation returns `false`.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#935-937)

Reads all bytes until EOF in this source, placing them into `buf`.

All bytes read from this source will be appended to the specified buffer `buf`. This function will continuously call [`read()`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") to append more data to `buf` until [`read()`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") returns either [`Ok(0)`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") or an error of non-[`ErrorKind::Interrupted`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.Interrupted "variant std::io::ErrorKind::Interrupted") kind.

If successful, this function will return the total number of bytes read.

##### [§](#errors-1)Errors

If this function encounters an error of the kind [`ErrorKind::Interrupted`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.Interrupted "variant std::io::ErrorKind::Interrupted") then the error is ignored and the operation will continue.

If any other read error is encountered then this function immediately returns. Any bytes which have already been read will be appended to `buf`.

##### [§](#examples-2)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let mut buffer = Vec::new();

    // read the whole file
    f.read_to_end(&mut buffer)?;
    Ok(())
}
```

(See also the [`std::fs::read`](https://doc.rust-lang.org/std/fs/fn.read.html "fn std::fs::read") convenience function for reading from a file.)

###### [§](#implementing-read_to_end)Implementing `read_to_end`

When implementing the `io::Read` trait, it is recommended to allocate memory using [`Vec::try_reserve`](https://doc.rust-lang.org/std/vec/struct.Vec.html#method.try_reserve "method std::vec::Vec::try_reserve"). However, this behavior is not guaranteed by all implementations, and `read_to_end` may not handle out-of-memory situations gracefully.

```rust
fn read_to_end(&mut self, dest_vec: &mut Vec<u8>) -> io::Result<usize> {
    let initial_vec_len = dest_vec.len();
    loop {
        let src_buf = self.example_datasource.fill_buf()?;
        if src_buf.is_empty() {
            break;
        }
        dest_vec.try_reserve(src_buf.len())?;
        dest_vec.extend_from_slice(src_buf);

        // Any irreversible side effects should happen after `try_reserve` succeeds,
        // to avoid losing data on allocation error.
        let read = src_buf.len();
        self.example_datasource.consume(read);
    }
    Ok(dest_vec.len() - initial_vec_len)
}
```

##### [§](#usage-notes)Usage Notes

`read_to_end` attempts to read a source until EOF, but many sources are continuous streams that do not send EOF. In these cases, `read_to_end` will block indefinitely. Standard input is one such stream which may be finite if piped, but is typically continuous. For example, `cat file | my-rust-program` will correctly terminate with an `EOF` upon closure of cat. Reading user input or running programs that remain open indefinitely will never terminate the stream with `EOF` (e.g. `yes | my-rust-program`).

Using `.lines()` with a [`BufReader`](https://doc.rust-lang.org/std/io/struct.BufReader.html "struct std::io::BufReader") or using [`read`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") can provide a better solution

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#991-993)

Reads all bytes until EOF in this source, appending them to `buf`.

If successful, this function returns the number of bytes which were read and appended to `buf`.

##### [§](#errors-2)Errors

If the data in this stream is *not* valid UTF-8 then an error is returned and `buf` is unchanged.

See [`read_to_end`](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_to_end "method std::io::Read::read_to_end") for other error semantics.

##### [§](#examples-3)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let mut buffer = String::new();

    f.read_to_string(&mut buffer)?;
    Ok(())
}
```

(See also the [`std::fs::read_to_string`](https://doc.rust-lang.org/std/fs/fn.read_to_string.html "fn std::fs::read_to_string") convenience function for reading from a file.)

##### [§](#usage-notes-1)Usage Notes

`read_to_string` attempts to read a source until EOF, but many sources are continuous streams that do not send EOF. In these cases, `read_to_string` will block indefinitely. Standard input is one such stream which may be finite if piped, but is typically continuous. For example, `cat file | my-rust-program` will correctly terminate with an `EOF` upon closure of cat. Reading user input or running programs that remain open indefinitely will never terminate the stream with `EOF` (e.g. `yes | my-rust-program`).

Using `.lines()` with a [`BufReader`](https://doc.rust-lang.org/std/io/struct.BufReader.html "struct std::io::BufReader") or using [`read`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") can provide a better solution

1.6.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1044-1046)

Reads the exact number of bytes required to fill `buf`.

This function reads as many bytes as necessary to completely fill the specified buffer `buf`.

*Implementations* of this method can make no assumptions about the contents of `buf` when this function is called. It is recommended that implementations only write data to `buf` instead of reading its contents. The documentation on [`read`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") has a more detailed explanation of this subject.

##### [§](#errors-3)Errors

If this function encounters an error of the kind [`ErrorKind::Interrupted`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.Interrupted "variant std::io::ErrorKind::Interrupted") then the error is ignored and the operation will continue.

If this function encounters an “end of file” before completely filling the buffer, it returns an error of the kind [`ErrorKind::UnexpectedEof`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.UnexpectedEof "variant std::io::ErrorKind::UnexpectedEof"). The contents of `buf` are unspecified in this case.

If any other read error is encountered then this function immediately returns. The contents of `buf` are unspecified in this case.

If this function returns an error, it is unspecified how many bytes it has read, but it will never read more than would be necessary to completely fill the buffer.

##### [§](#examples-4)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let mut buffer = [0; 10];

    // read exactly 10 bytes
    f.read_exact(&mut buffer)?;
    Ok(())
}
```

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1057-1059)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Pull some bytes from this source into the specified buffer.

This is equivalent to the [`read`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") method, except that it is passed a [`BorrowedCursor`](https://doc.rust-lang.org/std/io/struct.BorrowedCursor.html "struct std::io::BorrowedCursor") rather than `[u8]` to allow use with uninitialized buffers. The new data will be appended to any existing contents of `buf`.

The default implementation delegates to `read`.

This method makes it possible to return both data and an error but it is advised against.

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1080-1082)

🔬This is a nightly-only experimental API. (`read_buf` [#78485](https://github.com/rust-lang/rust/issues/78485))

Reads the exact number of bytes required to fill `cursor`.

This is similar to the [`read_exact`](https://doc.rust-lang.org/std/io/trait.Read.html#method.read_exact "method std::io::Read::read_exact") method, except that it is passed a [`BorrowedCursor`](https://doc.rust-lang.org/std/io/struct.BorrowedCursor.html "struct std::io::BorrowedCursor") rather than `[u8]` to allow use with uninitialized buffers.

##### [§](#errors-4)Errors

If this function encounters an error of the kind [`ErrorKind::Interrupted`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.Interrupted "variant std::io::ErrorKind::Interrupted") then the error is ignored and the operation will continue.

If this function encounters an “end of file” before completely filling the buffer, it returns an error of the kind [`ErrorKind::UnexpectedEof`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.UnexpectedEof "variant std::io::ErrorKind::UnexpectedEof").

If any other read error is encountered then this function immediately returns.

If this function returns an error, all bytes read will be appended to `cursor`.

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1119-1124)

Creates a “by reference” adapter for this instance of `Read`.

The returned adapter also implements `Read` and will simply borrow this current reader.

##### [§](#examples-5)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::Read;
use std::fs::File;

fn main() -> io::Result<()> {
    let mut f = File::open("foo.txt")?;
    let mut buffer = Vec::new();
    let mut other_buffer = Vec::new();

    {
        let reference = f.by_ref();

        // read at most 5 bytes
        reference.take(5).read_to_end(&mut buffer)?;

    } // drop our &mut reference so we can use f again

    // original file still usable, read the rest
    f.read_to_end(&mut other_buffer)?;
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1162-1167)

Transforms this `Read` instance to an [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") over its bytes.

The returned type implements [`Iterator`](https://doc.rust-lang.org/std/iter/trait.Iterator.html "trait std::iter::Iterator") where the [`Item`](https://doc.rust-lang.org/std/iter/trait.Iterator.html#associatedtype.Item "associated type std::iter::Iterator::Item") is `Result<u8, io::Error>`. The yielded item is [`Ok`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok") if a byte was successfully read and [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") otherwise. EOF is mapped to returning [`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None "variant std::option::Option::None") from this iterator.

The default implementation calls `read` for each byte, which can be very inefficient for data that’s not in memory, such as [`File`](https://doc.rust-lang.org/std/fs/struct.File.html "fs::File"). Consider using a [`BufReader`](https://doc.rust-lang.org/std/io/struct.BufReader.html "struct std::io::BufReader") in such cases.

##### [§](#examples-6)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::io::BufReader;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = BufReader::new(File::open("foo.txt")?);

    for byte in f.bytes() {
        println!("{}", byte?);
    }
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1200-1205)

Creates an adapter which will chain this stream with another.

The returned `Read` instance will first read all bytes from this object until EOF is encountered. Afterwards the output is equivalent to the output of `next`.

##### [§](#examples-7)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let f1 = File::open("foo.txt")?;
    let f2 = File::open("bar.txt")?;

    let mut handle = f1.chain(f2);
    let mut buffer = String::new();

    // read the value into a String. We could use any Read method here,
    // this is just one example.
    handle.read_to_string(&mut buffer)?;
    Ok(())
}
```

1.0.0 · [Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1239-1244)

Creates an adapter which will read at most `limit` bytes from it.

This function returns a new instance of `Read` which will read at most `limit` bytes, after which it will always return EOF ([`Ok(0)`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Ok "variant std::result::Result::Ok")). Any read errors will not count towards the number of bytes read and future calls to [`read()`](https://doc.rust-lang.org/std/io/trait.Read.html#tymethod.read "method std::io::Read::read") may succeed.

##### [§](#examples-8)Examples

[`File`](https://doc.rust-lang.org/std/fs/struct.File.html "struct std::fs::File")s implement `Read`:

```rust
use std::io;
use std::io::prelude::*;
use std::fs::File;

fn main() -> io::Result<()> {
    let f = File::open("foo.txt")?;
    let mut buffer = [0; 5];

    // read at most five bytes
    let mut handle = f.take(5);

    handle.read(&mut buffer)?;
    Ok(())
}
```

[Source](https://doc.rust-lang.org/src/std/io/mod.rs.html#1274-1284)

🔬This is a nightly-only experimental API. (`read_array` [#148848](https://github.com/rust-lang/rust/issues/148848))

Read and return a fixed array of bytes from this source.

This function uses an array sized based on a const generic size known at compile time. You can specify the size with turbofish (`reader.read_array::<8>()`), or let type inference determine the number of bytes needed based on how the return value gets used. For instance, this function works well with functions like [`u64::from_le_bytes`](https://doc.rust-lang.org/std/primitive.u64.html#method.from_le_bytes "associated function u64::from_le_bytes") to turn an array of bytes into an integer of the same size.

Like `read_exact`, if this function encounters an “end of file” before reading the desired number of bytes, it returns an error of the kind [`ErrorKind::UnexpectedEof`](https://doc.rust-lang.org/std/io/enum.ErrorKind.html#variant.UnexpectedEof "variant std::io::ErrorKind::UnexpectedEof").

```rust
#![feature(read_array)]
use std::io::Cursor;
use std::io::prelude::*;

fn main() -> std::io::Result<()> {
    let mut buf = Cursor::new([1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2]);
    let x = u64::from_le_bytes(buf.read_array()?);
    let y = u32::from_be_bytes(buf.read_array()?);
    let z = u16::from_be_bytes(buf.read_array()?);
    assert_eq!(x, 0x807060504030201);
    assert_eq!(y, 0x9080706);
    assert_eq!(z, 0x504);
    Ok(())
}
```