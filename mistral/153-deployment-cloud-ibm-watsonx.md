---
title: IBM watsonx.ai | Mistral Docs
url: https://docs.mistral.ai/deployment/cloud/ibm-watsonx
source: crawler
fetched_at: 2026-01-29T07:34:25.416978354-03:00
rendered_js: false
word_count: 218
summary: This document provides instructions for accessing and querying Mistral AI's Large model on the IBM watsonx.ai platform using both SDK and HTTP methods. It covers prerequisite credentials, environment configuration, and recommended Python libraries for secure API integration.
tags:
    - ibm-watsonx
    - mistral-large
    - api-setup
    - python-sdk
    - llm-integration
    - iam-authentication
category: guide
---

Mistral AI's Large model is available on the **IBM watsonx.ai** platform as a fully managed solution, as well as an on-premise deployment.

The following sections outline the steps to query **Mistral Large** on the SaaS version of IBM watsonx.ai.

The following items are required:

- An **IBM watsonx project** (`IBM_CLOUD_PROJECT_ID`)
- A **Service ID** with an access policy enabling the use of the Watson Machine Learning service.

To enable access to the API, ensure that:

- Your Service ID has been added to the project as `EDITOR`.
- You have generated an **API key** (`IBM_CLOUD_API_KEY`) for your Service ID.

You can query Mistral Large using either IBM's SDK or plain HTTP calls.

The examples below use the `mistral-common` Python package to properly format user messages with special tokens. **Avoid passing raw strings or handling special tokens manually**, as this may result in silent tokenization errors that degrade model output quality.

You will need to run your code from a virtual environment with the following packages:

- `httpx` (tested with `0.27.2`)
- `ibm-watsonx-ai` (tested with `1.1.11`)
- `mistral-common` (tested with `1.4.4`)

In the following snippet, your API key generates an IAM token, and the model call uses this token for authentication.

For more information and examples, check:

- The [IBM watsonx.ai Python SDK documentation](https://ibm.github.io/watsonx-ai-python-sdk/index.html)
- This [IBM Developer tutorial](https://developer.ibm.com/tutorials/awb-using-mistral-ai-llms-in-watsonx-ai-flows-engine/) on using Mistral Large with IBM watsonx.ai flows engine.