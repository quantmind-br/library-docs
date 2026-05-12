---
title: Rust Documentation
url: https://doc.rust-lang.org/nightly/
source: sitemap
fetched_at: 2026-05-06T21:07:02.466213744-03:00
rendered_js: false
word_count: 689
summary: This document provides a comprehensive directory of the official Rust documentation ecosystem, including language learning materials, toolchain references, and specialized guides.
tags:
    - rust-programming
    - language-reference
    - developer-tools
    - documentation-resources
    - programming-tutorials
    - rust-ecosystem
category: reference
---

Welcome to an overview of the documentation provided by the [Rust project](https://www.rust-lang.org). This page contains links to various helpful references, most of which are available offline (if opened with `rustup doc`). Many of these resources take the form of “books”; we collectively call these “The Rust Bookshelf.” Some are large, some are small.

All of these books are managed by the Rust Organization, but other unofficial documentation resources are included here as well!

If you’re just looking for the standard library reference, here it is: [Rust API documentation](https://doc.rust-lang.org/nightly/std/index.html)

## [§](#learning-rust)Learning Rust

If you’d like to learn Rust, this is the section for you! All of these resources assume that you have programmed before, but not in any specific language:

### [§](#the-rust-programming-language)The Rust Programming Language

Affectionately nicknamed “the book,” [The Rust Programming Language](https://doc.rust-lang.org/nightly/book/index.html) will give you an overview of the language from first principles. You’ll build a few projects along the way, and by the end, you’ll have a solid grasp of how to use the language.

### [§](#rust-by-example)Rust By Example

If reading multiple hundreds of pages about a language isn’t your style, then [Rust By Example](https://doc.rust-lang.org/nightly/rust-by-example/index.html) has you covered. RBE shows off a bunch of code without using a lot of words. It also includes exercises!

### [§](#rustlings)Rustlings

[Rustlings](https://github.com/rust-lang/rustlings) guides you through downloading and setting up the Rust toolchain, then provides an interactive tool that teaches you how to solve coding challenges in Rust.

### [§](#rust-playground)Rust Playground

The [Rust Playground](https://play.rust-lang.org) is a great place to try out and share small bits of code, or experiment with some of the most popular crates.

## [§](#using-rust)Using Rust

Once you’ve gotten familiar with the language, these resources can help you put it to work.

### [§](#the-standard-library)The Standard Library

Rust’s standard library has [extensive API documentation](https://doc.rust-lang.org/nightly/std/index.html), with explanations of how to use various things, as well as example code for accomplishing various tasks. Code examples have a “Run” button on hover that opens the sample in the playground.

### [§](#your-personal-documentation)Your Personal Documentation

Whenever you are working in a crate, `cargo doc --open` will generate documentation for your project *and* all its dependencies in their correct version, and open it in your browser. Add the flag `--document-private-items` to also show items not marked `pub`.

### [§](#rust-version-history)Rust Version History

[The Release Notes](https://doc.rust-lang.org/nightly/releases.html) describes the change history of the Rust toolchain and language.

[The Edition Guide](https://doc.rust-lang.org/nightly/edition-guide/index.html) describes the Rust editions and their differences. The latest version of the toolchain supports all historical editions.

### [§](#the-rustc-book)The `rustc` Book

[The `rustc` Book](https://doc.rust-lang.org/nightly/rustc/index.html) describes the Rust compiler, `rustc`.

### [§](#the-cargo-book)The Cargo Book

[The Cargo Book](https://doc.rust-lang.org/nightly/cargo/index.html) is a guide to Cargo, Rust’s build tool and dependency manager.

### [§](#the-rustdoc-book)The Rustdoc Book

[The Rustdoc Book](https://doc.rust-lang.org/nightly/rustdoc/index.html) describes our documentation tool, `rustdoc`.

### [§](#the-clippy-book)The Clippy Book

[The Clippy Book](https://doc.rust-lang.org/nightly/clippy/index.html) describes our static analyzer, Clippy.

### [§](#extended-error-listing)Extended Error Listing

Many of Rust’s errors come with error codes, and you can request extended diagnostics from the compiler on those errors (with `rustc --explain`). You can also read them here if you prefer: [rustc error codes](https://doc.rust-lang.org/nightly/error_codes/index.html)

## [§](#mastering-rust)Mastering Rust

Once you’re quite familiar with the language, you may find these advanced resources useful.

### [§](#the-reference)The Reference

[The Reference](https://doc.rust-lang.org/nightly/reference/index.html) is not a formal spec, but is more detailed and comprehensive than the book.

### [§](#the-style-guide)The Style Guide

[The Rust Style Guide](https://doc.rust-lang.org/nightly/style-guide/index.html) describes the standard formatting of Rust code. Most developers use `cargo fmt` to invoke `rustfmt` and format the code automatically (the result matches this style guide).

### [§](#the-rustonomicon)The Rustonomicon

[The Rustonomicon](https://doc.rust-lang.org/nightly/nomicon/index.html) is your guidebook to the dark arts of unsafe Rust. It’s also sometimes called “the ’nomicon.”

### [§](#the-unstable-book)The Unstable Book

[The Unstable Book](https://doc.rust-lang.org/nightly/unstable-book/index.html) has documentation for unstable features.

### [§](#the-rustc-development-guide)The `rustc` Development Guide

[The `rustc-dev-guide`](https://rustc-dev-guide.rust-lang.org/) documents how the compiler works and how to contribute to it. This is useful if you want to build or modify the Rust compiler from source (e.g. to target something non-standard).

## [§](#specialized-rust)Specialized Rust

When using Rust in specific domains, consider using the following resources tailored to each area.

### [§](#embedded-systems)Embedded Systems

When developing for Bare Metal or Embedded Linux systems, you may find these resources maintained by the [Embedded Working Group](https://github.com/rust-embedded) useful.

#### [§](#the-embedded-rust-book)The Embedded Rust Book

[The Embedded Rust Book](https://doc.rust-lang.org/nightly/embedded-book/index.html) is targeted at developers who are familiar with embedded development and Rust, but who have not used Rust for embedded development.