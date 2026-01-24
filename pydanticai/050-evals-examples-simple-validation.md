---
title: Simple Validation - Pydantic AI
url: https://ai.pydantic.dev/evals/examples/simple-validation/
source: sitemap
fetched_at: 2026-01-22T22:25:27.990828422-03:00
rendered_js: false
word_count: 135
summary: This document provides a practical example of using the pydantic-evals library to perform deterministic validation and performance benchmarking on a Python function.
tags:
    - pydantic-evals
    - validation
    - unit-testing
    - benchmarking
    - python
    - data-science
category: tutorial
---

## Example: Simple Validation

A proof of concept example of evaluating a simple text transformation function with deterministic checks.

## Scenario

We're testing a function that converts text to title case. We want to verify:

- Output is always a string
- Output matches expected format
- Function handles edge cases correctly
- Performance meets requirements

## Complete Example

```
frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport (
    Contains,
    EqualsExpected,
    IsInstance,
    MaxDuration,
)


# The function we're testing
defto_title_case(text: str) -> str:
"""Convert text to title case."""
    return text.title()


# Create evaluation dataset
dataset = Dataset(
    name='title_case_validation',
    cases=[
        # Basic functionality
        Case(
            name='basic_lowercase',
            inputs='hello world',
            expected_output='Hello World',
        ),
        Case(
            name='basic_uppercase',
            inputs='HELLO WORLD',
            expected_output='Hello World',
        ),
        Case(
            name='mixed_case',
            inputs='HeLLo WoRLd',
            expected_output='Hello World',
        ),

        # Edge cases
        Case(
            name='empty_string',
            inputs='',
            expected_output='',
        ),
        Case(
            name='single_word',
            inputs='hello',
            expected_output='Hello',
        ),
        Case(
            name='with_punctuation',
            inputs='hello, world!',
            expected_output='Hello, World!',
        ),
        Case(
            name='with_numbers',
            inputs='hello 123 world',
            expected_output='Hello 123 World',
        ),
        Case(
            name='apostrophes',
            inputs="don't stop believin'",
            expected_output="Don'T Stop Believin'",
        ),
    ],
    evaluators=[
        # Always returns a string
        IsInstance(type_name='str'),

        # Matches expected output
        EqualsExpected(),

        # Output should contain capital letters
        Contains(value='H', evaluation_name='has_capitals'),

        # Should be fast (under 1ms)
        MaxDuration(seconds=0.001),
    ],
)


# Run evaluation
if __name__ == '__main__':
    report = dataset.evaluate_sync(to_title_case)

    # Print results
    report.print(include_input=True, include_output=True)
"""
                            Evaluation Summary: to_title_case
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID          ┃ Inputs               ┃ Outputs              ┃ Assertions ┃ Duration ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
│ basic_lowercase  │ hello world          │ Hello World          │ ✔✔✔✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ basic_uppercase  │ HELLO WORLD          │ Hello World          │ ✔✔✔✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ mixed_case       │ HeLLo WoRLd          │ Hello World          │ ✔✔✔✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ empty_string     │ -                    │ -                    │ ✔✔✗✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ single_word      │ hello                │ Hello                │ ✔✔✔✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ with_punctuation │ hello, world!        │ Hello, World!        │ ✔✔✔✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ with_numbers     │ hello 123 world      │ Hello 123 World      │ ✔✔✔✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ apostrophes      │ don't stop believin' │ Don'T Stop Believin' │ ✔✔✗✗       │     10ms │
├──────────────────┼──────────────────────┼──────────────────────┼────────────┼──────────┤
│ Averages         │                      │                      │ 68.8% ✔    │     10ms │
└──────────────────┴──────────────────────┴──────────────────────┴────────────┴──────────┘
"""
# Check if all passed
avg = report.averages()
if avg and avg.assertions == 1.0:
    print('\n✅ All tests passed!')
else:
    print(f'\n❌ Some tests failed (pass rate: {avg.assertions:.1%})')
"""
    ❌ Some tests failed (pass rate: 68.8%)
    """
```

## Expected Output

```
                        Evaluation Summary: to_title_case
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Case ID           ┃ Inputs               ┃ Outputs               ┃ Assertions ┃ Duration ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━┩
│ basic_lowercase   │ hello world          │ Hello World           │ ✔✔✔✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ basic_uppercase   │ HELLO WORLD          │ Hello World           │ ✔✔✔✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ mixed_case        │ HeLLo WoRLd          │ Hello World           │ ✔✔✔✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ empty_string      │                      │                       │ ✔✔✗✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ single_word       │ hello                │ Hello                 │ ✔✔✔✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ with_punctuation  │ hello, world!        │ Hello, World!         │ ✔✔✔✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ with_numbers      │ hello 123 world      │ Hello 123 World       │ ✔✔✔✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ apostrophes       │ don't stop believin' │ Don'T Stop Believin'  │ ✔✔✔✔       │      <1ms│
├───────────────────┼──────────────────────┼───────────────────────┼────────────┼──────────┤
│ Averages          │                      │                       │ 96.9% ✔    │      <1ms│
└───────────────────┴──────────────────────┴───────────────────────┴────────────┴──────────┘

✅ All tests passed!
```

Note: The `empty_string` case has one failed assertion (`has_capitals`) because an empty string contains no capital letters.

## Saving and Loading

Save the dataset for future use:

```
fromtypingimport Any

frompydantic_evalsimport Case, Dataset
frompydantic_evals.evaluatorsimport EqualsExpected


# The function we're testing
defto_title_case(text: str) -> str:
"""Convert text to title case."""
    return text.title()


# Create dataset
dataset: Dataset[str, str, Any] = Dataset(
    cases=[Case(inputs='test', expected_output='Test')],
    evaluators=[EqualsExpected()],
)

# Save to YAML
dataset.to_file('title_case_tests.yaml')

# Load later
dataset = Dataset.from_file('title_case_tests.yaml')
report = dataset.evaluate_sync(to_title_case)
```

## Adding More Cases

As you find bugs or edge cases, add them to the dataset:

```
frompydantic_evalsimport Dataset

# Load existing dataset
dataset = Dataset.from_file('title_case_tests.yaml')

# Found a bug with unicode
dataset.add_case(
    name='unicode_chars',
    inputs='café résumé',
    expected_output='Café Résumé',
)

# Found a bug with all caps words
dataset.add_case(
    name='acronyms',
    inputs='the USA and FBI',
    expected_output='The Usa And Fbi',  # Python's title() behavior
)

# Test with very long input
dataset.add_case(
    name='long_input',
    inputs=' '.join(['word'] * 1000),
    expected_output=' '.join(['Word'] * 1000),
)

# Save updated dataset
dataset.to_file('title_case_tests.yaml')
```

## Using with pytest

Integrate with pytest for CI/CD:

```
importpytest

frompydantic_evalsimport Dataset


# The function we're testing
defto_title_case(text: str) -> str:
"""Convert text to title case."""
    return text.title()


@pytest.fixture
deftitle_case_dataset():
    return Dataset.from_file('title_case_tests.yaml')


deftest_title_case_evaluation(title_case_dataset):
"""Run evaluation tests."""
    report = title_case_dataset.evaluate_sync(to_title_case)

    # All cases should pass
    avg = report.averages()
    assert avg is not None
    assert avg.assertions == 1.0, f'Some tests failed (pass rate: {avg.assertions:.1%})'


deftest_title_case_performance(title_case_dataset):
"""Verify performance."""
    report = title_case_dataset.evaluate_sync(to_title_case)

    # All cases should complete quickly
    for case in report.cases:
        assert case.task_duration < 0.001, f'{case.name} took {case.task_duration}s'
```

## Next Steps

- [**Built-in Evaluators**](https://ai.pydantic.dev/evals/evaluators/built-in/) - Explore all available evaluators
- [**Custom Evaluators**](https://ai.pydantic.dev/evals/evaluators/custom/) - Write your own evaluation logic
- [**Dataset Management**](https://ai.pydantic.dev/evals/how-to/dataset-management/) - Save, load, and manage datasets
- [**Concurrency & Performance**](https://ai.pydantic.dev/evals/how-to/concurrency/) - Optimize evaluation performance