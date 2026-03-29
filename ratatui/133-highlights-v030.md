---
title: v0.30.0
url: https://ratatui.rs/highlights/v030/
source: crawler
fetched_at: 2026-02-01T21:13:23.03828827-03:00
rendered_js: false
word_count: 1754
summary: This document announces the release of Ratatui 0.30.0, detailing major architectural changes like crate modularization, no_std support for embedded systems, and various widget and layout API improvements.
tags:
    - ratatui
    - rust
    - terminal-ui
    - release-notes
    - no-std
    - embedded-rust
    - tui-library
category: other
---

![animation](https://ratatui.rs/_astro/ratatui-animation.CFnuoY9b_fES4P.webp)

We are excited to announce Ratatui 0.30.0, one of our biggest releases yet! 🐁🚀🌕

In this release we’ve [modularized the crates](#modularization), added full [`no_std` support](#no_std-support) for embedded targets, introduced the new [`ratatui::run()`](#execution) API, and brought major [widget](#widgets) and [layout](#layout) improvements — all with better [backend](#backend) flexibility and styling improvements.

See the [changelog](https://github.com/ratatui/ratatui/blob/main/CHANGELOG.md) for the full list of changes. See the breaking changes for this release [here](https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md).

Starting with Ratatui 0.30.0, the codebase was reorganized from a single monolithic crate into a modular workspace consisting of multiple specialized crates. This architectural decision was made to improve modularity, reduce compilation times, enable more flexible dependency management, and provide better API stability for third-party widget libraries.

Here is the new structure of the Ratatui workspace:

```

ratatui
├── ratatui-core
├── ratatui-widgets (depends on ratatui-core)
├── ratatui-crossterm (depends on ratatui-core)
├── ratatui-termion (depends on ratatui-core)
├── ratatui-termwiz (depends on ratatui-core)
└── ratatui-macros
```

See the [architecture overview](https://github.com/ratatui/ratatui/blob/main/ARCHITECTURE.md) for more details.

If you are an application developer, you can continue using `ratatui` as before 🎉

If you are a widget author, consider switching to `ratatui-core` for better stability:

```

// Before (0.29.x and earlier; v0.30.0+ for regular users)
use ratatui::{
widgets::{Widget, StatefulWidget},
buffer::Buffer,
layout::Rect,
};
// After (0.30.0+ for widget developers)
use ratatui_core::{
widgets::{Widget, StatefulWidget},
buffer::Buffer,
layout::Rect,
};
```

## `no_std` Support 🛠️

[Section titled “no\_std Support 🛠️”](#no_std-support)

*we are so embedded*

Ratatui now supports compilation for `no_std` targets! 🎉

This means it can run on bare metal or microcontrollers. Ratatui was successfully tested to run on ESP32, STM32H7, PSP (yes, the console) and UEFI using experimental backends.

![mousefood demo](https://raw.githubusercontent.com/ratatui/mousefood/599f1026d37c8d6308a6df64a234dbefaedc0c6f/assets/demo.gif)

To use it in your `no_std` project, disable `default-features`:

```

ratatui = { version = "0.30.0", default-features = false }
```

All of the features that don’t depend on `std` feature are also supported in `no_std` and can be re-enabled if needed.

We introduced `ratatui::run()` method which runs a closure with a terminal initialized with reasonable defaults for most applications.

This calls `ratatui::init()` before running the closure and `ratatui::restore()` after the closure completes, and returns the result of the closure.

A minimal hello world example using the new `ratatui::run()` method:

```

fnmain() -> Result<(), Box<dynstd::error::Error>> {
ratatui::run(|terminal| {
loop {
terminal.draw(|frame|frame.render_widget("Hello World!", frame.area()))?;
if crossterm::event::read()?.is_key_press() {
break Ok(());
}
}
})
}
```

Of course, this also works both with apps that use free methods and structs:

```

fnrun(terminal:&mut DefaultTerminal) -> Result<(), AppError> { ... }
ratatui::run(run)?;
```

```

struct App { ... }
impl App {
fnnew() ->Self { ... }
fnrun(mutself, terminal:&mut DefaultTerminal) -> Result<(), AppError> { ... }
}
ratatui::run(|terminal| App::new().run(terminal))?;
```

#### Simplified label handling

[Section titled “Simplified label handling”](#simplified-label-handling)

`Bar::label()` & `BarGroup::label()` now accept `Into<Line<'a>>` instead of `Line<'a>`:

```

Bar::default().label("foo".into());
Bar::default().label("foo");
```

```

BarGroup::default().label("bar".into());
BarGroup::default().label("bar");
```

- `BarChart::new` , `BarChart::vertical`, `BarChart::horizontal`, `BarChart::grouped`
- `Bar::new`, `Bar::with_label`
- `BarGroup::new`, `BarGroup::with_label`

This makes it easier to create barcharts and bars without needing to use the builder pattern:

```

BarChart::grouped(vec![
BarGroup::with_label(
"Group 1",
vec![Bar::with_label("A", 10), Bar::with_label("B", 20)],
),
BarGroup::with_label(
"Group 2",
[Bar::with_label("C", 30), Bar::with_label("D", 40)],
),
]);
```

#### Other improvements

[Section titled “Other improvements”](#other-improvements)

`Bar` now implements `Styled`

New marker types are added to `Canvas` for better resolution:

- `Marker::Quadrant`: densely packed and regularly spaced pseudo-pixels with a 2x2 resolution per character, without visible bands between cells. (e.g. ’▌’, ’▞’, ’▛’)
- `Marker::Sextant`: same as `Quadrant` but with a 2x3 resolution per character (e.g. ’🬪’, ’🬫’, ’🬬’)
- `Marker::Octant`: same as `Braille` but with a 2x4 resolution per character (e.g. ’𜶟’, ’𜶠’, ’𜶡’)

You can now retrieve the `ScrollbarState` position via `ScrollbarState::get_position()`

#### Support for merging borders

[Section titled “Support for merging borders”](#support-for-merging-borders)

When two borders overlap, they will automatically merge into a single, clean border instead of overlapping.

This improves visual clarity and reduces rendering glitches around corners.

For example:

```

assert_eq!(Cell::new("┘").merge_symbol("┏", MergeStrategy::Exact).symbol(), "╆");
```

See the `MergeStrategy` documentation for more details on how this works.

But in a nutshell, it makes it possible to collapse borders as follows:

```

┌───┐    ┌───┐  ┌───┬───╮┌───┐
│   │    │   │  │   │   ││   │
│   │    │ ╭─┼─╮│   │   ││   │
│   │    │ │ │ ││   │   ││   │
└───┼───╮└─┼─┘ │└───┴───╯├───┤
│   │  │   │         │   │
│   │  ╰───╯         │   │
│   │                │   │
╰───╯                ╰───╯
```

Click here to see them!

`LightDoubleDashed`:

`HeavyDoubleDashed`:

`LightTripleDashed`:

`HeavyTripleDashed`:

`LightQuadrupleDashed`:

`HeavyQuadrupleDashed`:

#### Remove `Block::title`

[Section titled “Remove Block::title”](#remove-blocktitle)

The title alignment is better expressed in the `Line` as this fits more coherently with the rest of the library.

- `widgets::block` is no longer exported
- `widgets::block::Title` no longer exists
- `widgets::block::Position` is now `widgets::TitlePosition`
- `Block::title()` now accepts `Into::<Line>` instead of `Into<Title>`
- `BlockExt` is now exported at `widgets::BlockExt` instead of `widgets::block::BlockExt`

This is a [breaking change](https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md#blocktitle-no-longer-exists-1926).

#### Support customizable symbols

[Section titled “Support customizable symbols”](#support-customizable-symbols)

`LineGauge` now support customizable symbols via `LineGauge::filled_symbol` and `LineGauge::unfilled_symbol` methods:

```

letgauge= LineGauge::default()
.filled_symbol("█")
.unfilled_symbol("░")
.ratio(0.80);
```

`LineGauge::line_set` method is now deprecated.

`List::highlight_symbol` now accepts `Into<Line>` instead of `&str`.

This makes it possible to customize the highlight symbol as follows:

```

letlist= List::new(["Item 0", "Item 1", "Item 2"])
.highlight_symbol(Line::from(">>").red().bold());
```

This is a breaking change and any code that uses conversion methods will need to be rewritten. Since `Into::into` is not const, this function cannot be called in const context.

Add `Tabs::width` method to easily calculate the total tab width including all dividers and padding

### `RatatuiMascot` widget 🐁

[Section titled “RatatuiMascot widget 🐁”](#ratatuimascot-widget)

Introducing `RatatuiMascot`: A widget that displays the Ratatui mascot!

```

letmascot= RatatuiMascot::new().set_eye(MascotEyeColor::Red);
```

```

▄▄███
▄███████
▄█████████
████████████
▀███████████▀   ▄▄██████
▀███▀▄█▀▀████████
▄▄▄▄▀▄████████████
████████████████
▀███▀██████████
▄▀▀▄   █████████
▄▀ ▄  ▀▄▀█████████
▄▀  ▀▀    ▀▄▀███████
▄▀      ▄▄    ▀▄▀█████████
▄▀         ▀▀     ▀▄▀██▀  ███
█                    ▀▄▀  ▄██
▀▄                    ▀▄▀█
```

The examples have been simplified and reorganized.

- [`ratatui-widgets/examples`](https://github.com/ratatui/ratatui/tree/main/ratatui-widgets/examples): contains simple widget examples (that are meant to be copy & pasted easily).
- [`examples/`](https://github.com/ratatui/ratatui/tree/main/examples): contains more complex application and concept examples that are useful for getting inspiration for designing your own applications.

Also new examples such as [`mouse-drawing`](https://github.com/ratatui/ratatui/tree/main/examples/apps/mouse-drawing), [`widget-ref-container`](https://github.com/ratatui/ratatui/tree/main/examples/apps/widget-ref-container) and [`collapsed-borders`](https://github.com/ratatui/ratatui/blob/main/ratatui-widgets/examples/collapsed-borders.rs) are added.

#### `AddAssign` for `Text`

[Section titled “AddAssign for Text”](#addassign-for-text)

`Text` now implements `AddAssign` trait.

This makes it possible to add a second `Text` instance to a first one using the `+=` operator.

```

letmuttext= Text::from("line 1");
text+= Text::from("line 2");
```

Style and alignment applied to the second text is ignored (though styles and alignment of lines and spans are copied).

#### Other improvements

[Section titled “Other improvements”](#other-improvements-1)

- Don’t render [control characters](https://en.wikipedia.org/wiki/Unicode_control_characters) for `Span`
- Implement `UnicodeWidthStr` for `Text`/`Line`/`Span` for retrieving the width via `width` and `width_cjk`

#### Conversions from `anstyle`

[Section titled “Conversions from anstyle”](#conversions-from-anstyle)

Support conversions from [anstyle](https://crates.io/crates/anstyle) styles (gated behind `anstyle` feature):

```

letanstyle_color= anstyle::Ansi256Color(42);
letcolor= Color::from(anstyle_color);
```

#### Conversions from tuples

[Section titled “Conversions from tuples”](#conversions-from-tuples)

Added generic color conversion methods from tuples:

```

Color::from([255, 0, 0]);
Color::from((255, 0, 0));
Color::from([255, 0, 0, 255]);
Color::from((255, 0, 0, 255));
```

#### Conversions from primitives

[Section titled “Conversions from primitives”](#conversions-from-primitives)

Implement `Styled` for primitives such as `u8`, `i32`, `f64`, `Cow<'a, str>`, etc.

```

lets= Cow::Borrowed("a");
assert_eq!(s.red(), "a".red());
```

#### Implement stylize methods directly on `Style`

[Section titled “Implement stylize methods directly on Style”](#implement-stylize-methods-directly-on-style)

This makes it possible to create constants using the shorthand methods.

```

constMY_STYLE: Style = Style::new().blue().on_black();
```

This is a [breaking change](https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md#style-no-longer-implements-styled-1572).

#### Ergonomic layouting methods

[Section titled “Ergonomic layouting methods”](#ergonomic-layouting-methods)

We introduced new methods for `Rect` that simplify the process of splitting a `Rect` into sub-rects according to a given `Layout`.

`Rect::layout` and `Rect::try_layout`:

```

use ratatui_core::layout::{Layout, Constraint, Rect};
letarea= Rect::new(0, 0, 10, 10);
letlayout= Layout::vertical([Constraint::Fill(1); 2]);
// Rect::layout() infers the number of constraints at compile time:
let [top, main] =area.layout(&layout);
```

`Layout::try_areas` method that returns an array of sub-rects, with compile-time checks for the number of constraints.

This is added mainly for consistency with the new `Rect` methods.

```

// Rect::try_layout() and Layout::try_areas() do the same, but return a
// Result:
let [top, main] =area.try_layout(&layout)?;
let [top, main] =layout.try_areas(area)?;
```

`Rect::layout_vec` method that returns a `Vec` of sub-rects.

```

letareas_vec=area.layout_vec(&layout);
```

#### Helper methods for centering `Rect`s

[Section titled “Helper methods for centering Rects”](#helper-methods-for-centering-rects)

For centering:

```

letarea=frame
.area()
.centered(Constraint::Ratio(1, 2), Constraint::Ratio(1, 3));
```

Or for vertical centering:

```

letarea=frame.area().centered_vertically(Constraint::Ratio(1, 2));
```

Horizontally centering:

```

letarea=frame.area().centered_horizontally(Constraint::Length(3));
```

#### Add `Rect::outer` method

[Section titled “Add Rect::outer method”](#add-rectouter-method)

This creates a new `Rect` outside the current one, with the given margin applied on each side.

Also added `VerticalAlignment` type.

#### Introduce `Flex::SpaceEvenly`

[Section titled “Introduce Flex::SpaceEvenly”](#introduce-flexspaceevenly)

Old `Flex::SpaceAround` behavior is available by using `Flex::SpaceEvenly` and new `Flex::SpaceAround` now distributes space evenly around each element except the middle spacers are twice the size of first and last elements

With this change, the following variants of `Flex` are supported:

- `Flex::Start`: Aligns items to the start; excess space appears at the end.
- `Flex::End`: Aligns items to the end; excess space appears at the start.
- `Flex::Center`: Centers items with equal space on both sides.
- `Flex::SpaceAround` (**new**): Distributes space *around* items; space between items is *twice* the edge spacing.
- `Flex::SpaceBetween`: Distributes space *evenly between* items except no space at the edges.
- `Flex::SpaceEvenly` (**previously `Flex::SpaceAround`** ): Distributes space *evenly between* items and edges.
- `Flex::Legacy`: Preserves legacy behavior, placing all excess space at the end.

This aligns behavior of `Flex` with CSS flexbox more closely.

The following is a screenshot in action:

![image](https://github.com/user-attachments/assets/2c7cd797-27bd-4242-a824-4565d369227b)

#### Other improvements

[Section titled “Other improvements”](#other-improvements-2)

- Rename `Alignment` to `HorizontalAlignment` to better reflect its purpose

```

use ratatui::layout::Alignment;
use ratatui::layout::HorizontalAlignment;
use Alignment::*;
use HorizontalAlignment::*;
```

- New constructors: `Offset::new`
- `Rect::from(size)` returns a new `Rect` at the origin (0, 0) with the specified `Size`

#### Backend conversion traits

[Section titled “Backend conversion traits”](#backend-conversion-traits)

The `From` implementations for backend types are now replaced with more specific traits.

This effects the styling conversions such as `Color`:

```

use ratatui::backend::crossterm::{FromCrossterm, IntoCrossterm};
let crossterm_color = crossterm::style::Color::Black;
let ratatui_color = crossterm_color.into();
let ratatui_color = ratatui::style::Color::from(crossterm_color);
let ratatui_color = ratatui::style::Color::from_crossterm(crossterm_color);
let crossterm_color = ratatui_color.into();
let crossterm_color = crossterm::style::Color::from(ratatui_color);
let crossterm_color = ratatui_color.into_crossterm();
```

Backend specific traits are added for `crossterm` (`FromCrossterm`, `IntoCrossterm`), `termion` (`FromTermion`, `IntoTermion`), and `termwiz` (`FromTermwiz`, `IntoTermwiz`).

See [this breaking changes entry](https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md#the-from-impls-for-backend-types-are-now-replaced-with-more-specific-traits-1464) for more information.

#### Associated `Error` type and required `clear_region` method

[Section titled “Associated Error type and required clear\_region method”](#associated-error-type-and-required-clear_region-method)

Custom `Backend` implementations now require an associated `Error` type and `clear_region` method.

This change was made to provide greater flexibility for custom backends, particularly to remove the explicit dependency on `std::io` for backends that want to support `no_std` targets.

Also, if your app or library uses the `Backend` trait directly - for example, by providing a generic implementation for many backends - you may need to update the referenced error type.

```

fn run<B: Backend>(mut terminal: Terminal<B>) -> io::Result<()> {
fn run<B: Backend>(mut terminal: Terminal<B>) -> Result<(), B::Error> {
```

See [this breaking changes entry](https://github.com/ratatui/ratatui/blob/main/BREAKING-CHANGES.md#backend-now-requires-an-associated-error-type-and-clear_region-method-1778) for more information and other workarounds.

#### Support for multiple crossterm versions

[Section titled “Support for multiple crossterm versions”](#support-for-multiple-crossterm-versions)

We now have individual feature flags for different crossterm versions. By default, the latest version is enabled. If multiple features are enabled, we choose the latest version.

e.g.

```

ratatui = { version = "0.30.0", features = ["crossterm_0_28"] } # or "crossterm_0_29"
```

If your dependency graph ends up with multiple Crossterm majors, see [Crossterm version compatibility](https://ratatui.rs/concepts/backends/#crossterm-version-compatibility) for the risks and mitigations.

#### Other improvements

[Section titled “Other improvements”](#other-improvements-3)

`TestBackend` now uses `core::convert::Infallible` for error handling instead of `std::io::Error`

#### `State` associated types are now `?Sized`

[Section titled “State associated types are now ?Sized”](#state-associated-types-are-now-sized)

`StatefulWidget::State` and `StatefulWidgetRef::State` are now `?Sized`.

This allows implementations of the traits to use unsized types for the State associated type. This is turn is useful when doing things like boxing different stateful widget types with State which implements `Any`, are slices or any other dynamically sized type.

#### Changes to `WidgetRef` trait

[Section titled “Changes to WidgetRef trait”](#changes-to-widgetref-trait)

`WidgetRef` no longer has a blanket implementation of `Widget`.

Previously there was a blanket implementation of `Widget` for `WidgetRef`. This has been reversed to instead be a blanket implementation of `WidgetRef` for all `&W` where `W: Widget`.

```

impl WidgetRef for Foo {
fn render_ref(&self, area: Rect, buf: &mut Buffer)
impl Widget for &Foo {
fn render(self, area: Rect, buf: &mut Buffer)
}
```

Any widgets that previously implemented `WidgetRef` directly should now instead implement `Widget` for a reference to the type.

#### New `FrameExt` trait

[Section titled “New FrameExt trait”](#new-frameext-trait)

To call `Frame::render_widget_ref()` or `Frame::render_stateful_widget_ref()` you now need to import the `FrameExt` trait and enable the `unstable-widget-ref` feature.

```

use ratatui::{
layout::Rect,
widgets::{Block, FrameExt},
};
letblock= Block::new();
letarea= Rect::new(0, 0, 5, 5);
frame.render_widget_ref(&block, area);
```

Disabling `default-features` will now disable layout cache, which can have a negative impact on performance

Layout cache is now opt-in in `ratatui-core` and enabled by default in `ratatui`.

If app doesn’t make use of `no_std`-compatibility, and disables `default-feature`, it is recommended to explicitly re-enable layout cache. Not doing so may impact performance.

```

ratatui = { version = "0.29.0", default-features = false }
ratatui = { version = "0.30.0", default-features = false, features = ["layout-cache"] }
```

Also, `Layout::init_cache` and `Layout::DEFAULT_CACHE_SIZE` are only available if `layout-cache` feature is enabled.

We have added a “Built with Ratatui” badge for downstream projects

If you’d like to show your support, you can add the Ratatui badge to your project’s README:

```

[![Built With Ratatui](https://ratatui.rs/built-with-ratatui/badge.svg)](https://ratatui.rs/)
```

[![Built With Ratatui](https://ratatui.rs/built-with-ratatui/badge.svg)](https://ratatui.rs/)

If you want a custom badge, Ratatui logo is also available on [shields.io](https://shields.io/)! Some examples are:

```

![](https://img.shields.io/badge/Ratatui-000?logo=ratatui&logoColor=fff)
![](https://img.shields.io/badge/Ratatui-fff?logo=ratatui&logoColor=000)
![](https://img.shields.io/badge/Built_With-Ratatui-000?logo=ratatui&logoColor=fff&labelColor=000&color=fff)
![](https://img.shields.io/badge/Ratatui-000?logo=ratatui&logoColor=fff&style=flat-square)
![](https://img.shields.io/badge/Ratatui-000?logo=ratatui&logoColor=fff&style=for-the-badge)
```

![](https://img.shields.io/badge/Ratatui-000?logo=ratatui&logoColor=fff) ![](https://img.shields.io/badge/Ratatui-fff?logo=ratatui&logoColor=000) ![](https://img.shields.io/badge/Built_With-Ratatui-000?logo=ratatui&logoColor=fff&labelColor=000&color=fff) ![](https://img.shields.io/badge/Ratatui-000?logo=ratatui&logoColor=fff&style=flat-square) ![](https://img.shields.io/badge/Ratatui-000?logo=ratatui&logoColor=fff&style=for-the-badge)

- MSRV is now 1.86.0
- The codebase now uses Rust 2024 edition
- Derive Serialize/Deserialize for `Constraint`, `Direction`, `Spacing`, `Layout`, `AccentedPalette`, `NonAccentedPalette`, `Palette`, `Padding`, `Borders`, `BorderType`, `ListDirection`, `ScrollbarOrientation`, `ScrollDirection`, `RenderDirection`, and `HighlightSpacing`, `HorizontalAlignment`, `VerticalAlignment`
- Allow omitting add/sub modifier fields in `Style` deserialization
- VS16 wide emojis are now properly cleared from the buffer
- Change `Cell::symbol` to `Option<CompactString>` to better represent empty cells
- Make it possible to render Braille characters over `Block` symbols in `Chart` and `Canvas`
- Add [AI contribution guidelines](https://github.com/ratatui/ratatui/blob/main/CONTRIBUTING.md#ai-generated-content) and [Copilot instructions](https://github.com/ratatui/ratatui/blob/main/.github/copilot-instructions.md)

* * *

*“Rats don’t just survive; they discover; they create. … I mean, just look at what they do with the terminal!” – Remy & Orhun*