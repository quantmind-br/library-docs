---
title: Displaying Text
url: https://ratatui.rs/recipes/render/display-text/
source: crawler
fetched_at: 2026-02-01T21:13:13.328038991-03:00
rendered_js: false
word_count: 421
summary: This document explains the core building blocks for rendering and styling text in Ratatui, specifically focusing on the Span, Line, and Text structs.
tags:
    - ratatui
    - rust-tui
    - text-rendering
    - terminal-ui
    - styling
    - ui-development
category: guide
---

This page covers how text displaying works. It will cover `Span`, `Line`, and `Text`, and how these can be created, styled, displayed, altered, and such.

A `Span` is a styled segment of text. You can think of it as a substring with its own unique style. It is the most basic unit of displaying text in `ratatui`.

The examples below assume the following imports:

```

use ratatui::{prelude::*, widgets::*};
```

A `Span` consists of “content” and a “style” for the content. And a `Span` can be created in a few different ways.

1. using `Span::raw`:
   
   ```
   
   fnui(_app:&App, f:&mut Frame) {
   letspan= Span::raw("This is text that is not styled");
   // --snip--
   }
   ```
2. using `Span::styled`:
   
   ```
   
   fnui(_app:&App, f:&mut Frame) {
   letspan= Span::styled("This is text that will be yellow", Style::default().fg(Color::Yellow));
   // --snip--
   }
   ```
3. using the `Stylize` trait:
   
   ```
   
   fnui(_app:&App, f:&mut Frame) {
   letspan="This is text that will be yellow".yellow();
   // --snip--
   }
   ```

A `Span` is the basic building block for any styled text, and can be used anywhere text is displayed.

The next building block that we are going to talk about is a `Line`. A `Line` represents a cluster of graphemes, where each unit in the cluster can have its own style. You can think of an instance of the `Line` struct as essentially a collection of `Span` objects, i.e. `Vec<Span>`.

Since each `Line` struct consists of multiple `Span` objects, this allows for varied styling in a row of words, phrases or sentences.

```

fnui(_:&App, f:&mut Frame) {
letline= Line::from(vec![
"hello".red(),
"".into(),
"world".red().bold()
]);
// --snip--
}
```

A `Line` can be constructed directly from content, where the content is `Into<Cow<'a, &str>>`.

```

fnui(_:&App, f:&mut Frame) {
letline= Line::from("hello world");
// --snip--
}
```

You can even style a full line directly:

```

fnui(_:&App, f:&mut Frame) {
letline= Line::styled("hello world", Style::default().fg(Color::Yellow));
// --snip--
}
```

And you can use the `Stylize` trait on the line directly by using `into()`:

```

fnui(_:&App, f:&mut Frame) {
letline: Line ="hello world".yellow().into();
// --snip--
}
```

Finally, you can also align it using `alignment()` or the shorthand methods `left_aligned()`, `centered()` and `right_aligned()`. Widgets using `Line` internally will generally respect this.

```

fnui(_:&App, f:&mut Frame) {
letline= Line::from("hello world").alignment(Alignment::Center);
letline= Line::from("hello world").centered(); // shorthand
// --snip--
}
```

`Text` is the final building block of outputting text. A `Text` object represents a collection of `Line`s.

Most widgets accept content that can be converted to `Text`.

```

fnui(_:&App, f:&mut Frame) {
letspan1="hello".red();
letspan2="world".red().bold();
letline= Line::from(vec![span1, "".into(), span2]);
lettext= Text::from(line);
f.render_widget(Paragraph::new(text).block(Block::bordered()), f.area());
}
```

Here’s an HTML representation of what you’d get in the terminal:

hello world

Often code like the one above can be simplified:

```

fnui(_:&App, f:&mut Frame) {
letline: Line =vec![
"hello".red(),
"".into(),
"world".red().bold()
].into();
f.render_widget(Paragraph::new(line).block(Block::bordered()), f.area());
}
```

This is because in this case, Rust is able to infer the types and convert them appropriately.

`Text` instances can be created using the `raw` or `styled` constructors too.

Something that you might find yourself doing pretty often for a `Paragraph` is wanting to have multiple lines styled differently. This is one way you might go about that:

```

fnui(_:&App, f:&mut Frame) {
lettext=vec![
"hello world 1".into(),
"hello world 2".blue().into(),
Line::from(vec!["hello".green(), "".into(), "world".green().bold(), "3".into()]),
];
f.render_widget(Paragraph::new(text).block(Block::bordered()), f.area());
}
```

hello world 1

hello world 2

hello world 3

We will talk more about styling in the next section.

As with `Line`, a `Text` can be aligned with `alignment()` or the shorthand methods `left_aligned()`, `centered()` and `right_aligned()`. Widgets using `Text` internally will generally respect this. Note in the example below, you can override the alignment for a particular line.

```

fnui(_:&App, f:&mut Frame) {
lettext= Text::from(vec![
Line::from("hello world 1").left_aligned(),
Line::from("hello world 2"),
Line::from("hello world 3").right_aligned(),
]).centered();
f.render_widget(Paragraph::new(text).block(Block::bordered()), f.area());
}
```

hello world 1

hello world 2

hello world 3