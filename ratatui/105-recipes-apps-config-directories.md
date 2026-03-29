---
title: Handle XDG Directories
url: https://ratatui.rs/recipes/apps/config-directories/
source: crawler
fetched_at: 2026-02-01T21:13:08.956152801-03:00
rendered_js: false
word_count: 310
summary: This document explains how to implement standardized file and directory management in Rust CLI applications using the XDG Base Directory Specification and the directories-rs library.
tags:
    - rust
    - xdg-base-directory
    - directories-rs
    - cli-development
    - file-handling
    - configuration-management
category: guide
---

Handling files and directories correctly in a command-line or TUI application ensures that the application fits seamlessly into a user’s workflow and adheres to established conventions. One of the key conventions on Linux-based systems is the XDG Base Directory Specification.

## Why the XDG Base Directory Specification?

[Section titled “Why the XDG Base Directory Specification?”](#why-the-xdg-base-directory-specification)

The XDG Base Directory Specification is a set of standards that define where user files should reside, ensuring a cleaner home directory and a more organized storage convention. By adhering to this standard, your application will store files in the expected directories, making it more predictable and user-friendly.

## Using `directories-rs` for Path Resolution

[Section titled “Using directories-rs for Path Resolution”](#using-directories-rs-for-path-resolution)

The `directories-rs` library offers a Rust-friendly interface to locate common directories (like config and data directories) based on established conventions, including the XDG Base Directory Specification.

1. Add `directories-rs` to your `Cargo.toml`
2. Use the `ProjectDirs` struct to retrieve paths based on your project’s domain and project name and create helper functions for getting the `data_dir` and `config_dir`.
3. Allow users to specify custom locations using environment variables. This flexibility can be crucial for users with unique directory structures or for testing.
4. A good practice is to notify the user about the location of the configuration and data directories. An example from the template is to print out these locations when the user invokes the `--version` command-line argument. See the section on [Command line argument parsing](https://ratatui.rs/recipes/apps/cli-arguments/)

Here’s an example `get_data_dir()` and `get_config_dir()` functions for your reference:

```

use std::path::PathBuf;
use color_eyre::eyre::{self, WrapErr};
use directories::ProjectDirs;
pubfnget_data_dir() -> eyre::Result<PathBuf> {
letdirectory=iflet Ok(s) = std::env::var("RATATUI_TEMPLATE_DATA") {
PathBuf::from(s)
} elseiflet Some(proj_dirs) = ProjectDirs::from("com", "kdheepak", "ratatui-template") {
proj_dirs.data_local_dir().to_path_buf()
} else {
return Err(eyre::eyre!("Unable to find data directory for ratatui-template"));
};
Ok(directory)
}
pubfnget_config_dir() -> eyre::Result<PathBuf> {
letdirectory=iflet Ok(s) = std::env::var("RATATUI_TEMPLATE_CONFIG") {
PathBuf::from(s)
} elseiflet Some(proj_dirs) = ProjectDirs::from("com", "kdheepak", "ratatui-template") {
proj_dirs.config_local_dir().to_path_buf()
} else {
return Err(eyre::eyre!("Unable to find config directory for ratatui-template"));
};
Ok(directory)
}
```

You will want to replace `kdheepak` with your user name or company name (or any unique name for that matter); and `ratatui-app` with the name of your CLI.

I own [https://kdheepak.com](https://kdheepak.com) so I tend to use `com.kdheepak.ratatui-app` for my project directories. That way it is unlikely that any other program will mess with the configuration files for the app I plan on distributing.