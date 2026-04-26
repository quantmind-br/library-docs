---
title: Vertex AI | Mistral Docs
url: https://docs.mistral.ai/models/deployment/cloud-deployments/vertex
source: sitemap
fetched_at: 2026-04-26T04:09:08.465255078-03:00
rendered_js: false
word_count: 267
summary: This document provides instructions for deploying and querying Mistral AI models on the Google Cloud Vertex AI platform, including setup requirements and authentication steps.
tags:
    - vertex-ai
    - google-cloud
    - mistral-ai
    - model-deployment
    - cloud-infrastructure
    - api-integration
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral AI's open and commercial models can be deployed on the Google Cloud Vertex AI platform as fully managed endpoints. Mistral models on Vertex AI are serverless services, so you don't have to manage any infrastructure.

## Available Models

- Mistral Medium 3 (25.05)
- Codestral 2 (25.08)
- Mistral OCR (25.05)
- Mistral Small (25.03)

## Prerequisites

The following items are required:

- Access to a **Google Cloud Project** with the Vertex AI API enabled.
- Relevant IAM permissions to enable the model and query endpoints through the following roles:
  - [Vertex AI User IAM role](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user)
  - Consumer Procurement Entitlement Manager role.

To enable the model of your choice, navigate to its card in the [Vertex Model Garden catalog](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models), then click on **"Enable"**.

## Querying

Available models expose a REST API that you can query using Mistral's SDKs or plain HTTP calls.

To run the examples below:

- Install the `gcloud` CLI to authenticate against the Google Cloud APIs. Refer to [this page](https://cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) for more details.
- Set the following environment variables:
  - `VERTEX_MODEL_NAME`: The name of the model to query (e.g., `mistral-large`)
  - `VERTEX_MODEL_VERSION`: The version of the model to query (e.g., `2407`)
  - *(V1 only)* `GOOGLE_CLOUD_REGION`: The target cloud region
  - *(V1 only)* `GOOGLE_CLOUD_PROJECT_ID`: The name of your project

## FIM Support

Codestral can be queried using an additional completion mode called **fill-in-the-middle (FIM)**.

For more information, see the [code generation section](https://docs.mistral.ai/mistral-vibe/using-fim-api).

## Resources

For more information and examples, check:
- The Google Cloud [Partner Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/mistral) documentation page
- The [Getting Started Colab Notebook](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/generative_ai/mistralai_intro.ipynb) for Mistral models on Vertex, along with the [source file on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/official/generative_ai/mistralai_intro.ipynb)