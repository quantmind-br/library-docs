---
title: test - Rust
url: https://doc.rust-lang.org/test/index.html
source: crawler
fetched_at: 2026-05-06T21:24:56.436205057-03:00
rendered_js: false
word_count: 283
summary: This document provides an overview of the experimental Rust test crate, which contains internal support code for unit testing and micro-benchmarking.
tags:
    - rust
    - testing
    - benchmarking
    - api-reference
    - experimental-api
    - unit-tests
category: api
---

🔬This is a nightly-only experimental API. (`test`)

Expand description

Support code for rustc’s built in unit-test and micro-benchmarking framework.

Almost all user code will only be interested in `Bencher` and `black_box`. All other interactions (such as writing tests and benchmarks themselves) should be done via the `#[test]` and `#[bench]` attributes.

See the [Testing Chapter](https://doc.rust-lang.org/book/ch11-00-testing.html) of the book for more details.

`pub use self::bench::Bencher;`Experimental

`pub use self::bench::black_box;`Experimental

`pub use self::ColorConfig::*;`Experimental

`pub use self::types::TestName::*;`Experimental

`pub use NamePadding::*;`Experimental

`pub use TestFn::*;`Experimental

`pub use TestName::*;`Experimental

[bench](https://doc.rust-lang.org/test/bench/index.html "mod test::bench")Experimental

Benchmarking module.

[stats](https://doc.rust-lang.org/test/stats/index.html "mod test::stats")Experimental

[test](https://doc.rust-lang.org/test/test/index.html "mod test::test")Experimental

[Options](https://doc.rust-lang.org/test/struct.Options.html "struct test::Options")Experimental

Options for the test run defined by the caller (instead of CLI arguments). In case we want to add other options as well, just add them in this struct.

[TestDesc](https://doc.rust-lang.org/test/struct.TestDesc.html "struct test::TestDesc")Experimental

[TestDescAndFn](https://doc.rust-lang.org/test/struct.TestDescAndFn.html "struct test::TestDescAndFn")Experimental

[TestId](https://doc.rust-lang.org/test/struct.TestId.html "struct test::TestId")Experimental

[TestOpts](https://doc.rust-lang.org/test/struct.TestOpts.html "struct test::TestOpts")Experimental

[ColorConfig](https://doc.rust-lang.org/test/enum.ColorConfig.html "enum test::ColorConfig")Experimental

Whether should console output be colored or not

[NamePadding](https://doc.rust-lang.org/test/enum.NamePadding.html "enum test::NamePadding")Experimental

[OutputFormat](https://doc.rust-lang.org/test/enum.OutputFormat.html "enum test::OutputFormat")Experimental

Format of the test results output

[RunIgnored](https://doc.rust-lang.org/test/enum.RunIgnored.html "enum test::RunIgnored")Experimental

Whether ignored test should be run or not

[ShouldPanic](https://doc.rust-lang.org/test/enum.ShouldPanic.html "enum test::ShouldPanic")Experimental

Whether test is expected to panic or not

[TestFn](https://doc.rust-lang.org/test/enum.TestFn.html "enum test::TestFn")Experimental

[TestName](https://doc.rust-lang.org/test/enum.TestName.html "enum test::TestName")Experimental

[TestType](https://doc.rust-lang.org/test/enum.TestType.html "enum test::TestType")Experimental

Type of the test according to the [Rust book](https://doc.rust-lang.org/cargo/guide/tests.html) conventions.

[ERROR\_EXIT\_CODE](https://doc.rust-lang.org/test/constant.ERROR_EXIT_CODE.html "constant test::ERROR_EXIT_CODE")Experimental

Process exit code to be used to indicate test failures.

[assert\_test\_result](https://doc.rust-lang.org/test/fn.assert_test_result.html "fn test::assert_test_result")Experimental

Invoked when unit tests terminate. Returns `Result::Err` if the test is considered a failure. By default, invokes `report()` and checks for a `0` result.

[convert\_benchmarks\_to\_tests](https://doc.rust-lang.org/test/fn.convert_benchmarks_to_tests.html "fn test::convert_benchmarks_to_tests")Experimental

[filter\_tests](https://doc.rust-lang.org/test/fn.filter_tests.html "fn test::filter_tests")Experimental

[print\_merged\_doctests\_times](https://doc.rust-lang.org/test/fn.print_merged_doctests_times.html "fn test::print_merged_doctests_times")Experimental

Public API used by rustdoc to display the `total` and `compilation` times in the expected format.

[run\_test](https://doc.rust-lang.org/test/fn.run_test.html "fn test::run_test")Experimental

[run\_tests](https://doc.rust-lang.org/test/fn.run_tests.html "fn test::run_tests")Experimental

[run\_tests\_console](https://doc.rust-lang.org/test/fn.run_tests_console.html "fn test::run_tests_console")Experimental

A simple console test runner. Runs provided tests reporting process and results to the stdout.

[test\_main](https://doc.rust-lang.org/test/fn.test_main.html "fn test::test_main")Experimental

[test\_main\_static](https://doc.rust-lang.org/test/fn.test_main_static.html "fn test::test_main_static")Experimental

A variant optimized for invocation with a static test vector. This will panic (intentionally) when fed any dynamic tests.

[test\_main\_static\_abort](https://doc.rust-lang.org/test/fn.test_main_static_abort.html "fn test::test_main_static_abort")Experimental

A variant optimized for invocation with a static test vector. This will panic (intentionally) when fed any dynamic tests.

[test\_main\_with\_exit\_callback](https://doc.rust-lang.org/test/fn.test_main_with_exit_callback.html "fn test::test_main_with_exit_callback")Experimental