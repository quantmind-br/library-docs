---
title: v1.3.39
url: https://docs.getbifrost.ai/changelogs/v1.3.39.md
source: llms
fetched_at: 2026-01-21T19:42:16.160191749-03:00
rendered_js: false
word_count: 268
summary: This document provides the release notes for Bifrost version 1.3.39, detailing improvements to streaming usage aggregation, API response updates, and bug fixes for model visibility.
tags:
    - changelog
    - release-notes
    - bifrost
    - streaming-fix
    - api-updates
    - version-history
category: reference
---

# v1.3.39

> v1.3.39 changelog - 2025-12-04

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.39
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.39
    docker run -p 8080:8080 maximhq/bifrost:v1.3.39
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.39">
  * fix: vertex and bedrock usage aggregation improvements for streaming
  * fix: choice index fixed to 0 for anthropic and bedrock streaming
  * feat: model field added to responses api response
  * feat: check allowed models and deployments of key for list models
  * bug: ui breaking when list models is empty on virtual key provider config
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="Core" description="1.2.33">
  * fix: vertex and bedrock usage aggregation improvements for streaming
  * fix: choice index fixed to 0 for anthropic and bedrock streaming
  * feat: model field added to responses api response
  * feat: check allowed models and deployments of key for list models
</Update>

<Update label="Framework" description="1.1.42">
  * chore: update core version to 1.2.33
</Update>

<Update label="governance" description="1.3.43">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="jsonparser" description="1.3.43">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="logging" description="1.3.43">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="maxim" description="1.4.42">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="mocker" description="1.3.42">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="otel" description="1.0.42">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="semanticcache" description="1.3.42">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>

<Update label="telemetry" description="1.3.42">
  * chore: update core version to 1.2.33 and framework version to 1.1.42
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt