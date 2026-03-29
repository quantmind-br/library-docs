---
title: v1.4.0-prerelease2
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease2.md
source: llms
fetched_at: 2026-01-21T19:42:56.459566334-03:00
rendered_js: false
word_count: 266
summary: This document provides release notes for Bifrost version 1.4.0-prerelease2, detailing bug fixes for AI model integrations, distributed tracing enhancements, and core dependency updates.
tags:
    - release-notes
    - bifrost
    - changelog
    - distributed-tracing
    - bug-fixes
    - version-update
category: reference
---

# v1.4.0-prerelease2

> v1.4.0-prerelease2 changelog - 2025-12-30

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease2
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease2
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease2
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease2">
  * fix: handling of nullable text fields in bedrock reasoning content
  * fix: gemini tool conversion with array parameters
  * fix: file name normalization in bedrock document blocks
  * fix: plugin status sync using configuration name
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
  * fix: adds parser for parent span id and root span parent to fix distributed tracing for datadog
</Update>

<Update label="Core" description="1.3.1">
  * fix: handling of nullable text fields in bedrock reasoning content
  * fix: gemini tool conversion with array parameters
  * fix: file name normalization in bedrock document blocks
  * fix: adds parser for parent span id and root span parent to fix distributed tracing for datadog
</Update>

<Update label="Framework" description="1.2.1">
  * fix: adds parser for parent span id and root span parent to fix distributed tracing for datadog
  * chore: upgrade core to 1.3.1
</Update>

<Update label="governance" description="1.4.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>

<Update label="jsonparser" description="1.4.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>

<Update label="logging" description="1.4.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>

<Update label="maxim" description="1.5.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>

<Update label="mocker" description="1.4.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>

<Update label="otel" description="1.1.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>

<Update label="semanticcache" description="1.4.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>

<Update label="telemetry" description="1.4.1">
  * chore: upgrade core to 1.3.1 and framework to 1.2.1
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt