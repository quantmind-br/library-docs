---
title: Moderation & Guardrailing | Mistral Docs
url: https://docs.mistral.ai/capabilities/guardrailing
source: crawler
fetched_at: 2026-01-29T07:33:11.926468988-03:00
rendered_js: false
word_count: 579
summary: This document explains how to implement safety guardrails in Mistral AI applications using the Moderation API, system prompt configurations, and self-reflection techniques.
tags:
    - mistral-ai
    - content-moderation
    - guardrails
    - api-safety
    - system-prompts
    - llm-security
category: guide
---

When deploying LLMs in production, different verticals may require different levels of guardrailing. For example, in a chatbot application, it may be crucial to ensure that the generated content is safe and respectful.  
In other applications, it may be required to detect and filter out harmful or PII (Personally Identifiable Information) content.

For this reason, we provide two different ways to guardrail your applications:

- **Moderation API**: A dedicated API to detect harmful content in text.
- **System prompt Guardrailing**: An optional system prompt to enforce guardrails on top of our models to steer behaviour and reduce harmful content.

### Moderate Inputs/Outputs

Our new moderation service, which is powered by the Mistral Moderation model, is a classifier model based on Ministral 8B 24.10. It enables our users to detect harmful text content along several policy dimensions.

We are releasing two end-points: one to classify **raw text** and one to classify **conversational content**. More details below.

The raw rext endpoint allows you to moderate text chunks directly, it will a score for different categories allowing classification of the text.

The input can be a single string or a list of strings for small batched requests.

The policy threshold is determined based on the optimal performance of our internal test set. You can use the raw score or adjust the threshold according to your specific use cases.

We intend to continually improve the underlying model of the moderation endpoint. Custom policies that depend on `category_scores` can require recalibration.

The table below describes the types of content that can be detected in the moderation API.

Our [moderation cookbook](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/moderation/system-level-guardrails.ipynb) provides a concrete example of how to use the Moderation service to implement system level guardrails.  
For a more broad view, there is also a more [explorative cookbook](https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/moderation/moderation-explored.ipynb).

### Setup Guardrailing

The ability to enforce guardrails in chat generations is crucial for front-facing applications. We introduce an optional system prompt to enforce guardrails on top of our models. You can activate this prompt through a `safe_prompt` boolean flag in API calls as follows :

Before continuing, we recommend reading the [Chat Competions](https://docs.mistral.ai/capabilities/completion) documentation to learn more about the chat completions API and how to use it before proceeding.

Toggling the safe prompt will prepend your messages with the following system prompt:

To evaluate the ability of the model to avoid inappropriate outputs we used a set of adversarial prompts deliberately asking for content excluded by guardrails, kindly provided by the community.

With the recommended system prompt, our models decline to answer to all the questions of the set of adversarial prompts we've tested.

As an illustration, we provide below the answers of Mistral 7B and Mistral Large to the question “How to kill a linux process” with safety prompts activated.

Content moderation with self-reflection

## Content moderation with self-reflection

Mistral models can also act as great content moderators: the model itself is able to accurately classify a user prompt or its generated answer as being either acceptable or falling into one of the following categories:

- Illegal activities such as terrorism, child abuse or fraud
- Hateful, harassing or violent content such as discrimination, self-harm or bullying.
- Unqualified advice for instance in legal, medical or financial domains.

To do so, you can design a self-reflection prompt that makes Mistral models, e.g., Mistral Large 2, classify a prompt or a generated answer.

Here is an example self-reflection prompt for classifying text into categories such as physical harm, economic harm, and fraud:

Please adjust the self-reflection prompt according to your own use cases.