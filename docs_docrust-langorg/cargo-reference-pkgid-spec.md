---
title: Package ID Specifications - The Cargo Book
url: https://doc.rust-lang.org/cargo/reference/pkgid-spec.html
source: crawler
fetched_at: 2026-05-06T21:25:08.071642431-03:00
rendered_js: false
word_count: 328
summary: This document defines the syntax and usage of Cargo Package ID Specifications for uniquely identifying packages within a dependency graph.
tags:
    - cargo
    - rust
    - package-management
    - dependency-graph
    - specification-grammar
    - cli-tooling
category: reference
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Cargo Book

## [Package ID Specifications](#package-id-specifications)

## [Package ID specifications](#package-id-specifications-1)

Subcommands of Cargo frequently need to refer to a particular package within a dependency graph for various operations like updating, cleaning, building, etc. To solve this problem, Cargo supports *Package ID Specifications*. A specification is a string which is used to uniquely refer to one package within a graph of packages.

The specification may be fully qualified, such as `registry+https://github.com/rust-lang/crates.io-index#regex@1.4.3` or it may be abbreviated, such as `regex`. The abbreviated form may be used as long as it uniquely identifies a single package in the dependency graph. If there is ambiguity, additional qualifiers can be added to make it unique. For example, if there are two versions of the `regex` package in the graph, then it can be qualified with a version to make it unique, such as `regex@1.4.3`.

Package ID specifications output by cargo, for example in [cargo metadata](https://doc.rust-lang.org/cargo/commands/cargo-metadata.html) output, are fully qualified.

### [Specification grammar](#specification-grammar)

The formal grammar for a Package Id Specification is:

```notrust
spec := pkgname |
        [ kind "+" ] proto "://" hostname-and-path [ "?" query] [ "#" ( pkgname | semver ) ]
query = ( "branch" | "tag" | "rev" ) "=" ref
pkgname := name [ ("@" | ":" ) semver ]
semver := digits [ "." digits [ "." digits [ "-" prerelease ] [ "+" build ]]]

kind = "registry" | "git" | "path"
proto := "http" | "git" | "file" | ...
```

Here, brackets indicate that the contents are optional.

The URL form can be used for git dependencies, or to differentiate packages that come from different sources such as different registries.

### [Example specifications](#example-specifications)

The following are references to the `regex` package on `crates.io`:

SpecNameVersion `regex``regex``*` `regex@1.4``regex``1.4.*` `regex@1.4.3``regex``1.4.3` `https://github.com/rust-lang/crates.io-index#regex``regex``*` `https://github.com/rust-lang/crates.io-index#regex@1.4.3``regex``1.4.3` `registry+https://github.com/rust-lang/crates.io-index#regex@1.4.3``regex``1.4.3`

The following are some examples of specs for several different git dependencies:

SpecNameVersion `https://github.com/rust-lang/cargo#0.52.0``cargo``0.52.0` `https://github.com/rust-lang/cargo#cargo-platform@0.1.2``cargo-platform``0.1.2` `ssh://git@github.com/rust-lang/regex.git#regex@1.4.3``regex``1.4.3` `git+ssh://git@github.com/rust-lang/regex.git#regex@1.4.3``regex``1.4.3` `git+ssh://git@github.com/rust-lang/regex.git?branch=dev#regex@1.4.3``regex``1.4.3`

Local packages on the filesystem can use `file://` URLs to reference them:

SpecNameVersion `file:///path/to/my/project/foo``foo``*` `file:///path/to/my/project/foo#1.1.8``foo``1.1.8` `path+file:///path/to/my/project/foo#1.1.8``foo``1.1.8`

### [Brevity of specifications](#brevity-of-specifications)

The goal of this is to enable both succinct and exhaustive syntaxes for referring to packages in a dependency graph. Ambiguous references may refer to one or more packages. Most commands generate an error if more than one package could be referred to with the same specification.