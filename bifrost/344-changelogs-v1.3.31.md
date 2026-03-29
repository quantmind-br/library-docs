---
title: v1.3.31
url: https://docs.getbifrost.ai/changelogs/v1.3.31.md
source: llms
fetched_at: 2026-01-21T19:42:06.491138573-03:00
rendered_js: false
word_count: 169
summary: This document outlines the release notes and update details for Bifrost version 1.3.31, including installation methods and module-specific bug fixes.
tags:
    - changelog
    - release-notes
    - bifrost
    - version-update
    - bug-fixes
    - docker
    - npx
category: other
---

# v1.3.31

> v1.3.31 changelog - 2025-11-19

<Tabs>
  <Tab title="NPX">
    ```bash  theme={null}
    npx -y @maximhq/bifrost --transport-version v1.3.31
    ```
  </Tab>

  <Tab title="Docker">
    ```bash  theme={null}
    docker pull maximhq/bifrost:v1.3.31
    docker run -p 8080:8080 maximhq/bifrost:v1.3.31
    ```
  </Tab>
</Tabs>

<Update label="Bifrost(HTTP)" description="1.3.31">
  fix: integration fixes for fallbacks
</Update>

<Update label="Core" description="1.2.27">
  fix: integration convertor fixes for fallbacks
</Update>

<Update label="Framework" description="1.1.34">
  chore: update core version to 1.2.27
</Update>

<Update label="governance" description="1.3.35">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>

<Update label="jsonparser" description="1.3.35">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>

<Update label="logging" description="1.3.35">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>

<Update label="maxim" description="1.4.34">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>

<Update label="mocker" description="1.3.34">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>

<Update label="otel" description="1.0.34">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>

<Update label="semanticcache" description="1.3.34">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>

<Update label="telemetry" description="1.3.34">
  chore: update core version to 1.2.27 to framework version 1.1.34
</Update>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.getbifrost.ai/llms.txt