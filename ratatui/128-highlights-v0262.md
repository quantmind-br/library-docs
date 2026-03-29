---
title: v0.26.2
url: https://ratatui.rs/highlights/v0262/
source: crawler
fetched_at: 2026-02-01T21:13:38.663285323-03:00
rendered_js: false
word_count: 285
summary: This document outlines the new features, API changes, and bug fixes introduced in version 0.26.2 of the Ratatui Rust library. It details updates to text widgets, list scrolling behavior, and the minimum supported Rust version.
tags:
    - ratatui
    - rust-library
    - release-notes
    - tui
    - api-updates
    - terminal-graphics
category: api
---

[https://github.com/ratatui/ratatui/releases/tag/v0.26.2](https://github.com/ratatui/ratatui/releases/tag/v0.26.2)

The minimum supported Rust version of Ratatui is updated from `1.70.0` to `1.74.0`.

* * *

We introduced a new method for `List` which allows a certain number of items be kept visible above and below the currently selected item while scrolling.

```

letlist= List::new(items).scroll_padding(1);
```

Demo of the new behavior

![scroll_padding](https://github.com/ratatui/ratatui/assets/30030363/66de2c06-1d5f-41ff-8cf3-09febb7ccdd3)

(visible on the left side)

* * *

## Text: Construct from Iterator 🏗️

[Section titled “Text: Construct from Iterator 🏗️”](#text-construct-from-iterator-%EF%B8%8F)

`Line` and `Text` widgets now implement `FromIterator` which means you can:

- Construct `Line` from an iterator of `Span`

```

letline= Line::from_iter(vec!["Hello".blue(), " world!".green()]);
letline: Line = iter::once("Hello".blue())
.chain(iter::once(" world!".green()))
.collect();
```

- Construct `Text` from an iterator of `Line`

```

lettext= Text::from_iter(vec!["The first line", "The second line"]);
lettext: Text = iter::once("The first line")
.chain(iter::once("The second line"))
.collect();
```

* * *

## Text: Push Methods 📥

[Section titled “Text: Push Methods 📥”](#text-push-methods)

We added the following methods to the `Text` and `Line` structs:

- `Text::push_line`
- `Text::push_span`
- `Line::push_span`

This allows for adding lines and spans to a text object without having to call methods on the fields directly, which is useful for incremental construction of text objects.

For example:

```

letmutline= Line::from("Hello, ");
line.push_span(Span::raw("world!"));
line.push_span(" How are you?");
```

* * *

`Widget` is now implemented for `&str` and `String`, which makes it easier to render strings with no styles as widgets.

Example usage:

```

terminal.draw(|f|f.render_widget("Hello World!", f.size()))?;
```

* * *

## Span: Rename Methods 🔄

[Section titled “Span: Rename Methods 🔄”](#span-rename-methods)

The following Span methods are renamed accordingly to the Rust method naming conventions.

Deprecated usage:

- `Span::to_centered_line`
- `Span::to_left_aligned_line`
- `Span::to_right_aligned_line`

New usage:

- `Span::into_centered_line`
- `Span::into_left_aligned_line`
- `Span::into_right_aligned_line`

* * *

We are happy to share that we have received a funding donation from [Radicle](https://radicle.xyz)!

You can read about the details [here](https://blog.orhun.dev/open-source-funding-with-ratatui).

* * *

- Marked various functions as const ([#951](https://github.com/ratatui/ratatui/pull/951))
- Respect alignment on Line truncation ([#987](https://github.com/ratatui/ratatui/pull/987))
- Don’t render scrollbar on zero length track ([#964](https://github.com/ratatui/ratatui/pull/964))
- Fix panic when rendering Text out of bounds ([#997](https://github.com/ratatui/ratatui/pull/997))
- Fix highlight\_symbol overflow ([#949](https://github.com/ratatui/ratatui/pull/949))
- Fix Scrollbar thumb not being visible on long lists ([#959](https://github.com/ratatui/ratatui/pull/959))
- Ensure that paragraph correctly renders styled text ([#992](https://github.com/ratatui/ratatui/pull/992))
- Applied clippy (pedantic) suggestions

And lastly, we welcome [@EdJoPaTo](https://github.com/EdJoPaTo) on board as a maintainer! 🥳