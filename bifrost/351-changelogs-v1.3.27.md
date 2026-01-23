---
title: v1.3.27
url: https://docs.getbifrost.ai/changelogs/v1.3.27.md
source: llms
fetched_at: 2026-01-21T19:42:00.494026511-03:00
rendered_js: false
word_count: 182
summary: This document provides the release notes for Bifrost version 1.3.27, detailing fixes for Bedrock memory and streaming response parsing alongside dependency updates across various modules.
tags:
    - bifrost
    - changelog
    - release-notes
    - bedrock
    - bug-fixes
    - version-update
category: other
---

# v1.3.27

> v1.3.27 changelog - 2025-11-17

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.27
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.27
    docker run -p 8080:8080 maximhq/bifrost:v1.3.27
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.27">
  * fix: bedrock memory and streaming response parsing fixes
</Update>

<Update label="Core" description="1.2.25">
  * fix: bedrock memory and streaming response parsing fixes
</Update>

<Update label="Framework" description="1.1.30">
  * chore: update core version to 1.2.25
</Update>

<Update label="governance" description="1.3.31">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>

<Update label="jsonparser" description="1.3.31">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>

<Update label="logging" description="1.3.31">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>

<Update label="maxim" description="1.4.30">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>

<Update label="mocker" description="1.3.30">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>

<Update label="otel" description="1.0.30">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>

<Update label="semanticcache" description="1.3.30">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>

<Update label="telemetry" description="1.3.30">
  * chore: update core version to 1.2.25 and framework version to 1.1.30
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt