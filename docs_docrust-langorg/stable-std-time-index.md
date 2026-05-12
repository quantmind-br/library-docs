---
title: std::time - Rust
url: https://doc.rust-lang.org/stable/std/time/index.html
source: crawler
fetched_at: 2026-05-06T21:28:28.848221823-03:00
rendered_js: false
word_count: 145
summary: Provides core utilities for temporal quantification, including types for measuring elapsed durations, system time, and monotonic clock instants.
tags:
    - rust
    - time-measurement
    - duration
    - system-time
    - monotonic-clock
category: reference
---

## Module time

1.3.0 · [Source](https://doc.rust-lang.org/stable/src/std/time.rs.html#1-859)

Expand description

Temporal quantification.

## [§](#examples)Examples

There are multiple ways to create a new [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration"):

```rust
let five_seconds = Duration::from_secs(5);
assert_eq!(five_seconds, Duration::from_millis(5_000));
assert_eq!(five_seconds, Duration::from_micros(5_000_000));
assert_eq!(five_seconds, Duration::from_nanos(5_000_000_000));

let ten_seconds = Duration::from_secs(10);
let seven_nanos = Duration::from_nanos(7);
let total = ten_seconds + seven_nanos;
assert_eq!(total, Duration::new(10, 7));
```

Using [`Instant`](https://doc.rust-lang.org/stable/std/time/struct.Instant.html "struct std::time::Instant") to calculate how long a function took to run:

[ⓘ](# "This example is not tested")

```rust
let now = Instant::now();

// Calling a slow function, it may take a while
slow_function();

let elapsed_time = now.elapsed();
println!("Running slow_function() took {} seconds.", elapsed_time.as_secs());
```

[Duration](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration")

A `Duration` type to represent a span of time, typically used for system timeouts.

[Instant](https://doc.rust-lang.org/stable/std/time/struct.Instant.html "struct std::time::Instant")

A measurement of a monotonically nondecreasing clock. Opaque and useful only with [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration").

[SystemTime](https://doc.rust-lang.org/stable/std/time/struct.SystemTime.html "struct std::time::SystemTime")

A measurement of the system clock, useful for talking to external entities like the file system or other processes.

[SystemTimeError](https://doc.rust-lang.org/stable/std/time/struct.SystemTimeError.html "struct std::time::SystemTimeError")

An error returned from the `duration_since` and `elapsed` methods on `SystemTime`, used to learn how far in the opposite direction a system time lies.

[TryFromFloatSecsError](https://doc.rust-lang.org/stable/std/time/struct.TryFromFloatSecsError.html "struct std::time::TryFromFloatSecsError")

An error which can be returned when converting a floating-point value of seconds into a [`Duration`](https://doc.rust-lang.org/stable/std/time/struct.Duration.html "struct std::time::Duration").

[UNIX\_EPOCH](https://doc.rust-lang.org/stable/std/time/constant.UNIX_EPOCH.html "constant std::time::UNIX_EPOCH")

An anchor in time which can be used to create new `SystemTime` instances or learn about where in time a `SystemTime` lies.