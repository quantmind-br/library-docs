---
title: PR Guidelines
url: https://wiki.hypr.land/Contributing-and-Debugging/PR-Guidelines/
source: sitemap
fetched_at: 2026-04-26T09:49:56.647886714-03:00
rendered_js: false
word_count: 570
summary: This document outlines the coding standards, submission requirements, and technical guidelines for contributors to the project.
tags:
    - contribution-guidelines
    - code-style
    - pull-request
    - c-plus-plus
    - development-workflow
    - coding-standards
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

## PR Requirements

- Clean, not hacky code
- Described changes and *why* they were made
- Style followed (see below)

> [!info]
> Using an AI tool? Check the [AI Policy](https://github.com/hyprwm/.github/blob/main/policies/AI_USAGE.md).

## Code Style

### Before you submit

```bash
clang-format -i $(find src -type f \( -name "*.cpp" -o -name "*.hpp" \))
```

Check `clang-tidy` violations (usually built into your IDE).

### Clang-format — non-negotiable

Code **must** be formatted with clang-format.

### Clang-tidy — strongly recommended

Clang-tidy violations are not hard requirements, but minimize them — only ignore if absolutely necessary. Tweaked so 99% of cases definitely need fixing.

### Testing

See [[088-contributing-and-debugging-tests|Tests]] for test information.

> [!important]
> No test regressions is a *must*. New tests *required* if possible (graphical stuff is often not testable).

### Other (clang-tidy / clang-format won't catch)

- No uninitialized *primitives* (int, float, double, size_t, etc.)
- No short if braces. If `if`/`else` body is 1 *line* (not 1 statement), don't use `{}`
- Above rule does not apply to loops
- Consider `;` in empty function bodies
- Commas after last element when initializing vectors/arrays/maps with many elements
- Forward-declare in headers when possible instead of including — speeds up compile times
- No `using namespace std;`. `using namespace (anything)` only in source files, not headers
- Prefer guards over nesting: `if(!valid) return;` over `if (valid) { /* ... */ }`

### Naming conventions

Moving away from hungarian notation. Current code should use `camelCase` with `m_` prefix for class member variables (not structs):

- classes: `C` prefix → `CMyClass`
- structs: `S` prefix → `SMyStruct`
- interfaces: `I` prefix → `IMyInterface`
- global singleton pointers: `g_` prefix → `g_someManager`
- constant variables: CAPS → `const auto MYVARIABLE = ...`

## General code requirements

### No raw pointers

Use `UP`, `SP`, `WP` (unique/shared/weak pointers). Don't use raw pointers (e.g. `CMyClass*`) unless absolutely necessary.

### No malloc

Don't use `malloc`/`free` unless absolutely necessary — you'll forget to free memory.

### Avoid dubious cleanups

For C-style allocators (e.g. `some_c_call_make_new()` / `some_c_call_free()`):
- wrap in a C++ class, or
- use `CScopeGuard` in single-function scope to always free on exit

### Use the STL

Prefer STL over reinventing the wheel.

### Use hyprutils

[hyprutils](https://wiki.hypr.land/Hypr-Ecosystem/hyprutils/) provides utilities well-suited for hyprland and other hypr* projects — use them.

### No absolute includes from /src

From `a.hpp`, include `b.hpp` as `../b/b.hpp`, **not** `b/b.hpp`. The latter breaks plugins.

Exception: absolute paths from root are allowed, e.g. `protocols/some-protocol.hpp`.

Last updated on April 20, 2026