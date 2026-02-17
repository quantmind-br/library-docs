---
title: Mage AI
url: https://coolify.io/docs/services/mage-ai.md
source: llms
fetched_at: 2026-02-17T14:45:38.466306-03:00
rendered_js: false
word_count: 92
summary: This document introduces Mage AI as a self-hosted data pipeline tool and provides essential setup information, including default login credentials and hardware compatibility requirements.
tags:
    - mage-ai
    - data-pipelines
    - etl
    - orchestration
    - troubleshooting
    - deployment
category: guide
---

## What is Mage AI?

Mage AI (Mage OSS) is a self-hosted development environment designed to help
teams create production-grade data pipelines with confidence.

Ideal for automating ETL tasks, architecting data flow, or orchestrating
transformations — all in a fast, notebook-style interface powered by modular
code.

## Default Credentials

On a fresh deployment, you can log in with the following details:

```
USERNAME: admin@admin.com
PASSWORD: admin
```

## Issue with Older CPUs

Mage AI requires modern CPU features to be available. On older
devices, you may see the error:

```
The following required CPU features were not detected:
  sse4.2, popcnt, avx, avx2, fma, bmi1, bmi2, lzcnt, pclmulqdq
```

For more details, refer to the [following issue](https://github.com/pola-rs/polars/issues/15404).

## Links

* [Official website](https://mage.ai/?utm_source=coolify.io)
* [GitHub](https://github.com/mage-ai/mage-ai?utm_source=coolify.io)