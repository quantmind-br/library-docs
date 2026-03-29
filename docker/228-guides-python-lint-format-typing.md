---
title: Linting and typing
url: https://docs.docker.com/guides/python/lint-format-typing/
source: llms
fetched_at: 2026-01-24T14:11:21.889718501-03:00
rendered_js: false
word_count: 248
summary: This guide explains how to set up and configure Python code quality tools, including Ruff for linting and formatting, Pyright for static type checking, and pre-commit hooks for automated checks.
tags:
    - python
    - linting
    - formatting
    - ruff
    - pyright
    - pre-commit
    - static-analysis
    - code-quality
category: guide
---

## Linting, formatting, and type checking for Python

Table of contents

* * *

## [Prerequisites](#prerequisites)

Complete [Develop your app](https://docs.docker.com/guides/python/develop/).

## [Overview](#overview)

In this section, you'll learn how to set up code quality tools for your Python application. This includes:

- Linting and formatting with Ruff
- Static type checking with Pyright
- Automating checks with pre-commit hooks

## [Linting and formatting with Ruff](#linting-and-formatting-with-ruff)

Ruff is an extremely fast Python linter and formatter written in Rust. It replaces multiple tools like flake8, isort, and black with a single unified tool.

Before using Ruff, install it in your Python environment:

If you're using a virtual environment, make sure it is activated so the `ruff` command is available when you run the commands below.

Create a `pyproject.toml` file:

```
[tool.ruff]
target-version = "py312"
[tool.ruff.lint]
select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
    "ARG001", # unused arguments in functions
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
    "W191",  # indentation contains tabs
    "B904",  # Allow raising exceptions without from e, for HTTPException
]
```

### [Using Ruff](#using-ruff)

Run these commands to check and format your code:

```
# Check for errors
ruff check .
# Automatically fix fixable errors
ruff check --fix .
# Format code
ruff format .
```

## [Type checking with Pyright](#type-checking-with-pyright)

Pyright is a fast static type checker for Python that works well with modern Python features.

Add `Pyright` configuration in `pyproject.toml`:

```
[tool.pyright]
typeCheckingMode = "strict"
pythonVersion = "3.12"
exclude = [".venv"]
```

### [Running Pyright](#running-pyright)

To check your code for type errors:

## [Setting up pre-commit hooks](#setting-up-pre-commit-hooks)

Pre-commit hooks automatically run checks before each commit. The following `.pre-commit-config.yaml` snippet sets up Ruff:

```
https:https://github.com/charliermarsh/ruff-pre-commitrev:v0.2.2hooks:- id:ruffargs:[--fix]- id:ruff-format
```

To install and use:

```
pre-commit install
git commit -m "Test commit"  # Automatically runs checks
```

## [Summary](#summary)

In this section, you learned how to:

- Configure and use Ruff for linting and formatting
- Set up Pyright for static type checking
- Automate checks with pre-commit hooks

These tools help maintain code quality and catch errors early in development.

## [Next steps](#next-steps)

- [Configure GitHub Actions](https://docs.docker.com/guides/python/configure-github-actions/) to run these checks automatically
- Customize linting rules to match your team's style preferences
- Explore advanced type checking features