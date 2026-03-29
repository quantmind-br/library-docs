---
title: v1.4.0-prerelease9
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease9.md
source: llms
fetched_at: 2026-01-21T19:43:05.643813453-03:00
rendered_js: false
word_count: 187
summary: This document outlines the changes in Bifrost version 1.4.0-prerelease9, focusing on fixes for streaming response timeouts and dependency updates across various internal modules.
tags:
    - release-notes
    - changelog
    - bifrost
    - bug-fix
    - streaming-responses
    - version-update
category: other
---

# v1.4.0-prerelease9

> v1.4.0-prerelease9 changelog - 2026-01-11

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease9
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease9
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease9
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease9">
  * fix: handles client disconnects and server timeouts gracefully for streaming responses
</Update>

<Update label="Core" description="1.3.8">
  * fix: adds timeout and connection disconnect handling for streaming responses
</Update>

<Update label="Framework" description="1.2.8">
  * chore: updated core version to 1.3.8
</Update>

<Update label="governance" description="1.4.9">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>

<Update label="jsonparser" description="1.4.8">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>

<Update label="logging" description="1.4.8">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>

<Update label="maxim" description="1.5.8">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>

<Update label="mocker" description="1.4.8">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>

<Update label="otel" description="1.1.8">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>

<Update label="semanticcache" description="1.4.8">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>

<Update label="telemetry" description="1.4.9">
  * chore: updated core version to 1.3.8 and framework version to 1.2.8
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt