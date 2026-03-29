---
title: Code Quality | liteLLM
url: https://docs.litellm.ai/docs/extras/code_quality
source: sitemap
fetched_at: 2026-01-21T19:45:10.204814978-03:00
rendered_js: false
word_count: 50
summary: This document outlines the coding standards and development tools used by LiteLLM to maintain code quality, including specific linting, formatting, and typing utilities.
tags:
    - python-style-guide
    - linting
    - formatting
    - type-checking
    - ruff
    - black-formatter
    - code-quality
category: guide
---

🚅 LiteLLM follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).

We run:

- Ruff for [formatting and linting checks](https://github.com/BerriAI/litellm/blob/e19bb55e3b4c6a858b6e364302ebbf6633a51de5/.circleci/config.yml#L320)
- Mypy + Pyright for typing [1](https://github.com/BerriAI/litellm/blob/e19bb55e3b4c6a858b6e364302ebbf6633a51de5/.circleci/config.yml#L90), [2](https://github.com/BerriAI/litellm/blob/e19bb55e3b4c6a858b6e364302ebbf6633a51de5/.pre-commit-config.yaml#L4)
- Black for [formatting](https://github.com/BerriAI/litellm/blob/e19bb55e3b4c6a858b6e364302ebbf6633a51de5/.circleci/config.yml#L79)
- isort for [import sorting](https://github.com/BerriAI/litellm/blob/e19bb55e3b4c6a858b6e364302ebbf6633a51de5/.pre-commit-config.yaml#L10)

If you have suggestions on how to improve the code quality feel free to open an issue or a PR.