---
title: IsTerminal in std::io - Rust
url: https://doc.rust-lang.org/stable/std/io/trait.IsTerminal.html#tymethod.is_terminal
source: crawler
fetched_at: 2026-05-06T21:31:19.835572736-03:00
rendered_js: false
word_count: 234
summary: This document defines the IsTerminal trait in Rust, which provides a standard interface to check if an I/O descriptor or handle is connected to a terminal or TTY.
tags:
    - rust
    - stdio
    - terminal-detection
    - tty
    - io-traits
    - platform-specific
category: reference
---

## Trait IsTerminal

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1197-1248)

```rust
pub trait IsTerminal: Sealed {
    // Required method
    fn is_terminal(&self) -> bool;
}
```

Expand description

Trait to determine if a descriptor/handle refers to a terminal/tty.

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1247)

Returns `true` if the descriptor/handle refers to a terminal/tty.

On platforms where Rust does not know how to detect a terminal yet, this will return `false`. This will also return `false` if an unexpected error occurred, such as from passing an invalid file descriptor.

##### [§](#platform-specific-behavior)Platform-specific behavior

On Windows, in addition to detecting consoles, this currently uses some heuristics to detect older msys/cygwin/mingw pseudo-terminals based on device name: devices with names starting with `msys-` or `cygwin-` and ending in `-pty` will be considered terminals. Note that this [may change in the future](https://doc.rust-lang.org/stable/std/io/index.html#platform-specific-behavior "mod std::io").

##### [§](#examples)Examples

An example of a type for which `IsTerminal` is implemented is [`Stdin`](https://doc.rust-lang.org/stable/std/io/struct.Stdin.html "struct std::io::Stdin"):

```rust
use std::io::{self, IsTerminal, Write};

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    // Indicate that the user is prompted for input, if this is a terminal.
    if stdin.is_terminal() {
        print!("> ");
        io::stdout().flush()?;
    }

    let mut name = String::new();
    let _ = stdin.read_line(&mut name)?;

    println!("Hello {}", name.trim_end());

    Ok(())
}
```

The example can be run in two ways:

- If you run this example by piping some text to it, e.g. `echo "foo" | path/to/executable` it will print: `Hello foo`.
- If you instead run the example interactively by running `path/to/executable` directly, it will prompt for input.

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-File)

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#253)[§](#impl-IsTerminal-for-BorrowedFd%3C'_%3E)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/fd/owned.rs.html#253)[§](#impl-IsTerminal-for-OwnedFd)

Available on **Unix or HermitCore or `target_os=trusty` or WASI or `target_os=motor`** only.

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#421)[§](#impl-IsTerminal-for-BorrowedHandle%3C'_%3E)

Available on **Windows** only.

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/os/windows/io/handle.rs.html#421)[§](#impl-IsTerminal-for-OwnedHandle)

Available on **Windows** only.

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-Stderr)

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-StderrLock%3C'_%3E)

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-Stdin)

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-StdinLock%3C'_%3E)

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-Stdout)

1.70.0 · [Source](https://doc.rust-lang.org/stable/src/std/io/stdio.rs.html#1265)[§](#impl-IsTerminal-for-StdoutLock%3C'_%3E)