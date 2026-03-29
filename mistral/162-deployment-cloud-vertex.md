---
title: Vertex AI | Mistral Docs
url: https://docs.mistral.ai/deployment/cloud/vertex
source: crawler
fetched_at: 2026-01-29T07:34:24.780723675-03:00
rendered_js: false
word_count: 263
summary: A guide on how to access, deploy, and utilize Mistral AI models within the Google Cloud Vertex AI ecosystem.
tags:
    - Mistral AI
    - Vertex AI
    - Google Cloud
    - Machine Learning
    - LLM
category: guide
---

Mistral AI's open and commercial models can be deployed on the Google Cloud Vertex AI platform as fully managed endpoints. Mistral models on Vertex AI are serverless services, so you don't have to manage any infrastructure.

As of today, the following models are available:

- Mistral Medium 3 (25.05)
- Codestral 2 (25.08)
- Mistral OCR (25.05)
- Mistral Small (25.03)

The following sections outline the steps to deploy and query a Mistral model on the Vertex AI platform.

The following items are required:

- Access to a **Google Cloud Project** with the Vertex AI API enabled.
- Relevant IAM permissions to enable the model and query endpoints through the following roles:
  
  - [Vertex AI User IAM role](https://cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.user).
  - Consumer Procurement Entitlement Manager role.

To enable the model of your choice, navigate to its card in the [Vertex Model Garden catalog](https://cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models), then click on **"Enable"**.

Available models expose a REST API that you can query using Mistral's SDKs or plain HTTP calls.

To run the examples below:

- Install the `gcloud` CLI to authenticate against the Google Cloud APIs. Refer to [this page](https://cloud.google.com/docs/authentication/provide-credentials-adc#google-idp) for more details.
- Set the following environment variables:
  
  - `GOOGLE_CLOUD_REGION`: The target cloud region.
  - `GOOGLE_CLOUD_PROJECT_ID`: The name of your project.
  - `VERTEX_MODEL_NAME`: The name of the model to query (e.g., `mistral-large`).
  - `VERTEX_MODEL_VERSION`: The version of the model to query (e.g., `2407`).

Codestral can be queried using an additional completion mode called **fill-in-the-middle (FIM)**.

For more information, see the [code generation section](https://docs.mistral.ai/capabilities/code_generation).

For more information and examples, check:

- The Google Cloud [Partner Models](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/mistral) documentation page.
- The [Getting Started Colab Notebook](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/generative_ai/mistralai_intro.ipynb) for Mistral models on Vertex, along with the [source file on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/official/generative_ai/mistralai_intro.ipynb).