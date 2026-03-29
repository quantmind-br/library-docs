---
title: Action.rs
url: https://ratatui.rs/templates/component/action-rs/
source: crawler
fetched_at: 2026-02-01T21:13:28.152128929-03:00
rendered_js: false
word_count: 29
summary: This document defines a Rust enumeration representing various application actions and events used for state management and messaging.
tags:
    - rust
    - enum-definition
    - event-handling
    - message-passing
    - boilerplate
    - state-management
category: reference
---

Defines the `Action` enum that represents actions that can be performed by the app.

These are also typically called `Action`s or `Message`s.

```

pubenum Action {
Tick,
Render,
Resize(u16, u16),
Suspend,
Resume,
Quit,
ClearScreen,
Error(String),
Help,
}
```

Full code for the `action.rs` file is:

```

use serde::{Deserialize, Serialize};
use strum::Display;
#[derive(Debug, Clone, PartialEq, Eq, Display, Serialize, Deserialize)]
pubenum Action {
Tick,
Render,
Resize(u16, u16),
Suspend,
Resume,
Quit,
ClearScreen,
Error(String),
Help,
}
```