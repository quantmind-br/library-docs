---
title: Documentation and Docstrings - Zencoder Docs
url: https://docs.zencoder.ai/features/documentation
source: crawler
fetched_at: 2026-01-23T09:28:15.490218064-03:00
rendered_js: false
word_count: 329
summary: This guide explains how to use Zencoder to generate in-code docstrings and external documentation through code lenses and direct prompting in various IDEs.
tags:
    - zencoder
    - documentation-generation
    - docstrings
    - vs-code
    - jetbrains
    - ai-coding-assistant
category: guide
---

This page covers how to generate two types of documentation with Zencoder:

1. **Docstrings** - In-code documentation for functions, classes, and methods (available via code lenses or direct prompting)
2. **Generic Documentation** - README files, API docs, and module documentation (available via prompting)

We’ll also cover best practices and troubleshooting for common issues.

## Docstring Generation

Docstrings are structured comments embedded directly in your code that document functions, methods, and classes. They follow language-specific conventions (Python docstrings, JSDoc for JavaScript/TypeScript, PHPDoc for PHP, Javadoc for Java, etc.) and are used by IDEs for tooltips, API documentation generators, and code intelligence features. Unlike generic documentation that might live in separate files, docstrings stay with the code they describe.

### How to Generate Docstrings

There are two methods to generate docstrings with Zencoder:

1. **Using Code Lenses** - The fastest way to add documentation directly in your editor
2. **Direct Prompting** - Generate docstrings and general documentation through the chat interface with custom requirements

#### Using Code Lenses

- VS Code
- JetBrains

#### VS Code Code Lenses

When you open a file in VS Code, you’ll see a `Zencoder` code lens above your functions, classes, and methods.

#### JetBrains Code Lenses

In JetBrains IDEs, you’ll see a `Doc Comment` code lens above your classes, functions, and methods.

#### Direct Prompting

Generate docstrings through the chat interface when code lenses aren’t available or when you need more control:

### Example: Before and After

Example of generated Python docstrings:

## Generic Documentation Generation

Generic documentation covers entire files, modules, or projects - things like README files, API documentation, architecture guides, and user manuals. This documentation lives in separate files rather than inline with code.

### How to Generate Broader Documentation

### Best Practices

1. **Be specific in your prompts** - Include details about format, style guide, or specific requirements
2. **Provide context** - Include surrounding code when generating docstrings for better accuracy
3. **Iterate as needed** - Complex code may require refinement over multiple attempts
4. **Include your standards** - Add team conventions or style guides to your prompts for consistency

## Troubleshooting