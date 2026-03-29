---
title: JSON Editor
url: https://ratatui.rs/tutorials/json-editor/
source: crawler
fetched_at: 2026-02-01T21:12:35.015953477-03:00
rendered_js: false
word_count: 161
summary: This tutorial guides users through building a terminal-based JSON editor using Ratatui, focusing on state management and modular application architecture in Rust.
tags:
    - rust
    - ratatui
    - tui
    - json-editor
    - serde
    - state-management
category: tutorial
---

Now that we have covered some of the basics of a [Hello Ratatui](https://ratatui.rs/tutorials/hello-ratatui) and [Counter](https://ratatui.rs/tutorials/counter-app) apps, we are ready to build and manage something more involved.

In this tutorial, we will be creating an application that gives the user a simple interface to enter key-value pairs, which will be converted and printed to `stdout` in json. The purpose of this application will be to give the user an interface to create correct json, instead of having to worry about commas and brackets themselves.

Here’s a gif of what it will look like if you run this:

![Demo](https://vhs.charm.sh/vhs-5VaEPLZP2OlOxPPAIiLqbF.gif)

Go ahead and set up a new rust project with

```

cargonewratatui-json-editor
```

and put the following in the `Cargo.toml`:

```

[dependencies]
ratatui = "0.29.0"
serde = { version = "1.0.219", features = ["derive"] }
serde_json = "1.0.140"
```

or the latest version of these libraries.

Now create two files inside of `src/` so it looks like this:

```

src
├── main.rs
├── ui.rs
└── app.rs
```

This follows a common approach to small applications in `ratatui`, where we have a state file, a UI file, and the main file to tie it all together.