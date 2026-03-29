---
title: Project Structure
url: https://ratatui.rs/templates/component/project-structure/
source: crawler
fetched_at: 2026-02-01T21:13:24.992285559-03:00
rendered_js: false
word_count: 61
summary: This document provides an overview of the directory structure and file organization for a component-based Rust project, explaining the purpose of various source files.
tags:
    - rust
    - project-structure
    - file-organization
    - component-architecture
    - source-code-layout
category: reference
---

The rust files in the `component` project are organized as follows:

```

$tree
.
├──build.rs
└──src
├──action.rs
├──app.rs
├──cli.rs
├──components
│  ├──fps.rs
│  └──home.rs
├──components.rs
├──config.rs
├──errors.rs
├──logging.rs
├──main.rs
└──tui.rs
```

Once you have set up the project, you shouldn’t need to change the contents of anything outside the `components` folder.

Let’s discuss the contents of the files in the `src` folder first, how these contents of these files interact with each other and why they do what they are doing.