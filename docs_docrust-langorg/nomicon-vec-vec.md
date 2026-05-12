---
title: Implementing Vec - The Rustonomicon
url: https://doc.rust-lang.org/nomicon/vec/vec.html
source: crawler
fetched_at: 2026-05-06T21:21:49.503828943-03:00
rendered_js: false
word_count: 137
summary: This document introduces a comprehensive tutorial on reimplementing the standard library's Vec collection using only stable Rust features.
tags:
    - rust-programming
    - vec-implementation
    - data-structures
    - memory-management
    - systems-programming
category: tutorial
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rustonomicon

## [Example: Implementing Vec](#example-implementing-vec)

To bring everything together, we’re going to write `std::Vec` from scratch. We will limit ourselves to stable Rust. In particular we won’t use any intrinsics that could make our code a little bit nicer or efficient because intrinsics are permanently unstable. Although many intrinsics *do* become stabilized elsewhere (`std::ptr` and `std::mem` consist of many intrinsics).

Ultimately this means our implementation may not take advantage of all possible optimizations, though it will be by no means *naive*. We will definitely get into the weeds over nitty-gritty details, even when the problem doesn’t *really* merit it.

You wanted advanced. We’re gonna go advanced.