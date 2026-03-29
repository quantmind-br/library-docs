---
title: Ratatui Logo
url: https://ratatui.rs/examples/apps/ratatui-logo/
source: crawler
fetched_at: 2026-02-01T21:12:42.900613394-03:00
rendered_js: false
word_count: 195
summary: This document provides a code example for rendering the Ratatui logo in a terminal using half-block graphics and built-in library widgets.
tags:
    - rust
    - ratatui
    - terminal-graphics
    - ui-widgets
    - code-example
    - terminal-ui
category: tutorial
---

A fun example of using half blocks to render graphics.

```

gitclonehttps://github.com/ratatui/ratatui.git--branchlatest
cdratatui
cargorun--example=ratatui-logo--features=crossterm
```

![ratatui-logo](https://ratatui.rs/_astro/ratatui-logo.sepLfHjm_Zzmtti.webp)

```

//! # [Ratatui] Logo example
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
use std::env::args;
use color_eyre::Result;
use crossterm::event::{self, Event};
use ratatui::{
layout::{Constraint, Layout},
widgets::{RatatuiLogo, RatatuiLogoSize},
DefaultTerminal, TerminalOptions, Viewport,
};
fnmain() -> Result<()> {
color_eyre::install()?;
letterminal= ratatui::init_with_options(TerminalOptions {
viewport: Viewport::Inline(3),
});
letsize=matchargs().nth(1).as_deref() {
Some("small") => RatatuiLogoSize::Small,
Some("tiny") => RatatuiLogoSize::Tiny,
_=> RatatuiLogoSize::default(),
};
letresult=run(terminal, size);
ratatui::restore();
println!();
result
}
fnrun(mutterminal: DefaultTerminal, size: RatatuiLogoSize) -> Result<()> {
loop {
terminal.draw(|frame| {
use Constraint::{Fill, Length};
let [top, bottom] = Layout::vertical([Length(1), Fill(1)]).areas(frame.area());
frame.render_widget("Powered by", top);
frame.render_widget(RatatuiLogo::new(size), bottom);
})?;
ifmatches!(event::read()?, Event::Key(_)) {
break Ok(());
}
}
}
```