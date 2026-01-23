---
title: v1.3.25
url: https://docs.getbifrost.ai/changelogs/v1.3.25.md
source: llms
fetched_at: 2026-01-21T19:41:58.992461668-03:00
rendered_js: false
word_count: 375
summary: This document provides the release notes for Bifrost version 1.3.25, detailing updates to the core engine, framework, and provider integrations such as Vertex AI and OpenRouter. Key features include unified streaming lifecycle events, pricing data in model lists, and enhanced authentication options.
tags:
    - changelog
    - release-notes
    - bifrost
    - vertex-ai
    - streaming-events
    - api-updates
category: other
---

# v1.3.25

> v1.3.25 changelog - 2025-11-14

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.25
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.25
    docker run -p 8080:8080 maximhq/bifrost:v1.3.25
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.25">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
  * feat: added unified streaming lifecycle events across all providers to fully align with OpenAI’s streaming response types.
  * chore: shift from `alpha/responses` to `v1/responses` in openrouter provider for responses API
  * feat: send back pricing data for models in list models response
  * fix: add support for keyless providers in list models request
  * feat: add support for custom fine-tuned models in vertex provider
  * feat: send deployment aliases in list models response for supported providers
  * feat: support for API Key auth in vertex provider
  * feat: support for system account in environment for vertex provider
</Update>

<Update label="Core" description="1.2.23">
  * feat: added unified streaming lifecycle events across all providers to fully align with OpenAI’s streaming response types.
  * chore: shift from `alpha/responses` to `v1/responses` in openrouter provider for responses API
  * fix: add support for keyless providers in list models request
  * feat: add support for custom fine-tuned models in vertex provider
  * fix: vertex provider list models now correctly returns the custom fine-tuned model ids in the response
  * feat: send deployment aliases in list models response for supported providers
  * feat: support for API Key auth in vertex provider
</Update>

<Update label="Framework" description="1.1.28">
  * chore: update core version to 1.2.23
  * feat: expose method to get pricing data for a model in model catalog
  * feat: add project number and deployments to vertex key config
</Update>

<Update label="governance" description="1.3.29">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>

<Update label="jsonparser" description="1.3.29">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>

<Update label="logging" description="1.3.29">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>

<Update label="maxim" description="1.4.28">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>

<Update label="mocker" description="1.3.28">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>

<Update label="otel" description="1.0.28">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>

<Update label="semanticcache" description="1.3.28">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>

<Update label="telemetry" description="1.3.28">
  * chore: update core version to 1.2.23 and framework version to 1.1.28
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt