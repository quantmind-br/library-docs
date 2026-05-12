---
title: Builder in std::thread - Rust
url: https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.spawn
source: crawler
fetched_at: 2026-05-06T21:22:01.793001147-03:00
rendered_js: false
word_count: 711
summary: The Builder struct provides a configurable interface for creating new threads in Rust, allowing developers to specify thread names and stack sizes while handling potential thread creation errors.
tags:
    - rust
    - threading
    - concurrency
    - thread-builder
    - stack-size
    - os-threads
category: api
---

## Struct Builder

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#49-56)

```rust
pub struct Builder { /* private fields */ }
```

Expand description

Thread factory, which can be used in order to configure the properties of a new thread.

Methods can be chained on it in order to configure it.

The two configurations available are:

- [`name`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.name "method std::thread::Builder::name"): specifies an [associated name for the thread](https://doc.rust-lang.org/stable/std/thread/index.html#naming-threads)
- [`stack_size`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.stack_size "method std::thread::Builder::stack_size"): specifies the [desired stack size for the thread](https://doc.rust-lang.org/stable/std/thread/index.html#stack-size)

The [`spawn`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.spawn "method std::thread::Builder::spawn") method will take ownership of the builder and create an [`io::Result`](https://doc.rust-lang.org/stable/std/io/type.Result.html "type std::io::Result") to the thread handle with the given configuration.

The [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn") free function uses a `Builder` with default configuration and [`unwrap`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap "method std::result::Result::unwrap")s its return value.

You may want to use [`spawn`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.spawn "method std::thread::Builder::spawn") instead of [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn"), when you want to recover from a failure to launch a thread, indeed the free function will panic where the `Builder` method will return a [`io::Result`](https://doc.rust-lang.org/stable/std/io/type.Result.html "type std::io::Result").

## [§](#examples)Examples

```rust
use std::thread;

let builder = thread::Builder::new();

let handler = builder.spawn(|| {
    // thread code
}).unwrap();

handler.join().unwrap();
```

[Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#58-263)[§](#impl-Builder)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#78-80)

Generates the base configuration for spawning a thread, from which configuration methods can be chained.

##### [§](#examples-1)Examples

```rust
use std::thread;

let builder = thread::Builder::new()
                              .name("foo".into())
                              .stack_size(32 * 1024);

let handler = builder.spawn(|| {
    // thread code
}).unwrap();

handler.join().unwrap();
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#107-110)

Names the thread-to-be. Currently the name is used for identification only in panic messages.

The name must not contain null bytes (`\0`).

For more information about named threads, see [this module-level documentation](https://doc.rust-lang.org/stable/std/thread/index.html#naming-threads).

##### [§](#examples-2)Examples

```rust
use std::thread;

let builder = thread::Builder::new()
    .name("foo".into());

let handler = builder.spawn(|| {
    assert_eq!(thread::current().name(), Some("foo"))
}).unwrap();

handler.join().unwrap();
```

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#130-133)

Sets the size of the stack (in bytes) for the new thread.

The actual stack size may be greater than this value if the platform specifies a minimal stack size.

For more information about the stack size for threads, see [this module-level documentation](https://doc.rust-lang.org/stable/std/thread/index.html#stack-size).

##### [§](#examples-3)Examples

```rust
use std::thread;

let builder = thread::Builder::new().stack_size(32 * 1024);
```

[Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#142-145)

🔬This is a nightly-only experimental API. (`thread_spawn_hook` [#132951](https://github.com/rust-lang/rust/issues/132951))

Disables running and inheriting [spawn hooks](https://doc.rust-lang.org/stable/std/thread/fn.add_spawn_hook.html "fn std::thread::add_spawn_hook").

Use this if the parent thread is in no way relevant for the child thread. For example, when lazily spawning threads for a thread pool.

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#185-192)

Spawns a new thread by taking ownership of the `Builder`, and returns an [`io::Result`](https://doc.rust-lang.org/stable/std/io/type.Result.html "type std::io::Result") to its [`JoinHandle`](https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html "struct std::thread::JoinHandle").

The spawned thread may outlive the caller (unless the caller thread is the main thread; the whole process is terminated when the main thread finishes). The join handle can be used to block on termination of the spawned thread, including recovering its panics.

For a more complete documentation see [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn").

##### [§](#errors)Errors

Unlike the [`spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn") free function, this method yields an [`io::Result`](https://doc.rust-lang.org/stable/std/io/type.Result.html "type std::io::Result") to capture any failure to create the thread at the OS level.

##### [§](#panics)Panics

Panics if a thread name was set and it contained null bytes.

##### [§](#examples-4)Examples

```rust
use std::thread;

let builder = thread::Builder::new();

let handler = builder.spawn(|| {
    // thread code
}).unwrap();

handler.join().unwrap();
```

1.82.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/builder.rs.html#254-262)

Spawns a new thread without any lifetime restrictions by taking ownership of the `Builder`, and returns an [`io::Result`](https://doc.rust-lang.org/stable/std/io/type.Result.html "type std::io::Result") to its [`JoinHandle`](https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html "struct std::thread::JoinHandle").

The spawned thread may outlive the caller (unless the caller thread is the main thread; the whole process is terminated when the main thread finishes). The join handle can be used to block on termination of the spawned thread, including recovering its panics.

This method is identical to [`thread::Builder::spawn`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.spawn "method std::thread::Builder::spawn"), except for the relaxed lifetime bounds, which render it unsafe. For a more complete documentation see [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn").

##### [§](#errors-1)Errors

Unlike the [`spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn") free function, this method yields an [`io::Result`](https://doc.rust-lang.org/stable/std/io/type.Result.html "type std::io::Result") to capture any failure to create the thread at the OS level.

##### [§](#panics-1)Panics

Panics if a thread name was set and it contained null bytes.

##### [§](#safety)Safety

The caller has to ensure that the spawned thread does not outlive any references in the supplied thread closure and its return type. This can be guaranteed in two ways:

- ensure that [`join`](https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html#method.join "method std::thread::JoinHandle::join") is called before any referenced data is dropped
- use only types with `'static` lifetime bounds, i.e., those with no or only `'static` references (both [`thread::Builder::spawn`](https://doc.rust-lang.org/stable/std/thread/struct.Builder.html#method.spawn "method std::thread::Builder::spawn") and [`thread::spawn`](https://doc.rust-lang.org/stable/std/thread/fn.spawn.html "fn std::thread::spawn") enforce this property statically)

##### [§](#examples-5)Examples

```rust
use std::thread;

let builder = thread::Builder::new();

let x = 1;
let thread_x = &x;

let handler = unsafe {
    builder.spawn_unchecked(move || {
        println!("x = {}", *thread_x);
    }).unwrap()
};

// caller has to ensure `join()` is called, otherwise
// it is possible to access freed memory if `x` gets
// dropped before the thread closure is executed!
handler.join().unwrap();
```

[Source](https://doc.rust-lang.org/stable/src/std/thread/scoped.rs.html#210-270)[§](#impl-Builder-1)

1.63.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/scoped.rs.html#256-269)

Spawns a new scoped thread using the settings set through this `Builder`.

Unlike [`Scope::spawn`](https://doc.rust-lang.org/stable/std/thread/struct.Scope.html#method.spawn "method std::thread::Scope::spawn"), this method yields an [`io::Result`](https://doc.rust-lang.org/stable/std/io/type.Result.html "type std::io::Result") to capture any failure to create the thread at the OS level.

##### [§](#panics-2)Panics

Panics if a thread name was set and it contained null bytes.

##### [§](#example)Example

```rust
use std::thread;

let mut a = vec![1, 2, 3];
let mut x = 0;

thread::scope(|s| {
    thread::Builder::new()
        .name("first".to_string())
        .spawn_scoped(s, ||
    {
        println!("hello from the {:?} scoped thread", thread::current().name());
        // We can borrow `a` here.
        dbg!(&a);
    })
    .unwrap();
    thread::Builder::new()
        .name("second".to_string())
        .spawn_scoped(s, ||
    {
        println!("hello from the {:?} scoped thread", thread::current().name());
        // We can even mutably borrow `x` here,
        // because no other threads are using it.
        x += a[0] + a[2];
    })
    .unwrap();
    println!("hello from the main thread");
});

// After the scope, we can modify and access our variables again:
a.push(4);
assert_eq!(x, a.len());
```

[§](#impl-Freeze-for-Builder)

[§](#impl-RefUnwindSafe-for-Builder)

[§](#impl-Send-for-Builder)

[§](#impl-Sync-for-Builder)

[§](#impl-Unpin-for-Builder)

[§](#impl-UnsafeUnpin-for-Builder)

[§](#impl-UnwindSafe-for-Builder)