---
title: Styling Text
url: https://ratatui.rs/recipes/render/style-text/
source: crawler
fetched_at: 2026-02-01T21:13:13.804962658-03:00
rendered_js: false
word_count: 175
summary: This document explains how to use the Ratatui Style struct to apply colors and text modifiers like bold or italic to terminal UI components.
tags:
    - ratatui
    - rust
    - terminal-ui
    - styling
    - colors
    - text-formatting
category: tutorial
---

Styling enhances user experience by adding colors, emphasis, and other visual aids. In `ratatui`, the primary tool for this is the `ratatui::style::Style` struct.

`ratatui::style::Style` provides a set of methods to apply styling attributes to your text. These styles can then be applied to various text structures like `Text`, `Span`, and `Line` (as well as other non text structures).

Common styling attributes include:

- Foreground and Background Colors (`fg` and `bg`)
- Modifiers (like `bold`, `italic`, and `underline`)

<!--THE END-->

1. Basic Color Styling
   
   Setting the foreground (text color) and background:
   
   ```
   
   letstyled_text= Span::styled(
   "Hello, Ratatui!",
   Style::default().fg(Color::Red).bg(Color::Yellow)
   );
   ```
2. Using `Modifiers`
   
   Making text bold or italic:
   
   ```
   
   letbold_text= Span::styled(
   "This is bold",
   Style::default().add_modifier(Modifier::BOLD)
   );
   letitalic_text= Span::styled(
   "This is italic",
   Style::default().add_modifier(Modifier::ITALIC)
   );
   ```
   
   You can also combine multiple modifiers:
   
   ```
   
   letbold_italic_text= Span::styled(
   "This is bold and italic",
   Style::default().add_modifier(Modifier::BOLD| Modifier::ITALIC)
   );
   ```
3. Styling within a Line
   
   You can mix and match different styled spans within a single line:
   
   ```
   
   letmixed_line= Line::from(vec![
   Span::styled("This is mixed", Style::default().fg(Color::Green)),
   Span::styled("styling", Style::default().fg(Color::Red).add_modifier(Modifier::BOLD)),
   Span::from("!"),
   ]);
   ```

This is what it would look like if you rendered a `Paragraph` with different styles for each line:

```

fnui(_:&App, f:&mut Frame) {
letstyled_text= Span::styled("Hello, Ratatui!", Style::default().fg(Color::Red).bg(Color::Yellow));
letbold_text= Span::styled("This is bold", Style::default().add_modifier(Modifier::BOLD));
letitalic_text= Span::styled("This is italic", Style::default().add_modifier(Modifier::ITALIC));
letbold_italic_text=
Span::styled("This is bold and italic", Style::default().add_modifier(Modifier::BOLD| Modifier::ITALIC));
letmixed_line=vec![
Span::styled("This is mixed", Style::default().fg(Color::Green)),
Span::styled("styling", Style::default().fg(Color::Red).add_modifier(Modifier::BOLD)),
Span::from("!"),
];
lettext: Vec<Line<'_>> =
vec![styled_text.into(), bold_text.into(), italic_text.into(), bold_italic_text.into(), mixed_line.into()];
f.render_widget(Paragraph::new(text).block(Block::default().borders(Borders::ALL)), f.area());
}
```

Here’s the HTML representation of the above styling:

Hello, Ratatui!

This is bold

This is italic

This is bold and italic

This is mixed styling !

You can read more about the [`Color` enum](https://docs.rs/ratatui/latest/ratatui/style/enum.Color.html) and [`Modifier`](https://docs.rs/ratatui/latest/ratatui/style/struct.Modifier.html) in the reference documentation online.