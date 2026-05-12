---
title: std::prelude::v1 - Rust
url: https://doc.rust-lang.org/stable/std/prelude/v1/index.html
source: crawler
fetched_at: 2026-05-06T21:25:22.410959196-03:00
rendered_js: false
word_count: 500
summary: This document outlines the contents of the Rust standard library prelude, listing the traits, macros, and types automatically imported into every Rust crate.
tags:
    - rust
    - prelude
    - standard-library
    - macros
    - traits
    - language-features
category: reference
---

Expand description

`pub use crate::marker::Send;`

`pub use crate::marker::Sized;`

`pub use crate::marker::Sync;`

`pub use crate::marker::Unpin;`

`pub use crate::ops::Drop;`

`pub use crate::ops::Fn;`

`pub use crate::ops::FnMut;`

`pub use crate::ops::FnOnce;`

`pub use crate::ops::AsyncFn;`

`pub use crate::ops::AsyncFnMut;`

`pub use crate::ops::AsyncFnOnce;`

`pub use crate::mem::drop;`

`pub use crate::mem::align_of;`

`pub use crate::mem::align_of_val;`

`pub use crate::mem::size_of;`

`pub use crate::mem::size_of_val;`

`pub use crate::convert::AsMut;`

`pub use crate::convert::AsRef;`

`pub use crate::convert::From;`

`pub use crate::convert::Into;`

`pub use crate::iter::DoubleEndedIterator;`

`pub use crate::iter::ExactSizeIterator;`

`pub use crate::iter::Extend;`

`pub use crate::iter::IntoIterator;`

`pub use crate::iter::Iterator;`

`pub use crate::option::Option;`

`pub use crate::option::Option::None;`

`pub use crate::option::Option::Some;`

`pub use crate::result::Result;`

`pub use crate::result::Result::Err;`

`pub use crate::result::Result::Ok;`

`pub use core::prelude::v1::assert;`

`pub use core::prelude::v1::assert_eq;`

`pub use core::prelude::v1::assert_ne;`

`pub use core::prelude::v1::cfg;`

`pub use core::prelude::v1::column;`

`pub use core::prelude::v1::compile_error;`

`pub use core::prelude::v1::concat;`

`pub use core::prelude::v1::debug_assert;`

`pub use core::prelude::v1::debug_assert_eq;`

`pub use core::prelude::v1::debug_assert_ne;`

`pub use core::prelude::v1::env;`

`pub use core::prelude::v1::file;`

`pub use core::prelude::v1::format_args;`

`pub use core::prelude::v1::include;`

`pub use core::prelude::v1::include_bytes;`

`pub use core::prelude::v1::include_str;`

`pub use core::prelude::v1::line;`

`pub use core::prelude::v1::matches;`

`pub use core::prelude::v1::module_path;`

`pub use core::prelude::v1::option_env;`

`pub use core::prelude::v1::stringify;`

`pub use core::prelude::v1::todo;`

`pub use core::prelude::v1::try;`Deprecated

`pub use core::prelude::v1::unimplemented;`

`pub use core::prelude::v1::unreachable;`

`pub use core::prelude::v1::write;`

`pub use core::prelude::v1::writeln;`

`pub use core::prelude::v1::Clone;`

`pub use core::prelude::v1::Clone;`

`pub use core::prelude::v1::Copy;`

`pub use core::prelude::v1::Copy;`

`pub use core::prelude::v1::Debug;`

`pub use core::prelude::v1::Default;`

`pub use core::prelude::v1::Default;`

`pub use core::prelude::v1::Eq;`

`pub use core::prelude::v1::Eq;`

`pub use core::prelude::v1::Hash;`

`pub use core::prelude::v1::Ord;`

`pub use core::prelude::v1::Ord;`

`pub use core::prelude::v1::PartialEq;`

`pub use core::prelude::v1::PartialEq;`

`pub use core::prelude::v1::PartialOrd;`

`pub use core::prelude::v1::PartialOrd;`

`pub use crate::dbg;`

`pub use crate::eprint;`

`pub use crate::eprintln;`

`pub use crate::format;`

`pub use crate::is_x86_feature_detected;`

`pub use crate::print;`

`pub use crate::println;`

`pub use crate::thread_local;`

`pub use self::ambiguous_macros_only::vec;`

`pub use self::ambiguous_macros_only::panic;`

`pub use core::prelude::v1::cfg_select;`

`pub use crate::borrow::ToOwned;`

`pub use crate::boxed::Box;`

`pub use crate::string::String;`

`pub use crate::string::ToString;`

`pub use crate::vec::Vec;`

`pub use core::prelude::v1::concat_bytes;`Experimental

`pub use core::prelude::v1::const_format_args;`Experimental

`pub use core::prelude::v1::log_syntax;`Experimental

`pub use core::prelude::v1::trace_macros;`Experimental

[deref](https://doc.rust-lang.org/stable/std/prelude/v1/macro.deref.html "macro std::prelude::v1::deref")Experimental

Unstable placeholder for deref patterns.

[type\_ascribe](https://doc.rust-lang.org/stable/std/prelude/v1/macro.type_ascribe.html "macro std::prelude::v1::type_ascribe")Experimental

Unstable placeholder for type ascription.

[derive](https://doc.rust-lang.org/stable/std/prelude/v1/attr.derive.html "attr std::prelude::v1::derive")

Attribute macro used to apply derive macros.

[global\_allocator](https://doc.rust-lang.org/stable/std/prelude/v1/attr.global_allocator.html "attr std::prelude::v1::global_allocator")

Attribute macro applied to a static to register it as a global allocator.

[test](https://doc.rust-lang.org/stable/std/prelude/v1/attr.test.html "attr std::prelude::v1::test")

Attribute macro applied to a function to turn it into a unit test.

[alloc\_error\_handler](https://doc.rust-lang.org/stable/std/prelude/v1/attr.alloc_error_handler.html "attr std::prelude::v1::alloc_error_handler")Experimental

Attribute macro applied to a function to register it as a handler for allocation failure.

[bench](https://doc.rust-lang.org/stable/std/prelude/v1/attr.bench.html "attr std::prelude::v1::bench")Experimental

Attribute macro applied to a function to turn it into a benchmark test.

[cfg\_accessible](https://doc.rust-lang.org/stable/std/prelude/v1/attr.cfg_accessible.html "attr std::prelude::v1::cfg_accessible")Experimental

Keeps the item it’s applied to if the passed path is accessible, and removes it otherwise.

[cfg\_eval](https://doc.rust-lang.org/stable/std/prelude/v1/attr.cfg_eval.html "attr std::prelude::v1::cfg_eval")Experimental

Expands all `#[cfg]` and `#[cfg_attr]` attributes in the code fragment it’s applied to.

[define\_opaque](https://doc.rust-lang.org/stable/std/prelude/v1/attr.define_opaque.html "attr std::prelude::v1::define_opaque")Experimental

Provide a list of type aliases and other opaque-type-containing type definitions to an item with a body. This list will be used in that body to define opaque types’ hidden types. Can only be applied to things that have bodies.

[derive\_const](https://doc.rust-lang.org/stable/std/prelude/v1/attr.derive_const.html "attr std::prelude::v1::derive_const")Experimental

Attribute macro used to apply derive macros for implementing traits in a const context.

[eii](https://doc.rust-lang.org/stable/std/prelude/v1/attr.eii.html "attr std::prelude::v1::eii")Experimental

Externally Implementable Item: Defines an attribute macro that can override the item this is applied to.

[eii\_declaration](https://doc.rust-lang.org/stable/std/prelude/v1/attr.eii_declaration.html "attr std::prelude::v1::eii_declaration")Experimental

Impl detail of EII

[test\_case](https://doc.rust-lang.org/stable/std/prelude/v1/attr.test_case.html "attr std::prelude::v1::test_case")Experimental

An implementation detail of the `#[test]` and `#[bench]` macros.

[unsafe\_eii](https://doc.rust-lang.org/stable/std/prelude/v1/attr.unsafe_eii.html "attr std::prelude::v1::unsafe_eii")Experimental

Unsafely Externally Implementable Item: Defines an unsafe attribute macro that can override the item this is applied to.