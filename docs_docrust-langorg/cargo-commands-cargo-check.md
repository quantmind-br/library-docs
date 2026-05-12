---
title: cargo check - The Cargo Book
url: https://doc.rust-lang.org/cargo/commands/cargo-check.html
source: crawler
fetched_at: 2026-05-06T21:25:05.244382349-03:00
rendered_js: false
word_count: 1928
summary: This document provides a reference for the 'cargo check' command, explaining how to use it to analyze local packages and dependencies for errors without performing a full code generation build.
tags:
    - cargo
    - rust
    - command-line-tool
    - package-management
    - development-tools
    - build-optimization
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Cargo Book

## [cargo-check(1)](#cargo-check1)

## [NAME](#name)

cargo-check — Check the current package

## [SYNOPSIS](#synopsis)

`cargo check` \[*options*]

## [DESCRIPTION](#description)

Check a local package and all of its dependencies for errors. This will essentially compile the packages without performing the final step of code generation, which is faster than running `cargo build`. The compiler will save metadata files to disk so that future runs will reuse them if the source has not been modified. Some diagnostics and errors are only emitted during code generation, so they inherently won’t be reported with `cargo check`.

## [OPTIONS](#options)

### [Package Selection](#package-selection)

By default, when no package selection options are given, the packages selected depend on the selected manifest file (based on the current working directory if `--manifest-path` is not given). If the manifest is the root of a workspace then the workspaces default members are selected, otherwise only the package defined by the manifest will be selected.

The default members of a workspace can be set explicitly with the `workspace.default-members` key in the root manifest. If this is not set, a virtual workspace will include all workspace members (equivalent to passing `--workspace`), and a non-virtual workspace will include only the root crate itself.

[`-p` *spec*…](#option-cargo-check--p)

[`--package` *spec*…](#option-cargo-check---package)

Check only the specified packages. See [cargo-pkgid(1)](https://doc.rust-lang.org/cargo/commands/cargo-pkgid.html) for the SPEC format. This flag may be specified multiple times and supports common Unix glob patterns like `*`, `?` and `[]`. However, to avoid your shell accidentally expanding glob patterns before Cargo handles them, you must use single quotes or double quotes around each pattern.

[`--workspace`](#option-cargo-check---workspace)

Check all members in the workspace.

[`--all`](#option-cargo-check---all)

Deprecated alias for `--workspace`.

[`--exclude` *SPEC*…](#option-cargo-check---exclude)

Exclude the specified packages. Must be used in conjunction with the `--workspace` flag. This flag may be specified multiple times and supports common Unix glob patterns like `*`, `?` and `[]`. However, to avoid your shell accidentally expanding glob patterns before Cargo handles them, you must use single quotes or double quotes around each pattern.

### [Target Selection](#target-selection)

When no target selection options are given, `cargo check` will check all binary and library targets of the selected packages. Binaries are skipped if they have `required-features` that are missing.

Passing target selection flags will check only the specified targets.

Note that `--bin`, `--example`, `--test` and `--bench` flags also support common Unix glob patterns like `*`, `?` and `[]`. However, to avoid your shell accidentally expanding glob patterns before Cargo handles them, you must use single quotes or double quotes around each glob pattern.

[`--lib`](#option-cargo-check---lib)

Check the package’s library.

[`--bin` *name*…](#option-cargo-check---bin)

Check the specified binary. This flag may be specified multiple times and supports common Unix glob patterns.

[`--bins`](#option-cargo-check---bins)

Check all binary targets.

[`--example` *name*…](#option-cargo-check---example)

Check the specified example. This flag may be specified multiple times and supports common Unix glob patterns.

[`--examples`](#option-cargo-check---examples)

Check all example targets.

[`--test` *name*…](#option-cargo-check---test)

Check the specified integration test. This flag may be specified multiple times and supports common Unix glob patterns.

[`--tests`](#option-cargo-check---tests)

Check all targets that have the `test = true` manifest flag set. By default this includes the library and binaries built as unittests, and integration tests. Be aware that this will also build any required dependencies, so the lib target may be built twice (once as a unittest, and once as a dependency for binaries, integration tests, etc.). Targets may be enabled or disabled by setting the `test` flag in the manifest settings for the target.

[`--bench` *name*…](#option-cargo-check---bench)

Check the specified benchmark. This flag may be specified multiple times and supports common Unix glob patterns.

[`--benches`](#option-cargo-check---benches)

Check all targets that have the `bench = true` manifest flag set. By default this includes the library and binaries built as benchmarks, and bench targets. Be aware that this will also build any required dependencies, so the lib target may be built twice (once as a benchmark, and once as a dependency for binaries, benchmarks, etc.). Targets may be enabled or disabled by setting the `bench` flag in the manifest settings for the target.

[`--all-targets`](#option-cargo-check---all-targets)

Check all targets. This is equivalent to specifying `--lib --bins --tests --benches --examples`.

### [Feature Selection](#feature-selection)

The feature flags allow you to control which features are enabled. When no feature options are given, the `default` feature is activated for every selected package.

See [the features documentation](https://doc.rust-lang.org/cargo/reference/features.html#command-line-feature-options) for more details.

[`-F` *features*](#option-cargo-check--F)

[`--features` *features*](#option-cargo-check---features)

Space or comma separated list of features to activate. Features of workspace members may be enabled with `package-name/feature-name` syntax. This flag may be specified multiple times, which enables all specified features.

[`--all-features`](#option-cargo-check---all-features)

Activate all available features of all selected packages.

[`--no-default-features`](#option-cargo-check---no-default-features)

Do not activate the `default` feature of the selected packages.

### [Compilation Options](#compilation-options)

[`--target` *triple*](#option-cargo-check---target)

Check for the specified target architecture. Flag may be specified multiple times. The default is the host architecture. The general format of the triple is `<arch><sub>-<vendor>-<sys>-<abi>`.

Possible values:

- Any supported target in `rustc --print target-list`.
- `"host-tuple"`, which will internally be substituted by the host’s target. This can be particularly useful if you’re cross-compiling some crates, and don’t want to specify your host’s machine as a target (for instance, an `xtask` in a shared project that may be worked on by many hosts).
- A path to a custom target specification. See [Custom Target Lookup Path](https://doc.rust-lang.org/rustc/targets/custom.html#custom-target-lookup-path) for more information.

This may also be specified with the `build.target` [config value](https://doc.rust-lang.org/cargo/reference/config.html).

Note that specifying this flag makes Cargo run in a different mode where the target artifacts are placed in a separate directory. See the [build cache](https://doc.rust-lang.org/cargo/reference/build-cache.html) documentation for more details.

[`-r`](#option-cargo-check--r)

[`--release`](#option-cargo-check---release)

Check optimized artifacts with the `release` profile. See also the `--profile` option for choosing a specific profile by name.

[`--profile` *name*](#option-cargo-check---profile)

Check with the given profile.

As a special case, specifying the `test` profile will also enable checking in test mode which will enable checking tests and enable the `test` cfg option. See [rustc tests](https://doc.rust-lang.org/rustc/tests/index.html) for more detail.

See [the reference](https://doc.rust-lang.org/cargo/reference/profiles.html) for more details on profiles.

[`--timings`](#option-cargo-check---timings)

Output information how long each compilation takes, and track concurrency information over time.

A file `cargo-timing.html` will be written to the `target/cargo-timings` directory at the end of the build. An additional report with a timestamp in its filename is also written if you want to look at a previous run. These reports are suitable for human consumption only, and do not provide machine-readable timing data.

### [Output Options](#output-options)

[`--target-dir` *directory*](#option-cargo-check---target-dir)

Directory for all generated artifacts and intermediate files. May also be specified with the `CARGO_TARGET_DIR` environment variable, or the `build.target-dir` [config value](https://doc.rust-lang.org/cargo/reference/config.html). Defaults to `target` in the root of the workspace.

### [Display Options](#display-options)

[`-v`](#option-cargo-check--v)

[`--verbose`](#option-cargo-check---verbose)

Use verbose output. May be specified twice for “very verbose” output which includes extra output such as dependency warnings and build script output. May also be specified with the `term.verbose` [config value](https://doc.rust-lang.org/cargo/reference/config.html).

[`-q`](#option-cargo-check--q)

[`--quiet`](#option-cargo-check---quiet)

Do not print cargo log messages. May also be specified with the `term.quiet` [config value](https://doc.rust-lang.org/cargo/reference/config.html).

[`--color` *when*](#option-cargo-check---color)

Control when colored output is used. Valid values:

- `auto` (default): Automatically detect if color support is available on the terminal.
- `always`: Always display colors.
- `never`: Never display colors.

May also be specified with the `term.color` [config value](https://doc.rust-lang.org/cargo/reference/config.html).

[`--message-format` *fmt*](#option-cargo-check---message-format)

The output format for diagnostic messages. Can be specified multiple times and consists of comma-separated values. Valid values:

- `human` (default): Display in a human-readable text format. Conflicts with `short` and `json`.
- `short`: Emit shorter, human-readable text messages. Conflicts with `human` and `json`.
- `json`: Emit JSON messages to stdout. See [the reference](https://doc.rust-lang.org/cargo/reference/external-tools.html#json-messages) for more details. Conflicts with `human` and `short`.
- `json-diagnostic-short`: Ensure the `rendered` field of JSON messages contains the “short” rendering from rustc. Cannot be used with `human` or `short`.
- `json-diagnostic-rendered-ansi`: Ensure the `rendered` field of JSON messages contains embedded ANSI color codes for respecting rustc’s default color scheme. Cannot be used with `human` or `short`.
- `json-render-diagnostics`: Instruct Cargo to not include rustc diagnostics in JSON messages printed, but instead Cargo itself should render the JSON diagnostics coming from rustc. Cargo’s own JSON diagnostics and others coming from rustc are still emitted. Cannot be used with `human` or `short`.

### [Manifest Options](#manifest-options)

[`--manifest-path` *path*](#option-cargo-check---manifest-path)

Path to the `Cargo.toml` file. By default, Cargo searches for the `Cargo.toml` file in the current directory or any parent directory.

[`--ignore-rust-version`](#option-cargo-check---ignore-rust-version)

Ignore `rust-version` specification in packages.

[`--locked`](#option-cargo-check---locked)

Asserts that the exact same dependencies and versions are used as when the existing `Cargo.lock` file was originally generated. Cargo will exit with an error when either of the following scenarios arises:

- The lock file is missing.
- Cargo attempted to change the lock file due to a different dependency resolution.

It may be used in environments where deterministic builds are desired, such as in CI pipelines.

[`--offline`](#option-cargo-check---offline)

Prevents Cargo from accessing the network for any reason. Without this flag, Cargo will stop with an error if it needs to access the network and the network is not available. With this flag, Cargo will attempt to proceed without the network if possible.

Beware that this may result in different dependency resolution than online mode. Cargo will restrict itself to crates that are downloaded locally, even if there might be a newer version as indicated in the local copy of the index. See the [cargo-fetch(1)](https://doc.rust-lang.org/cargo/commands/cargo-fetch.html) command to download dependencies before going offline.

May also be specified with the `net.offline` [config value](https://doc.rust-lang.org/cargo/reference/config.html).

[`--frozen`](#option-cargo-check---frozen)

Equivalent to specifying both `--locked` and `--offline`.

### [Common Options](#common-options)

[`+`*toolchain*](#option-cargo-check-+toolchain)

If Cargo has been installed with rustup, and the first argument to `cargo` begins with `+`, it will be interpreted as a rustup toolchain name (such as `+stable` or `+nightly`). See the [rustup documentation](https://rust-lang.github.io/rustup/overrides.html) for more information about how toolchain overrides work.

[`--config` *KEY=VALUE* or *PATH*](#option-cargo-check---config)

Overrides a Cargo configuration value. The argument should be in TOML syntax of `KEY=VALUE`, or provided as a path to an extra configuration file. This flag may be specified multiple times. See the [command-line overrides section](https://doc.rust-lang.org/cargo/reference/config.html#command-line-overrides) for more information.

[`-C` *PATH*](#option-cargo-check--C)

Changes the current working directory before executing any specified operations. This affects things like where cargo looks by default for the project manifest (`Cargo.toml`), as well as the directories searched for discovering `.cargo/config.toml`, for example. This option must appear before the command name, for example `cargo -C path/to/my-project build`.

This option is only available on the [nightly channel](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html) and requires the `-Z unstable-options` flag to enable (see [#10098](https://github.com/rust-lang/cargo/issues/10098)).

[`-h`](#option-cargo-check--h)

[`--help`](#option-cargo-check---help)

Prints help information.

[`-Z` *flag*](#option-cargo-check--Z)

Unstable (nightly-only) flags to Cargo. Run `cargo -Z help` for details.

### [Miscellaneous Options](#miscellaneous-options)

[`-j` *N*](#option-cargo-check--j)

[`--jobs` *N*](#option-cargo-check---jobs)

Number of parallel jobs to run. May also be specified with the `build.jobs` [config value](https://doc.rust-lang.org/cargo/reference/config.html). Defaults to the number of logical CPUs. If negative, it sets the maximum number of parallel jobs to the number of logical CPUs plus provided value. If a string `default` is provided, it sets the value back to defaults. Should not be 0.

[`--keep-going`](#option-cargo-check---keep-going)

Build as many crates in the dependency graph as possible, rather than aborting the build on the first one that fails to build.

For example if the current package depends on dependencies `fails` and `works`, one of which fails to build, `cargo check -j1` may or may not build the one that succeeds (depending on which one of the two builds Cargo picked to run first), whereas `cargo check -j1 --keep-going` would definitely run both builds, even if the one run first fails.

[`--future-incompat-report`](#option-cargo-check---future-incompat-report)

Displays a future-incompat report for any future-incompatible warnings produced during execution of this command

See [cargo-report(1)](https://doc.rust-lang.org/cargo/commands/cargo-report.html)

## [ENVIRONMENT](#environment)

See [the reference](https://doc.rust-lang.org/cargo/reference/environment-variables.html) for details on environment variables that Cargo reads.

## [EXIT STATUS](#exit-status)

- `0`: Cargo succeeded.
- `101`: Cargo failed to complete.

## [EXAMPLES](#examples)

1. Check the local package for errors:
   
   ```
   cargo check
   ```
2. Check all targets, including unit tests:
   
   ```
   cargo check --all-targets --profile=test
   ```

## [SEE ALSO](#see-also)

[cargo(1)](https://doc.rust-lang.org/cargo/commands/cargo.html), [cargo-build(1)](https://doc.rust-lang.org/cargo/commands/cargo-build.html)