---
title: std::future - Rust
url: https://doc.rust-lang.org/stable/std/future/index.html
source: crawler
fetched_at: 2026-05-06T21:25:42.30792707-03:00
rendered_js: false
word_count: 136
summary: This document provides the reference documentation for the Rust standard library's future module, covering the core traits, functions, and types used to implement asynchronous computations.
tags:
    - rust-programming
    - asynchronous-programming
    - futures
    - concurrency
    - async-await
category: reference
---

## Module future

1.36.0 · [Source](https://doc.rust-lang.org/stable/src/core/lib.rs.html#325)

Expand description

Asynchronous basic functionality.

Please see the fundamental [`async`](https://doc.rust-lang.org/stable/std/keyword.async.html) and [`await`](https://doc.rust-lang.org/stable/std/keyword.await.html) keywords and the [async book](https://rust-lang.github.io/async-book/) for more information on asynchronous programming in Rust.

[join](https://doc.rust-lang.org/stable/std/future/macro.join.html "macro std::future::join")Experimental

Polls multiple futures simultaneously, returning a tuple of all results once complete.

[Pending](https://doc.rust-lang.org/stable/std/future/struct.Pending.html "struct std::future::Pending")

Creates a future which never resolves, representing a computation that never finishes.

[PollFn](https://doc.rust-lang.org/stable/std/future/struct.PollFn.html "struct std::future::PollFn")

A Future that wraps a function returning [`Poll`](https://doc.rust-lang.org/stable/std/task/enum.Poll.html "enum std::task::Poll").

[Ready](https://doc.rust-lang.org/stable/std/future/struct.Ready.html "struct std::future::Ready")

A future that is immediately ready with a value.

[Future](https://doc.rust-lang.org/stable/std/future/trait.Future.html "trait std::future::Future")

A future represents an asynchronous computation, commonly obtained by use of [`async`](https://doc.rust-lang.org/stable/std/keyword.async.html).

[IntoFuture](https://doc.rust-lang.org/stable/std/future/trait.IntoFuture.html "trait std::future::IntoFuture")

Conversion into a `Future`.

[AsyncDrop](https://doc.rust-lang.org/stable/std/future/trait.AsyncDrop.html "trait std::future::AsyncDrop")Experimental

Async version of Drop trait.

[pending](https://doc.rust-lang.org/stable/std/future/fn.pending.html "fn std::future::pending")

Creates a future which never resolves, representing a computation that never finishes.

[poll\_fn](https://doc.rust-lang.org/stable/std/future/fn.poll_fn.html "fn std::future::poll_fn")

Creates a future that wraps a function returning [`Poll`](https://doc.rust-lang.org/stable/std/task/enum.Poll.html "enum std::task::Poll").

[ready](https://doc.rust-lang.org/stable/std/future/fn.ready.html "fn std::future::ready")

Creates a future that is immediately ready with a value.

[async\_drop\_in\_place](https://doc.rust-lang.org/stable/std/future/fn.async_drop_in_place.html "fn std::future::async_drop_in_place")⚠Experimental

Async drop.