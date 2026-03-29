---
title: Hello Ratatui
url: https://ratatui.rs/tutorials/hello-ratatui/
source: crawler
fetched_at: 2026-02-01T21:12:32.259438026-03:00
rendered_js: false
word_count: 484
summary: A step-by-step tutorial for creating a basic 'Hello World' terminal user interface application using Rust and the Ratatui library.
tags:
    - ratatui
    - rust
    - tui
    - terminal-ui
    - hello-world
    - cargo-generate
category: tutorial
---

This tutorial will lead you through creating a simple “Hello World” TUI app that displays some text in the top-left corner of the screen and waits for the user to press any key to exit. It demonstrates the tasks that any application developed with Ratatui needs to undertake.

We assume you have a basic understanding of the terminal, and have a text editor or IDE. If you don’t have a preference, [VSCode](https://code.visualstudio.com/) with [rust-analyzer](https://marketplace.visualstudio.com/items?itemName=rust-lang.rust-analyzer) makes a good default choice.

First install Rust if it is not already installed. See the [Installation](https://doc.rust-lang.org/book/ch01-01-installation.html) section of the official Rust Book for more information. Most people use `rustup`, a command line tool for managing Rust versions and associated tools. Ratatui requires at least Rust 1.74, but it’s generally a good idea to work with the latest stable version if you can. Once you’ve installed Rust, verify it’s installed by running:

You should see output similar to the following (the exact version, date and commit hash will vary):

```

rustc 1.83.0 (90b35a623 2024-11-26)
```

### Install Cargo generate

[Section titled “Install Cargo generate”](#install-cargo-generate)

Ratatui has a few templates that make it easy to get started with a new project. [Cargo generate](https://cargo-generate.github.io/cargo-generate/) is a developer tool to help you get up and running quickly with a new Rust project by leveraging a pre-existing git repository as a template. We will use it to create a new Ratatui project.

Install `cargo-generate` by running the following command (or see the [installation instructions](https://cargo-generate.github.io/cargo-generate/installation.html) for other approaches to installing cargo-generate.)

```

cargoinstallcargo-generate
```

## Create a New Project

[Section titled “Create a New Project”](#create-a-new-project)

Let’s create a new Rust project. In the terminal, navigate to a folder where you will store your projects and run the following command to generate a new app using the simple ratatui template. (You can find more information about this template in the [Hello World Template README](https://github.com/ratatui/templates/blob/main/hello-world/README.md))

```

cargogenerateratatui/templateshello-world
```

You will be prompted for a project name to use. Enter `hello-ratatui`.

```

$cargogenerateratatui/templates
⚠️Favorite`ratatui/templates`notfoundinconfig,usingitasagitrepository:https://github.com/ratatui/templates.git
✔🤷Whichsub-templateshouldbeexpanded?·hello-world
🤷ProjectName:hello-ratatui
🔧Destination:/Users/joshka/local/ratatui-website/code/tutorials/hello-ratatui...
🔧project-name:hello-ratatui...
🔧Generatingtemplate...
🤷Shortdescriptionoftheproject:ARatatuiHelloWorldapp
🔧Movinggeneratedfilesinto:`/Users/joshka/local/ratatui-website/code/tutorials/hello-ratatui`...
🔧InitializingafreshGitrepository
✨Done!Newprojectcreated/Users/joshka/local/ratatui-website/code/tutorials/hello-ratatui
```

### Examine the Project

[Section titled “Examine the Project”](#examine-the-project)

The `cargo generate` command creates a new folder called `hello-ratatui` with a basic binary application in it. If you examine the folders and files created this will look like:

```

hello-ratatui/
├── src/
│  └── main.rs
├── Cargo.toml
├── LICENSE
└── README.md
```

The `Cargo.toml` file is filled with some default values and the necessary dependencies (Ratatui and Crossterm), and one useful dependency (Color-eyre) for nicer error handling.

```

[package]
name="hello-ratatui"
version="0.1.0"
description="A Ratatui Hello World app"
authors= ["Josh McKinney <[email protected]>"]
license="MIT"
edition="2024"
[dependencies]
color-eyre="0.6.3"
crossterm="0.29.0"
ratatui="0.30.0"
# Read theoptimizationguidelineformoredetails:https://ratatui.rs/recipes/apps/release-your-app/#optimizations
[profile.release]
codegen-units=1
lto=true
opt-level="s"
strip=true
```

The generate command created a default `main.rs` that runs the app:

```

use ratatui::{DefaultTerminal, Frame};
fnmain() -> color_eyre::Result<()> {
color_eyre::install()?;
ratatui::run(app)?;
Ok(())
}
fnapp(terminal:&mut DefaultTerminal) -> std::io::Result<()> {
loop {
terminal.draw(render)?;
if crossterm::event::read()?.is_key_press() {
break Ok(());
}
}
}
fnrender(frame:&mut Frame) {
frame.render_widget("hello world", frame.area());
}
```

Let’s build and execute the project. Run:

```

cdhello-ratatui
cargorun
```

You should see the build output and then a TUI app with a `Hello world` message.

![hello](https://ratatui.rs/_astro/hello-ratatui.BUSC3RMX_Z16g3cK.webp)

You can press any key to exit and go back to your terminal as it was before.

Congratulations! 🎉 You have written a “hello world” terminal user interface with Ratatui. The next sections will go into more detail about how Ratatui works.

The next tutorial, [Counter App](https://ratatui.rs/tutorials/counter-app/), introduces some more interactivity, and a more robust approach to arranging your application code.