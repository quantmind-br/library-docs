---
title: v1.3.52
url: https://docs.getbifrost.ai/changelogs/v1.3.52.md
source: llms
fetched_at: 2026-01-21T19:42:33.29272382-03:00
rendered_js: false
word_count: 286
summary: This document provides the release notes for version 1.3.52 of Bifrost, detailing bug fixes, new model features for Anthropic and Gemini, and dependency updates across various modules.
tags:
    - release-notes
    - changelog
    - bifrost
    - gemini
    - anthropic
    - software-update
category: other
---

# v1.3.52

> v1.3.52 changelog - 2025-12-22

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.52
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.52
    docker run -p 8080:8080 maximhq/bifrost:v1.3.52
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.52">
  * fix: gemini thought signature handling in multi-turn conversations
  * feat: support computer-use-2025-11-24 in anthropic for claude-opus-4-5
  * refactor: use gemini native embedding endpoint for gemini embeddings
  * refactor: for fine-tuned or custom models in vertex use gemini native endpoint instead of openai compatible chat completions endpoint
  * fix: append bedrock and cohere routes in langchain and litellm integration
  * fix: handle dynamic thinking budget (-1) in gemini and other providers
</Update>

<Update label="Core" description="1.2.41">
  * fix: gemini thought signature handling in multi-turn conversations
  * feat: support computer-use-2025-11-24 in anthropic for claude-opus-4-5
  * refactor: use gemini native embedding endpoint for gemini embeddings
  * refactor: for fine-tuned or custom models in vertex use gemini native endpoint instead of openai compatible chat completions endpoint
  * fix: handle dynamic thinking budget (-1) in gemini and other providers
</Update>

<Update label="Framework" description="1.1.51">
  * chore: upgraded version of core to 1.2.41
</Update>

<Update label="governance" description="1.3.52">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>

<Update label="jsonparser" description="1.3.52">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>

<Update label="logging" description="1.3.52">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>

<Update label="maxim" description="1.4.52">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>

<Update label="mocker" description="1.3.51">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>

<Update label="otel" description="1.0.51">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>

<Update label="semanticcache" description="1.3.51">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>

<Update label="telemetry" description="1.3.51">
  * chore: upgraded versions of core to 1.2.41 and framework to 1.1.51
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt