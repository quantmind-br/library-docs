---
title: Retry Strategies - Pydantic AI
url: https://ai.pydantic.dev/evals/how-to/retry-strategies/
source: sitemap
fetched_at: 2026-01-22T22:25:33.745406755-03:00
rendered_js: false
word_count: 334
summary: This document explains how to implement automatic retry logic for tasks and evaluators using the Tenacity library to handle transient failures like rate limits and network timeouts.
tags:
    - pydantic-evals
    - tenacity
    - error-handling
    - retries
    - rate-limiting
    - exponential-backoff
category: guide
---

Handle transient failures in tasks and evaluators with automatic retry logic.

## Overview

LLM-based systems can experience transient failures:

- Rate limits
- Network timeouts
- Temporary API outages
- Context length errors

Pydantic Evals supports retry configuration for both:

- **Task execution** - The function being evaluated
- **Evaluator execution** - The evaluators themselves

## Basic Retry Configuration

Pass a retry configuration to `evaluate()` or `evaluate_sync()` using [Tenacity](https://tenacity.readthedocs.io/) parameters:

```
fromtenacityimport stop_after_attempt

frompydantic_evalsimport Case, Dataset


defmy_function(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

report = dataset.evaluate_sync(
    task=my_function,
    retry_task={'stop': stop_after_attempt(3)},
    retry_evaluators={'stop': stop_after_attempt(2)},
)
```

## Retry Configuration Options

Retry configurations use [Tenacity](https://tenacity.readthedocs.io/) and support the same options as Pydantic AI's [`RetryConfig`](https://ai.pydantic.dev/api/retries/#pydantic_ai.retries.RetryConfig "RetryConfig"):

```
fromtenacityimport stop_after_attempt, wait_exponential

frompydantic_evalsimport Case, Dataset


defmy_function(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

retry_config = {
    'stop': stop_after_attempt(3),  # Stop after 3 attempts
    'wait': wait_exponential(multiplier=1, min=1, max=10),  # Exponential backoff: 1s, 2s, 4s, 8s (capped at 10s)
    'reraise': True,  # Re-raise the original exception after exhausting retries
}

dataset.evaluate_sync(
    task=my_function,
    retry_task=retry_config,
)
```

### Common Parameters

The retry configuration accepts any parameters from the tenacity `retry` decorator. Common ones include:

Parameter Type Description `stop` `StopBaseT` Stop strategy (e.g., `stop_after_attempt(3)`, `stop_after_delay(60)`) `wait` `WaitBaseT` Wait strategy (e.g., `wait_exponential()`, `wait_fixed(2)`) `retry` `RetryBaseT` Retry condition (e.g., `retry_if_exception_type(TimeoutError)`) `reraise` `bool` Whether to reraise the original exception (default: `False`) `before_sleep` `Callable` Callback before sleeping between retries

See the [Tenacity documentation](https://tenacity.readthedocs.io/) for all available options.

## Task Retries

Retry the task function when it fails:

```
fromtenacityimport stop_after_attempt, wait_exponential

frompydantic_evalsimport Case, Dataset


async defcall_llm(inputs: str) -> str:
    return f'LLM response to: {inputs}'


async defflaky_llm_task(inputs: str) -> str:
"""This might hit rate limits or timeout."""
    response = await call_llm(inputs)
    return response


dataset = Dataset(cases=[Case(inputs='test')])

report = dataset.evaluate_sync(
    task=flaky_llm_task,
    retry_task={
        'stop': stop_after_attempt(5),  # Try up to 5 times
        'wait': wait_exponential(multiplier=1, min=1, max=30),  # Exponential backoff, capped at 30s
        'reraise': True,
    },
)
```

### When Task Retries Trigger

Retries trigger when the task raises an exception:

```
classRateLimitError(Exception):
    pass


classValidationError(Exception):
    pass


async defcall_api(inputs: str) -> str:
    return f'API response: {inputs}'


async defmy_task(inputs: str) -> str:
    try:
        return await call_api(inputs)
    except RateLimitError:
        # Will trigger retry
        raise
    except ValidationError:
        # Will also trigger retry
        raise
```

### Exponential Backoff

When using `wait_exponential()`, delays increase exponentially:

```
Attempt 1: immediate
Attempt 2: ~1s delay (multiplier * 2^0)
Attempt 3: ~2s delay (multiplier * 2^1)
Attempt 4: ~4s delay (multiplier * 2^2)
Attempt 5: ~8s delay (multiplier * 2^3, capped at max)
```

The actual delay depends on the `multiplier`, `min`, and `max` parameters passed to `wait_exponential()`.

## Evaluator Retries

Retry evaluators when they fail:

```
fromtenacityimport stop_after_attempt, wait_exponential

frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport LLMJudge


defmy_task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # LLMJudge might hit rate limits
        LLMJudge(rubric='Response is accurate'),
    ],
)

report = dataset.evaluate_sync(
    task=my_task,
    retry_evaluators={
        'stop': stop_after_attempt(3),
        'wait': wait_exponential(multiplier=1, min=0.5, max=10),
        'reraise': True,
    },
)
```

### When Evaluator Retries Trigger

Retries trigger when an evaluator raises an exception:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


async defexternal_api_call(output: str) -> bool:
    return len(output) > 0


@dataclass
classAPIEvaluator(Evaluator):
    async defevaluate(self, ctx: EvaluatorContext) -> bool:
        # If this raises an exception, retry logic will trigger
        result = await external_api_call(ctx.output)
        return result
```

### Evaluator Failures

If an evaluator fails after all retries, it's recorded as an [`EvaluatorFailure`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorFailure "EvaluatorFailure            dataclass   "):

```
fromtenacityimport stop_after_attempt

frompydantic_evalsimport Case, Dataset


deftask(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

report = dataset.evaluate_sync(task, retry_evaluators={'stop': stop_after_attempt(3)})

# Check for evaluator failures
for case in report.cases:
    if case.evaluator_failures:
        for failure in case.evaluator_failures:
            print(f'Evaluator {failure.name} failed: {failure.error_message}')
    #> (No output - no evaluator failures in this case)
```

View evaluator failures in reports:

```
frompydantic_evalsimport Case, Dataset


deftask(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])
report = dataset.evaluate_sync(task)

report.print(include_evaluator_failures=True)
"""
  Evaluation Summary:
         task
┏━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID  ┃ Duration ┃
┡━━━━━━━━━━╇━━━━━━━━━━┩
│ Case 1   │     10ms │
├──────────┼──────────┤
│ Averages │     10ms │
└──────────┴──────────┘
"""
#>
#> ✅ case_0                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% (0/0)
```

## Combining Task and Evaluator Retries

You can configure both independently:

```
fromtenacityimport stop_after_attempt, wait_exponential

frompydantic_evalsimport Case, Dataset


defflaky_task(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

report = dataset.evaluate_sync(
    task=flaky_task,
    retry_task={
        'stop': stop_after_attempt(5),  # Retry task up to 5 times
        'wait': wait_exponential(multiplier=1, min=1, max=30),
        'reraise': True,
    },
    retry_evaluators={
        'stop': stop_after_attempt(3),  # Retry evaluators up to 3 times
        'wait': wait_exponential(multiplier=1, min=0.5, max=10),
        'reraise': True,
    },
)
```

## Practical Examples

### Rate Limit Handling

```
fromtenacityimport stop_after_attempt, wait_exponential

frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport LLMJudge


async defexpensive_llm_call(inputs: str) -> str:
    return f'LLM response: {inputs}'


async defllm_task(inputs: str) -> str:
"""Task that might hit rate limits."""
    return await expensive_llm_call(inputs)


dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        LLMJudge(rubric='Quality check'),  # Also might hit rate limits
    ],
)

# Generous retries for rate limits
report = dataset.evaluate_sync(
    task=llm_task,
    retry_task={
        'stop': stop_after_attempt(10),  # Rate limits can take multiple retries
        'wait': wait_exponential(multiplier=2, min=2, max=60),  # Start at 2s, exponential up to 60s
        'reraise': True,
    },
    retry_evaluators={
        'stop': stop_after_attempt(5),
        'wait': wait_exponential(multiplier=2, min=2, max=30),
        'reraise': True,
    },
)
```

### Network Timeout Handling

```
importhttpx
fromtenacityimport stop_after_attempt, wait_exponential

frompydantic_evalsimport Case, Dataset


async defapi_task(inputs: str) -> str:
"""Task that calls external API which might timeout."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.post('https://api.example.com', json={'input': inputs})
        return response.text


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Quick retries for network issues
report = dataset.evaluate_sync(
    task=api_task,
    retry_task={
        'stop': stop_after_attempt(4),  # A few quick retries
        'wait': wait_exponential(multiplier=0.5, min=0.5, max=5),  # Fast retry, capped at 5s
        'reraise': True,
    },
)
```

### Context Length Handling

```
fromtenacityimport stop_after_attempt

frompydantic_evalsimport Case, Dataset


classContextLengthError(Exception):
    pass


async defllm_call(inputs: str, max_tokens: int = 8000) -> str:
    return f'LLM response: {inputs[:100]}'


async defsmart_llm_task(inputs: str) -> str:
"""Task that might exceed context length."""
    try:
        return await llm_call(inputs, max_tokens=8000)
    except ContextLengthError:
        # Retry with shorter context
        truncated_inputs = inputs[:4000]
        return await llm_call(truncated_inputs, max_tokens=4000)


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Don't retry context length errors (handle in task)
report = dataset.evaluate_sync(
    task=smart_llm_task,
    retry_task={'stop': stop_after_attempt(1)},  # No retries, we handle it
)
```

## Retry vs Error Handling

**Use retries for:** - Transient failures (rate limits, timeouts) - Network issues - Temporary service outages - Recoverable errors

**Use error handling for:** - Validation errors - Logic errors - Permanent failures - Expected error conditions

```
classRateLimitError(Exception):
    pass


async defllm_call(inputs: str) -> str:
    return f'LLM response: {inputs}'


defis_valid(result: str) -> bool:
    return len(result) > 0


async defsmart_task(inputs: str) -> str:
"""Handle expected errors, let retries handle transient failures."""
    try:
        result = await llm_call(inputs)

        # Validate output (don't retry validation errors)
        if not is_valid(result):
            return 'ERROR: Invalid output format'

        return result

    except RateLimitError:
        # Let retry logic handle this
        raise

    except ValueError as e:
        # Don't retry - this is a permanent error
        return f'ERROR: {e}'
```

## Troubleshooting

### "Still failing after retries"

Increase retry attempts or check if error is retriable:

```
importlogging

fromtenacityimport stop_after_attempt

frompydantic_evalsimport Case, Dataset


deftask(inputs: str) -> str:
    return f'Result: {inputs}'


# Add logging to see what's failing
logging.basicConfig(level=logging.DEBUG)

dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Tenacity logs retry attempts
report = dataset.evaluate_sync(task, retry_task={'stop': stop_after_attempt(5)})
```

### "Evaluations taking too long"

Reduce retry attempts or wait times:

```
fromtenacityimport stop_after_attempt, wait_exponential

# Faster retries
retry_config = {
    'stop': stop_after_attempt(3),  # Fewer attempts
    'wait': wait_exponential(multiplier=0.1, min=0.1, max=2),  # Quick retries, capped at 2s
    'reraise': True,
}
```

### "Hitting rate limits despite retries"

Increase delays or use `max_concurrency`:

```
fromtenacityimport stop_after_attempt, wait_exponential

frompydantic_evalsimport Case, Dataset


deftask(inputs: str) -> str:
    return f'Result: {inputs}'


dataset = Dataset(cases=[Case(inputs='test')], evaluators=[])

# Longer delays
retry_config = {
    'stop': stop_after_attempt(5),
    'wait': wait_exponential(multiplier=5, min=5, max=60),  # Start at 5s, exponential up to 60s
    'reraise': True,
}

# Also reduce concurrency
report = dataset.evaluate_sync(
    task=task,
    retry_task=retry_config,
    max_concurrency=2,  # Only 2 concurrent tasks
)
```

## Next Steps

- [**Concurrency & Performance**](https://ai.pydantic.dev/evals/how-to/concurrency/) - Optimize evaluation performance
- [**Logfire Integration**](https://ai.pydantic.dev/evals/how-to/logfire-integration/) - View retries in Logfire