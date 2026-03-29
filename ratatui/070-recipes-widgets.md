---
title: Use Widgets
url: https://ratatui.rs/recipes/widgets/
source: crawler
fetched_at: 2026-02-01T21:13:17.488367996-03:00
rendered_js: false
word_count: 68
summary: This document introduces the concept of widgets in Ratatui, explaining how they implement specific traits for terminal rendering and providing links to further documentation for built-in and custom types.
tags:
    - ratatui
    - rust
    - widgets
    - terminal-ui
    - ui-components
    - stateful-widget
category: concept
---

Widgets are types that implement the [`Widget`](https://docs.rs/ratatui/latest/ratatui/widgets/trait.Widget.html) or [`StatefulWidget`](https://docs.rs/ratatui/latest/ratatui/widgets/trait.StatefulWidget.html) trait which allows applications to render them to a terminal.

The following pages document how to use the following widgets:

- [Block](https://ratatui.rs/recipes/widgets/block/)
- [Paragraph](https://ratatui.rs/recipes/widgets/paragraph/)
- [Custom Widgets](https://ratatui.rs/recipes/widgets/custom/)

There are more widgets available than just the above list. The crate docs document all the built-in widgets. See the [`widgets` module](https://docs.rs/ratatui/latest/ratatui/widgets/index.html) for a list. There are also [Third Party Crates](https://ratatui.rs/showcase/third-party-widgets) that implement more widgets.