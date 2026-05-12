---
title: Arguments in std::fmt - Rust
url: https://doc.rust-lang.org/std/fmt/struct.Arguments.html
source: crawler
fetched_at: 2026-05-06T21:24:01.05227418-03:00
rendered_js: false
word_count: 261
summary: The Arguments structure provides a safely precompiled representation of format strings and their arguments for use with formatting macros in Rust. It enables efficient string formatting and includes utility methods for optimization, such as retrieving raw string literals.
tags:
    - rust
    - formatting
    - precompiled-strings
    - macro-support
    - memory-optimization
category: reference
---

## Struct Arguments

1.0.0 · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#716)

```rust
pub struct Arguments<'a> { /* private fields */ }
```

Expand description

This structure represents a safely precompiled version of a format string and its arguments. This cannot be generated at runtime because it cannot safely be done, so no constructors are given and the fields are private to prevent modification.

The [`format_args!`](https://doc.rust-lang.org/std/macro.format_args.html "macro std::format_args") macro will safely create an instance of this structure. The macro validates the format string at compile-time so usage of the [`write()`](https://doc.rust-lang.org/std/fmt/fn.write.html "fn std::fmt::write") and [`format()`](https://doc.rust-lang.org/std/fmt/fn.format.html) functions can be safely performed.

You can use the `Arguments<'a>` that [`format_args!`](https://doc.rust-lang.org/std/macro.format_args.html "macro std::format_args") returns in `Debug` and `Display` contexts as seen below. The example also shows that `Debug` and `Display` format to the same thing: the interpolated format string in `format_args!`.

```rust
let debug = format!("{:?}", format_args!("{} foo {:?}", 1, 2));
let display = format!("{}", format_args!("{} foo {:?}", 1, 2));
assert_eq!("1 foo 2", display);
assert_eq!(display, debug);
```

[Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#809)[§](#impl-Arguments%3C'a%3E)

[Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#815)

🔬This is a nightly-only experimental API. (`fmt_arguments_from_str` [#148905](https://github.com/rust-lang/rust/issues/148905))

Create a `fmt::Arguments` object for a single static string.

Formatting this `fmt::Arguments` will just produce the string as-is.

1.52.0 (const: 1.84.0) · [Source](https://doc.rust-lang.org/src/core/fmt/mod.rs.html#871)

Gets the formatted string, if it has no arguments to be formatted at runtime.

This can be used to avoid allocations in some cases.

##### [§](#guarantees)Guarantees

For `format_args!("just a literal")`, this function is guaranteed to return `Some("just a literal")`.

For most cases with placeholders, this function will return `None`.

However, the compiler may perform optimizations that can cause this function to return `Some(_)` even if the format string contains placeholders. For example, `format_args!("Hello, {}!", "world")` may be optimized to `format_args!("Hello, world!")`, such that `as_str()` returns `Some("Hello, world!")`.

The behavior for anything but the trivial case (without placeholders) is not guaranteed, and should not be relied upon for anything other than optimization.

##### [§](#examples)Examples

```rust
use std::fmt::Arguments;

fn write_str(_: &str) { /* ... */ }

fn write_fmt(args: &Arguments<'_>) {
    if let Some(s) = args.as_str() {
        write_str(s)
    } else {
        write_str(&args.to_string());
    }
}
```

```rust
assert_eq!(format_args!("hello").as_str(), Some("hello"));
assert_eq!(format_args!("").as_str(), Some(""));
assert_eq!(format_args!("{:?}", std::env::current_dir()).as_str(), None);
```

[§](#impl-Freeze-for-Arguments%3C'a%3E)

[§](#impl-RefUnwindSafe-for-Arguments%3C'a%3E)

[§](#impl-Unpin-for-Arguments%3C'a%3E)

[§](#impl-UnsafeUnpin-for-Arguments%3C'a%3E)

[§](#impl-UnwindSafe-for-Arguments%3C'a%3E)