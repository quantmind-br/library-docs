---
title: Paragraph
url: https://ratatui.rs/recipes/widgets/paragraph/
source: crawler
fetched_at: 2026-02-01T21:13:18.129623917-03:00
rendered_js: false
word_count: 123
summary: This document explains how to use the Paragraph widget to display and format text in a terminal user interface, covering features like styling, alignment, and scrolling.
tags:
    - tui
    - paragraph-widget
    - text-styling
    - terminal-ui
    - rust-programming
    - rich-text
category: guide
---

The `Paragraph` widget provides a way to display text content in your terminal user interface. It allows not only plain text display but also handling text wrapping, alignment, and styling. This page will delve deeper into the functionality of the `Paragraph` widget.

```

letp= Paragraph::new("Hello, World!");
f.render_widget(p, chunks[0]);
```

## Styling and Borders

[Section titled “Styling and Borders”](#styling-and-borders)

You can also apply styles to your text and wrap it with a border:

```

letp= Paragraph::new("Hello, World!")
.style(Style::default().fg(Color::Yellow))
.block(
Block::default()
.borders(Borders::ALL)
.title("Title")
.border_type(BorderType::Rounded)
);
f.render_widget(p, chunks[0]);
```

The `Paragraph` widget will wrap the content based on the available width in its containing block. You can also control the wrapping behavior using the `wrap` method:

```

letp= Paragraph::new("A very long text that might not fit the container...")
.wrap(Wrap { trim:true });
f.render_widget(p, chunks[0]);
```

Setting `trim` to `true` will ensure that trailing whitespaces at the end of each line are removed.

```

letp= Paragraph::new("Centered Text")
.alignment(Alignment::Center);
f.render_widget(p, chunks[0]);
```

`Paragraph` supports rich text through `Span`, `Line`, and `Text`:

```

letmutlines=vec![];
lines.push(Line::from(vec![
Span::styled("Hello ", Style::default().fg(Color::Yellow)),
Span::styled("World", Style::default().fg(Color::Blue).bg(Color::White)),
]));
lines.push(Line::from(vec![
Span::styled("Goodbye ", Style::default().fg(Color::Yellow)),
Span::styled("World", Style::default().fg(Color::Blue).bg(Color::White)),
]));
lettext= Text::from(lines);
letp= Paragraph::new(text);
f.render_widget(p, chunks[0]);
```

For long content, `Paragraph` supports scrolling:

```

letmutp= Paragraph::new("Lorem ipsum ...")
.scroll((1, 0));  // Scroll down by one line
f.render_widget(p, chunks[0]);
```