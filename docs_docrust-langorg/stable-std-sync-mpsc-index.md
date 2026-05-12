---
title: std::sync::mpsc - Rust
url: https://doc.rust-lang.org/stable/std/sync/mpsc/index.html
source: crawler
fetched_at: 2026-05-06T21:28:14.610952123-03:00
rendered_js: false
word_count: 512
summary: This module provides multi-producer, single-consumer communication primitives through asynchronous and synchronous channels for message passing between threads.
tags:
    - rust
    - concurrency
    - channels
    - mpsc
    - message-passing
    - multi-threading
category: reference
---

## Module mpsc

1.0.0 · [Source](https://doc.rust-lang.org/stable/src/std/sync/mpsc.rs.html#1-1214)

Expand description

Multi-producer, single-consumer FIFO queue communication primitives.

This module provides message-based communication over channels, concretely defined among three types:

- [`Sender`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Sender.html "struct std::sync::mpsc::Sender")
- [`SyncSender`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.SyncSender.html "struct std::sync::mpsc::SyncSender")
- [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver")

A [`Sender`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Sender.html "struct std::sync::mpsc::Sender") or [`SyncSender`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.SyncSender.html "struct std::sync::mpsc::SyncSender") is used to send data to a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver"). Both senders are clone-able (multi-producer) such that many threads can send simultaneously to one receiver (single-consumer).

These channels come in two flavors:

1. An asynchronous, infinitely buffered channel. The [`channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.channel.html "fn std::sync::mpsc::channel") function will return a `(Sender, Receiver)` tuple where all sends will be **asynchronous** (they never block). The channel conceptually has an infinite buffer.
2. A synchronous, bounded channel. The [`sync_channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.sync_channel.html "fn std::sync::mpsc::sync_channel") function will return a `(SyncSender, Receiver)` tuple where the storage for pending messages is a pre-allocated buffer of a fixed size. All sends will be **synchronous** by blocking until there is buffer space available. Note that a bound of 0 is allowed, causing the channel to become a “rendezvous” channel where each sender atomically hands off a message to a receiver.

### [§](#disconnection)Disconnection

The send and receive operations on channels will all return a [`Result`](https://doc.rust-lang.org/stable/std/result/enum.Result.html "enum std::result::Result") indicating whether the operation succeeded or not. An unsuccessful operation is normally indicative of the other half of a channel having “hung up” by being dropped in its corresponding thread.

Once half of a channel has been deallocated, most operations can no longer continue to make progress, so [`Err`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#variant.Err "variant std::result::Result::Err") will be returned. Many applications will continue to [`unwrap`](https://doc.rust-lang.org/stable/std/result/enum.Result.html#method.unwrap "method std::result::Result::unwrap") the results returned from this module, instigating a propagation of failure among threads if one unexpectedly dies.

## [§](#examples)Examples

Simple usage:

```rust
use std::thread;
use std::sync::mpsc::channel;

// Create a simple streaming channel
let (tx, rx) = channel();
thread::spawn(move || {
    tx.send(10).unwrap();
});
assert_eq!(rx.recv().unwrap(), 10);
```

Shared usage:

```rust
use std::thread;
use std::sync::mpsc::channel;

// Create a shared channel that can be sent along from many threads
// where tx is the sending half (tx for transmission), and rx is the receiving
// half (rx for receiving).
let (tx, rx) = channel();
for i in 0..10 {
    let tx = tx.clone();
    thread::spawn(move || {
        tx.send(i).unwrap();
    });
}

for _ in 0..10 {
    let j = rx.recv().unwrap();
    assert!(0 <= j && j < 10);
}
```

Propagating panics:

```rust
use std::sync::mpsc::channel;

// The call to recv() will return an error because the channel has already
// hung up (or been deallocated)
let (tx, rx) = channel::<i32>();
drop(tx);
assert!(rx.recv().is_err());
```

Synchronous channels:

```rust
use std::thread;
use std::sync::mpsc::sync_channel;

let (tx, rx) = sync_channel::<i32>(0);
thread::spawn(move || {
    // This will wait for the parent thread to start receiving
    tx.send(53).unwrap();
});
rx.recv().unwrap();
```

Unbounded receive loop:

```rust
use std::sync::mpsc::sync_channel;
use std::thread;

let (tx, rx) = sync_channel(3);

for _ in 0..3 {
    // It would be the same without thread and clone here
    // since there will still be one `tx` left.
    let tx = tx.clone();
    // cloned tx dropped within thread
    thread::spawn(move || tx.send("ok").unwrap());
}

// Drop the last sender to stop `rx` waiting for message.
// The program will not complete if we comment this out.
// **All** `tx` needs to be dropped for `rx` to have `Err`.
drop(tx);

// Unbounded receiver waiting for all senders to complete.
while let Ok(msg) = rx.recv() {
    println!("{msg}");
}

println!("completed");
```

[IntoIter](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.IntoIter.html "struct std::sync::mpsc::IntoIter")

An owning iterator over messages on a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver"), created by [`into_iter`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html#method.into_iter "method std::sync::mpsc::Receiver::into_iter").

[Iter](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Iter.html "struct std::sync::mpsc::Iter")

An iterator over messages on a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver"), created by [`iter`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html#method.iter "method std::sync::mpsc::Receiver::iter").

[Receiver](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver")

The receiving half of Rust’s [`channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.channel.html "fn std::sync::mpsc::channel") (or [`sync_channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.sync_channel.html "fn std::sync::mpsc::sync_channel")) type. This half can only be owned by one thread.

[RecvError](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.RecvError.html "struct std::sync::mpsc::RecvError")

An error returned from the [`recv`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html#method.recv "method std::sync::mpsc::Receiver::recv") function on a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver").

[SendError](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.SendError.html "struct std::sync::mpsc::SendError")

An error returned from the [`Sender::send`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Sender.html#method.send "method std::sync::mpsc::Sender::send") or [`SyncSender::send`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.SyncSender.html#method.send "method std::sync::mpsc::SyncSender::send") function on **channel**s.

[Sender](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Sender.html "struct std::sync::mpsc::Sender")

The sending-half of Rust’s asynchronous [`channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.channel.html "fn std::sync::mpsc::channel") type.

[SyncSender](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.SyncSender.html "struct std::sync::mpsc::SyncSender")

The sending-half of Rust’s synchronous [`sync_channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.sync_channel.html "fn std::sync::mpsc::sync_channel") type.

[TryIter](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.TryIter.html "struct std::sync::mpsc::TryIter")

An iterator that attempts to yield all pending values for a [`Receiver`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html "struct std::sync::mpsc::Receiver"), created by [`try_iter`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html#method.try_iter "method std::sync::mpsc::Receiver::try_iter").

[RecvTimeoutError](https://doc.rust-lang.org/stable/std/sync/mpsc/enum.RecvTimeoutError.html "enum std::sync::mpsc::RecvTimeoutError")

This enumeration is the list of possible errors that made [`recv_timeout`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html#method.recv_timeout "method std::sync::mpsc::Receiver::recv_timeout") unable to return data when called. This can occur with both a [`channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.channel.html "fn std::sync::mpsc::channel") and a [`sync_channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.sync_channel.html "fn std::sync::mpsc::sync_channel").

[TryRecvError](https://doc.rust-lang.org/stable/std/sync/mpsc/enum.TryRecvError.html "enum std::sync::mpsc::TryRecvError")

This enumeration is the list of the possible reasons that [`try_recv`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.Receiver.html#method.try_recv "method std::sync::mpsc::Receiver::try_recv") could not return data when called. This can occur with both a [`channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.channel.html "fn std::sync::mpsc::channel") and a [`sync_channel`](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.sync_channel.html "fn std::sync::mpsc::sync_channel").

[TrySendError](https://doc.rust-lang.org/stable/std/sync/mpsc/enum.TrySendError.html "enum std::sync::mpsc::TrySendError")

This enumeration is the list of the possible error outcomes for the [`try_send`](https://doc.rust-lang.org/stable/std/sync/mpsc/struct.SyncSender.html#method.try_send "method std::sync::mpsc::SyncSender::try_send") method.

[channel](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.channel.html "fn std::sync::mpsc::channel")

Creates a new asynchronous channel, returning the sender/receiver halves.

[sync\_channel](https://doc.rust-lang.org/stable/std/sync/mpsc/fn.sync_channel.html "fn std::sync::mpsc::sync_channel")

Creates a new synchronous, bounded channel.