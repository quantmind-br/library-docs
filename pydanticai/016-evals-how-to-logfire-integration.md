---
title: Logfire Integration - Pydantic AI
url: https://ai.pydantic.dev/evals/how-to/logfire-integration/
source: sitemap
fetched_at: 2026-01-22T22:25:32.082456462-03:00
rendered_js: false
word_count: 460
summary: This guide explains how to integrate Pydantic Evals with Pydantic Logfire to visualize, analyze, and debug evaluation results using OpenTelemetry traces. It covers installation, configuration, and best practices for monitoring evaluation performance.
tags:
    - pydantic-evals
    - pydantic-logfire
    - opentelemetry
    - observability
    - tracing
    - debugging
category: guide
---

Visualize and analyze evaluation results using Pydantic Logfire.

## Overview

Pydantic Evals uses OpenTelemetry to record traces of the evaluation process. These traces contain all the information from your evaluation reports, plus full tracing from the execution of your task function.

You can send these traces to any OpenTelemetry-compatible backend, including [Pydantic Logfire](https://logfire.pydantic.dev/docs/guides/web-ui/evals/).

## Installation

Install the optional logfire dependency:

```
pipinstall'pydantic-evals[logfire]'
```

## Basic Setup

Configure Logfire before running evaluations:

basic\_logfire\_setup.py

```
importlogfire

frompydantic_evalsimport Case, Dataset

# Configure Logfire
logfire.configure(
    send_to_logfire='if-token-present',  # (1)!
)


# Your evaluation code
defmy_task(inputs: str) -> str:
    return f'result for {inputs}'


dataset = Dataset(cases=[Case(name='test', inputs='example')])
report = dataset.evaluate_sync(my_task)
```

1. Sends data to Logfire only if the `LOGFIRE_TOKEN` environment variable is set

That's it! Your evaluation traces will now appear in the Logfire web UI as long as you have the `LOGFIRE_TOKEN` environment variable set.

## What Gets Sent to Logfire

When you run an evaluation, Logfire receives:

1. **Evaluation metadata**
   
   1. Dataset name
   2. Number of cases
   3. Evaluator names
2. **Per-case data**
   
   1. Inputs and outputs
   2. Expected outputs
   3. Metadata
   4. Execution duration
3. **Evaluation results**
   
   1. Scores, assertions, and labels
   2. Reasons (if included)
   3. Evaluator failures
4. **Task execution traces**
   
   1. All OpenTelemetry spans from your task function
   2. Tool calls (for Pydantic AI agents)
   3. API calls, database queries, etc.

## Viewing Results in Logfire

### Evaluation Overview

Logfire provides a special table view for evaluation results on the root evaluation span:

[![Logfire Evals Overview](https://ai.pydantic.dev/img/logfire-evals-overview.png)](https://ai.pydantic.dev/img/logfire-evals-overview.png)

This view shows:

- Case names
- Pass/fail status
- Scores and assertions
- Execution duration
- Quick filtering and sorting

### Individual Case Details

Click any case to see detailed inputs and outputs:

[![Logfire Evals Case](https://ai.pydantic.dev/img/logfire-evals-case.png)](https://ai.pydantic.dev/img/logfire-evals-case.png)

### Full Trace View

View the complete execution trace including all spans generated during evaluation:

[![Logfire Evals Case Trace](https://ai.pydantic.dev/img/logfire-evals-case-trace.png)](https://ai.pydantic.dev/img/logfire-evals-case-trace.png)

This is especially useful for:

- Debugging failed cases
- Understanding performance bottlenecks
- Analyzing tool usage patterns
- Writing span-based evaluators

## Analyzing Traces

### Comparing Runs

Run the same evaluation multiple times and compare in Logfire:

```
frompydantic_evalsimport Case, Dataset


deforiginal_task(inputs: str) -> str:
    return f'original result for {inputs}'


defimproved_task(inputs: str) -> str:
    return f'improved result for {inputs}'


dataset = Dataset(cases=[Case(name='test', inputs='example')])

# Run 1: Original implementation
report1 = dataset.evaluate_sync(original_task)

# Run 2: Improved implementation
report2 = dataset.evaluate_sync(improved_task)

# Compare in Logfire by filtering by timestamp or attributes
```

### Debugging Failed Cases

Find failed cases quickly:

1. Search for `service_name = 'my_service_evals' AND is_exception` (replace with the actual service name you are using)
2. View the full span tree to see where the failure occurred
3. Inspect attributes and logs for error messages

## Span-Based Evaluation

Logfire integration enables powerful span-based evaluators. See [Span-Based Evaluation](https://ai.pydantic.dev/evals/evaluators/span-based/) for details.

Example: Verify specific tools were called:

```
importlogfire

frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport HasMatchingSpan

logfire.configure(send_to_logfire='if-token-present')


defmy_agent(inputs: str) -> str:
    return f'result for {inputs}'


dataset = Dataset(
    cases=[Case(name='test', inputs='example')],
    evaluators=[
        HasMatchingSpan(
            query={'name_contains': 'search_tool'},
            evaluation_name='used_search',
        ),
    ],
)

report = dataset.evaluate_sync(my_agent)
```

The span tree is available in both:

- Your evaluator code (via `ctx.span_tree`)
- Logfire UI (visual trace view)

## Troubleshooting

### No Data Appearing in Logfire

Check:

1. **Token is set**: `echo $LOGFIRE_TOKEN`
2. **Configuration is correct**:
   
   ```
   importlogfire
   
   logfire.configure(send_to_logfire='always')  # Force sending
   ```
3. **Network connectivity**: Check firewall settings
4. **Project exists**: Verify project name in Logfire UI

### Traces Missing Spans

If some spans are missing:

1. **Ensure logfire is configured before imports**:
   
   ```
   importlogfire
   
   logfire.configure()  # Must be first
   ```
2. **Check instrumentation**: Ensure your code has enabled all instrumentations you want:
   
   ```
   importlogfire
   
   logfire.instrument_pydantic_ai()
   logfire.instrument_httpx(capture_all=True)
   ```

## Best Practices

### 1. Configure Early

Always configure Logfire before running evaluations:

```
importlogfire

frompydantic_evalsimport Case, Dataset

logfire.configure(send_to_logfire='if-token-present')


# Now import and run evaluations
deftask(inputs: str) -> str:
    return f'result for {inputs}'


dataset = Dataset(cases=[Case(name='test', inputs='example')])
dataset.evaluate_sync(task)
```

### 2. Use Descriptive Service Names And Environments

```
importlogfire

logfire.configure(
    service_name='rag-pipeline-evals',
    environment='development',
)
```

### 3. Review Periodically

- Check Logfire regularly to identify patterns
- Look for consistently failing cases
- Analyze performance trends
- Adjust evaluators based on insights

## Next Steps

- [**Span-Based Evaluation**](https://ai.pydantic.dev/evals/evaluators/span-based/) - Use OpenTelemetry spans in evaluators
- [**Logfire Documentation**](https://logfire.pydantic.dev/docs/guides/web-ui/evals/) - Complete Logfire guide
- [**Metrics & Attributes**](https://ai.pydantic.dev/evals/how-to/metrics-attributes/) - Add custom data to traces