---
title: v1.4.0-prerelease7
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease7.md
source: llms
fetched_at: 2026-01-21T19:43:02.218260261-03:00
rendered_js: false
word_count: 231
summary: This document outlines the changes in Bifrost v1.4.0-prerelease7, focusing on bug fixes for xAI provider integration, query parsing, and internal dependency updates.
tags:
    - release-notes
    - changelog
    - bifrost
    - xai-integration
    - bug-fixes
    - version-update
category: reference
---

# v1.4.0-prerelease7

> v1.4.0-prerelease7 changelog - 2026-01-08

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease7
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease7
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease7
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease7">
  * fix: correct query parameter parsing in transport interceptor middleware
  * fix: added custom error handling support for xAI provider
  * fix: strip unsupported parameters from xai request for reasoning models
  * fix: make the output field in BifrostResponsesResponse required by removing the omitempty tag.
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="Core" description="1.3.6">
  * fix: added custom error handling support for xAI provider
  * fix: strip unsupported parameters from xai request for reasoning models
  * fix: make the output field in BifrostResponsesResponse required by removing the omitempty tag.
</Update>

<Update label="Framework" description="1.2.6">
  * chore: upgrade core to v1.3.6
</Update>

<Update label="governance" description="1.4.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="jsonparser" description="1.4.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="logging" description="1.4.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="maxim" description="1.5.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="mocker" description="1.4.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="otel" description="1.1.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="semanticcache" description="1.4.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>

<Update label="telemetry" description="1.4.6">
  * chore: upgrade core to v1.3.6 and framework to 1.2.6
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt