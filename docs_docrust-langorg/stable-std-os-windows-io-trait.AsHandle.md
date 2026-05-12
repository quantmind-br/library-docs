---
title: AsHandle in std::os::windows::io - Rust
url: https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html
source: crawler
fetched_at: 2026-05-06T21:31:15.755964568-03:00
rendered_js: false
word_count: 181
summary: This document lists the implementations of the AsHandle trait for various types within the Rust standard library on Windows, enabling safe access to underlying system handles.
tags:
    - rust
    - windows-api
    - system-handles
    - trait-implementation
    - standard-library
category: reference
---

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#523-528)[§](#impl-AsHandle-for-File)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [File](https://doc.rust-lang.org/stable/std/fs/struct.File.html "struct std::fs::File")

1.87.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#664-668)[§](#impl-AsHandle-for-PipeReader)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [PipeReader](https://doc.rust-lang.org/stable/std/io/struct.PipeReader.html "struct std::io::PipeReader")

1.87.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#678-682)[§](#impl-AsHandle-for-PipeWriter)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [PipeWriter](https://doc.rust-lang.org/stable/std/io/struct.PipeWriter.html "struct std::io::PipeWriter")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#581-586)[§](#impl-AsHandle-for-Stderr)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [Stderr](https://doc.rust-lang.org/stable/std/io/struct.Stderr.html "struct std::io::Stderr")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#549-554)[§](#impl-AsHandle-for-Stdin)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [Stdin](https://doc.rust-lang.org/stable/std/io/struct.Stdin.html "struct std::io::Stdin")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#565-570)[§](#impl-AsHandle-for-Stdout)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [Stdout](https://doc.rust-lang.org/stable/std/io/struct.Stdout.html "struct std::io::Stdout")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/process.rs.html#45-50)[§](#impl-AsHandle-for-Child)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [Child](https://doc.rust-lang.org/stable/std/process/struct.Child.html "struct std::process::Child")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#631-636)[§](#impl-AsHandle-for-ChildStderr)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [ChildStderr](https://doc.rust-lang.org/stable/std/process/struct.ChildStderr.html "struct std::process::ChildStderr")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#597-602)[§](#impl-AsHandle-for-ChildStdin)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [ChildStdin](https://doc.rust-lang.org/stable/std/process/struct.ChildStdin.html "struct std::process::ChildStdin")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#614-619)[§](#impl-AsHandle-for-ChildStdout)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [ChildStdout](https://doc.rust-lang.org/stable/std/process/struct.ChildStdout.html "struct std::process::ChildStdout")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#504-509)[§](#impl-AsHandle-for-BorrowedHandle%3C'_%3E)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [BorrowedHandle](https://doc.rust-lang.org/stable/std/os/windows/io/struct.BorrowedHandle.html "struct std::os::windows::io::BorrowedHandle")&lt;'\_&gt;

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#512-520)[§](#impl-AsHandle-for-OwnedHandle)

### impl [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [OwnedHandle](https://doc.rust-lang.org/stable/std/os/windows/io/struct.OwnedHandle.html "struct std::os::windows::io::OwnedHandle")

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#589-594)[§](#impl-AsHandle-for-StderrLock%3C'a%3E)

### impl&lt;'a&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [StderrLock](https://doc.rust-lang.org/stable/std/io/struct.StderrLock.html "struct std::io::StderrLock")&lt;'a&gt;

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#557-562)[§](#impl-AsHandle-for-StdinLock%3C'a%3E)

### impl&lt;'a&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [StdinLock](https://doc.rust-lang.org/stable/std/io/struct.StdinLock.html "struct std::io::StdinLock")&lt;'a&gt;

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#573-578)[§](#impl-AsHandle-for-StdoutLock%3C'a%3E)

### impl&lt;'a&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [StdoutLock](https://doc.rust-lang.org/stable/std/io/struct.StdoutLock.html "struct std::io::StdoutLock")&lt;'a&gt;

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#648-653)[§](#impl-AsHandle-for-JoinHandle%3CT%3E)

### impl&lt;T&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [JoinHandle](https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html "struct std::thread::JoinHandle")&lt;T&gt;

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#444-449)[§](#impl-AsHandle-for-%26T)

### impl&lt;T: [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") + ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized")&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [&T](https://doc.rust-lang.org/stable/std/primitive.reference.html)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#452-457)[§](#impl-AsHandle-for-%26mut+T)

### impl&lt;T: [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") + ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized")&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [&mut T](https://doc.rust-lang.org/stable/std/primitive.reference.html)

1.71.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#496-501)[§](#impl-AsHandle-for-Box%3CT%3E)

### impl&lt;T: [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") + ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized")&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [Box](https://doc.rust-lang.org/stable/std/boxed/struct.Box.html "struct std::boxed::Box")&lt;T&gt;

1.71.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#480-485)[§](#impl-AsHandle-for-Rc%3CT%3E)

### impl&lt;T: [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") + ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized")&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [Rc](https://doc.rust-lang.org/stable/std/rc/struct.Rc.html "struct std::rc::Rc")&lt;T&gt;

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#488-493)[§](#impl-AsHandle-for-UniqueRc%3CT%3E)

### impl&lt;T: [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") + ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized")&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [UniqueRc](https://doc.rust-lang.org/stable/std/rc/struct.UniqueRc.html "struct std::rc::UniqueRc")&lt;T&gt;

1.71.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#472-477)[§](#impl-AsHandle-for-Arc%3CT%3E)

### impl&lt;T: [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") + ?[Sized](https://doc.rust-lang.org/stable/std/marker/trait.Sized.html "trait std::marker::Sized")&gt; [AsHandle](https://doc.rust-lang.org/stable/std/os/windows/io/trait.AsHandle.html "trait std::os::windows::io::AsHandle") for [Arc](https://doc.rust-lang.org/stable/std/sync/struct.Arc.html "struct std::sync::Arc")&lt;T&gt;

This impl allows implementing traits that require `AsHandle` on Arc.

```rust
use std::fs::File;
use std::sync::Arc;

trait MyTrait: AsHandle {}
impl MyTrait for Arc<File> {}
impl MyTrait for Box<File> {}
```