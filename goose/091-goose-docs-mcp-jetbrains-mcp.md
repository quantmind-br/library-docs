---
title: JetBrains Extension | goose
url: https://block.github.io/goose/docs/mcp/jetbrains-mcp
source: github_pages
fetched_at: 2026-01-22T22:15:23.2075062-03:00
rendered_js: true
word_count: 443
summary: This tutorial explains how to integrate JetBrains IDEs with Goose using a dedicated extension to perform project-aware code refactoring and modernization tasks.
tags:
    - jetbrains-extension
    - ide-integration
    - java-modernization
    - refactoring
    - goose-ai
    - code-editor
category: tutorial
---

This tutorial covers how to add the JetBrains extension to integrate with any JetBrains IDE. While goose can use the [Developer extension](https://block.github.io/goose/docs/mcp/developer-mcp) for developer-centric tasks, the JetBrains extension provides a more integrated and project-aware way to work with code.

**Important**: The configuration steps depend on your IDE version. You can find the version in `[IDE Name] > About` (macOS) or `Help > About` (Windows/Linux).

In this example, I'm going to upgrade a Java project to the latest LTS version.

tip

When using goose to refactor code, it's recommended to commit your code to version control *before* making changes. This way, you have a clean snapshot to compare against, making it easy to review goose's modifications, revert if needed, and track improvements.

```
using the JetBrains IDE tools, upgrade this project to use the latest Java LTS version and refactor the codebase to use newer Java features where beneficial.
```

```
I'll make several improvements to modernize this codebase to use Java 21 (latest LTS) features. Here are the changes I'll implement:

1. Update the `pom.xml` to use Java 21
2. Use newer Java features

[... code changes ...]

Here's a summary of the modernization changes made:

1.`pom.xml`:
- Set Java version to 21
- Enabled preview features
- Updated all dependencies to their latest stable versions

2.`AccountsOverviewPage.java`:
- Made the class `final` since it extends the sealed `Page` class
- Updated stream collection to use `.toList()` instead of `collect(Collectors.toList())`
- Made fields final for better immutability

3.`Page.java`:
- Converted to a sealed class
- Restricted which classes can extend it using `permits`
- Made fields protected and final where appropriate
- Added pattern matching for exception handling
- Implemented Optional for null safety
- Used String Templates for error messages
- Added functional programming concepts with Supplier
- Enhanced error handling with specific exception types

4.`LoginComponent.java`:
- Added a private record for credentials
- Implemented pattern matching with record patterns
- Made fields final for better immutability

5.`AccountTests.java`:
- Implemented structured concurrency using `StructuredTaskScope`
- Used parallel execution for UI and API tasks
- Improved error handling with structured task management
- Used pattern matching and type inference with `var`

6.`BaseTests.java`:
- Implemented structured concurrency for setup tasks
- Improved resource management
- Better exception handling
- Used modern Duration API

7.`APIUtil.java`:
- Implemented String Templates (Java 21 preview feature)
- Used modern text blocks

8.`Customers.java`:
- Added sealed interface for customer types
- Implemented pattern matching for switch expressions
- Added pattern matching for instanceof
- Enhanced type safety with records

Key modern Java features used:
- String Templates (Java 21 Preview)
- Pattern Matching for switch (Java 21)
- Sealed Classes and Interfaces (Java 17)
- Records (Java 16)
- Pattern Matching for instanceof (Java 16)
- Text Blocks (Java 15)
- Switch Expressions (Java 14)

The codebase is now using the latest Java LTS version (21) and incorporates many modern Java features that improve:
- Type safety
- Null safety
- Code readability
- Error handling
- Performance
```

Using the JetBrains extension provided several advantages and made it easier for goose to: