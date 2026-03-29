---
title: Component Architecture
url: https://ratatui.rs/concepts/application-patterns/component-architecture/
source: crawler
fetched_at: 2026-02-01T21:13:02.693777162-03:00
rendered_js: false
word_count: 249
summary: This document explains the component-based architectural pattern for organizing terminal user interfaces, detailing how to encapsulate state, event handling, and rendering within modular traits.
tags:
    - tui-architecture
    - ratatui
    - component-pattern
    - rust
    - design-patterns
    - state-management
category: concept
---

If you are interested in a more object oriented approach to organizing TUIs, you can use a `Component` based approach.

A couple of projects in the wild use this approach

- [https://github.com/TaKO8Ki/gobang](https://github.com/TaKO8Ki/gobang)
- [https://github.com/nomadiz/edma](https://github.com/nomadiz/edma)

We also have a `component` template that has an example of this `Component` based approach:

- [https://github.com/ratatui/templates/tree/main/component](https://github.com/ratatui/templates/tree/main/component)

We already covered [TEA](https://ratatui.rs/concepts/application-patterns/the-elm-architecture/) in the previous section. The `Component` architecture takes a slightly more object oriented trait based approach.

Each component encapsulates its own state, event handlers, and rendering logic.

1. Component Initialization (`init`) - This is where a component can set up any initial state or resources it needs. It’s a separate process from handling events or rendering.
2. Event Handling (`handle_events`, `handle_key_events`, `handle_mouse_events`) - Each component has its own event handlers. This allows for a finer-grained approach to event handling, with each component only dealing with the events it’s interested in. This contrasts with Elm’s single update function that handles messages for the entire application.
3. State Update (`update`) - Components can have their own local state and can update it in response to actions. This state is private to the component, which differs from Elm’s global model.
4. Rendering (`render`) - Each component defines its own rendering logic. It knows how to draw itself, given a rendering context. This is similar to Elm’s view function but on a component-by-component basis.

Here’s an example of the `Component` trait implementation you might use:

```

use color_eyre::eyre::Result;
use ratatui::crossterm::event::{KeyEvent, MouseEvent};
use ratatui::layout::Rect;
usecrate::{action::Action, event::Event, terminal::Frame};
pubtrait Component {
fninit(&mutself) -> Result<()> {
Ok(())
}
fnhandle_events(&mutself, event: Option<Event>) -> Action {
matchevent {
Some(Event::Quit) => Action::Quit,
Some(Event::Tick) => Action::Tick,
Some(Event::Key(key_event)) =>self.handle_key_events(key_event),
Some(Event::Mouse(mouse_event)) =>self.handle_mouse_events(mouse_event),
Some(Event::Resize(x, y)) => Action::Resize(x, y),
Some(_) => Action::Noop,
None => Action::Noop,
}
}
fnhandle_key_events(&mutself, key: KeyEvent) -> Action {
Action::Noop
}
fnhandle_mouse_events(&mutself, mouse: MouseEvent) -> Action {
Action::Noop
}
fnupdate(&mutself, action: Action) -> Action {
Action::Noop
}
fnrender(&mutself, f:&mut Frame, rect: Rect);
}
```

One advantage of this approach is that it incentivizes co-locating the `handle_events`, `update` and `render` functions on a component level.