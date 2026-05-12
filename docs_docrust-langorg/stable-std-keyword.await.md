---
title: await - Rust
url: https://doc.rust-lang.org/stable/std/keyword.await.html
source: crawler
fetched_at: 2026-05-06T21:28:48.284310398-03:00
rendered_js: false
word_count: 64
summary: This document explains the functionality of the await keyword in Rust, which suspends function execution until an asynchronous future has completed.
tags:
    - rust
    - async-await
    - concurrency
    - future-trait
    - language-features
category: concept
---

Expand description

Suspend execution until the result of a [`Future`](https://doc.rust-lang.org/stable/std/future/trait.Future.html "trait std::future::Future") is ready.

`.await`ing a future will suspend the current function’s execution until the executor has run the future to completion.

Read the [async book](https://rust-lang.github.io/async-book/) for details on how [`async`](https://doc.rust-lang.org/stable/std/keyword.async.html)/`await` and executors work.

### [§](#editions)Editions

`await` is a keyword from the 2018 edition onwards.

It is available for use in stable Rust from version 1.39 onwards.