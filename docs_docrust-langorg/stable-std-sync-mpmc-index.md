---
title: std::sync::mpmc - Rust
url: https://doc.rust-lang.org/stable/std/sync/mpmc/index.html
source: crawler
fetched_at: 2026-05-06T21:28:13.317467285-03:00
rendered_js: false
word_count: 373
summary: This module provides multi-producer, multi-consumer FIFO channel primitives for message-based communication between threads, supporting both asynchronous unbounded and synchronous bounded configurations.
tags:
    - rust
    - concurrency
    - mpmc
    - channels
    - message-passing
    - synchronization
category: reference
---

🔬This is a nightly-only experimental API. (`mpmc_channel` [#126840](https://github.com/rust-lang/rust/issues/126840))

Expand description

Multi-producer, multi-consumer FIFO queue communication primitives.

This module provides message-based communication over channels, concretely defined by two types:

- [`Sender`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Sender.html "struct std::sync::mpmc::Sender")
- [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver")

[`Sender`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Sender.html "struct std::sync::mpmc::Sender")s are used to send data to a set of [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver")s where each item sent is delivered to (at most) one receiver. Both sender and receiver are cloneable (multi-producer) such that many threads can send simultaneously to receivers (multi-consumer).

These channels come in two flavors:

1. An asynchronous, infinitely buffered channel. The [`channel`](https://doc.rust-lang.org/stable/std/sync/mpmc/fn.channel.html "fn std::sync::mpmc::channel") function will return a `(Sender, Receiver)` tuple where all sends will be **asynchronous** (they never block). The channel conceptually has an infinite buffer.
2. A synchronous, bounded channel. The [`sync_channel`](https://doc.rust-lang.org/stable/std/sync/mpmc/fn.sync_channel.html "fn std::sync::mpmc::sync_channel") function will return a `(Sender, Receiver)` tuple where the storage for pending messages is a pre-allocated buffer of a fixed size. All sends will be **synchronous** by blocking until there is buffer space available. Note that a bound of 0 is allowed, causing the channel to become a “rendezvous” channel where each sender atomically hands off a message to a receiver.

### [§](#disconnection)Disconnection

The send and receive operations on channels will all return a [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") indicating whether the operation succeeded or not. An unsuccessful operation is normally indicative of the other half of a channel having “hung up” by being dropped in its corresponding thread.

Once half of a channel has been deallocated, most operations can no longer continue to make progress, so [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") will be returned. Many applications will continue to [`unwrap`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap "method std::result::Result::unwrap") the results returned from this module, instigating a propagation of failure among threads if one unexpectedly dies.

## [§](#examples)Examples

Simple usage:

```rust
#![feature(mpmc_channel)]

use std::thread;
use std::sync::mpmc::channel;

// Create a simple streaming channel
let (tx, rx) = channel();
thread::spawn(move || {
    tx.send(10).unwrap();
});
assert_eq!(rx.recv().unwrap(), 10);
```

Shared usage:

```rust
#![feature(mpmc_channel)]

use std::thread;
use std::sync::mpmc::channel;

thread::scope(|s| {
    // Create a shared channel that can be sent along from many threads
    // where tx is the sending half (tx for transmission), and rx is the receiving
    // half (rx for receiving).
    let (tx, rx) = channel();
    for i in 0..10 {
        let tx = tx.clone();
        s.spawn(move || {
            tx.send(i).unwrap();
        });
    }

    for _ in 0..5 {
        let rx1 = rx.clone();
        let rx2 = rx.clone();
        s.spawn(move || {
            let j = rx1.recv().unwrap();
            assert!(0 <= j && j < 10);
        });
        s.spawn(move || {
            let j = rx2.recv().unwrap();
            assert!(0 <= j && j < 10);
        });
    }
})
```

Propagating panics:

```rust
#![feature(mpmc_channel)]

use std::sync::mpmc::channel;

// The call to recv() will return an error because the channel has already
// hung up (or been deallocated)
let (tx, rx) = channel::<i32>();
drop(tx);
assert!(rx.recv().is_err());
```

`pub use crate::sync::mpsc::RecvError;`

`pub use crate::sync::mpsc::RecvTimeoutError;`

`pub use crate::sync::mpsc::SendError;`

`pub use crate::sync::mpsc::TryRecvError;`

`pub use crate::sync::mpsc::TrySendError;`

[IntoIter](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.IntoIter.html "struct std::sync::mpmc::IntoIter")Experimental

An owning iterator over messages on a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver"), created by [`into_iter`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html#method.into_iter "method std::sync::mpmc::Receiver::into_iter").

[Iter](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Iter.html "struct std::sync::mpmc::Iter")Experimental

An iterator over messages on a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver"), created by [`iter`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html#method.iter "method std::sync::mpmc::Receiver::iter").

[Receiver](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver")Experimental

The receiving half of Rust’s [`channel`](https://doc.rust-lang.org/stable/std/sync/mpmc/fn.channel.html "fn std::sync::mpmc::channel") (or [`sync_channel`](https://doc.rust-lang.org/stable/std/sync/mpmc/fn.sync_channel.html "fn std::sync::mpmc::sync_channel")) type. Different threads can share this [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver") by cloning it.

[Sender](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Sender.html "struct std::sync::mpmc::Sender")Experimental

The sending-half of Rust’s synchronous [`channel`](https://doc.rust-lang.org/stable/std/sync/mpmc/fn.channel.html "fn std::sync::mpmc::channel") type.

[TryIter](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.TryIter.html "struct std::sync::mpmc::TryIter")Experimental

An iterator that attempts to yield all pending values for a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html "struct std::sync::mpmc::Receiver"), created by [`try_iter`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Receiver.html#method.try_iter "method std::sync::mpmc::Receiver::try_iter").

[SendTimeoutError](https://doc.rust-lang.org/stable/std/sync/mpmc/enum.SendTimeoutError.html "enum std::sync::mpmc::SendTimeoutError")Experimental

An error returned from the [`send_timeout`](https://doc.rust-lang.org/stable/std/sync/mpmc/struct.Sender.html#method.send_timeout "method std::sync::mpmc::Sender::send_timeout") method.

[channel](https://doc.rust-lang.org/stable/std/sync/mpmc/fn.channel.html "fn std::sync::mpmc::channel")Experimental

Creates a new asynchronous channel, returning the sender/receiver halves.

[sync\_channel](https://doc.rust-lang.org/stable/std/sync/mpmc/fn.sync_channel.html "fn std::sync::mpmc::sync_channel")Experimental

Creates a new synchronous, bounded channel.