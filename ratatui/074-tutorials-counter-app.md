---
title: Counter App
url: https://ratatui.rs/tutorials/counter-app/
source: crawler
fetched_at: 2026-02-01T21:12:33.98970047-03:00
rendered_js: false
word_count: 100
summary: This tutorial teaches how to manage application state and handle user keyboard input to create interactive terminal user interfaces using the Ratatui library.
tags:
    - ratatui
    - rust
    - tui
    - state-management
    - event-handling
    - terminal-ui
    - widgets
category: tutorial
---

The previous [Hello Ratatui](https://ratatui.rs/tutorials/hello-ratatui) tutorial introduced how to create a simple TUI that displayed some text and waited for the user to press a key. This tutorial will cover how to handle state and some more complex interactions. You will build a counter application that allows the user to increment and decrement a value on the screen.

When you’re finished the application will look like the following:

![basic-app demo](https://ratatui.rs/_astro/basic-app.Ct70-NG2_9Kk2v.webp)

The application will render the counter in a [`Paragraph`](https://docs.rs/ratatui/latest/ratatui/widgets/struct.Paragraph.html) widget. When the user presses the left and right arrow keys, the application will increment and decrement the value of the counter.