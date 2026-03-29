---
title: Feature Flags
url: https://ratatui.rs/installation/feature-flags/
source: crawler
fetched_at: 2026-02-01T21:12:32.594124806-03:00
rendered_js: false
word_count: 121
summary: This document explains how to configure the Ratatui library by selecting specific terminal backends and enabling optional features like the calendar widget and Serde support.
tags:
    - ratatui
    - rust
    - terminal-ui
    - cargo-features
    - backend-selection
    - serde
    - widgets
category: configuration
---

As ratatui grows and evolves, this list may change, so make sure to check the [main repo](https://github.com/ratatui/ratatui) if you are unsure.

## Backend Selection

[Section titled “Backend Selection”](#backend-selection)

For most cases, the default `crossterm` backend is the correct choice. See [Backends](https://ratatui.rs/concepts/backends/) for more information. However, this can be changed to termion or termwiz

```

# Defaults to crossterm
cargoaddratatui
# For termion, unset the default crossterm feature and select the termion feature
cargoaddratatui--no-default-features--features=termion
cargoaddtermion
# For termwiz, unset the default crossterm feature and select the termwiz feature
cargoaddratatui--no-default-features--features=termwiz
cargoaddtermwiz
```

As of v0.21, the only widget in this feature group is the `calendar` widget, which can be enabled with the `widget-calendar` feature.

```

cargoaddratatui--no-default-features--features=all-widgets
```

This feature enables the calendar widget, which requires the `time` crate. It is enabled by default as part of the `all-widgets` feature.

```

cargoaddratatui--no-default-features--features=widget-calendar
```

Enables serialization and deserialization of style and color types using the Serde crate. This is useful if you want to save themes to a file.

```

cargoaddratatui--featuresserde
```