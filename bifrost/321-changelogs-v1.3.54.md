---
title: v1.3.54
url: https://docs.getbifrost.ai/changelogs/v1.3.54.md
source: llms
fetched_at: 2026-01-21T19:42:34.830352487-03:00
rendered_js: false
word_count: 200
summary: This document outlines the changes in Bifrost version 1.3.54, highlighting new document support for AI providers and header management features.
tags:
    - release-notes
    - changelog
    - bifrost
    - ai-providers
    - header-filtering
category: other
---

# v1.3.54

> v1.3.54 changelog - 2025-12-29

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.54
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.54
    docker run -p 8080:8080 maximhq/bifrost:v1.3.54
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.54">
  * feat: add document/file support for Anthropic, Bedrock, and Gemini
  * feat: adds support for allowlist and denylist in config for forward or block headers from forwarding it to providers
</Update>

<Update label="Core" description="1.2.43">
  * feat: add document/file support for Anthropic, Bedrock, and Gemini
  * feat: adds support for allow-list and deny-list for custom and built-in headers
</Update>

<Update label="Framework" description="1.1.53">
  * feat: adds support for HeaderFilterConfig in configstore
</Update>

<Update label="governance" description="1.3.54">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>

<Update label="jsonparser" description="1.3.54">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>

<Update label="logging" description="1.3.54">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>

<Update label="maxim" description="1.4.54">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>

<Update label="mocker" description="1.3.53">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>

<Update label="otel" description="1.0.53">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>

<Update label="semanticcache" description="1.3.53">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>

<Update label="telemetry" description="1.3.53">
  * chore: upgrade core to 1.2.43 and framework to 1.1.53
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt