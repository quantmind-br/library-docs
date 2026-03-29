---
title: v1.3.22
url: https://docs.getbifrost.ai/changelogs/v1.3.22.md
source: llms
fetched_at: 2026-01-21T19:41:53.497802758-03:00
rendered_js: false
word_count: 167
summary: This document provides the release notes for Bifrost version 1.3.22, detailing new features, breaking changes, and module updates across the platform.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - software-maintenance
category: reference
---

# v1.3.22

> v1.3.22 changelog - 2025-11-09

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.22
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.22
    docker run -p 8080:8080 maximhq/bifrost:v1.3.22
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.22">
  * feat: Adds option to disable authentication on inference calls
  * chore: Adds dark image for new version infographic
</Update>

<Update label="Core" description="v1.3.22">
  * feat: add numberOfRetries, fallbackIndex and selected key name to context
    \[BREAKING] changed BifrostContextKeySelectedKey to BifrostContextKeySelectedKeyID
  * feat: send model deployment back in response extra fields
  * feat: add headers to MCP client config
</Update>

<Update label="Framework" description="v1.3.22">
  * Adds DisableAuthOnInference to AuthConfig
</Update>

<Update label="governance" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>

<Update label="jsonparser" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>

<Update label="logging" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>

<Update label="maxim" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>

<Update label="mocker" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>

<Update label="otel" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>

<Update label="semanticcache" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>

<Update label="telemetry" description="v1.3.22">
  * chore: version update framework to 1.1.25
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt