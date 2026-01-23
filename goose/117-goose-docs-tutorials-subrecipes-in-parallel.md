---
title: Running Subrecipes In Parallel | goose
url: https://block.github.io/goose/docs/tutorials/subrecipes-in-parallel
source: github_pages
fetched_at: 2026-01-22T22:16:26.963330758-03:00
rendered_js: true
word_count: 548
summary: This document explains how to execute goose subrecipes concurrently using isolated worker processes to optimize batch operations and complex workflows. It details configuration settings, prompting techniques for parallel execution, and methods for monitoring progress via the CLI.
tags:
    - goose-recipes
    - parallel-processing
    - subrecipes
    - concurrency
    - workflow-optimization
    - cli-dashboard
category: guide
---

goose recipes can execute multiple [subrecipe](https://block.github.io/goose/docs/guides/recipes/subrecipes) instances concurrently using isolated worker processes. This feature enables efficient batch operations, parallel processing of different tasks, and faster completion of complex workflows.

Experimental Feature

Running subrecipes in parallel is an experimental feature in active development. Behavior and configuration may change in future releases.

Here are some common use cases:

- **Monorepo build failures**: When 3 services fail in a monorepo build, use a "diagnose failure" subrecipe with each build URL to diagnose all failures in parallel
- **Document summarization**: Process a CSV file with document links by running a "summarize document" subrecipe for each link simultaneously
- **Code analysis across repositories**: Run security, quality, and performance analysis on multiple codebases simultaneously

## How It Works[​](#how-it-works "Direct link to How It Works")

Parallel subrecipe execution uses an isolated worker system that automatically manages concurrent task execution. goose creates individual tasks for each subrecipe instance and distributes them across up to 10 concurrent workers.

ScenarioDefault BehaviorOverride Options**Different subrecipes**SequentialAdd "in parallel" to prompt**Same subrecipe** with different parametersParallel• Set `sequential_when_repeated: true`  
• Add "sequentially" to prompt

### Different Subrecipes[​](#different-subrecipes "Direct link to Different Subrecipes")

When running different subrecipes, goose determines the execution mode based on:

1. **Explicit user request** in the prompt ("in parallel", "sequentially")
2. **Sequential execution by default**: Different subrecipes run one after another unless explicitly requested to run in parallel

In your prompt, you can simply mention "in parallel" in your prompt when calling different subrecipes:

```
prompt:|
  run the following subrecipes in parallel:
    - use weather subrecipe to get the weather for Sydney
    - use things-to-do subrecipe to find activities in Sydney
```

### Same Subrecipe[​](#same-subrecipe "Direct link to Same Subrecipe")

When running the same subrecipe with different parameters, goose determines the execution mode based on:

1. [**Recipe-level configuration**](#choosing-between-execution-modes) (`sequential_when_repeated` flag) - when set to true, this forces sequential execution
2. **User request** in the prompt ("sequentially" to override default parallel behavior)
3. **Parallel execution by default**: Multiple instances of the same subrecipe run concurrently

If your prompt implies multiple executions of the same subrecipe, goose will automatically create parallel instances:

```
prompt:|
  get the weather for three biggest cities in Australia
```

In this example, goose recognizes that "three biggest cities" requires running the weather subrecipe multiple times for different cities, so it executes them in parallel.

If you wanted to run them sequentially, you can just tell goose:

```
prompt:|
  get the weather for three biggest cities in Australia one at a time
```

### Real-Time Progress Monitoring[​](#real-time-progress-monitoring "Direct link to Real-Time Progress Monitoring")

When running multiple tasks in parallel from the CLI, you can track progress through a real-time dashboard that automatically appears during execution. The dashboard provides:

- **Live progress tracking**: Monitor task completion in real-time with statistics for completed, running, failed, and pending counts
- **Task details**: View unique task IDs, parameter sets, execution timing, output previews, and error information as tasks progress from Pending → Running → Completed/Failed

## Examples[​](#examples "Direct link to Examples")

### Running Different Subrecipes in Parallel[​](#running-different-subrecipes-in-parallel "Direct link to Running Different Subrecipes in Parallel")

This example runs the `weather` and `things-to-do` subrecipes in parallel:

```
# plan_trip.yaml
version: 1.0.0
title: Plan Your Trip
description: Get weather forecast and find things to do for your destination
instructions: You are a travel planning assistant that helps users prepare for their trips.
prompt:|
  run the following subrecipes in parallel to plan my trip:
    - use weather subrecipe to get the weather forecast for Sydney
    - use things-to-do subrecipe to find activities and attractions in Sydney
sub_recipes:
-name: weather
path:"./subrecipes/weather.yaml"
values:
city: Sydney
-name: things-to-do
path:"./subrecipes/things-to-do.yaml"
values:
city: Sydney
duration:"3 days"
extensions:
-type: builtin
name: developer
timeout:300
bundled:true
```

### Running the Same Subrecipe in Parallel (with Different Parameters)[​](#running-the-same-subrecipe-in-parallel-with-different-parameters "Direct link to Running the Same Subrecipe in Parallel (with Different Parameters)")

This example runs three instances of the `weather` subrecipe in parallel for different cities:

```
# multi_city_weather.yaml
version: 1.0.0
title: Multi-City Weather Comparison
description: Compare weather across multiple cities for trip planning
instructions: You are a travel weather specialist helping users compare conditions across cities.
prompt:|
  get the weather forecast for the three biggest cities in Australia 
  to help me decide where to visit
sub_recipes:
-name: weather
path:"./subrecipes/weather.yaml"
extensions:
-type: builtin
name: developer
timeout:300
bundled:true
```

**Subrecipes:**

weather

things-to-do

## Choosing Between Execution Modes[​](#choosing-between-execution-modes "Direct link to Choosing Between Execution Modes")

While parallel execution offers speed benefits, sequential execution is sometimes necessary or preferable. Here's how to decide:

**Use Sequential When:**

- Tasks modify shared resources
- Order of execution matters
- Memory or CPU constraints exist
- Debugging complex failures in parallel mode

**Use Parallel When:**

- Tasks are independent
- Faster completion is desired
- System resources can handle concurrent executions for up to 10 parallel workers
- Processing large datasets or multiple files

**Recipe-Level Configuration:**

For subrecipes that should never run in parallel, set `sequential_when_repeated: true` to override user requests:

```
sub_recipes:
-name: database-migration
path:"./subrecipes/migrate.yaml"
sequential_when_repeated:true# Always sequential
```

## Learn More[​](#learn-more "Direct link to Learn More")

Check out the [Recipes](https://block.github.io/goose/docs/guides/recipes) guide for more docs, tools, and resources to help you master goose recipes.