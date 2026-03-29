---
title: Installation
url: https://ratatui.rs/installation/
source: crawler
fetched_at: 2026-02-01T21:12:27.693839813-03:00
rendered_js: false
word_count: 70
summary: This document provides instructions for installing the ratatui Rust crate and configuring its optional backend features using Cargo.
tags:
    - rust
    - ratatui
    - installation
    - cargo
    - dependencies
    - terminal-ui
    - backend-configuration
category: guide
---

`ratatui` is a standard rust crate and can be installed into your app using the following command:

or by adding the following to your `Cargo.toml` file:

```

[dependencies]
ratatui = "0.30.0"
```

By default, `ratatui` enables the `crossterm` feature, but it’s possible to alternatively use `termion`, or `termwiz` instead by enabling the appropriate feature and disabling the default features. See [Backend](https://ratatui.rs/concepts/backends/) for more information.

For Termion:

```

cargoaddratatui--no-default-features--featurestermion
```

or in your `Cargo.toml`:

```

[dependencies]
ratatui = { version = "0.30.0", default-features = false, features = ["termion"] }
```

For Termwiz:

```

cargoaddratatui--no-default-features--featurestermwiz
```

or in your `Cargo.toml`:

```

[dependencies]
ratatui = { version = "0.30.0", default-features = false, features = ["termwiz"] }
```