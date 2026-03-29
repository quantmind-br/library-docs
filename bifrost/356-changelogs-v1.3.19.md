---
title: v1.3.19
url: https://docs.getbifrost.ai/changelogs/v1.3.19.md
source: llms
fetched_at: 2026-01-21T19:41:48.43523629-03:00
rendered_js: false
word_count: 320
summary: This document provides the release notes for Bifrost version v1.3.19, detailing new features in telemetry metrics, logging enhancements, and updates to the core framework components.
tags:
    - changelog
    - release-notes
    - bifrost
    - telemetry
    - logging
    - mcp-client
    - version-update
category: reference
---

# v1.3.19

> v1.3.19 changelog

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.19
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.19
    docker run -p 8080:8080 maximhq/bifrost:v1.3.19
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
  * chore: allowed changing name when updating a virtual key
  * feat: add numberOfRetries, fallbackIndex and selected key name and id to context to telemetry metrics
  * feat: add used virtual key name and id to telemetry metrics
  * feat: send model deployment back in response extra fields
  * feat: add selected key and virtual key to logs filter
  * feat: add headers to MCP client config
  * feat: add `is_success` label to upstream latency metrics
</Update>

<Update label="Core" description="v1.3.19">
  * feat: add numberOfRetries, fallbackIndex and selected key name to context
    \[BREAKING] changed BifrostContextKeySelectedKey to BifrostContextKeySelectedKeyID
  * feat: send model deployment back in response extra fields
  * feat: add headers to MCP client config
</Update>

<Update label="Framework" description="v1.3.19">
  * chore: Upgrades core to 1.2.20
  * feat: add selected key and virtual key to logs table
  * feat: add headers to MCP client config
</Update>

<Update label="governance" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
</Update>

<Update label="jsonparser" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
</Update>

<Update label="logging" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
  * feat: add selected key and virtual key to logs
</Update>

<Update label="maxim" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
</Update>

<Update label="mocker" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
</Update>

<Update label="otel" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
</Update>

<Update label="semanticcache" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
</Update>

<Update label="telemetry" description="v1.3.19">
  * chore: version update core to 1.2.20 and framework to 1.1.24
  * feat: add numberOfRetries, fallbackIndex and selected key name and id to context to telemetry metrics
  * feat: add used virtual key name and id to telemetry metrics
  * feat: add `is_success` label to upstream latency metrics
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt