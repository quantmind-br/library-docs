---
title: v1.3.45
url: https://docs.getbifrost.ai/changelogs/v1.3.45.md
source: llms
fetched_at: 2026-01-21T19:42:22.95338783-03:00
rendered_js: false
word_count: 199
summary: This document details the changelog for Bifrost version 1.3.45, providing information on new features, bug fixes, and component updates across the platform.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - bug-fixes
    - deployment
category: reference
---

# v1.3.45

> v1.3.45 changelog - 2025-12-11

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.45
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.45
    docker run -p 8080:8080 maximhq/bifrost:v1.3.45
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.45">
  * feat: complete config.json to config-store sync using hash
  * fix: structured output in bedrock, cohere and anthropic
  * fix: tool calls in bedrock chat completion
</Update>

<Update label="Core" description="1.2.36">
  * feat: complete config.json to config-store sync using hash
  * fix: structured output in bedrock, cohere and anthropic
  * fix: tool calls in bedrock chat completion
</Update>

<Update label="Framework" description="1.1.46">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="governance" description="1.3.47">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="jsonparser" description="1.3.47">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="logging" description="1.3.47">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="maxim" description="1.4.47">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="mocker" description="1.3.46">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="otel" description="1.0.46">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="semanticcache" description="1.3.46">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>

<Update label="telemetry" description="1.3.46">
  * chore: updating core to 1.2.36 and framework to 1.1.46
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt