---
title: Minimal Hello World
url: https://ratatui.rs/examples/apps/minimal/
source: crawler
fetched_at: 2026-02-01T21:12:41.684519258-03:00
rendered_js: false
word_count: 201
summary: This document provides a minimal starter example for building terminal user interfaces with the Ratatui library in Rust, demonstrating basic terminal initialization and frame rendering.
tags:
    - rust
    - ratatui
    - terminal-ui
    - hello-world
    - crossterm
    - tui-development
category: tutorial
---

Demonstrates a minimal hello world. Source [minimal.rs](https://github.com/ratatui/ratatui/blob/main/examples/apps/minimal/src/main.rs).

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=minimal--features=crossterm
```

![minimal](https://ratatui.rs/_astro/minimal.Hy-GBu8d_Uqmyb.webp)

```

//! # [Ratatui] Minimal example
//!
//! This is a bare minimum example. There are many approaches to running an application loop, so
//! this is not meant to be prescriptive. See the [examples] folder for more complete examples.
//! In particular, the [hello-world] example is a good starting point.
//!
//! [examples]: https://github.com/ratatui-org/ratatui/blob/main/examples
//! [hello-world]: https://github.com/ratatui-org/ratatui/blob/main/examples/hello_world.rs
//!
//! The latest version of this example is available in the [examples] folder in the repository.
//!
//! Please note that the examples are designed to be run against the `main` branch of the Github
//! repository. This means that you may not be able to compile with the latest release version on
//! crates.io, or the one that you have installed locally.
//!
//! See the [examples readme] for more information on finding examples that match the version of the
//! library you are using.
//!
//! [Ratatui]: https://github.com/ratatui/ratatui
//! [examples]: https://github.com/ratatui/ratatui/blob/main/examples
//! [examples readme]: https://github.com/ratatui/ratatui/blob/main/examples/README.md
use crossterm::event::{self, Event};
use ratatui::{text::Text, Frame};
fnmain() {
letmutterminal= ratatui::init();
loop {
terminal.draw(draw).expect("failed to draw frame");
ifmatches!(event::read().expect("failed to read event"), Event::Key(_)) {
break;
}
}
ratatui::restore();
}
fndraw(frame:&mut Frame) {
lettext= Text::raw("Hello World!");
frame.render_widget(text, frame.area());
}
```