---
title: Snowflake Cortex | Mistral Docs
url: https://docs.mistral.ai/models/deployment/cloud-deployments/sfcortex
source: sitemap
fetched_at: 2026-04-26T04:09:07.232878233-03:00
rendered_js: false
word_count: 216
summary: This document provides instructions for accessing and utilizing Mistral AI models within the Snowflake Cortex platform using SQL or Python.
tags:
    - snowflake-cortex
    - mistral-ai
    - llm-integration
    - cloud-computing
    - snowpark-ml
    - serverless-ai
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral AI's open and commercial models can be leveraged from the Snowflake Cortex platform as fully managed endpoints. Mistral models on Snowflake Cortex are serverless services, so you don't have to manage any infrastructure.

## Available Models

- Mistral Large
- Mistral 7B

For more details, visit the [models](https://docs.mistral.ai/models/overview) page.

## Prerequisites

The following items are required:

- The associated Snowflake account must be in a compatible region (see the [region list](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions#availability) in the Snowflake documentation).
- The principal calling the model must have the `CORTEX_USER` database role.

## Calling the Model

The model can be called either directly in SQL or in Python using Snowpark ML. It is exposed via the [`COMPLETE` *LLM function*](https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex).

## SQL Execution

Execute this code either from a hosted Snowflake notebook or from your local machine:

```sql
```

## Python Execution

For local execution, you need to:

- Create a virtual environment with the following package:
  - `snowflake-ml-python` (tested with version `1.6.1`)
- Ensure that you have a [configuration file](https://docs.snowflake.com/en/user-guide/snowsql-config) with the proper credentials on your system. The example below assumes that you have a named connection called `mistral` that is configured appropriately.

```python
```

## Resources

For more information and examples, you can check the Snowflake documentation for:

- [LLM functions](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions)
- The API of the `COMPLETE` function in [SQL](https://docs.snowflake.com/en/sql-reference/functions/complete-snowflake-cortex) and [Python](https://docs.snowflake.com/en/developer-guide/snowpark-ml/reference/latest/api/model/snowflake.cortex.Complete).