---
title: Azure AI | Mistral Docs
url: https://docs.mistral.ai/models/deployment/cloud-deployments/azure
source: sitemap
fetched_at: 2026-04-26T04:09:01.575547714-03:00
rendered_js: false
word_count: 198
summary: This document outlines the deployment options for Mistral AI models on Microsoft Azure AI, detailing how to set up managed or real-time endpoints and configure the environment for API access.
tags:
    - mistral-ai
    - azure-ai
    - model-deployment
    - cloud-infrastructure
    - api-integration
    - maas
category: guide
optimized: true
optimized_at: 2026-04-26T00:00:00Z
---

Mistral AI's open and commercial models can be deployed on the Microsoft Azure AI cloud platform in two ways:

- *Pay-as-you-go managed services*: Using Model-as-a-Service (MaaS) serverless API deployments billed on endpoint usage. No GPU capacity quota is required for deployment.
- *Real-time endpoints*: With quota-based billing tied to the underlying GPU infrastructure you choose to deploy.

## Available Models

- Mistral Large 3 (25.12)
- Mistral Large (24.07, 24.11)
- Mistral Medium (25.05)
- Mistral Small (25.03)
- Mistral Document AI (25.05)
- Mistral OCR (25.05)
- Ministral 3B (24.10)
- Mistral Nemo
- Codestral (25.01)

## Deployment

Follow the instructions on the [Azure documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/how-to/create-model-deployments) to create a new deployment for the model of your choice. Once deployed, take note of its corresponding URL and secret key.

Deployed endpoints expose a REST API that you can query using Mistral's SDKs, HTTPS calls, and in some cases the Microsoft Foundry SDK.

## Setup

Before running the examples below, ensure you:

- Set the following environment variables:
  - `AZUREAI_ENDPOINT`: Your endpoint URL, should be of the form `https://your-endpoint.inference.ai.azure.com/v1/chat/completions`
  - `AZUREAI_API_KEY`: Your secret key

For more details and examples, refer to the following resources: