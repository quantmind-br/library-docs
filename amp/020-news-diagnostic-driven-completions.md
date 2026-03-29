---
title: Diagnostic-Driven Completions
url: https://ampcode.com/news/diagnostic-driven-completions
source: crawler
fetched_at: 2026-02-06T02:08:39.905384937-03:00
rendered_js: false
word_count: 56
summary: This document explains how Amp Tab uses language server diagnostics to suggest follow-up edits and provide file-wide completions for resolving introduced errors.
tags:
    - amp-tab
    - language-server
    - diagnostics
    - code-completion
    - error-resolution
    - editor-features
category: concept
---

Amp Tab now uses language server diagnostics to suggest follow-up edits that resolve errors introduced by previous edits.

This means you can get completions across the entire file, not just in nearby code.

It's particularly useful when making changes that immediately introduce fixable errors, such as changing the signature of a function or renaming a variable.