---
title: Interior mutability - The Rust Reference
url: https://doc.rust-lang.org/reference/interior-mutability.html
source: crawler
fetched_at: 2026-05-06T21:26:58.684783821-03:00
rendered_js: false
word_count: 210
summary: This document explains the interior mutability pattern in Rust, which allows for data mutation through shared references using the UnsafeCell primitive and related standard library types.
tags:
    - rust-programming
    - interior-mutability
    - memory-safety
    - unsafe-cell
    - shared-references
category: concept
---

## Keyboard shortcuts

Press `←` or `→` to navigate between chapters

Press `S` or `/` to search in the book

Press `?` to show this help

Press `Esc` to hide this help

## The Rust Reference

## [Interior mutability](#interior-mutability)

Sometimes a type needs to be mutated while having multiple aliases. In Rust this is achieved using a pattern called *interior mutability*.

A type has interior mutability if its internal state can be changed through a [shared reference](https://doc.rust-lang.org/reference/types/pointer.html#shared-references-) to it.

This goes against the usual [requirement](https://doc.rust-lang.org/reference/behavior-considered-undefined.html) that the value pointed to by a shared reference is not mutated.

[`std::cell::UnsafeCell<T>`](https://doc.rust-lang.org/core/cell/struct.UnsafeCell.html) type is the only allowed way to disable this requirement. When `UnsafeCell<T>` is immutably aliased, it is still safe to mutate, or obtain a mutable reference to, the `T` it contains.

As with all other types, it is undefined behavior to have multiple `&mut UnsafeCell<T>` aliases.

Other types with interior mutability can be created by using `UnsafeCell<T>` as a field. The standard library provides a variety of types that provide safe interior mutability APIs.

For example, [`std::cell::RefCell<T>`](https://doc.rust-lang.org/core/cell/struct.RefCell.html) uses run-time borrow checks to ensure the usual rules around multiple references.

The [`std::sync::atomic`](https://doc.rust-lang.org/core/sync/atomic/index.html) module contains types that wrap a value that is only accessed with atomic operations, allowing the value to be shared and mutated across threads.