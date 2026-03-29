---
title: Block
url: https://ratatui.rs/recipes/widgets/block/
source: crawler
fetched_at: 2026-02-01T21:13:17.183150688-03:00
rendered_js: false
word_count: 105
summary: This document provides a technical overview of the Block widget, explaining how to use it as a structural container with borders, titles, and custom styling in terminal user interfaces.
tags:
    - rust
    - ratatui
    - tui-library
    - block-widget
    - ui-design
    - terminal-graphics
category: reference
---

The `Block` widget serves as a foundational building block for structuring and framing other widgets. It’s essentially a container that can have borders, a title, and other styling elements to enhance the aesthetics and structure of your terminal interface. This page provides an in-depth exploration of the `Block` widget.

The simplest use case for a `Block` is to create a container with borders:

```

letb= Block::default()
.borders(Borders::ALL);
f.render_widget(b, chunks[0]);
```

A common use case for Block is to give a section of the UI a title or a label:

```

letb= Block::default()
.title("Header")
.borders(Borders::ALL);
f.render_widget(b, chunks[0]);
```

You can also use the `Line` struct for better positioning or multiple titles.

```

letb= Block::default()
.title(Line::from("Left Title").left_aligned())
.title(Line::from("Middle Title").centered())
.title(Line::from("Right Title").right_aligned())
.borders(Borders::ALL);
f.render_widget(b, chunks[0]);
```

Block provides flexibility in both the borders style and type:

```

letb= Block::default()
.title("Styled Header")
.border_style(Style::default().fg(Color::Magenta))
.border_type(BorderType::Rounded)
.borders(Borders::ALL);
f.render_widget(b, chunks[0]);
```