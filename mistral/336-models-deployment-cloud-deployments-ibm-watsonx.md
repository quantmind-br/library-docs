---
title: IBM watsonx.ai | Mistral Docs
url: https://docs.mistral.ai/models/deployment/cloud-deployments/ibm-watsonx
source: sitemap
fetched_at: 2026-04-26T04:09:03.735324609-03:00
rendered_js: false
word_count: 212
summary: This document outlines the prerequisites and setup steps required to access and query the Mistral Large model via the IBM watsonx.ai platform.
tags:
    - ibm-watsonx
    - mistral-large
    - llm-integration
    - ai-api
    - cloud-configuration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral AI's Large model is available on the **IBM watsonx.ai** platform as a fully managed solution.

## Prerequisites

The following items are required:

- An **IBM watsonx project** (`IBM_CLOUD_PROJECT_ID`)
- A **Service ID** with an access policy enabling the use of the Watson Machine Learning service.

To enable access to the API, ensure that:
- Your Service ID has been added to the project as `EDITOR`.
- You have generated an **API key** (`IBM_CLOUD_API_KEY`) for your Service ID.

## Query Methods

You can query Mistral Large using either IBM's SDK or plain HTTP calls.

The examples below use the `mistral-common` Python package to properly format user messages with special tokens. **Avoid passing raw strings or handling special tokens manually**, as this may result in silent tokenization errors that degrade model output quality.

## Setup

You will need to run your code from a virtual environment with the following packages:

- `httpx` (tested with `0.27.2`)
- `ibm-watsonx-ai` (tested with `1.1.11`)
- `mistral-common` (tested with `1.4.4`)

In the following snippet, your API key generates an IAM token, and the model call uses this token for authentication:

```python
```

## Resources

For more information and examples, check:
- The [IBM watsonx.ai Python SDK documentation](https://ibm.github.io/watsonx-ai-python-sdk/index.html)
- This [IBM Developer tutorial](https://developer.ibm.com/tutorials/awb-using-mistral-ai-llms-in-watsonx-ai-flows-engine/) on using Mistral Large with IBM watsonx.ai flows engine.