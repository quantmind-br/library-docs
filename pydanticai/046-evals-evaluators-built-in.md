---
title: Built-in Evaluators - Pydantic AI
url: https://ai.pydantic.dev/evals/evaluators/built-in/
source: sitemap
fetched_at: 2026-01-22T22:25:18.828351648-03:00
rendered_js: false
word_count: 698
summary: This document details the built-in evaluators provided by Pydantic Evals for verifying model outputs through comparisons, type checks, performance metrics, and LLM-based judgments.
tags:
    - pydantic-evals
    - evaluators
    - llm-judge
    - model-evaluation
    - performance-testing
    - type-validation
category: reference
---

Pydantic Evals provides several built-in evaluators for common evaluation tasks.

## Comparison Evaluators

### EqualsExpected

Check if the output exactly equals the expected output from the case.

```
frompydantic_evals.evaluatorsimport EqualsExpected

EqualsExpected()
```

**Parameters:** None

**Returns:** `bool` - `True` if `ctx.output == ctx.expected_output`

**Example:**

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport EqualsExpected

dataset = Dataset(
    cases=[
        Case(
            name='addition',
            inputs='2 + 2',
            expected_output='4',
        ),
    ],
    evaluators=[EqualsExpected()],
)
```

**Notes:**

- Skips evaluation if `expected_output` is `None` (returns empty dict `{}`)
- Uses Python's `==` operator, so works with any comparable types
- For structured data, considers nested equality

* * *

### Equals

Check if the output equals a specific value.

```
frompydantic_evals.evaluatorsimport Equals

Equals(value='expected_result')
```

**Parameters:**

- `value` (Any): The value to compare against
- `evaluation_name` (str | None): Custom name for this evaluation in reports

**Returns:** `bool` - `True` if `ctx.output == value`

**Example:**

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport Equals

# Check output is always "success"
dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        Equals(value='success', evaluation_name='is_success'),
    ],
)
```

**Use Cases:**

- Checking for sentinel values
- Validating consistent outputs
- Testing classification into specific categories

* * *

### Contains

Check if the output contains a specific value or substring.

```
frompydantic_evals.evaluatorsimport Contains

Contains(
    value='substring',
    case_sensitive=True,
    as_strings=False,
)
```

**Parameters:**

- `value` (Any): The value to search for
- `case_sensitive` (bool): Case-sensitive comparison for strings (default: `True`)
- `as_strings` (bool): Convert both values to strings before checking (default: `False`)
- `evaluation_name` (str | None): Custom name for this evaluation in reports

**Returns:** [`EvaluationReason`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationReason "EvaluationReason            dataclass   ") - Pass/fail with explanation

**Behavior:**

For **strings**: checks substring containment

- `Contains(value='hello', case_sensitive=False)`
- Matches: "Hello World", "say hello", "HELLO"
- Doesn't match: "hi there"

For **lists/tuples**: checks membership

- `Contains(value='apple')`
- Matches: `['apple', 'banana']`, `('apple',)`
- Doesn't match: `['apples', 'orange']`

For **dicts**: checks key-value pairs

- `Contains(value={'name': 'Alice'})`
- Matches: `{'name': 'Alice', 'age': 30}`
- Doesn't match: `{'name': 'Bob'}`

**Example:**

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport Contains

dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # Check for required keywords
        Contains(value='terms and conditions', case_sensitive=False),
        # Check for PII (fail if found)
        # Note: Use a custom evaluator that returns False when PII found
    ],
)
```

**Use Cases:**

- Required content verification
- Keyword detection
- PII/sensitive data detection
- Multi-value validation

* * *

## Type Validation

### IsInstance

Check if the output is an instance of a type with the given name.

```
frompydantic_evals.evaluatorsimport IsInstance

IsInstance(type_name='str')
```

**Parameters:**

- `type_name` (str): The type name to check (uses `__name__` or `__qualname__`)
- `evaluation_name` (str | None): Custom name for this evaluation in reports

**Returns:** [`EvaluationReason`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationReason "EvaluationReason            dataclass   ") - Pass/fail with type information

**Example:**

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport IsInstance

dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # Check output is always a string
        IsInstance(type_name='str'),
        # Check for Pydantic model
        IsInstance(type_name='MyModel'),
        # Check for dict
        IsInstance(type_name='dict'),
    ],
)
```

**Notes:**

- Matches against both `__name__` and `__qualname__` of the type
- Works with built-in types (`str`, `int`, `dict`, `list`, etc.)
- Works with custom classes and Pydantic models
- Checks the entire MRO (Method Resolution Order) for inheritance

**Use Cases:**

- Format validation
- Structured output verification
- Type consistency checks

* * *

## Performance Evaluation

### MaxDuration

Check if task execution time is under a maximum threshold.

```
fromdatetimeimport timedelta

frompydantic_evals.evaluatorsimport MaxDuration

MaxDuration(seconds=2.0)
# or
MaxDuration(seconds=timedelta(seconds=2))
```

**Parameters:**

- `seconds` (float | timedelta): Maximum allowed duration

**Returns:** `bool` - `True` if `ctx.duration <= seconds`

**Example:**

```
fromdatetimeimport timedelta

frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport MaxDuration

dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # SLA: must respond in under 2 seconds
        MaxDuration(seconds=2.0),
        # Or using timedelta
        MaxDuration(seconds=timedelta(milliseconds=500)),
    ],
)
```

**Use Cases:**

- SLA compliance
- Performance regression testing
- Latency requirements
- Timeout validation

**See Also:** [Concurrency & Performance](https://ai.pydantic.dev/evals/how-to/concurrency/)

* * *

## LLM-as-a-Judge

### LLMJudge

Use an LLM to evaluate subjective qualities based on a rubric.

```
frompydantic_evals.evaluatorsimport LLMJudge

LLMJudge(
    rubric='Response is accurate and helpful',
    model='openai:gpt-5',
    include_input=False,
    include_expected_output=False,
    model_settings=None,
    score=False,
    assertion={'include_reason': True},
)
```

**Parameters:**

- `rubric` (str): The evaluation criteria (required)
- `model` (Model | KnownModelName | None): Model to use (default: `'openai:gpt-4o'`)
- `include_input` (bool): Include task inputs in the prompt (default: `False`)
- `include_expected_output` (bool): Include expected output in the prompt (default: `False`)
- `model_settings` (ModelSettings | None): Custom model settings
- `score` (OutputConfig | False): Configure score output (default: `False`)
- `assertion` (OutputConfig | False): Configure assertion output (default: includes reason)

**Returns:** Depends on `score` and `assertion` parameters (see below)

**Output Modes:**

By default, returns a **boolean assertion** with reason:

- `LLMJudge(rubric='Response is polite')`
- Returns: `{'LLMJudge_pass': EvaluationReason(value=True, reason='...')}`

Return a **score** (0.0 to 1.0) instead:

- `LLMJudge(rubric='Response quality', score={'include_reason': True}, assertion=False)`
- Returns: `{'LLMJudge_score': EvaluationReason(value=0.85, reason='...')}`

Return **both** score and assertion:

- `LLMJudge(rubric='Response quality', score={'include_reason': True}, assertion={'include_reason': True})`
- Returns: `{'LLMJudge_score': EvaluationReason(value=0.85, reason='...'), 'LLMJudge_pass': EvaluationReason(value=True, reason='...')}`

**Customize evaluation names:**

- `LLMJudge(rubric='Response is factually accurate', assertion={'evaluation_name': 'accuracy', 'include_reason': True})`
- Returns: `{'accuracy': EvaluationReason(value=True, reason='...')}`

**Example:**

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport LLMJudge

dataset = Dataset(
    cases=[Case(inputs='test', expected_output='result')],
    evaluators=[
        # Basic accuracy check
        LLMJudge(
            rubric='Response is factually accurate',
            include_input=True,
        ),
        # Quality score with different model
        LLMJudge(
            rubric='Overall response quality',
            model='anthropic:claude-sonnet-4-5',
            score={'evaluation_name': 'quality', 'include_reason': False},
            assertion=False,
        ),
        # Check against expected output
        LLMJudge(
            rubric='Response matches the expected answer semantically',
            include_input=True,
            include_expected_output=True,
        ),
    ],
)
```

**See Also:** [LLM Judge Deep Dive](https://ai.pydantic.dev/evals/evaluators/llm-judge/)

* * *

## Span-Based Evaluation

### HasMatchingSpan

Check if OpenTelemetry spans match a query (requires Logfire configuration).

```
frompydantic_evals.evaluatorsimport HasMatchingSpan

HasMatchingSpan(
    query={'name_contains': 'tool_call'},
    evaluation_name='called_tool',
)
```

**Parameters:**

- `query` ([`SpanQuery`](https://ai.pydantic.dev/api/pydantic_evals/otel/#pydantic_evals.otel.SpanQuery "SpanQuery")): Query to match against spans
- `evaluation_name` (str | None): Custom name for this evaluation in reports

**Returns:** `bool` - `True` if any span matches the query

**Example:**

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport HasMatchingSpan

dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # Check that a specific tool was called
        HasMatchingSpan(
            query={'name_contains': 'search_database'},
            evaluation_name='used_database',
        ),
        # Check for errors
        HasMatchingSpan(
            query={'has_attributes': {'error': True}},
            evaluation_name='had_errors',
        ),
        # Check duration constraints
        HasMatchingSpan(
            query={
                'name_equals': 'llm_call',
                'max_duration': 2.0,  # seconds
            },
            evaluation_name='llm_fast_enough',
        ),
    ],
)
```

**See Also:** [Span-Based Evaluation](https://ai.pydantic.dev/evals/evaluators/span-based/)

* * *

## Quick Reference Table

Evaluator Purpose Return Type Cost Speed [`EqualsExpected`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EqualsExpected "EqualsExpected            dataclass   ") Exact match with expected `bool` Free Instant [`Equals`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Equals "Equals            dataclass   ") Equals specific value `bool` Free Instant [`Contains`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Contains "Contains            dataclass   ") Contains value/substring `bool` + reason Free Instant [`IsInstance`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.IsInstance "IsInstance            dataclass   ") Type validation `bool` + reason Free Instant [`MaxDuration`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.MaxDuration "MaxDuration            dataclass   ") Performance threshold `bool` Free Instant [`LLMJudge`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.LLMJudge "LLMJudge            dataclass   ") Subjective quality `bool` and/or `float` $$ Slow [`HasMatchingSpan`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.HasMatchingSpan "HasMatchingSpan            dataclass   ") Behavioral check `bool` Free Fast

## Combining Evaluators

Best practice is to combine fast deterministic checks with slower LLM evaluations:

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport (
    Contains,
    IsInstance,
    LLMJudge,
    MaxDuration,
)

dataset = Dataset(
    cases=[Case(inputs='test')],
    evaluators=[
        # Fast checks first (fail fast)
        IsInstance(type_name='str'),
        Contains(value='required_field'),
        MaxDuration(seconds=2.0),
        # Expensive LLM checks last
        LLMJudge(rubric='Response is helpful and accurate'),
    ],
)
```

This approach:

1. Catches format/structure issues immediately
2. Validates required content quickly
3. Only runs expensive LLM evaluation if basic checks pass
4. Provides comprehensive quality assessment

## Next Steps

- [**LLM Judge**](https://ai.pydantic.dev/evals/evaluators/llm-judge/) - Deep dive on LLM-as-a-Judge evaluation
- [**Custom Evaluators**](https://ai.pydantic.dev/evals/evaluators/custom/) - Write your own evaluation logic
- [**Span-Based Evaluation**](https://ai.pydantic.dev/evals/evaluators/span-based/) - Using OpenTelemetry spans for behavioral checks