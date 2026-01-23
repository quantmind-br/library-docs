---
title: v1.4.1
url: https://docs.getbifrost.ai/changelogs/v1.4.1.md
source: llms
fetched_at: 2026-01-21T19:43:07.461110878-03:00
rendered_js: false
word_count: 195
summary: This document details the updates and bug fixes for Bifrost version 1.4.1, primarily addressing streaming support for Bedrock structured output and associated component upgrades.
tags:
    - release-notes
    - changelog
    - bifrost
    - bedrock
    - structured-output
    - streaming
    - bug-fixes
category: other
---

# v1.4.1

> v1.4.1 changelog - 2026-01-19

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.1
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.1
    docker run -p 8080:8080 maximhq/bifrost:v1.4.1
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.1">
  * fix: fixes tool call-based structured output flow for Bedrock streaming requests (Chat and Responses API)
  * chore: updates test cases to assert content and tool\_calls validations
</Update>

<Update label="Core" description="1.3.11">
  * fix: fixes streaming support for bedrock structured output
</Update>

<Update label="Framework" description="1.2.12">
  * chore: upgrades core to 1.3.11
</Update>

<Update label="governance" description="1.4.13">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="jsonparser" description="1.4.12">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="litellmcompat" description="0.0.2">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="logging" description="1.4.12">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="maxim" description="1.5.11">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="mocker" description="1.4.12">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="otel" description="1.1.12">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="semanticcache" description="1.4.12">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>

<Update label="telemetry" description="1.4.13">
  * chore: upgrades core to 1.3.11 and framework to 1.2.12
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt