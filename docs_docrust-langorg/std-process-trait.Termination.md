---
title: Termination in std::process - Rust
url: https://doc.rust-lang.org/std/process/trait.Termination.html
source: crawler
fetched_at: 2026-05-06T21:21:49.55571756-03:00
rendered_js: false
word_count: 119
summary: This document defines the Termination trait, which allows the main function in Rust to return arbitrary types by converting them into operating system-compatible exit codes.
tags:
    - rust
    - trait
    - termination
    - exit-code
    - process-management
    - main-function
category: reference
---

## Trait Termination

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2571-2576)

```rust
pub trait Termination {
    // Required method
    fn report(self) -> ExitCode;
}
```

Expand description

A trait for implementing arbitrary return types in the `main` function.

The C-main function only supports returning integers. So, every type implementing the `Termination` trait has to be converted to an integer.

The default implementations are returning `libc::EXIT_SUCCESS` to indicate a successful execution. In case of a failure, `libc::EXIT_FAILURE` is returned.

Because different runtimes have different specifications on the return value of the `main` function, this trait is likely to be available only on standard library’s runtime for convenience. Other runtimes are not required to provide similar functionality.

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2575)

Is called to get the representation of the value as status code. This status code is returned to the operating system.