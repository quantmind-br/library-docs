---
title: v1.3.43
url: https://docs.getbifrost.ai/changelogs/v1.3.43.md
source: llms
fetched_at: 2026-01-21T19:42:22.255223739-03:00
rendered_js: false
word_count: 223
summary: This document outlines the updates and new features introduced in version 1.3.43 of Bifrost, including global proxy support, Datadog integration, and enterprise plugin handling.
tags:
    - release-notes
    - bifrost-updates
    - docker-deployment
    - proxy-support
    - datadog-integration
    - otel-plugin
category: other
---

# v1.3.43

> v1.3.43 changelog - 2025-12-09

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.43
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.43
    docker run -p 8080:8080 maximhq/bifrost:v1.3.43
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.43">
  * feat: adds global proxy support
  * feat: adds datadog native integration handling
  * feat: enterprise plugin handling for OSS
  * feat: adds support `OTEL_RESOURCE_ATTRIBUTES` for otel plugin
  * chore: some minor bug fixes
</Update>

<Update label="Core" description="1.2.35">
  * feat: added missing extrafields to errors in core
  * feat: adds global proxy support
  * feat: handle cached tokens in Anthropic streaming responses
  * fix: adds status field for responses API
</Update>

<Update label="Framework" description="1.1.44">
  * feat: adds global proxy support
  * feat: enterprise plugin handling
</Update>

<Update label="governance" description="1.3.45">
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>

<Update label="jsonparser" description="1.3.45">
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>

<Update label="logging" description="1.3.45">
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>

<Update label="maxim" description="1.4.45">
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>

<Update label="mocker" description="1.3.44">
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>

<Update label="otel" description="1.0.44">
  * feat: add custom CA TLS cert support for protocols
  * feat: enterprise plugin handling
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>

<Update label="semanticcache" description="1.3.44">
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>

<Update label="telemetry" description="1.3.44">
  * chore: updating core to 1.2.35 and framework to 1.1.44
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt