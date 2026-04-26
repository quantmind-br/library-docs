---
title: Concurrency Patterns | Mistral Docs
url: https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/concurrency
source: sitemap
fetched_at: 2026-04-26T04:14:23.922787553-03:00
rendered_js: false
word_count: 1156
summary: This document outlines the concurrency framework in Mistral Workflows, providing patterns for parallelizing tasks across large datasets while managing fault tolerance and resource limits.
tags:
    - concurrency
    - workflows
    - parallel-processing
    - fault-tolerance
    - data-pagination
    - scalability
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Process thousands of items efficiently with Mistral Workflows' parallel execution patterns.

**Small batches**: For fewer than ~10,000 activities, `asyncio.gather` works well and keeps your code simple. Use the concurrency framework below when you need automatic continue-as-new, progress tracking, or are processing larger datasets that could exceed the 51,200-event history limit.

## Executor Patterns

Mistral Workflows provides a concurrency framework that enables you to execute activities in parallel across three distinct patterns:

| Pattern | Use Case |
|---------|----------|
| **List Executor** | Process a known collection of items |
| **Chain Executor** | Process items sequentially from a stream/queue (token-based pagination) |
| **Offset Pagination Executor** | Process items by fetching pages/chunks by index |

All patterns provide:
- **Massive Parallelism**: Execute thousands of activities concurrently
- **Automatic Continue-As-New**: Handle large datasets without hitting execution history limits (51,200 events)
- **Type Safety**: Comprehensive type validation for all inputs and outputs
- **Fault Tolerance**: Built-in error handling and retry mechanisms
- **Progress Tracking**: Monitor execution progress through built-in observability features

## List Executor

Process a known collection of items where you have all items upfront.

Use cases:
- Database query results
- File contents or uploaded documents
- API responses that return all items at once
- Batch processing of users, files, or records

> [!note] The List Executor doesn't use `max_concurrent_executions_per_worker` parameter. This parameter is only relevant for the Offset Pagination Executor.

## Chain Executor

Process items sequentially from a stream/queue using token-based pagination.

Use cases:
- AWS S3 ListObjects (uses ContinuationToken)
- DynamoDB Scan/Query (uses LastEvaluatedKey)
- Azure Blob Storage (uses marker)
- Any API that uses continuation tokens instead of page numbers

> [!note] The Chain Executor doesn't use `max_concurrent_scheduled_tasks` or `max_concurrent_executions_per_worker` parameters.

The Chain Executor separates **item discovery** (sequential) from **item processing** (parallel):

1. **Item fetching is chained**: The executor calls `get_item_from_prev_item_activity` sequentially—first with `None` to get the first item, then with each result to get the next item, until the function returns `None`
2. **Processing is parallelized**: As soon as an item is fetched, it's immediately dispatched for processing via the `activity` function. Items don't wait for each other to finish processing

This means fetching item N+1 depends on item N's result, but *processing* item N+1 runs concurrently with processing items 1 through N.

## Offset Pagination Executor

Process items by fetching pages/chunks using index-based pagination.

Use cases:
- Traditional REST APIs with page numbers
- SQL database chunking with OFFSET/LIMIT
- File processing by byte offset
- Any index-based data fetching

> [!warning] Items processed together are wrapped in a single activity. If any item fails, the entire group is retried together.

### Best Practices

The Offset Pagination Executor uses two key parameters:

1. **`max_concurrent_executions_per_worker`** — Controls how many items are processed together in a single activity execution.
2. **`max_concurrent_scheduled_tasks`** — Controls how many of these activity executions can run concurrently.

**Example**: If you have 1000 items with `max_concurrent_executions_per_worker=10` and `max_concurrent_scheduled_tasks=5`, the system will:
- Process items in groups of 10
- Execute up to 5 groups concurrently
- Process all items efficiently while maintaining manageable group sizes

**Important**: All items processed together are wrapped in a single activity. This means:
- **Pros**: Efficient processing, reduced overhead
- **Cons**: If any single item in a group fails, the entire group is retried

**Best Practices**:
- Choose `max_concurrent_executions_per_worker` values that balance efficiency with retry granularity
- Smaller values: More fine-grained retries, but higher overhead
- Larger values: More efficient, but larger retry scope
- Consider item failure rates when choosing values

## Configuration Guidelines

| Workload Type | Group Size | Concurrency | Example |
|---------------|------------|-------------|---------|
| I/O-bound (API calls, DB) | 50-100 | 100-200 | `max_concurrent_executions_per_worker=50, max_concurrent_scheduled_tasks=150` |
| CPU-bound | 5-20 | 20-50 | `max_concurrent_executions_per_worker=10, max_concurrent_scheduled_tasks=30` |
| Mixed | 20-50 | 50-100 | `max_concurrent_executions_per_worker=25, max_concurrent_scheduled_tasks=75` |

> [!warning]
> - **Group size impacts memory usage**: Larger groups consume more memory per activity
> - **Concurrency impacts resource contention**: Higher concurrency may lead to resource exhaustion
> - **Size limits**: Remember the 2MB input/output limit per activity

## Automatic Handling

The concurrency framework automatically handles:
- Activity failures with retry mechanisms
- Type validation errors
- Workflow continuation for large datasets
- Progress tracking and state management

For very large datasets, the framework automatically handles continue-as-new:

```python
```

## Use Cases

**Document OCR**: Extract text from a set of documents in parallel using an OCR service. Each document is processed as a separate activity, so failures are isolated — a single failed extraction doesn't block the rest.

**User Enrichment**: Enrich user records by fetching data from multiple external services. The `max_concurrent_scheduled_tasks` parameter caps how many activities run at once, preventing you from overwhelming downstream services.

**Order Processing**: Process pending orders by coordinating payment, inventory, and shipping services. Each order is handled as its own activity, and within each activity the service calls run in parallel.

## Optimization Notes

- Large datasets are processed efficiently to avoid memory issues
- The continue-as-new mechanism ensures workflow state remains manageable
- Each activity execution is isolated with its own memory footprint
- Activities can be executed on workers close to data sources
- Use `sticky_to_worker=True` for activities that benefit from locality
- Configure appropriate concurrency limits based on network bandwidth

## Error Handling

- Failed activities are automatically retried according to their retry policy
- The framework maintains progress state, so only failed items need reprocessing
- Implement custom event recording with `workflows.record_event()`
- Set up alerts for long-running or failed executions

## Common Issues

**Issue**: `ValueError: 'activity' must be an activity, please decorate it with @workflows.activity`

**Solution**: Ensure your activity function is decorated with `@workflows.activity()`

**Issue**: `ValueError: Must specify one execution pattern`

**Solution**: Provide exactly one of: `items`, `get_item_from_prev_item_activity`, or `get_item_from_index_activity`

**Issue**: Excessive retries with Offset Pagination Executor

**Solution**: If you're experiencing excessive retries with the Offset Pagination Executor, consider:
- Reducing `max_concurrent_executions_per_worker` to create smaller groups of items
- Investigating individual item failures that might be causing entire groups to retry
- Adding better error handling within your activity to prevent failures

**Issue**: Memory issues with large groups

**Solution**: If you encounter memory issues:
- Reduce `max_concurrent_executions_per_worker` to process fewer items together
- Ensure individual items are not too large (remember the 2MB limit)
- Monitor memory usage and adjust group sizes accordingly

## Debugging

1. **Check Activity Signatures**: Ensure all activities have proper type annotations
2. **Validate Concurrency Limits**: Start with lower concurrency and increase gradually
3. **Use Logging**: Add detailed logging in your activities for debugging
4. **Offset Pagination Debugging**: For Offset Pagination Executor issues:
   - Start with small values (e.g., `max_concurrent_executions_per_worker=1`)
   - Check for individual item failures that might affect entire groups

## Parameters

| Parameter | Executor | Description |
|-----------|----------|-------------|
| `activity` | all | The activity function to execute on each item |
| `items` | List | List of items to process |
| `get_item_from_prev_item_activity` | Chain | Function to get next item from previous |
| `get_item_from_index_activity` | Offset Pagination | Function to get item by index |
| `n_items` | Offset Pagination | Total number of items |
| `max_concurrent_scheduled_tasks` | List, Offset Pagination | Maximum number of concurrent activity executions |
| `max_concurrent_executions_per_worker` | Offset Pagination only | Controls how many items are processed together in a single activity execution |
| `extra_params` | all | Extra parameters to pass to activities |

**Returns**:
- `None` if activity returns None
- `List[U]` list of activity results

**Raises**:
- `ValueError`: If activity is not properly decorated or parameters are invalid