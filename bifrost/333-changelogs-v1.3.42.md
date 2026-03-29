---
title: v1.3.42
url: https://docs.getbifrost.ai/changelogs/v1.3.42.md
source: llms
fetched_at: 2026-01-21T19:42:21.518485905-03:00
rendered_js: false
word_count: 195
summary: This document provides the release notes for Bifrost version 1.3.42, detailing installation instructions via NPX and Docker along with bug fixes and dependency updates.
tags:
    - release-notes
    - changelog
    - bifrost
    - version-update
    - docker
    - npx
    - amazon-bedrock
category: other
---

# v1.3.42

> v1.3.42 changelog - 2025-12-05

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.42
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.42
    docker run -p 8080:8080 maximhq/bifrost:v1.3.42
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.42">
  * fix: added region prefix check for bedrock list models
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="Core" description="1.2.34">
  * fix: added region prefix check for bedrock list models
</Update>

<Update label="Framework" description="1.1.43">
  * chore: upgraded core version to 1.2.34
</Update>

<Update label="governance" description="1.3.44">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="jsonparser" description="1.3.44">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="logging" description="1.3.44">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="maxim" description="1.4.44">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="mocker" description="1.3.43">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="otel" description="1.0.43">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="semanticcache" description="1.3.43">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>

<Update label="telemetry" description="1.3.43">
  * chore: update core version to 1.2.34 and framework version to 1.1.43
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt