---
title: Scope in std::thread - Rust
url: https://doc.rust-lang.org/std/thread/struct.Scope.html
source: crawler
fetched_at: 2026-05-06T21:25:21.324261093-03:00
rendered_js: false
word_count: 167
summary: The Scope struct provides a mechanism for spawning threads that can borrow non-static data from the surrounding environment by ensuring they complete before the scope ends.
tags:
    - rust
    - concurrency
    - scoped-threads
    - multi-threading
    - memory-safety
category: reference
---

## Struct Scope

1.63.0 · [Source](https://doc.rust-lang.org/src/std/thread/scoped.rs.html#16-33)

```rust
pub struct Scope<'scope, 'env: 'scope> { /* private fields */ }
```

Expand description

A scope to spawn scoped threads in.

See [`scope`](https://doc.rust-lang.org/std/thread/fn.scope.html "fn std::thread::scope") for details.

[Source](https://doc.rust-lang.org/src/std/thread/scoped.rs.html#176-208)[§](#impl-Scope%3C'scope,+'env%3E)

1.63.0 · [Source](https://doc.rust-lang.org/src/std/thread/scoped.rs.html#201-207)

Spawns a new thread within a scope, returning a [`ScopedJoinHandle`](https://doc.rust-lang.org/std/thread/struct.ScopedJoinHandle.html "struct std::thread::ScopedJoinHandle") for it.

Unlike non-scoped threads, threads spawned with this function may borrow non-`'static` data from the outside the scope. See [`scope`](https://doc.rust-lang.org/std/thread/fn.scope.html "fn std::thread::scope") for details.

The join handle provides a [`join`](https://doc.rust-lang.org/std/thread/struct.ScopedJoinHandle.html#method.join "method std::thread::ScopedJoinHandle::join") method that can be used to join the spawned thread. If the spawned thread panics, [`join`](https://doc.rust-lang.org/std/thread/struct.ScopedJoinHandle.html#method.join "method std::thread::ScopedJoinHandle::join") will return an [`Err`](https://doc.rust-lang.org/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") containing the panic payload.

If the join handle is dropped, the spawned thread will be implicitly joined at the end of the scope. In that case, if the spawned thread panics, [`scope`](https://doc.rust-lang.org/std/thread/fn.scope.html "fn std::thread::scope") will panic after all threads are joined.

This function creates a thread with the default parameters of [`Builder`](https://doc.rust-lang.org/std/thread/struct.Builder.html "struct std::thread::Builder"). To specify the new thread’s stack size or the name, use [`Builder::spawn_scoped`](https://doc.rust-lang.org/std/thread/struct.Builder.html#method.spawn_scoped "method std::thread::Builder::spawn_scoped").

##### [§](#panics)Panics

Panics if the OS fails to create a thread; use [`Builder::spawn_scoped`](https://doc.rust-lang.org/std/thread/struct.Builder.html#method.spawn_scoped "method std::thread::Builder::spawn_scoped") to recover from such errors.

[§](#impl-Freeze-for-Scope%3C'scope,+'env%3E)

[§](#impl-RefUnwindSafe-for-Scope%3C'scope,+'env%3E)

[§](#impl-Send-for-Scope%3C'scope,+'env%3E)

[§](#impl-Sync-for-Scope%3C'scope,+'env%3E)

[§](#impl-Unpin-for-Scope%3C'scope,+'env%3E)

[§](#impl-UnsafeUnpin-for-Scope%3C'scope,+'env%3E)

[§](#impl-UnwindSafe-for-Scope%3C'scope,+'env%3E)