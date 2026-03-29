---
title: Codebase Analysis | goose
url: https://block.github.io/goose/docs/guides/codebase-analysis
source: github_pages
fetched_at: 2026-01-22T22:13:35.658748969-03:00
rendered_js: true
word_count: 419
summary: This document explains how to use the analyze tool in the Goose Developer extension to explore code structure, inspect file details, and track symbol usage across a project.
tags:
    - goose-mcp
    - developer-extension
    - code-analysis
    - symbol-tracking
    - static-analysis
    - developer-tools
category: reference
---

The [Developer extension](https://block.github.io/goose/docs/mcp/developer-mcp) includes an `analyze` tool that helps you understand code structure, track symbol usage, and explore call graphs across your codebase. It's automatically available when the Developer extension is enabled and supports file types for [multiple programming languages](https://github.com/block/goose/blob/main/crates/goose-mcp/src/developer/analyze/languages/mod.rs).

Example analysis: Tracking a function across files

## Analysis Modes[​](#analysis-modes "Direct link to Analysis Modes")

The `analyze` tool operates in three modes—Structure, Semantic, and Focus—depending on whether you’re analyzing directories, files, or symbols. Invoke it through natural language or direct commands with [parameters](#common-parameters).

### Understanding Project Organization[​](#understanding-project-organization "Direct link to Understanding Project Organization")

Get a structural overview of your codebase by analyzing a directory—understand project organization, identify large files, and view codebase metrics.

**Natural language:**

- "Can you analyze the structure of my src/ directory?"
- "Give me an overview of this project's code structure"
- "What's the main entry point of this Python project?"

**Direct commands:**

```
# Get overview with default depth (3 levels)
analyze path="src/"

# Get overview limited to 2 subdirectory levels
analyze path="." max_depth=2
```

### Inspecting a File[​](#inspecting-a-file "Direct link to Inspecting a File")

Get semantic details for a single file—see its functions, classes, and imports to understand structure and find specific implementations.

**Natural language:**

- "What functions are in main.py?"
- "Show me the structure of src/utils.py"

**Direct commands:**

```
# Get file details
analyze path="main.py"

# Analyze specific file
analyze path="src/utils.py"
```

### Tracking a Symbol Across Files[​](#tracking-a-symbol-across-files "Direct link to Tracking a Symbol Across Files")

Focus on a specific function, class, or method to see where it’s defined and how it’s called across files—useful for refactoring and debugging.

**Natural language:**

- "Trace the dependencies for the authenticate function"
- "Show me the call graph for UserClass"

**Direct commands:**

```
# Track function usage
analyze path="src/" focus="authenticate"

# Track with deeper call chains
analyze path="." focus="UserClass" follow_depth=3
```

## Common Parameters[​](#common-parameters "Direct link to Common Parameters")

ParameterDefaultDescription`path`None (required)Absolute or relative path to the file or directory to analyze`focus`NoneName of the symbol to track. For cross-file tracking, `path` must be a directory.`follow_depth`2How many steps to trace from the focused symbol (0=where defined, 1=immediate callers/callees, 2=their callers/callees, etc.). Used with the `focus` parameter.`max_depth`3How many subdirectory levels to analyze when `path` is a directory (0=unlimited)`force`falseReceive full analysis results (otherwise, only a warning message is shown when the results exceed 1000 lines)

## Best Practices[​](#best-practices "Direct link to Best Practices")

### Handling Large Outputs[​](#handling-large-outputs "Direct link to Handling Large Outputs")

If the analysis results exceed 1000 lines, the tool returns a warning message instead of the analysis. Options for managing large outputs:

- **Use `force=true`** to bypass the warning and see the full output (may consume significant conversation context)
- **Narrow your scope** by analyzing a specific subdirectory or file
- **Reduce depth** with `max_depth=1` or `max_depth=2` for directories
- **Delegate to a [subagent](https://block.github.io/goose/docs/guides/subagents)** to analyze and summarize without filling your conversation history, for example: "Use a subagent to analyze the entire src/ directory and summarize the main components"

### Performance Tips[​](#performance-tips "Direct link to Performance Tips")

- Start with smaller scopes (specific files or subdirectories) before analyzing entire projects
- Use `max_depth=1` or `max_depth=2` to limit directory traversal depth
- Use [`.gooseignore`](https://block.github.io/goose/docs/guides/using-gooseignore) and `.gitignore` files to exclude unnecessary files from analysis (like `node_modules/`, build artifacts, or sensitive files)