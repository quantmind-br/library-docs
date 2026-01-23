---
title: v1.3.44
url: https://docs.getbifrost.ai/changelogs/v1.3.44.md
source: llms
fetched_at: 2026-01-21T19:42:22.360094037-03:00
rendered_js: false
word_count: 149
summary: This document provides the release notes and changelog for Bifrost version 1.3.44, detailing new features like RBAC support and various bug fixes and dependency updates.
tags:
    - changelog
    - release-notes
    - rbac
    - bifrost
    - docker
    - deployment
    - version-update
category: reference
---

# v1.3.44

> v1.3.44 changelog - 2025-12-10

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.44
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.44
    docker run -p 8080:8080 maximhq/bifrost:v1.3.44
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.44">
  * feat: adds rbac support across all pages
  * fix: fixes config.json - config store streaming cases for virtual keys, providers and keys. Improved test coverage for this flow.
  * fix: adds support for text streaming logging
</Update>

<Update label="Framework" description="1.1.45">
  * fix: adds support for text streaming accumulation
</Update>

<Update label="governance" description="1.3.46">
  * chore: updates framework to 1.1.45
</Update>

<Update label="jsonparser" description="1.3.46">
  * chore: updates framework to 1.1.45
</Update>

<Update label="logging" description="1.3.46">
  * chore: updates framework to 1.1.45
</Update>

<Update label="maxim" description="1.4.46">
  * chore: updates framework to 1.1.45
</Update>

<Update label="mocker" description="1.3.45">
  * chore: updates framework to 1.1.45
</Update>

<Update label="otel" description="1.0.45">
  * chore: updates framework to 1.1.45
</Update>

<Update label="semanticcache" description="1.3.45">
  * chore: updates framework to 1.1.45
</Update>

<Update label="telemetry" description="1.3.45">
  * chore: updates framework to 1.1.45
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt