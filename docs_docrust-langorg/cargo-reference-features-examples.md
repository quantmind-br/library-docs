---
title: Features Examples - The Cargo Book
url: https://doc.rust-lang.org/cargo/reference/features-examples.html
source: crawler
fetched_at: 2026-05-06T21:25:07.520045428-03:00
rendered_js: false
word_count: 920
summary: This document explores common patterns and real-world usage scenarios for defining and managing optional features in Rust Cargo packages.
tags:
    - rust
    - cargo
    - package-management
    - build-optimization
    - crate-features
    - dependency-management
category: guide
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Cargo Book

## [Features Examples](#features-examples)

The following illustrates some real-world examples of features in action.

## [Minimizing build times and file sizes](#minimizing-build-times-and-file-sizes)

Some packages use features so that if the features are not enabled, it reduces the size of the crate and reduces compile time. Some examples are:

- [`syn`](https://crates.io/crates/syn) is a popular crate for parsing Rust code. Since it is so popular, it is helpful to reduce compile times since it affects so many projects. It has a [clearly documented list](https://docs.rs/syn/1.0.54/syn/#optional-features) of features which can be used to minimize the amount of code it contains.
- [`regex`](https://crates.io/crates/regex) has a [several features](https://github.com/rust-lang/regex/blob/1.4.2/Cargo.toml#L33-L101) that are [well documented](https://docs.rs/regex/1.4.2/regex/#crate-features). Cutting out Unicode support can reduce the resulting file size as it can remove some large tables.
- [`winapi`](https://crates.io/crates/winapi) has [a large number](https://github.com/retep998/winapi-rs/blob/0.3.9/Cargo.toml#L25-L431) of features that limit which Windows API bindings it supports.
- [`web-sys`](https://crates.io/crates/web-sys) is another example similar to `winapi` that provides a [huge surface area](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/crates/web-sys/Cargo.toml#L32-L1395) of API bindings that are limited by using features.

## [Extending behavior](#extending-behavior)

The [`serde_json`](https://crates.io/crates/serde_json) package has a [`preserve_order` feature](https://github.com/serde-rs/json/blob/v1.0.60/Cargo.toml#L53-L56) which [changes the behavior](https://github.com/serde-rs/json/blob/v1.0.60/src/map.rs#L23-L26) of JSON maps to preserve the order that keys are inserted. Notice that it enables an optional dependency [`indexmap`](https://crates.io/crates/indexmap) to implement the new behavior.

When changing behavior like this, be careful to make sure the changes are [SemVer compatible](https://doc.rust-lang.org/cargo/reference/features.html#semver-compatibility). That is, enabling the feature should not break code that usually builds with the feature off.

## [`no_std` support](#no_std-support)

Some packages want to support both [`no_std`](https://doc.rust-lang.org/reference/names/preludes.html#the-no_std-attribute) and `std` environments. This is useful for supporting embedded and resource-constrained platforms, but still allowing extended capabilities for platforms that support the full standard library.

The [`wasm-bindgen`](https://crates.io/crates/wasm-bindgen) package defines a [`std` feature](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/Cargo.toml#L25) that is [enabled by default](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/Cargo.toml#L23). At the top of the library, it [unconditionally enables the `no_std` attribute](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L8). This ensures that `std` and the [`std` prelude](https://doc.rust-lang.org/std/prelude/index.html) are not automatically in scope. Then, in various places in the code ([example1](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L270-L273), [example2](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L67-L75)), it uses `#[cfg(feature = "std")]` attributes to conditionally enable extra functionality that requires `std`.

## [Re-exporting dependency features](#re-exporting-dependency-features)

It can be convenient to re-export the features from a dependency. This allows the user depending on the crate to control those features without needing to specify those dependencies directly. For example, [`regex`](https://crates.io/crates/regex) [re-exports the features](https://github.com/rust-lang/regex/blob/1.4.2/Cargo.toml#L65-L89) from the [`regex_syntax`](https://github.com/rust-lang/regex/blob/1.4.2/regex-syntax/Cargo.toml#L17-L32) package. Users of `regex` don’t need to know about the `regex_syntax` package, but they can still access the features it contains.

## [Vendoring of C libraries](#vendoring-of-c-libraries)

Some packages provide bindings to common C libraries (sometimes referred to as [“sys” crates](https://doc.rust-lang.org/cargo/reference/build-scripts.html#-sys-packages)). Sometimes these packages give you the choice to use the C library installed on the system, or to build it from source. For example, the [`openssl`](https://crates.io/crates/openssl) package has a [`vendored` feature](https://github.com/sfackler/rust-openssl/blob/openssl-v0.10.31/openssl/Cargo.toml#L19) which enables the corresponding `vendored` feature of [`openssl-sys`](https://crates.io/crates/openssl-sys). The `openssl-sys` build script has some [conditional logic](https://github.com/sfackler/rust-openssl/blob/openssl-v0.10.31/openssl-sys/build/main.rs#L47-L54) which causes it to build from a local copy of the OpenSSL source code instead of using the version from the system.

The [`curl-sys`](https://crates.io/crates/curl-sys) package is another example where the [`static-curl` feature](https://github.com/alexcrichton/curl-rust/blob/0.4.34/curl-sys/Cargo.toml#L49) causes it to build libcurl from source. Notice that it also has a [`force-system-lib-on-osx`](https://github.com/alexcrichton/curl-rust/blob/0.4.34/curl-sys/Cargo.toml#L52) feature which forces it [to use the system libcurl](https://github.com/alexcrichton/curl-rust/blob/0.4.34/curl-sys/build.rs#L15-L20), overriding the static-curl setting.

## [Feature precedence](#feature-precedence)

Some packages may have mutually-exclusive features. One option to handle this is to prefer one feature over another. The [`log`](https://crates.io/crates/log) package is an example. It has [several features](https://github.com/rust-lang/log/blob/0.4.11/Cargo.toml#L29-L42) for choosing the maximum logging level at compile-time described [here](https://docs.rs/log/0.4.11/log/#compile-time-filters). It uses [`cfg-if`](https://crates.io/crates/cfg-if) to [choose a precedence](https://github.com/rust-lang/log/blob/0.4.11/src/lib.rs#L1422-L1448). If multiple features are enabled, the higher “max” levels will be preferred over the lower levels.

## [Proc-macro companion package](#proc-macro-companion-package)

Some packages have a proc-macro that is intimately tied with it. However, not all users will need to use the proc-macro. By making the proc-macro an optional-dependency, this allows you to conveniently choose whether or not it is included. This is helpful, because sometimes the proc-macro version must stay in sync with the parent package, and you don’t want to force the users to have to specify both dependencies and keep them in sync.

An example is [`serde`](https://crates.io/crates/serde) which has a [`derive`](https://github.com/serde-rs/serde/blob/v1.0.118/serde/Cargo.toml#L34-L35) feature which enables the [`serde_derive`](https://crates.io/crates/serde_derive) proc-macro. The `serde_derive` crate is very tightly tied to `serde`, so it uses an [equals version requirement](https://github.com/serde-rs/serde/blob/v1.0.118/serde/Cargo.toml#L17) to ensure they stay in sync.

## [Nightly-only features](#nightly-only-features)

Some packages want to experiment with APIs or language features that are only available on the Rust [nightly channel](https://doc.rust-lang.org/book/appendix-07-nightly-rust.html). However, they may not want to require their users to also use the nightly channel. An example is [`wasm-bindgen`](https://crates.io/crates/wasm-bindgen) which has a [`nightly` feature](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/Cargo.toml#L27) which enables an [extended API](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/closure.rs#L257-L269) that uses the [`Unsize`](https://doc.rust-lang.org/std/marker/trait.Unsize.html) marker trait that is only available on the nightly channel at the time of this writing.

Note that at the root of the crate it uses [`cfg_attr` to enable the nightly feature](https://github.com/rustwasm/wasm-bindgen/blob/0.2.69/src/lib.rs#L11). Keep in mind that the [`feature` attribute](https://doc.rust-lang.org/unstable-book/index.html) is unrelated to Cargo features, and is used to opt-in to experimental language features.

The [`simd_support` feature](https://github.com/rust-random/rand/blob/0.7.3/Cargo.toml#L40) of the [`rand`](https://crates.io/crates/rand) package is another example, which relies on a dependency that only builds on the nightly channel.

## [Experimental features](#experimental-features)

Some packages have new functionality that they may want to experiment with, without having to commit to the stability of those APIs. The features are usually documented that they are experimental, and thus may change or break in the future, even during a minor release. An example is the [`async-std`](https://crates.io/crates/async-std) package, which has an [`unstable` feature](https://github.com/async-rs/async-std/blob/v1.8.0/Cargo.toml#L38-L42), which [gates new APIs](https://github.com/async-rs/async-std/blob/v1.8.0/src/macros.rs#L46) that people can opt-in to using, but may not be completely ready to be relied upon.