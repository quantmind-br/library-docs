---
title: Send in std::marker - Rust
url: https://doc.rust-lang.org/stable/std/marker/trait.Send.html
source: crawler
fetched_at: 2026-05-06T21:25:24.139731445-03:00
rendered_js: false
word_count: 97
summary: This document defines the Send marker trait in Rust, which specifies types that can be safely transferred between threads.
tags:
    - rust
    - concurrency
    - thread-safety
    - marker-traits
    - memory-safety
category: reference
---

## Trait Send

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/core/marker.rs.html#95)

```rust
pub unsafe auto trait Send { }
```

Expand description

Types that can be transferred across thread boundaries.

This trait is automatically implemented when the compiler determines it’s appropriate.

An example of a non-`Send` type is the reference-counting pointer [`rc::Rc`](https://doc.rust-lang.org/stable/std/rc/struct.Rc.html). If two threads attempt to clone [`Rc`](https://doc.rust-lang.org/stable/std/rc/struct.Rc.html)s that point to the same reference-counted value, they might try to update the reference count at the same time, which is [undefined behavior](https://doc.rust-lang.org/stable/reference/behavior-considered-undefined.html) because [`Rc`](https://doc.rust-lang.org/stable/std/rc/struct.Rc.html) doesn’t use atomic operations. Its cousin [`sync::Arc`](https://doc.rust-lang.org/stable/std/sync/struct.Arc.html) does use atomic operations (incurring some overhead) and thus is `Send`.

See [the Nomicon](https://doc.rust-lang.org/stable/nomicon/send-and-sync.html) and the [`Sync`](https://doc.rust-lang.org/stable/std/marker/trait.Sync.html "trait std::marker::Sync") trait for more details.