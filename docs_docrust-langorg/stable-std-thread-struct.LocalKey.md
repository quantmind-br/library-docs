---
title: LocalKey in std::thread - Rust
url: https://doc.rust-lang.org/stable/std/thread/struct.LocalKey.html
source: crawler
fetched_at: 2026-05-06T21:28:43.74730961-03:00
rendered_js: false
word_count: 1235
summary: LocalKey provides a mechanism for thread-local storage in Rust, allowing data to be lazily initialized and accessed exclusively within the context of a single thread.
tags:
    - rust
    - thread-local-storage
    - concurrency
    - memory-safety
    - tls
    - synchronization
category: reference
---

## Struct LocalKey

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#115-131)

```rust
pub struct LocalKey<T: 'static> { /* private fields */ }
```

Expand description

A thread local storage (TLS) key which owns its contents.

This key uses the fastest implementation available on the target platform. It is instantiated with the [`thread_local!`](https://doc.rust-lang.org/stable/std/macro.thread_local.html "macro std::thread_local") macro and the primary method is the [`with`](https://doc.rust-lang.org/stable/std/thread/struct.LocalKey.html#method.with "method std::thread::LocalKey::with") method, though there are helpers to make working with [`Cell`](https://doc.rust-lang.org/stable/std/cell/struct.Cell.html "struct std::cell::Cell") types easier.

The [`with`](https://doc.rust-lang.org/stable/std/thread/struct.LocalKey.html#method.with "method std::thread::LocalKey::with") method yields a reference to the contained value which cannot outlive the current thread or escape the given closure.

## [§](#initialization-and-destruction)Initialization and Destruction

Initialization is dynamically performed on the first call to a setter (e.g. [`with`](https://doc.rust-lang.org/stable/std/thread/struct.LocalKey.html#method.with "method std::thread::LocalKey::with")) within a thread, and values that implement [`Drop`](https://doc.rust-lang.org/stable/std/ops/trait.Drop.html "trait std::ops::Drop") get destructed when a thread exits. Some platform-specific caveats apply, which are explained below. Note that, should the destructor panic, the whole process will be [aborted](https://doc.rust-lang.org/stable/std/process/fn.abort.html "fn std::process::abort"). On platforms where initialization requires memory allocation, this is performed directly through [`System`](https://doc.rust-lang.org/stable/std/alloc/struct.System.html "struct std::alloc::System"), allowing the [global allocator](https://doc.rust-lang.org/stable/std/alloc/index.html "mod std::alloc") to make use of thread local storage.

A `LocalKey`’s initializer cannot recursively depend on itself. Using a `LocalKey` in this way may cause panics, aborts, or infinite recursion on the first call to `with`.

## [§](#single-thread-synchronization)Single-thread Synchronization

Though there is no potential race with other threads, it is still possible to obtain multiple references to the thread-local data in different places on the call stack. For this reason, only shared (`&T`) references may be obtained.

To allow obtaining an exclusive mutable reference (`&mut T`), typically a [`Cell`](https://doc.rust-lang.org/stable/std/cell/struct.Cell.html "struct std::cell::Cell") or [`RefCell`](https://doc.rust-lang.org/stable/std/cell/struct.RefCell.html "struct std::cell::RefCell") is used (see the [`std::cell`](https://doc.rust-lang.org/stable/std/cell/index.html "mod std::cell") for more information on how exactly this works). To make this easier there are specialized implementations for [`LocalKey<Cell<T>>`](https://doc.rust-lang.org/stable/std/thread/struct.LocalKey.html#impl-LocalKey%3CCell%3CT%3E%3E) and [`LocalKey<RefCell<T>>`](https://doc.rust-lang.org/stable/std/thread/struct.LocalKey.html#impl-LocalKey%3CRefCell%3CT%3E%3E).

## [§](#examples)Examples

```rust
use std::cell::Cell;
use std::thread;

// explicit `const {}` block enables more efficient initialization
thread_local!(static FOO: Cell<u32> = const { Cell::new(1) });

assert_eq!(FOO.get(), 1);
FOO.set(2);

// each thread starts out with the initial value of 1
let t = thread::spawn(move || {
    assert_eq!(FOO.get(), 1);
    FOO.set(3);
});

// wait for the thread to complete and bail out on panic
t.join().unwrap();

// we retain our original value of 2 despite the child thread
assert_eq!(FOO.get(), 2);
```

## [§](#platform-specific-behavior)Platform-specific behavior

Note that a “best effort” is made to ensure that destructors for types stored in thread local storage are run, but not all platforms can guarantee that destructors will be run for all types in thread local storage. For example, there are a number of known caveats where destructors are not run:

1. On Unix systems when pthread-based TLS is being used, destructors will not be run for TLS values on the main thread when it exits. Note that the application will exit immediately after the main thread exits as well.
2. On all platforms it’s possible for TLS to re-initialize other TLS slots during destruction. Some platforms ensure that this cannot happen infinitely by preventing re-initialization of any slot that has been destroyed, but not all platforms have this guard. Those platforms that do not guard typically have a synthetic limit after which point no more destructors are run.
3. When the process exits on Windows systems, TLS destructors may only be run on the thread that causes the process to exit. This is because the other threads may be forcibly terminated.

### [§](#synchronization-in-thread-local-destructors)Synchronization in thread-local destructors

On Windows, synchronization operations (such as [`JoinHandle::join`](https://doc.rust-lang.org/stable/std/thread/struct.JoinHandle.html#method.join "method std::thread::JoinHandle::join")) in thread local destructors are prone to deadlocks and so should be avoided. This is because the [loader lock](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-best-practices) is held while a destructor is run. The lock is acquired whenever a thread starts or exits or when a DLL is loaded or unloaded. Therefore these events are blocked for as long as a thread local destructor is running.

[Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#438-543)[§](#impl-LocalKey%3CT%3E)

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#473-481)

Acquires a reference to the value in this TLS key.

This will lazily initialize the value if this thread has not referenced this key yet.

##### [§](#panics)Panics

This function will `panic!()` if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-1)Examples

```rust
thread_local! {
    pub static STATIC: String = String::from("I am");
}

assert_eq!(
    STATIC.with(|original_value| format!("{original_value} initialized")),
    "I am initialized",
);
```

1.26.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#508-514)

Acquires a reference to the value in this TLS key.

This will lazily initialize the value if this thread has not referenced this key yet. If the key has been destroyed (which may happen if this is called in a destructor), this function will return an [`AccessError`](https://doc.rust-lang.org/stable/std/thread/struct.AccessError.html "struct std::thread::AccessError").

##### [§](#panics-1)Panics

This function will still `panic!()` if the key is uninitialized and the key’s initializer panics.

##### [§](#examples-2)Examples

```rust
thread_local! {
    pub static STATIC: String = String::from("I am");
}

assert_eq!(
    STATIC.try_with(|original_value| format!("{original_value} initialized")),
    Ok(String::from("I am initialized")),
);
```

[Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#545-693)[§](#impl-LocalKey%3CCell%3CT%3E%3E)

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#573-582)

Sets or initializes the contained value.

Unlike the other methods, this will *not* run the lazy initializer of the thread local. Instead, it will be directly initialized with the given value if it wasn’t initialized yet.

##### [§](#panics-2)Panics

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-3)Examples

```rust
use std::cell::Cell;

thread_local! {
    static X: Cell<i32> = panic!("!");
}

// Calling X.get() here would result in a panic.

X.set(123); // But X.set() is fine, as it skips the initializer above.

assert_eq!(X.get(), 123);
```

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#606-611)

Returns a copy of the contained value.

This will lazily initialize the value if this thread has not referenced this key yet.

##### [§](#panics-3)Panics

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-4)Examples

```rust
use std::cell::Cell;

thread_local! {
    static X: Cell<i32> = const { Cell::new(1) };
}

assert_eq!(X.get(), 1);
```

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#636-641)

Takes the contained value, leaving `Default::default()` in its place.

This will lazily initialize the value if this thread has not referenced this key yet.

##### [§](#panics-4)Panics

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-5)Examples

```rust
use std::cell::Cell;

thread_local! {
    static X: Cell<Option<i32>> = const { Cell::new(Some(1)) };
}

assert_eq!(X.take(), Some(1));
assert_eq!(X.take(), None);
```

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#667-669)

Replaces the contained value, returning the old value.

This will lazily initialize the value if this thread has not referenced this key yet.

##### [§](#panics-5)Panics

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-6)Examples

```rust
use std::cell::Cell;

thread_local! {
    static X: Cell<i32> = const { Cell::new(1) };
}

assert_eq!(X.replace(2), 1);
assert_eq!(X.replace(3), 2);
```

[Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#687-692)

🔬This is a nightly-only experimental API. (`local_key_cell_update` [#143989](https://github.com/rust-lang/rust/issues/143989))

Updates the contained value using a function.

##### [§](#examples-7)Examples

```rust
#![feature(local_key_cell_update)]
use std::cell::Cell;

thread_local! {
    static X: Cell<i32> = const { Cell::new(5) };
}

X.update(|x| x + 1);
assert_eq!(X.get(), 6);
```

[Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#695-865)[§](#impl-LocalKey%3CRefCell%3CT%3E%3E)

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#720-725)

Acquires a reference to the contained value.

This will lazily initialize the value if this thread has not referenced this key yet.

##### [§](#panics-6)Panics

Panics if the value is currently mutably borrowed.

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-8)Examples

```rust
use std::cell::RefCell;

thread_local! {
    static X: RefCell<Vec<i32>> = RefCell::new(Vec::new());
}

X.with_borrow(|v| assert!(v.is_empty()));
```

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#753-758)

Acquires a mutable reference to the contained value.

This will lazily initialize the value if this thread has not referenced this key yet.

##### [§](#panics-7)Panics

Panics if the value is currently borrowed.

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-9)Examples

```rust
use std::cell::RefCell;

thread_local! {
    static X: RefCell<Vec<i32>> = RefCell::new(Vec::new());
}

X.with_borrow_mut(|v| v.push(1));

X.with_borrow(|v| assert_eq!(*v, vec![1]));
```

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#789-798)

Sets or initializes the contained value.

Unlike the other methods, this will *not* run the lazy initializer of the thread local. Instead, it will be directly initialized with the given value if it wasn’t initialized yet.

##### [§](#panics-8)Panics

Panics if the value is currently borrowed.

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-10)Examples

```rust
use std::cell::RefCell;

thread_local! {
    static X: RefCell<Vec<i32>> = panic!("!");
}

// Calling X.with() here would result in a panic.

X.set(vec![1, 2, 3]); // But X.set() is fine, as it skips the initializer above.

X.with_borrow(|v| assert_eq!(*v, vec![1, 2, 3]));
```

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#830-835)

Takes the contained value, leaving `Default::default()` in its place.

This will lazily initialize the value if this thread has not referenced this key yet.

##### [§](#panics-9)Panics

Panics if the value is currently borrowed.

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-11)Examples

```rust
use std::cell::RefCell;

thread_local! {
    static X: RefCell<Vec<i32>> = RefCell::new(Vec::new());
}

X.with_borrow_mut(|v| v.push(1));

let a = X.take();

assert_eq!(a, vec![1]);

X.with_borrow(|v| assert!(v.is_empty()));
```

1.73.0 · [Source](https://doc.rust-lang.org/stable/src/std/thread/local.rs.html#862-864)

Replaces the contained value, returning the old value.

##### [§](#panics-10)Panics

Panics if the value is currently borrowed.

Panics if the key currently has its destructor running, and it **may** panic if the destructor has previously been run for this thread.

##### [§](#examples-12)Examples

```rust
use std::cell::RefCell;

thread_local! {
    static X: RefCell<Vec<i32>> = RefCell::new(Vec::new());
}

let prev = X.replace(vec![1, 2, 3]);
assert!(prev.is_empty());

X.with_borrow(|v| assert_eq!(*v, vec![1, 2, 3]));
```

[§](#impl-Freeze-for-LocalKey%3CT%3E)

[§](#impl-RefUnwindSafe-for-LocalKey%3CT%3E)

[§](#impl-Send-for-LocalKey%3CT%3E)

[§](#impl-Sync-for-LocalKey%3CT%3E)

[§](#impl-Unpin-for-LocalKey%3CT%3E)

[§](#impl-UnsafeUnpin-for-LocalKey%3CT%3E)

[§](#impl-UnwindSafe-for-LocalKey%3CT%3E)