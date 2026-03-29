---
title: Shareable Walkthroughs
url: https://ampcode.com/news/walkthrough
source: crawler
fetched_at: 2026-02-06T02:07:45.945226822-03:00
rendered_js: false
word_count: 315
summary: This document introduces Shareable Walkthroughs, an interactive tool for creating and sharing annotated diagrams that explain codebases, database schemas, and library functionalities.
tags:
    - ampcode
    - walkthrough-skill
    - code-visualization
    - interactive-diagrams
    - documentation-tools
    - diagram-generation
category: guide
---

Shareable Walkthroughs are a new interface we're trying—a way to create and share annotated diagrams with your team.

Ask Amp to use the walkthrough skill to explain a feature, function, database schema, or any part of your codebase. It generates an interactive diagram where each node contains detailed context. The Walkthrough diagram lets you start at a high level and drill down into the details you care about.

## Examples

### Understand how something in your codebase works

Ask the walkthrough skill to explain any part of your code with a clickable diagram that links directly to the source.

> Use the walkthrough skill and explain the process of what happens when an email invite is accepted by a user.
> 
> [View Walkthrough](https://ampcode.com/docs/T-019baa18-8416-71e8-8602-196914e94941)

![creating a code walkthrough](https://static.ampcode.com/news/flow_walkthrough.png)

### Combine with the librarian to understand libraries and packages

Pair the walkthrough skill with the librarian to explore how external libraries work—great for understanding new features or comparing versions.

> Use the librarian, look at Svelte version 5 and explain how event handling has been improved. Can you compare this to Svelte version 4? Use the walkthrough skill to explain the differences.
> 
> [View Walkthrough](https://ampcode.com/docs/T-019ba592-ddac-77c8-8d37-3f15223761e4)

### Generate different diagram types for your use case

The walkthrough skill can produce various diagram types. Just specify what you need—for example, ask for an ER diagram when exploring database relationships.

> Use the walkthrough skill and explain how the invites entity is stored in the database, what depends on it. Use an ER diagram.
> 
> [View Walkthrough](https://ampcode.com/docs/T-019ba5d4-4d79-74eb-a5b6-99bce84f2c20)

![creating a code erd walkthrough](https://static.ampcode.com/news/erd_walkthrough.png)

### Advanced: Combine with custom tools and data sources

You can pair the walkthrough skill with additional data sources and tools you've built to visualize answers to complex questions.

> Query the lineage SQLite database to find all dependencies for the `[calculated_field_name]` field in `[CTE_name]` job, then use the walkthrough skill to show how it's calculated and trace the impact of changing its logic—upstream sources, downstream consumers, and breaking changes.