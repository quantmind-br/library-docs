---
title: Using no_std
url: https://ratatui.rs/concepts/no-std/
source: crawler
fetched_at: 2026-02-01T21:13:00.121918278-03:00
rendered_js: false
word_count: 229
summary: This document provides instructions on how to use Ratatui in no_std and embedded environments, covering dependency configuration and widget implementation.
tags:
    - rust
    - ratatui
    - no-std
    - embedded-systems
    - tui
    - widget-development
category: guide
---

Ratatui is `no_std`-compatible, which allows it to run in embedded and other resource-constrained environments. This means you can run TUIs on a wider range of targets and have widget usable in both desktop and embedded environments.

## Using Ratatui without `std`

[Section titled “Using Ratatui without std”](#using-ratatui-without-std)

1. Disable default features so the crate does not pull in `std`-only dependencies:

```

ratatui = { version = "0.30", default-features = false }
```

2. Choose a backend that works on your platform.

The built-in backends rely on `std`, so `no_std` targets need a custom backend that implements `ratatui::backend::Backend` or a third-party option like [`mousefood`](https://ratatui.rs/ecosystem/mousefood/) 🧀

3. When checking a `no_std` build, compile with a `no_std` target.

For example, on ESP32:

```

cargocheck--targetriscv32imc-unknown-none-elf
```

If you already have a Ratatui widget, you can make it `no_std`-compatible with a few small changes. Even if you haven’t built for embedded before!

1. Opt into `no_std` and add `alloc` crate:
   
   ```
   
   #![no_std]
   externcrate alloc;
   ```
2. Depend on `ratatui-core` instead of the full `ratatui` crate to avoid backend dependencies:
   
   ```
   
   ratatui-core = { version = "0.1", default-features = false }
   ```
3. Swap `std` types for their `core`/`alloc` equivalents, for example `core::fmt`, `alloc::string::String`, `alloc::vec::Vec`, and `alloc::boxed::Box`.
4. Keep a `std` feature (off by default) for conveniences like tests or examples, but write your core widget logic so it also works without it.
5. Avoid `std`-only APIs in widget code paths. Examples: use `core::time::Duration` instead of `std::time::Duration`, pass in data rather than reading files, and keep logging behind a feature so it can be disabled on targets without I/O.

Here is a minimal `no_std` widget implementation:

```

#![no_std]
externcrate alloc;
use alloc::string::String;
use ratatui_core::buffer::Buffer;
use ratatui_core::layout::Rect;
use ratatui_core::text::Line;
use ratatui_core::widgets::Widget;
struct Greeting {
message: String,
}
impl Widget for&Greeting {
fnrender(self, area: Rect, buf:&mut Buffer) {
Line::raw(&self.message).render(area, buf);
}
}
```