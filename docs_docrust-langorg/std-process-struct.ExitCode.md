---
title: ExitCode in std::process - Rust
url: https://doc.rust-lang.org/std/process/struct.ExitCode.html
source: crawler
fetched_at: 2026-05-06T21:26:39.63324994-03:00
rendered_js: false
word_count: 577
summary: This document describes the ExitCode struct in Rust, which represents the status code returned by a process to its parent upon termination, facilitating cross-platform process exit handling.
tags:
    - rust
    - exit-code
    - process-management
    - termination
    - std-library
    - systems-programming
category: reference
---

## Struct ExitCode

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2100)

```rust
pub struct ExitCode(/* private fields */);
```

Expand description

This type represents the status code the current process can return to its parent under normal termination.

`ExitCode` is intended to be consumed only by the standard library (via [`Termination::report()`](https://doc.rust-lang.org/std/process/trait.Termination.html#tymethod.report "method std::process::Termination::report")). For forwards compatibility with potentially unusual targets, this type currently does not provide `Eq`, `Hash`, or access to the raw value. This type does provide `PartialEq` for comparison, but note that there may potentially be multiple failure codes, some of which will *not* compare equal to `ExitCode::FAILURE`. The standard library provides the canonical `SUCCESS` and `FAILURE` exit codes as well as `From<u8> for ExitCode` for constructing other arbitrary exit codes.

## [§](#portability)Portability

Numeric values used in this type don’t have portable meanings, and different platforms may mask different amounts of them.

For the platform’s canonical successful and unsuccessful codes, see the [`SUCCESS`](https://doc.rust-lang.org/std/process/struct.ExitCode.html#associatedconstant.SUCCESS "associated constant std::process::ExitCode::SUCCESS") and [`FAILURE`](https://doc.rust-lang.org/std/process/struct.ExitCode.html#associatedconstant.FAILURE "associated constant std::process::ExitCode::FAILURE") associated items.

## [§](#differences-from-exitstatus)Differences from `ExitStatus`

`ExitCode` is intended for terminating the currently running process, via the `Termination` trait, in contrast to [`ExitStatus`](https://doc.rust-lang.org/std/process/struct.ExitStatus.html "struct std::process::ExitStatus"), which represents the termination of a child process. These APIs are separate due to platform compatibility differences and their expected usage; it is not generally possible to exactly reproduce an `ExitStatus` from a child for the current process after the fact.

## [§](#examples)Examples

`ExitCode` can be returned from the `main` function of a crate, as it implements [`Termination`](https://doc.rust-lang.org/std/process/trait.Termination.html "trait std::process::Termination"):

```rust
use std::process::ExitCode;

fn main() -> ExitCode {
    if !check_foo() {
        return ExitCode::from(42);
    }

    ExitCode::SUCCESS
}
```

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2107-2166)[§](#impl-ExitCode)

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2114)

The canonical `ExitCode` for successful termination on this platform.

Note that a `()`-returning `main` implicitly results in a successful termination, so there’s no need to return this from `main` unless you’re also returning other possible codes.

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2122)

The canonical `ExitCode` for unsuccessful termination on this platform.

If you’re only returning this and `SUCCESS` from `main`, consider instead returning `Err(_)` and `Ok(())` respectively, which will return the same codes (but will also `eprintln!` the error).

[Source](https://doc.rust-lang.org/src/std/process.rs.html#2163-2165)

🔬This is a nightly-only experimental API. (`exitcode_exit_method` [#97100](https://github.com/rust-lang/rust/issues/97100))

Exit the current process with the given `ExitCode`.

Note that this has the same caveats as [`process::exit()`](https://doc.rust-lang.org/std/process/fn.exit.html "fn std::process::exit"), namely that this function terminates the process immediately, so no destructors on the current stack or any other thread’s stack will be run. Also see those docs for some important notes on interop with C code. If a clean shutdown is needed, it is recommended to simply return this ExitCode from the `main` function, as demonstrated in the [type documentation](#examples).

##### [§](#differences-from-processexit)Differences from `process::exit()`

`process::exit()` accepts any `i32` value as the exit code for the process; however, there are platforms that only use a subset of that value (see [`process::exit` platform-specific behavior](https://doc.rust-lang.org/std/process/fn.exit.html#platform-specific-behavior "fn std::process::exit")). `ExitCode` exists because of this; only `ExitCode`s that are supported by a majority of our platforms can be created, so those problems don’t exist (as much) with this method.

##### [§](#examples-1)Examples

```rust
#![feature(exitcode_exit_method)]
// there's no way to gracefully recover from an UhOhError, so we just
// print a message and exit
fn handle_unrecoverable_error(err: UhOhError) -> ! {
    eprintln!("UH OH! {err}");
    let code = match err {
        UhOhError::GenericProblem => ExitCode::FAILURE,
        UhOhError::Specific => ExitCode::from(3),
        UhOhError::WithCode { exit_code, .. } => exit_code,
    };
    code.exit_process()
}
```

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2098)[§](#impl-Clone-for-ExitCode)

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2098)[§](#impl-Debug-for-ExitCode)

1.75.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2190-2194)[§](#impl-Default-for-ExitCode)

[Source](https://doc.rust-lang.org/src/std/os/windows/process.rs.html#476-480)[§](#impl-ExitCodeExt-for-ExitCode)

Available on **Windows** only.

[Source](https://doc.rust-lang.org/src/std/os/windows/process.rs.html#477-479)[§](#method.from_raw)

🔬This is a nightly-only experimental API. (`windows_process_exit_code_from` [#111688](https://github.com/rust-lang/rust/issues/111688))

Creates a new `ExitCode` from the raw underlying `u32` return value of a process. [Read more](https://doc.rust-lang.org/std/os/windows/process/trait.ExitCodeExt.html#tymethod.from_raw)

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2197-2202)[§](#impl-From%3Cu8%3E-for-ExitCode)

[Source](https://doc.rust-lang.org/src/std/process.rs.html#2199-2201)[§](#method.from)

Constructs an `ExitCode` from an arbitrary u8 value.

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2098)[§](#impl-PartialEq-for-ExitCode)

[Source](https://doc.rust-lang.org/src/std/process.rs.html#2098)[§](#method.eq)

Tests for `self` and `other` values to be equal, and is used by `==`.

1.0.0 · [Source](https://doc.rust-lang.org/src/core/cmp.rs.html#264)[§](#method.ne)

Tests for `!=`. The default implementation is almost always sufficient, and should not be overridden without very good reason.

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2601-2606)[§](#impl-Termination-for-ExitCode)

[Source](https://doc.rust-lang.org/src/std/process.rs.html#2603-2605)[§](#method.report)

Is called to get the representation of the value as status code. This status code is returned to the operating system.

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2098)[§](#impl-Copy-for-ExitCode)

1.61.0 · [Source](https://doc.rust-lang.org/src/std/process.rs.html#2098)[§](#impl-StructuralPartialEq-for-ExitCode)

[§](#impl-Freeze-for-ExitCode)

[§](#impl-RefUnwindSafe-for-ExitCode)

[§](#impl-Send-for-ExitCode)

[§](#impl-Sync-for-ExitCode)

[§](#impl-Unpin-for-ExitCode)

[§](#impl-UnsafeUnpin-for-ExitCode)

[§](#impl-UnwindSafe-for-ExitCode)