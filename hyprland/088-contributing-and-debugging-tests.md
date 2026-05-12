---
title: Tests
url: https://wiki.hypr.land/Contributing-and-Debugging/Tests/
source: sitemap
fetched_at: 2026-04-26T09:49:58.654002445-03:00
rendered_js: false
word_count: 292
summary: This document outlines the procedures for running unit and integration tests within Hyprland projects to ensure code quality and verify fixes.
tags:
    - hyprland
    - unit-testing
    - gtest
    - hyprtester
    - code-quality
    - software-testing
    - development-workflow
category: guide
optimized: true
optimized_at: 2026-04-26T10:50:00Z
---

Hyprland and hypr* projects have tests to catch bugs and regressions before merging.

Building in Debug builds tests by default.

## Running tests

### GTests

GTests are Google unit tests. Run with ctest:

```bash
ctest -j$(nproc) -C Debug --test-dir=build
```

### Hyprtester

Hyprland code cannot be fully unit tested, so Hyprtester binary runs Hyprland, issues commands, and validates results.

```bash
cd ./hyprtester && ../build/hyprtester/hyprtester --plugin ./plugin/hyprtestplugin.so
```

> [!warning]
> Runs for a while. Goal: **0 failed tests**.

## Submitting new tests

New tests should be GTests (if testable as unit) or part of hyprtester.

GTests live in `tests/`, hyprtester tests in `hyprtester/`.

### What to test

- New feature → test your feature
- Fix → write a test that would fail before your fix

### Coverage report

After running both ctest and hyprtester:

```bash
gcovr -r . build --html --html-details -o build/coverage.html --gcov-ignore-parse-errors="negative_hits.warn" && xdg-open ./build/coverage.html
```

Review the report to find untested paths and add tests for them.

See also: [[087-contributing-and-debugging-pr-guidelines|PR Guidelines]] · [[089-contributing-and-debugging-translations|Translations]]

#hyprland #unit-testing #gtest #hyprtester