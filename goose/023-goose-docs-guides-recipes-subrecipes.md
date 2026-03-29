---
title: Subrecipes For Specialized Tasks | goose
url: https://block.github.io/goose/docs/guides/recipes/subrecipes
source: github_pages
fetched_at: 2026-01-22T22:14:17.672125224-03:00
rendered_js: true
word_count: 469
summary: This document explains how to use subrecipes to create modular, reusable components and multi-step workflows within the Goose framework. It details configuration, parameter passing, and best practices for implementing isolated sub-tasks.
tags:
    - sub-recipes
    - workflow-automation
    - goose-recipes
    - modular-design
    - parameter-passing
    - configuration-guide
category: guide
---

Subrecipes are recipes that are used by another recipe to perform specific tasks. They enable:

- **Multi-step workflows** - Break complex tasks into distinct phases with specialized expertise
- **Reusable components** - Create common tasks that can be used in various workflows

Experimental Feature

Subrecipes are an experimental feature in active development. Behavior and configuration may change in future releases.

## How Subrecipes Work[​](#how-subrecipes-work "Direct link to How Subrecipes Work")

The "main recipe" registers its subrecipes in the `sub_recipes` field, which contains the following fields:

- `name`: Unique identifier for the subrecipe, used to generate the tool name
- `path`: File path to the subrecipe file (relative or absolute)
- `values`: (Optional) Pre-configured parameter values that are always passed to the subrecipe

When the main recipe is run, goose generates a tool for each subrecipe that:

- Accepts parameters defined by the subrecipe
- Executes the subrecipe in a separate session with its own context
- Returns output to the main recipe

Sub-recipe sessions run in isolation - they don't share conversation history, memory, or state with the main recipe or other subrecipes. Additionally, subrecipes cannot define their own subrecipes (no nesting allowed).

### Parameter Handling[​](#parameter-handling "Direct link to Parameter Handling")

Parameters received by subrecipes can be used in prompts and instructions using `{{ parameter_name }}` syntax. Subrecipes receive parameters in two ways:

1. **Pre-set values**: Fixed parameter values defined in the `values` field are automatically provided and cannot be overridden at runtime
2. **Context-based parameters**: The AI agent can extract parameter values from the conversation context, including results from previous subrecipes

Pre-set values take precedence over context-based parameters. If both the conversation context and `values` field provide the same parameter, the `values` version is used.

tip

Use the `indent()` filter to maintain valid YAML format when passing multi-line parameter values to subrecipes, for example: `{{ content | indent(2) }}`. See [Template Support](https://block.github.io/goose/docs/guides/recipes/recipe-reference#template-support) for more details.

## Examples[​](#examples "Direct link to Examples")

### Sequential Processing[​](#sequential-processing "Direct link to Sequential Processing")

This Code Review Pipeline example shows a main recipe that uses two subrecipes to perform a comprehensive code review:

**Usage:**

```
goose run --recipe code-review-pipeline.yaml --params repository_path=/path/to/repo
```

**Main Recipe:**

```
# code-review-pipeline.yaml
version:"1.0.0"
title:"Code Review Pipeline"
description:"Automated code review using subrecipes"
instructions:|
  Perform a code review using the available subrecipe tools.
  Run security analysis first, then code quality analysis.

parameters:
-key: repository_path
input_type: string
requirement: required
description:"Path to the repository to review"

sub_recipes:
-name:"security_scan"
path:"./subrecipes/security-analysis.yaml"
values:
scan_level:"comprehensive"

-name:"quality_check"
path:"./subrecipes/quality-analysis.yaml"

extensions:
-type: builtin
name: developer
timeout:300
bundled:true

prompt:|
  Review the code at {{ repository_path }} using the subrecipe tools.
  Run security scan first, then quality analysis.
```

**Subrecipes:**

security\_scan

quality\_check

### Conditional Processing[​](#conditional-processing "Direct link to Conditional Processing")

This Smart Project Analyzer example shows conditional logic that chooses between different subrecipes based on analysis:

**Usage:**

```
goose run --recipe smart-analyzer.yaml --params repository_path=/path/to/project
```

**Main Recipe:**

```
# smart-analyzer.yaml
version:"1.0.0"
title:"Smart Project Analyzer"
description:"Analyze project and choose appropriate processing based on type"
instructions:|
  First examine the repository to determine the project type (web app, CLI tool, library, etc.).
  Based on what you find:
  - If it's a web application, use the web_security_audit subrecipe
  - If it's a CLI tool or library, use the api_documentation subrecipe
  Only run one subrecipe based on your analysis.

parameters:
-key: repository_path
input_type: string
requirement: required
description:"Path to the repository to analyze"

sub_recipes:
-name:"web_security_audit"
path:"./subrecipes/web-security.yaml"
values:
check_cors:"true"
check_csrf:"true"

-name:"api_documentation"
path:"./subrecipes/api-docs.yaml"
values:
format:"markdown"

extensions:
-type: builtin
name: developer
timeout:300
bundled:true

prompt:|
  Analyze the project at {{ repository_path }} and determine its type.
  Then run the appropriate subrecipe tool based on your findings.
```

**Subrecipes:**

web\_security\_audit

api\_documentation

### Context-Based Parameter Passing[​](#context-based-parameter-passing "Direct link to Context-Based Parameter Passing")

This Travel Planner example shows how subrecipes can receive parameters from conversation context, including results from previous subrecipes:

**Usage:**

```
goose run --recipe travel-planner.yaml
```

**Main Recipe:**

```
# travel-planner.yaml
version:"1.0.0"
title:"Travel Activity Planner"
description:"Get weather data and suggest appropriate activities"
instructions:|
  Plan activities by first getting weather data, then suggesting activities based on conditions.

prompt:|
  Plan activities for Sydney by first getting weather data, then suggesting activities based on the weather conditions we receive.

sub_recipes:
-name: weather_data
path:"./subrecipes/weather-data.yaml"
# No values - location parameter comes from prompt context

-name: activity_suggestions
path:"./subrecipes/activity-suggestions.yaml"
# weather_conditions parameter comes from conversation context

extensions:
-type: builtin
name: developer
timeout:300
bundled:true
```

**Subrecipes:**

weather\_data

activity\_suggestions

In this example:

- The `weather_data` subrecipe gets the location from the prompt context (the AI extracts "Sydney" from the natural language prompt)
- The `activity_suggestions` subrecipe gets weather conditions from the conversation context (the AI uses the weather results from the first subrecipe)

## Best Practices[​](#best-practices "Direct link to Best Practices")

- **Single responsibility**: Each subrecipe should have one clear purpose
- **Clear parameters**: Use descriptive names and descriptions
- **Pre-set fixed values**: Use `values` for parameters that don't change
- **Test independently**: Verify subrecipes work alone before combining

## Learn More[​](#learn-more "Direct link to Learn More")

Check out the [Recipes](https://block.github.io/goose/docs/guides/recipes) guide for more docs, tools, and resources to help you master goose recipes.