---
title: async - Rust
url: https://doc.rust-lang.org/stable/std/keyword.async.html
source: crawler
fetched_at: 2026-05-06T21:28:49.041414282-03:00
rendered_js: false
word_count: 212
summary: This document explains the usage of async/await syntax in Rust, detailing how asynchronous blocks generate futures and describing the specific control flow behavior within these blocks.
tags:
    - rust-programming
    - async-await
    - concurrency
    - asynchronous-programming
    - futures
    - control-flow
category: concept
---

Expand description

Returns a [`Future`](https://doc.rust-lang.org/stable/std/future/trait.Future.html "trait std::future::Future") instead of blocking the current thread.

Use `async` in front of `fn`, `closure`, or a `block` to turn the marked code into a `Future`. As such the code will not be run immediately, but will only be evaluated when the returned future is [`.await`](https://doc.rust-lang.org/stable/std/keyword.await.html)ed.

We have written an [async book](https://rust-lang.github.io/async-book/) detailing `async`/`await` and trade-offs compared to using threads.

### [§](#control-flow)Control Flow

[`return`](https://doc.rust-lang.org/stable/std/keyword.return.html) statements and [`?`](https://doc.rust-lang.org/stable/reference/expressions/operator-expr.html#r-expr.try) operators within `async` blocks do not cause a return from the parent function; rather, they cause the `Future` returned by the block to return with that value.

For example, the following Rust function will return `5`, causing `x` to take the [`!` type](https://doc.rust-lang.org/stable/reference/types/never.html):

```rust
#[expect(unused_variables)]
fn example() -> i32 {
    let x = {
        return 5;
    };
}
```

In contrast, the following asynchronous function assigns a `Future<Output = i32>` to `x`, and only returns `5` when `x` is `.await`ed:

```rust
async fn example() -> i32 {
    let x = async {
        return 5;
    };

    x.await
}
```

Code using `?` behaves similarly - it causes the `async` block to return a [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") without affecting the parent function.

Note that you cannot use `break` or `continue` from within an `async` block to affect the control flow of a loop in the parent function.

Control flow in `async` blocks is documented further in the [async book](https://rust-lang.github.io/async-book/part-guide/more-async-await.html#async-blocks).

### [§](#editions)Editions

`async` is a keyword from the 2018 edition onwards.

It is available for use in stable Rust from version 1.39 onwards.