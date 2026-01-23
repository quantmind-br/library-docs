---
title: v1.3.26
url: https://docs.getbifrost.ai/changelogs/v1.3.26.md
source: llms
fetched_at: 2026-01-21T19:41:59.404878292-03:00
rendered_js: false
word_count: 190
summary: This document outlines the changes in version 1.3.26, featuring the addition of Elevenlabs provider support, security fixes for CORS settings, and various module dependency updates.
tags:
    - release-notes
    - changelog
    - elevenlabs-integration
    - bifrost-update
    - version-v1-3-26
    - deployment
category: other
---

# v1.3.26

> v1.3.26 changelog - 2025-11-16

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.26
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.26
    docker run -p 8080:8080 maximhq/bifrost:v1.3.26
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.26">
  * feat: adds support for elevenlabs provider
  * fix: fixes security settings form submission with empty cors domains.
  * chore: minor ui enhancements
</Update>

<Update label="Core" description="1.2.24">
  * feat: Added Elevenlabs provider
</Update>

<Update label="Framework" description="1.1.29">
  * chore: update core version to 1.2.24
</Update>

<Update label="governance" description="1.3.30">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>

<Update label="jsonparser" description="1.3.30">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>

<Update label="logging" description="1.3.30">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>

<Update label="maxim" description="1.4.29">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>

<Update label="mocker" description="1.3.29">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>

<Update label="otel" description="1.0.29">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>

<Update label="semanticcache" description="1.3.29">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>

<Update label="telemetry" description="1.3.29">
  * chore: update core version to 1.2.24 and framework version to 1.1.29
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt