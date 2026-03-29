---
title: Quickstart | Mistral Docs
url: https://docs.mistral.ai/getting-started/quickstart
source: crawler
fetched_at: 2026-01-29T07:33:06.569399024-03:00
rendered_js: false
word_count: 317
summary: This document provides a step-by-step guide for getting started with the Mistral AI API, covering account creation, billing setup, and API key management.
tags:
    - mistral-ai
    - api-setup
    - billing-configuration
    - api-keys
    - developer-onboarding
category: guide
---

Looking for the **AI Studio** previously La Plateforme? Head to [console.mistral.ai](https://console.mistral.ai/)

## Start using Mistral AI API

To get started with Mistral AI, you need to create an account and set up your payment information; once done you can create an API key and start using our API.

- Create a Mistral account or sign in at [https://console.mistral.ai](https://console.mistral.ai).
- Then, navigate to your "Organization" settings at [https://admin.mistral.ai](https://admin.mistral.ai).
- To add your payment information and activate payments on your account, find the [billing](https://admin.mistral.ai/organization/billing) section under Administration.
  
  - You may be later prompted to select a plan; pick between Experiment (free experimental tier) and Scale (pay as you go) plans.
- You can now manage all your [Workspaces](https://admin.mistral.ai/organization/workspaces) and Organization via this page.
- Return to [https://console.mistral.ai](https://console.mistral.ai) once everything is settled.
- After that, go to the [API keys](https://console.mistral.ai/api-keys) page under your Workspace and create a new API key by clicking "Create new key". Make sure to copy the API key, save it securely, and do not share it with anyone.

[Open in Colab ↗](https://colab.research.google.com/github/mistralai/cookbook/blob/main/quickstart.ipynb)

Mistral AI API provides a seamless way for developers to integrate Mistral's state-of-the-art models into their applications and production workflows with just a few lines of code. Our API is currently available through [La Plateforme](https://console.mistral.ai/). You need to activate payments on your account to enable your API keys. After a few moments, you will be able to use our endpoints.

Below, you can see some quickstart code snippets and examples of a few of our endpoints you can visit!

Our Chat Completion endpoint allows you to interact with Mistral AI's models in a **conversational manner**, pretty much how you would interact with a chatbot.

To learn more about the Chat Completion endpoint, check out our [Chat Completions Docs](https://docs.mistral.ai/capabilities/completion).

We offer multiple services and models, from transcription to reasoning and sota document AI and OCR systems; For a full description of the models offered on the API, head on to the [**models page**](https://docs.mistral.ai/models).