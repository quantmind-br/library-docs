---
title: Azure AI | Mistral Docs
url: https://docs.mistral.ai/deployment/cloud/azure
source: crawler
fetched_at: 2026-01-29T07:34:25.45950597-03:00
rendered_js: false
word_count: 198
summary: Documentation and instructions for deploying and utilizing Mistral AI models through the Microsoft Azure AI platform.
tags:
    - Azure AI
    - Mistral
    - Machine Learning
    - Cloud
    - LLM
category: guide
---

Mistral AI's open and commercial models can be deployed on the Microsoft Azure AI cloud platform in two ways:

- *Pay-as-you-go managed services*: Using Model-as-a-Service (MaaS) serverless API deployments billed on endpoint usage. No GPU capacity quota is required for deployment.
- *Real-time endpoints*: With quota-based billing tied to the underlying GPU infrastructure you choose to deploy.

As of today, the following models are available:

- Mistral Large 3 (25.12)
- Mistral Large (24.07, 24.11)
- Mistral Medium (25.05)
- Mistral Small (25.03)
- Mistral Document AI (25.05)
- Mistral OCR (25.05)
- Ministral 3B (24.10)
- Mistral Nemo
- Codestral (25.01)

The following sections outline the steps to deploy and query a Mistral model on the Azure AI MaaS platform.

Follow the instructions on the [Azure documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/create-model-deployments) to create a new deployment for the model of your choice. Once deployed, take note of its corresponding URL and secret key.

Deployed endpoints expose a REST API that you can query using Mistral's SDKs, HTTPS calls, and in some cases the Microsoft Foundry SDK.

Before running the examples below, ensure you:

- Set the following environment variables:
  
  - `AZUREAI_ENDPOINT`: Your endpoint URL, should be of the form `https://your-endpoint.inference.ai.azure.com/v1/chat/completions`.
  - `AZUREAI_API_KEY`: Your secret key.

For more details and examples, refer to the following resources: