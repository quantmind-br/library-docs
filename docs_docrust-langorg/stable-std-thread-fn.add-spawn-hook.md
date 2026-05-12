---
title: add_spawn_hook in std::thread - Rust
url: https://doc.rust-lang.org/stable/std/thread/fn.add_spawn_hook.html
source: crawler
fetched_at: 2026-05-06T21:26:50.58393016-03:00
rendered_js: false
word_count: 137
summary: This document describes the add_spawn_hook experimental API, which allows developers to register hooks that execute in both parent and newly spawned threads.
tags:
    - rust-api
    - thread-management
    - spawn-hooks
    - concurrency
    - experimental-api
    - thread-local-storage
category: api
---

## Function add\_spawn\_hook

[Source](https://doc.rust-lang.org/stable/src/std/thread/spawnhook.rs.html#92-106)

```rust
pub fn add_spawn_hook<F, G>(hook: F)
where
    F: 'static + Send + Sync + Fn(&Thread) -> G,
    G: 'static + Send + FnOnce(),
```

🔬This is a nightly-only experimental API. (`thread_spawn_hook` [#132951](https://github.com/rust-lang/rust/issues/132951))

Expand description

Registers a function to run for every newly thread spawned.

The hook is executed in the parent thread, and returns a function that will be executed in the new thread.

The hook is called with the `Thread` handle for the new thread.

The hook will only be added for the current thread and is inherited by the threads it spawns. In other words, adding a hook has no effect on already running threads (other than the current thread) and the threads they might spawn in the future.

Hooks can only be added, not removed.

The hooks will run in reverse order, starting with the most recently added.

## [§](#usage)Usage

```rust
#![feature(thread_spawn_hook)]

std::thread::add_spawn_hook(|_| {
    ..; // This will run in the parent (spawning) thread.
    move || {
        ..; // This will run it the child (spawned) thread.
    }
});
```

## [§](#example)Example

A spawn hook can be used to “inherit” a thread local from the parent thread:

```rust
#![feature(thread_spawn_hook)]

use std::cell::Cell;

thread_local! {
    static X: Cell<u32> = Cell::new(0);
}

// This needs to be done once in the main thread before spawning any threads.
std::thread::add_spawn_hook(|_| {
    // Get the value of X in the spawning thread.
    let value = X.get();
    // Set the value of X in the newly spawned thread.
    move || X.set(value)
});

X.set(123);

std::thread::spawn(|| {
    assert_eq!(X.get(), 123);
}).join().unwrap();
```