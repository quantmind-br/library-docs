---
title: v0.26.3
url: https://ratatui.rs/highlights/v0263/
source: crawler
fetched_at: 2026-02-01T21:13:35.218505631-03:00
rendered_js: false
word_count: 470
summary: Release notes for Ratatui v0.26.3 detailing critical bug fixes for Unicode truncation, improved color serialization, and rendering performance optimizations.
tags:
    - ratatui
    - rust
    - release-notes
    - tui
    - bug-fix
    - performance-optimization
    - api-update
category: other
---

[https://github.com/ratatui/ratatui/releases/tag/v0.26.3](https://github.com/ratatui/ratatui/releases/tag/v0.26.3)

We are happy to announce a brand new [Ratatui Forum](https://forum.ratatui.rs) 🐭 for Rust & TUI enthusiasts.

![ratatui-forum](https://github.com/ratatui/ratatui/assets/24392180/b13016ca-1044-4c34-9687-f0e39167fb14)

Join here: [**https://forum.ratatui.rs**](https://forum.ratatui.rs)

Here you can get help with your Rust/Ratatui questions and share your projects!

* * *

## Fix Unicode Truncation Bug 🐛

[Section titled “Fix Unicode Truncation Bug 🐛”](#fix-unicode-truncation-bug)

If you are using Ratatui `0.26.2` you might have hit this bug:

> panic occurred at `ratatui-0.26.2/src/text/line.rs:477:59` byte index 51 is not a char boundary; it is inside ‘で’ (bytes 49..52) of `🦀 RFC8628 OAuth 2.0 Device Authorization GrantでCLIからGithubのaccess tokenを取得する`

This issue was introduced in [this PR](https://github.com/ratatui/ratatui/pull/987) and now fixed with `0.26.3`!

```

#[test]
fntruncation_works_with_emoji() {
letline= Line::raw( "123456789🦀");
letmutbuf= Buffer::empty(Rect::new(0, 0, 10, 1));
line.render(buf.area, &mutbuf);
assert_buffer_eq!(buf, Buffer::with_lines(vec!["123456789 "]));
}
```

- Details: [https://github.com/ratatui/ratatui/issues/1032](https://github.com/ratatui/ratatui/issues/1032)
- Implementation: [https://github.com/ratatui/ratatui/pull/1089](https://github.com/ratatui/ratatui/pull/1089)

* * *

## Color: Better Serialization 🎨

[Section titled “Color: Better Serialization 🎨”](#color-better-serialization)

`Color::Rgb` will now be serialized as the hex representation of their value.

For example, `Color::Rgb(255, 0, 255)` would be serialized as `"#FF00FF"` rather than `{"Rgb": [255, 0, 255]}`:

```

letjson_rgb= serde_json::to_string(&Color::Rgb(255, 0, 255))?;
assert_eq!(json_rgb, r##""#FF00FF""##);
assert_eq!(
serde_json::from_str::<Color>(&json_rgb)?,
Color::Rgb(255, 0, 255)
);
```

Similarly, `Color::Indexed` will now be serialized as just the string of the index.

For example, with serde\_json, `Color::Indexed(10)` would be serialized as `"10"` rather than `{"Indexed": 10}`:

```

letjson_indexed= serde_json::to_string(&Color::Indexed(10))?;
assert_eq!(json_indexed, r#""10""#);
assert_eq!(
serde_json::from_str::<Color>(&json_indexed)?,
Color::Indexed(10)
);
```

* * *

## Faster Rendering 🚀

[Section titled “Faster Rendering 🚀”](#faster-rendering)

We sped up combined foreground and background color changes for the `crossterm` backend by up to 20%! 🔥

For more information, see:

- [https://github.com/ratatui/ratatui/pull/1072](https://github.com/ratatui/ratatui/pull/1072)
- [https://github.com/crossterm-rs/crossterm/pull/879](https://github.com/crossterm-rs/crossterm/pull/879)

> I changed the SetColors command to write both colors at once with a single write instead of multiple writes that more bytes. This led to a 15-25% fps increase when testing the colors\_rgb example on iTerm2 on an M2 Macbook Pro.

* * *

## Deprecate `assert_buffer_eq` macro 🚫

[Section titled “Deprecate assert\_buffer\_eq macro 🚫”](#deprecate-assert_buffer_eq-macro)

[`assert_buffer_eq`](https://docs.rs/ratatui/0.26.3/ratatui/macro.assert_buffer_eq.html) is now deprecated in favor of the standard `assert_eq` macro:

```

assert_buffer_eq!(actual, expected);
assert_eq!(actual, expected);
```

We also introduced `TestBackend::assert_buffer_lines` for checking if `TestBackend`’s buffer is equal to the expected lines.

Here is an example usage:

```

#[test]
fnbuffer() {
letbackend= TestBackend::new(10, 2);
backend.assert_buffer_lines([""; 2]);
}
```

So the usage can be simplified as follows:

```

backend.assert_buffer(&Buffer::with_lines(["          "; 2]));
backend.assert_buffer_lines(["          "; 2]);
```

* * *

### Use `Block::bordered` 🟦

[Section titled “Use Block::bordered 🟦”](#use-blockbordered)

Throughout the codebase we switched to the new way of creating bordered Blocks: `Block::bordered`

```

Block::default().borders(Borders::ALL);
Block::bordered();
```

This was added in [0.26](https://ratatui.rs/highlights/v026/#block-bordered) and it requires one less import!

* * *

## Exposed Error Type 🔍

[Section titled “Exposed Error Type 🔍”](#exposed-error-type)

Have you ever tried to wrap `ParseColorError` in your custom error implementation?

```

9|ParseColor(ratatui::style::color::ParseColorError),
|^^^^^---------------struct `ParseColorError` isnotpubliclyre-exported
||
|privatemodule
```

This is now possible since `ParseColorError` is re-exported as `ratatui::style::ParseColorError`!

* * *

We made improvements in some widgets to make use of constant functions and types:

- Make `TableState::new` constant ([#1040](https://github.com/ratatui/ratatui/pull/1040))
- Change canvas map data to const instead of static ([#1037](https://github.com/ratatui/ratatui/pull/1037))
- Use constant function for calendar ([#1039](https://github.com/ratatui/ratatui/pull/1039))

* * *

- Improve performance!
  
  - Simplify `Buffer::filled` with macro ([#1036](https://github.com/ratatui/ratatui/pull/1036))
  - Avoid allocating memory when using split ergonomic utils ([#1105](https://github.com/ratatui/ratatui/pull/1105))
- Changed user\_input example to work with multi-byte unicode chars ([#1069](https://github.com/ratatui/ratatui/pull/1069))
- Handle ZWSP (allow wrapping at zero width whitespace) ([#1074](https://github.com/ratatui/ratatui/pull/1074))
- Fix the Debug panic in Buffer ([#1098](https://github.com/ratatui/ratatui/pull/1098))
- Track caller for index\_of method of Buffer ([#1046](https://github.com/ratatui/ratatui/pull/1046))
- Simplify test cases using [`rstest`](https://github.com/la10736/rstest) ([#1095](https://github.com/ratatui/ratatui/pull/1095))
- Enable and fix some clippy lints (including `clippy::cargo_common_metadata` and `clippy::cargo`)
- Update crate metadata such as keywords and homepage

* * *

[🧀](https://www.youtube.com/shorts/_TuUyB0kAGE)