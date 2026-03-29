---
title: Cli.rs
url: https://ratatui.rs/templates/component/cli-rs/
source: crawler
fetched_at: 2026-02-01T21:13:35.6924501-03:00
rendered_js: false
word_count: 25
summary: This document demonstrates how to define command-line arguments and display application version metadata using the clap crate in a Rust project.
tags:
    - rust
    - clap-crate
    - cli-parsing
    - command-line-interface
    - rust-development
category: reference
---

The `cli.rs` file is where we define the command line arguments for our app.

```

use clap::Parser;
usecrate::config::{get_config_dir, get_data_dir};
#[derive(Parser, Debug)]
#[command(author, version = version(), about)]
pubstruct Cli {
/// Tick rate, i.e. number of ticks per second
#[arg(short, long, value_name ="FLOAT", default_value_t = 4.0)]
pubtick_rate: f64,
/// Frame rate, i.e. number of frames per second
#[arg(short, long, value_name ="FLOAT", default_value_t = 60.0)]
pubframe_rate: f64,
}
constVERSION_MESSAGE:&str =concat!(
env!("CARGO_PKG_VERSION"),
"-",
env!("VERGEN_GIT_DESCRIBE"),
" (",
env!("VERGEN_BUILD_DATE"),
")"
);
pubfnversion() -> String {
letauthor= clap::crate_authors!();
// let current_exe_path = PathBuf::from(clap::crate_name!()).display().to_string();
letconfig_dir_path=get_config_dir().display().to_string();
letdata_dir_path=get_data_dir().display().to_string();
format!(
"\
{VERSION_MESSAGE}
Authors: {author}
Config directory: {config_dir_path}
Data directory: {data_dir_path}"
)
}
```

It uses the `clap` crate to define the command line interface.