---
title: Custom Evaluators - Pydantic AI
url: https://ai.pydantic.dev/evals/evaluators/custom/
source: sitemap
fetched_at: 2026-01-22T22:25:21.011195571-03:00
rendered_js: false
word_count: 476
summary: This guide explains how to implement custom evaluators in the pydantic-evals framework by subclassing the base Evaluator class and utilizing the execution context. It covers defining parameters, handling various return types like boolean flags and numeric scores, and implementing complex evaluation logic.
tags:
    - pydantic-evals
    - custom-evaluators
    - llm-evaluation
    - python-testing
    - evaluation-metrics
    - dataclasses
category: guide
---

Write custom evaluators for domain-specific logic, external integrations, or specialized metrics.

## Basic Custom Evaluator

All evaluators inherit from [`Evaluator`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.Evaluator "Evaluator            dataclass   ") and must implement `evaluate`:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classExactMatch(Evaluator):
"""Check if output exactly matches expected output."""

    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return ctx.output == ctx.expected_output
```

**Key Points:**

- Use `@dataclass` decorator (required)
- Inherit from `Evaluator`
- Implement `evaluate(self, ctx: EvaluatorContext) -> EvaluatorOutput`
- Return `bool`, `int`, `float`, `str`, [`EvaluationReason`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationReason "EvaluationReason            dataclass   "), or `dict` of these

## EvaluatorContext

The context provides all information about the case execution:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classMyEvaluator(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> bool:
        # Access case data
        ctx.name              # Case name
        ctx.inputs            # Task inputs
        ctx.metadata          # Case metadata
        ctx.expected_output   # Expected output (may be None)
        ctx.output            # Actual output

        # Performance data
        ctx.duration          # Task execution time (seconds)

        # Custom metrics/attributes (see metrics guide)
        ctx.metrics           # dict[str, int | float]
        ctx.attributes        # dict[str, Any]

        # OpenTelemetry spans (if logfire configured)
        ctx.span_tree         # SpanTree for behavioral checks

        return True
```

## Evaluator Parameters

Add configurable parameters as dataclass fields:

```
fromdataclassesimport dataclass

frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classContainsKeyword(Evaluator):
    keyword: str
    case_sensitive: bool = True

    defevaluate(self, ctx: EvaluatorContext) -> bool:
        output = ctx.output
        keyword = self.keyword

        if not self.case_sensitive:
            output = output.lower()
            keyword = keyword.lower()

        return keyword in output


# Usage
dataset = Dataset(
    cases=[Case(name='test', inputs='This is important')],
    evaluators=[
        ContainsKeyword(keyword='important', case_sensitive=False),
    ],
)
```

## Return Types

### Boolean Assertions

Simple pass/fail checks:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classIsValidJSON(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> bool:
        try:
            importjson
            json.loads(ctx.output)
            return True
        except Exception:
            return False
```

### Numeric Scores

Quality metrics:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classLengthScore(Evaluator):
"""Score based on output length (0.0 = too short, 1.0 = ideal)."""

    ideal_length: int = 100
    tolerance: int = 20

    defevaluate(self, ctx: EvaluatorContext) -> float:
        length = len(ctx.output)
        diff = abs(length - self.ideal_length)

        if diff <= self.tolerance:
            return 1.0
        else:
            # Decay score as we move away from ideal
            score = max(0.0, 1.0 - (diff - self.tolerance) / self.ideal_length)
            return score
```

### String Labels

Categorical classifications:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classSentimentClassifier(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> str:
        output_lower = ctx.output.lower()

        if any(word in output_lower for word in ['error', 'failed', 'wrong']):
            return 'negative'
        elif any(word in output_lower for word in ['success', 'correct', 'great']):
            return 'positive'
        else:
            return 'neutral'
```

### With Reasons

Add explanations to any result:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport EvaluationReason, Evaluator, EvaluatorContext


@dataclass
classSmartCheck(Evaluator):
    threshold: float = 0.8

    defevaluate(self, ctx: EvaluatorContext) -> EvaluationReason:
        score = self._calculate_score(ctx.output)

        if score >= self.threshold:
            return EvaluationReason(
                value=True,
                reason=f'Score {score:.2f} exceeds threshold {self.threshold}',
            )
        else:
            return EvaluationReason(
                value=False,
                reason=f'Score {score:.2f} below threshold {self.threshold}',
            )

    def_calculate_score(self, output: str) -> float:
        # Your scoring logic
        return 0.75
```

### Multiple Results

You can return multiple evaluations from one evaluator by returning a dictionary of key-value pairs.

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport (
    EvaluationReason,
    Evaluator,
    EvaluatorContext,
    EvaluatorOutput,
)


@dataclass
classComprehensiveCheck(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> EvaluatorOutput:
        format_valid = self._check_format(ctx.output)

        return {
            'valid_format': EvaluationReason(
                value=format_valid,
                reason='Valid JSON format' if format_valid else 'Invalid JSON format',
            ),
            'quality_score': self._score_quality(ctx.output),  # float
            'category': self._classify(ctx.output),  # str
        }

    def_check_format(self, output: str) -> bool:
        return output.startswith('{') and output.endswith('}')

    def_score_quality(self, output: str) -> float:
        return len(output) / 100.0

    def_classify(self, output: str) -> str:
        return 'short' if len(output) < 50 else 'long'
```

Each key in the returned dictionary becomes a separate result in the report. Values can be:

- Primitives (`bool`, `int`, `float`, `str`)
- [`EvaluationReason`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluationReason "EvaluationReason            dataclass   ") (value with explanation)
- Nested dicts of these types

The [`EvaluatorOutput`](https://ai.pydantic.dev/api/pydantic_evals/evaluators/#pydantic_evals.evaluators.EvaluatorOutput "EvaluatorOutput            module-attribute   ") type represents all legal values that can be returned by an evaluator, and can be used as the return type annotation for your custom `evaluate` method.

### Conditional Results

Evaluators can dynamically choose whether to produce results for a given case by returning an empty dict when not applicable:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport (
    EvaluationReason,
    Evaluator,
    EvaluatorContext,
    EvaluatorOutput,
)


@dataclass
classSQLValidator(Evaluator):
"""Only evaluates SQL queries, skips other outputs."""

    defevaluate(self, ctx: EvaluatorContext) -> EvaluatorOutput:
        # Check if this case is relevant for SQL validation
        if not isinstance(ctx.output, str) or not ctx.output.strip().upper().startswith(
            ('SELECT', 'INSERT', 'UPDATE', 'DELETE')
        ):
            # Return empty dict - this evaluator doesn't apply to this case
            return {}

        # This is a SQL query, perform validation
        try:
            # In real implementation, use sqlparse or similar
            is_valid = self._validate_sql(ctx.output)
            return {
                'sql_valid': is_valid,
                'sql_complexity': self._measure_complexity(ctx.output),
            }
        except Exception as e:
            return {'sql_valid': EvaluationReason(False, reason=f'Exception: {e}')}

    def_validate_sql(self, query: str) -> bool:
        # Simplified validation
        return 'FROM' in query.upper() or 'INTO' in query.upper()

    def_measure_complexity(self, query: str) -> str:
        joins = query.upper().count('JOIN')
        if joins == 0:
            return 'simple'
        elif joins <= 2:
            return 'moderate'
        else:
            return 'complex'
```

This pattern is useful when:

- An evaluator only applies to certain types of outputs (e.g., code validation only for code outputs)
- Validation depends on metadata tags (e.g., only evaluate cases marked with `language='python'`)
- You want to run expensive checks conditionally based on other evaluator results

**Key Points:**

- Returning `{}` means "this evaluator doesn't apply here" - the case won't show results from this evaluator
- Returning `{'key': value}` means "this evaluator applies and here are the results"
- This is more practical than using case-level evaluators when it applies to a large fraction of cases, or when the condition is based on the output itself
- The evaluator still runs for every case, but can short-circuit when not relevant

## Async Evaluators

Use `async def` for I/O-bound operations:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classAPIValidator(Evaluator):
    api_url: str

    async defevaluate(self, ctx: EvaluatorContext) -> bool:
        importhttpx

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url,
                json={'output': ctx.output},
            )
            return response.json()['valid']
```

Pydantic Evals handles both sync and async evaluators automatically.

Access case metadata for context-aware evaluation:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classDifficultyAwareScore(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> float:
        # Base score
        base_score = self._score_output(ctx.output)

        # Adjust based on difficulty from metadata
        if ctx.metadata and 'difficulty' in ctx.metadata:
            difficulty = ctx.metadata['difficulty']

            if difficulty == 'easy':
                # Penalize mistakes more on easy questions
                return base_score
            elif difficulty == 'hard':
                # Be more lenient on hard questions
                return min(1.0, base_score * 1.2)

        return base_score

    def_score_output(self, output: str) -> float:
        # Your scoring logic
        return 0.8
```

## Using Metrics

Access custom metrics set during task execution:

```
fromdataclassesimport dataclass

frompydantic_evalsimport increment_eval_metric, set_eval_attribute
frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


# In your task
defmy_task(inputs: str) -> str:
    result = f'processed: {inputs}'

    # Record metrics
    increment_eval_metric('api_calls', 3)
    set_eval_attribute('used_cache', True)

    return result


# In your evaluator
@dataclass
classEfficiencyCheck(Evaluator):
    max_api_calls: int = 5

    defevaluate(self, ctx: EvaluatorContext) -> bool:
        api_calls = ctx.metrics.get('api_calls', 0)
        return api_calls <= self.max_api_calls
```

See [Metrics & Attributes Guide](https://ai.pydantic.dev/evals/how-to/metrics-attributes/) for more.

## Generic Type Parameters

Make evaluators type-safe with generics:

```
fromdataclassesimport dataclass
fromtypingimport TypeVar

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext

InputsT = TypeVar('InputsT')
OutputT = TypeVar('OutputT')


@dataclass
classTypedEvaluator(Evaluator[InputsT, OutputT, dict]):
    defevaluate(self, ctx: EvaluatorContext[InputsT, OutputT, dict]) -> bool:
        # ctx.inputs and ctx.output are now properly typed
        return True
```

## Custom Evaluation Names

Control how evaluations appear in reports:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classCustomNameEvaluator(Evaluator):
    check_type: str

    defget_default_evaluation_name(self) -> str:
        # Use check_type as the name instead of class name
        return f'{self.check_type}_check'

    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return True


# In reports, appears as "format_check" instead of "CustomNameEvaluator"
evaluator = CustomNameEvaluator(check_type='format')
```

Or use the `evaluation_name` field (if using the built-in pattern):

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classMyEvaluator(Evaluator):
    evaluation_name: str | None = None

    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return True


# Usage
MyEvaluator(evaluation_name='my_custom_name')
```

## Real-World Examples

### SQL Validation

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport EvaluationReason, Evaluator, EvaluatorContext


@dataclass
classValidSQL(Evaluator):
    dialect: str = 'postgresql'

    defevaluate(self, ctx: EvaluatorContext) -> EvaluationReason:
        try:
            importsqlparse
            parsed = sqlparse.parse(ctx.output)

            if not parsed:
                return EvaluationReason(
                    value=False,
                    reason='Could not parse SQL',
                )

            # Check for dangerous operations
            sql_upper = ctx.output.upper()
            if 'DROP' in sql_upper or 'DELETE' in sql_upper:
                return EvaluationReason(
                    value=False,
                    reason='Contains dangerous operations (DROP/DELETE)',
                )

            return EvaluationReason(
                value=True,
                reason='Valid SQL syntax',
            )
        except Exception as e:
            return EvaluationReason(
                value=False,
                reason=f'SQL parsing error: {e}',
            )
```

### Code Execution

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport EvaluationReason, Evaluator, EvaluatorContext


@dataclass
classExecutablePython(Evaluator):
    timeout_seconds: float = 5.0

    async defevaluate(self, ctx: EvaluatorContext) -> EvaluationReason:
        importasyncio
        importos
        importtempfile

        # Write code to temp file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(ctx.output)
            temp_path = f.name

        try:
            # Execute with timeout
            process = await asyncio.create_subprocess_exec(
                'python', temp_path,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            try:
                stdout, stderr = await asyncio.wait_for(
                    process.communicate(),
                    timeout=self.timeout_seconds,
                )
            except asyncio.TimeoutError:
                process.kill()
                return EvaluationReason(
                    value=False,
                    reason=f'Execution timeout after {self.timeout_seconds}s',
                )

            if process.returncode == 0:
                return EvaluationReason(
                    value=True,
                    reason='Code executed successfully',
                )
            else:
                return EvaluationReason(
                    value=False,
                    reason=f'Execution failed: {stderr.decode()}',
                )
        finally:
            os.unlink(temp_path)
```

### External API Validation

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classAPIResponseValid(Evaluator):
    api_endpoint: str
    api_key: str

    async defevaluate(self, ctx: EvaluatorContext) -> dict[str, bool | float]:
        importhttpx

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.api_endpoint,
                    headers={'Authorization': f'Bearer {self.api_key}'},
                    json={'data': ctx.output},
                    timeout=10.0,
                )

                result = response.json()

                return {
                    'api_reachable': True,
                    'validation_passed': result.get('valid', False),
                    'confidence_score': result.get('confidence', 0.0),
                }
        except Exception:
            return {
                'api_reachable': False,
                'validation_passed': False,
                'confidence_score': 0.0,
            }
```

## Testing Evaluators

Test evaluators like any other Python code:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classExactMatch(Evaluator):
"""Check if output exactly matches expected output."""

    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return ctx.output == ctx.expected_output


deftest_exact_match():
    evaluator = ExactMatch()

    # Test match
    ctx = EvaluatorContext(
        name='test',
        inputs='input',
        metadata=None,
        expected_output='expected',
        output='expected',
        duration=0.1,
        _span_tree=None,
        attributes={},
        metrics={},
    )
    assert evaluator.evaluate(ctx) is True

    # Test mismatch
    ctx.output = 'different'
    assert evaluator.evaluate(ctx) is False
```

## Best Practices

### 1. Keep Evaluators Focused

Each evaluator should check one thing:

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


defcheck_format(output: str) -> bool:
    return output.startswith('{')


defcheck_content(output: str) -> bool:
    return len(output) > 10


defcheck_length(output: str) -> bool:
    return len(output) < 1000


defcheck_spelling(output: str) -> bool:
    return True  # Placeholder


# Bad: Doing too much
@dataclass
classEverythingChecker(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> dict:
        return {
            'format_valid': check_format(ctx.output),
            'content_good': check_content(ctx.output),
            'length_ok': check_length(ctx.output),
            'spelling_correct': check_spelling(ctx.output),
        }


# Good: Separate evaluators
@dataclass
classFormatValidator(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return check_format(ctx.output)


@dataclass
classContentChecker(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return check_content(ctx.output)


@dataclass
classLengthChecker(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return check_length(ctx.output)


@dataclass
classSpellingChecker(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> bool:
        return check_spelling(ctx.output)
```

Some exceptions to this:

- When there is a significant amount of shared computation or network request latency, it may be better to have a single evaluator calculate all dependent outputs together.
- If multiple checks are tightly coupled or very closely related to each other, it may make sense to include all their logic in one evaluator.

### 2. Handle Missing Data Gracefully

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport EvaluationReason, Evaluator, EvaluatorContext


@dataclass
classSafeEvaluator(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> EvaluationReason:
        if ctx.expected_output is None:
            return EvaluationReason(
                value=True,
                reason='Skipped: no expected output provided',
            )

        # Your evaluation logic
        ...
```

### 3. Provide Helpful Reasons

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport EvaluationReason, Evaluator, EvaluatorContext


@dataclass
classHelpfulEvaluator(Evaluator):
    defevaluate(self, ctx: EvaluatorContext) -> EvaluationReason:
        # Bad
        return EvaluationReason(value=False, reason='Failed')

        # Good
        return EvaluationReason(
            value=False,
            reason=f'Expected {ctx.expected_output!r}, got {ctx.output!r}',
        )
```

### 4. Use Timeouts for External Calls

```
fromdataclassesimport dataclass

frompydantic_evals.evaluatorsimport Evaluator, EvaluatorContext


@dataclass
classAPIEvaluator(Evaluator):
    timeout: float = 10.0

    async def_call_api(self, output: str) -> bool:
        # Placeholder for API call
        return True

    async defevaluate(self, ctx: EvaluatorContext) -> bool:
        importasyncio

        try:
            return await asyncio.wait_for(
                self._call_api(ctx.output),
                timeout=self.timeout,
            )
        except asyncio.TimeoutError:
            return False
```

## Next Steps

- [**Span-Based Evaluation**](https://ai.pydantic.dev/evals/evaluators/span-based/) - Using OpenTelemetry spans
- [**Examples**](https://ai.pydantic.dev/evals/examples/simple-validation/) - Practical examples