---
title: v1.4.0-prerelease8
url: https://docs.getbifrost.ai/changelogs/v1.4.0-prerelease8.md
source: llms
fetched_at: 2026-01-21T19:43:03.314061059-03:00
rendered_js: false
word_count: 245
summary: This document details the updates and bug fixes for Bifrost version 1.4.0-prerelease8, including model enhancements for Vertex and Gemini and dependency updates across various modules.
tags:
    - release-notes
    - changelog
    - bifrost
    - vertex-ai
    - gemini
    - telemetry
    - version-update
category: other
---

# v1.4.0-prerelease8

> v1.4.0-prerelease8 changelog - 2026-01-09

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.4.0-prerelease8
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.4.0-prerelease8
    docker run -p 8080:8080 maximhq/bifrost:v1.4.0-prerelease8
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.4.0-prerelease8">
  * fix: vertex list models enhanced to support values from deployments
  * fix: header keys are now converted to lowercase for better consistency in plugin usage
  * fix: gemini system message conversion and added support for using instructions parameter as a fallback when no system message
</Update>

<Update label="Core" description="1.3.7">
  * fix: vertex list models enhanced to support values from deployments
  * fix: gemini system message conversion and added support for using instructions parameter as a fallback when no system message
</Update>

<Update label="Framework" description="1.2.7">
  * chore: updated core version to 1.3.7
</Update>

<Update label="governance" description="1.4.8">
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>

<Update label="jsonparser" description="1.4.7">
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>

<Update label="logging" description="1.4.7">
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>

<Update label="maxim" description="1.5.7">
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>

<Update label="mocker" description="1.4.7">
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>

<Update label="otel" description="1.1.7">
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>

<Update label="semanticcache" description="1.4.7">
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>

<Update label="telemetry" description="1.4.8">
  * feat: adds support for external Prometheus registry
  * chore: updated core version to 1.3.7 and framework version to 1.2.7
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt