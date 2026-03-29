---
title: v0.27.0
url: https://ratatui.rs/highlights/v027/
source: crawler
fetched_at: 2026-02-01T21:13:32.188940341-03:00
rendered_js: false
word_count: 833
summary: This document details the new features and breaking changes in Ratatui version 0.27.0, highlighting widget updates, backend re-exports, and trait improvements for terminal UI development.
tags:
    - ratatui
    - rust
    - release-notes
    - terminal-ui
    - tui-library
    - api-updates
category: reference
---

[https://github.com/ratatui/ratatui/releases/tag/v0.27.0](https://github.com/ratatui/ratatui/releases/tag/v0.27.0)

⚠️ See the [breaking changes](https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md) for this release.

## LineGauge: Background Styles 📊

[Section titled “LineGauge: Background Styles 📊”](#linegauge-background-styles)

`LineGauge::gauge_style` is now deprecated in favor of `filled_style` and `unfilled_style` methods which makes it possible to set the foreground/background styles for different states.

```

letgauge= LineGauge::default()
.filled_style(Style::default().fg(Color::Green))
.unfilled_style(Style::default().fg(Color::White))
.ratio(0.43);
```

We also added a [Line Gauge example](https://github.com/ratatui/ratatui/blob/main/examples/line_gauge.rs):

Your browser does not support the video tag.

* * *

## List: Navigation Methods 🧭

[Section titled “List: Navigation Methods 🧭”](#list-navigation-methods)

You can now navigate in the `List` widget by using the following methods!

```

letmutstate= ListState::default();
state.select_first();
state.select_next();
state.select_previous();
state.select_last();
```

It also clamps the selected index to the bounds of the list when navigating.

* * *

## Text: Conversion From Display 🔄

[Section titled “Text: Conversion From Display 🔄”](#text-conversion-from-display)

`Text`, `Span` and `Line` now supports conversion from any type that implements the `Display` trait!

```

lettext="line1\nline2".to_text();
letspan= (6.66).to_span();
letline=42.to_line();
```

This has been made possible with the newly added `ToText`, `ToSpan` and `ToLine` traits respectfully.

* * *

⚠️ This is behind the “palette” feature flag.

You can now use colors from the [palette](https://crates.io/crates/palette) crate in Ratatui!

```

use palette::{LinSrgb, Srgb};
use ratatui::style::Color;
letcolor= Color::from(Srgb::new(1.0f32, 0.0, 0.0));
letcolor= Color::from(LinSrgb::new(1.0f32, 0.0, 0.0));
```

* * *

## New Border Sets 🖼️

[Section titled “New Border Sets 🖼️”](#new-border-sets-%EF%B8%8F)

It uses an empty space symbol (░)

```

letblock= Block::bordered().title("Title").border_set(border::EMPTY);
```

```

░░░░░░░░
░░    ░░
░░ ░░ ░░
░░ ░░ ░░
░░    ░░
░░░░░░░░
```

This is useful for when you need to allocate space for the border and apply the border style to a block without actually drawing a border. This makes it possible to style the entire title area or a block rather than just the title content.

It uses a full block symbol (█)

```

letblock= Block::bordered().title("Title").border_set(border::FULL);
```

* * *

## Re-export Backends 📤

[Section titled “Re-export Backends 📤”](#re-export-backends)

`crossterm`, `termion`, and `termwiz` can now be accessed as `ratatui::{crossterm, termion, termwiz}` respectively.

This makes it possible to just add the Ratatui crate as a dependency and use the backend of choice without having to add the backend crates as dependencies.

To update existing code, replace all instances of `crossterm::` with `ratatui::crossterm::`, `termion::` with `ratatui::termion::`, and `termwiz::` with `ratatui::termwiz::`.

Example for `crossterm`:

```

use crossterm::event::{Event, KeyCode, KeyEvent, KeyEventKind};
use ratatui::crossterm::event::{Event, KeyCode, KeyEvent, KeyEventKind};
```

And then you can remove `crossterm` from `Cargo.toml`!

* * *

Based on a [suggestion on Reddit](https://www.reddit.com/r/rust/comments/1cle18j/comment/l2uuuh7/) we made changes to the `prelude` module.

> Note: This module allows you to easily use `ratatui` without a huge amount of imports! e.g. `use ratatui::prelude::*;`

The following items have been removed from the prelude:

- `style::Styled` - this trait is useful for widgets that want to support the Stylize trait, but it adds complexity as widgets have two `style` methods and a `set_style` method.
- `symbols::Marker` - this item is used by code that needs to draw to the `Canvas` widget, but it’s not a common item that would be used by most users of the library.
- `terminal::{CompletedFrame, TerminalOptions, Viewport}` - these items are rarely used by code that needs to interact with the terminal, and they’re generally only ever used once in any app.

The following items have been added to the prelude:

- `layout::{Position, Size}` - these items are used by code that needs to interact with the layout system. These are newer items that were added in the last few releases, which should be used more liberally.

* * *

## Tracing Example 🔍

[Section titled “Tracing Example 🔍”](#tracing-example)

Wondering how to debug TUI apps? Tried `println` and it didn’t work? We got you covered!

We added an example that demonstrates how to log to a file:

![tracing example](https://vhs.charm.sh/vhs-21jgJCedh2YnFDONw0JW7l.gif)

- Code: [https://github.com/ratatui/ratatui/blob/main/examples/tracing.rs](https://github.com/ratatui/ratatui/blob/main/examples/tracing.rs)
- Related discussion on Ratatui Forum: [https://forum.ratatui.rs/t/how-do-you-println-debug-your-tui-programs/66](https://forum.ratatui.rs/t/how-do-you-println-debug-your-tui-programs/66)

* * *

## Hyperlink Example 🔗

[Section titled “Hyperlink Example 🔗”](#hyperlink-example)

We added a proof-of-concept example for using hyperlinks in the terminal.

![Demo](https://vhs.charm.sh/vhs-2c5cvJzN7KTKR7U3Jbk71J.gif)

> The code is available [here](https://github.com/ratatui/ratatui/blob/main/examples/hyperlink.rs).

* * *

## Cell: New methods 🔧

[Section titled “Cell: New methods 🔧”](#cell-new-methods)

You can now create empty `Cell`s like this:

```

letmutcell= Cell::EMPTY;
assert_eq!(cell.symbol(), "");
```

We also added a constant `Cell:new` method for simplify the construction as follows:

```

let mut cell = Cell::default();
cell.set_symbol("a");
let cell = Cell::new("a");
```

* * *

## Make `Stylize::bg()` generic 🔄

[Section titled “Make Stylize::bg() generic 🔄”](#make-stylizebg-generic)

Previously, `Stylize::bg()` accepted `Color` but now accepts `Into<Color>`. This allows more flexible types from calling scopes, though it can break some type inference in the calling scope.

```

letsrgb_color: Srgb<u8> = Srgb::new(255, 0, 0);
foo.bg(srgb_color);
```

* * *

## Writer Methods on Backends 🖋️

[Section titled “Writer Methods on Backends 🖋️”](#writer-methods-on-backends-%EF%B8%8F)

`crossterm` and `termion` backends now have `writer()` and `writer_mut()` methods for obtain access to the underlying writer.

This is useful e.g. if you want to see what has been written so far.

```

letterminal= Terminal::new(CrosstermBackend::new(Vec::<u8>::new()));
letui=|frame| { ... };
terminal.draw(ui);
letcrossterm_backend=terminal.backend();
letbuffer=crossterm_backend.writer();
```

* * *

## Add Missing VHS Tapes 📼

[Section titled “Add Missing VHS Tapes 📼”](#add-missing-vhs-tapes)

We were missing demos for some of our examples. They are now added!

[Constraint explorer example](https://github.com/ratatui/ratatui/blob/main/examples/constraint-explorer.rs):

![constraint-explorer](https://github.com/ratatui/ratatui/assets/381361/9933df57-3afc-4d5b-88bd-15909f6dcdaf)

[Minimal example](https://github.com/ratatui/ratatui/blob/main/examples/minimal.rs):

![minimal](https://github.com/ratatui/ratatui/assets/381361/d39b518e-906b-4725-8cae-6fbad17f3a90)

* * *

## List: Remove deprecated `start_corner()` 🚫

[Section titled “List: Remove deprecated start\_corner() 🚫”](#list-remove-deprecated-start_corner)

`List::start_corner` was deprecated back in v0.25.

Use `List::direction` and `ListDirection` instead:

```

list.start_corner(Corner::TopLeft);
list.start_corner(Corner::TopRight);
// This is not an error, BottomRight rendered top to bottom previously
list.start_corner(Corner::BottomRight);
// all becomes
list.direction(ListDirection::TopToBottom);
```

```

list.start_corner(Corner::BottomLeft);
// becomes
list.direction(ListDirection::BottomToTop);
```

`layout::Corner` is also removed entirely.

* * *

## Padding: Deprecate `zero()` 🚫

[Section titled “Padding: Deprecate zero() 🚫”](#padding-deprecate-zero)

It is now a constant!

```

Padding::zero()
Padding::ZERO
```

* * *

## Buffer: Improve Performance ⚡️

[Section titled “Buffer: Improve Performance ⚡️”](#buffer-improve-performance-%EF%B8%8F)

`Buffer::filled` now moves the cell instead of taking a reference:

```

Buffer::filled(area, &Cell::new("X"));
Buffer::filled(area, Cell::new("X"));
```

* * *

## Rect: Improve Performance ⚡️

[Section titled “Rect: Improve Performance ⚡️”](#rect-improve-performance-%EF%B8%8F)

`Margin` needs to be passed without reference now:

```

let area = area.inner(&Margin {
let area = area.inner(Margin {
vertical: 0,
horizontal: 2,
});
```

* * *

- `Position` and `Size` now implements `Display` ([#1162](https://github.com/ratatui/ratatui/pull/1162))
- Remove newlines when converting strings to `Line`s ([#1191](https://github.com/ratatui/ratatui/pull/1191))
  
  - `Line::from("a\nb")` now returns a `Line` with two `Span`s instead of one
- Ensure that zero-width characters are rendered correctly ([#1165](https://github.com/ratatui/ratatui/pull/1165))
- Respect area width while rendering &str and String ([#1177](https://github.com/ratatui/ratatui/pull/1177))
- Improve benchmark consistency ([#1126](https://github.com/ratatui/ratatui/pull/1126))

* * *

*“I can’t believe it! A real gourmet kitchen, and I get to watch!” – Remy*