---
title: JoinHandle in std::thread - Rust
url: https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html
source: crawler
fetched_at: 2026-05-06T21:26:50.611068303-03:00
rendered_js: false
word_count: 465
summary: The JoinHandle struct provides a mechanism to join a spawned thread, allowing the main thread to wait for its completion or detach it entirely.
tags:
    - rust
    - threading
    - concurrency
    - join-handle
    - asynchronous-programming
    - thread-management
category: reference
---

## Struct JoinHandle

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#71)

```rust
pub struct JoinHandle<T>(/* private fields */);
```

Expand description

An owned permission to join on a thread (block on its termination).

A `JoinHandle` *detaches* the associated thread when it is dropped, which means that there is no longer any handle to the thread and no way to `join` on it.

Due to platform restrictions, it is not possible to [`Clone`](https://doc.rust-lang.org/stable/std/clone/trait.Clone.html "trait std::clone::Clone") this handle: the ability to join a thread is a uniquely-owned permission.

This `struct` is created by the [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn") function and the [`thread::Builder::spawn`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.spawn "method std::thread::Builder::spawn") method.

## [§](#examples)Examples

Creation from [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn"):

```rust
use std::thread;

let join_handle: thread::JoinHandle<_> = thread::spawn(|| {
    // some work here
});
```

Creation from [`thread::Builder::spawn`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.spawn "method std::thread::Builder::spawn"):

```rust
use std::thread;

let builder = thread::Builder::new();

let join_handle: thread::JoinHandle<_> = builder.spawn(|| {
    // some work here
}).unwrap();
```

A thread being detached and outliving the thread that spawned it:

```rust
use std::thread;
use std::time::Duration;

let original_thread = thread::spawn(|| {
    let _detached_thread = thread::spawn(|| {
        // Here we sleep to make sure that the first thread returns before.
        thread::sleep(Duration::from_millis(10));
        // This will be called, even though the JoinHandle is dropped.
        println!("♫ Still alive ♫");
    });
});

original_thread.join().expect("The thread being joined has panicked");
println!("Original thread is joined.");

// We make sure that the new thread has time to run, before the main
// thread returns.

thread::sleep(Duration::from_millis(1000));
```

[Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#78-167)[§](#impl-JoinHandle%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#97-99)

Extracts a handle to the underlying thread.

##### [§](#examples-1)Examples

```rust
use std::thread;

let builder = thread::Builder::new();

let join_handle: thread::JoinHandle<_> = builder.spawn(|| {
    // some work here
}).unwrap();

let thread = join_handle.thread();
println!("thread id: {:?}", thread.id());
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#149-151)

Waits for the associated thread to finish.

This function will return immediately if the associated thread has already finished. Otherwise, it fully waits for the thread to finish, including all destructors for thread-local variables that might be running after the main function of the thread.

In terms of [atomic memory orderings](https://doc.rust-lang.org/stable/std/sync/atomic/index.html "mod std::sync::atomic"), the completion of the associated thread synchronizes with this function returning. In other words, all operations performed by that thread [happen before](https://doc.rust-lang.org/nomicon/atomics.html#data-accesses) all operations that happen after `join` returns.

If the associated thread panics, [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") is returned with the parameter given to [`panic!`](https://doc.rust-lang.org/stable/std/macro.panic.html "macro std::panic") (though see the Notes below).

##### [§](#panics)Panics

This function may panic on some platforms if a thread attempts to join itself or otherwise may create a deadlock with joining threads.

##### [§](#examples-2)Examples

```rust
use std::thread;

let builder = thread::Builder::new();

let join_handle: thread::JoinHandle<_> = builder.spawn(|| {
    // some work here
}).unwrap();
join_handle.join().expect("Couldn't join on the associated thread");
```

##### [§](#notes)Notes

If a “foreign” unwinding operation (e.g. an exception thrown from C++ code, or a `panic!` in Rust code compiled or linked with a different runtime) unwinds all the way to the thread root, the process may be aborted; see the Notes on [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn"). If the process is not aborted, this function will return a `Result::Err` containing an opaque type.

1.61.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#164-166)

Checks if the associated thread has finished running its main function.

`is_finished` supports implementing a non-blocking join operation, by checking `is_finished`, and calling `join` if it returns `true`. This function does not block. To block while waiting on the thread to finish, use [`join`](https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html#method.join "method std::thread::JoinHandle::join").

This might return `true` for a brief moment after the thread’s main function has returned, but before the thread itself has stopped running. However, once this returns `true`, [`join`](https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html#method.join "method std::thread::JoinHandle::join") can be expected to return quickly, without blocking for any significant amount of time.

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#648-653)[§](#impl-AsHandle-for-JoinHandle%3CT%3E)

Available on **Windows** only.

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/thread.rs.html#12-17)[§](#impl-AsRawHandle-for-JoinHandle%3CT%3E)

Available on **Windows** only.

1.16.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#182-186)[§](#impl-Debug-for-JoinHandle%3CT%3E)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#656-661)[§](#impl-From%3CJoinHandle%3CT%3E%3E-for-OwnedHandle)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#658-660)[§](#method.from)

Converts to this type from the input type.

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/thread.rs.html#20-25)[§](#impl-IntoRawHandle-for-JoinHandle%3CT%3E)

Available on **Windows** only.

1.9.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/unix/thread.rs.html#33-41)[§](#impl-JoinHandleExt-for-JoinHandle%3CT%3E)

Available on **Unix** only.

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/thread.rs.html#34-36)[§](#method.as_pthread_t)

Extracts the raw pthread\_t without taking ownership

[Source](https://doc.rust-lang.org/stable/src/std/os/unix/thread.rs.html#38-40)[§](#method.into_pthread_t)

Consumes the thread, returning the raw pthread\_t [Read more](https://doc.rust-lang.org/stable/std/os/unix/thread/trait.JoinHandleExt.html#tymethod.into_pthread_t)

1.29.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#74)[§](#impl-Send-for-JoinHandle%3CT%3E)

1.29.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/join_handle.rs.html#76)[§](#impl-Sync-for-JoinHandle%3CT%3E)

[§](#impl-Freeze-for-JoinHandle%3CT%3E)

[§](#impl-RefUnwindSafe-for-JoinHandle%3CT%3E)

[§](#impl-Unpin-for-JoinHandle%3CT%3E)

[§](#impl-UnsafeUnpin-for-JoinHandle%3CT%3E)

[§](#impl-UnwindSafe-for-JoinHandle%3CT%3E)